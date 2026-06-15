---
type: chain
title: "Clean → Big Time Articulate Ducking Delay"
date: 2026-06-15
artists: [ambienttrash, Nils Frahm]
instrument: guitar / synth
gear:
  - Chase Bliss Clean
  - Chase Bliss Big Time
  - Elektron Digitakt 2
---

# Clean → Big Time Articulate Ducking Delay ⭐

The "delay that stays out from under your attack." A long rhythmic delay's worst habit is washing over the player — every dry note arrives into a cloud of its own past repeats, so the line turns to mush. The fix here is two compressors doing two *different* jobs, not the same job twice. **Clean** sits at the front and just *levels the source* — gentle, transparent, so the player hits Big Time at a steady, predictable level. **Big Time** then runs its own internal limiter in **Compressed STATE**, which ambienttrash's demo names exactly: *"snappy ducking."* The repeats duck under your fresh attack and bloom back up in the gaps. Lock the multi-taps to the Digitakt clock at a dotted-8th and you get punchy, even, articulate ping-pong repeats that breathe around the groove instead of burying it.

🟣 DOUG-designed integration. The Clean→Big Time pairing mirrors ambienttrash's documented rig (EAE Halberd → **Chase Bliss Clean** comp → **Big Time** → Mercury7); the per-unit patch sheets carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

guitar / synth → **CB Clean — "Home Base (Safe Space)"** (gentle transparent leveler, EQ off — just sets a steady level) → **CB Big Time — "Articulate Ducking Multitap"** (MODE Short, STATE Compressed/ducking, CLUSTER ~½ multi-tap, SPREAD ping-pong, dotted-8th, IN-L auto-MISO if mono) → amp / interface. **Elektron Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template"** is clock MASTER: DT2 DIN MIDI OUT → Big Time MIDI IN (native 5-pin, no MIDIBox) → Big Time follows the tempo and the taps land on the grid.

## Per-unit

- **Clean — "Home Base (Safe Space)":** the leveler, not a character comp. Set `Sensitivity` FIRST by ear to the left red LED at playing volume, per source (the guitar and a synth line will never share a value). `Dynamics ~10–11:00` (gentle comp, below noon), `Attack ~10–11:00`, `Release Mid (User 650 ms)`, `EQ noon (off)`, `Wet ~1:00` (unity-to-slight boost), `Dry off`, all dips OFF. The whole point is a steady, even level into Big Time — **not** hard squash. Resist the urge to slam it: if you double-compress hard here, Big Time's Compressed limiter has nothing left to duck and the repeats go flat and lifeless.
- **Big Time — "Articulate Ducking Multitap" (NEW):** `MODE Short`, `STATE Compressed` — this is the engine of the chain; Compressed is the "snappy ducking" voice (ambienttrash 6:46) that holds the repeats out from under your attack and stops runaway. `VOICING Focus` (shaves highs+lows over time → focused floating repeats, keeps each tap defined). `SCALE Off`, `MOTION Off`, `0.5X off` (this is the *clean* articulate cousin of the Lo-Fi Rhythmic Groove, not a crushed one). `CLUSTER ~½` for the multi-tap rhythmic pattern, `SPREAD ping-pong` so the added taps scatter L↔R, `FEEDBACK ~40%` (articulate, decays musically — not a wall), `COLOR low ~25–30%` then up to taste, `TILT EQ slightly up`, `WET ~40%`. `TIME` = MIDI clock; subdivision dotted-8th via `CC54`; `CC111 = 0` to follow.
- **Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template":** clock master. `SETTINGS → MIDI CONFIG > SYNC` → `CLOCK SEND` + `TRANSPORT SEND` ON. Drive the dotted-8th feel from the pattern tempo; optionally p-lock Big Time's `COLOR=CC14 … WET=CC19` from a DT2 MIDI track for grid-quantized delay moves on pattern changes, and fire Big Time preset recalls with PC on a trigless trig.

## Routing

Clock chain: **DT2 = clock master**, Big Time = slave. Big Time takes MIDI natively on 5-pin DIN — DT2 DIN MIDI OUT → Big Time MIDI IN directly, no MIDIBox. On Big Time, `CC111 = 0` (FOLLOW) and `CC54` sets the subdivision (`0–12 = 1/16…whole`; pick the dotted-8th value). With `SCALE Off`, the clock snaps delay TIME to the incoming quarter so you can bend TIME without losing tempo. Run a mono guitar in and Big Time's `IN-L auto-engages MISO` (mono-in / stereo-out) so the ping-pong taps fan out stereo; a stereo synth feeds both ins directly.

**Gain-staging is the whole argument, and it's two comps doing two jobs:** Clean *levels* the source (transparent, steady level — slow-ish attack, gentle ratio) so Big Time's analog limiter sees a predictable, consistent input. Big Time's `STATE Compressed` then does the *musical* ducking on the repeats. Keep `COLOR` modest — start low and bring it up only until the repeats just begin to compress; too much COLOR + a hot input clamps the limiter and the multi-taps "turn to porridge." If the repeats wash over the line, that's the tell you over-compressed at Clean — back `Dynamics` off, don't reach for more.

## Sound

Punchy, even, ducking multitap repeats that stay out from under your attack — a tight live rhythmic delay locked to tempo. Each fresh note is clear and dry on top; the repeats duck beneath it and bloom back up in the gaps, ping-ponging dotted-8th across the stereo field, articulate and grid-locked instead of washy.

**Taste-ref:** ambienttrash's stereo Big Time voice (Clean comp → Big Time "snappy ducking" Compressed state) crossed with a Nils-Frahm-style clocked rhythmic-delay pulse — a delay that grooves with you rather than over you.

## Play

1. Start the Digitakt; confirm Big Time is following (`CC111 = 0`) and the taps land on the dotted-8th (`CC54`).
2. Re-LED Clean's `Sensitivity` against the instrument, then play and feel the level sit even and steady.
3. Play *into the gaps* — let the ducking do its job: the repeats sink under your attack and rise in the spaces, so leave space.
4. Ride `CLUSTER` to thicken/thin the multi-tap density and `WET` to swell the delay in for a chorus; raise `FEEDBACK` toward 55% for a fuller pulse, drop it back for a tight slap. Hold the MODE button as a panic-reset to a clean simple delay if it ever runs away.

## Sources

- **Basis:** designed integration; chains **Clean "Home Base (Safe Space)"** + **Big Time "Articulate Ducking Multitap"** + **DT2 "MIDI / Clock-Master Rig Template"**. The Clean→Big Time pairing and the "snappy ducking" Compressed-state voice are documented in `Gear/Chase Bliss Big Time/research/transcripts/ambienttrash-big-time-full-demo-stereo-NOTES.md` (6:46 "Compressed state — snappy ducking"; chain shown: EAE Halberd → Chase Bliss Clean comp → Big Time → Mercury7). MODE Short + CLUSTER multi-tap + STATE Compressed locked to clock, COLOR-low gain-staging, and CC54/CC111 clock CCs from `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §"Rhythmic delay locked to the groove" [V/R] and §"Clock-sync".
- Clean leveler (gentle below-noon comp, EQ off, level-not-character) from the Clean "Home Base (Safe Space)" sheet (`research/links/cb-manual-clean-compression-recipes.md`).
- `Research/Taste-Profile/taste-profile.md` (clocked rhythmic-delay lens)
</content>
</invoke>
