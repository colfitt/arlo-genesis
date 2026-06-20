---
type: patch
title: Frippertronics Carve Loop
device: Chase Bliss Big Time
date: 2026-06-15
description: "DOUG-designed Loop-mode sound-on-sound recipe — record on the LEFT footswitch, overdub passes, and let VOICING Warm/Analog carve the old layers away as new ones pile on. Wet-only (DRY KILL ON) hands-on performative looper; companion to factory #8 Nostalgic Repeater on the same pedal. Loop/footswitch/VOICING-degrade mechanics are sourced; numeric knob positions are a dialable interpretation."
tags: [frippertronics, looping, sound-on-sound, wet-only, degraded, loop-mode, designed]
dips:
  DRY KILL: "ON (Options menu — double-tap both footswitches; wet-only output)"
controls:
  - { name: "MODE", type: switch, value: "Loop", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Saturated (cosmetic in Loop — see Notes)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm (or Analog ~4k for darker destroy) — this is the carve knob", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off (or slow Sine for drift)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "TIME", type: knob, value: "toward max for the long lo-fi loop window (3+ min lo-fi); back to ~noon for ~45s higher-fidelity loops" }
  - { name: "COLOR", type: knob, value: "~40% (modest — degrade via VOICING + sound-on-sound, not clipping)" }
  - { name: "CLUSTER", type: knob, value: "~25-30%" }
  - { name: "TILT EQ", type: knob, value: "noon to slightly down (lows feed the loop = longer/louder)" }
  - { name: "FEEDBACK", type: knob, value: "high ~70% (keep passes loud enough to keep carving)" }
  - { name: "WET", type: knob, value: "set carefully — wet-only means the loop is your entire output" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "LEFT footswitch", type: button, value: "RECORD/PLAY — tap to record, again to set endpoint, then tap to alternate overdub↔playback (records + overdubs; manual p.15/29)" }
  - { name: "RIGHT footswitch", type: button, value: "TAP = STOP/reset (2nd tap resumes playback); HOLD = DELETE the loop — RIGHT never overdubs (manual p.15/29)" }
---

# Frippertronics Carve Loop

## Concept
A purpose-built Loop-mode sound-on-sound recipe: record a phrase on the LEFT footswitch, overdub passes, and let VOICING Warm/Analog eat the old layers as new ones pile on. Wet-only (DRY KILL ON) so your live playing stays clean against a slowly self-destroying Frippertronics bed. Distinct from factory #8 Nostalgic Repeater (which is the sit-back crumbling-repeats voice) by committing to LOOP mode as a performative looper with the carve happening via the filter slope, not the analog limiter.

## How to play it
1. Switch **MODE to Loop** and confirm **DRY KILL is ON** (Options menu — double-tap both footswitches).
2. Set **VOICING to Warm** (or **Analog** for a darker ~4k destroy) — this is the knob that does the slow carve.
3. Tap **LEFT to record** a phrase; tap **LEFT again to play**, then **overdub successive passes** on top.
4. Let it ride: each Warm/Analog pass is darker and more degraded than the last, so the bed eats itself as you add to it.
5. Play melody over the decaying bed — wet-only keeps your live signal clean against the crumble.
6. To collapse, **delete the loop** (**HOLD** the RIGHT footswitch in Loop mode; a *tap* of RIGHT only stops/resets) or **hold MODE ~2s to panic-reset** to a simple delay.

## Notes
- HONESTY: Loop mode runs **DIGITAL feedback behind the scenes** (manual p.29), so STATE/TEXTURE changes aren't heard until you re-overdub. The "slow destroy" comes from **VOICING Warm/Analog = sound-on-sound degrade**, NOT the Saturated analog limiter. VOICING is the destroy knob; STATE is mostly cosmetic until you overdub again.
- All numeric values are a **designed dial-in recipe, not published/sourced settings** — Chase Bliss publishes character, not numbers.
- Wet-only (DRY KILL ON) means **WET sets your entire output level** and high FEEDBACK climbs — set WET carefully before performing.
- No MIDI clock needed — free-running performative loop. Slave to master clock only if you want the carve to lock to a rig tempo.
- Footswitch labels reflect Loop-mode per-mode behavior; the physical left/right caps are TEMPO/BYPASS in other modes (manual p.16).

## Sources
- 🟣 DOUG-designed Loop-mode recipe. Loop/footswitch/VOICING-degrade mechanics are sourced (DeepResearch + UsageGuide); all numeric knob positions are a dialable interpretation flagged as such (Chase Bliss publishes character, not numbers).
- Loop-mode mechanics + "performative phrase-freeze" looper role: `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` (line 71; line 122 / manual p.29; footswitch per-mode behavior line 32).
- "Warm/Analog = sound-on-sound degrade" + looper fidelity vs TIME: `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` §1 (line 58).
- DRY KILL in Options menu + wet-only routing: `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` (line 36; line 62).
- Loudness-driven COLOR → FEEDBACK → WET interaction: manual p.10 (cited in DeepResearch line 40).
- Taste-ref: Fripp/Eno Frippertronics — making-aesthetic reference, not a sourced rig.
