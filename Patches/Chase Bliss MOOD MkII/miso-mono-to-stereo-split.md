---
type: patch
title: MISO — mono-in to stereo-out split
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: Feed MOOD a single mono instrument and get a true stereo output — the MISO dip splits a mono input (TS cable in) into a stereo out (TRS cable out), letting a mono guitar/banjo/bass drive MOOD's stereo wet and looper engines. A factory dip-switch / I/O feature documented in the official video manual pt.1 + pt.2 and manual p.44.
tags: [dip, stereo, routing, io, factory, technique]
dips:
  MISO: on
controls:
  - { name: "MISO (dip switch)", type: switch, value: "on", options: ["on", "off"] }
  - { name: "Input cable", type: switch, value: "TS (mono)" }
  - { name: "Output cable", type: switch, value: "TRS (stereo)" }
  - { name: "SPREAD (dip switch, optional)", type: switch, value: "on to widen/animate the stereo image per mode", options: ["on", "off"] }
  - { name: "STEREO WIDTH (hidden, Wet TIME)", type: knob, value: "set to taste — no published value" }
---

# MISO — mono-in to stereo-out split

## Concept
Feed MOOD a single mono instrument and get a **true stereo output**. The **MISO** dip splits a mono input into a stereo out (**TS cable in, TRS cable out**), so a mono guitar/banjo/bass can drive MOOD's stereo wet and looper engines and land in a stereo rig. Note: **MISO is what creates stereo from mono** — SPREAD only *widens* stereo that already exists. This is a routing/IO switch, not a tone recipe — no knob values are involved.

## How to play it
1. Run a **TS (mono)** cable into MOOD's input and a **TRS (stereo)** cable out of its output.
2. Flick the **MISO** dip switch on.
3. Play — your mono source is now split to a stereo output through MOOD's stereo engines.
4. (Optional) Engage **SPREAD** to widen/animate the stereo image per mode; set **STEREO WIDTH** (hidden, Wet TIME) to taste.

## Notes
- **MISO CREATES stereo** from a mono source; **SPREAD only WIDENS** existing stereo — don't confuse the two.
- With a stereo input already present, leave MISO **off**.
- Rig flag: a mono Blooper immediately downstream will re-collapse any stereo image — wide stereo has to land at a later stereo stage.
- This is an I/O routing feature; the only adjustable here is the optional **STEREO WIDTH** (hidden Wet TIME), which has **no published value** — dial it to taste.

## Sources
- gear/Chase Bliss MOOD MkII/research/transcripts/chasebliss-mood-mkii-video-manual-pt1.md (I/O: "Mono-in → stereo-out: TS cable in, TRS cable out, activate the MISO dip switch")
- gear/Chase Bliss MOOD MkII/research/transcripts/chasebliss-mood-mkii-video-manual-pt2.md (Dip switches — MISO)
- gear/Chase Bliss MOOD MkII/research/links/community-mood-mkii-pitfalls-and-gotchas.md (SPREAD widens, MISO creates stereo)
- Chase Bliss MOOD MkII manual, "Customize" p.44 (MISO) — chasebliss.com
