Multiple manufacturer sources (per-pedal URLs inline below)
Compiled from Chase Bliss / Strymon / Eventide / Hologram official manuals + midi.guide CC references · 2026-06

# Which owned pedals sync to the DT2's MIDI clock — VERIFIED, per device

The DT2 sends MIDI clock + transport (CLOCK SEND / TRANSPORT SEND in MIDI CONFIG > SYNC). A time-based pedal then tempo-syncs its delay/loop/modulation to that clock. **Chase Bliss pedals take MIDI over a 1/4" TRS jack** (not 5-pin DIN) — you need a TRS-MIDI adapter or the **Chase Bliss MIDIBox** (5-pin DIN → TRS) between the DT2's DIN MIDI OUT and each CB pedal. Strymon/Eventide/Hologram have their own MIDI jacks (DIN and/or USB) — check each below.

## ✅ CONFIRMED — syncs to MIDI clock

### Chase Bliss Blooper (looper) — https://www.chasebliss.com/blooper
- "You can sync looping with a CV clock source or via **MIDI beat clock**." Loop stays phase-locked to a drum machine — "no phasing or getting out of time."
- **Auto-channel:** "If blooper detects incoming MIDI, it will automatically change to that channel (and stay that way even after being turned off)." So just send clock on the channel you want and Blooper adopts it.
- Recipe: DT2 CLOCK SEND ON → TRS-MIDI → Blooper; record a loop, it locks to DT2 bars/tempo. (Source: Blooper MIDI quick-start PDF + product page.)

### Chase Bliss MOOD MkII (looper/delay/synth) — https://www.chasebliss.com/mood-mkii
- "Clock sync and control over every parameter." Receives MIDI via 1/4" TRS (MIDIBox converts DIN→TRS).
- ⚠️ **Gotcha (verified):** "MIDI clock is **ignored when in MIDI Synth Mode**." Avoid Synth Mode when you want clock sync. (Source: MOOD MkII MIDI Manual.)

### Chase Bliss Big Time (analog/digital echo) — https://www.chasebliss.com/big-time
- Delay can be controlled by MIDI; **SCALE** sets whether time changes smoothly or in musical steps for tempo-synced subdivisions ("creative transposition or Thermae-like sequencing"). Dedicated Big Time MIDI Manual documents clock. → delay syncs to DT2 clock. (Source: Big Time manual + MIDI manual PDFs.)

### Chase Bliss Lost + Found (gate/dynamics) — https://www.chasebliss.com/lost-and-found
- "Use MIDI with Lost + Found to control any of its parameters, **sync to external clock**, and save/recall up to 122 presets." The gate/tremolo timing locks to clock.
- ⚠️ "Tap tempo doesn't work when the pedal is synced to MIDI clock" (expected — clock overrides tap). (Source: Lost + Found MIDI Manual; midi.guide/d/chase-bliss/lost-and-found.)

### Chase Bliss Onward (dynamic sampler/glitch) — https://www.chasebliss.com/onward
- "Compatible with **MIDI Clock that can be used for tempo sync of GLITCH**." MIDI = PC, CC, **Clock Sync**. SIZE sets glitch length / overall timing → syncs to DT2. (Source: Onward MIDI Manual PDF; midi.guide/d/chase-bliss/onward.)

### Chase Bliss Clean (stereo compressor) — https://www.chasebliss.com/clean
- Feature list explicitly includes **clock sync** alongside MIDI PC/CC, CV, expression, and internal modulation (ramp/bounce). "MIDI automation… can allow for **tempo-synced stereo modulation**." → its Bounce/modulation LFO can lock to DT2 clock. (Verified from product page feature list; for exact synced-modulation behavior consult the Clean MIDI manual.)

### Strymon TimeLine (delay) — https://www.strymon.net/using-midi-control-pedals-2/
- Per-preset **MIDICL = ON** → "TimeLine will respond to an external MIDI clock from the MIDI Input." Set per preset (push value encoder, turn to MIDICL). Delays auto-follow incoming tempo; **TAPDIV** sets the subdivision.
- ⚠️ "The TimeLine's **delays sync to MIDI Clock, but the looper does NOT**." (Source: Strymon "Using MIDI Part 2"; TimeLine manual.)

### Strymon Big Sky (reverb) — https://www.strymon.net/using-midi-control-pedals-2/
- Big Sky syncs the **Pre-Delay** parameter to MIDI clock (it has no delay/looper to sync). Firmware 1.44+ made **MIDI CL per-preset** (moved from GLOBLS to PARAMS). Modest but real. (Source: Strymon MIDI guide.)

