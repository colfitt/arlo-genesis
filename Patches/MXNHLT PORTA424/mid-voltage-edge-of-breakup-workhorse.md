---
type: patch
title: Mid-Voltage Edge-of-Breakup Workhorse
device: MXNHLT PORTA424
date: 2026-06-14
description: All-purpose middle setting living right at the edge of breakup — warmer than the clean default, not as gone as the wall; the go-to for obvious-but-controlled cassette grit on a sustained part from any source.
tags: [dynamic-saturation, edge-of-breakup, workhorse, designed, signature]
controls:
  - { name: "Input Trim", type: knob, value: "12–1 o'clock (the gate — noon-up progressively clips)" }
  - { name: "Treble", type: knob, value: "11 o'clock" }
  - { name: "Bass", type: knob, value: "12–1 o'clock" }
  - { name: "Channel Fader", type: knob, value: "~80%" }
  - { name: "Master Volume", type: knob, value: "unity-ish (into JHS 424)" }
  - { name: "Voltage", type: switch, value: "18V (drop to 9V to pull breakup earlier)", options: ["9V", "18V"] }
  - { name: "Placement", type: switch, value: "end of chain", options: ["front of chain", "end of chain"] }
---

# Mid-Voltage Edge-of-Breakup Workhorse

## Concept
An all-purpose middle setting living right at the edge of breakup — warmer than the clean default but not as gone as the ruined wall. The go-to for obvious-but-controlled cassette grit on a sustained part, from any source. Fills the gap between the subtle-warmth default and the ruined-wall extreme.

## How to play it
1. Set Input Trim to 12–1 o'clock — noon is the documented inflection point where audible grit begins.
2. Treble 11, Bass 12–1.
3. Channel Fader ~80%, Master unity-ish into the JHS 424.
4. Run 18V for a firmer clean-warm range before breakup; drop to 9V to pull the breakup point earlier.
5. Mono-sum the bus; place at the end of chain.

## Notes
- Trim at noon is the documented inflection point where audible grit begins.
- 18V gives a firmer pre-breakup range; 9V pulls breakup earlier.
- All clock/fader/voltage values are designed-to-spec from the Trim-as-gate behavioral mapping.

## Sources
- Designed from the Trim-as-gate behavioral mapping (`PORTA424-DeepResearch.md` §4: "below ~9–10 o'clock clean-with-warmth; from noon up it progressively clips") + the 18V/9V headroom split (`research/links/staging-mono-print-tips.md`).
- Transformed from Pedalxly PORTA424-Patches.md (DOUG-designed)
