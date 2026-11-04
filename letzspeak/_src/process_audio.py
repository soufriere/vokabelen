"""Import a recorder export zip:  python3 -I letzspeak/_src/process_audio.py /path/to/letzspeak-audio-*.zip
Trims leading/trailing silence, loudness-normalises, writes mono MP3 to letzspeak/audio/<id>.mp3,
merges audio/manifest.json, then rebuilds. Unzips into a fresh temp dir (untrusted input)."""
import json, os, re, subprocess, sys, tempfile, zipfile
SRC = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(SRC); OUT = os.path.join(ROOT, "audio")
sys.path.insert(0, SRC); import deck as D
ids = {c["id"]: c for c in D.deck()}
os.makedirs(OUT, exist_ok=True)
man_p = os.path.join(OUT, "manifest.json"); man = json.load(open(man_p)) if os.path.exists(man_p) else {}
tmp = tempfile.mkdtemp(prefix="lsaudio_")
with zipfile.ZipFile(sys.argv[1]) as z:
    inc = json.loads(z.read("manifest.json"))
    for i, (cid, meta) in enumerate(sorted(inc.items()), 1):
        if not re.fullmatch(r"[a-z0-9-]+", cid) or cid not in ids:
            print(f"skip unknown id {cid!r}"); continue
        src = os.path.join(tmp, cid + os.path.splitext(meta["file"])[1])
        open(src, "wb").write(z.read(meta["file"]))
        dst = os.path.join(OUT, cid + ".mp3")
        af = ("highpass=f=70,silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.08,"
              "areverse,silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.12,areverse,"
              "loudnorm=I=-16:TP=-1.5:LRA=11,adelay=120:all=1,apad=pad_dur=0.15")
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af", af, "-ac", "1", "-ar", "44100",
                            "-c:a", "libmp3lame", "-b:a", "64k", dst], capture_output=True, text=True)
        if r.returncode: print(f"FAIL {cid}: {r.stderr.strip()[:200]}"); continue
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", dst], capture_output=True, text=True).stdout or 0)
        warn = " ⚠ very short — check" if dur < 0.45 else (" ⚠ long — check" if dur > 6 else "")
        warn += "" if meta["lb"] == ids[cid]["lb"] else f" ⚠ recorded as {meta['lb']!r}, deck now {ids[cid]['lb']!r}"
        man[cid] = {"lb": meta["lb"], "t": meta.get("t")}
        print(f"[{i}/{len(inc)}] {cid:22s} {dur:4.1f}s{warn}")
json.dump(man, open(man_p, "w"), ensure_ascii=False, indent=1, sort_keys=True)
subprocess.run([sys.executable, "-I", os.path.join(SRC, "build.py")])
