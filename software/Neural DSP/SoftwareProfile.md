---
name: Neural DSP
brand: Neural DSP
category: software
subcategory: bundle
formats: [vst3, au, aax]
host_in: [logic, ableton]
installed: true
version: latest
status: owned
tags: []
related: []
---

# Neural DSP

**Summary** — Boutique amp/cab-sim plugins, each a full rig in a window (amp + pre/post FX +
cab/IR + onboard reverb & delay). Installed: **Archetype: John Mayer X**, **Archetype: Nolly
X**, **Parallax X** (bass). "X" = the new platform (resizable UI, Transpose, Doubler, Live
Tuner, Quad Cortex compat). Deep usage → `research/Neural-DSP-Archetype-UsageGuide.md`.

## Why I have it
The software amp/FX option where I want a *specific* modelled amp + its onboard ambient FX,
revisable at mix (vs the committed hardware Iridium DI, vs Guitar Rig 7's modular rack).
**John Mayer X** = lush ambient/shoegaze cleans + swells (Gravity Tank → Dream Delay →
Studio Verb). **Nolly X** = doom/sludge low-gain walls + big ambient washes on the baritone,
with a rare *pre-amp delay* and a transpose-down-a-fifth = instant baritone.

## Signature uses
- **Ambient-clean wall (JM X):** single-amp clean → Gravity Tank (harmonic trem + spring) →
  Dream Delay (ping-pong, long) → Studio Verb Hall; volume-swell the Output in.
- **Doom/sludge baritone wall (Nolly X):** Rhythm (5150) / low-gain Lead (Kraken), loose
  gain, Mesa B30 or Zilla V30 cab, fuzz in front, 9-band EQ tighten.
- **Shoegaze chaos (Nolly X):** the PRE-delay fed into Overdrive 1 + a dirty amp — repeats
  stack into the gain (a post delay can't).
- **Baritone/banjo:** Transpose −5th ≈ convincing baritone; Doubler = one-pass width; banjo
  through Nolly Clean (Shiva) + Room Send + long reverb.
- **Reamp/send:** audition amps non-destructively on DI banjo/synth/baritone at mix.

## Notes
- **CPU-heavy** → freeze in Logic; or run the **standalone app + print the wet** to dodge
  insert latency (and reamp DI at mix).
- **No effect reordering** in any Neural plugin (fixed chain) — do distortion-last walls in
  Logic/Guitar Rig instead.
- **JM X 3-amp blend locks the cab** — drop to a single amp to edit cab/mics/Room Send.
- Both load **custom/3rd-party IRs** (cab block → Load Custom IR) and can **unlink amp↔cab**.
- Onboard reverbs are one (good) washed-out Hall flavour — pair Valhalla/ChromaVerb for a
  different colour. Global input → peak −14 to −9 dB; Cmd-drag = fine; right-click = MIDI Learn.
- Community skews metal/djent — the ambient/doom relevance here is by technique, not artist
  precedent.
