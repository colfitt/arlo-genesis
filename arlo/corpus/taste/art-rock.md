---
title: Art-rock / studio-as-instrument — Cluster Index (Track B1)
cluster: art-rock-studio-as-instrument
anchors: [Radiohead, Talking Heads, David Bowie]
focus_artist: Radiohead
focus_songs: ["Let Down", "Ful Stop", "Daydreaming", "Kid A era"]
generated: 2026-06-14
derived_patches: 23
documented_green: 0
emulated_purple: 23
lens: Research/Taste-Profile/taste-profile.md
tags: [taste-profile, track-b, radiohead, art-rock, reverse, glitch, jangle-delay, drone]
---

# Art-rock / studio-as-instrument — Radiohead cluster index

> **What this is.** The cross-rig view of every patch derived this wave from the Radiohead
> (art-rock) lens, anchored on the user's currently-tracked songs **"Let Down"** and **"Ful Stop"**
> plus signature Radiohead textures (reverse/looped delays, Ondes-Martenot leads, modulated wash,
> tape flutter, glitch/stutter, Kid A loop textures). Patches that live on a Wave-1 gear sheet are
> appended there too (single source of truth); patches for gear without a sheet yet are documented
> **here only**.
>
> **Provenance honesty (the headline).** **Every patch is 🟣 designed-to-emulate.** Radiohead's
> actual methods are Max/MSP patches, an EHX 45000 looper, tape splicing, and a roomful of
> polysynths — **none of the user's Chase Bliss / time gear was ever used by Radiohead, and no
> artist setting exists for any of it.** So there are **0 🟢 documented settings and 23 🟣
> emulations** — by design, and flagged honestly per the lens. The Refs name the real Radiohead
> sound/record each patch chases; the *settings* are first-principles from each unit's manual +
> the cited sources. No artist attribution is fabricated.

## How Radiohead actually get these sounds (research summary)

Captured to `Research/Taste-Profile/sources/`:

- **Reverse delays** are not a pedal mode — they're **captured-then-reversed samples**. Jonny's
  reversed guitar (Backdrifts) = a Max/MSP patch; Thom's Daydreaming reverse = he samples ringing
  glockenspiel notes on an **EHX 45000** and reverses them so each "gently fades in."
  (`kingofgear-jonny-reverse-delay-backdrifts.md`, `kingofgear-thom-looping-daydreaming.md`)
- **Glitch/stutter** (Go To Sleep, There There) = Jonny's **randomized-stutter Max/MSP patch**: a
  random generator loops chunks of audio for "x" time; folded in via a **Boss LS-2** first in the
  chain. The Feral Glitch pedal (by the King of Gear) recreates it: random/fixed mode, kill-dry
  toggle, time + volume knobs. (`musicradar-feral-glitch-greenwood-stutter.md`)
- **"Let Down" jangle** = Jonny's cascading Telecaster arpeggio **doubled an octave higher**, then
  **a third Jazzmaster layer** — a Phil-Spector wall built from one line — with the arpeggio in
  **5 against the 4/4** (Steve Reich phasing), recorded in the St Catherine's ballroom at 3am for
  its "supernatural" natural reverb. Outro = a dying ZX Spectrum's random in-key bleeps.
  (`poeticwax-let-down-wall-of-sound.md`)
