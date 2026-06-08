https://www.chasebliss.com/ (per-pedal manuals, URLs inline)
chasebliss.com + midi.guide + local MIDI manuals · Chase Bliss · accessed 2026-06-03

# CB-stack MIDI clock sync — per-pedal, VERIFIED

Master clock = **Elektron Digitakt 2** (DIN MIDI OUT, CLOCK SEND + TRANSPORT SEND on in MIDI CONFIG > SYNC). DIN → CB MIDIBox → ring-active TRS to each CB pedal (except Big Time, which takes DIN directly — see the TRS/MIDIBox file). This file is the factual clock-capability table for all 7 CB pedals, corroborating and going deeper than the prior verified table at `Gear/Elektron Digitakt 2/research/links/rig-dt2-clock-sync-pedals-verified.md`.

## The shared CB clock convention
Across the CB stack, MIDI clock follow/ignore is the **same CC on every pedal that supports it**:
- **CC51 = MIDI CLOCK IGNORE** — value `0 = ignore`, `>0 = follow`. (Verified identical on MOOD MkII, Lost + Found, Onward.)
  - ⚠️ Watch the polarity wording: MOOD/Onward manuals say "0 = ignore, >0 follow." Lost + Found prints "ignore = 0, follow = 1 or >." Same behavior. Big Time inverts the number AND the wording (CC111, "FOLLOW = 0, IGNORE = 1 or >") — see its row.
- Note subdivision (what division the synced parameter locks to) is per-pedal: usually **CC53/CC54**.
- When following clock, **tap tempo is overridden** (Lost + Found: "Tap tempo doesn't work when synced to MIDI clock").

## Per-pedal table

| Pedal | Clock sync? | What locks to clock | Clock-ignore CC | Subdivision CC | MIDI jack | Verified |
|---|---|---|---|---|---|---|
| **Blooper** | ✅ Yes | Loop record/playback ("synced blooping" — arms, starts on next pulse; stays phase-locked) | (CC for clock not printed in quick-start) | **CC54** sets note division | TRS (MIDIBox) | ✅ Quick-start PDF + product page |
| **MOOD MkII** | ✅ Yes (NOT in Synth Mode) | Wet-Channel delay time + Micro-Looper loop length (via CLOCK), tape/stretch speeds, ramping | **CC51** (0=ignore) | **CC53** (wet) + **CC54** (looper), 0–7 = 1/32…whole | TRS (MIDIBox) | ✅ MOOD MkII MIDI Manual |
| **Big Time** | ✅ Yes — and can be **clock MASTER** | Delay TIME / subdivision; behavior depends on SCALE | **CC111** (FOLLOW=0, IGNORE=1+) | **CC54**, 0–12 = 1/16…whole | **5-pin DIN** (no MIDIBox) | ✅ Big Time MIDI Manual |
| **Lost + Found** | ✅ Yes | The TIME subdivision of whichever delay/LFO algorithm is loaded per channel (Slow-verb, Pitch Repeater, Orchestral Swell, Spectral Modulator, Tape Echo sync usefully; **Useful Ambience does NOT beat-sync**; Phaser syncs uselessly). **MIDI clock overrides the UNSYNC dip.** *(Not a dedicated gate/tremolo — corrected from the L+F usage research.)* | **CC51** (ignore=0) | **CC53** (L) / **CC54** (R), 0–12 = 1/32…double-whole | TRS (MIDIBox) | ✅ Lost + Found MIDI Manual + BachelorMachinesTV teardown |
| **Onward** | ✅ Yes | GLITCH timing / overall timing (SIZE sets the synced subdivision) | **CC51** (0=ignore) | **CC53** (8 divisions) | TRS (MIDIBox) | ✅ Onward MIDI Manual + midi.guide |
| **Clean** | ⚠️ Likely (feature-listed) | Bounce/internal modulation LFO ("tempo-synced stereo modulation") | none documented (no clock-ignore CC on midi.guide) | — | TRS (MIDIBox) | ⚠️ Product page lists "Clock Sync"; midi.guide CC ref shows NO clock CC. SEE FLAG below. |
| **Generation Loss MkII** | ❌ **NO** | — PC/CC only; Wow/Flutter free-runs | n/a | n/a | TRS (MIDIBox, for PC/CC) | ✅ Product page "MIDI (PC, CC)" + midi.guide ("clock: None") |
| *(Brothers AM — not in the 7, gain pedal)* | n/a | no time param | n/a | n/a | TRS | ✅ — DT2 useful only for PC/CC |

## Per-pedal detail (verified quotes)

### Blooper — ✅ "synced blooping"
*"When blooper is following an external tempo (MIDI or CV), it waits until the next pulse to start recording... pressing record gets blooper ready, but it won't begin until the next beat... playback is also synced to avoid drift."* Product page: *"sync looping with... MIDI beat clock — no phasing or getting out of time."* **Set the sync note division with CC54.** Blooper also auto-adopts the channel of incoming MIDI (hold both footswitches at power-up). CC#1 = RECORD, CC#15 = LAYERS, CC#20 = RAMP.

### MOOD MkII — ✅ except Synth Mode
MOOD MkII MIDI Manual: *"MIDI clock is ignored when in MIDI Synth Mode."* (Synth Mode auto-engages on any incoming MIDI Note and turns CLOCK into pitch/semitone control — so a stray Note message from the Digitakt will silently knock MOOD out of clock sync. Exit via CC59 or by moving the CLOCK knob.) Outside Synth Mode, CLOCK governs loop length/quality and locks to clock; **CC51 = clock ignore (0=ignore)**, **CC53/CC54 = per-channel divisions** (0=1/32 … 7=whole). Default ch.2, 122 presets.

