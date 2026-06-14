# Kontakt 8 — Usage Guide

Kontakt is the industry-standard **sampler engine**, and it earns its place in this
rig two ways: (1) as the **builder** that turns your own recordings — pedalboard
tails, banjo/baritone, OP-1/Digitakt/MPC/Octatrack/VG-800 one-shots, field
recordings — into **playable instruments**; and (2) as the **host** for the big
libraries you already own (Komplete's granular/ambient set + all the
Spitfire-in-Kontakt libraries). The killer move for this aesthetic is the first
one: **sample your own degraded sound and loop it into an evolving drone.** This is
the deepest unit in the software set — researched across four facets (sampling,
engine, community/management, ambient).

---

## 1. What's new in Kontakt 8 (released Sept 2024)

The biggest engine jump in years. `research/links/k8-engine-whats-new-musictech-review.md`, `research/links/k8-engine-whats-new-synthanatomy-updates.md`
- **Conflux** — a new **hybrid wavetable + sample** instrument: original PPG
  wavetables, **FM / phase / ring modulation**, dual shapers, multimode filter, dual
  envelopes + dual LFOs, a step "Animator," six macros, and a multi-FX block with a
  **shimmer reverb**. ~200 atmospheric presets. Reviewers peg it as *the* tool for
  "evolving textures, swamping bass swells, cinematic sound design" — squarely this
  rig's aesthetic. `research/links/k8-engine-conflux-scifi-pads-ni-blog.md`
- **Leap** — a "sampler within a sampler" performance engine (white keys = in-key
  one-shots/loops, black keys = live pitch/time/stutter/granular FX). *Limitation:*
  **stereo-only output.**
- **Tools** — instrument-agnostic **MIDI effects** usable on *any* loaded
  instrument: **Chords** (~130 progressions) and **Phrases** (181 melodies), plus
  the **8.6** additions (arpeggiator, 8-voice chord builder, humanizer, scale-lock,
  velocity-curve, multi-Tool stacking). Free in the Player too.
- **Redesigned UI/browser** (Navigator · Stage · Browser tabs: Instruments /
  Combined / Tools / Leap / Loops / One-Shots), with a **Classic View** toggle that
  restores the K7 layout. New **Combined** preset format saves multi-instrument
  layers + Tools/macros.
- **Factory Library** — redesigned, HiDPI, 7 new collections, **900+ instruments**,
  an Orchestral Tools collaboration (Noire, Stradivari Violin, Hybrid Keys).
