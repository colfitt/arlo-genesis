https://www.youtube.com/watch?v=ScHbHOfAQVk

Alex Emrich | Audio Edges · "How To Use Melodyne | FULL BEGINNER GUIDE | Everything You Need To Know" · 2023-01-31 · 23:21

(Tool-by-tool walkthrough. Demoed in Pro Tools but the workflow is DAW-agnostic. Distilled from auto-subs.)

---

## Getting audio in
- Put **Melodyne first in the chain**, above any other processing. Melodyne **records (transfers) the original audio** into the plugin — anything before it is ignored, anything after it is "post" the tuned version.
- **Transfer the old way**: hit **Transfer**, play the audio, it records into the plugin. A faster trick in a non-ARA DAW: arm Transfer, then **freeze the track** (the audio transfers near-instantly), then unfreeze.
- **In a DAW with ARA / Audio Random Access**, the DAW exchanges info with Melodyne in real time and you skip the transfer/record step entirely.
- After transfer, if it detects in the wrong format, set **Algorithm → "Melodic" (standard)** to separate the pitches.

## Reading the display
- The **thin red line** through each blob = the **pitch** of the note.
- The **size/height of the yellow blob** = the **volume** of the note.
- You can visually see if a note is sharp/flat by where the red line sits relative to the centre of the lane.

## Navigation (fastest methods)
- **Scroll** up/down to move vertically; **hold Shift + scroll** to move left/right. A mouse/trackball beats a trackpad here.
- **Hold opt-cmd** to summon the **Zoom tool** at any moment (click-drag to zoom).
- **Hold Ctrl + click** to pop the tool picker and hover-select a tool on the fly (much faster than the top toolbar).
- **Double-click in front of a note** to start playback from there (works on any tool).

## The tools, one by one
- **Main tool** — click/select notes (single or multi).
- **Pitch tool** — **hold Opt** and drag a note up/down in pitch. **Double-click** a note to snap it to the centre of the nearest lane (perfects intonation). Trick: select a group with the Main tool, switch to Pitch, double-click → snaps the whole group to grid. Watch that low/high notes don't snap to the wrong lane.
  - **Pitch Modulation tool** (sub-tool) — controls/flattens **vibrato**. Overdo it → autotune sound. Click-drag down to reduce. `Restore Original` undoes it on a selection.
  - **Pitch Drift tool** (sub-tool) — fixes a note that **falls flat (or drifts) over its duration**; click-drag to level it out while keeping the vibrato/movement. (Presenter's most-used tool.)
- **Formant tool** — used when you've moved a note far from where it was naturally sung and it sounds fake. Click-drag the formant to find a more natural place by ear; can be pushed drastically for an artificial/creative effect.
- **Amplitude tool** — volume per note (bigger blob = louder); shows dB change. Handy for taming a note that came in hot, or catching missed clip-gain.
- **Time tool** — **hold Opt**, drag the start of a note to move/retime it; double-click to audition. Make sure the DAW tempo matches the song so the grid lines up. Best for tightening, not drastic sustains (artifacts).
- **Note Separation tool** — **double-click** to split a blob Melodyne didn't separate (e.g. a fast run or a scoop). Lets you edit/snap each part independently.

## Bonus tips
- **Don't tune breaths** — breaths have no red pitch line, just a small blob; learn to recognise and leave them.
- Separate a swooping/scooping note (an attack that slides up) at the point where it lands, then snap the landing note only.
