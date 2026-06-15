---
type: chain
title: "Big Time → MOOD Frozen Bed, Live Glitch On Top"
date: 2026-06-15
artists: [Chase Bliss]
instrument: guitar / synth pad
gear:
  - Chase Bliss Big Time
  - Chase Bliss MOOD MkII
  - Elektron Digitakt 2
---

# Big Time → MOOD Frozen Bed, Live Glitch On Top ⭐

The canonical Big Time → MOOD pairing. Freeze a held chord into a non-degrading infinite stereo cloud on Big Time, then let MOOD micro-loop and time-warp a *slice* of that frozen bed while you solo over the whole thing. One Digitakt clock keeps MOOD's glitch grid locked to the Big Time delay subdivision, so the warped slice stutters in time with the bed instead of fighting it.

🟣 DOUG-designed integration. The Big Time + Digitakt patches carry their own provenance; the MOOD patch is purpose-built for this chain (full spec saved alongside). The Taste-ref names the sound it chases.

## Signal path

Guitar / synth pad → **CB Big Time — "Oceanic Drone Bed"** (Long, DIFFUSE+CLUSTER high, SPREAD widen, IN-L auto-**MISO** mono→stereo, hold **RIGHT = FREEZE**) → **CB MOOD MkII — "Frozen-Bed Slice Warp"** (Stretch micro-loop + clock-locked time-warp, hold **LEFT = freeze the slice**) → amp/interface, stereo.

Off to the side, **Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template"** is the clock master: its MIDI clock feeds Big Time (sets the delay subdivision) and MOOD (sets the micro-loop length / warp grid) so both pedals share one grid. No audio runs through the Digitakt here — it is purely the clock/transport brain.

The only "real signal-order" invoked is the standard **delay → glitch-looper** placement (capture the established repeats, then chop them), not an artist-specific path.

## Per-unit

- **CB Big Time — "Oceanic Drone Bed"** — MODE **Long**, STATE **#!&% (misbias)** or Saturated, VOICING Analog, COLOR **~25–30%** (low so echoes climb into the limiter), FEEDBACK **~80%** (well above COLOR → climbing wall), CLUSTER **high ~70%**, DIFFUSE **~80%** with DIFFUSE TYPE **on** (ghostly), SPREAD **widen**, TILT slightly below noon (boost lows for longer tails). Build the wall, then **hold RIGHT to FREEZE** → non-degrading infinite stereo pad. WET is LOUD here — set it carefully before you commit. Feed Big Time's MIDI clock from the Digitakt so its TIME tracks the master tempo (the frozen bed is static, but the *pre-freeze* repeats and any post-freeze re-arm land on the grid).
- **CB MOOD MkII — "Frozen-Bed Slice Warp"** (new, purpose-built) — Looper MODE **Stretch**, Wet MODE **Reverb** (wash around the warped slice; **Delay** if you want the slice to also echo on-grid), ROUTING **IN+micro-loop**, CLOCK ~11:00 (a little grit), MIX ~1:00. **SYNC = LEFT** (Micro-Looper synced to Wet) and feed **MIDI clock** so the loop length locks to the Digitakt grid (CC51>0 follow, CC54 sets loop division). Tap the **RIGHT (Micro-Looper)** footswitch to grab a slice of the frozen bed; **hold LEFT to freeze** the Stretch, then ride Looper **MODIFY toward NOON** to warp/freeze the grain and rotate **LENGTH** to resize it. ⚠️ A stray MIDI *Note* auto-engages Synth Mode (which ignores clock) — keep the Digitakt sending clock + CC only, no notes, to MOOD's channel.
- **Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template"** — `SETTINGS → MIDI CONFIG > SYNC` → `CLOCK SEND` + `TRANSPORT SEND` ON; `PORT CONFIG` OUT PORT FUNC = MIDI. Chase Bliss pedals take MIDI over 1/4" TRS — use a TRS adapter or the CB MIDIBox to fan the clock to both Big Time and MOOD. Set the project tempo so the delay subdivision and the MOOD loop length feel musical against the held bed.

## Routing

Mono in → Big Time **IN-L auto-engages MISO** (mono-in / stereo-out); everything from Big Time onward is stereo, so MOOD sits in a stereo field and its warped slice can pan against the wide frozen cloud. Keep MOOD's MIX moderate — it is a *featured glitch on top*, not a second wall; the Big Time bed should still own the low-mids.

**Gain-staging / grid discipline is the whole game:** keep Big Time COLOR modest so the climbing feedback doesn't slam the limiter to porridge before you freeze. One clock keeps MOOD's micro-loop on the same subdivision as the (pre-freeze) Big Time repeats, so the glitch stutters *with* the bed. If MOOD ever ignores the clock, you've tripped Synth Mode — re-check that only clock/CC (no Notes) are reaching it.

## Sound

A vast, non-degrading stereo cloud holds one chord forever while a small chopped, time-warped fragment of that same cloud stutters and pitch-warps in rhythmic lockstep on top — you solo over both. The bed is glassy and infinite; the glitch is granular and grid-tight.

**Taste-ref:** ambient / experimental — the Chase Bliss "freeze-and-mangle" aesthetic (frozen Big Time bed as ideal MOOD fodder); shoegaze-meets-glitch sustained walls with rhythmic micro-detail.

## Play

1. Play one chord/pad and let the Big Time wall climb (low COLOR / high FEEDBACK).
2. **Hold Big Time RIGHT to FREEZE** → infinite stereo bed.
3. Tap **MOOD RIGHT (Micro-Looper)** to grab a slice of the frozen bed; **hold MOOD LEFT to freeze** the Stretch.
4. Ride MOOD **MODIFY toward NOON** (warp → freeze the grain) and rotate **LENGTH** to resize the held slice — it stutters on the Digitakt grid.
5. Solo over the whole thing. To collapse: tap MOOD's footswitches off, then **hold Big Time MODE to panic-reset** to a clean delay.

## Sources

- **Basis:** designed integration; chains **CB Big Time — "Oceanic Drone Bed"** + **CB MOOD MkII — "Frozen-Bed Slice Warp"** (new) + **Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template"**. Freeze-then-solo + MISO auto-engage + low-COLOR/high-FEEDBACK climb from the Big Time "Oceanic Drone Bed" sheet (manual pp.16, 24–25). MOOD Stretch-freeze / micro-loop / SYNC + MIDI-clock lock (CC51/CC53/CC54) from the MOOD "SYNC", "Stretching 101", and "Clock-Synced Loop Layer" sheets (manual pp.17, 34–35); Synth-Mode-ignores-clock caveat from the MOOD SYNC sheet. One-clock-master rig wiring + TRS-MIDI to CB pedals from the DT2 clock-master template.
- 🟣 designed (DOUG); knob values are dialable starting points, not published presets — see each patch sheet.
