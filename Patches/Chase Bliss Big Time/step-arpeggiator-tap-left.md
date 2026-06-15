---
type: patch
title: Step Arpeggiator (tap LEFT to walk the scale)
device: Chase Bliss Big Time
date: 2026-06-15
description: "The PERFORMED version of the Thermae cascade — STEP MODE turns the LEFT footswitch into a sequencer step button so single banjo plucks become a hand-driven arpeggio, walking up a quantized Oct+4+5 ladder one composed step per tap. Deliberately distinct from the auto-cascade sheets (banjo-thermae-cascade-lead, bouncy-thermae) where the repeats step themselves: here STEP MODE is the whole point. Designed from the Mark Johnston deep-dive + harp-lady transcript."
tags: [pitched, sequenced, step-mode, performed, melodic, banjo, thermae, arpeggiator, designed, signature]
hidden:
  STEP MODE: "ON (Options → enable; the LEFT footswitch becomes a step button — each tap advances pitch one rung up the SCALE)"
  SCALE IGNORE: "optional ON (smooth sine modulation + scaled transposition without the chaos)"
  MISO: "auto-engages off IN-L (mono-in / stereo-out) so the stepped arpeggio opens to the full stereo field"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27; recall by PC (flying faders fly to it on recall)" }
  - { name: "MODE", type: switch, value: "Short (snappy, defined steps)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (keeps stepped repeats articulate, no runaway)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi or Focus (clean pitch)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Oct+4+5 (the octave/4th/5th ladder the steps climb)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Square (Thermae-style pitch jumps)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~40% (modest — keep stepped pitches clean, not smeared)" }
  - { name: "TIME", type: knob, value: "mid (step legato / decay length)" }
  - { name: "CLUSTER", type: knob, value: "low-mid (let the core stepped voice read clearly)" }
  - { name: "TILT EQ", type: knob, value: "noon → up (keep bright banjo transients defined)" }
  - { name: "FEEDBACK", type: knob, value: "~45–55% (how long each rung sustains before you tap the next; higher = the previous rung stacks under the new one)" }
  - { name: "WET", type: knob, value: "~45%" }
  - { name: "RATE", type: knob, value: "moderate (alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "LEFT footswitch", type: button, value: "STEP — with STEP MODE on, each tap advances pitch one step up the SCALE (the primary performance move)" }
---

# Step Arpeggiator (tap LEFT to walk the scale)

## Concept
Big Time's STEP MODE turns the LEFT footswitch into a sequencer step button. With **SCALE = Oct+4+5** and **MOTION = Square**, every tap transposes the whole cascade one rung up a quantized octave/4th/5th ladder, so single banjo plucks become a PERFORMED arpeggio — you decide when the pitch climbs, in time with the phrase. This is deliberately distinct from the auto-cascade patches (**banjo-thermae-cascade-lead**, **bouncy-thermae**) where the repeats step themselves on a clock or via feedback: here STEP MODE is the whole point, not a footnote variant. Big Time auto-engages MISO (mono-in/stereo-out) off IN-L. NOTE: knob/fader numerics below are DESIGNED DIALABLE STARTING POINTS, not published artist values — flying faders override them on recall.

## How to play it
1. Recall the slot (PC); enable **STEP MODE** in Options so the LEFT footswitch becomes a step button.
2. Set **SCALE = Oct+4+5** and **MOTION = Square** — this is the ladder the taps climb.
3. Feed single banjo plucks (GK-5 → VG-800, high SUSTAIN so each note rings long enough to survive a tap or two).
4. Tap the **LEFT footswitch** to walk the pitch up one rung per tap, in time with the phrase, so the climb is composed rather than random.
5. Set **FEEDBACK ~45–55%** so the previous rung sustains underneath while you step to the next for a building stack.
6. Keep **COLOR** modest (~40%) and **TILT EQ** at noon → up so the stepped pitches stay clean and the banjo transients read.
7. Optional **SCALE IGNORE ON** for smoother pitch ramps with less chaos.
8. To reset to the bottom of the ladder, stop tapping and let the cascade settle, or recall the slot.

## Notes
- This is the PERFORMED counterpart to **banjo-thermae-cascade-lead** / **bouncy-thermae**: STEP MODE primary (foot-driven), not a clock/feedback auto-cascade. The whole distinction is keeping the step on your foot.
- No clock needed — the LEFT footswitch drives the steps by hand instead of CC54 subdivision. For a hands-free grid-locked auto-step version, turn STEP MODE off and slave to clock (see **bouncy-thermae** pitch-sequenced banjo lead direction).
- **Honesty flag:** numeric knob/fader values are DESIGNED STARTING POINTS, NOT published artist settings — flying faders override on recall. Dial by ear. The control surface (switch positions, hidden SCALE IGNORE / STEP MODE) is verified against the existing Big Time patch sheets and GearProfile; the VALUES are designed.
- Source banjo needs high VG-800 SUSTAIN: too short and the note dies before the next step lands, breaking the arpeggio.

## Sources
- 🟣 designed (DOUG) from `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (STEP MODE → LEFT footswitch steps pitch through SCALE; SCALE / MOTION / SCALE IGNORE behavior).
- `centerpiece-harp-lady-emily-hopkins-big-time-as-instrument` transcript ("more mature Thermae").
- Existing Big Time cascade patches (`banjo-thermae-cascade-lead.md`, `bouncy-thermae.md`) document STEP MODE as a variant — this patch promotes it to the PRIMARY mechanism; MISO + CC27 slot-save conventions from those sheets.
- Big Time numeric values are designed dialable starting points, not published artist settings.
