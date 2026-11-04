"""Import a recorder export zip:  python3 -I letzspeak/_src/process_audio.py /path/to/letzspeak-audio-*.zip
Trims leading/trailing silence, loudness-normalises, writes mono MP3 to letzspeak/audio/<id>.mp3,
merges audio/manifest.json, then rebuilds. Unzips into a fresh temp dir (untrusted input)."""
import json, os, re, subprocess, sys, tempfile, zipfile
import numpy as np

def speech_bounds(path, sr=16000):
    """Adaptive trim: frame RMS in dB, threshold relative to this clip's own noise floor and peak (works for quiet recordings)."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768
    fl = sr // 50  # 20 ms frames
    n = len(x) // fl
    if n < 5: return 0.0, len(x) / sr, len(x) / sr
    db = 20 * np.log10(np.sqrt((x[:n * fl].reshape(n, fl) ** 2).mean(1)) + 1e-9)
    noise, peak = np.percentile(db, 10), db.max()
    thr = noise + max(6.0, 0.22 * (peak - noise))
    on = np.where(db > thr)[0]
    if not len(on): return 0.0, len(x) / sr, len(x) / sr
    s = max(0.0, on[0] * 0.02 - 0.15); e = min(len(x) / sr, (on[-1] + 1) * 0.02 + 0.25)
    return s, e, len(x) / sr

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
        s, e, rawdur = speech_bounds(src)
        af = (f"atrim=start={s:.3f}:end={e:.3f},asetpts=PTS-STARTPTS,highpass=f=70,"
              "loudnorm=I=-16:TP=-1.5:LRA=11,adelay=80:all=1,apad=pad_dur=0.1")
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af", af, "-ac", "1", "-ar", "44100",
                            "-c:a", "libmp3lame", "-b:a", "64k", dst], capture_output=True, text=True)
        if r.returncode: print(f"FAIL {cid}: {r.stderr.strip()[:200]}"); continue
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", dst], capture_output=True, text=True).stdout or 0)
        warn = " ⚠ very short — check" if dur < 0.45 else (" ⚠ long — check" if dur > 6 else "")
        warn += "" if meta["lb"] == ids[cid]["lb"] else f" ⚠ recorded as {meta['lb']!r}, deck now {ids[cid]['lb']!r}"
        man[cid] = {"lb": meta["lb"], "t": meta.get("t")}
        print(f"[{i}/{len(inc)}] {cid:22s} raw {rawdur:4.1f}s -> {dur:4.1f}s{warn}")
json.dump(man, open(man_p, "w"), ensure_ascii=False, indent=1, sort_keys=True)
subprocess.run([sys.executable, "-I", os.path.join(SRC, "build.py")])
