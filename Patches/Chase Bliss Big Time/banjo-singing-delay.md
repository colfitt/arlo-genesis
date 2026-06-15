---
type: patch
title: Banjo Singing Delay
device: Chase Bliss Big Time
date: 2026-06-15
description: "The downstream delay for the Clean→Hizumitas banjo transient-tamer chain — a Long/Compressed melodic singing delay (not a wall) that lets an already-sustained banjo note ring out in long, even, decaying repeats."
tags: [delay, banjo, singing-delay, lead, fuzz, compressed, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27" }
  - { name: "Chain / Input", type: switch, value: "Hizumitas (mono) → IN-L (auto MISO mono-in/stereo-out)", options: ["mono → IN-L (MISO)", "stereo in"] }
  - { name: "MODE", type: switch, value: "Long (matches the now-sustaining source)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (holds the hot Hizumitas together, prevents runaway)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Focus (keeps the muffed banjo line defined)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine subtle", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "LOW ~25–35% (fuzz already saturates — bring up only until repeats just begin to compress)" }
  - { name: "TIME", type: knob, value: "long, musical (~1–2 s feel, not max)" }
  - { name: "CLUSTER", type: knob, value: "~30% (clean repeats, not dense)" }
  - { name: "TILT EQ", type: knob, value: "pushed slightly UP (cut muff low-mud)" }
  - { name: "FEEDBACK", type: knob, value: "~45–55% (SINGING decay range — lower than the wall patches so repeats die out musically instead of self-oscillating)" }
  - { name: "WET", type: knob, value: "~40% (line + halo, dry still present)" }
  - { name: "SPREAD", type: switch, value: "widen (off IN-L auto-MISO mono-in/stereo-out)", options: ["off", "widen", "ping-pong"] }
---

# Banjo Singing Delay

## Concept
Most Big Time fuzz patches in this rig chase an endless self-oscillating drone wall. This one is the opposite intent: because Clean has already reshaped the banjo into a long, even-decay source upstream, the delay's job is to let that singing note echo out *musically* — long repeats that sing and decay rather than self-oscillate. MODE Long matches the now-sustaining source; STATE Compressed holds the hot Hizumitas together and prevents runaway; COLOR stays low because the fuzz already supplies saturation (too much COLOR + hot fuzz clamps the internal limiter to porridge); and FEEDBACK is deliberately kept in the 45–55% singing-decay range rather than the 60–80% wall range. The result is a melodic stereo singing delay on a folk instrument made to sustain like a guitar lead.

## How to play it
1. Run the Hizumitas (mono) into **IN-L** so **MISO** auto-engages (mono-in / stereo-out).
2. Set MODE **Long**, STATE **Compressed**, VOICING **Focus**.
3. Set COLOR **LOW (~25–35%)** — the fuzz already supplies saturation; bring it up only until repeats just begin to compress.
4. Set FEEDBACK to **~45–55%** so the repeats SING and decay musically — this is a melodic delay, not a self-oscillating wall. Push higher only if you want it to bloom into a held bed.
5. Push TILT EQ slightly **UP** to cut muff low-mud; keep WET **~40%** so the dry line stays present.
6. Play sparse single banjo notes — the upstream Clean sustain + this delay fill the space; let each note ring out.

## Notes
- Built specifically to pair with Clean "Banjo Transient Tamer" upstream — the compressor does the sustain work, so this delay can stay a clean singing delay rather than an endless wall.
- Differs from the "Hizumitas Fuzz Wall" patch (same MODE Long / STATE Compressed gain-staging) by keeping FEEDBACK in the singing-decay range and CLUSTER low — wall patches run FEEDBACK 60–80% and SPREAD/CLUSTER high to self-oscillate.
- Keep COLOR modest: too much COLOR + a hot Hizumitas makes the internal limiter clamp the repeats to porridge.
- To turn it into a held bed, raise FEEDBACK toward 70%+ and let the swell stack; back it down to return to a clean singing delay.
- ⚠ Recipe/designed: numeric fader values are a dialable starting point; flying faders override on recall — re-trim by ear.

## Sources
- 🟣 designed from `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A (fuzz→Big Time gain-staging: COLOR modest, STATE Compressed under sustaining fuzz, TILT up + Focus to tame mud, MISO auto-engage).
- Hizumitas GearProfile (banjo decays in ~1.5 s; Hizumitas completes the note) + Clean "Banjo Transient Tamer" sheet (compressor-before-fuzz extends decay into guitar-like sustain).
- Big Time manual pp.24–25 (low-COLOR / FEEDBACK behavior) + p.16 (MISO / IN-L auto-engage).
</content>
</invoke>