- **Update history (don't conflate):** 8.1 added stomp/amp FX + delay/reverb types;
  **8.3** added **Moog-style passband + Japanese Sallen-Key filters**; 8.6 added the
  extra MIDI Tools. Full $299 / upgrade $99; Tools+Leap reach the free **Player**.

## 2. The instrument-building workflow (your own samples)

The canonical path: `research/transcripts/k8-sampling-firststeps-ch2-ep1-mapping-editor.md`, `research/transcripts/k8-engine-build-kontakt-instrument-ni-audioprogrammer.md`
1. **Classic View** (View menu) → `File → New Instrument` → click the **wrench** to
   enter the Instrument Editor. (Default View hides it.) Three layers: Instrument
   Editor (sampling/playback) · Komplete UI (GUI) · KSP (logic).
2. **Mapping Editor** — drag samples into key/velocity **zones**. **Auto-map from
   filenames:** name samples `instrument_group_note` (e.g. `banjo_plucks_C2`), then
   `Edit → Auto Map Setup` → assign a token as **Make Root Key** (critical — wrong
   root = wrong transpose) → `Auto Map Functions → Auto spread key ranges`. **Always
   label sharps, never flats** (auto functions only understand sharps).
3. **Groups** (`Group Editor`) — separate layers/articulations/round-robins for
   independent volume/pan/tune/FX. **Turn OFF the red "Edit All Groups"** by default
   (a common footgun); use **Group Solo** to audition one at a time.
4. **Source / playback mode** — **Sampler** (RAM) · **DFD** (streams huge libraries) ·
   **Wavetable** · **Tone Machine** (granular) / **Time Machine 1/2/Pro** (stretch to
   hold duration across pitch — best for stretching one sample far) · **Beat
   Machine** (slice loops to keys) · **S1200/MP60** (vintage-sampler grit). `research/transcripts/k8-sampling-audioprogrammer-build-start-to-finish.md`
5. **Save** (`File → Save Edited Instrument`): **Patch Only** (.nki, samples stay in
   place — while developing) · **Patch + Samples** (copies samples beside the .nki —
   for sharing) · **Monolith** (all-in-one; avoid once you add scripting/graphics).
6. **Creator Tools** (free standalone app) — connects live to a running Kontakt,
   runs **Lua scripts** to **auto-map from a disk folder**, batch-rename groups/zones,
   and copy settings; **MIR** does **pitch detection** (auto root keys, monophonic)
   and **RMS detection** (auto velocity layers); batch funcs take a whole folder; can
   **export out to Decent Sampler / SFZ.** `research/links/k8-sampling-creator-tools-manual.md`

## 3. Looping for drones & sustained instruments (the key skill)

The most rig-relevant craft. `research/links/k8-sampling-drone-pad-looping-technique.md`, `research/transcripts/k8-sampling-hilowitz-looping-samples.md`
- **Recipe A (DAW-side, cleanest):** record **4× longer than one cycle**, grab the
  **middle two bars** (the join matches because each end already holds the other's
  ring-out), tiny fades, then loop **start-to-finish with NO crossfade** in Kontakt.
- **Recipe B (in Kontakt, fast):** Wave Editor → enable **Sample Loop**, offset
  start/end into the middle, add a **heavy crossfade**; the volume dip is inaudible
  on **polyphonic** pads **if loop lengths vary across zones** (give each zone a
  slightly different loop length so a held chord *evolves* instead of dipping in
  unison).
- **Concrete values:** pad loop **0.25 → 0.75 s** with **~500-sample** crossfade; a
  long evolving pad wants a **big crossfade ~50,000 samples (~1 s @ 48 kHz)**.
- **Loop modes:** *Until End* (default) vs *Until Release* (plays the post-loop tail
  on note-off); **8 loop points max** (count 0 = forever); crossfade is in **samples**.
- **Trust your ears, not zero-crossing snap; longer loops sound more natural; never
  loop plucked/decaying sources** (banjo) — keep the natural tail and use **round
  robins** instead. `research/transcripts/k8-sampling-round-robins-kontakt-logic.md`
- **★ Export gotcha:** loop points set *inside Kontakt* **can't be exported** — if
  you'll ever port to SFZ/Decent/Ableton, set loops in the DAW/WaveLab (Hilowitz
  embeds `#loop` regions → BWF chunk, which Kontakt/Decent/SFZ all read).

## 4. Sampling the hardware rig into Kontakt (recipes by gear)

