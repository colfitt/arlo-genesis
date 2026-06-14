https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_LogicARA_InsertVorbereitungen?env=logic

celemony.com help (+ Apple Support ARA2 guide + Logic Pro Help/Gearspace threads) · ARA2 in Logic Pro · accessed 2026-06-11

How Melodyne runs in **Logic Pro (the user's primary, AU-only host)** — and why ARA2 is the mode you want.

## Three ways Melodyne runs
1. **Standalone app** — drag audio in, edit, bounce out. No DAW needed. Good for prepping a one-off sample.
2. **Conventional plugin insert** — you must **Transfer** (record) the audio into the plugin before editing; the edit lives inside that plugin instance on that region.
3. **ARA2 (Audio Random Access)** — Logic and Melodyne share the audio + timeline in real time. **No transfer/record step.** This is the modern, preferred mode in Logic.

## Inserting Melodyne as ARA in Logic
- Select the track. Insert **"Melodyne (ARA)"** into the **first Audio Effect slot** (it must be first / in the first slot for edits to travel with the region).
- **Press Play** in Logic to kick off Logic↔Melodyne communication — shortly after, the track's contents appear in Melodyne and you can start editing the blobs.
- **Multiple tracks at once**: select several channel strips in the Logic mixer, insert "Melodyne (ARA)" on one of them → Logic opens **one Melodyne window per selected track**, each filling with its track's audio on Play.

## Why ARA2 wins (vs plugin mode)
- **No capture step** — you don't have to record audio into the plugin first.
- **Edits are preserved when you move or copy the region** to another track — *as long as Melodyne was inserted in ARA mode in the first slot*.
- Apple has supported ARA2 in Logic since **10.4** (the first DAW feature to use ARA2). Melodyne is the flagship ARA partner.

## Logic specifics / gotchas
- Logic is **AU-only** — use the **Audio Units** Melodyne, and specifically the **"Melodyne (ARA)"** entry, not the plain insert.
- Logic also has **Flex Pitch** built in (its own free note-level tuner). Reach for Flex Pitch for quick monophonic touch-ups; reach for Melodyne when you need DNA polyphonic, better-sounding stretch, formants, scale tools, or audio-to-MIDI.
- Bounce/flatten when you're done if you want to free the analysis and lock the edit.
