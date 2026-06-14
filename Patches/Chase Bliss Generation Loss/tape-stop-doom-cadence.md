---
type: patch
title: Tape-Stop Doom Cadence
device: Chase Bliss Generation Loss
date: 2026-06-14
description: Ending a sustained drone with a rubbery tape-halt that the downstream Big Time catches and smears into a dying repeat — the doom song-end move.
tags: [drone, doom, tape-stop, cadence, designed, signature]
hidden:
  Aux Onset (Wow knob): ~CCW-ish (slowish-but-not-instant fade)
controls:
  - { name: "Aux", type: switch, value: "Stop", options: ["Stop", "Filter", "Fail"] }
  - { name: "Wow", type: knob, value: "1–2:00 (from #3 Dying Cassette)" }
  - { name: "Flutter", type: knob, value: "12:00 (from #3)" }
  - { name: "Volume", type: knob, value: "noon (from #3)" }
  - { name: "Saturate", type: knob, value: "11:00 (from #3)" }
  - { name: "Failure", type: knob, value: "9:00 (from #3)" }
  - { name: "Model", type: knob, value: "Model 5 (Portamax-HT, from #3)" }
  - { name: "Dry", type: switch, value: "None (whole wet voice halts)", options: ["None", "Small", "Unity"] }
  - { name: "Left footswitch (Aux)", type: button, value: "tap = latching stop, hold = momentary" }
---

# Tape-Stop Doom Cadence

## Concept
End a sustained drone with a rubbery tape-halt that the downstream Big Time catches and smears into a dying repeat — the doom song-end move. Built on the Dying Cassette base, with the Aux footswitch reassigned to **Stop**. Dry **None** so the whole wet voice halts together.

## How to play it
1. Start from **Dying Cassette / Seasick Wow-Flutter** (patch #3).
2. Set the **Aux toggle = Stop**.
3. Set the hidden **Aux Onset** (the Wow knob in the hidden menu) ~CCW-ish for a slowish-but-not-instant fade.
4. **Tap** the left footswitch for a latching stop, **hold** for momentary.
5. Big Time on long FEEDBACK catches the slowdown and smears it into the dying repeat.

## Notes
- 🟣 designed — combines the manual's Aux-Stop behavior with the rig's degrade-then-delay logic; the hidden Aux Onset value is approximate intent.
- An external normally-open momentary on the MIDI/aux jack fires it hands-free (no MIDI needed).
- Store as an onboard preset with Aux=Stop saved.

## Sources
- 🟣 designed from `research/links/genloss-aux-freeze-classic-trick.md` + UsageGuide §5 + `research/transcripts/kevwyxin-read-the-manual-part1-basics.md`.
- Transformed from Pedalxly Generation-Loss-Patches.md (designed).
