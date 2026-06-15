---
type: patch
title: Dynamics-Crumble Long Echo
device: Chase Bliss Big Time
date: 2026-06-15
description: "Designed misbias-as-instrument performance patch — a long, high-feedback loop that stays pristine under gentle playing and sags/drops out/crumbles as you dig in, with MOTION Env letting your picking envelope ride the degradation. Fills the dynamics-responsive-disintegration gap the other Big Time patches don't cover."
tags: [delay, misbias, dynamic, degraded, looping, designed, signature]
hidden:
  TEXTURE: "alt under COLOR — misbias sensitivity; how violently hard attacks crumble"
  DIFFUSE: "alt under FEEDBACK — mid"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot, or dial PC0 LIVE while building" }
  - { name: "MODE", type: switch, value: "Long (8–12 s repeats)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "#!&% (misbias)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Env (envelope drives wobble/degrade depth)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~25–30% (LOW — gentle playing stays clean; only hard attacks bite)" }
  - { name: "TIME", type: knob, value: "long" }
  - { name: "CLUSTER", type: knob, value: "~30%" }
  - { name: "TILT EQ", type: knob, value: "slightly above noon (keep decayed repeats out of the mud)" }
  - { name: "FEEDBACK", type: knob, value: "~70% (sustaining loop)" }
  - { name: "WET", type: knob, value: "~50%" }
  - { name: "TEXTURE", type: knob, value: "~60% (alt under COLOR — misbias sensitivity; this is what makes digging in CRUMBLE)" }
  - { name: "DIFFUSE", type: knob, value: "mid (alt under FEEDBACK)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
---

# Dynamics-Crumble Long Echo

## Concept
Snyder's misbias-as-an-instrument move turned into a performance: run a long, high-feedback loop in the #!&% (misbias) STATE with MOTION Env so your playing envelope rides the degradation. Keep COLOR low so soft attacks stay clean and only hard attacks push the misbias into audible sag, dropout, and crumble — Basinski decay you conduct with your hands. Fills a gap none of the existing Big Time patches cover: crushed-analog is Short, nostalgic-repeater is a cozy fixed-feedback looper, oceanic-drone-bed is the freeze move, sagging-echoes is the clean Compressed delay. This one makes disintegration dynamics-responsive.

## How to play it
1. Set MODE **Long**, STATE **#!&% (misbias)**, VOICING **Warm**, MOTION **Env**; FEEDBACK ~70% for a sustaining loop.
2. Keep **COLOR LOW** (~25–30%) and **TEXTURE up** (~60%) so the misbias only bites on hard attacks.
3. Play gently — the loop holds clean and pristine.
4. Dig in — hard attacks push the misbias into audible sag, dropout, and crumble in real time.
5. Lean back into soft playing and the loop partially recovers (Snyder misbias sag-return).
6. Feed the wet downstream (L&F → OP-1) to re-grain, re-age, and resample the decayed loop.

## Notes
- **Dialable recipe, not sourced numbers** — Chase Bliss publishes character, not numeric knob values; these positions are a designed starting point and the motorized flying faders override anything written here on recall.
- COLOR-low is load-bearing: it is what preserves the pristine-when-gentle / crumbles-when-you-dig-in response. Raising COLOR makes it degrade constantly and kills the dynamic move.
- TEXTURE (alt under COLOR) sets misbias sensitivity = how violently hard attacks crumble.
- MISO auto-engages off IN-L for mono-in/stereo-out.
- Don't double-degrade downstream — Gen Lite on the L&F already carries tape-age; let this pedal own the dynamic crumble.

## Sources
- 🟣 designed (DOUG-built; misbias/Snyder-grounded, dialable recipe — knob numbers interpreted, not published).
- Designed from STATE #!&% (misbias) behavior + Snyder misbias sag-return — `gear/Chase Bliss Big Time/research/.../sonicstate-superbooth-john-snyder-eae-interview.md`.
- MOTION Env + TEXTURE (misbias sensitivity, alt under COLOR) mechanics from `Patches/Chase Bliss Big Time/nostalgic-repeater.md` & `crushed-analog.md`.
- Low-COLOR-so-gentle-stays-clean gain-staging from `Patches/Chase Bliss Big Time/oceanic-drone-bed.md` & `crushed-analog.md`.
- Big Time manual (Long mode, misbias STATE) — `gear/Chase Bliss Big Time/manuals/Big+Time_Manual_Chase+Bliss.pdf`.
</content>
</invoke>