### Big Time — ✅ and a clock SOURCE
*"You can use MIDI with Big Time to... sync to external clock, **use as clock source**."* Clock behavior depends on SCALE: in **OFF/CHROMATIC** it snaps the delay to the incoming quarter note (you can bend time without losing tempo); in **OCT+4+5/OCTAVE** it sets quarter-note at slider center and moves to musical subdivisions above/below. **To output clock:** set the MIDI OUT jack active with **CC110 (OUT=1+)**, range **60–240 bpm** (auto-subdivides to nearest half/double if out of range). **CC111 = MIDI CLOCK IGNORE (FOLLOW=0, IGNORE=1+).** So Big Time can either follow the Digitakt OR be the master that clocks the rig. Default ch.2, **127** presets (10 factory). Subdivision **CC54** (0–12).

### Lost + Found — ✅
Product/MIDI: *"Use MIDI with Lost + Found to control any of its parameters, **sync to external clock**, and save/recall up to 122 presets."* **CC51 = MIDI clock ignore (ignore=0, follow=1+)**; **CC53 (L) / CC54 (R) = tap subdivision** (0=1/32 … 11=whole, >11=double-whole). ⚠️ Tap tempo disabled while clock-synced. Default ch.2.

### Onward — ✅
Base manual: *"SIZE will also control the subdivision when MIDI is clock-synced"* and *"MIDI is clock-synced"* / *"compatible with MIDI Clock that can be used for tempo sync of GLITCH."* **CC51 = MIDI clock ignore (0=ignore, 1–127=follow)**; **CC53 = MIDI sync subdivision** (8 options). SIZE = CC14. Default ch.2, 122 presets. Glitch/Freeze retrigger via CC108/CC109 — useful for clock-quantized re-triggers from the Digitakt.

### Clean — ⚠️ FLAG: feature-listed but CC-reference shows no clock CC
The Clean product page lists **"clock sync"** in its feature set and markets *"tempo-synced stereo modulation"* for its Bounce LFO. **However**, the midi.guide CC reference for Clean documents **no MIDI clock ignore/follow CC** and **no clock-related capability** — only Ramp/Bounce on/off (CC52) and Ramp Speed (CC20, an internal rate). Default ch.2. **HONEST VERDICT: treat Clean's clock-sync as PROBABLE-BUT-UNCONFIRMED at the CC level.** Its Bounce modulation can plausibly lock to clock per the marketing, but I could not verify the mechanism (which CC, what divisions) from the CC reference. ➜ Confirm against the full **Clean MIDI manual** before relying on tempo-synced Bounce in a critical patch. Do NOT assert Clean locks to the grid as fact.

### Generation Loss MkII — ❌ NO clock (double-verified)
Product page MIDI line, verbatim: **"MIDI (PC, CC)"** — no clock listed. midi.guide: 41 params, *"Documented MIDI clock-related capabilities: None."* **Wow & Flutter cannot be tempo-synced**; the only timing CC is Ramp Speed (CC20), an internal free-running LFO. The Digitakt can still recall GL MkII presets via PC and modulate any knob via CC p-locks (rhythmic CC moves), but the warble will NOT lock to the bar grid. This is the one true "no clock" pedal in the stack.

## How to clock the whole stack from the Digitakt 2
1. DT2: MIDI CONFIG > SYNC > **CLOCK SEND = ON**, **TRANSPORT SEND = ON**.
2. DT2 DIN MIDI OUT → CB MIDIBox(es) → TRS to: Blooper, MOOD (out of Synth Mode), Lost + Found, Onward, Clean. + DT2 DIN → Big Time directly (or via THRU).
3. Set CC51=ignore→follow as needed per pedal (default behavior is to follow when clock is present); pick subdivisions via each pedal's CC53/CC54 (Blooper CC54).
4. Generation Loss MkII rides along for PC/CC only — its warble free-runs by design.
5. Alternative master: let **Big Time output clock** (CC110=OUT) and clock the rig from the loops/echoes instead of the DT2.

## Sources
- https://www.chasebliss.com/blooper + https://blooper.chasebliss.com/midi/docs/midi-quick-start.pdf
- https://www.chasebliss.com/mood-mkii + MOOD MkII MIDI Manual (CC51/53/54, Synth-Mode clock-ignore)
- https://www.chasebliss.com/big-time + Big Time MIDI Manual (CC110 clock out, CC111 ignore, SCALE behavior)
- https://www.chasebliss.com/lost-and-found + Lost + Found MIDI Manual (CC51/53/54)
- https://www.chasebliss.com/onward + Onward MIDI Manual + https://midi.guide/d/chase-bliss/onward/ (CC51/CC53)
- https://www.chasebliss.com/clean + https://midi.guide/d/chase-bliss/clean/ (clock UNCONFIRMED at CC level)
- https://www.chasebliss.com/generation-loss-mkii (MIDI PC, CC) + https://midi.guide/d/chase-bliss/generation-loss-mkii (no clock)
- Prior verified table: Gear/Elektron Digitakt 2/research/links/rig-dt2-clock-sync-pedals-verified.md
