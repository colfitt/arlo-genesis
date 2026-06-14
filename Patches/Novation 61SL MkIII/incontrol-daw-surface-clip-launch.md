---
type: patch
title: InControl DAW Surface + Clip Launch (Ableton/Logic)
device: Novation 61SL MkIII
date: 2026-06-14
description: Serve the DAW — transport, track select/arm, faders→volume, encoders→device params, and (Ableton only) clip launch on the pad grid + device banking; the "SL serves Logic/Ableton" world.
tags: [incontrol, daw-surface, ableton, logic, drivenbymoss, community]
controls:
  - { name: "World/Mode", type: switch, value: "InControl (Shift+InControl) — host port 'SL MkIII InControl / Port 2'", options: ["Standalone", "InControl"] }
  - { name: "Ableton features", type: knob, value: "Clip launch (pad grid mirrors clip colors), device banking, track names, metronome" }
  - { name: "Logic features", type: knob, value: "Device control + Smart Controls + count-in (NO Save, NO clip launch)" }
  - { name: "Control surface script", type: switch, value: "DrivenByMoss (free) — upgrades the weak stock HUI", options: ["Stock HUI", "DrivenByMoss"] }
  - { name: "Knob modes (DrivenByMoss)", type: switch, value: "Track / Vol / Pan / Send (color-coded)", options: ["Track", "Vol", "Pan", "Send"] }
  - { name: "Transport (DrivenByMoss)", type: button, value: "Real ⏪/⏩ (stock HUI breaks FF/RW in Reaper)" }
  - { name: "Faders", type: knob, value: "→ track volume (not motorized/touch — values JUMP; Fader Pickup BYPASSED in InControl)" }
  - { name: "Slot/Bank", type: knob, value: "InControl mode (not a Session) — set DrivenByMoss as the control surface in the DAW" }
---

# InControl DAW Surface + Clip Launch (Ableton/Logic)

## Concept
Serving the DAW: transport, track select/arm, faders→volume, encoders→device params, and (Ableton only) clip launch on the pad grid + device banking. This is the "SL serves Logic/Ableton" world — the alternative to the standalone-brain Sessions. It is a HARD toggle from the sequencer world; pick one transport per song. DrivenByMoss is the community-standard fix for the weak stock HUI.

## How to play it
1. WORLD = InControl (Shift+InControl) — host port "SL MkIII InControl / Port 2".
2. ABLETON (most capable): clip launch (pad grid mirrors clip colors), device banking, track names, metronome.
3. LOGIC: device control + Smart Controls + count-in, but NO Save and NO clip launch.
4. UPGRADE the weak stock HUI with DrivenByMoss (free): color-coded knob modes (Track/Vol/Pan/Send), real ⏪/⏩ transport (stock HUI breaks FF/RW in Reaper), faders→track volume — enable via the InControl button, set the 2nd InControl port as primary.

## Notes
- Documented DAW-surface workflow.
- Mutually exclusive transport with the standalone-sequencer patches — this is the "other world."
- CAVEATS: Automap is GONE (no deep per-plugin auto-map — use the DAW script's device banking, or a standard-MIDI template + plugin MIDI-learn, or DrivenByMoss); faders aren't motorized/touch-sensitive so values JUMP and Fader Pickup is BYPASSED in InControl; no MPE.
- DrivenByMoss is the community-standard fix for the stock HUI.

## Sources
- research/links/incontrol-overview-hui.md + incontrol-ableton-setup.md + incontrol-logic-reason-setup.md + forum-drivenbymoss-slmkiii-doc.md + forum-reaper-transport-bug-drivenbymoss.md + gearspace-automap-removed-plugin-control.md + transcripts/gammalens-incontrol-ableton.md + UsageGuide §5.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (community)
