---
type: patch
title: Thru → Neighbor ×3 — 8-FX Serial Rack
device: Elektron Octatrack MkII
date: 2026-06-14
description: Stacking up to 8 serial FX on the incoming pedalboard signal by chaining a Thru head into three Neighbor tracks.
tags: [live-fx, neighbor-chain, thru-machine, serial-fx, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 1 · T1 Thru + T2/T3/T4 Neighbor" }
  - { name: "MIXER DIR AB", type: knob, value: "0 (input only via Thru)" }
  - { name: "Track 1 machine", type: switch, value: "Thru, INAB = A B + FX1+FX2 (e.g. filter → Lo-Fi)", options: ["Thru", "Flex", "Neighbor"] }
  - { name: "Track 2 machine", type: switch, value: "Neighbor (listens to T1 output) + 2 FX (e.g. comb → chorus)" }
  - { name: "Track 3 machine", type: switch, value: "Neighbor (listens to T2 output) + 2 FX (e.g. phaser → reverb)" }
  - { name: "Track 4 machine", type: switch, value: "Neighbor (listens to T3 output) + 2 FX (e.g. EQ → Dark Reverb)" }
  - { name: "Track 1 trig", type: button, value: "one trig on step 1; [PLAY]" }
  - { name: "Neighbor routing", type: switch, value: "MAIN (series); CUE = parallel/phasing", options: ["MAIN", "CUE"] }
  - { name: "Mute", type: button, value: "mute the last Neighbor (track 4) to silence the whole chain" }
---

# Thru → Neighbor ×3 — 8-FX Serial Rack

## Concept
The way to exceed the 2-FX-per-track limit on a single source: chain a Thru head into three Neighbor tracks, each adding two more FX, for up to **8 serial FX** on the live pedalboard wall. Neighbor tracks listen to the output of the preceding track, so the signal flows T1 → T2 → T3 → T4 as an 8-deep serial rack.

## How to play it
1. MIXER **DIR AB = 0** (input only via Thru); confirm `<REC>` LEDs show signal.
2. **Track 1 = Thru, INAB = A B**, FX1+FX2 (e.g. filter → Lo-Fi). Place one trig on step 1; [PLAY].
3. **Track 2/3/4 = Neighbor** (each listens to the OUTPUT of the preceding track; CANNOT be on track 1 or 5 = chain heads).
4. Assign 2 FX to each of tracks 2/3/4 (e.g. comb → chorus, then phaser → reverb, then EQ → Dark Reverb) = **8-deep serial rack**.
5. Neighbor is **series when routed to MAIN, parallel/phasing when routed to CUE** — route intermediate stages to MAIN.
6. **Muting:** tracks preceding the last Neighbor can't be muted individually — mute the **last Neighbor (track 4)** to silence the whole chain.

## Notes
- **Autopilot variant:** put a Flex with recorder buffer 1 on track 1 instead of Thru, drop recorder + sample trigs with per-step pitch/FX/LFO p-locks → continuous capture-and-destroy under the live guitar.
- The way to exceed the 2-FX-per-track limit on a single source.
- FX choices are **designed** suggestions — dial to taste.

## Sources
- designed from links/int-ot-effects-processor-neighbor-chain.md (Manual §17.5 p111, Appendix A.4 Neighbor p120)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)
