# SketchCassette II — Usage Guide

SketchCassette II is the **in-the-box answer to the tape-pedal sound** — a
4-track-cassette degradation plugin that lives **per-track / per-stem** (never on
the master). For this rig it's the recallable, automatable degrade that
*complements* the hardware Big Time / Generation Loss: real-time wobble you play
*into* on the way in (pedals), recallable artifacts you dial *after the fact* on
stems (this). The whole community is unusually unanimous: per-track character
box, not a 2-bus strap.

## 1. Essential workflows (the core moves)

- **Per-track / per-stem insert.** Drop it on a single drone layer, banjo/baritone
  stem, or texture aux — "make *this track* sound very old," not the whole mix. `research/links/kvr-tapetown-cpu-and-gotchas.md`, `research/transcripts/plugin-boutique.md`
- **Automate the (gain-compensated) Saturation** to swell grit into a drone over a
  long section without level jumps — the one knob you can ride hard. `research/transcripts/jimijaymes.md`
- **Tempo-synced Wow as a rhythmic device** — sync Wow/Flutter to note values,
  Sine shape, use the **Offset** knobs to align the pitch-slur to the beat (a
  pad/piano that slurs in time). `research/transcripts/jimijaymes.md`
- **Ghost-tape layer** (works around the missing global wet/dry): duplicate the
  source, put a *second* SketchCassette at extreme settings low under the main
  sound = artifacts haunting a sustained bed. `research/links/theatre-of-noise-three-plugins.md`
- **Hiss-only texture track:** one empty track with just the noise setting = a
  subtle tape-ambience floor under the wall. `research/links/kvr-tapetown-cpu-and-gotchas.md`

## 2. Signature settings & presets (copyable)

**Controls map** (source of truth = the official manual): `research/links/manual-sketchcassette-ii.md`
- **Tape Type** — 12 profiles: formulation **Type I (Ferric)** = good lows/rolled
  highs (grimiest); **Type II (Chrome)** = pushed highs/thinner lows (a KVR pro's
  "most authentic"); **Type IV (Metal)** = flattest/most extended but rolls off
  some lows; + a filter-bypass button. Quality **Cheap→Value→Standard→Master** =
  progressively more high-end. Auto gain-compensated.
- **Age** — *the master degradation knob* (continuous HF roll-off, New→Worn);
  pairs with Dropouts for realism.
- **Saturation** — **Type A** gentle/darker · **Type B** harsher/brighter (near
  digital, "crushes the low end"); gain-compensated. Push **Input** for a *second*
  saturation/compression stage before this knob even moves.
- **Dropouts** — Depth (strength) + Intensity (longer periodic drops) + **Width**
  (full-left = mono-safe; right = independent L/R, tremolo-like).
- **Wow + Flutter** — Wow = slow pitch mod (~0.02–5 cps), Flutter = fast (~5–12
  cps). Shapes: **random** (most realistic), sine (vibrato, use when synced),
  smoothed/reverse saw (pulses). **Tempo-sync + Offset**, a **Flanging** blend
  knob, and **FM mode** (Wow modulates Flutter rate = sticky capstan / dying
  battery).
- **NR Comp** — emulated Dolby encode/decode mismatch = a **brightness/air** tool
  (Brightness + Amount); the **Comp Mix** knob runs it as a parallel compressor.
- **Hiss** (−96→−30 dB; defaults OFF in II) · **two Mix knobs** (Tape filter +
  Comp) — there is **no single global dry/wet**. `research/transcripts/jimijaymes.md`, `research/transcripts/mrdifferent.md`

**Named recipes (copyable):** `research/transcripts/stock-music-musician.md`, `research/transcripts/jimijaymes.md`
- *Blown-out garage drums:* avg-quality tape, boost Saturation, slight Age, NR
  Comp parallel ~52–66% wet, no wow/flutter.
- *Worn rhythm guitar:* Type-worn old tape, push Input for "tapiness," fair
  Saturation. Double-track partner on Type IV Standard for bite.
