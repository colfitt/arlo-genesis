# Teenage Engineering OP-1 Field — Deep Research

A working dossier for the one piece of gear in this studio that doesn't sit in a chain at all. The OP-1 Field is the rig's *sketchpad* — a self-contained synth/sampler/sequencer/4-track-tape that you pick up off the desk, not patch into the boards. Most of this document is concerned with where it fits in an ecosystem that already has three serious samplers (Digitakt 2, Octatrack MkII, MPC Sample) and three pedalboards printing to an Apollo: not as another workstation, but as the fast, tactile, "capture-the-moment" box that samples the banjo and the fuzz wall before the idea evaporates, then degrades it on tape.

## 1. Lineage: OP-1 (2011) → OP-1 Field (2022)

Teenage Engineering, based in Stockholm, released the original **Operator-1** in 2011 — a wedge of aluminium that fused a synth, a sampler, a drum machine, an FM radio, and a tape recorder into something the size of a hardback book. It became a genuine cult object: expensive, idiosyncratic, beloved by people who valued *constraint* as a creative engine. Justin Vernon (Bon Iver) famously credits it as the creative kickstarter behind *22, A Million*, using it to grab fragments off the radio and his own records ([Fast Company](https://www.fastcompany.com/90712641/teenage-engineering-op-1-synthisizer)).

The **OP-1 Field** landed at Superbooth 2022 — TE pitched it as "more than a decade of ideas, refinements and improvements" with **over 100 new features** ([Synthtopia](https://www.synthtopia.com/content/2022/05/12/teenage-engineering-intros-1999-op-1-field-portable-sound-studio/)). The headline changes versus the original:

- **Fully stereo signal path, 32-bit** end to end — the original was largely mono and lower bit-depth ([Sound On Sound](https://www.soundonsound.com/reviews/teenage-engineering-op-1-field), [MusicRadar](https://www.musicradar.com/news/op-1-vs-op-1-field-synth-best-buy)).
- **Eight swappable tapes** (the original held only one at a time — you had to back up and wipe to start something new).
- **Longer tape and more storage** — each tape up to ~6 minutes; over 160 minutes of total sample storage; sampling time up to ~20 seconds (was 12) ([teenage.engineering](https://teenage.engineering/products/op-1)).
- **New Dimension synth engine** plus a Vocoder; the rest of the original engine roster carried over, now stereo.
- **FM radio transmitter** (RX *and* TX) — it can broadcast its own FM station to a car stereo or TE's OB-4.
- **Bluetooth Low Energy MIDI**, **USB-C** (power, class-compliant audio, MIDI), a brighter LCD (no longer OLED), a much better speaker with passive radiator, and quadrupled RAM (64 → 256 MB).
- Price: **$1,999** at launch — roughly 2.5× the original's ~$800, which kicked off a real "are TE testing customer loyalty" backlash ([Engadget](https://www.engadget.com/teenage-engineering-op1-tx6-expensive-fun-181029889.html)).

One thing the marketing copy obscures: the keyboard is still **not velocity-sensitive**. It responds to velocity from *external* MIDI controllers and velocity is usable as a mod source, but the onboard keys are on/off ([Sound On Sound](https://www.soundonsound.com/reviews/teenage-engineering-op-1-field)). For this rig that's fine — the Novation 61SL MkIII can drive it with real velocity over USB/BLE.

## 2. Architecture and Controls

The OP-1 Field is organised as four "modes," each on a labelled button, with a **color-coded workflow** built around four rotary encoders — **Blue, Ochre (orange-yellow), Grey, Orange** — that change function per context. The architecture (from the official notebook's routing diagram) flows: **sound source → envelope → FX → 4-track tape → mixer → EQ bus → FX bus → master drive → volume → stereo out**.

- **Synth `[Synth]`** — the 14 marketed synth engines (see §3). `[Shift]+[T1]` opens the browser, `[1]`–`[8]` jump presets.
- **Drum `[Drum]`** — a Drum Sampler engine (24-slot kit mapped across the keyboard) and the **DBox** physical-modelling drum synth. Stereo sampling, with a zoomable waveform editor for trimming/looping.
- **Tape `[Tape]`** — the 4-track stereo tape deck (§2 below in depth). `[Shift]+[Tape]` for settings; `[T1]`–`[T4]` select tracks.
- **Mixer `[Mixer]`** — per-track level/pan, EQ, a master FX slot, and the master output drive compressor. `[Shift]+[Mixer]` shows the live animated routing diagram.
- **Sequencers** — not a mode but a layer that drives synth/drum: **Arpeggio, Endless, Finger, Hold, Pattern, Sketch, Tombola**. Tombola is a physics-based note-spitter; Endless is a generative note-stream; Finger is step-style; Sketch records melodic gestures.
- **Effects** — a single master FX slot per the OP-1 paradigm, chosen from **CWO, Delay, Grid, Mother (reverb), Nitro, Phone, Punch, Spring, Terminal** (Mother is the new lush stereo reverb on the Field).
- **LFOs** — Value, Element, Random, Tremolo, Velocity, and MIDI LFO, assignable to engine parameters (with the caveat that only one internal mod connection is allowed per patch — see §4/§11).
- **Tape (the heart of it):** **4 tracks, each recorded in true stereo**, up to ~6 minutes per tape at default speed, **44.1 kHz at 32-bit**, eight tapes in memory, four tape *styles*: **Studio, Vintage, Porta, Disc (Disk Mini)**. Classic tape ops — splice, cut, lift/drop, varispeed, half/double speed, reverse — are all preserved.

Transport and editing live on dedicated keys: **Lift/Drop** (copy/paste audio or presets to clipboard), **Split/Glue**, **Rec/Play/Stop**, **Rewind/Forward** (which double as octave transpose in synth/drum). An **accelerometer** lets you tilt the unit to modulate parameters.

## 3. Sonic Character — the Engines and the Tape

TE markets **"14 synth engines."** Under the hood, the Field carries the original OP-1's eleven — **FM, Cluster, Digital, DNA, DSynth, Dr Wave, String, Phase, Pulse, Sampler, Voltage** — now stereo, and adds **Dimension** and **Vocoder** ([Synthtopia engine comparison](https://www.synthtopia.com/content/2023/02/10/teenage-engineering-op-1-op-1-field-synth-engines-compared/), [Wikipedia](https://en.wikipedia.org/wiki/Teenage_Engineering_OP-1)). The "14" counts the samplers and sub-variants. Quick character notes:

- **Dimension** — the "basic" subtractive analogue-style synth the original always lacked. Clean mono/poly pads, basses, classic supersaw-adjacent tones. This is the one you reach for to make a *usable bed*, not a weird texture.
- **Cluster** — JP-8000-supersaw-ish, distorted, huge. Drone fuel.
- **FM / Phase / Pulse / Digital** — the gnarly, metallic, ring-mod-and-wave-shaping engines. Where the OP-1's "alien" reputation comes from.
- **String** — string-machine emulation, bass to pads; lovely for shoegaze bedding.
- **DNA / Dr Wave / Voltage / DSynth** — noise generator, talk-box-ish, multi-osc, dual-osc-with-filters respectively. Sound-design oddities.
- **Sampler / Drum Sampler** — the engines that matter most for *this* rig (see §5–6). Feeds from internal mic, line-in, FM radio, or USB.
- **Amp (firmware addition):** a later-firmware engine — amp / compressor / tone / distortion, plus a tuner and phaser — that processes *any* input including the internal mic. On-box grit before the signal ever leaves the unit, which strengthens the Board-1 trick in §5 (two grit stages: amp engine → board fuzz). *(verified against current-firmware tutorials — see the UsageGuide.)*

**The tape is the character.** Even the "clean" Studio mode has the OP-1's signature gentle limiting and stereo glue. **Vintage** adds warmth and saturation; **Porta** emulates a Tascam-style 4-track cassette (wow/flutter, narrowed bandwidth); **Disc** is the lo-fi minidisc-ish mode. Reviewers single out Vintage for "warmth and saturation without losing quality" ([Sound On Sound](https://www.soundonsound.com/reviews/teenage-engineering-op-1-field)). For a drone/doom/"recorded-wrong" aesthetic, Porter and Disc are the money modes — they degrade in exactly the right direction.

## 4. Workflow / Behavioral Notes

The OP-1 is famous for being **constraint-as-feature**. There is **one master FX slot**, **one internal mod connection per patch**, four tape tracks, a two-octave non-velocity keyboard. These are not oversights — they force commitment. You audition fewer options and finish more sketches. That's precisely why it earns its slot next to three vastly more capable Elektron/Akai boxes: those reward planning; the OP-1 rewards *not* planning.

- **Tape-centric, but now with undo:** the tape overdubs and re-records over existing material. The OS 1.5.7 notebook says there's no DAW-style undo, but **later firmware added tape UNDO (hold `[Tape]`+LEFT, ~7 levels) + REDO (`[Tape]`+RIGHT) and a metronome count-in** — so a slip is no longer unrecoverable. Lift/Drop and the eight-tape store remain your primary safety net (you protect a take by copying it elsewhere), and the notebook's "backing up tape or moving sections can protect any previously recorded material" still applies. *(undo/count-in verified against current-firmware tutorials — see the UsageGuide §1.)*
- **Still no project recall in tape:** a tape reel stores *audio only* — not the synth/mixer state that made it. Capture the sound to tape and it's frozen; the patch that made it can change underneath you. (Undo ≠ recall.)
- **The "sketchpad" feel:** the whole thing is instant-on, battery-powered, self-monitoring (speaker), and survives being grabbed off the desk. The friction to *start* is near zero, which is the entire point.

## 5. Role in the Studio / Integration with the Rig

This is the section that matters. The OP-1 Field is **not** a board pedal and **not** a workhorse sequencer — it's the immediate-capture and sound-design satellite. Concretely, in this rig:

- **Sampling the pedalboard wall.** The three boards print stereo to the **UA Apollo x8**. Take a headphone/monitor feed or an Apollo output into the OP-1's **3.5 mm line-in** and sample 20 seconds of the Longsword/Generation-Loss/H90 wall directly. That sampled wall becomes a playable synth-sampler patch or a one-shot on the drum sampler — the fuzz texture, now chromatic across the keys.
- **Sampling the banjo and baritone.** Mic the EBM-5/Gold Tone banjo with the internal mic or feed the VG-800 line out into line-in, grab a phrase, and chop/loop it on tape or into the sampler. (See §6.)
- **As a sound source *into* the rig.** OP-1 **Audio Out → an instrument-level conversion (the EHX Effects Interface on the bench is exactly this line↔instrument utility) → Board 1's front end.** Now the OP-1's Cluster drone or Dimension pad gets fuzzed by the MXR 108 and smeared through Microcosm/Dark Star like a guitar would. This is the most rig-native trick it has.
- **MIDI clock / sync.** Over **USB-C or BLE MIDI** the OP-1 can sync to or from the rig's MIDI brain. Practically, let the Elektrons or the DAW be clock master and have the OP-1 follow, or use the Novation 61SL MkIII to play OP-1 engines with real velocity.
- **USB audio to the Apollo/RME.** The OP-1 is a **class-compliant 2-in/2-out USB interface**. You can stream its stereo out straight into the **Apollo x8** or **RME Babyface Pro FS** as a digital source — no D/A/A/D round-trip, no cables to the analog patchbay. Its onboard tape degradation gets printed clean.

**Versus the other samplers (the key differentiator):**
- **OP-1 Field** = playful, tactile, *fast capture + degrade*. You finish a sketch in one sitting on the couch.
- **Elektron Digitakt 2** = the groove-box workhorse. Tight sequencing, p-locks, the drum/loop engine you build a track on.
- **Elektron Octatrack MkII** = the performance/mangling deep-end. Live resampling, scenes, crossfader chaos — the OP-1's destructive playfulness but with an order of magnitude more depth and a learning cliff.
- **Akai MPC Sample** = standalone chopping/beat-making workstation. The "real" production hub when the sketch graduates.

The OP-1's niche is the **front of the funnel**: catch the idea, give it tape character, then hand it to the Elektrons/MPC (or the DAW via USB) to actually build out.

## 6. Source-Specific Notes (banjo, baritone, the fuzz walls, VG-800)

- **Banjo (EBM-5 / Gold Tone):** the banjo's fast attack/fast decay and bright 2–4 kHz content sample beautifully as *one-shots* and short loops. Sample a single banjo roll, drop it on the **Drum Sampler** across the keys, and you have a chromatic, gamelan-ish plucked instrument. Run it through **Vintage** or **Porta** tape to roll off the ice-pick highs. This is the OP-1 doing something none of the boards can: turning the banjo into a *keyboard*.
- **Baritone Jazzmaster:** sample a drone or a single chord, then varispeed/half-speed it on tape for sub-octave doom beds. The 32-bit stereo path keeps it clean until *you* choose to wreck it.
- **The fuzz walls:** resample the printed Apollo output (Board 1's Hizumitas/Longsword wall) into the synth sampler — granular-ish stutters via the Sketch/Tombola sequencers turn a static wall into a moving texture.
- **VG-800 / GK-5:** the VG-800's synth and modeled-amp outputs are line level; through the EHX Effects Interface they sample cleanly. Modeled-pad → OP-1 sampler → tape degradation is a tidy path to a "broken synth choir."
- **Resampling on-box:** the OP-1's own sound-on-sound — sample its tape back into a synth/drum engine — is the canonical lo-fi degradation loop. Each pass through Porta/Disc tape adds generation loss, which is exactly this studio's stated aesthetic.

## 7. Famous Users

The OP-1 has a genuine, decade-deep artist following (mostly the original; the Field is its successor):

- **Justin Vernon / Bon Iver** — the canonical example; credits the OP-1 across *22, A Million* ([Fast Company](https://www.fastcompany.com/90712641/teenage-engineering-op-1-synthisizer), [NME](https://www.nme.com/photos/19-much-loved-musicians-turned-super-producers-from-albert-hammond-jr-and-bon-iver-to-trent-reznor-1407476)).
- **Trent Reznor, Thom Yorke (Radiohead), Childish Gambino, Deadmau5, Skrillex, John Mayer** are all cited among notable OP-1 users ([Creative Computing Studio writeup](https://wordpress.cs.vt.edu/ccs2018f/2018/09/19/music-in-the-digital-age-the-op-1-and-other-new-tools/)).
- On the demo/education side, **Red Means Recording (Jeremy Blake)**, **Cuckoo**, and **Hainbach** are the defining OP-1/OP-1 Field YouTube voices ([SoundTech tutorials roundup](https://www.soundtech.co.uk/musicians-blog/the-best-teenage-engineering-op-1-tutorials-reviews-and-demos.html), [Perfect Circuit / Hainbach review](https://www.perfectcircuit.com/signal/teenage-engineering-op-1-field-review)).

The honest caveat: most documented artist use is the *original* OP-1. The Field is new enough (2022) that its own discography is still accruing, but it's the same instrument philosophy.

## 8. Connectivity / Power / I/O

- **Audio In:** 3.5 mm stereo jack. 13 kΩ input impedance, 0–31 dB analog gain, max level 8 dBU at 2 Vrms, S/N typically 98 dBA (per official notebook spec).
- **Audio Out:** 3.5 mm stereo jack. Max 8 dBU at 2 Vrms, S/N typically 124 dBA. M-1 headset (mic + earphone) compatible.
- **USB:** USB Type-C — power, **Audio Class 1.0 host & device** (with support for Class 2.0 devices), and MIDI. Functions as a class-compliant **2-in/2-out** interface.
- **Bluetooth:** BLE MIDI, 2402–2480 MHz, < 10 dBm.
- **FM Radio:** transmitter 87.5–108 MHz / 49.56 dBm; receiver 87.5–108 MHz.
- **Power:** internal rechargeable battery, **~24 h** life; TE advises recharging at least every 6 months to keep the cell healthy.
- **Mounting:** underside has dual Velcro rings (plus included spares) and a passive audio radiator behind the speaker.
- **The dongle situation:** the 3.5 mm jacks mean you live on **TRS-to-1/4"** and **3.5 mm-to-3.5 mm** adapters to interface with a 1/4"/XLR studio. Keep a small adapter kit with the unit. USB-C is the cleanest path into the Apollo/RME and avoids the analog adapter shuffle entirely.

## 9. Pairing Recommendations (by name)

- **Into the UA Apollo x8 / RME Babyface Pro FS:** USB-C for clean digital capture; 3.5 mm-to-1/4" into an analog input if you want to re-color through Unison preamps. Default to USB for sketches, analog when you want the Apollo's character.
- **Into Board 1 (front of the rig):** OP-1 Out → **EHX Effects Interface** (line→instrument) → VG-800/Polytune front end, so the OP-1 gets fuzzed and smeared like a guitar.
- **Versus / alongside Digitakt 2:** let the **Digitakt 2** sequence and hold the groove; sample its output or feed it OP-1 one-shots. OP-1 is the idea, Digitakt is the arrangement.
- **Versus / alongside Octatrack MkII:** the OP-1 captures, the **Octatrack** mangles in performance. Resample OP-1 tape into the Octatrack for live scene/crossfader destruction.
- **Versus / alongside MPC Sample:** OP-1 sketch → **MPC** for full chop/beat production. The MPC is where a sketch becomes a track.
- **With the Novation 61SL MkIII:** drive OP-1 engines with real velocity over USB/BLE — the workaround for the non-velocity keys.
- **MIDI clock:** slave the OP-1 to the rig's master clock (DAW or Elektron) so tape loops lock to the boards' tempo-synced delays (Big Time, H90).

## 10. Reviews and Demos (real links)

- [Sound On Sound — OP-1 Field review](https://www.soundonsound.com/reviews/teenage-engineering-op-1-field) — the most thorough written review; best on tape modes, Mother reverb, and the velocity/mod limitations.
- [MusicRadar — OP-1 Field review](https://www.musicradar.com/reviews/teenage-engineering-op-1-field) and [OP-1 vs OP-1 Field buyer's guide](https://www.musicradar.com/news/op-1-vs-op-1-field-synth-best-buy).
- [Perfect Circuit — OP-1 Field review (Hainbach demo)](https://www.perfectcircuit.com/signal/teenage-engineering-op-1-field-review).
- [Gearnews — OP-1 Field review](https://www.gearnews.com/teenage-engineering-op-1-field-review/).
- [Synthtopia — OP-1 vs OP-1 Field synth engines compared](https://www.synthtopia.com/content/2023/02/10/teenage-engineering-op-1-op-1-field-synth-engines-compared/) — the clearest engine-by-engine breakdown.
- [Adrian Thomas — OP-1 Field: A Guitarist's Review](https://adrianthomas.com/op-1-field-a-guitarists-review) — relevant to sampling guitar/strings into it.
- [Teenage Engineering — official OP-1 Field product page](https://teenage.engineering/products/op-1).
- Red Means Recording and Cuckoo's YouTube channels are the go-to video demos ([roundup](https://www.soundtech.co.uk/musicians-blog/the-best-teenage-engineering-op-1-tutorials-reviews-and-demos.html)).

## 11. Quirks / Known Issues

- **Price controversy.** $1,999 at launch — ~2.5× the original — and TE's accessories (a £249 leather wrap) drew open criticism. The "are TE testing customer loyalty" framing is real and worth knowing before recommending it as anything but a luxury sketchpad ([Engadget](https://www.engadget.com/teenage-engineering-op1-tx6-expensive-fun-181029889.html)).
- **No velocity keyboard.** Onboard keys are on/off; you need an external MIDI controller for expressive velocity (the 61SL covers this).
- **One internal mod connection per patch** and **one master FX slot** — deliberate constraints, but limiting if you expect modular-style routing.
- **Tape stores audio only**, not instrument/mixer state — no project recall the way a DAW or Elektron pattern works.
- **Durability questions.** The LCD is no longer the original's OLED. The Velcro-ring mounting (vs bolts) raised some confidence concerns in reviews. The aluminium shell is otherwise solid but the unit is a premium object you'll baby.
- **Adapter dependency.** 3.5 mm I/O in a 1/4"/XLR studio means living on dongles unless you route via USB.
- **No SD/expandable storage** — internal storage only; you manage tapes/samples over USB.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Portable synth / sampler / drum machine / 4-track tape / sequencer |
| Release | 2022 (successor to 2011 OP-1) |
| Synth engines | 14 marketed (11 original carried over + Dimension + Vocoder; incl. Drum/Synth samplers) |
| Drum | Drum Sampler engine + DBox physical-model drum synth |
| Sequencers | Arpeggio, Endless, Finger, Hold, Pattern, Sketch, Tombola |
| Tape | 4 tracks, true stereo each; ~6 min/tape; 8 tapes stored; 44.1 kHz / 32-bit |
| Tape styles | Studio, Vintage, Porta, Disc |
| Effects | CWO, Delay, Grid, Mother (reverb), Nitro, Phone, Punch, Spring, Terminal (1 master slot) |
| Sampling | Up to ~20 s per sample; 160+ min total storage; src: mic / line-in / FM / USB |
| Signal path | Fully stereo, 32-bit |
| Audio In | 3.5 mm stereo, 13 kΩ, 0–31 dB gain, max 8 dBU @ 2 Vrms |
| Audio Out | 3.5 mm stereo, max 8 dBU @ 2 Vrms; M-1 headset compatible |
| USB | USB-C; Audio Class 1.0 host & device (supports Class 2.0); MIDI; 2-in/2-out interface |
| Bluetooth | BLE MIDI, 2402–2480 MHz, < 10 dBm |
| FM Radio | TX 87.5–108 MHz / 49.56 dBm; RX 87.5–108 MHz |
| Power | Internal rechargeable, ~24 h; recharge ≥ every 6 months |
| RAM | 256 MB (4× the original's 64 MB) |
| Display | LCD (original was OLED) |
| Dimensions | 300 × 120 × 20 mm |
| Weight | 590 g / 20.8 oz |
| Launch price | $1,999 USD |

Sources: [teenage.engineering product page](https://teenage.engineering/products/op-1), official OP-1 Field Notebook (§10.10 Technical Specifications), [Sound On Sound](https://www.soundonsound.com/reviews/teenage-engineering-op-1-field). *Engine-name granularity ("14") is TE's marketing count; the underlying engine list is verified against [Synthtopia](https://www.synthtopia.com/content/2023/02/10/teenage-engineering-op-1-op-1-field-synth-engines-compared/) and [Wikipedia](https://en.wikipedia.org/wiki/Teenage_Engineering_OP-1).*

## 13. Starting-Point Workflows

**(a) Sample-the-banjo sketch** — turn the banjo into a keyboard
1. Mic the EBM-5 with the internal mic (or VG-800 line-out → line-in). Sample a single roll/phrase into the **Drum Sampler**.
2. It maps chromatically across the keys — play it like a gamelan/plucked-string instrument.
3. Route through **Vintage** or **Porta** tape to tame the highs. Record a take to one tape track.
4. Add a **Dimension** pad on track 2 underneath for a bed.

**(b) Tape-degraded loop** — lo-fi generation-loss texture
1. Record any source (banjo, baritone drone, a synth pad) to tape track 1 in **Porta** mode.
2. Lift the take, drop it into the **Synth Sampler**, play it back, re-record to track 2 — repeat 2–3× to stack generation loss.
3. Set a **Tape Loop** and varispeed/half-speed for sub-octave doom. Resample once more for the "recorded-wrong" finish.

**(c) Synth-pad bed** — clean foundation, then wreck it later
1. **Dimension** or **String** engine, slow attack, **Mother** reverb in the master FX slot.
2. Hold a chord with the **Hold** sequencer; record a long take to tape (Studio mode, keep it clean).
3. Send OP-1 Out → EHX Effects Interface → Board 1, and let the rig's fuzz/granular pedals do the wrecking instead of the tape.

**(d) Resample-the-wall** — the pedalboard as an instrument
1. Print a fuzz/texture wall from Board 1 to the **Apollo x8**; feed an output back into the OP-1 line-in.
2. Sample 20 s into the **Synth Sampler**; it's now chromatic across the keys.
3. Drive it with the **Tombola** or **Sketch** sequencer for moving, stuttering re-pitched texture.
4. Bounce to tape (Disc mode) for extra lo-fi, then USB the result back into the Apollo/DAW.

## 14. Versus Alternatives

- **vs Elektron Digitakt 2** — the Digitakt is the *groove workhorse*: deep sequencing, parameter locks, a focused sampling/drum engine you build whole tracks on. The OP-1 has nothing like its sequencer depth or pattern recall. Reach for the OP-1 when you want to *capture and play*, the Digitakt when you want to *arrange and lock*. They're complementary, not competitive.
- **vs Elektron Octatrack MkII** — the Octatrack is the OP-1's destructive-playfulness taken to a performance extreme: live resampling, scenes, crossfader mangling, flex/static machines. It out-depths the OP-1 in every direction but has a brutal learning curve. The OP-1 is the box you actually pick up; the Octatrack is the box you commit a month to.
- **vs Akai MPC Sample** — the MPC is the standalone production hub: chopping, beat-making, full arrangement. The OP-1 sketch *graduates* to the MPC. Different stages of the same pipeline.
- **vs original OP-1** — the Field is the better instrument on paper (stereo, 32-bit, 8 tapes, Dimension/Vocoder, BLE, USB-C, FM TX) but costs ~2.5× and trades the OLED for an LCD. If you already had an OG OP-1 the upgrade is real but not essential; buying in fresh, the Field is the one to get if budget allows.

In *this* studio, the OP-1 Field's niche is singular and defensible: it's the only sampler here that's a **couch instrument**. The Elektrons and MPC reward sitting down with intent; the OP-1 rewards grabbing it mid-thought, sampling the banjo or the fuzz wall, degrading it on tape, and handing a finished sketch to the workhorses. It earns its slot not by being the most capable box on the desk — it's clearly the least — but by being the one that *starts* things.

## Sources

- [Teenage Engineering — OP-1 Field product page](https://teenage.engineering/products/op-1)
- Official OP-1 Field Notebook (SynthDawg Producer Guides, OS 1.5.7) — §1.6 Architecture, §2 Tape, §10.10 Technical Specifications (local PDF)
- [Sound On Sound — OP-1 Field review](https://www.soundonsound.com/reviews/teenage-engineering-op-1-field)
- [MusicRadar — OP-1 Field review](https://www.musicradar.com/reviews/teenage-engineering-op-1-field)
- [MusicRadar — OP-1 vs OP-1 Field](https://www.musicradar.com/news/op-1-vs-op-1-field-synth-best-buy)
- [Synthtopia — TE intros $1,999 OP-1 Field](https://www.synthtopia.com/content/2022/05/12/teenage-engineering-intros-1999-op-1-field-portable-sound-studio/)
- [Synthtopia — OP-1 / OP-1 Field synth engines compared](https://www.synthtopia.com/content/2023/02/10/teenage-engineering-op-1-op-1-field-synth-engines-compared/)
- [Wikipedia — Teenage Engineering OP-1](https://en.wikipedia.org/wiki/Teenage_Engineering_OP-1)
- [Perfect Circuit — OP-1 Field review (Hainbach demo)](https://www.perfectcircuit.com/signal/teenage-engineering-op-1-field-review)
- [Gearnews — OP-1 Field review](https://www.gearnews.com/teenage-engineering-op-1-field-review/)
- [Engadget — TE Field products testing customer loyalty](https://www.engadget.com/teenage-engineering-op1-tx6-expensive-fun-181029889.html)
- [Fast Company — How the OP-1 went from cult to classic](https://www.fastcompany.com/90712641/teenage-engineering-op-1-synthisizer)
- [NME — musicians turned producers (Bon Iver / OP-1)](https://www.nme.com/photos/19-much-loved-musicians-turned-super-producers-from-albert-hammond-jr-and-bon-iver-to-trent-reznor-1407476)
- [SoundTech — best OP-1 tutorials, reviews and demos](https://www.soundtech.co.uk/musicians-blog/the-best-teenage-engineering-op-1-tutorials-reviews-and-demos.html)
- [Adrian Thomas — OP-1 Field: A Guitarist's Review](https://adrianthomas.com/op-1-field-a-guitarists-review)