### Eventide H90 — https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/tempo-menu.html
- System Menu > MIDI: set clock source; **Tempo Menu > Tempo Source = MIDI** to sync tempo to MIDI clock (DIN or USB). Per-program/preset Tempo Sync toggled in Parameters Edit Mode (press Presets + Parameters buttons together). With Tempo Sync ON, delay displays as rhythmic subdivisions of the beat. Looper records sync to next beat only when on external clock AFTER a MIDI Start. (Source: Eventide H90 docs, Tempo + MIDI sections.)

### Hologram Microcosm — https://www.hologramelectronics.com/pages/microcosm-manual
- Accepts MIDI clock via MIDI IN; **on MIDI Start it switches from internal to external clock**, on MIDI Stop reverts. No manual "enable" needed — sending clock+transport is enough. Sets tempo for its time-based effects. Can also output MIDI clock. ⚠️ Tap tempo disabled while synced. (Source: Microcosm manual.)

### Hologram Chroma Console — https://www.hologramelectronics.com/pages/chroma-console
- "Highly-configurable MIDI implementation over **DIN and USB-C, including MIDI sync** and full control over effects." Time-based effects (e.g. its modulation/space characters) follow incoming clock. (Source: Chroma Console product/MIDI page. Verify exact synced parameters in its MIDI manual before a specific patch.)

## ❌ DOES NOT sync to MIDI clock (verified)

### Chase Bliss Generation Loss MkII — https://www.chasebliss.com/generation-loss-mkii
- **MIDI is PC + CC only — NO MIDI clock.** Verified against both the official product page MIDI line ("MIDI (PC, CC)") and the midi.guide CC reference (41 params; "Documented MIDI clock-related capabilities: None"). The **Wow and Flutter cannot be tempo-synced** to the DT2; the only timing CC is "Ramp speed" (CC 20), an internal LFO rate, not clock-locked.
- The DT2 can still **recall GL MkII presets via Program Change** and **modulate any knob via CC p-locks** (rhythmic CC moves), but the warble rate will free-run, not lock to the grid.

## ⚠️ Not applicable / no time-synced parameter

### Chase Bliss Brothers AM (dual overdrive/boost) — https://www.chasebliss.com/brothers-am
- A gain pedal: full MIDI control of every parameter + the Ramp LFO, but it has **no delay/looper/tempo'd-modulation parameter** for clock to lock to. "MIDI clock sync" isn't meaningfully applicable. The DT2 is useful here only for **PC preset recall** and **CC automation** (e.g. ramping gain/tone), not clock. (Treat any "Brothers AM clock sync" claim as a non-feature.)

## Summary table
| Pedal | MIDI clock sync? | What syncs | DT2 connection |
|---|---|---|---|
| CB Blooper | ✅ Yes | Loop length/playback | TRS (MIDIBox) |
| CB MOOD MkII | ✅ Yes (not in Synth Mode) | Loop/delay | TRS (MIDIBox) |
| CB Big Time | ✅ Yes | Delay time/subdivision | TRS (MIDIBox) |
| CB Lost + Found | ✅ Yes | Gate/dynamics timing | TRS (MIDIBox) |
| CB Onward | ✅ Yes | GLITCH timing/size | TRS (MIDIBox) |
| CB Clean | ✅ Yes | Bounce/stereo modulation | TRS (MIDIBox) |
| CB Generation Loss MkII | ❌ No | — (PC/CC only) | TRS (PC/CC use only) |
| CB Brothers AM | n/a | — (gain pedal) | TRS (PC/CC use only) |
| Strymon TimeLine | ✅ Yes (delays; not looper) | Delay; per-preset MIDICL | DIN |
| Strymon Big Sky | ✅ Yes (limited) | Pre-Delay; per-preset (fw1.44+) | DIN |
| Eventide H90 | ✅ Yes | Delay/tempo'd algos; per-program | DIN or USB |
| Hologram Microcosm | ✅ Yes (auto on MIDI Start) | All time-based effects | DIN |
| Hologram Chroma Console | ✅ Yes | Time-based effects | DIN or USB-C |

> Honesty flags: Generation Loss MkII (no clock) and Brothers AM (no time param) are the two that do NOT lock to the DT2 grid — verified against manufacturer MIDI docs. Chroma Console's *exact* set of clock-synced parameters and CB Clean's synced-modulation detail were confirmed at feature-list level; nail down the precise synced params in each pedal's full MIDI manual before building a critical patch.
