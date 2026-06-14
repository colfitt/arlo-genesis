---
type: patch
title: Banjo Bowed-Pipe Doom Drone
device: Chase Bliss Lost & Found
date: 2026-06-14
description: DOUG-designed — banjo plinks resonate forever into a glassy bowed-pipe drone (Sympathetic Resonator), frozen via PITCH FREEZE as a sustained doom wall haloed by reverb; the rig's banjo-as-lead-into-drone signature move (post-punk/Swans-style sustained drone wall).
tags: [drone, doom, ambient, post-punk, banjo-as-lead, designed, signature]
dips:
  TRAILS: on
  SPREAD: on
  LATCH: on
hidden:
  GLUE: "10:00 (light)"
  ALT (R octave): "−1, then sweep the octave during the ring for expression"
  ALT (L diffusion): "3:00"
controls:
  - { name: "ROUTING", type: switch, value: "L<R series (Right into Left)", options: ["L>R", "L+R", "L<R"] }
  - { name: "R slot mode", type: switch, value: "5B Sympathetic Resonator" }
  - { name: "L slot mode", type: switch, value: "1B Useful Ambience (halo)" }
  - { name: "MODIFY (R feedback)", type: knob, value: "4:00–5:00 (MAXED — resonates forever)" }
  - { name: "TIME (R onset)", type: knob, value: "noon" }
  - { name: "MODIFY (L feedback)", type: knob, value: "1:00" }
  - { name: "TIME (L size)", type: knob, value: "2:00 (large)" }
  - { name: "BLEND", type: knob, value: "2:00 (toward the reverb / 2nd-effect mix in series)" }
  - { name: "MIX (RAMP)", type: knob, value: "2:00–3:00" }
  - { name: "FREEZE (HOLD R footswitch)", type: button, value: "PITCH FREEZE — locks the drone" }
  - { name: "Slot/Bank", type: knob, value: "Preset bank 2 (BANK dip)" }
---

# Banjo Bowed-Pipe Doom Drone

## Concept
Banjo plinks feed the Sympathetic Resonator (R slot, 5B) with feedback maxed so it resonates forever into a glassy/vibraphone bowed-pipe drone. Holding the R footswitch hits PITCH FREEZE to lock the drone as a sustained doom wall. The drone then runs `L<R` (Right into Left) into Useful Ambience (1B) as an internal reverb halo. This is the rig's banjo-as-lead-into-drone signature move — a Swans-style sustained drone wall.

## How to play it
1. Set ROUTING to `L<R` (Right slot feeds Left).
2. Play sustained banjo notes/chords into the Resonator — feedback MAXED makes them resonate forever.
3. **HOLD the R footswitch = PITCH FREEZE** to lock the drone into a sustained wall.
4. Sweep the ALT octave (start at −1) **during the ring** for expression — octave only does something when swept mid-ring.
5. The Useful Ambience halo (L slot) blooms over the top; BLEND ~2:00 toward the reverb sets its mix in the series chain.

## Notes
- **DESIGNED, not found** — no owner published this exact recipe.
- Onset (TIME on the Resonator) is barely audible on shipping units — leave it ~noon.
- ALT octave only does something when swept during the ring (not a static setting).
- TRAILS on so the frozen pad survives bypass; LATCH on so the FREEZE hold latches.
- Don't stack against the Microcosm / Dark Star / Etherealizer reverb downstream — that's why the halo is kept internal here. Feeds the Microcosm a moving, sustained texture.

## Sources
- Sympathetic Resonator shipping map + "feedback max = resonates forever" + PITCH FREEZE hold — `research/transcripts/bachelormachinestv-science-part2.md`
- Knobs "forgiving note-gated drone source" — `research/transcripts/cb-lost-found-walkthrough-knobs.md`
- Dossier Starting-point (b) "Bowed drone" L<R into Useful Ambience halo — `research/Lost-and-Found-DeepResearch.md` §13(b)
- Taste lens post-punk/doom cluster — `Research/Taste-Profile/taste-profile.md`
- Ref: Taste cluster — post-punk/experimental (Swans-style sustained drone wall); banjo-as-lead aesthetic
- Transformed from Pedalxly Lost-and-Found-Patches.md (designed)
