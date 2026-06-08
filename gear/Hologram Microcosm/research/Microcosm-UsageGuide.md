# Hologram Microcosm — Usage Guide

The Microcosm is the Texture board's **granular sequencer / looper / ambient engine** — a
"probability-driven granular sequencer" more than a delay pedal. You get the most out of it
by (1) learning what **Activity / Time / Repeats** do *per engine* (they change meaning in
every category), (2) using the **Hold-Sampler** to freeze a moment into a drone and twisting
parameters over the frozen bed, and (3) **clock-syncing it to the Digitakt** so the rhythmic
engines lock instead of running wild. Feed it the **Board 1 fuzz wall** and it becomes a
self-evolving texture machine. Notably, **Ed O'Brien (Radiohead) runs his Microcosm right
beside a Chroma Console** on his 2025 board — the same pairing in this rig.

> Firmware note: the latest Microcosm firmware is **v1.13 (May 2022)** — there is **no
> "version 2.0"** (Hologram's newer effort became the separate Chroma Console). Don't chase a
> 2.0. Verify your build in Global Config (hold Shift + Phrase Looper ~2 s, tap Reverse ×3;
> v1.13 = Mosaic + Haze + Tunnel + Strum LEDs lit). *(firmware-version-check)*

---

## 1. Essential workflows

### The knob mental model
**Activity / Time / Repeats = "what the effect does"** (Activity = more of it; Time = rate, can
sync to MIDI clock; Repeats = feedback-like). **Shape / Filter / Space = "how it blends"**
(Shape is a 4-position envelope switch — saw/triangle/ramp/square; Filter open fully CW; Space
= reverb). **Reverse = press the selector knob in** (easy to forget). *(jorb, starsky-carr)*

### Engines, by what Activity does in each (the practical map)
*(whirrings — the all-44-algorithms reference)*
- **Micro Loop — Mosaic:** Activity = number of active loopers (A oct-up, B oct-down, C all
  ×2, D −1 to +2 oct). **Seq:** filter-shuffle / octave-bounce (B reveals a sustainer pad
  when a knob is fully CW) / bit-crush (D adds a sub-octave layer fully CW). **Glide:** Activity
  = pitch-shift rate, Shape = glide pattern.
- **Granules — Haze:** Activity = grain density/spread. **Tunnel** (the drone engine): A =
  sample-length LFO, B = sub-octave, C = resonant bandpass (watch the resonance), D = noisier
  envelope LFO. **Strum:** A repeats the most-recent note, B phasing/cascading chains.
- **Glitch — Blocks / Interrupt / Arp:** A basic, B pitch-shift, C filter, **D bit-crush**;
  Interrupt's **Repeats = how often glitches fire**; Arp's Activity = number of steps.
- **Multidelay — Pattern / Warp:** Pattern A = linear delay, B–D rhythmic (Activity = active
  taps); Warp A env-filter, C pitch-per-tap, **D crossfade w/ double-speed grains**.

### The Hold-Sampler drone (the headline rig technique)
Hit **Hold** to freeze the current wet segment (it keeps feeding the FX) → **scroll the A/B/C/D
sub-modes over the frozen bed to stack octave ranges** → roll **Filter** back for less top end
without changing modes → keep twisting **Activity and Time live** (fast Time = choppy). Pull
**Mix back** and your dry signal passes through unaffected, so you can **play a fresh lead over
the frozen drone**. Toggle is default; momentary is set in Global Config. **Engine changes the
result:** Tunnel B under Hold sustains only the *most recent* sample; Arp A arpeggiates
*multiple* buffered notes; Blocks → pad, Mosaic → looped cluster. *(andy-othling-hold-drone, hologram-hold-sampler, deliciousaudio)*

### The looper
Record = red, stop/loop = green, next layer = yellow; **erase = hold the Hold button**;
**Reverse** reverses the recording. **Pre-FX routing** (loop dry, then apply one FX set to the
whole loop): looper mode → hold looper button → "Pre-FX" lights → push selector → push looper
again (default post-FX prints the effect into each layer). No feedback knob — **oldest overdubs
self-fade** as you stack (intended "auto-feedback"). **Burst** (CC 26): left footswitch records
only while held, for glitch stabs. *(worship-guitar-lab, hologram-looper, microcosm-five-effects)*

---

## 2. Signature presets & settings

**First, the big constraint:** the Microcosm has **NO preset file format and no SysEx dump** —
SysEx is firmware-only. Presets live **on-device only** (16 slots / 4 color banks: Red/Yellow/
Green/Blue), are **wiped by factory reset**, and "sharing a preset" = **publishing the recipe**
(engine + variation + knob clock-positions + Global Config) to dial by hand. Back up your slots
by photographing the panel + writing down positions. Recall the 16 slots over MIDI via **PC
#45–60**. The one commercial pack (**The Tone Shepherd**, $19.99, 6 presets) is a recipe sheet,
not a file. *(presets-banks-and-management, tone-shepherd)*

**Concrete engine → setting recipes** (real, from demos — dial by ear):
- **Ambient bed (Andy Othling):** **Mosaic D, ±2 octaves, very long Time, Mix ~2 o'clock** for
  unity (noon does *not* read as 50/50 to the ear). *(andy-othling-generative)*
- **Seasick pitch-drift drone:** **Glide A + Shape = triangle + very slow subdivision** — great
  on a baritone drone. *(reverb-nine-odd-sounds)*
- **Diffuse smeared wash:** **Haze A + Reverse + slowed playback speed** from a sustained source.
- **Dark onset-chains:** **Strum B**, speed knob down an octave (Strum D cascades). 
- **Rhythmic arps from plucks:** **Arp B + Shape = square + 4× tempo.**
- **Frozen single-sample drone:** **Tunnel B under Hold Sampler** sustains only the latest
  sample regardless of Activity. *(reverb-nine-odd-sounds, deliciousaudio)*

---

## 3. Power-user tips, tricks & hidden features

- **Effect Volume = the level-match fix:** **Shift + MIX** (MIDI **CC 16**) sets the wet master
  output independent of dry/wet — use it so the pedal doesn't jump in level when a hot fuzz wall
  engages it. *(microcosm-hidden-controls)*
- **For smooth sweeps use the EXP jack or MIDI CC, not the knobs** — the encoders read in coarse
  steps. *(elektronauts-megathread)*
- **CC 48 = remote Freeze/Hold** — trigger/release the freeze from the Digitakt or a Morningstar
  on a downbeat, no footswitch. CC map: **Activity 6, Filter 8, Time 10, Repeats 11, Space 12,
  Effect Vol 16, Freeze 48, Burst 26.** *(midiguide-cc-pc-map)*
- **EXP-to-Filter generative trick (Andy Othling):** assign a slow ramper to **Filter** at full
  Mix so it "opens for the twinkles, then filters itself out" — a hands-free self-modulating bed.
  *(andy-othling-generative)*
- **Global Config secondaries:** **Activity = mono/stereo input**, **Mix = instrument/line
  level** (wrong level "just sounds rubbish"), **Space = bypass mode** (buffered + trails
  recommended — a hard cut sounds abrupt on so active a pedal). *(worship-guitar-lab, microcosm-hidden-controls)*
- **Looper auto-feedback** (oldest layers self-fade) + **Burst mode** for held-only glitch
  recording. *(hologram-looper)*

---

## 4. Notable users & techniques

- **Ed O'Brien (Radiohead)** — VERIFIED: Microcosm on his **2025 touring "Pitch and Glitch"
  ambient board, beside the Chroma Console** (the exact pairing in this rig), as a textural
  layer from his solo material. Settings not published. *(ed-obrien-radiohead-2025)*
- **Sean Shibe** — classical guitarist; uses the Microcosm across *Lost & Found* (full-wet,
  self-standing washes). *Track attribution is uncertain:* the dossier ties it to a Hildegard
  von Bingen reinterpretation; another source ties it to the gong intro of Julius Eastman's
  "Buddha." The album contains both pieces — treat the specific-track link as unconfirmed.
  *(sean-shibe-lost-and-found)*
- **Toto Ronzulli (Truemantic)** — runs **Particle → Microcosm → Eventide Space** as a full
  ambient chain (mirrors this rig's granular→smear→space division). *(martin-yam-moller)*
- **TJ Dumser (Six Missing)** — record into the looper, set routing **Pre-FX**, then twist live
  engines to **re-granulate the recorded loop** — bed-building without a second pedal. *(martin-yam-moller)*
- **Andy Othling (Lowercase Noises)** — the ambient-guitar reference for the Hold-drone and
  EXP-filter generative techniques above. *(andy-othling-hold-drone)*

---

## 5. Rig-specific recipes (using gear actually owned)

- **Feed it the Board 1 fuzz wall:** run the Hizumitas/Longsword wall into the Microcosm at
  **Mix 100%** on **Glitch or Tunnel** and "lock onto the pedal's pulse" — sustained fuzz becomes
  a self-evolving granular texture. Use **Effect Volume (Shift+MIX / CC 16)** to match levels so
  it doesn't jump. *(microcosm-five-effects, microcosm-hidden-controls)*
- **Hold-drone + banjo lead:** freeze a baritone/fuzz bed with Hold, pull **Mix** back, and play
  the banjo as a dry lead over the frozen drone — fits "banjo-as-lead / sustained walls." *(andy-othling-hold-drone)*
- **Self-modulating generative bed:** EXP ramper → **Filter**, Mix high, Mosaic D ±2 oct + long
  Time → a hands-free evolving pad to print to the Apollo. *(andy-othling-generative)*
- **Clock from the Digitakt (rig-critical wiring):** feed the Microcosm **directly from Digitakt
  MIDI OUT** (its THRU only echoes what hits its own IN, so don't route clock *through* another
  synth's THRU), enable the Digitakt's **Transport/Start** (the Microcosm only syncs after a
  Start), and daisy-chain other slaves off the **Microcosm's OUT** (it echoes incoming MIDI).
  Note: while slaved to clock, **CC 10 (Time) stops responding** — turn Clock Send off if you
  want to hand-modulate Time. *(elektronauts-digitakt-clock, youtube-digitakt-cc-modulation)*
- **Place in chain:** Middle/Texture board — after Board 1 fuzz, before the End board's
  TimeLine/Big Sky/H90 → tape. Run **Stereo Input ON** and set **line level** in Global Config
  (the VG-800 output is line-level). *(worship-guitar-lab)*
- **The Ed O'Brien move:** pair the Microcosm with the **Chroma Console** for layered pitch-and-
  glitch texture, as he does live. *(ed-obrien-radiohead-2025)*

---

## 6. Best learning resources

- **WHIRRINGS** — the definitive engine-by-engine reference (all 44 algorithms); sells a printed
  cheat-card. Watch first for the algorithm map.
- **Jorb** — best conceptual "what every knob does in any mode" mental model.
- **Starsky Carr** — synth/producer "demystified" angle; strong on the Shift secondary functions.
- **Worship Guitar Lab** — the operational video manual (looper routing, preset saving, Global
  Config, trails).
- **Andy Othling (Lowercase Noises)** — the on-aesthetic ambient artist (Hold-drone, generative
  EXP-filter).
- **Communities:** Elektronauts "Microcosm | Hologram Electronics" megathread (deepest, esp. on
  Elektron clock behavior), the "Digitakt + Microcosm clock issue" thread (the THRU lesson),
  Morningstar forum (MIDI control), **midi.guide** (verified CC/PC map). *(whirrings, jorb, starsky-carr, worship-guitar-lab, andy-othling, elektronauts-megathread, morningstar, midiguide)*

---

## 7. Common pitfalls / gotchas

- **No preset file format / no SysEx backup** — presets are on-device only and die on factory
  reset; back up by writing down recipes. *(presets-banks-and-management)*
- **No firmware "2.0"** — v1.13 is the latest; don't chase non-existent features. *(firmware-version-check)*
- **MIDI clock THRU trap** — feed clock *directly* from Digitakt OUT, not through another synth's
  THRU; the slave only follows after a **Start** command (enable Transport). *(elektronauts-digitakt-clock)*
- **Clock-sync OR CC-modulate Time, not both** — slaving to clock disables CC 10. *(youtube-digitakt-cc-modulation)*
- **Quantized loops drift** ~a 16th/minute on external clock — re-trigger long beds rather than
  free-run. **Loop-transition pops** persist; community fix = factory reset after a firmware
  update. *(elektronauts-megathread)*
- **Coarse encoders** — use EXP/MIDI for smooth parameter motion. *(elektronauts-megathread)*
- **EXP "dead pedal" trap** — a pedal plugged in at power-on auto-binds to **Filter, heel-down =
  filter closed = no wet**; looks broken, just toe-down or reassign. *(microcosm-hidden-controls)*
- **PC→CC timing** — a CC fired at the same instant as a Program Change is swallowed while the
  engine loads; stagger by ~100–500 ms. *(morningstar)*
- **Level matching** — set the correct instrument/line level in Global Config and use Effect
  Volume so a hot fuzz upstream doesn't make it jump. *(worship-guitar-lab, microcosm-hidden-controls)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `whirrings-microcosm-44-algorithms-walkthrough.md` — full engine-by-engine reference (all 44) + RC600 clock sync
- `jorb-microcosm-how-to-actually-use.md` — conceptual knob/mode mental model
- `starsky-carr-microcosm-demystified.md` — "granular sequencer" framing + Shift secondaries
- `worship-guitar-lab-microcosm-video-manual.md` — looper (pre-FX), preset saving, Global Config, trails
- `andy-othling-microcosm-hold-drone-technique.md` — the Hold→freeze→evolve drone workflow
- `andy-othling-microcosm-generative-loop-deconstruction.md` — Mosaic-D ambient bed, EXP-ramped Filter
- `hologram-official-hold-sampler-overview.md` — official Hold Sampler walkthrough
- `microcosm-how-to-be-advanced-five-new-effects.md` — 5 advanced effect-design techniques
- `reverb-nine-odd-sounds-into-microcosm.md` — 9 sources → specific engine+mode+settings
- `youtube-microcosm-master-clock-midi-out-setup.md` — exact steps to enable Microcosm MIDI clock out
- `youtube-microcosm-digitakt-cc-modulation-workflow.md` — Digitakt LFOs → Microcosm CCs; clock-vs-CC-Time tradeoff
- `youtube-microcosm-looping-prepost-reverse-feedback.md` — official pre/post-FX mental model + auto-feedback

**Links** (`research/links/`)
- `midiguide-microcosm-cc-pc-map.md` — verified full CC + PC map
- `elektronauts-microcosm-digitakt-clock-thru-gotcha.md` — the THRU-vs-OUT clock failure + fix
- `elektronauts-microcosm-megathread-tips-gotchas.md` — clock drift, start/stop, pop fix, encoders
- `morningstar-microcosm-midi-control-threads.md` — PC→CC timing, expression-over-MIDI, preset scrolling
- `deliciousaudio-microcosm-hold-sampler-arp-granules.md` — Hold-then-twist; Blocks=drone/Mosaic=loop
- `hologram-microcosm-firmware-version-check.md` — no-"2.0" confirmation + version-check trick
- `hologram-microcosm-looper-prepost-reverse-burst.md` — looper routing, reverse, burst, auto-feedback
- `microcosm-hidden-controls-exp-effectvolume-config.md` — effect-volume secondary, EXP trap, Global Config
- `microcosm-presets-banks-and-management.md` — 16 slots/4 banks, no-SysEx-sharing, PC map
- `tone-shepherd-microcosm-preset-pack.md` — the one commercial pack (recipe sheet, not file)
- `ed-obrien-radiohead-2025-microcosm.md` — verified 2025 board placement (beside Chroma Console)
- `sean-shibe-lost-and-found-microcosm.md` — Shibe's full-wet use (track attribution uncertain)
- `martin-yam-moller-microcosm-artist-interviews.md` — Truemantic / Six Missing / Aqeel Phillips techniques

## Sources

Video (YouTube): WHIRRINGS `9_9kY5jVIKM` · Jorb `VamR0i5HIvI` · Starsky Carr `42cVBk8tuJw` ·
Worship Guitar Lab `7qlT0MxLOto` · Andy Othling `E90ArJBEKTM`, `qkOYRXs49lY` · Hologram
`9dE6f16Z1Lg`, `MnSR022Biig` · Reverb `-WTCWLztwQY` · master-clock `9M1ysTqGGK0` · Digitakt CC
`dKsp6xwjLXc` · looping `czENIgW9l_k`.
Community: elektronauts.com (Microcosm megathread t/121669, Digitakt clock t/193212) ·
forum.morningstar.io · midi.guide/d/hologram/microcosm · modwiggler.com (403, not captured).
Presets/artists: hologramelectronics.com (manual, firmware, looper) · thetoneshepherd.com ·
thekingofgear.com (Ed O'Brien) · prestomusic.com / pentatonemusic.com / artmuselondon.com
(Sean Shibe) · martinyammoller.com.
