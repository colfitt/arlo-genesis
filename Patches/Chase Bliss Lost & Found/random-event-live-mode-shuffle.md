---
type: patch
title: Random Event (Live Mode-Shuffle)
device: Chase Bliss Lost & Found
date: 2026-06-14
description: DOUG-designed — the rig's "Random" tag in action; constantly-shifting mode combos drawn live from the Digitakt/Deluge (CC112/113/114) for a controlled-chaos texture event feeding the Microcosm, with a frozen version saved to recall on cue.
tags: [random, controlled-chaos, midi, performance, texture, designed, signature]
dips:
  SPREAD: on
  TRAILS: on
  UNSYNC: off
hidden:
  GLUE: "10:00–11:00"
  "Control-bank BOUNCE (alt approach)": "armed across L MODIFY + R MODIFY for hands-free knob churn; MIX(RAMP) sets speed"
controls:
  - { name: "ROUTING", type: switch, value: "L+R parallel", options: ["L>R", "L+R", "L<R"] }
  - { name: "Both slots modes", type: switch, value: "on-aesthetic pair (e.g. Grain Tumbler + Spectral Modulator, or Gen Lite + Sympathetic Resonator)" }
  - { name: "BLEND", type: knob, value: "noon" }
  - { name: "MIX (RAMP)", type: knob, value: "noon–1:00" }
  - { name: "CC112 (Random L Mode)", type: button, value: "draw MIDI ramps/triggers in Digitakt/Deluge automation" }
  - { name: "CC113 (Random R Mode)", type: button, value: "draw MIDI ramps/triggers in Digitakt/Deluge automation" }
  - { name: "CC114 (Random Both Modes)", type: button, value: "draw MIDI ramps/triggers in Digitakt/Deluge automation" }
  - { name: "6A Ensemble HOLD = RANDOM", type: button, value: "smooth, non-cyclical movement instead of an LFO" }
  - { name: "Save as preset (PC)", type: button, value: "so a fixed scene can also be recalled" }
  - { name: "Slot/Bank", type: knob, value: "Preset L or R (recall a frozen version on cue)" }
---

# Random Event (Live Mode-Shuffle)

## Concept
The patch that earns the rig's "Random" tag — constantly-shifting mode/variant combos drawn live from the Digitakt or Deluge, a controlled-chaos texture event feeding the Microcosm. Load both channels with on-aesthetic modes, run `L+R` parallel, then drive the pedal's Random-mode CCs from the controller so it keeps jumping to new combinations. The randomness is recallable / clock-synced — controlled chaos, not noise — and a frozen version can be saved to recall on cue.

## How to play it
1. Load BOTH channels with on-aesthetic modes (e.g. Grain Tumbler + Spectral Modulator, or Gen Lite + Sympathetic Resonator).
2. Set ROUTING `L+R` parallel, BLEND ~noon, MIX ~noon–1:00.
3. **Drive from the controller:** CC112 = Random L Mode, CC113 = Random R Mode, CC114 = Random Both Modes — draw MIDI ramps/triggers in the Digitakt's CC automation (or the Deluge automation view) so the pedal jumps to new mode/variant combos.
4. **Alternatively** arm BOUNCE across L MODIFY + R MODIFY (Control-bank dips) for hands-free knob churn; MIX (RAMP) sets speed.
5. **6A Ensemble HOLD = RANDOM** gives smooth, non-cyclical movement instead of an LFO.
6. **SAVE as a preset (PC)** so a fixed scene can also be recalled on cue.

## Notes
- **DESIGNED, not found** — Bay Mud demonstrates the technique in a no-talking jam; exact CC ramp values are not spoken (they're the standard L+F CCs per the MIDI manual).
- This is the patch that earns the rig's "Random" tag.
- The randomness is recallable / clock-synced — controlled chaos, not noise.

## Sources
- Bay Mud "Randomizing Effects with MIDI" (Deluge automation view drawing MIDI ramps to L+F CCs) — `research/transcripts/baymud-randomizing-midi-deluge.md`
- CC112/113/114 Random L/R/Both from the L+F MIDI manual + dossier §4 — `research/Lost-and-Found-DeepResearch.md`
- Ensemble HOLD = RANDOM from BachelorMachinesTV Pt2 + community-tips — `research/transcripts/bachelormachinestv-science-part2.md`, `research/links/community-tips-gotchas-firmware.md`
- cb-stack clock/preset-recall files (Blooper folder)
- Ref: Bay Mud "Randomizing Effects with MIDI — Lost + Found & Deluge Jam" (technique; CC values are the standard L+F CCs)
- Transformed from Pedalxly Lost-and-Found-Patches.md (designed)
