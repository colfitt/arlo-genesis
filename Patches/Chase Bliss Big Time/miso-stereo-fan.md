---
type: patch
title: MISO Stereo Fan
device: Chase Bliss Big Time
date: 2026-06-15
description: "MXR 108 → (Hizumitas wall) mono fuzz → Big Time IN-L only — the splitter-free MISO trick that fans one mono cable into a wide stereo delay FIELD. The 108-fuzz STEREO-FAN sibling the Hizumitas Fuzz Wall patch's own note points at (Saturated + higher CLUSTER), distinct from that patch's endless self-oscillating drone."
tags: [stereo, miso, fuzz, width, multi-tap, shoegaze, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot (CC27). On recall the motorized faders fly to the saved values and override any live knob positions below." }
  - { name: "Chain / Input", type: switch, value: "Mono fuzz (108 → Hizumitas wall) → IN-L ONLY → auto-MISO (mono-in / stereo-out). No external splitter.", options: ["mono → IN-L (MISO)", "full stereo in", "mono in/out"] }
  - { name: "MODE", type: switch, value: "Short (keeps it a delay FIELD, not a drone)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Saturated (the 108-fuzz variant — spitty, slightly-gated stabs stay articulate as the taps multiply them)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Focus (shaves highs+lows over time → the muff wall stays defined across the image)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off (or Sine subtle for gentle drift)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "LOW ~25–35% (fuzz already supplies all the saturation; too much COLOR + a hot fuzz clamps the analog limiter to porridge)" }
  - { name: "TIME", type: knob, value: "medium-short" }
  - { name: "CLUSTER", type: knob, value: "~50–60% (the multi-tap fan — scatters each mono stab into a stereo pattern; CLUSTER itself also generates stereo image)" }
  - { name: "TILT EQ", type: knob, value: "above noon (cut muff low mud so the width reads)" }
  - { name: "FEEDBACK", type: knob, value: "~35–40% (the field overlaps without runaway)" }
  - { name: "WET", type: knob, value: "~40%" }
  - { name: "SPREAD", type: button, value: "OFF = subtle widening (the gentle widen — NOT ping-pong). A cohesive wide bed, not hard-panned bouncing echoes.", options: ["off (subtle widening)", "on (ping-pong)"] }
  - { name: "DRY KILL", type: switch, value: "ON (Options menu) — print a clean wet stereo field without a centered mono dry note pinning the image" }
  - { name: "TEXTURE", type: knob, value: "low (alt — comp/aliasing amount)" }
  - { name: "DIFFUSE", type: knob, value: "low-mid (alt under FEEDBACK)" }
---

# MISO Stereo Fan

## Concept
Feed Big Time's IN-L ONLY from a mono fuzz (here a 108→Hizumitas wall) to auto-engage MISO (mono-in / stereo-out). CLUSTER fans the mono stab into a scattered stereo multi-tap pattern and SPREAD widen makes it a cohesive wide field rather than a hard L/R ping-pong. Short MODE keeps it a delay FIELD, not an infinite drone. Saturated STATE is the 108-fuzz variant — the spitty, slightly-gated stabs stay articulate as the taps multiply them. COLOR stays low because the fuzz already supplies all the saturation; too much COLOR + a hot fuzz clamps the analog limiter to porridge. The whole value is width and movement from a single mono source with no external splitter.

## How to play it
1. Run the mono fuzz (108 → Hizumitas wall) into Big Time **IN-L ONLY** — a single mono cable auto-engages **MISO** (mono-in/stereo-out).
2. Confirm MISO: you should hear the mono source open into a stereo field.
3. Keep COLOR low (~25–35%) — the fuzz supplies the saturation; STATE **Saturated** keeps the spitty stabs articulate.
4. Set CLUSTER ~50–60% to fan each stab into a scattered stereo multi-tap pattern; **SPREAD widen** (off = subtle widening, NOT ping-pong) for a cohesive wide bed.
5. A/B SPREAD widen ↔ ping-pong to hear how much stereo width MISO + CLUSTER are buying you.
6. Pick single stabs and short phrases and let them overlap to fill the field; hold the MODE button to panic-reset to a clean delay if it runs away.

## Notes
- **Distinct from the existing Big Time "Hizumitas Fuzz Wall" patch:** that one is voiced for an endless self-oscillating drone (FEEDBACK ~60%, Compressed, Long MODE, drone-tagged). This patch is the **108-fuzz STEREO-FAN variant the Fuzz Wall patch's own note points at** — Saturated + higher CLUSTER for spitty stabs the multi-taps echo across the stereo image, Short MODE for a field not a drone.
- **SPREAD naming:** Big Time's SPREAD is an alt *button* with two states — **off = subtle widening, on = ping-pong** (manual p.18). The "widen" called for here is SPREAD **off**: a wide cohesive bed, not hard-panned bouncing echoes. CLUSTER also generates stereo image ("bump it up if your field is feeling narrow," manual p.36), so the width here comes from MISO + CLUSTER + SPREAD-off together.
- Favor **DRY KILL ON** (Options) to print a clean wet stereo field without a centered mono dry note pinning the image.
- Big Time's input is an analog preamp (COLOR) → analog limiter (STATE), built to be slammed by a hot source — a fuzz in front is the intended drive, but keep COLOR modest so it doesn't clamp to porridge.
- **Honesty:** numeric fader positions (COLOR/CLUSTER/FEEDBACK/WET %) are **designed starting points (a dialable recipe), not sourced/published settings**. On recall the motorized faders fly to the saved values and override these live knob positions. The *mechanics* — MISO auto-engage on IN-L, COLOR-modest gain-staging, Saturated + CLUSTER for the 108-fuzz stab variant, SPREAD-off for a cohesive field — are sourced [V/R].

## Sources
- MISO mono-in/stereo-out + "a clean way to fan a mono fuzz into a stereo delay field" + "input is an analog stereo preamp (COLOR) feeding an analog limiter (STATE) … built to be driven hard … A fuzz in front is exactly the intended drive": `gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A (lines 22–43) [V/R].
- 108-fuzz variant = Saturated + higher CLUSTER for spitty rhythmic stabs the multi-taps echo: same dossier §"Which owned fuzz for which centerpiece job" (lines 51–53) + existing Big Time "Hizumitas Fuzz Wall" patch note ("MXR 108 fuzz variant: Saturated + CLUSTER higher").
- SPREAD off=widen / on=ping-pong, CLUSTER multi-tap + stereo-image behavior, MISO auto-engage, DRY KILL: `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` (SPREAD alt-button p.18, stereo §, DRY KILL Options) + `Big-Time-UsageGuide.md` (CLUSTER arrangement fader / ping-pong taps).
- 🟣 designed integration; mechanics are sourced [V/R]; numeric fader positions are a dialable recipe (designed starting points), not published settings.
