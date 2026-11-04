"""Rebuild letzspeak/index.html (trainer) and letzspeak/record/index.html (recorder).
Run from anywhere:  python3 letzspeak/_src/build.py
Edit vocab in deck.py (never change an existing id), UI in body.html / rec_body.html."""
import json, os, sys
SRC = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(SRC)
sys.path.insert(0, SRC); import deck as D
rd = lambda f: open(os.path.join(SRC, f), encoding="utf8").read()
deck = D.deck(); mods = {str(k): list(v) for k, v in D.MODULES.items()}
man_p = os.path.join(ROOT, "audio", "manifest.json")
man = json.load(open(man_p, encoding="utf8")) if os.path.exists(man_p) else {}
live = {i: v["lb"] for i, v in man.items() if os.path.exists(os.path.join(ROOT, "audio", i + ".mp3"))}
cur = {c["id"]: c["lb"] for c in deck}
audio = {i: 1 for i, lb in live.items() if cur.get(i) == lb}
stale = sorted(i for i, lb in live.items() if i in cur and cur[i] != lb)
head = rd("head.html").replace("<title>Margots Kaarten</title>", '<title>Lëtz Speak Vocab</title>\n<meta name="description" content="Lëtzebuergesch fir Ufänker · luxembourgeois pour débutants · Luxembourgish for beginners">\n<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 3 3%22%3E%3Crect width=%223%22 height=%221%22 fill=%22%23C8323A%22/%3E%3Crect y=%221%22 width=%223%22 height=%221%22 fill=%22%23fff%22/%3E%3Crect y=%222%22 width=%223%22 height=%221%22 fill=%22%234AA3DF%22/%3E%3C/svg%3E">')
J = lambda o: json.dumps(o, ensure_ascii=False)
def sub(t): return t.replace("__MODULES__", J(mods)).replace("__DECK__", J(deck)).replace("__AUDIO__", J(audio))
open(os.path.join(ROOT, "index.html"), "w", encoding="utf8").write(head + sub(rd("body.html")))
open(os.path.join(ROOT, "record", "index.html"), "w", encoding="utf8").write(head.replace("<title>Lëtz Speak Vocab</title>", "<title>Lëtz Speak · Recorder</title>") + rd("rec_body.html").replace("__MODULES__", J(mods)).replace("__DECK__", J(deck)).replace("__AUDIO__", J(live)))
print(f"built: {len(deck)} items, {len(audio)} with audio, {len(deck)-len(audio)} without" + (f", STALE (spelling changed, re-record): {stale}" if stale else ""))
