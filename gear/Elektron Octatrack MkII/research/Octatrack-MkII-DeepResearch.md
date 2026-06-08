# Elektron Octatrack MkII — Deep Research

A working dossier for the deepest, most dangerous box in the studio. The Octatrack MkII is not on the guitar board — it lives downstream of the whole rig, on the desk, where it can take the pedalboard's stereo print, swallow it whole, and re-sequence it into something the guitar never actually played. Where the Digitakt 2 is the disciplined drum/sample workhorse and the OP-1 Field is the sketchpad, the Octatrack is the rig's **live-mangling and resampling brain** — the one machine here that can sit in the signal path as a live effects processor *and* a sampler *and* an 8-track sequencer at the same time. Most of this document is concerned with that role: how the Thru machines eat the pedalboard's degraded fuzz walls and banjo loops, how the crossfader turns a static drone into a performance, and how to keep all that power from collapsing under its own famously brutal learning curve.

## 1. Lineage: Octatrack DPS-1 → MkII

The original **Octatrack DPS-1** ("Dynamic Performance Sampler") shipped in **January 2011** ([Elektron Octatrack — Wikipedia](https://en.wikipedia.org/wiki/Elektron_Octatrack)), Elektron's first sampler since the Machinedrum UW. Across what Elektron's own manual calls its "seven year life span" it became the de-facto standalone live-sampling instrument — the box that, more than any other, made "dawless" performance credible. Eight stereo tracks, a crossfader, a step sequencer, live resampling: nobody else was doing all of it in one enclosure. The original earned a cult reputation in equal parts for its capability and for the savagery of its workflow; "the Octatrack will hate you for at least six months" is folklore for a reason.

The **MkII** arrived in 2017 and is, deliberately, **a hardware refresh rather than a new instrument**. Per [MusicRadar's review](https://www.musicradar.com/reviews/elektron-octatrack-mkii) and [Sound on Sound](https://www.soundonsound.com/reviews/elektron-mkii-analog-four-analog-rytm-octatrack), there are *no MkII-exclusive features* — every OS capability was eventually pushed to original owners too ([CDM](https://cdm.link/newswires/original-octatrack-owners-get-mkii-features/)). What changed is the body:

- **OLED screen** — the crisp 128×64 OLED replaces the original's dimmer LCD; far more legible on a dark stage.
- **Backlit buttons** rated ~50 million presses, plus **dedicated front-panel track/scene buttons** that cut down menu-diving versus the MkI's `[FUNC]`-heavy layout ([Mark Mosher's MkI-vs-MkII deep dive](https://markmoshermusic.com/2017/07/04/elektron-octatrack-mii-vs-octatrack-mki-a-deeper-look-beyond-the-bullet-points/)).
- **Contactless "silky smooth" crossfader** replacing the MkI's Infinium optical fader — shorter throw, lighter friction, more DJ-mixer feel.
- **Impedance-balanced inputs** — the four external inputs went from unbalanced to balanced TRS, and output level rose by roughly **+6 dB** versus the MkI.
- Upgraded hi-res encoders.

For this rig the takeaway is: the MkII is the *right* one to own specifically because of the balanced inputs (clean interface with the Apollo/Babyface and the pedalboard) and the brighter screen for live work — but you are buying refined ergonomics on a 2011 engine, and that engine is still the gold standard.

## 2. Architecture & Controls

The Octatrack is organized hierarchically, and understanding the data model is more than half the battle. From the [manual](manuals/elektron-octatrack-mkii-manual.pdf):

- **Set → Project → Bank → Pattern / Part.** A **Set** is the top level (one per CompactFlash card's worth of work) and holds one shared **Audio Pool** plus near-unlimited **Projects**. A **Project** holds 16 banks, 8 arrangements, 128 Flex sample slots, 128 Static sample slots, and the BPM. Each **Bank** hosts 16 patterns and 4 **Parts**; a Part holds machine assignments, track parameters, FX assignments, and 16 scenes, and a pattern is always linked to a Part. This is why "I changed one knob and the whole song changed" happens — you edited the Part, not the pattern.
- **8 audio tracks + 8 MIDI tracks** per pattern. Each audio track hosts one **machine**.
- **The five machine types** (Appendix A) — the heart of the instrument:
  - **Flex** — sample lives in **RAM**; the most malleable. Pitch, timestretch, slice, retrig, reverse, instant start-point scrubbing. This is where live-recorded buffers and loops go.
  - **Static** — sample **streamed from the CompactFlash card**, so a single sample can be **up to 2 GB**. Same mangling parameters; built for long backing-track-length material.
  - **Thru** — a **utility machine that listens to the physical inputs** (INAB / INCD) and passes them through the track's FX and amp. *This is the rig-integration machine.* It must be triggered (a sample trig on the sequencer) to start passing audio.
  - **Neighbor** — listens to the *output of the preceding track*, letting you chain tracks into multi-stage FX racks (can't be on track 1 or 5).
  - **Pickup** — the looper machine, hard-linked to the track recorder; overdub/loop-pedal behavior with timestretch sync.
- **Track recorders (8) + recorder buffers.** Each track has a recorder that can sample the inputs *or* internal sources (resampling). `[REC1]`/`[REC2]` capture the external input pairs; `[REC3]` captures internal. This is the resampling engine.
- **The sampler/editor.** An onboard **Audio Editor** does trim, slice (auto/grid/transient), and per-sample attributes (loop, timestretch mode, pitch). Timestretch algorithms keep loops locked to the project BPM.
- **The sequencer.** Elektron's parameter-lock step sequencer: per-step trigs with **p-locks** on any parameter, **sample locks** (different sample per step), conditional/probability trigs, micro-timing, swing, scale-per-track, retrig. Two recording modes — **Grid** (step-program) and **Live**.
- **Scenes + Crossfader.** Each Part holds **16 scenes**; you assign one to **Scene A** and one to **Scene B**, and the crossfader morphs between the two sets of locked parameter values, interpolating smoothly. This is the performance soul of the machine (see §4).
- **Two FX blocks per track**, each choosing from **14 effects** (see §3), plus **three assignable LFOs per track** with a custom LFO Designer.
- **Front panel** (from the manual): `[REC1/2/3]`, eight `[TRACK]` keys (also showing mute/cue state), `LEVEL`, four `DATA ENTRY` encoders, `[TEMPO]`, `[SCENE A]`/`[SCENE B]`, the 16-step `[TRIG]` row, and the crossfader.

## 3. Sonic Character

The Octatrack has no "sound" of its own in the way a fuzz does — it sounds like *whatever you feed it, broken in a controllable way*. Its character is the character of digital sample manipulation taken to an extreme: timestretch artifacts, slice-stutter, pitch-shimmer, the grain of a loop pushed past where it wants to go. Elektron's own framing calls it a "radical sound processor" and an "audio mangler" ([manual §2.1](manuals/elektron-octatrack-mkii-manual.pdf)).

The 44.1 kHz / 24-bit converters are clean — this is not a lo-fi box by default — but the **14-effect engine per FX slot, two slots per track** can make it filthy on demand. The processor list (Appendix B): **multimode resonant filter (12/24 dB), 2-band parametric EQ, DJ-style kill EQ, 2–10 stage phaser, flanger, 2–10 tap chorus, spatializer, comb filter, Dynamix compressor, Lo-Fi Collection (bit/sample-rate crush, distortion), Echo Freeze Delay, Gatebox Plate Reverb, Spring Reverb, Dark Reverb.** The **Echo Freeze Delay** and **Lo-Fi Collection** are the ones that matter most for this aesthetic — the freeze delay can capture and infinitely sustain a fragment, and the Lo-Fi block degrades it on the way out.

But the legendary part is the **live-remix capability**: the combination of real-time resampling, the slice engine, conditional trigs, and the crossfader means you can capture a four-bar fuzz wall and, without ever touching a DAW, chop it into eight slices, p-lock pitch and filter per step, scatter it with probability trigs, and crossfade between the clean loop and the destroyed version — live. No other box in this studio does that.

## 4. Workflow & Behavioral Notes

**The learning curve is real and it is the headline quirk.** MusicRadar calls the workflow "complex and often challenging" and tells you to "expect to spend a lot of time reading the manual." This is the price of admission. The Octatrack does not reward casual use; it rewards a built template Project and muscle memory.

Three behavioral truths to internalize:

1. **Parts, not patterns, hold the sound.** Tweaks to machine assignments, FX, and scenes live in the **Part** shared by multiple patterns. Save Parts deliberately; use **Part Reload** (`[FUNC]`+`[CUE]`) live to snap back to a saved state after heavy tweaking.
2. **The crossfader is an instrument.** Assigning two scenes and performing the fader is the single most expressive thing the machine does. Scene locks have priority over p-locks during a fade, so transitions stay smooth. Use the dedicated **scene volume-lock parameters (XLV/XVOL/XDIR)** for equal-power crossfades between two sources without the level dip you'd otherwise get at center.
3. **Resampling is the loop.** Capture → mangle → resample the mangle → mangle *that*. The recorder-buffer-back-into-a-Flex-machine cycle is where "capture and destroy" lives. Everything is auto-cached to the CF card; only **Save Project** before pulling the card.

## 5. Role in the Studio / Integration with the Rig

**This is the section that justifies the box.** The Octatrack is the one piece of gear here that can sit *inside* the guitar rig's signal path as a live processor while also being a sequencer and sampler. The integration angle is unique among the owner's samplers.

**The pedalboard → Thru machine, live.** The three guitar boards end in a stereo print (CE-2W/Deco out of Board 1, through Board 2's texture section, into Board 3's Generation Loss → Big Time → MOOD → Blooper → Chroma Console → H90 → tape stage). That stereo pair is the most processable signal in the building. Patch it (or a parallel send/the Apollo's monitor outs) into the Octatrack's **balanced inputs A/B**, drop a **Thru machine** on a track, place a trig, and the entire degraded wall is now flowing *through* the Octatrack's filters, LFOs, and 14-effect FX blocks in real time ([manual §16.1.2 / §16.3](manuals/elektron-octatrack-mkii-manual.pdf)). At that moment you can:

- **Resample it** on the fly with the track recorder (`[REC1]`) into a buffer.
- **Slice and re-sequence** the captured wall into a new rhythmic part.
- **Crossfade** between the live pedalboard and the mangled capture using scenes.

Two routing methods from the manual: the **DIR method** (MIXER menu, DIR AB = 127, monitors the input straight to the mains with no track cost) and the **Thru machine method** (DIR = 0, the input only exists through a track, so it gets that track's FX and can be muted/processed). For this rig the **Thru method is the goal** — it's what turns the Octatrack into a live effects unit for the pedalboard.

**MIDI clock / the dawless brain.** Over its single 5-pin MIDI Out, the Octatrack can **send MIDI clock and transport** to slave the rest of the electronic ecosystem (Digitakt 2, the MIDI-equipped Chase Bliss boxes, Microcosm, H90, Chroma Console — all of which take MIDI on the boards), or it can **slave to** an external clock. The 8 MIDI tracks also sequence external gear (the VG-800, the 61SL MkIII's targets, synths).

**The classic Digitakt + Octatrack pairing.** The canonical Elektron dawless duo: **Digitakt 2 sequences/drives drums and tight one-shots; the Octatrack mangles, resamples, and performs** ([59perlen dawless jam](https://www.59perlen.com/post/dawless-octatrack-housejam-digitakt-digitone-novationpeak-roland-tb03)). The Digitakt is the disciplined timekeeper; the Octatrack is the chaos engine on top. Run Digitakt as clock master or let the Octatrack lead — either works.

**Into the Apollo x8 / Babyface.** The balanced main outs (and separate **cue outs**) print cleanly to the **UA Apollo x8** or **RME Babyface Pro FS**. Cue outs let you audition/record a track in isolation — e.g., print the resampled banjo loop on the cue bus to the interface while the mains carry the full performance.

## 6. Source-Specific Notes (banjo, fuzz walls, baritone, VG-800)

This rig's raw material is unusually good Octatrack food because it's already textural and sustained:

- **Sustained fuzz walls** (Longsword / Hizumitas / Brothers stacks) are *ideal* resampling sources — a dense, droning capture timestretches without the gaps and clicks that kill transient material. Capture a wall, set the Flex machine's timestretch to hold it indefinitely, and you have an evolving bed under the live guitar.
- **Banjo loops** (Gold Tone EBM-5 via GK-5 → VG-800) are bright and fast-decaying — the opposite extreme. Sliced on transients and re-triggered with conditional trigs, banjo rolls become glitchy, banjo-as-lead-as-sequence material. The timestretch transient-sensitivity (`TSNS`) parameter is worth tuning here so the algorithm tracks the picking attack.
- **Baritone drones** (Baritone Jazzmaster) sit between — sustained enough to resample cleanly, low enough that pitch-shifting up an octave (Flex `PTCH`) yields useful shimmer layers.
- **The VG-800's synth/COSM patches** — modeled pads and guitar-synth output are continuous-waveform sources that resample and timestretch beautifully into drones.

The aesthetic match is exact: "degraded, recorded-wrong, sustained walls, banjo-as-lead." The Octatrack's slice/p-lock/Lo-Fi chain is a machine purpose-built to make on-aesthetic destruction *repeatable and performable* rather than a happy accident.

## 7. Famous Users

The Octatrack has a genuine, deep artist following — unusual for a sampler this difficult. Be honest about which attributions are *documented* vs. merely *name-dropped* (verified during the usage-research pass — see `research/links/artist-verification-roundup.md`):

**Well-evidenced (on-record interviews / filmed live rigs):**
- **Alessandro Cortini** (Nine Inch Nails) — crossfader+scenes to play chords from ~32 Buchla samples; repeated on-record interviews.
- **Panda Bear** (Noah Lennox) — two units, "DJ the stems" live (Reverb interview + Sydney Opera House 2018).
- **Stimming** — rebuilt his live show around two Octatrack MkIIs, one as the mixer (Cercle set; his own comments).
- **Mumdance** (Jack Adams) — one-shot live track-building with a TR-909 (Elektron spotlight).
- **Surgeon** (Anthony Child) — OT as the foundation of his live techno rig + Faderfox (CDM / RA).
- **Kangding Ray** — gear listings + Boiler Room live electronics; OT plausible, exact live role not transcribed (*mostly verified*).

**Name-dropped, NOT confirmed** (photos/Twitter/anecdote only — do not repeat as fact): The Haxan Cloak, Terence Fixmer, Jacques Greene, Shifted, Paul Birken, James Ruskin & Mark Broom / The Fear Ratio. **Karenn** (Blawan & Pariah) is flagged as possibly abandoned ("hardly touched it"). These all trace to the [Elektronauts "high-profile OT users" thread](https://www.elektronauts.com/t/high-profile-ot-users/15652) without supporting evidence.

It skews techno/experimental/ambient, and the verified through-line is *live performance* — these are people using it on stage, not just in the box.

## 8. Connectivity / Power / I/O

| I/O | Detail |
|---|---|
| Audio inputs | 4 × 1/4" **impedance-balanced** (Input A/B and C/D pairs); accept TRS balanced or TS unbalanced |
| Main outs | 2 × 1/4" impedance-balanced (L/R) |
| Cue outs | 2 × 1/4" impedance-balanced (L/R) — separate cue bus |
| Headphones | 1 × 1/4" stereo TRS |
| MIDI | DIN **In / Out / Thru** (5-pin) |
| USB | Hi-Speed USB 2.0 (disk mode / OS transfer; **no USB audio, no Overbridge**) |
| Storage | CompactFlash reader |
| Power | 12 V DC, 2 A, center-positive 5.5 × 2.5 mm barrel (PSU-3b/3c); ~7 W typical |

Use **only the bundled Elektron PSU** — the manual explicitly warns that wrong adapters can damage the unit and void warranty. Note this is **12 V**, *not* the 9 V the pedalboard runs on — it cannot share a pedal power supply. There's also an internal battery for pattern/part memory (holds data ~6 years; "BATTERY LOW" warns when it's time).

## 9. Pairing Recommendations (by name)

- **Digitakt 2 (the headline pairing).** Digitakt = drums/disciplined sampling/clock; Octatrack = resampling, performance, FX. The definitive dawless duo here. Clock-link over MIDI DIN.
- **The pedalboard, via Thru machine (the rig-defining setup).** Stereo print of Boards 1–3 → Octatrack balanced inputs A/B → Thru machine track → live FX + resample. The single strongest integration of any box in the studio.
- **VG-800 / Novation 61SL MkIII.** Octatrack MIDI tracks sequence the VG-800; the 61SL plays/controls. Octatrack as MIDI clock master to the whole electronic rig.
- **UA Apollo x8 / RME Babyface Pro FS.** Balanced main outs print cleanly; cue outs give an independent stem to the interface.
- **vs OP-1 Field / MPC Sample.** Different jobs (see §14) — the OP-1 sketches, the MPC composes standalone, the Octatrack performs and destroys.

## 10. Reviews & Demos

- [MusicRadar — Octatrack MkII review](https://www.musicradar.com/reviews/elektron-octatrack-mkii) — best concise verdict; "no other hardware sampler can match the Octatrack for the sheer amount of creative depth."
- [Sound on Sound — Elektron MkII trio (A4/Rytm/Octatrack)](https://www.soundonsound.com/reviews/elektron-mkii-analog-four-analog-rytm-octatrack) — MkI-vs-MkII hardware detail.
- [Mark Mosher — MkII vs MkI deep look beyond the bullet points](https://markmoshermusic.com/2017/07/04/elektron-octatrack-mii-vs-octatrack-mki-a-deeper-look-beyond-the-bullet-points/) — the most thorough hardware comparison.
- [macProVideo — Octatrack MkII OS 1.30C review](https://macprovideo.com/article/audio-hardware/review-elektron-octatrack-mkii-os-1-30c).
- [CDM — original Octatrack owners get MkII features](https://cdm.link/newswires/original-octatrack-owners-get-mkii-features/) — confirms no MkII-exclusive features.
- [Cuckoo — Octatrack Tutorial #1 (YouTube)](https://www.youtube.com/watch?v=NrhPOGzn7LI) — the canonical beginner on-ramp.
- [Cuckoo — Octatrack Loopbox / Pickup Machine tutorial (YouTube)](https://www.youtube.com/watch?v=JnbQ8ichm54) — looping workflow.
- [Sound on Sound — original Octatrack DPS-1 review](https://www.soundonsound.com/reviews/elektron-octatrack-dps1) — historical context.

## 11. Quirks / Known Issues

- **The learning curve.** The defining caveat. Budget months, build a template Project, watch Cuckoo before touching anything serious.
- **CompactFlash, not SD.** It needs **UDMA, ≥133x (~20 MB/s) R/W, FAT16/FAT32 (prefer FAT32), up to 64 GB** cards. CF is now a slightly archaic, pricier format — buy a known-good card and a backup. **Never pull the card while the CARD STATUS LED blinks** (data corruption).
- **Auto-cache vs Save.** Work auto-caches, but you must **Save Project** before removing the card or you can lose the saved-state safety net (Reload depends on a prior Save).
- **No Overbridge, no USB audio/MIDI.** Unlike newer Elektron boxes, the Octatrack does **not** integrate over USB — it's MIDI-DIN-and-audio-cables only. Plan the studio routing accordingly (this is fine for the analog-cable-centric rig, but worth knowing). USB *can* inject computer noise into the outputs — use balanced cables.
- **12 V power** — not pedalboard-compatible; needs its own PSU.
- **Single mono FX per source pair caveats** and **two FX slots per track** mean heavy FX racks eat tracks (Neighbor chaining is the workaround).
- No widely reported reliability failures; Elektron build quality is excellent. The internal memory battery is the only consumable.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | 8-track stereo dynamic performance sampler / sequencer |
| Audio tracks | 8 stereo |
| MIDI tracks | 8 |
| Sample slots | 256 per project (128 Flex / 128 Static) |
| Machine types | Flex, Static, Thru, Neighbor, Pickup |
| Max sample size | 2 GB (Static, streamed from CF) |
| FX | 2 FX blocks/track, 14 effect types each; 3 LFOs/track |
| Scenes / crossfader | 16 scenes per Part; A/B crossfader morph |
| Converters | 44.1 kHz, 24-bit D/A and A/D |
| Main out S/N | 104 dB (20–20,000 Hz) |
| Input S/N | 106 dB (20–20,000 Hz) |
| Audio inputs | 4 × 1/4" impedance-balanced (A/B, C/D) |
| Main outs | 2 × 1/4" impedance-balanced |
| Cue outs | 2 × 1/4" impedance-balanced |
| Headphones | 1 × 1/4" stereo TRS |
| MIDI | In / Out / Thru (5-pin DIN) |
| USB | Hi-Speed USB 2.0 (no audio/Overbridge) |
| Screen | 128 × 64 OLED |
| Storage | CompactFlash (UDMA ≥133x, FAT32, ≤64 GB); 32 GB card included |
| Power | 12 V DC, 2 A, center-positive 5.5×2.5 mm; ~7 W typical |
| Dimensions | 340 × 184 × 63 mm (13.3 × 7.2 × 2.5 in) |
| Weight | ~2.3 kg (5 lbs) |

Sources: [Elektron Octatrack MkII specs](https://www.elektron.se/product/octatrack-mkii?section=specs), [manual](manuals/elektron-octatrack-mkii-manual.pdf).

## 13. Starting-Point Workflows

Four named templates to build as separate Parts/Projects.

**(a) Live-Mangle-the-Pedalboard** — the rig-defining patch
- Pedalboard stereo print → Octatrack **inputs A/B**.
- Track 1 = **Thru machine**, INAB = A/B; place one trig; MIXER DIR AB = 0 (Thru-only).
- FX1 = Lo-Fi Collection, FX2 = Echo Freeze Delay; assign an LFO to filter cutoff.
- `[REC1]` to capture the wall into a buffer → load buffer into a Flex machine on Track 2.
- Scene A = clean Thru, Scene B = sliced/destroyed Flex capture; perform the crossfader.

**(b) Resample-the-Banjo-Loop**
- Record a banjo (EBM-5 → VG-800) phrase into a recorder buffer.
- Flex machine, auto-slice on transients; tune `TSNS` to the picking attack.
- Sequence the slices with conditional/probability trigs and per-step pitch p-locks → banjo-as-glitch-lead.
- Light Lo-Fi + spring reverb FX for the degraded character.

**(c) Scene-Crossfade Performance**
- One Part, two contrasting scenes: A = dry loop, filter open, no FX; B = filter swept low, Lo-Fi crushed, freeze-delay feedback high.
- Lock **XLV/XVOL** for equal-power level so there's no dip at center.
- The whole performance is one hand on the crossfader.

**(d) Ambient Drone Bed**
- Capture a sustained fuzz/baritone wall into a Static or Flex machine.
- Timestretch to hold indefinitely at project BPM; slow LFO on filter + pitch for drift.
- Dark Reverb on FX2; run it as a continuous bed under the live guitar — the "capture and sustain the wall forever" patch.

## 14. Versus Alternatives — Its Niche in *This* Studio

Four samplers, four jobs. The Octatrack's niche is **live performance, resampling, and processing the rig** — not composition, not sketching.

- **Octatrack MkII vs Elektron Digitakt 2.** Digitakt is the **focused, learnable drum/sample workhorse** — tighter workflow, better for building beats and one-shots, the disciplined clock. The Octatrack is **deeper, harder, and built for performance and live audio processing** (Thru machines, crossfader, 8 stereo tracks, 2 GB Static streaming). They're a *pair*, not a choice: Digitakt drives, Octatrack mangles.
- **Octatrack vs TE OP-1 Field.** The OP-1 is the **portable sketchpad / idea catcher** — fun, immediate, battery-powered, tape metaphor. The Octatrack is the **studio performance beast** — no contest on depth, routing, or live processing; the OP-1 wins on grab-and-go inspiration. Different rooms, different jobs.
- **Octatrack vs Akai MPC Sample.** The MPC is a **standalone composition/production environment** — big screen, pads, full arrangement, self-contained song-building. The Octatrack is **not a composer's tool**; it's a **live re-sequencer and mangler**. Use the MPC to write; use the Octatrack to perform and destroy.
- **Why it earns its desk space here.** Nothing else in this studio can take the pedalboard's stereo output as a *live input*, run it through filters and a 14-effect engine, resample it, slice it, and crossfade between clean and ruined — on stage, without a computer. That Thru-machine-into-the-wall capability is the Octatrack's and the Octatrack's alone. It is the rig's "capture and destroy" companion to the guitar boards.

## Sources

- [Elektron — Octatrack MkII product/specs page](https://www.elektron.se/product/octatrack-mkii?section=specs)
- [Elektron Octatrack MkII User Manual (OS 1.40A)](manuals/elektron-octatrack-mkii-manual.pdf)
- [Wikipedia — Elektron Octatrack](https://en.wikipedia.org/wiki/Elektron_Octatrack)
- [MusicRadar — Elektron Octatrack MkII review](https://www.musicradar.com/reviews/elektron-octatrack-mkii)
- [Sound on Sound — Elektron MkII Analog Four, Analog Rytm & Octatrack](https://www.soundonsound.com/reviews/elektron-mkii-analog-four-analog-rytm-octatrack)
- [Sound on Sound — Elektron Octatrack DPS-1 (original)](https://www.soundonsound.com/reviews/elektron-octatrack-dps1)
- [Mark Mosher — Octatrack MkII vs MkI: a deeper look](https://markmoshermusic.com/2017/07/04/elektron-octatrack-mii-vs-octatrack-mki-a-deeper-look-beyond-the-bullet-points/)
- [macProVideo — Review: Elektron Octatrack MkII, OS 1.30C](https://macprovideo.com/article/audio-hardware/review-elektron-octatrack-mkii-os-1-30c)
- [CDM — Original Octatrack owners get MkII features](https://cdm.link/newswires/original-octatrack-owners-get-mkii-features/)
- [Perfect Circuit — Octatrack MkII](https://www.perfectcircuit.com/elektron-octatrack-mkii.html)
- [Elektronauts — High-profile OT users thread](https://www.elektronauts.com/t/high-profile-ot-users/15652)
- [59perlen — Dawless Octatrack housejam with Digitakt](https://www.59perlen.com/post/dawless-octatrack-housejam-digitakt-digitone-novationpeak-roland-tb03)
- [Cuckoo — Octatrack Tutorial #1 (YouTube)](https://www.youtube.com/watch?v=NrhPOGzn7LI)
- [Cuckoo — Octatrack Loopbox / Pickup Machine tutorial (YouTube)](https://www.youtube.com/watch?v=JnbQ8ichm54)