- **Sequence-and-record any line-out hardware** (OP-1 Field / Digitakt / VG-800):
  in Logic make an **External MIDI** track at the gear, **pre-program the note
  sequence** (e.g. 2-bar notes with a gap so tails don't bleed), arm the audio-return
  track, hit record, **walk away — hands-free**. Then de-noise, slice, fade, tune,
  map. **De-noise even direct-injected gear** (10 stacked noisy samples = 10× hiss). `research/transcripts/k8-sampling-firststeps-ch1-ep3-hardware-synth.md`
- **Logic Auto Sampler → EXS → Kontakt** (fastest): Logic's **Sampler → Sample
  (Auto Sampler)** auto-plays MIDI to the hardware and renders an EXS; drag the
  rendered WAVs into Kontakt and auto-map. `research/transcripts/k8-sampling-hilowitz-modular-autosampler.md`
- **Banjo / baritone instrument** (the pro pipeline): record the scale → **iZotope RX**
  spectral de-noise → chop in Reaper (`D` = split on silence) → **aubio pitch-detect**
  (more accurate than any DAW) → **round robins, don't loop** (plucked decays). `research/transcripts/k8-sampling-hilowitz-make-libraries-2020.md`
- **Drone from a sustained pedalboard tail** — print a long wall (Big Sky / Microcosm
  / VG-800 pad / OP-1 drone), loop it (§3), one zone per few semitones, **varied loop
  length per zone** so a held chord boils.
- **Bowed-source → wall (Clinton Shorter method):** bow an instrument, record 2–3
  bars with variations, **pan takes hard L/R**, **stretch one note across the whole
  keyboard**, layer variations by velocity/key-switch, toggle **stereo on/off**
  (lonely → huge), and **modulate pan + volume, not pitch, to "keep it boiling."**
  Ethos: *imperfect sounds are the feature* — the banjo→wall recipe verbatim. `research/links/k8-ambient-clinton-shorter-bowed-instruments-kontakt.md`
- **Field recordings / found sound → granular pads** — run a short capture through a
  granular mode (Tone Machine) before/while sampling to turn a pluck into a wall. `research/transcripts/k8-sampling-firststeps-ch1-ep4-pads.md`

## 5. The engine for evolving/ambient sound

**Modulation system** — Envelopes (AHDSR + multi-stage **Flexible/DAHDSR**), LFOs, a
**Complex LFO** (non-periodic motion), **Step Modulator / Envelope Follower / Glide**,
and external (**MIDI CC, random**). Right-click a param or **Add Modifier**; the
assignment appears in the **Mod router**; you can **modulate a modulator** (sine LFO
→ a rectangle LFO's rate = accelerating motion on a pad). The **Modulation Shaper**
maps source→target through a drawn curve with **Lag/Smoothing**. `research/transcripts/k8-engine-modulators-adsr-lfo-velocity-cc-cmdshiftnew.md`

> **★ The #1 modulation gotcha:** only **Source / Amplifier / Group-Insert FX** params
> can be *internally* modulated. **Instrument Insert, Send, and Main FX cannot** — to
> make a reverb/delay/filter "breathe," put it as a **Group Insert** or drive it via
> **host automation.** `research/links/k8-engine-advanced-modulation-ni-blog.md`

**Evolving-pad recipe:** sample-loop on → AHDSR with long Attack/Hold → filter as a
**Group Insert** → slow **sine LFO → cutoff (~0.1–0.3 Hz)** → a **second LFO →
pan** at a different rate → **random → pitch** at low intensity for detune life → one
**macro** riding filter+reverb live. `research/links/k8-ambient-ni-advanced-modulation-tricks.md`

**Granular "single sample → forever wall":** grain size **~600 ms**, interval **~40
ms**, **jitter ~50%**, bounce-edges on; then **LFO1 → grain interval @0.05 Hz** and
**LFO2 → grain size @0.09 Hz** (deliberately different, both sub-0.1 Hz) = minute-scale
drift that never cycles. `research/links/k8-ambient-ni-granular-synthesis-guide.md`

**Effects (~92 modules)** — RAUM (reverb, cosmic/modulated tails), Replika (delay),
Reaktor filters, tape saturation, the new Moog/Sallen-Key filters. The
**Convolution** effect (insert or send) accepts **any dragged-in audio as an IR** —
load a **degraded/untuned IR** (a pedalboard tail, a banjo scrape, tape hiss),
**pitch it down up to 8×** for thick tails, high-pass, 100% wet = "recorded-wrong"
spaces. `research/links/k8-ambient-convolution-creative-irs.md`, `research/links/k8-engine-effects-filters-ksp-roundup.md`

**Print-the-reverb-tail pad generator** (fastest): any source → a **20 s reverb
tail** → bounce the wet tail → that *becomes* the pad sample; stitch several at
different roots into a chord-bed. `research/transcripts/k8-ambient-any-sample-into-a-pad.md`

## 6. KSP scripting (honest scope)

**KSP** sits between incoming MIDI and the Source at the instrument level; it
reads/writes Kontakt params and builds custom GUIs (every pro library uses it). A
script is plain text, compiled with **Apply**, saved as **.nkp**. **Easy wins:** load
and tweak factory script presets (Harmonize, arpeggiators) with zero coding. **Deep
end:** real programming — callbacks (`on init/note/release/controller`), UI widgets,
sequencers, exotic tunings, round-robin logic. Honest learning curve: trivial scripts
are friendly, real instruments are genuine coding. Free canonical resource = **Nils
Liberg's KSP tutorial**; **Creator Tools** handles GUI/debug more easily than raw KSP. `research/transcripts/k8-engine-ksp-intro-session-1-microphonic.md`

## 7. Performance & library management (Logic + drives)

- **Purge** (the core RAM-saver): the winning order is **purge-after-playing** —
  load full → record the part → **Reset Markers** → play it through once → **Update
  Sample Pool** (drops only unused samples). On a drone session holding a multi-GB
  Spitfire patch on one note, this collapses it to a tiny footprint. **SSD only** for
  purge-on-demand (HDD clicks). `research/links/k8-community-purge-function-scanproaudio.md`
- **DFD vs RAM:** *Options → Memory → "Override Instrument's preload size."* Lower =
  less RAM/more CPU; higher = the reverse. `research/links/k8-community-impact-soundworks-optimize-cpu-ram.md`
- **★ Batch Re-Save** (the essential post-install step): *Files → Batch Re-Save →*
  pick the library folder — bakes in machine-specific paths (much faster loads) and
  **relinks missing samples**. **One library at a time**, and **re-run if the
  external drive's mount path changes.** `research/links/k8-community-batch-resave-soundiron.md`
- **Add non-Player libraries** (the "Add Library" button is **gone**): the **cogwheel
  "Import Content" icon, bottom-left of the Library tab → Add →** pick the folder;
  check **"import subfolders as individual libraries"** to bulk-add a whole drive. `research/links/k8-community-add-nonplayer-library-cogwheel.md`
- **NKS / Komplete Kontrol:** scans only **.NKI / .NKSN (snapshot)** — **.NKM multis
  are NOT recognized** (load from inside Kontakt); non-NKS snapshots can throw
  "content missing" (batch re-save first); your **61SL MkIII** gets auto key-colors
  for Chords. `research/links/k8-community-komplete-kontrol-nks-kkaccess.md`
- **Logic AU specifics:** use the **Multi-Output (16×Stereo)** variant → *View →
  Outputs → "+"* to add channels → set each instrument's output → in Logic's Mixer
  click the **"+"** on the Kontakt strip to spawn the Aux tracks. **Multitimbral:**
  check Multi-timbral on the track. **★ Freeze is disabled for multi-out/multitimbral
  instances → use Bounce In Place.** CPU/crackle playbook: I/O buffer **1024** for
  mixing, one **shared reverb on a Kontakt aux** (CPU + a cohesive drone tail), freeze
  single instances. `research/links/k8-community-logic-multiout-gregkocis.md`, `research/links/k8-community-logic-cpu-freeze-crackle.md`

## 8. The library ecosystem for this aesthetic (what to reach for)

All run **in Kontakt** and most accept your **own samples** in the sample layer: `research/links/k8-ambient-komplete-granular-trilogy.md`
- **Komplete 15 Ultimate granular trilogy:** **Ashlight** (dark granular — the doom
  pick) · **Straylight** (fragile sci-fi pads) · **Pharlight** (granular voice).
- **Cinematic/textural (in Ultimate):** Arkhis, Thrill, Mysteria, Rise & Hit, **Fables**
  (new in K15, 57 GB), Damage, Schema Dark/Light, Lores, Sequis.
- **Built into K8:** **Conflux** for evolving wavetable+sample textures.
- **Spitfire-in-Kontakt** (LABS / Ólafur Arnalds) — runs via the Spitfire/Kontakt
  path; covered in the dedicated Spitfire wave (cross-ref).
- **Free in Kontakt:** Play Series (Ethereal Earth/Hybrid Keys/Analog Dreams),
  Soniccouture Tape Choir ("infinite choir"), Signal. `research/links/k8-ambient-ni-5-free-libraries.md`

## 9. Notable users & techniques (sourced, flagged)

- **Clinton Shorter** (District 9, The Expanse) — the bowed-source→Kontakt-pad method
  (§4). Sourced from an NI Blog interview. HIGH. `research/links/k8-ambient-clinton-shorter-bowed-instruments-kontakt.md`
- **Dark-ambient producers** — **protoU** ("mostly Kontakt, morphing field
  recordings"), **Mebitek** (Kontakt + time-stretch/delay/dist/reverb), **Seesar**
  (bowed cymbals/scrapes as sources) — direct quotes from This Is Darkness interviews.
  HIGH. `research/links/k8-ambient-thisisdarkness-drones-producers.md`
- **Honest gap:** no named *shoegaze* producer surfaced — Kontakt's ambient practice
  genuinely lives in **film-score / dark-ambient**, which *is* well documented. None
  invented.

## 10. Rig-specific recipes (your gear by name)

- **Banjo/baritone sampled instrument** — RX → Reaper → aubio → round robins (don't
  loop); use **Cycle Random** with slightly-detuned groups for organic motion.
- **Pedalboard-tail drone** — print a wall → loop with varied per-zone length →
  Group-Insert filter with a slow LFO so it boils.
- **OP-1 / Digitakt / MPC / Octatrack one-shots** → sequence-and-record or Auto
  Sampler → playable Kontakt instrument; degrade further with the built-in Lo-Fi/Tape
  FX.
- **Your own convolution IRs** — drag a pedalboard tail / banjo scrape into the
  **Convolution** effect for a "recorded-wrong" space no preset gives you.
- **Logic** — Multi-Output variant for per-part processing; one shared reverb aux;
  Bounce In Place (not Freeze) on multi-out.

## 11. Best learning resources

1. **NI "KONTAKT: FIRST STEPS" (Steve)** — the free A-to-Z course; Ch.1 plan/record
   (incl. hardware sampling), Ch.2 build (mapping/groups/looping), Ch.3 KSP GUI. Best
   starting point.
2. **David Hilowitz** — the real working-dev pipeline (RX → Reaper → aubio →
   Creator-Tools export); endless "I sampled a weird thing" videos — models this rig's
   ethos.
3. **The Audio Programmer × NI** — the most-current official Kontakt 8 build series.
4. **Cmd Shift New** (modulation) · **Microphonic Designs** (KSP intro).
5. **This Is Darkness** + **NI Blog** (advanced modulation, granular, Conflux) — the
   ambient/drone technique layer.

## 12. Common pitfalls / gotchas

- **Quick Load works only in Classic View** (the most-cited K8 regression). `research/links/k8-community-whats-new-browser-quickload-gotcha.md`
- **Version lock-in:** opening a library in Kontakt 8 (incl. K8 Player) can stop it
  loading in Kontakt 7 — be deliberate with shared/legacy content.
- **Only Source/Amp/Group-Insert are internally modulatable** (not Instrument
  Insert/Send/Main) — see §5.
- **Kontakt-set loop points can't be exported** — set loops in the DAW if porting (§3).
- **Logic Freeze disabled for multi-out/multitimbral** → Bounce In Place.
- **.NKM multis + non-NKS snapshots** don't play nice with Komplete Kontrol.
- **De-noise stacked samples**; **never loop plucked/decaying sources**; **SSD** for
  purge-on-demand.
- New UI annoyances: MIDI-channel changes hidden behind right-click; can't hide
  instrument UIs when stacking; Tools presets audition on "Piano Uno," not your sample.

## 13. Captured sources (50 — four deep facets)

**`k8-sampling-*` (15):** the instrument-building/looping/hardware-sampling spine —
FIRST STEPS Ch.1–2, Hilowitz pipeline + looping + Auto Sampler, Audio Programmer
build, Creator Tools, drone-loop technique, round robins, 344 Audio guide.
**`k8-engine-*` (12):** what's-new (MusicTech/SynthAnatomy), Conflux, the modulation
walkthrough + the can't-modulate-Insert/Send gotcha, effects/filters/convolution,
factory library, KSP intro, full builds.
**`k8-community-*` (12):** Purge/DFD/Batch-Resave, library management (cogwheel
import, Native Access, NKS), Logic multi-out/multitimbral/freeze/CPU, the new-UI
gotchas.
**`k8-ambient-*` (10) + `k8-loop-*` (1):** evolving-pad + granular recipes,
convolution IRs, bowed→wall (Clinton Shorter), sample-to-instrument, dark-ambient
producers, the Komplete granular trilogy + free libs.

(Full filenames listed in `research/transcripts/` and `research/links/`, each
prefixed by facet.)

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: NI's KONTAKT First Steps, the
Audio Programmer × NI build series, David Hilowitz, Cmd Shift New, Microphonic
Designs, NI Blog (advanced modulation/granular/Conflux/Clinton Shorter), MusicTech /
SynthAnatomy / MusicRadar reviews, Soundiron / Impact Soundworks / Scan Pro Audio /
344 Audio (management), This Is Darkness (ambient artists). **Honesty flags:** NI's
own manual/KB and VI-Control 403 automated fetch, so "what's new" and management
procedures are triangulated across ≥2 independent mirrors/reviews (corroborated, not
first-party); Conflux/Leap internals are review-level, not hands-on tested; exact
Ultimate-vs-Standard library presence should be confirmed on the install drive; no
named shoegaze artist verified (the sourced users are film-score/dark-ambient).
