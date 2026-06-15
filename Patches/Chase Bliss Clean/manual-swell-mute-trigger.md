---
type: patch
title: "Manual Swell — Footswitch Mute & Trigger"
device: Chase Bliss Clean
date: 2026-06-15
description: "Flip the SWELL AUX dip and the AUX footswitch stops being the play-triggered Dynamic Swell and becomes a manual swell trigger — tap for a single (tempo-synced) swell, or hold to mute and release to swell back up to full. A hands-on volume-swell gesture for deliberate violined entrances, distinct from the auto-triggered Dynamic Swell. From the Clean manual (Swell pp.30-31, Customize SWELL AUX p.35)."
tags: [swell, volume-swell, manual, tempo-sync, ambient, performance, factory]
dips:
  Dusty: off
  Swell Aux: "on (manual trigger — AUX becomes a manual swell instead of Dynamic Swell)"
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: "off (momentary) — ON for a toggle"
  Spread: off
  MISO: off
hidden:
  Swell In time (Wet knob): "dial to taste (100 ms-4 s) — no single published value beyond the range"
  Swell Out time (Dry knob): "dial to taste (100 ms-4 s) — no single published value beyond the range"
controls:
  - { name: "SWELL AUX dip", type: switch, value: "ON — turns the AUX footswitch into a Manual Swell trigger", options: ["off (Dynamic Swell)", "on (Manual Swell)"] }
  - { name: "AUX footswitch", type: button, value: "tap = one swell / hold = mute, release = swell up to full (momentary)" }
  - { name: "Latch", type: switch, value: "off (momentary) — ON to make AUX a toggle", options: ["off momentary", "on toggle"] }
  - { name: "Wet", type: knob, value: "main page level — repurposed as Swell In time (100 ms-4 s) on hidden page" }
  - { name: "Dry", type: knob, value: "main page level — repurposed as Swell Out time (100 ms-4 s) on hidden page" }
  - { name: "Sensitivity", type: knob, value: "to taste underneath (does not gate the manual trigger)" }
  - { name: "EQ", type: knob, value: "to taste underneath" }
  - { name: "Dynamics", type: knob, value: "to taste underneath" }
  - { name: "External footswitch (MIDI/TRS jack)", type: button, value: "normally-open footswitch can trigger AUX remotely" }
---

# Manual Swell — Footswitch Mute & Trigger

## Concept
With the SWELL AUX dip flipped ON, the AUX footswitch stops behaving as the play-triggered Dynamic Swell and becomes a hands-on manual swell trigger. Tap it for a single (tempo-synced) swell, or hold it to mute the signal and release to swell back up to full. This is a deliberate, footswitch-driven volined entrance — you decide exactly when each swell happens, rather than letting your playing cross the Sensitivity threshold. The swell-in and swell-out shapes still live in the Hidden Options (Wet = Swell In, Dry = Swell Out, ~100 ms–4 s each). It's the performance-oriented sibling of the Dynamic Volume Swell patch, and like that one it can feed pre-swelled material into the granular/loop boards downstream.

## How to play it
1. **Flip the SWELL AUX dip ON** — the AUX footswitch is now a Manual Swell trigger instead of Dynamic Swell.
2. **Hidden Options** (hold both footswitches until LEDs go green): set Wet = Swell In time and Dry = Swell Out time to taste (100 ms–4 s each).
3. **TAP the AUX footswitch** for a single swell, or **HOLD** to mute and **release** to swell back up to full.
4. Use the hold-mute-release move for deliberate violined entrances. Pipe a normally-open external footswitch into the MIDI/TRS jack to trigger AUX remotely (hands free).

## Notes
- **No published knob values:** the Swell In/Out times are a dialable recipe within the documented 100 ms–4 s range — there's no single published setting, so dial Wet/Dry to taste against the LEDs.
- The manual frames the single tap as enabling "precise, tempo-synced swells," but clock-sync at the CC level is **CC-UNCONFIRMED** — don't assume it locks to the Digitakt grid.
- **Distinct from the play-triggered Dynamic Volume Swell:** here YOU trigger every swell by foot, rather than the signal crossing the Sensitivity threshold.
- Sensitivity, EQ, and Dynamics still color the tone underneath, but the manual trigger is the gesture — they don't gate it.

## Sources
- `research/transcripts/chase-bliss-clean-official-video-manual.md` (Manual Swell via SWELL AUX dip: "holding mutes, releasing swells back to full; single tap = one swell")
- `research/links/cb-manual-clean-compression-recipes.md` (Manual Swell, manual pp.30–31)
- Chase Bliss Clean official manual (Swell pp.30–31, Customize SWELL AUX p.35, External Control p.39)
- Dynamic Volume Swell (Patch 12) — Wet = Swell In, Dry = Swell Out
- Transformed from Pedalxly Clean-Patches.md (factory)
