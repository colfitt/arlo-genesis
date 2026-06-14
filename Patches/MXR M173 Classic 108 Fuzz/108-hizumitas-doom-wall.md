---
type: patch
title: 108 → Hizumitas DOOM WALL
device: MXR M173 Classic 108 Fuzz
date: 2026-06-14
description: The marquee rig texture — the 108 supplies splat/grind/level, the Hizumitas smooths it into a sustained wall and supplies the EQ the 108 lacks; gapless food for the Microcosm / Dark Star / H90.
tags: [fuzz, doom, wall, rig-signature, designed, signature]
controls:
  - { name: "OUTPUT/VOLUME", type: knob, value: "12:00 (to unity)" }
  - { name: "FUZZ/INPUT", type: knob, value: "12:00–2:00" }
  - { name: "BUFFER", type: switch, value: "ON", options: ["ON", "OFF"] }
---

# 108 → Hizumitas DOOM WALL

## Concept
The marquee rig texture. The 108 supplies splat/grind/level, then the Hizumitas smooths it into a sustained wall and supplies the EQ the 108 lacks. The result is gapless food for the Microcosm / Dark Star / H90 downstream. 108→Muff is the **unconventional** order (a Muff usually goes first) and is the reason the 108 earns its slot.

## How to play it
1. **108:** OUTPUT/VOLUME 12 o'clock (to unity), FUZZ/INPUT 12–2 o'clock, BUFFER ON.
2. **Then Hizumitas:** Volume max, Sustain max, Tone full CW (bass side), long verb/delay downstream.
3. *Live move:* park the Hizumitas Sustain at noon and sweep its Tone through the decay.

## Notes
- The canonical 108 chain is "fuzz → light drive → Muff" (SixStringSensei) — insert the **CB Brothers AM** (or a low-gain drive) between the 108 and Hizumitas to push the fuzz, mask its gate, and make it sustain *longer*.
- **Order-swap fix** if the 108 sounds thin even with buffer ON: Hizumitas → 108 (the Muff's low output Z drives the FF cleanly).
- Inferred — verify by ear. Nobody documents a 108 into a Hizumitas.

## Sources
- Designed from `research/108-Fuzz-UsageGuide.md` §5–6 + `108-Fuzz-DeepResearch.md` §5, §13 + `research/links/stack-gilmourish-bigmuff-stacking.md` + `research/links/stack-sixstringsensei-108-chain.md`
- Transformed from Pedalxly 108-Fuzz-Patches.md (designed)
