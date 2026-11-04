# Lëtz Speak Vocab — sources
- `deck.py` — modules + vocab (lb/fr/en/note). **Never change an existing id** (student progress + audio are keyed by it).
- `body.html` — trainer UI/engine template · `rec_body.html` — recorder template · `head.html` — shared CSS.
- `build.py` — writes `../index.html` (trainer) and `../record/index.html` (Jim's recorder).
- `process_audio.py <zip>` — imports a recorder export → `../audio/<id>.mp3` + `manifest.json`, then rebuilds.
A clip only shows in the trainer while its recorded spelling matches the deck; after a spelling fix it shows as ⚠ in the recorder.

## Update rules — never break students' progress
Progress lives in each student's browser (localStorage key `letzspeak-vocab-v1`), keyed by word **id** and module **number**.
- Fix spellings/glosses freely; **never rename an id**. Moving a word to another module is fine.
- Only **append** modules (11, 12…); never renumber or delete one.
- Removing a word: delete the line and add its id to `RETIRED` in deck.py.
- `published.json` is the append-only registry of every id ever published; `build.py` refuses to build if a rule is broken.
- The loader never wipes saved data: unknown/old formats are upgraded in place (`upgrade()` in body.html).
- Adding words to a finished module makes it "not complete" again, but unlocked modules stay unlocked.
