# Lëtz Speak Vocab — sources
- `deck.py` — modules + vocab (lb/fr/en/note). **Never change an existing id** (student progress + audio are keyed by it).
- `body.html` — trainer UI/engine template · `rec_body.html` — recorder template · `head.html` — shared CSS.
- `build.py` — writes `../index.html` (trainer) and `../record/index.html` (Jim's recorder).
- `process_audio.py <zip>` — imports a recorder export → `../audio/<id>.mp3` + `manifest.json`, then rebuilds.
A clip only shows in the trainer while its recorded spelling matches the deck; after a spelling fix it shows as ⚠ in the recorder.
