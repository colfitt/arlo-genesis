---
title: Electronic / groove-first — Cluster Index (Track B3)
cluster: electronic-groove-first
anchors: [LCD Soundsystem, Daft Punk, The Postal Service]
focus_artist: LCD Soundsystem
focus_songs: ["All My Friends", "Dance Yrself Clean", "Around the World", "Da Funk", "Such Great Heights"]
generated: 2026-06-14
derived_patches: 16
documented_green: 0
emulated_purple: 16
index_only: 2
lens: Research/Taste-Profile/taste-profile.md
tags: [taste-profile, track-b, lcd-soundsystem, daft-punk, postal-service, filter-house, sidechain, sequenced, additive-build, vocoder]
---

# Electronic / groove-first — LCD / Daft Punk / Postal Service cluster index

> **What this is.** The cross-rig view of every patch derived this wave from the electronic /
> groove-first lens, anchored on **LCD Soundsystem** ("All My Friends" one-loop long build,
> "Dance Yrself Clean" quiet-build-then-explosion), **Daft Punk** ("Around the World" /
> "Da Funk" filter-house, talkbox/vocoder), and **The Postal Service** ("Such Great Heights"
> glitch beat under soft vocals). Signature sounds chased: **sequenced analog/synth lines**,
> **filtered loops that open/close over a build**, **vocoder/talkbox**, **four-on-the-floor +
> motorik pulse**, **sidechain pump**, **drum-machine backbone**, **additive arrangement**
> (lock a loop, stack and filter layers across minutes). Patches live on the relevant gear
> sheet (single source of truth); a couple of vocoder/talkbox approximations are documented
> **index-only**.
>
> **Provenance honesty (the headline).** **Every patch is 🟣 designed-to-emulate.** None of
> these artists ever touched the user's gear — LCD/DFA built grooves on a CS-60/SH-101/808/909
> resampled in Pro Tools→Logic; Daft Punk used a Juno-106/MKS-80/TB-303/SP-1200 at Daft House;
> the Postal Service used a Kurzweil K2000RS + NI Battery in Cubase, mailed by post. **No artist
> setting exists for any Elektron, MPC, OP-1, 61SL or VG-800 here.** So there are **0 🟢
> documented settings and 16 🟣 emulations** — by design, flagged honestly per the lens. The
> Refs name the real record/sound each patch chases; the *settings* are first-principles from
> each unit's manual + the cited sources. No artist attribution is fabricated.
>
> **Approximation flags (say-so, non-negotiable).** The rig has **no vocoder and no talkbox.**
> The "robot voice" patches (VG-800 #VG-E3, OP-1 #OP1-E3) only **approximate** the *result* —
> they feed a carrier and modulate its filter rhythmically, an envelope/filter fake, not a
> bank-of-bandpass vocoder. They are marked **INDEX-ONLY · approximate**. The **sidechain
> pump** is also an emulation: the Elektrons/MPC have no true DAW-style sidechain key, so the
> duck is faked with an **LFO-ramp on track volume** or the OT's input compressors — flagged
> per patch.

## How these artists actually get these sounds (research summary)

Captured to `Research/Taste-Profile/sources/`:

- **LCD "All My Friends" = one loop, additive build.** Two pianos play one interlocking
  figure (Steve Reich *Music for 18 Musicians* lineage) and **that double-piano loop runs
  essentially unchanged through the whole ~7:45 track**, with a deliberate slur left in. James
  Murphy's method is **additive** — lock a tempo + a tiny core, then enter layers one at a
  time across minutes; the unchanging loop lets each new layer register. Aimed at the feeling
  of Joy Division's "Transmission" / Arthur Russell's "Go Bang." (`lcd-all-my-friends-piano-loop-build.md`)
- **LCD "Dance Yrself Clean" = withholding, then explosion.** ~3 min of a sparse two-chord
  vamp (bass toll + tapped percussion/cowbell + hurdy-gurdy organ + muted close vocal), then a
  **cued drop** into a huge **fuzzy/distorted synth-arp** wall + full drum-machine groove. The
  build is **arrangement, not a filter sweep** (contrast Daft Punk) — layers withheld then
  slammed in at one boundary; the drop arp is run **hot/saturated**, on-aesthetic for the rig.
  (`lcd-dance-yrself-clean-build-explosion.md`)
- **LCD method = resample the synth for the drums + analog imperfection.** Murphy
  **synthesizes drum hits on a polysynth and resamples them** to build the rhythm track — the
  "Get Innocuous!" kit was built from a **Yamaha CS-60** and sampled back in. Drum sources:
  TR-808 (heavy), TR-909, CR-78, Simmons SDS-V; DBX 162SL bus comp for glue. Philosophy:
  **"analog and imperfect over synthetic and streamlined"** — vintage gear is a small part; the
  *method* (tight palette → resample → loop → layer additively, human looseness left in) is the
  thing. Tyler Pope's discipline: "one drum machine + one synth" (CR-78 + ARP Odyssey).
  (`lcd-murphy-resample-synth-drums-analog-imperfection.md`, `lcd-tyler-pope-one-machine-one-synth-gear.md`)
- **Daft Punk filter-house = one loop, vary the timbre not the notes.** A 2–4-bar disco/funk
  loop (or a short synth figure) repeats through the whole track; the story is told by
  **filter-cutoff automation** (lowpass/highpass opening over a build), plus phasing/flanging
  and **cutting up the loop** into different slices. **"Around the World" bass** = sawtooth,
  filter cutoff low (~2.7 on a 0–10 scale), **resonance high (not screeching, ~6.9 in TAL
  U-NO-LX)**, small env→filter, **ADSR attack 1 / decay 6 / no sustain** = the pluck. **Lead**
  = square, filter ~3, reso ~6, env-mod halfway, attack ~2 = "funky wah-wah." Tempo-synced
  stereo delay (1/8 L, dotted-1/8 R, ~25% mix, ~40% fb). Drums = "dirty 909-type with shuffle."
  (`daft-punk-around-the-world-bass-macprovideo.md`, `daft-punk-homework-synths-reverbmachine.md`, `splice-filter-house-techniques.md`)
- **Daft Punk "Da Funk" lead = distorted, band-passed, portamento mono line.** Originally an
  **MS-20** (distorted filter envelope into the high-pass) or a Juno-106/MKS-80 into an Ibanez
  Fat Cat — reads like an overdriven guitar; melody moves in **perfect fourths**. Recreation
  spec: sawtooth + **GLIDE/portamento ~10 o'clock**, VCA full, filter-env "wah" attack. The
  303 bassline = a real TB-303 acid pattern. (`daft-punk-da-funk-lead-portamento-moog.md`,
  `daft-punk-homework-synths-reverbmachine.md`)
- **Daft Punk vocals = NO single vocoder.** Three families per song: **talkbox** (a tube into
  the mouth modulating a Juno-106 — "Around the World"; Heil/Rocktron Banshee), **vocoder**
  (Roland SVC-350 / DigiTech Talker / Sennheiser VSM201), **harmonizer/Auto-Tune** (DigiTech
  Vocalist; Auto-Tune on "One More Time"). **The rig has neither talkbox nor vocoder** → the
  robot-voice patches are flagged approximate. (`daft-punk-talkbox-vocoder-per-song-bjango.md`)
- **Filter-house grit + pump.** The lo-fi crunch = a loop recorded into an **SP-1200 at 45 rpm
  then pitched down** (juicy artifacts → approximate with bitcrush); the **pump** = a quarter-
  note **kick triggers sidechain compression** on the loop. Pump settings: **attack 1–10 ms,
  release 150–250 ms @ ~120 BPM, ratio 4:1–10:1, 6–12 dB gain reduction.**
  (`splice-filter-house-techniques.md`, `sidechain-pump-settings-house-techno.md`)
- **Postal Service "Such Great Heights" = glitchy programmed beat, NO pump.** Jimmy Tamborello's
  **Kurzweil K2000RS** generated the beeping melodies + glitchy rhythms; sequenced in **Cubase**
  with **NI Battery** kits; FX = a **Line 6 delay** + **Alesis MIDIverb**. Crucially: **"none of
  that [sidechain] on the album"** — the clatter is raw programmed beats + delay, the
  un-pumped counterpoint to Daft Punk. Glitch lineage (Dntel): "every song had something
  broken-sounding in it" — sequence tight beeps/clicks, then add the broken element.
  (`postal-service-give-up-tamborello-gear-musicradar.md`, `dntel-tamborello-glitch-tools-westword.md`)

---

## Patches on gear sheets (appended there too)

### Elektron Digitakt 2 — sample sequencer  (3 patches)

| # | Patch | Ref (electronic sound) | Prov |
|---|-------|------------------------|------|
| DT2-E1 | **Filter-House Loop (open/close cutoff sweep)** ⭐ | Daft Punk "Around the World"/"Da Funk" filter-house | 🟣 |
| DT2-E2 | **Sidechain-Pump Bus (LFO-ramp duck)** ⭐ | Filter-house / LCD 4-on-the-floor breathing | 🟣 |
| DT2-E3 | **Glitch Beat under Soft Vox (Postal Service, un-pumped)** ⭐ | Postal Service "Such Great Heights" K2000 clatter | 🟣 |

- **DT2-E1:** Load a 2–4-bar disco/funk-style loop (or resample a VG-800/banjo figure) on one
  track, `SRC` ONESHOT/`LOOP ON`, track length = loop length so it never changes (the
  filter-house rule — vary timbre, not notes). FX page: **multimode filter**, start `FREQUENCY`
  low + `RESONANCE` high-but-not-screaming. **LFO → filter FREQUENCY**, `WAVE = TRIANGLE`,
  `MULT` tempo-synced very slow (one cycle over many bars) so the cutoff **opens over the
  build**; or p-lock/hand-ride `FREQUENCY` for a manual sweep. Add a touch of `BIT REDUCTION`
  for the SP-1200 grit. Send a slap of `DELAY` (tempo-synced). The single signature filter-house
  move. **Ref:** `daft-punk-homework-synths-reverbmachine.md`, `splice-filter-house-techniques.md`.
- **DT2-E2:** On any track that should "breathe" with the kick (the loop/bass/pad): **LFO →
  track LEVEL (AMP volume)**, `WAVE = RAMP` (saw that snaps down on the beat then rises),
  `MULT` synced so **one LFO cycle = one beat** (1/4), `DEP` high (deep duck), `MODE = TRIG`
  retriggered on the downbeat. The ramp's down-then-recover shape **fakes the sidechain pump**
  — the DT2 has no true sidechain key. Set the kick on the same step the ramp resets. **Ref:**
  `sidechain-pump-settings-house-techno.md`, `splice-filter-house-techniques.md`.
- **DT2-E3:** Resample a VG-800/OP-1 **blip/beep** (single tone) and chop it; program a **fast,
  clattery 16th beat** of beeps + clicks. **NO pump** (Postal Service had none). Add the broken
  element: a `BIT REDUCTION` p-lock on a few steps, **conditional/probability trigs** (60–80% or
  1:2) + micro-timing nudges for the Dntel cut-up feel, short retrigs (`RTRG`) on one step. Send
  a `DELAY` slap (the Line 6 / MIDIverb role); keep it dry-forward so a soft lead sits on top.
  **Ref:** `postal-service-give-up-tamborello-gear-musicradar.md`, `dntel-tamborello-glitch-tools-westword.md`.

### Elektron Octatrack MkII — performance sampler  (3 patches)

| # | Patch | Ref (electronic sound) | Prov |
|---|-------|------------------------|------|
| OT-E1 | **Filter-House Crossfader Open/Close** ⭐ | Daft Punk filter-house cutoff automation | 🟣 |
| OT-E2 | **4-on-the-Floor Sidechain-Pump Loop** ⭐ | Filter-house / LCD pump (input comp + LFO duck) | 🟣 |
| OT-E3 | **One-Loop Additive Long Build (All My Friends)** ⭐ | LCD "All My Friends" / "Dance Yrself Clean" build | 🟣 |

- **OT-E1:** Put the disco/funk loop (or a resampled banjo/VG figure) on a **Flex** track,
  `LOOP ON`. **FX1 = multimode resonant filter**, FX2 = delay. **Scene A** (fader left) =
  filter **closed** (`CUTOFF` low, `RESONANCE` up); **Scene B** (fader right) = filter **open**
  (`CUTOFF` high). Throwing the crossfader A→B **is** the filter-house build; add a slow
  **LFO → FX1 cutoff** under it for motion, and **Lo-Fi (bit reduction)** for SP-1200 grit. The
  OT's crossfader is the most natural filter-house controller on the rig. **Ref:**
  `splice-filter-house-techniques.md`, `daft-punk-homework-synths-reverbmachine.md`.
- **OT-E2:** Loop on a Flex/Static track; **kick on Track for the 4-on-the-floor**. Two ways to
  pump: (a) route the loop through an **input compressor** (the OT has one per input pair) — the
  OT factory template even ships "sidechain pumping on every pattern (default 4-on-the-floor)";
  (b) **LFO → AMP volume** on the loop track, `WAVE = RAMP`, synced 1/4, `DEP` high, retrigged on
  the kick step. Pump targets from house practice: deep, fast attack, recover before the next
  beat. The pump is an **emulation** (no true sidechain key) — flagged. **Ref:**
  `sidechain-pump-settings-house-techno.md`, OT patch #? input comps.
- **OT-E3:** Lock **ONE loop** (piano-ish / banjo / VG figure) on a Flex track, `LOOP ON`, and
  **never change it** (the "All My Friends" rule). Build the song by **adding tracks across
  minutes** — percussion, bass, pad — each entering one at a time, muted/unmuted live with
  `[FUNC]+[TRACK]`. Stage the **"Dance Yrself Clean" explosion** as a **cued Part switch** (or
  Pattern change at the next boundary) that drops in a distorted VG-800 saw arp + full kick on
  the downbeat. Build = arrangement, not a filter sweep. Keep the deliberate loop slur in.
  **Ref:** `lcd-all-my-friends-piano-loop-build.md`, `lcd-dance-yrself-clean-build-explosion.md`.

### Akai MPC Sample (AC50) — sampler/groovebox  (3 patches)

| # | Patch | Ref (electronic sound) | Prov |
|---|-------|------------------------|------|
| MPC-E1 | **4-on-the-Floor 909/808 Kit + Cowbell** ⭐ | LCD / filter-house drum-machine backbone | 🟣 |
| MPC-E2 | **Resample-the-Synth-for-Drums (Get Innocuous kit)** ⭐ | LCD "Get Innocuous!" CS-60-built kit | 🟣 |
| MPC-E3 | **Glitchy Beep-Beat (Postal Service, un-pumped + dry)** ⭐ | Postal Service "Such Great Heights" K2000 beat | 🟣 |

- **MPC-E1:** Build a kit of 909/808-style samples on one pad bank: kick (center), snare/clap,
  **closed + open hat in one Mute Group** (closed chokes open), **cowbell** (the LCD/DFA staple),
  ride/perc. **Tune drums to the song key** (Tune page Semi −24…+24 / Fine ±90¢; kick = root,
  snare = minor 3rd) so they lock to the baritone sub-bed. Program a **four-on-the-floor** kick
  + offbeat hats; add **Swing 54–58%** (the "shuffle" of dirty 909 house). **Transient Knob FX**
  on the kick (Attack +30–60%, Sustain −20%) for snap. Pan kick/snare center, hats/perc to the
  sides. **Ref:** `splice-filter-house-techniques.md`, `lcd-tyler-pope-one-machine-one-synth-gear.md`.
- **MPC-E2:** The signature DFA method on the AC50. **Synthesize** a kick/snare/cowbell from the
  **VG-800 SYNTH** (or OP-1) — one polysynth's voices — and **Resample (Pad 11)** each into the
  sampler (resample is silent the first try — do it twice). Tune to key, shape with Amp Env
  (Attack 0, short Decay-From-Start) + Transient FX, then **loop and layer additively** like
  "All My Friends." This is the "one synth → the whole kit" backbone, AC50-mapped. **Ref:**
  `lcd-murphy-resample-synth-drums-analog-imperfection.md`.
- **MPC-E3:** Resample a **VG-800/OP-1 beep** and chop it into pitched beeps; sequence a **fast,
  slightly-clattery** beat. **NO compression/pump** (Tamborello: "none of that on the album").
  Add the broken element with the **LoFi Bitcrush FX** (24→~6-bit) on a couple of hits and loose
  16th-note timing; send the bus to the **Delay FX** (the Line 6 / MIDIverb role). Keep it
  **dry-forward** under a soft lead. The un-pumped counterpoint to MPC-E1/MPC-E2. **Ref:**
  `postal-service-give-up-tamborello-gear-musicradar.md`, `dntel-tamborello-glitch-tools-westword.md`.

### TE OP-1 Field — synth/sampler  (3 patches)

| # | Patch | Ref (electronic sound) | Prov |
|---|-------|------------------------|------|
| OP1-E1 | **Da Funk Portamento Mono Lead** ⭐ | Daft Punk "Da Funk" glided band-passed lead | 🟣 |
| OP1-E2 | **Around-the-World Acid-Pluck Bass** ⭐ | Daft Punk "Around the World" sawtooth pluck bass | 🟣 |
| OP1-E3 | **Talkbox/Vocoder Robot-Voice (carrier source)** · INDEX-ONLY approximate | Daft Punk talkbox/vocoder vocals | 🟣 |

- **OP1-E1:** A distorted, glided mono lead. Engine **Voltage** (AM/biting, "good for evolving")
  or **Digital** for the band-passed squelch; **portamento/glide ON** (slide between notes is
  signature — Da Funk moves in perfect fourths); short filter-env "wah" attack; FX **nitro** (on)
  for the overdriven-guitar grit; LFO **value** for a touch of movement; Octave 0. Mono playing.
  Print to **Porta** tape for the degrade lean. Banjo-as-lead can carry this line via the VG
  (see VG-E1). **Ref:** `daft-punk-da-funk-lead-portamento-moog.md`.
- **OP1-E2:** A bouncing acid-pluck bass. Engine **Cluster** or **Dr Wave** at **Octave −1/−2**
  (saw character), **short DECAY / no SUSTAIN** envelope (the "subtle pluck"), filter cutoff low
  + resonance high (the acid signature), FX **filter** or **nitro**. Sequence a short repeating
  bass figure (the part doesn't change — the *filter* does). Ride the filter open over a build.
  **Ref:** `daft-punk-around-the-world-bass-macprovideo.md`, `daft-punk-homework-synths-reverbmachine.md`.
- **OP1-E3 · INDEX-ONLY · APPROXIMATE:** The OP-1 has **no vocoder/talkbox**. Closest fake:
  use it as the **carrier** — a sustained **Cluster/Dr Wave** saw note — and modulate its filter
  rhythmically (value-LFO or hand-ride) in time with a spoken/sung phrase, OR use the **Synth
  Sampler** to one-note-sample a voice and play it chromatically for a robotic-choir flavor.
  This reproduces the *result* (a moving, formant-ish robot tone), **not** the talkbox/vocoder
  method. Flagged approximate. **Ref:** `daft-punk-talkbox-vocoder-per-song-bjango.md`.

### Novation 61SL MkIII — controller / sequencer  (2 patches)

| # | Patch | Ref (electronic sound) | Prov |
|---|-------|------------------------|------|
| 61SL-E1 | **Filter-Cutoff Ride + Pump-CC Template** ⭐ | Daft Punk filter-house cutoff automation; LCD pump | 🟣 |
| 61SL-E2 | **Dance-Yrself-Clean Cued-Explosion Session** ⭐ | LCD "Dance Yrself Clean" withhold-then-drop build | 🟣 |

- **61SL-E1:** A standalone template/session that **rides the filter** of whatever holds the
  loop (VG-800 SYNTH cutoff via its CONTROL ASSIGN CCs, or a soft synth, or an Elektron FX CC).
  **enc1 → filter CUTOFF** CC (slow open/close = the filter-house build); **fader1 → a pump-CC**
  (or record a CC automation lane that ramps down on each beat = the duck); **enc2 → RESONANCE**.
  Set Low/High to scale; Fader Pickup ON. SL = **clock master** (Tx On) so the loop and any
  synced delays follow one tempo (4-on-the-floor). The hands-on filter-house controller. **Ref:**
  `splice-filter-house-techniques.md`, `daft-punk-homework-synths-reverbmachine.md`, `sidechain-pump-settings-house-techno.md`.
- **61SL-E2:** A standalone **Session** staging the LCD withhold-then-explosion. **Part 1** =
  the sparse quiet vamp (a held organ/baritone drone + a tapped-percussion pattern, low density,
  sustained for ~3 min). **Part 2** = the full drop (distorted VG-800 saw arp + full kick
  groove). Use **Sequence Transpose** / a **cued Session or pattern switch** at the boundary to
  **slam Part 2 in on the downbeat** (the explosion is arrangement, not a filter sweep). SL =
  clock master driving the Elektrons/MPC. **Ref:** `lcd-dance-yrself-clean-build-explosion.md`,
  `lcd-all-my-friends-piano-loop-build.md`.

### Roland VG-800 — guitar-synth modeler (banjo/baritone source)  (3 patches)

| # | Patch | Ref (electronic sound) | Prov |
|---|-------|------------------------|------|
| VG-E1 | **Da Funk Band-Passed Portamento Lead (banjo-as-lead)** ⭐ | Daft Punk "Da Funk" distorted glided lead | 🟣 |
| VG-E2 | **Around-the-World Acid Filter-Bass (baritone)** ⭐ | Daft Punk "Around the World" acid-pluck bass | 🟣 |
| VG-E3 | **Talkbox/Vocoder Carrier (filter-modulated synth)** · INDEX-ONLY approximate | Daft Punk talkbox vocal (Juno carrier) | 🟣 |

- **VG-E1:** Banjo via GK-5 as a Da Funk lead. `INST TYPE = SYNTH`, `SYNTH TYPE = SOLO` (or
  GR-300 for more grit). **PITCH-glide/portamento ON** (the Da Funk slide — moves in 4ths);
  `FILTER CUTOFF` mid + `TOUCH SENS` up = pick-triggered filter "wah" (the band-passed,
  overdriven-guitar voice); `RESONANCE` moderate. `NORMAL MIX` low. Into the rig's distortion
  (MXR 108 / Hizumitas) for the overdriven-guitar read — on-aesthetic. Banjo-as-lead carries the
  Da Funk line. **Ref:** `daft-punk-da-funk-lead-portamento-moog.md`, `daft-punk-homework-synths-reverbmachine.md`.
- **VG-E2:** Baritone JM (or banjo) as the bouncing acid bass. Switch to **BASS mode**,
  `INST TYPE = SYNTH`, `SYNTH TYPE = FILTER BASS`. `FILTER CUTOFF ~50` (low), `FILTER RESO ~60`
  (high — the acid signature), `TOUCH SENS ~40`, **`FILTER DECAY ~25` (snappy = the pluck / "no
  sustain")**, `COLOR 70–90` (weight). Optional `ALT TUNE = -12 STEP` for a sub-octave. Play a
  short repeating figure; ride `FILTER CUTOFF` open over the build (or have the 61SL/Elektron do
  it). The VG's acid-bass is the closest hardware "Around the World" bass. **Ref:**
  `daft-punk-around-the-world-bass-macprovideo.md`, `daft-punk-homework-synths-reverbmachine.md`.
- **VG-E3 · INDEX-ONLY · APPROXIMATE:** The VG-800 has **no vocoder/talkbox**. Closest fake:
  `INST TYPE = SYNTH` (saw/GR-300) as the **carrier**, then have the **61SL/Digitakt send a
  sequenced CC to the VG's FILTER CUTOFF** (CONTROL ASSIGN, CC#1–31 window) so the filter opens
  and closes rhythmically in time with a phrase — an **envelope/filter** robot voice, not a
  bank-of-bandpass vocoder. The VG's `ALT TUNE HARMONY` / `12-STRING` blocks add a harmonizer-
  choir flavor. Reproduces the *result*, not the method. Flagged approximate. **Ref:**
  `daft-punk-talkbox-vocoder-per-song-bjango.md`.

---

## Index-only patches — approximate / no clean rig path

> These are the cluster's **vocoder/talkbox** sounds. The rig has **no vocoder and no talkbox**,
> so these are flagged **approximate** and documented here for completeness. The patches above
> (VG-E3, OP1-E3) are the closest fakes; both reproduce the *result* (a moving, robotic/formant
> tone), not the method.

| # | Sound | Closest rig approximation | Prov |
|---|-------|---------------------------|------|
| IO-E1 | **Talkbox vocal** ("Around the World" Juno-106 + tube) | VG-E3 / OP1-E3 carrier + sequenced filter-CC modulation; **no tube, no mouth-formant** — only a rhythmic filter fake. | 🟣 approximate |
| IO-E2 | **Vocoder vocal** (SVC-350 / DigiTech Talker / VSM201) | No bank-of-bandpass vocoder on the rig. Nearest in the wider rig (not this cluster's target gear): granular/formant movement on Microcosm or Chroma Console; or VG `ALT TUNE HARMONY` for a robotic harmonized choir flavor. **True vocoder = not achievable here.** | 🟣 approximate |

**Ref (both):** `daft-punk-talkbox-vocoder-per-song-bjango.md`.

---

## Chain recipes (putting it together)

- **Filter-house build (one player):** banjo/VG figure or sampled disco loop locked on **OT-E1**
  (or **DT2-E1**), filter **closed → open** via the OT crossfader (or **61SL-E1** enc1 riding the
  VG/Elektron cutoff CC), **bit-reduction** for SP-1200 grit, a **VG-E2** acid bass underneath,
  tempo-synced delay → CB Big Time. Pump the loop with **DT2-E2 / OT-E2** (LFO-ramp duck) on the
  4-on-the-floor. Saturate the drop arp (degrade lean).
- **LCD additive long build:** lock ONE loop on **OT-E3** and never change it; build the kit on
  **MPC-E2** (resample a VG-800 voice = the Get Innocuous method) + **MPC-E1** 909 backbone;
  enter layers across minutes; stage the **Dance Yrself Clean** drop as a cued Part/Session switch
  (**OT-E3 / 61SL-E2**) that slams a distorted **VG-E1** saw arp + full kick in on the downbeat.
- **Da Funk banjo lead:** **VG-E1** banjo (SOLO, portamento, filter-wah) → MXR 108 → Hizumitas
  for the overdriven-guitar read; **OP1-E1** can double or carry the line; melody in 4ths.
- **Postal Service glitch bed:** resample a VG/OP-1 beep → **MPC-E3** (or **DT2-E3**) fast
  clattery beat, **NO pump**, LoFi-bitcrush + loose timing + conditional retrigs, send a delay
  slap (Line 6 / MIDIverb role), keep dry-forward under a soft lead. The un-pumped counterpoint.
- **Robot voice (approximate):** **VG-E3 / OP1-E3** carrier + **61SL-E1** (or Digitakt) sending a
  sequenced filter-CC in time with a phrase. Flagged: not a real vocoder/talkbox.

## Honesty ledger

- **Documented 🟢:** 0. (No LCD / Daft Punk / Postal Service artist setting exists for any of
  the user's gear — they used CS-60/SH-101/808/909, Juno-106/MKS-80/TB-303/SP-1200, and a
  Kurzweil K2000RS in DAWs, none of it this rig.)
- **Emulated 🟣:** 16 — **all on gear sheets** (3 Digitakt 2, 3 Octatrack MkII, 3 MPC Sample,
  3 OP-1 Field, 2 61SL MkIII, 3 VG-800). **2 of those are flagged INDEX-ONLY · approximate**
  (VG-E3, OP1-E3 = the vocoder/talkbox fakes), and there are **2 pure index-only sounds**
  (IO-E1 talkbox, IO-E2 vocoder) documented with no clean rig path.
- **Approximation flags:** (1) **No vocoder/talkbox** on the rig — the robot-voice patches only
  mimic the *result* via filter modulation/harmonizer; true vocoder is not achievable. (2) The
  **sidechain pump** is faked with an **LFO-ramp on track volume** (or the OT's input
  compressors) — there is no DAW-style sidechain key on the Elektrons/MPC. (3) Daft Punk's
  filter-house was a **sampled disco loop**; the rig recreates the *timbre-variation method*
  (filter sweeps + bitcrush grit), not the original samples. (4) LCD's drums were a **resampled
  polysynth** — the rig reproduces the *method* (synthesize → resample → loop) on the AC50/
  Elektrons, not LCD's CS-60. All flagged inline.
