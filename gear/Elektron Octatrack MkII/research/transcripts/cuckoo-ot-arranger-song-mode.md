https://www.youtube.com/watch?v=TnE4rUa46SE
True Cuckoo · Octatrack Arranger Tutorial - how to structure a song · 2016-05-29

The **Arranger** = the OT's song mode: a row-by-row list of patterns with per-row repeat count, scene A/B, MIDI transpose, tempo, and mute info — so the box plays a whole structured set hands-free. Pitched at performers (singers/guitarists) whose hands or attention are elsewhere on stage.

## Build patterns first (and slice everything)
- New project: `[FUNC]` + `PROJECT` → CHANGE → CREATE EMPTY PROJECT → "arranger".
- Load a sliced drum loop into track 1 (slot list → AUDIO → `[FUNC]` + `YES` to audition). Set project tempo to match the sample (130 BPM) so it stretches cleanly.
- **Key philosophy (slice, don't drop long samples):** A pre-sliced file carries a companion slice file of the same name, so a loaded sample is instantly playable as slices (turn SLICES on in PLAYBACK; set keyboard to SLICE mode with `[FUNC]` + up/down). Sequencing *slices* (vs one long sample on a single trig) lets you keep retrig, reverse, and tempo-lock — drop a long sample on one trig and you get one shot with no further control and it drifts off time. He builds intro / loop / variation / solo patterns this way, including a reversed slice (#17 reverse) for the intro.
- Layer a vocal "hey hey" track (track 2, sliced) and a solo track (track 4, 13 slices) the same way. Slices stay in tempo even when slowed or retriggered because each trig fires a slice.

## Opening the Arranger
- `[FUNC]` + `ARRANGER` (same key as PATTERN, red label). A small window shows `0000 ... END OF ARRANGEMENT`.
- An LED indicates arranger mode on/off. **Context-sensitive `[FUNC]` + `[BANK]`/EDIT:**
  - NOT in arranger mode → per-track pattern settings.
  - In arranger mode → the arranger window (rename / save the whole arrangement).
- With arranger active, press EDIT to enter the big arranger editor. "Arrangement is empty — press `[FUNC]` + down to insert row."

## Arranger rows
Each row holds, left to right:
- **PATTERN** (the pattern to play).
- **Repetition** — how long to stay; not limited to whole pages — any odd number of steps to jump early/late off the grid.
- **Scene A** and **Scene B** — preloaded per row so you don't hand-select scenes mid-song.
- **T** = MIDI transpose.
- **B** = tempo (set it on row 1 so the song always loads at the right tempo).
- **M** = mute (per row; lets you mute/unmute audio + MIDI tracks for arrangement variations — the interface shows red = MIDI tracks, orange = audio tracks).

`[FUNC]` + down inserts a row; select pattern per row (he builds 1, 2, 3, 2, 3). Press play to audition. Press STOP while stopped to rewind to the top. (Sometimes needs a second press to register a row as the entry point.)

## Navigating + editing live
- Press `NO` to exit edit → out in the list view you see all rows; move the arrow up/down and press `YES` to jump straight into that row's pattern (useful for tweaking just that section, e.g. making the "hey hey" track appear less often via mutes + repeat = 4).

## Driving scenes from the arrangement
- Convention: **Scene A = clean** (no changes) on every row; **Scene B changes per row**.
- He pre-builds scenes, then assigns them per row so they're armed automatically:
  - **Scene 2** (vocal track 2, **RATE = -64**) — slows/reverses the voice's playback.
  - **Scene 3** (solo track 4, **pitch shift up** + send to delay with more feedback/shorter/stereo + a **Lo-Fi** second FX) — a rising pitch-bend freakout for the solo.
  - **Scene 4** (track 1 playback **backwards/reverse** + dark reverb + Lo-Fi destruction on other tracks) — the "freak out" section; he also tries baking a retrig in but finds it too much.
- In the editor, set Scene A = scene 1 throughout, Scene B = 2 / 3 / 4 / 3 across the rows. Now the scenes are armed automatically as the song advances; he still has to manually select which track he's *playing* for live jamming over the top.

## Saving + the 8-arrangement limit
- Arranger window → RENAME → name it ("awesome") → SAVE → confirm `YES` → "Arrangement saved."
- CHANGE lists all arrangements for the project — **8 slots / 8 arrangements** max. One arrangement per song for a gig; for a longer set, chain via an empty/pause pattern in the middle (you'll see e.g. "B1" as the new song's start point in the list).
- Then `[FUNC]` + `PROJECT` → SAVE → `YES`.

## Rig relevance
For a doom/drone set this is the unattended backbone: lay out drone/wall patterns as rows, arm a clean Scene A vs a destroyed Scene B (reverse + Lo-Fi + dark reverb — exactly this rig's aesthetic) per section, set per-row mutes and tempo, and let the OT walk the structure while both hands stay on the banjo/baritone. The "slice everything, never drop a long static sample on one trig" rule is the difference between a re-sequenceable performance and a static backing track.