- *Lead guitar (come-alive):* heavy Saturation + lo-fi + lots of Wow/Flutter +
  lots of Dropouts.
- *"Dolby A" vocal trick:* Type I + NR Comp for in-your-face breathy intimacy
  (jimijaymes' favorite).
- *Most-realistic:* "pick a tape, turn up **Input**, prefer **Chrome (Type II)**." `research/links/kvr-most-realistic-cassette-thread.md`

**Two named user presets (Zed Marty), with values:** `research/transcripts/zed-marty.md`
- *Old Cassette* — Type I Standard, light Age/Hiss/Saturation, some Dropouts, a
  little Wow/Flutter, NR Comp ~50%.
- *Master Cassette* — Type IV Master, slight Age/Saturation, no Hiss, a little NR
  Comp (run ~50% mix on a bus).

**Degraded-drone targets** (named sound → controls):
- *Subtle warble* → Type II/IV Standard, low Age, small slow sine Wow, Mix ~50%.
- *Broken/warped cassette* → Type I Cheap, high Age, random Wow + Flutter,
  Dropouts depth+intensity up, mono Width.
- *Dictaphone/answering-machine* → Type I Cheap, Age high, Saturation B, moderate
  Dropouts, NR off.
- *Worn tape bed* → Type I Value, Age near-max, Hiss in, light random Flutter, NR
  off.

## 3. Power-user tips, tricks & hidden features

- **In/Out gain = a second saturation stage** — drive Input for more tape
  compression before touching the Saturation knob. `research/transcripts/jimijaymes.md`
- **Flanging-on-a-pad** is a standout: drop the whole instance with the Flanging
  knob up onto a sustained pad = watery throwback texture (exactly the drone use). `research/links/theatre-of-noise-three-plugins.md`
- **NR Comp to claw back highs** on an over-dark Type-I-Cheap/worn setting; its
  Comp Mix makes it a parallel "gloss" compressor (~50% on vocals/synths). `research/transcripts/jimijaymes.md`
- **v2 QoL:** Hiss now defaults OFF; keep it off while producing, enable only for
  the final bounce (or gate after it so it mutes in silence). **Double-click any
  param = reset to default** (itself a clean tape-sat starting point). `research/transcripts/mrdifferent.md`
- **Step the 61 factory presets** as starting points — the original had none. `research/transcripts/mrdifferent.md`

## 4. Notable users & techniques (sourced, honest)

- **Colin Dupuis** — mix engineer (Angel Olsen, Lana Del Rey, Yves Tumor),
  featured on Aberrant's own product page (vendor association HIGH; specific-quote
  MEDIUM). The closest documented *pro* to this rig's indie/dream-pop/degraded
  aesthetic; uses it as selective per-track color. `research/links/artists-sourced-colin-dupuis.md`
- **Genre class (sourced as a class, not named):** bedroom-pop, lo-fi hip-hop,
  chillwave, synthwave — on vocals/drums/synths/guitars.
- **Honest gap:** no verifiable *named ambient/drone artist* uses SketchCassette
  specifically (that scene names hardware tape / ChowTape). None invented — treat
  any such claim with suspicion. `research/links/artists-sourced-colin-dupuis.md`

## 5. Rig-specific recipes (your gear by name)

- **vs the hardware tape pedals (Big Time / Generation Loss):** use the **pedals
  live / on the way in** (real-time wobble you play into, committed to the
  recording); use **SketchCassette in-the-box, after the fact, on stems** for
  recallable/automatable degrade (tempo-synced wow as rhythm, automated dropouts,
  parallel NR-comp brightness). **Don't double-degrade the same wow/flutter on
  both** or it turns to mush — pick hardware *or* software per layer. `research/links/theatre-of-noise-three-plugins.md`
