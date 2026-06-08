# Hologram Electronics Chroma Console — Deep Research

A working dossier for the **5th pedal on Board 3 (End / Time → Tape)** of a stereo banjo/baritone rig. The Chroma Console sits *after* the Chase Bliss Blooper (which is mono) and *before* the Eventide H90 — so it inherits a mono-collapsed loop signal and, being a full stereo box, gets to re-expand it before the H90 reverbs run. In a rig that already carries four other tape voices, this is the second major tape/lo-fi engine after the upstream Generation Loss, and most of this document is about keeping those two from doubling each other: per the Generation Loss dossier, the labor split is **Gen Loss breaks the source → Chroma morphs the textures → PORTA424/424 print** — and the Chroma's job here is *texture-morphing over the time effects*, not being the primary degrader.

> **Profile note.** The on-disk `GearProfile.md` is a stub ("role in the rig — fill in"). The authoritative facts here come from the on-disk manual (`manuals/ChromaConsole.pdf`, **Firmware v1.04**) and the `rig-design.html` map, which places Chroma Console 5th on Board 3 between Blooper and H90. The manual is treated as the source of truth for module/effect names.

## 1. Lineage: Hologram's Tactile Multi-Effect (and where it sits next to Microcosm)

Hologram Electronics is a Knoxville, TN boutique founded 2015 by **Ryan Schaefer** (musician, Royal Bangs) and **Jason Campbell** (engineer) — the two names signing the Chroma Console manual's "Note From The Designers." Hologram's actual product lineage runs **Dream Sequence → Infinite Jets Resynthesizer → Microcosm (2020) → Chroma Console (2024)** ([Equipboard brand page](https://equipboard.com/brands/hologram-electronics), [Hologram Microcosm page](https://www.hologramelectronics.com/products/microcosm)). So the brief's framing of "Hologram's 2nd pedal after Microcosm" is a *rig-context* simplification — it's the owner's **second Hologram pedal** and the sibling to the Board 2 Microcosm, not literally the company's second release. **(Manual-vs-web flag: corrected — it's their fourth product, not second.)**

The Chroma Console was announced **November 2023**, opened pre-orders, and began shipping worldwide by **April 2024** at **$399** ([Sonicstate "Now Shipping"](https://sonicstate.com/news/2024/04/03/hologram-chroma-console-now-shipping/), [Premier Guitar unveiling](https://www.premierguitar.com/news/hologram-effects-chroma-console)). The designers' stated thesis (manual pg. 5): it's "a tribute to the sometimes messy, sometimes chaotic, but always exciting things that can happen when you allow yourself to experiment" — happy accidents from cranked four-track preamps, snarling vintage filters, runaway analog delays — distilled "into something you can use and enjoy every day." Critically, **it is *not* a Microcosm Lite**: Hologram positions it to "sit next to Microcosm or similar granular pedal on your board and not duplicate effects" ([VI-Control thread](https://vi-control.net/community/threads/hologram-chroma-console-similar-to-microcosm-pedal.145458/)), which is exactly how it lives in this rig — Microcosm does granular on Board 2, Chroma does tape/lo-fi morphing on Board 3.

The current firmware is **v1.04 (May 5, 2025)**, which "optimizes Preset Browser with faster preset load time, introduces MIDI CCs for module bypass/engage, plus bug fixes" ([Hologram firmware page](https://www.hologramelectronics.com/pages/chroma-console-firmware)). The on-disk manual is the v1.04 revision.

## 2. Controls — The 4 Modules, 20 Effects, and the "Console"

The face is a deliberately screen-free "control deck": **four color-coded modules**, each with a top knob, an **AMOUNT** knob (doubling as **EFFECT VOL** secondary), and a **button** that steps through that module's five effects (manual pg. 7). A fifth black **MIX** knob blends dry/effected globally. The two footswitches are **TAP/CAPTURE** (left) and **BYPASS/PRESETS** (right). Press a button to descend through effects; **press-and-hold a button to bypass** that module (manual pg. 10).

The four modules and all 20 effects, verbatim from the manual (pg. 12–19) — **this is authoritative**:

- **CHARACTER** (red, TILT + AMOUNT) — drive/dynamics. **DRIVE** (tube-like overdrive), **SWEETEN** (preamp EQ + compression + gentle saturation), **FUZZ** (vintage fuzz; TILT changes transient/bias), **HOWL** (resonant filter fuzz — synth-like stabs), **SWELL** (envelope-triggered volume swells). TILT controls tone (dark↔bright); secondary **SENSITIVITY** sets breakup/swell-trigger threshold.
- **MOVEMENT** (yellow, RATE + AMOUNT) — modulation. **DOUBLER** (stereo double-tracking/slapback), **VIBRATO** (sine→tape-warble pitch mod), **PHASER** (2- to 12-stage), **TREMOLO** (shimmer→square chop), **PITCH** (−1 to +1 octave, lo-fi). Secondary **DRIFT** adds randomness/tape instability.
- **DIFFUSION** (green, TIME + AMOUNT) — time-based. **CASCADE** (BBD analog delay, self-oscillates), **REELS** (worn tape echo, "constantly evolving"), **SPACE** (reverb blending 5 spaces, tight echo→massive cloud), **COLLAGE** (looping delay that destructively edits as you move TIME — pitch bends, half/double-speed loops), **REVERSE** (reverse delay, −1 to +1 octave, "backwards tape"). Secondary **DRIFT**; EFFECT VOL here adjusts only the *wet* signal.
- **TEXTURE** (blue, AMOUNT only) — destruction/polish. **FILTER** (multi-mode: TILT/LPF/HPF, set in FX SETUP), **SQUASH** (heavy compressor→overdrive), **CASSETTE** (wow/flutter/warble/tape degradation/pitch artifacts), **BROKEN** (periodic pitch drops + AM/FM mangling, "motorized audio in need of service"), **INTERFERENCE** (telecom-glitch/radio-static dissolution).

Default chain order is **Character → Movement → Diffusion → Texture**, but **all four modules are freely reorderable** in the FX SETUP menu (manual pg. 27). Secondary controls (SENSITIVITY, DRIFT ×2, OUTPUT LEVEL, EFFECT VOL ×4) live under an A+B button combo (manual pg. 20–23).

## 3. Sonic Character — A Tape/Lo-Fi Color Box, Not a Granular Machine

Where Generation Loss is a *specialist* (it models real tape machines and adds dropouts/failure), the Chroma Console is a **generalist color box** — drive, modulation, delay/reverb, and tape destruction all in one chain, each voiced for "vintage decrepitude." Sound On Sound calls the experience "pouring honey over your cables… warm and full," with **DRIFT** as the central vintage-character control "injecting tape instability throughout the effects chain" ([SOS review](https://www.soundonsound.com/reviews/hologram-electronics-chroma-console)). Reviewers across the board read it as "20 pedals in one" with a uniquely tactile, menu-free workflow ([AltWire](https://altwire.net/chroma-console-by-hologram-electronics-review/), [Guitar.com](https://guitar.com/reviews/effects-pedal/hands-on-hologram-electronics-chroma-console-review/), [MusicRadar](https://www.musicradar.com/news/is-the-hologram-electronics-chroma-console-an-effects-suite-for-people-who-dont-like-multi-effects-pedals)).

The tape/lo-fi palette specifically lives in: **CASSETTE** (the dedicated wow/flutter/saturation effect), **REELS** + **COLLAGE** (wonky evolving tape echo), **BROKEN** + **INTERFERENCE** (degradation/glitch), **VIBRATO** + **PITCH** with **DRIFT** up (tape-warble pitch instability), and **REVERSE** ("backwards tape"). It can be the subtlest of the rig's tape voices (a hair of CASSETTE for glue) or the most chaotic (BROKEN + COLLAGE self-destructing). It does **not** model named tape machines and has **no dropout/failure engine** — that's Gen Loss's territory, which is the whole reason the two coexist.

## 4. Behavioral Notes — Gesture, Capture, Stacking, Stereo

- **GESTURE (knob-motion recorder).** Press **C+D** to enter; turn any primary knob and the motion is recorded and **looped** as a "manual LFO" (manual pg. 24–25; [SOS](https://www.soundonsound.com/reviews/hologram-electronics-chroma-console)). Multiple knobs can be layered (re-enter per knob). Recorded gestures **sync to tap tempo / MIDI clock**, so you can record a slow sweep and then *speed it up past what your hand could physically do* — the manual's stated trick for complex evolving motion. Delete one knob's gesture by moving it live; hold C+D to wipe all.
- **CAPTURE (looper/sustainer).** Hold the TAP footswitch to record up to **30 seconds**; release to loop (manual pg. 26). Short captures crossfade into a **seamless ambient pad/sustainer** (blue lights); longer captures act as a **traditional looper** (green lights). Routable **PRE-FX or POST-FX** per preset (FX SETUP). **Captures are not saved in presets.** SOS flagged the sustainer-pad variant as "finicky" and not quite matching the docs — manage expectations there.
- **Stacking modules.** Because effects are one-per-module, you build a 4-stage chain (e.g. FUZZ → VIBRATO → REELS → CASSETTE), not two effects in the same module. Reorder freely. DRIFT on the two middle modules is the "how broken" master control.
- **Stereo.** True stereo I/O with auto mono/stereo detection: connect one input + both outputs for **mono-in→stereo-out**. This is the key fact for placement — see §5.

## 5. Signal-Chain Placement — Texture-Morph After Blooper, and Re-Stereo-izing

Board 3 reads: **Generation Loss → Big Time → MOOD MkII → Blooper (MONO) → Chroma Console → H90 → PORTA424 → 424 → Apollo/FOH.** Three things matter for the Chroma's exact slot:

1. **It re-expands the mono Blooper.** The Blooper immediately upstream is mono, so by the time signal reaches the Chroma the stereo field built across Boards 1–2 has collapsed to a point source. The Chroma — being true stereo with mono-in→stereo-out detection — is the rig's **first opportunity to rebuild a stereo image post-Blooper**. Effects that generate width (DOUBLER, the stereo-spread side of VIBRATO/PHASER DRIFT, SPACE reverb) fan the mono loop back out *before* the H90, which then preserves and processes that stereo field. Make sure both outputs are connected and the bypass mode preserves stereo (see §8 — True Bypass *defeats* the mono-to-stereo routing).
2. **It morphs textures, it does not re-degrade from scratch.** Per the Generation Loss labor split, the heavy tape character (wow/flutter/dropout/EQ color) is already stamped on the signal by Gen Loss at the *head* of Board 3. The Chroma's job five slots later is to **morph what's already there** — re-pitch a Blooper loop (PITCH/REVERSE), smear it (COLLAGE/REELS), filter it (FILTER/HOWL), or add a *different* flavor of grit (BROKEN/INTERFERENCE) than Gen Loss's cassette-EQ. **Tape-voice redundancy warning: do not run CASSETTE here heavy while Gen Loss is also on heavy tape** — you double the wow/flutter and the low end turns to mush. Pick one as "the tape." If Gen Loss owns the tape character for a song, let the Chroma do filter/pitch/space/drive instead; only lean on CASSETTE when Gen Loss is dialed back or off.
3. **It feeds the H90, not the print stage.** The Chroma's degraded/morphed stereo output is *ideal* fodder for H90 algorithms (CrushedHall, MangledVerb, Blackhole) — same logic as Gen Loss → H90, but now the H90 is processing a *texture-morphed* loop rather than a freshly-degraded source. The PORTA424 + JHS 424 stage downstream is the final cassette *print* of the whole bus; the Chroma is a mid-chain *effect*, not a mastering tape stage. If the overall mix gets too lo-fi, pull the Chroma's TEXTURE module toward FILTER (clean) or bypass it before touching the print stage.

**The full four-voice tape split (consistent with the Gen Loss dossier):** Deco V2 (Board 1) warms the source → **Generation Loss (Board 3 head) breaks the source** → **Chroma Console (Board 3 mid) morphs the textures** → PORTA424 + 424 (Board 3 tail) print the whole thing to cassette. Four tape voices, four jobs, minimal overlap — provided Chroma and Gen Loss aren't both on heavy tape at once.

## 6. Source-Specific Notes (banjo, baritone, modeled VG-800, bass)

By the time signal reaches the Chroma it has been through the *entire* front + middle + early-end chain, so it's no longer raw instrument — but the source character still bleeds through:

- **GK-5 banjo (EBM-5) via VG-800.** Banjo's bright, staccato attack survives a long way down a chain. The Chroma's **CASSETTE** and **FILTER (LPF)** roll off the residual top; **SWELL** (Character) or recorded **GESTURE** volume swells turn percussive banjo loops into bowed-sounding drones; **COLLAGE/REVERSE** on a banjo Blooper loop is the "banjo-as-lead, recorded-wrong" texture the rig is built around. Calibrate at **MEDIUM/HIGH** headroom (manual pg. 9) since the signal arriving here is processed and hot.
- **Baritone Jazzmaster.** Low-end mass means watch **SQUASH** and heavy **CASSETTE** (both can flub the lows). VHS-style destruction is better left to Gen Loss; use the Chroma here for **SPACE** reverb, **PHASER/VIBRATO** movement, or **HOWL** resonant stabs that cut through a baritone drone.
- **Modeled VG-800 signal.** Pad/COSM synth patches that have been degraded upstream become deep ambient beds; the Chroma's **DRIFT** + **COLLAGE** turns them into evolving clouds. Calibration's "Very High" headroom category explicitly lists "line level signals, modular" — relevant since VG-800 runs near line level (manual pg. 9).
- **Bass (Jazz bass).** Use sparingly and keep MIX low. Lean on **DOUBLER**/**SPACE** for width and size; keep **BROKEN**/**SQUASH** modest so the fundamental survives. Set calibration to the appropriate (lower-distortion) headroom.

## 7. Famous Users (honest)

Newer pedal, but real sightings exist. **Rhett Shull** runs it in his live rig (Premier Guitar Rig Rundown). **Yvette Young** has demoed it (Instagram). **Finn Wolfhard** has been seen using one onstage. **Matthew Followill (Kings of Leon)** had it on his board for an August 2025 show. **Ryan Lee West (Rival Consoles)** used one on his desk during "The Making of *Landscape from Memory*." Equipboard lists ~36 pro users ([Equipboard](https://equipboard.com/items/hologram-electronics-chroma-console)). *Unverified:* specific studio credits and "X uses it live" claims beyond Rig Rundowns are hard to confirm — treat skeptically. The pedal's real cultural footprint is the ambient/shoegaze/experimental scene that already adopted the Microcosm.

## 8. Live / Power / I/O

| Item | Detail |
|---|---|
| Power | 9V DC center-negative, 2.1mm; requires **≥500 mA** continuous (manual pg. 44) — a **heavy draw**, needs a high-current isolated slot |
| I/O | True stereo in / stereo out (1/4"); auto mono/stereo detection; **mono-in→stereo-out** via one input + both outputs |
| AD/DA | 24-bit / 48 kHz; max input **+8 dBu**; input impedance **1 MΩ**, output **<1 kΩ** (manual pg. 44) |
| MIDI | **5-pin DIN In/Out/Thru + USB-C**; clock sync; full CC/PC implementation (manual pg. 36–49) |
| Expression | TRS EXP jack, >10kΩ pot; maps to any one primary control (TILT/RATE/TIME/MIX/AMOUNT) (manual pg. 45) |
| Presets | **80 user presets** (4 banks × 20), recallable via PC; CAPTURE *not* saved |
| Bypass | Configurable: **Buffered**, **Buffered + trails**, or **True Bypass** (Global Settings) — **True Bypass defeats the auto mono↔stereo routing** (manual pg. 41) |
| Dual Bypass | BYPASS footswitch can be set to bypass *specific modules* instead of the whole pedal (manual pg. 28) |
| Dimensions | ~6.0 × 5.0 × 3.0 in per retailer listings ([Sound On Sound](https://www.soundonsound.com/reviews/hologram-electronics-chroma-console)); *exact mm not in manual — unverified* |
| Warranty | 2 years (manual pg. 50) |

**Live cautions:** (1) The **≥500 mA** draw is the headline — give it a dedicated high-current isolated output; do not daisy-chain. (2) For this rig, set bypass to **Buffered + trails** (or Buffered), **not True Bypass** — True Bypass kills the mono-Blooper→stereo re-expansion that's the Chroma's structural value here. (3) Preset switching is **clunky for live** (no dedicated preset footswitches; you scroll banks) — reviewers flag this consistently ([SOS](https://www.soundonsound.com/reviews/hologram-electronics-chroma-console), [Guitar.com](https://guitar.com/reviews/effects-pedal/hands-on-hologram-electronics-chroma-console-review/)). **Drive preset changes via MIDI Program Change** from the rig's MIDI brain instead. (4) Disable **Preset Browser Audition** (Global Settings) for live so the current preset persists while you scroll.

## 9. Pairing Recommendations (by name)

- **← CB Blooper (immediately upstream, MONO):** the Chroma is the **mono→stereo re-expander** for Blooper's loops. Capture/layer in Blooper, then let DOUBLER/SPACE/DRIFT fan it to stereo. This is the single most important adjacency on the board for the Chroma.
- **vs CB Generation Loss (Board 3 head):** **redundant if both run heavy tape.** Split the labor — Gen Loss = tape EQ/wow/dropout *at the source*; Chroma = a *different* job downstream (filter sweep, pitch/reverse, lo-fi space, drive, or BROKEN/INTERFERENCE glitch). **Never double CASSETTE-on-Chroma with heavy Gen Loss.**
- **vs Strymon Deco V2 (Board 1):** complementary, far apart in the chain — Deco warms the clean source; Chroma morphs already-processed loops. No conflict.
- **vs PORTA424 + JHS 424 (Board 3 tail):** complementary — those are the final cassette *bounce* of the whole bus; Chroma is a mid-chain effect. If too lo-fi, pull Chroma's TEXTURE toward FILTER before touching the print.
- **→ Eventide H90 (next):** the Chroma's morphed stereo output is excellent reverb/pitch fodder — CrushedHall / MangledVerb / Blackhole over a Chroma-smeared loop is a textbook doom-ambient move. MIDI-sync both.
- **vs Hologram Microcosm (Board 2, sibling):** by design *not* duplicative — Microcosm does granular/glitch looping mid-chain; Chroma does tape/lo-fi morphing on the End Board. Keep their jobs distinct (don't make both "the granular pedal").
- **MIDI scene recall:** with the rig's stack of MIDI pedals (the Chase Bliss line, Microcosm, H90), a single Program Change scene can recall a Chroma preset (effects + routing + gestures + filter style + dual-bypass + capture routing) alongside the rest. Map one Chroma preset per song scene.

## 10. Reviews & Demos (real links)

- [Sound On Sound — Chroma Console review](https://www.soundonsound.com/reviews/hologram-electronics-chroma-console) — best on DRIFT, the gesture/capture features, and honest criticisms (clunky preset switching, finicky sustainer).
- [Guitar.com — "the best user-friendly multi-effects?"](https://guitar.com/reviews/effects-pedal/hands-on-hologram-electronics-chroma-console-review/) — workflow-focused; strong on the menu-free design.
- [MusicRadar — "an effects suite for people who don't like multi-effects?"](https://www.musicradar.com/news/is-the-hologram-electronics-chroma-console-an-effects-suite-for-people-who-dont-like-multi-effects-pedals) — framing/context.
- [AltWire — "20 pedals in one"](https://altwire.net/chroma-console-by-hologram-electronics-review/) — module-by-module overview.
- [SineSquares — hands-on review](https://www.sinesquares.net/musicgear/hologram-electronics-chroma-console-review) — and their [Hologram founders interview](https://www.sinesquares.net/musicgear/hologram-electronics-interview-meet-the-creators).
- [Delicious Audio — Multi-Effector overview](https://delicious-audio.com/hologram-electronic-chroma-console-multi-effector/) — concise feature rundown.
- [Pedal of the Day — Chroma Console](https://www.pedal-of-the-day.com/2025/04/20/hologram-electronics-chroma-console-multi-effector/) — demo writeup.
- [Magnetic Mag — "favorite effects pedal this year"](https://magneticmag.com/2024/10/hologram-chroma-console-review-our-favorite-effects-pedal-and-units-this-year/) — synth/studio-leaning take.
- [Hologram official Chroma Console page](https://www.hologramelectronics.com/pages/chroma-console) — specs, demos, sound clips.

## 11. Mods / Quirks / Firmware

- **No user mods** — DSP pedal; "modding" = FX SETUP, Global Settings, and firmware. Behavior changes in software, not soldering.
- **Firmware v1.04 (May 5, 2025)** is current: faster preset loading, **MIDI CCs for module bypass/engage**, bug fixes ([firmware page](https://www.hologramelectronics.com/pages/chroma-console-firmware)). Update over USB-C via `firmware.hologramelectronics.com/chroma-console/` (cable + supply ship in the box). *Earlier changelogs not publicly detailed — unverified.*
- **Quirks (reviewer-confirmed):** preset switching is **clunky/impractical live** (no preset footswitches); the **sustainer-pad capture mode is finicky** and doesn't perfectly match the docs (SOS); **one effect per module** by design (you can't stack two effects from the same module). The CASSETTE/SQUASH effects can flub bass-heavy material.
- **Manual-vs-web flag:** Hologram product lineage — it's the company's **fourth pedal** (Dream Sequence → Infinite Jets → Microcosm → Chroma Console), not the "second." Dimensions appear only in retailer listings (~6×5×3 in), not the manual — **unverified** for exact mm/weight. Current draw "≥500 mA" is from the manual (pg. 44).

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Stereo digital multi-effect (drive / modulation / delay-reverb / lo-fi-tape), motion recorder + looper |
| Effects | **20** across **4 reorderable modules** (Character, Movement, Diffusion, Texture) |
| Power | 9V DC center-negative, 2.1mm, **≥500 mA** |
| Max voltage | 9V (do not exceed; out-of-spec supply may cause damage) |
| I/O | Stereo in / stereo out, 1/4"; auto mono/stereo; mono-in→stereo-out |
| AD/DA | 24-bit / 48 kHz; max input +8 dBu |
| Input / output impedance | 1 MΩ / <1 kΩ |
| Bypass | Buffered / Buffered + trails / True Bypass (selectable); True Bypass defeats mono↔stereo routing |
| Presets | 80 (4 banks × 20); recallable via MIDI PC; CAPTURE not saved |
| MIDI | 5-pin DIN In/Out/Thru + USB-C; clock sync; full CC/PC |
| Expression | TRS, >10kΩ; maps to any one primary control |
| Special features | GESTURE knob-motion recorder (clock-syncable), CAPTURE 30s looper/sustainer, DUAL BYPASS, configurable FILTER style |
| Firmware | v1.04 (May 5, 2025) |
| Dimensions | ~6.0 × 5.0 × 3.0 in (retailer listings; exact mm unverified) |
| Warranty | 2 years |

Source: manual (`ChromaConsole.pdf`, Firmware v1.04) + [Hologram product page](https://www.hologramelectronics.com/pages/chroma-console). Exact dimensions/weight not published in manual — **unverified**.

## 13. Starting-Point Settings

Clock-face positions, viewing the pedal from above. Build order is Character → Movement → Diffusion → Texture unless noted; bypass unused modules (hold their button).

**(a) Subtle tape glue** — nearly-always-on cohesion under a loop
- TEXTURE: **CASSETTE**, AMOUNT 9 · MOVEMENT: **VIBRATO**, RATE 9, AMOUNT 8, DRIFT 9 · others bypassed · MIX ~70%
- The lightest of the rig's tape voices. **Only use when Gen Loss is dialed back** — otherwise you double the wow. A whisper of CASSETTE + a hair of DRIFT-warbled vibrato = "recorded a while ago" glue.

**(b) Gestural motion swells** — bowed-drone from a percussive loop
- CHARACTER: **SWELL**, AMOUNT 12, SENSITIVITY to taste · DIFFUSION: **SPACE**, TIME 1 o'clock, AMOUNT 11 · Record a **GESTURE** on MIX or TILT, sync to tap tempo, speed it up · MIX ~60%
- Turns staccato banjo/baritone Blooper loops into evolving swells. The gesture is the "manual LFO" doing the work.

**(c) Lo-fi destruction** — broken, glitched, motorized
- TEXTURE: **BROKEN**, AMOUNT 1 o'clock · DIFFUSION: **COLLAGE**, TIME moving / automated, AMOUNT 12, DRIFT 1 o'clock · MOVEMENT: **PITCH**, AMOUNT to taste, DRIFT up · MIX 80–100%
- Chroma as the *primary* chaos engine **when Gen Loss is off/clean**. COLLAGE's destructive TIME edits + BROKEN's pitch drops = genuinely unpredictable; record it.

**(d) Ambient diffusion bed** — wide, dark, stereo wash that re-expands the mono Blooper
- DIFFUSION: **SPACE**, TIME 2 o'clock (big), AMOUNT 1 o'clock, DRIFT 11 · MOVEMENT: **DOUBLER**, RATE 11, AMOUNT 10 (stereo width) · TEXTURE: **FILTER (LPF)**, AMOUNT 1–2 o'clock (roll off highs) · MIX ~50%
- Fans the mono Blooper loop back to stereo *before* the H90. DOUBLER + SPACE build the width; LPF darkens it into a bed. Let H90 reverb sit on top.

## 14. Versus Alternatives — Why It Earns the Board-3 Slot

- **CB Generation Loss (in-rig, upstream)** — a tape *specialist* with real-machine EQ models + dropout/failure; Chroma has neither but adds drive, modulation, delay/reverb, glitch, and a motion recorder in one box. They're complementary by design — Gen Loss decides *how broken*, Chroma decides *what to do with it*. Don't double the tape.
- **Hologram Microcosm (in-rig, sibling)** — granular/glitch looper. Chroma is *not* a granular pedal; Hologram built it to coexist with Microcosm, not replace it. Different jobs, both kept.
- **Strymon Deco V2 / PORTA424 / 424 (in-rig tape voices)** — Deco warms the source at the front; PORTA424/424 print the bus at the end. Chroma is the *mid-end-board morpher* between them. No overlap once the labor is split.
- **Chase Bliss MOOD MkII / generic lo-fi multi-fx (Hungry Robot, Zvex Instant Lo-Fi, etc.)** — none combine **four reorderable color modules + a knob-motion recorder (GESTURE) + a 30s looper/sustainer (CAPTURE) + true stereo + full MIDI/preset recall** the way the Chroma does in one tactile, screen-free box.

In this rig — drone/doom/shoegaze, banjo-as-lead, a stereo End Board themed "Delay · Loop · Reverb · Print" — the Chroma Console earns its **5th-on-Board-3 slot** for three reasons no other pedal here covers at once: (1) it's the **first true-stereo box after the mono Blooper**, so it rebuilds the stereo image the H90 then preserves; (2) it's a **multi-character texture-morpher** that does *everything Gen Loss doesn't* (drive, modulation, pitch/reverse, glitch, motion automation) on already-degraded loops; and (3) it's a **MIDI/preset citizen** with a clock-syncable GESTURE recorder, so evolving textures scene-recall in lockstep with the rest of the board. Gen Loss breaks the source, Chroma morphs the textures, PORTA424/424 print the whole thing — and the Chroma owns the job of turning a mono loop into a moving, broken, stereo texture before it hits the reverbs.

## Sources

- Manual: `manuals/ChromaConsole.pdf` (Firmware v1.04) — on disk, authoritative for module/effect names and I/O specs.
- [Hologram Electronics — Chroma Console product page](https://www.hologramelectronics.com/pages/chroma-console)
- [Hologram Electronics — Chroma Console firmware page (v1.04)](https://www.hologramelectronics.com/pages/chroma-console-firmware)
- [Hologram Electronics — Microcosm product page](https://www.hologramelectronics.com/products/microcosm)
- [Equipboard — Hologram Electronics brand page (founders, lineage)](https://equipboard.com/brands/hologram-electronics)
- [Equipboard — Chroma Console (users / where to buy)](https://equipboard.com/items/hologram-electronics-chroma-console)
- [Sonicstate — Hologram Chroma Console Now Shipping (April 2024)](https://sonicstate.com/news/2024/04/03/hologram-chroma-console-now-shipping/)
- [Premier Guitar — Hologram Chroma Console unveiled](https://www.premierguitar.com/news/hologram-effects-chroma-console)
- [Sound On Sound — Chroma Console review](https://www.soundonsound.com/reviews/hologram-electronics-chroma-console)
- [Guitar.com — Chroma Console review](https://guitar.com/reviews/effects-pedal/hands-on-hologram-electronics-chroma-console-review/)
- [MusicRadar — Chroma Console "effects suite" feature](https://www.musicradar.com/news/is-the-hologram-electronics-chroma-console-an-effects-suite-for-people-who-dont-like-multi-effects-pedals)
- [AltWire — Chroma Console review](https://altwire.net/chroma-console-by-hologram-electronics-review/)
- [SineSquares — Chroma Console hands-on review](https://www.sinesquares.net/musicgear/hologram-electronics-chroma-console-review)
- [SineSquares — Hologram founders interview](https://www.sinesquares.net/musicgear/hologram-electronics-interview-meet-the-creators)
- [Delicious Audio — Chroma Console Multi-Effector](https://delicious-audio.com/hologram-electronic-chroma-console-multi-effector/)
- [Pedal of the Day — Chroma Console](https://www.pedal-of-the-day.com/2025/04/20/hologram-electronics-chroma-console-multi-effector/)
- [Magnetic Mag — Chroma Console review](https://magneticmag.com/2024/10/hologram-chroma-console-review-our-favorite-effects-pedal-and-units-this-year/)
- [VI-Control — Chroma Console vs Microcosm discussion](https://vi-control.net/community/threads/hologram-chroma-console-similar-to-microcosm-pedal.145458/)