- **"Ful Stop" wash** = **multiple synths playing single notes in unison, each voiced differently**
  (Moog Voyager + Prophet 5 + Juno-60 + Prophet '08) — the **pitch/envelope DRIFT between voices is
  the sound**. The "good phasing arpeggios" = EHX Small Stone → **Boss RE-20 Space Echo** under the
  wash. (`ful-stop-synth-wash-phasing-arpeggios.md`)
- **Ondes-Martenot leads** (Kid A) = a ribbon for **seamless pitch glides** + an **intensity key
  that shapes attack/decay like a violin bow** — "an instrument like singing." Polysynth roster is
  Prophet-dominated; the filter is the signature. (`kingofgear-radiohead-synths-ondes.md`)
- **Kid A method** = "loops mistreated, stretched, **pulled out of phase… everything breathes wrong
  on purpose**"; Ed cut up Thom's Rhodes in real time over loops; granular breaks, artifacts left
  uncorrected. (This line IS the user's making aesthetic.) (`kid-a-loops-mistreated-granular.md`)

---

## Patches on Wave-1 gear sheets (appended there too)

### CB Big Time — delay / centerpiece  (3 patches)

| # | Patch | Ref (Radiohead sound) | Prov |
|---|-------|-----------------------|------|
| BT-TB1 | **"Let Down" Cascading Jangle-Delay** ⭐ | "Let Down" doubled/tripled arpeggios, 5/4-vs-4/4 phasing | 🟣 |
| BT-TB2 | **"Ful Stop" Space-Echo Arpeggio Bed** ⭐ | "Ful Stop" Small Stone arps → Boss RE-20 under the wash | 🟣 |
| BT-TB3 | **Ondes-Martenot Lead Delay** ⭐ | Kid A Ondes leads → banjo-as-voice, singing trails | 🟣 |

- **BT-TB1:** MODE Short · STATE Compressed · VOICING HiFi · MOTION Sine subtle · 0.5X OFF · COLOR
  ~30–35% · TIME dotted-8th or **5-against-4** tap · CLUSTER ~45–55% · TILT above noon · FEEDBACK
  ~40% · WET ~40% · **SPREAD ping-pong** · clock-lock CC54. Bright/clean — resists the degrade
  tie-breaker (the jangle is the hook).
- **BT-TB2:** MODE Short · STATE Saturated/Compressed · VOICING Warm · MOTION Sine · COLOR ~40% ·
  TIME dotted-8th clock-locked · CLUSTER ~25% · TILT slightly below noon · FEEDBACK ~45% · WET ~35%
  (sits *under* the wash) · DEPTH moderate (Space-Echo flutter). Phaser swirl lives upstream.
- **BT-TB3:** MODE Long · STATE Compressed (ducking/sagging trails) · VOICING Focus · MOTION Sine
  slow+shallow · COLOR ~35% · TIME long musical · CLUSTER low ~15% · TILT noon→up · FEEDBACK ~50% ·
  WET ~40% · TEXTURE ~50%. Pair with CB Clean swell + VG-800 glide.

### CB Blooper — looper / glitch  (5 patches)

| # | Patch | Ref (Radiohead sound) | Prov |
|---|-------|-----------------------|------|
| BL-TB1 | **Go-To-Sleep Random Stutter (Scrambler)** ⭐ | "Go To Sleep"/"There There" random-stutter Max/MSP | 🟣 |
| BL-TB2 | **"Let Down" Octave-Stack Arpeggio Builder (Pitcher)** ⭐ | "Let Down" arpeggio doubled an octave + 3rd layer | 🟣 |
| BL-TB3 | **Daydreaming Half-Speed Octave-Down Grind** ⭐ | "Daydreaming" loop → half-speed octave-down grind | 🟣 |
| BL-TB4 | **Reverse-Bloom Loop** ⭐ | "Daydreaming" reversed glockenspiel + "Backdrifts" reverse | 🟣 |
| BL-TB5 | **Kid-A "Loops Mistreated" Aging Wall** ⭐ | Kid A mistreated/out-of-phase loops; Ed cutting up Rhodes | 🟣 |

- **BL-TB1:** record a dense source · MOD B **Scrambler (B5)** CCW = random (toggle = re-roll), CW
  = fixed sequence · REPEATS up · **DRY KILL** = Feral kill-dry · sync to Digitakt clock.
- **BL-TB2:** Mode ADD · record clean bright arp · MOD A **Pitcher (ALT A2)** +1 oct, punch-in
  overdub · optional 3rd pass at 5th/octave · REPEATS max. Pairs with BT-TB1.
- **BL-TB3:** Mode ADD · build a dense loop · MOD B **Stepped Speed (B4)** octave-down · mild
  STABILITY ~10:00 + optional Filter B6 CCW for grind · REPEATS max.
- **BL-TB4:** capture a ringing pluck/tail · MOD B **Stepped Speed (B4)** knob **CCW = reverse** ·
  in ADD overdub the reversed pass over the forward loop (sample-then-reverse-and-layer).
- **BL-TB5:** Mode ADD · clean loop, STABILITY off → **up** (age/drift = "breathes wrong") · keep
  overdubbing · REPEATS ~11–1:00 (fade) · Dropper A2 mild (granular) · BLIP slider → flutter not hiss.

### CB MOOD MkII — looper / delay / verb  (3 patches)

| # | Patch | Ref (Radiohead sound) | Prov |
|---|-------|-----------------------|------|
| MD-TB1 | **Real-Time Reverse Swell** ⭐ | "Daydreaming" reversed glock + "Backdrifts" reverse | 🟣 |
| MD-TB2 | **Kid-A Mistreated Micro-Loop (CLASSIC + Tape)** ⭐ | Kid A mistreated/out-of-phase loops | 🟣 |
| MD-TB3 | **Ful-Stop / Modulated Synth Wash (frozen Reverb)** ⭐ | "Ful Stop" unison-drift wash; modulated verb | 🟣 |

- **MD-TB1:** Wet MODE **Slip** · **MODIFY CCW = reverse** · TIME low = instant / high = reversed
  phrases that fade in · CLASSIC for crunch · freeze (hold LEFT) for a held reversed bed.
- **MD-TB2:** Micro MODE **Tape** · **CLASSIC ON** · Balance Beam: lower CLOCK (grit) then raise
  MODIFY (back to recorded speed) = degraded-but-in-tune · Wet Reverb over it.
- **MD-TB3:** Wet MODE **Reverb** · TIME ~1:00 · MODIFY CW (washed) · freeze (hold LEFT, LATCH) ·
  slowly turn **CLOCK down** for the moving/detuning drift (fakes the unison-voice drift).

### CB Clean — preamp / dynamics  (1 patch)

| # | Patch | Ref (Radiohead sound) | Prov |
|---|-------|-----------------------|------|
| CL-TB1 | **Ondes-Martenot Bowed-Swell** ⭐ | Kid A Ondes intensity-key swell → banjo bows in | 🟣 |

- **CL-TB1:** AUX = Dynamic Swell (LATCH for toggle) · Hidden: **Wet = Swell In ~noon–1:00**, **Dry
  = Swell Out ~noon** · Sensitivity by LED · gentle Dynamics · EQ NOON. Banjo plucks bow in like the
  Ondes' intensity key; feed into Big Time BT-TB3 + VG-800 portamento for the glide.

---

## Index-only patches — gear without a sheet yet

> Derived for completeness from the lens' target gear; no patch sheet exists for these units, so
> they live here only. All 🟣 designed-to-emulate.

### Eventide H90 — multi-fx (reverse, phaser, hall)

| # | Patch | Ref | Settings (designed) | Prov |
|---|-------|-----|---------------------|------|
| H90-TB1 | **Backwards reverse-swell algorithm** ⭐ | "Daydreaming"/"Backdrifts" reverse | Load a **Reverse** delay/`Reverse` algo: reverse-window ~medium, feedback low-mid, mix ~40%; each note swells in. Stack with a hall in a parallel/series preset for the ballroom space. | 🟣 |
| H90-TB2 | **Ful-Stop Small-Stone phaser** ⭐ | "Ful Stop" Small Stone arpeggios | **Phaser** algorithm, 4-stage, **slow rate** (~0.3–0.6 Hz), depth ~60–70%, feedback/regen moderate for the Small Stone V4 throb; feed into Big Time BT-TB2. The rig's closest true phaser. | 🟣 |
| H90-TB3 | **St Catherine's ballroom hall** ⭐ | "Let Down" 3am ballroom reverb | **Hall/Blackhole**: long **pre-delay** (~80–120 ms), decay ~4–6 s, low diffusion-modulation, mix ~25–30% under the jangle. The "supernatural natural reverb." | 🟣 |
| Refs | | | `kingofgear-thom-looping-daydreaming.md`, `ful-stop-synth-wash-phasing-arpeggios.md`, `poeticwax-let-down-wall-of-sound.md` | |

### Strymon Big Sky — reverb (modulated wash, plate, room)

| # | Patch | Ref | Settings (designed) | Prov |
|---|-------|-----|---------------------|------|
| BSky-TB1 | **Modulated detuning wash** ⭐ | Modulated/detuned verb (art-rock lens); "Ful Stop" drift | **Shimmer/Cloud or Chorale** machine, decay long, **MOD depth up + slow rate** (the verb "moves and detunes"), low-mid mix. The moving-wash signature. | 🟣 |
| BSky-TB2 | **St Catherine's plate/room** ⭐ | "Let Down" EMT 140 plate + ballroom | **Plate** (EMT 140 role) or **Room/Hall**, long pre-delay, decay ~4 s, low mix under the cascade. | 🟣 |
| Refs | | | `poeticwax-let-down-wall-of-sound.md` (EMT 140 plate + ballroom), taste-profile lens (modulated wash) | |

### Roland VG-800 — guitar-synth modeler (banjo/baritone source)

| # | Patch | Ref | Settings (designed) | Prov |
|---|-------|-----|---------------------|------|
| VG-TB1 | **Ondes-Martenot lead voice** ⭐ | Kid A Ondes leads | A smooth lead/sine-ish model with **portamento/glide ON** (slow), light vibrato, slow attack; played on the banjo voice → the gliding, singing Ondes line. Pair with Clean CL-TB1 swell + Big Time BT-TB3. | 🟣 |
| VG-TB2 | **Ful-Stop unison-drift pad** ⭐ | "Ful Stop" multi-synth unison wash | Two detuned saw/pad voices (the drift between voices = the wash), slight chorus; sustained single notes. The synth-bed source for MOOD MD-TB3. | 🟣 |
| VG-TB3 | **Baritone motorik sub** | "Ful Stop" 1st-half motorik bass | Baritone model, clean/tight, fed to a clock-locked Big Time groove (16ths, flat) — the dark motorik first half. | 🟣 |
| Refs | | | `kingofgear-radiohead-synths-ondes.md`, `ful-stop-synth-wash-phasing-arpeggios.md` | |

### TE OP-1 Field — synth-sampler

| # | Patch | Ref | Settings (designed) | Prov |
|---|-------|-----|---------------------|------|
| OP1-TB1 | **Prophet/Juno unison wash** ⭐ | "Ful Stop" / Kid A polysynth pads | Two slightly-detuned synth-engine voices (or one voice + a sampled pad), chorus on, played as sustained single notes → the unison-drift wash. Layer with VG-TB2. | 🟣 |
| OP1-TB2 | **ZX-Spectrum outro bleeps** ⭐ | "Let Down" dying-ZX-Spectrum outro | A lo-fi/8-bit-ish synth or chopped sample sequenced to random-ish in-key notes → the "broken modem" bleeps; or feed into Blooper Scrambler for the randomness. | 🟣 |
| Refs | | | `ful-stop-synth-wash-phasing-arpeggios.md`, `poeticwax-let-down-wall-of-sound.md` (ZX Spectrum bleeps) | |

### Chase Bliss / Cooper FX Generation Loss — tape degrade

| # | Patch | Ref | Settings (designed) | Prov |
|---|-------|-----|---------------------|------|
| GL-TB1 | **Tape flutter / wow under the jangle** ⭐ | Kid A "breathes wrong"; tape flutter (lens) | Gen Loss (before Big Time on Board 3): moderate **WOW/FLUTTER**, gentle generations/gen, light HP/LP filtering → the cascade arrives already tape-warped and pitch-drifting. The pre-degrade for BT-TB1/BT-TB2. | 🟣 |
| Refs | | | `kid-a-loops-mistreated-granular.md` (loops out of phase / breathe wrong), taste-profile lens (tape flutter) | |

---

## Chain recipes (putting it together)

- **"Let Down" wall (one player):** banjo arpeggio → CB Clean (light comp) → Gen Loss (GL-TB1
  flutter) → **Big Time BT-TB1** (5-against-4 cascade, ping-pong) with a **Blooper BL-TB2** octave-up
  stack underneath → **H90 H90-TB3 / Big Sky BSky-TB2** ballroom hall. Bright, jangly, Spector-wide.
- **"Ful Stop" two halves:** *first half* — Digitakt/MPC motorik 16ths + VG-TB3 baritone → Big Time
  clock-locked groove. *Second half* — **VG-TB2 / OP1-TB1** unison-drift wash held on **MOOD MD-TB3**,
  the phasing arpeggio through **H90-TB2 phaser → Big Time BT-TB2** Space-Echo bed under it.
- **Daydreaming reverse bed:** ringing banjo/glock-like notes → **MOOD MD-TB1** (live reverse) or
  **Blooper BL-TB4** (committed reversed layer); switch to **BL-TB3** half-speed octave-down for the
  grinding finale.
- **Go To Sleep glitch:** dense banjo/VG → **Blooper BL-TB1** Scrambler random (DRY KILL = kill-dry),
  synced to the Digitakt clock.
- **Ondes lead:** VG-TB1 glide voice → **Clean CL-TB1** bowed-swell → **Big Time BT-TB3** singing
  trails.

## Honesty ledger

- **Documented 🟢:** 0. (No Radiohead artist setting exists for any of the user's gear — they used
  Max/MSP, an EHX 45000, tape, and polysynths.)
- **Emulated 🟣:** 23 — **12 on gear sheets** (3 Big Time, 5 Blooper, 3 MOOD, 1 Clean) + **11
  index-only** (3 H90, 2 Big Sky, 3 VG-800, 2 OP-1, 1 Gen Loss).
- **Approximation flags:** the rig has **no true phaser** (H90 phaser block is closest; the swirl is
  approximate) and **cannot multi-voice a synth unison** (the drift is faked via frozen-reverb CLOCK
  drift / two detuned VG/OP-1 voices). Radiohead's reverse is a captured-then-reversed *sample* — the
  pedals approximate the *result*, not the method. All flagged inline.