- **vs XLN RC-20 (also owned):** different jobs, not stacked. SketchCassette =
  realistic tape *distortion + wow/flutter* specialist; RC-20 = a 6-module lo-fi
  *suite* with built-in reverb (Space) + a global Magnitude wet/dry. Reach for
  RC-20 for overt/cartoon destruction or its reverb; SketchCassette for authentic
  cassette character. `research/transcripts/retro-plugin-showdown-vinyl-sc-rc20.md`, `research/links/kvr-most-realistic-cassette-thread.md`
- **In Logic:** **automate the Dropout** so it hits only at chosen moments (not
  constant random); **freeze/commit** heavy or multiple instances before tracking
  over them (latency, below). On banjo/baritone drone stems, Type I worn + random
  Wow + NR-comp brightness = the signature "found in the dirt" lead. `research/links/theatre-of-noise-three-plugins.md`

## 6. Best learning resources

1. **JimijaymesGuitarist (38 min)** — deepest; every control + source-by-source
   recipes + the two real limits (no master volume; synced-Wow won't go slow
   enough for long drone sections). Guitar-centric → best rig fit.
2. **Plugin Boutique "Unofficial Video Manual" (Joshua Casper, 14 min)** —
   cleanest full control walkthrough.
3. **Stock Music Musician (22 min)** — A/B mix demos + per-instrument settings +
   the latency/PDC gotcha.
4. **Zed Marty (18 min)** — two named presets with values.
5. **MrDifferentTV (13 min)** — best v1-vs-v2 "what's new."
6. **KVR Aberrant DSP threads / Tapetown guide / Theatre of Noise** — realism
   comparisons + ambient-specific hacks.

## 7. Common pitfalls / gotchas

- **Master-bus overuse** — the #1 warning across every source; per-track/aux only
  (even minimal settings cause issues across a whole mix). `research/links/kvr-tapetown-cpu-and-gotchas.md`
- **Send/parallel latency** — significant reported latency as a send/parallel and
  with several instances; DAW PDC didn't fully fix it. Prefer it as an **insert**;
  if on an aux, check timing/nudge and **freeze/bounce** before overdubbing. (CPU
  itself is low — this is latency, not load.) `research/transcripts/stock-music-musician.md`
- **No global dry/wet & no hiss envelope** — only Tape-filter + Comp Mix knobs;
  use a parallel/duplicate track (the ghost-tape hack) for overall blend.
- **NR Comp over-hypes highs / thins lows** at extremes — back off its Mix.
- **Preset system has had host-dependent quirks** — save to the plugin's **User**
  bank if host-menu presets misbehave. **AU/VST3/AAX only (no VST2)** — fine for
  Logic + Live 12. `research/links/kvr-tapetown-cpu-and-gotchas.md`

## 8. Captured sources

**Transcripts (6)** — `research/transcripts/`: jimijaymes (38-min deep dive) ·
plugin-boutique (video manual) · stock-music-musician (per-instrument + latency) ·
zed-marty (two named presets) · mrdifferent (v1-vs-v2) ·
retro-plugin-showdown-vinyl-sc-rc20 (vs RC-20/Vinyl).

**Links (6)** — `research/links/`: manual-sketchcassette-ii (authoritative
parameter reference) · theatre-of-noise-three-plugins (ambient hacks:
automate-dropout, ghost-tape, no-global-wet workaround) · kvr-most-realistic-
cassette-thread (realism vs RC-20/Nebula/ChowTape) · kvr-tapetown-cpu-and-gotchas
(source-by-source settings + CPU + preset gotcha) · whippedcream-review-martin-
glover (Age as the crucial knob) · artists-sourced-colin-dupuis (the one sourced
pro + honesty gap).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: Aberrant DSP manual/site,
JimijaymesGuitarist, Plugin Boutique (Joshua Casper), Stock Music Musician, Zed
Marty, MrDifferentTV, KVR Audio, Theatre of Noise, Tape Op (Larry Crane).
**Honesty flags:** boutique $20–36 plugin → community depth is thinner than a
Soundtoys-tier product; no named drone/ambient artist verified (only Colin Dupuis
+ a genre class); no third-party preset packs found.
