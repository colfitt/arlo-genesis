---
type: patch
title: Loop Disintegration Drone
device: Chase Bliss Big Time
date: 2026-06-19
description: "Weaponizes Big Time's hidden-digital-feedback quirk as a feature — build a bed in Long, switch to Loop (audio carries over), ride frozen playback as a stable drone, then set STATE Saturated/#!&% misbias and push TEXTURE (you'll hear NOTHING yet) and re-engage OVERDUB to write progressive degradation into each new layer while old layers persist. Inverse of `frippertronics-carve-loop` (which treats STATE as cosmetic and carves only via VOICING). Loop mechanics are fully manual-confirmed; the clock-face numbers are a dialable DOUG recipe."
tags: [loop, drone, disintegration, misbias, saturated, overdub, sound-on-sound, looping, designed]
dips:
  DRY KILL: "optional ON (Options menu) for a wet-only drone; OFF keeps live playing dry over the bed"
hidden:
  TEXTURE: "alt under COLOR — set BEFORE re-overdubbing; inaudible until the next OVERDUB pass (hidden digital feedback)"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot (10 internal / 127 via MIDI); recall flies the faders to saved positions" }
  - { name: "MODE", type: switch, value: "Build in Long → switch to Loop (audio carries over). Loop is the patch; Long is just how you capture the bed", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Start Digital (stable bed), then switch to Saturated or #!&% (misbias) before re-overdubbing — INAUDIBLE until you overdub again (see Notes)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm or Analog — the ALWAYS-LIVE carve (filter slope is heard immediately, unlike STATE/TEXTURE)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off (or slow Sine for drift in the bed)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "TIME", type: knob, value: "center ≈ 48 s @ ~44 kHz; up ≈ 3.2 min @ ~11 kHz (longer, lo-fi); down ≈ 12 s @ ~172 kHz (short, hi-fi) — sets the loop fidelity/length trade" }
  - { name: "COLOR", type: knob, value: "~40% (modest — degrade via STATE-on-overdub + VOICING, not by clipping the bed)" }
  - { name: "CLUSTER", type: knob, value: "~25–30% (on re-overdub, higher CLUSTER scatters the new layers)" }
  - { name: "TILT EQ", type: knob, value: "noon to slightly down (lows feed the loop = louder/longer; a feedback-decay governor)" }
  - { name: "FEEDBACK", type: knob, value: "high ~70–80% on overdub (turn DOWN and layers fade away; this is the fade-vs-persist control)" }
  - { name: "WET", type: knob, value: "set carefully if DRY KILL ON — the loop is then your entire output" }
  - { name: "TEXTURE", type: knob, value: "alt under COLOR — push it for misbias grain; HEARD ONLY on the next OVERDUB pass" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
  - { name: "DRY KILL", type: switch, value: "optional ON (Options) for a wet-only drone", options: ["off", "on"] }
  - { name: "LEFT footswitch", type: button, value: "TAP = record, then set endpoint, then toggle OVERDUB ↔ PLAYBACK (re-overdub is how degradation gets written in)" }
  - { name: "RIGHT footswitch", type: button, value: "TAP = STOP/reset; HOLD = DELETE the loop" }
  - { name: "MODE button (hold 2s)", type: button, value: "Panic reset → clean simple delay" }
---

# Loop Disintegration Drone

## Concept
Big Time's looper has a deliberate quirk: in Loop mode playback is **frozen** ("will not change or deteriorate, regardless of how you change the controls"), and STATE/TEXTURE changes run on **hidden digital feedback** — they're inaudible until the next OVERDUB pass. This patch weaponizes that as a feature. Build a bed in **Long**, switch to **Loop** (the audio carries over), and ride it as a stable frozen drone. Then quietly set **STATE Saturated or #!&% misbias** and push **TEXTURE** — you hear nothing yet — and **re-engage OVERDUB**: now each *new* layer is written with progressive degradation while the *old* layers persist. The bed disintegrates a layer at a time, on your command. The exact inverse of `frippertronics-carve-loop`, which deliberately treats STATE as cosmetic and carves only via VOICING; here STATE-on-overdub is the whole point.

## How to play it
1. **MODE Long.** Build a phrase/bed you like; set **FEEDBACK high** so it sustains.
2. **Switch MODE to Loop** — the audio carries over. Tap **LEFT to record**, set the endpoint, then **LEFT again to PLAYBACK**. The bed is now frozen and stable (use **STATE Digital** here for "traditional," stable looping).
3. Let it ride as a drone. Live-play over it (or flip **DRY KILL ON** in Options for a wet-only bed).
4. **Set the disintegration before you write it:** switch **STATE to Saturated** (or **#!&% misbias** for the harshest crumble) and push **TEXTURE** (alt under COLOR). You will hear NO change yet — that's expected.
5. **Re-engage OVERDUB** (toggle on LEFT) and add a pass — the new layer is written through the degraded STATE while old layers persist. Repeat to disintegrate the bed a layer at a time.
6. Shape the evolution on re-overdub: **CLUSTER up** scatters new layers, **FEEDBACK down** fades layers away, **VOICING Warm/Analog** is the always-live filter carve (heard immediately, no overdub needed).
7. To collapse: **HOLD RIGHT to DELETE**, or **hold MODE ~2 s** to panic-reset.

## Notes
- **The OVERDUB pass is the entire mechanism.** Frozen playback never changes; STATE/TEXTURE/CLUSTER/FEEDBACK only bite when you overdub again, because Loop runs hidden **digital feedback** behind the scenes (manual). VOICING (Warm/Analog filter carve) is the one always-live control. So: set the destruction, hear nothing, overdub to commit it.
- "For stable, 'traditional' looping use the Digital state. Every other state is designed to change and disintegrate over time" (manual) — which is exactly why you build the bed in Digital and switch to Saturated/misbias only when you want the next layer to start crumbling.
- **STEP is non-functional in LOOP mode** (verified) — no footswitch sequence-stepping in Loop (nor in MOD). The LEFT/RIGHT footswitches are the looper transport (LEFT = record / set-endpoint / OVERDUB↔PLAYBACK toggle; RIGHT tap = STOP/reset, hold = DELETE), not a step sequencer.
- **TIME is the fidelity/length trade:** center ≈ 48 s @ ~44 kHz; up ≈ 3.2 min @ ~11 kHz (longer but lo-fi); down ≈ 12 s @ ~172 kHz (short but hi-fi). Pick the window before you commit the loop.
- **MIDI loop choreography** (hands-free): RECORD CC104, PLAY CC105, DELETE CC106, STOP CC107, PLAY/DUB Options toggle CC42. Big Time takes full-size 5-pin DIN MIDI (IN + THRU, default channel 2) — clock/trigger it with a direct DIN cable, no TRS adapter or CB MIDIBox.
- ⚠️ HONEST: the Loop mechanics (frozen playback, hidden digital feedback, STATE-disintegrates-on-overdub, TIME fidelity/length numbers, the CC map) are fully manual-confirmed. The clock-face fader positions (COLOR / CLUSTER / TILT / FEEDBACK / WET / TEXTURE) are a dialable DOUG recipe, not published Chase Bliss numerics. On recall the motorized faders fly to saved positions and override these starting points.

## Sources
- 🟣 DOUG-designed patch. Loop mechanics are fully manual-confirmed; numeric fader positions are a dialable recipe (designed starting points), flagged as such — the motorized faders override on recall.
- `research/bloops/2026-06-19-chase-bliss-big-time.md` (Lens: patches — LOOP-mode mechanics): playback frozen ("will not change or deteriorate, regardless of how you change the controls"); "Big Time switches over to digital feedback behind the scenes… changing STATE or adjusting TEXTURE will not be heard until you start overdubbing again"; "For stable, 'traditional' looping use the Digital state. Every other state is designed to change and disintegrate over time"; TIME fidelity/length trade (≈48 s @ ~44 kHz center, ≈3.2 min @ ~11 kHz up, ≈12 s @ ~172 kHz down). The "loop-disintegration-drone" build (Long→Loop carry-over, frozen bed, STATE Saturated/#!&% + push TEXTURE inaudibly, re-engage OVERDUB to write degradation while old layers persist) and its distinctness from `frippertronics-carve-loop` are specified there.
- `research/bloops/2026-06-19-chase-bliss-big-time.md` (Suggested corpus edits): add `loop-disintegration-drone` as the inverse of `frippertronics-carve-loop`; include the loop CC map (REC 104 / PLAY 105 / DELETE 106 / STOP 107 / PLAY-DUB toggle 42) and the TIME fidelity/length trade.
- LOOP footswitch transport (LEFT = record / set-endpoint / OVERDUB↔PLAYBACK; RIGHT tap = STOP/reset, hold = DELETE) and STEP non-functional in LOOP & MOD: `research/bloops/2026-06-19-chase-bliss-big-time.md` (candidate index chunks).
- 5-pin DIN MIDI (IN + THRU, channel 2), no TRS adapter: `research/bloops/2026-06-19-chase-bliss-big-time.md` (Lens: combinations).
- Distinctness checked against `Patches/Chase Bliss Big Time/frippertronics-carve-loop.md` (STATE-as-cosmetic, VOICING-only carve) — this patch is the inverse (STATE-on-overdub = the disintegration engine).
