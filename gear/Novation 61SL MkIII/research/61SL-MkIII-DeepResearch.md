# Novation 61SL MkIII — Deep Research

A working dossier for the one piece of gear that sits *above* every board in this rig rather than inside one. The 61SL MkIII is the master control hub: the velocity keybed and 8-track sequencer that can play soft synths in Logic/Ableton, drive the Boss VG-800 and the MIDI pedals, fire and clock the Elektrons and the MPC, and throw CV at anything analog. It is also the thing that answers the rig's one obvious gap — the OP-1 Field is a wonderful instrument but it is not a 61-key velocity-and-aftertouch keyboard, and the Octatrack/Digitakt have pads, not a keybed. This document is concerned less with how the SL sounds (it makes no sound) and more with where it sits in the signal-and-clock topology and how it behaves as a controller and a standalone brain.

## 1. Lineage: ReMOTE SL → SL MkII → SL MkIII

The SL line is old by controller standards. The original **ReMOTE SL** (2005) and **SL MkII** (2009) were USB master keyboards built around Novation's **Automap** software, which auto-mapped knobs/faders to plug-in parameters. They were good controllers and nothing else — they did not make a peep without a computer in the loop.

The **SL MkIII** (announced October 2018) is a different animal, and Novation signaled it by [dropping "ReMOTE" from the name](https://www.musictech.com/reviews/novation-sl-mkiii-review/). Per [CDM's launch coverage](https://cdm.link/novations-sl-mkiii-has-it-all-sequencer-cv-midi-software-control/), it merges three Novation lineages at once: Launchpad's pad workflow, **Circuit's step sequencer**, and the SL's DAW-control heritage, then bolts on analog CV/Gate. The headline addition is the **eight-track polyphonic step sequencer derived from the Circuit engine** ([Sound on Sound](https://www.soundonsound.com/reviews/novation-sl-mkiii)), which means — for the first time in the SL family — the keyboard is a fully **DAW-less instrument** that runs standalone off its own 12V supply. The MkII line shipped in 25/49/61 sizes; the MkIII dropped the 25 and ships only as **49SL** and **61SL** ([MusicRadar](https://www.musicradar.com/reviews/novation-sl-mkiii)). The 61 is the one here.

The concept, in one line: a Circuit's brain and a Launchpad's pads grafted onto a real 61-note semi-weighted keybed with five color screens, analog CV, and HUI/InControl DAW mapping. It is deliberately the "hub of a hybrid studio" — Novation's own framing in the manual.

## 2. Architecture & Controls

This is a dense surface. From the [user guide hardware overview](manuals/SL%20MkIII%20User%20Guide%20V2%20English.pdf) and verified against Novation's spec pages:

- **Keybed.** 61 semi-weighted, individually-sprung, **synth-style velocity-sensitive** keys with a **channel-aftertouch strip** (not poly-AT). Eight selectable velocity curves (Low → Fixed) in Global Settings. RGB LEDs above every key that mirror Zone colors, played notes, arp notes, sequencer notes, or incoming external MIDI.
- **16 RGB pads** (laid out 8×2), velocity-sensitive, with both hit and pressure mapping. These are the sequencer step grid in Steps view, the pattern/session selectors elsewhere, and assignable drum/clip triggers in templates.
- **8 endless rotary encoders** + **8 faders** + **16 assignable buttons** (across two banks → effectively 16 rotaries, 16 buttons addressable per template).
- **Five RGB TFT screens** ("the screens") that label every control contextually — the single biggest usability differentiator versus a knob-and-blind-LED controller. [SOS](https://www.soundonsound.com/reviews/novation-sl-mkiii) compares the part-indicator LED strip to NI's S-series.
- **The 8-track sequencer.** Each of 8 Parts has its own 16-step pattern (8 patterns per Part), its own template, MIDI channel, and destination. Per step you get **velocity, gate (up to 32 steps long), chance/probability, and 6 micro-steps** for off-grid placement. Pattern view adds start/end position, direction (Forward/Backwards/Ping-Pong/**Random**), sync rate (1/32T up to 1/4), pattern shift, and **pattern chains**. Live record (quantized or non-quantized to 1/6 ticks), momentary record, and 8 automation lanes per track. **64 Sessions** total.
- **Arpeggiator** with per-Part routing, 8 types (Up/Down/Up-Down 1&2/Random/Played/Chord), octave range to 6, latch, and per-step chance.
- **Zones** — split the keybed into up to 8 independent zones, each with its own destination Part, key range, octave/transpose, pedal/wheel/aftertouch enables. This is how you play a bass synth in the low octave and a pad up top from one keybed.
- **Scales** — 16 scale types + chromatic, root selection, Snap/Filter/Display-Only modes, applied to keys *and* sequencer; plus independent sequence transpose ±11 semitones.
- **InControl / HUI** — dedicated DAW-control mode (see §6).
- **CV/Gate/Mod** — two CV pitch + two Gate + two Mod outputs, plus Clock Out, on 3.5mm jacks (see §8).
- **MIDI** — three 5-pin DIN sockets: **In / Out / Out2-Thru**, plus class-compliant USB.

## 3. Character & Feel

The keybed is the honest center of gravity. It is **synth-action semi-weighted** — sprung, fast, scannable at high resolution — not a hammer-action piano bed. [SOS](https://www.soundonsound.com/reviews/novation-sl-mkiii) calls the build solid and notes the **thick rubber track around the base** ("teal silicone strip" in the manual) that replaces feet and keeps it stable even when overhanging a desk. For someone who already owns a **Yamaha S08** for 88-key weighted duty, the SL's job is explicitly the *other* feel: fast synth-bass, arp riffs, drum-pad finger-drumming, lead lines — the playing the weighted bed is bad at.

Aftertouch is **channel pressure via a strip**, assignable in firmware 1.2+ to any MIDI CC, which makes it genuinely useful for filter sweeps and mod-depth on soft synths and the MIDI pedals. The pads are good-but-not-MPC: fine for clip launch and step entry, serviceable for finger drumming, not a reason to retire the MPC's pads. Build is plastic-bodied but rigid; at 6.54 kg it is a desk fixture, not a gig-bag throw-in.

## 4. Workflow & Behavioral Notes

- **Standalone vs DAW is a hard mode toggle.** The sequencer/Sessions world and the InControl DAW world are separate; you flip between them, and [reviewers consistently flag the "clunkiness in juggling all this"](https://tapeop.com/reviews/gear/130/61sl-mkiii-keyboard-controller) — you have to "remember to stick to one transport." In a hybrid setup you pick: is the SL running the room (standalone clock master + sequencer) or serving Logic (InControl)? Switching mid-session is awkward.
- **Sessions are the save unit.** A Session = all 8 Parts × 8 patterns + templates + scales + arp + zones. 64 of them, loadable by pad, by Program Change (ch.16), or by Song Select. **"Save Lock"** exists to stop accidental overwrites — turn it on for any Session you care about, because Program Change ch.16 can change Sessions *on the SL itself* and lose unsaved work.
- **Templates are computer-edited.** You cannot build a template on the hardware — you need [Novation **Components**](https://components.novationmusic.com) (web or standalone) to define what each control sends. This is the SL's biggest day-to-day friction: dialing in CC maps for the VG-800 or a Chase Bliss pedal means a trip to Components, not a menu dive.
- **"Happy accidents" are designed in.** Random pattern direction, per-step chance, pattern shift, and copying patterns between tracks are all surfaced as generative tools. For a degradation/aleatoric aesthetic this is a feature, not filler.
- **Micro-steps + 32-step gates (firmware 1.2)** turn the 16-step grid into something that can do triplet runs, glitch repeats, and notes longer than a bar — important before you write off "16 steps" as too coarse.

## 5. Role in the Studio / Integration with the Rig

This is the section that matters. The 61SL MkIII is the **central nervous system** of the hybrid setup. Concretely:

- **Master keyboard for soft synths.** It is the velocity-and-aftertouch front end for **NI Komplete 15 / Kontakt 8** and **Arturia V Collection 11** inside **Logic Pro** and **Ableton Live 12**. The OP-1 Field cannot do this; the S08 can but is weighted and 88 keys of desk. The SL is the daily-driver controller for playing-in parts.
- **Sequencer/clock brain for the DAW-less rig.** Eight tracks of polyphonic MIDI can sequence the **Digitakt 2**, **Octatrack MkII**, and **Akai MPC Sample** simultaneously — each Part on its own DIN-or-USB destination and MIDI channel — while the SL acts as **clock master at 24 PPQN** over USB *and* both DIN ports. [SOS](https://www.soundonsound.com/reviews/novation-sl-mkiii) puts it bluntly: "Eight tracks of polyphonic sequencing over MIDI, USB and CV is a big hairy deal." Alternatively it follows the Elektrons' clock — MIDI Clock Rx makes it a slave, Tx makes it the master.
- **Controller for the MIDI pedalboard.** The rig is heavily MIDI-clocked — the **Chase Bliss stack** (Brothers AM, Clean, MOOD MkII, Blooper, Big Time, Generation Loss), the **VG-800**, the **Microcosm**, **Chroma Console**, and **H90** all take MIDI. Templates let the SL send CC/PC to those boxes, and its clock can drive their tempo-synced functions. The VG-800 in particular — which does pitch-to-MIDI from the GK-5 baritone/banjo — can be played *and* configured from the SL.
- **CV bridge.** Two CV/Gate/Mod pairs make it a MIDI-to-CV converter for any analog/modular gear, with Clock Out for analog sync. Nothing else in the rig does this.
- **The keyboard the OP-1 lacks.** Plain and simple: when a part needs a real keybed with velocity, the SL is it.

In the [rig-design.html](../../rig-design.html) topology the SL is **off-board** — it doesn't live in the signal chain of Boards 1/2/3 at all. It sits upstream of *everything*, on the MIDI/clock/CV plane, talking to the Apollo x8 (USB/MIDI) and out to the DIN web.

## 6. Use-Specific Notes

- **Playing the VG-800 models.** Route a Part to a DIN destination on the VG-800's MIDI channel; build a Components template that maps the 8 knobs/faders to the VG-800 CCs (amp/cab/effect params). Use the keybed to audition the VG's guitar-synth and modeled-amp patches without picking up the baritone. Aftertouch → a useful VG mod-depth CC.
- **Sequencing the Elektrons.** Assign Parts 1–3 to Digitakt / Octatrack / MPC on separate MIDI channels and DIN/USB destinations. Run the SL as clock master (MIDI Clock Tx On, both DIN + USB carrying clock). Use Random direction + chance for generative drum/bass interplay; pattern-chain for arrangement. Mute/Solo per Part for live arranging. Note: the Octatrack and Digitakt have their own sequencers — decide who is the master sequencer per song to avoid double-sequencing chaos.
- **Mapping Logic / Ableton.** InControl mode gives transport, track select/arm, faders for level/automation, encoders for device params. Ableton integration is the strongest (clip launch, device control); Logic and Reason have dedicated scripts; everything else falls back to **HUI/Mackie** ([SOS](https://www.soundonsound.com/reviews/novation-sl-mkiii), [Tape Op](https://tapeop.com/reviews/gear/130/61sl-mkiii-keyboard-controller)). Caveat below re: Automap.
- **CV control.** MIDI notes 24–108 map to **0–7 V** CV pitch (notes outside clamp); Gate goes high while a note is held; each Mod output is a configurable CC → voltage with a selectable **−5/+5 V or 0/+5 V** range ([Novation CV guide](https://userguides.novationmusic.com/hc/en-gb/articles/25626767118994-Using-the-SL-MkIII-s-CV-and-Gate-connections)). CV is **monophonic** — the poly note stream collapses to last-note priority. Calibrate the pitch ports (A2/220 Hz and A4/880 Hz reference points) for accurate tracking. Pitch wheel can drive CV ±1 to ±12 semitones *(the ability to route pitch-bend to CV at all was **added in firmware 1.4** — not an original-spec feature; the ±range is configurable per the CV guide)*.

## 7. Famous Users

Honest answer: controllers do not accrue signature-artist mythology the way fuzzes do, and the SL MkIII is no exception. It shows up on plenty of hybrid/DAW-less studio desks and synth-heavy YouTube rigs (it was widely reviewed and [shortlisted as a 2018 standout by MusicTech](https://www.musictech.com/reviews/novation-sl-mkiii-review/)), but no headline artist has claimed it as a defining instrument. Treat the absence of a name-drop list as normal for the category — its credibility is in the spec sheet and the reviews, not a hero endorsement. *(Unverified: any specific artist attribution — none found in research.)*

## 8. Connectivity / Power / I/O

| I/O | Detail |
|---|---|
| USB | USB-B 2.0, class-compliant; exposes MIDI, InControl, and From-DIN-1 ports to the host |
| MIDI DIN | 3× 5-pin: **In**, **Out**, **Out2/Thru** (Out2 switchable to a second clock-capable Out, or pure Thru) |
| CV / Gate / Mod | 2× CV pitch (0–7 V), 2× Gate, 2× Mod (−5/+5 V or 0/+5 V, CC-assignable), all 3.5 mm TS |
| Clock Out | 3.5 mm analog clock, 1/2/4/8/24 PPQN selectable |
| Pedals | 2× 1/4" TS/TRS (Sustain + Expression) + 1× 1/4" TS (Footswitch) |
| Power | **12 V DC, 1 A** external PSU (center-positive); **no USB power** — this is a real constraint |
| Weight / size (61) | 6.54 kg; 981 × 100 × 300 mm |

Source: [user guide V2](manuals/SL%20MkIII%20User%20Guide%20V2%20English.pdf) + [Novation CV guide](https://userguides.novationmusic.com/hc/en-gb/articles/25626767118994-Using-the-SL-MkIII-s-CV-and-Gate-connections). The no-USB-power point ([CDM](https://cdm.link/novations-sl-mkiii-has-it-all-sequencer-cv-midi-software-control/)) matters for desk layout — it always needs the wall wart.

## 9. Pairing Recommendations (by name)

- **Boss VG-800** — play/audition its models from the keybed; map params via DIN + Components template; clock its synced effects from the SL.
- **Elektron Digitakt 2 / Octatrack MkII** — sequence over DIN/USB on separate Parts; or follow their clock. Decide master-sequencer ownership per song.
- **Akai MPC Sample** — drive from a Part for melodic/keys sequencing the MPC pads can't easily play; or use MPC as the clock master and let the SL play into it.
- **Logic Pro / Ableton Live 12** — InControl for transport+mixer; the keybed for soft synths. Ableton is the better-integrated of the two.
- **NI Komplete 15 / Arturia V Collection 11** — the SL is their hardware front end; aftertouch-to-CC unlocks expressive control.
- **UA Apollo x8 / RME Babyface Pro FS** — the SL's USB/MIDI rides alongside; clock and note data into the DAW, audio stays on the interface.
- **Any CV/modular gear** — the two CV/Gate/Mod pairs + Clock Out make the SL the rig's only MIDI-to-CV bridge.

## 10. Reviews & Demos

- [Sound on Sound — Novation SL MkIII](https://www.soundonsound.com/reviews/novation-sl-mkiii) — the most thorough written review; best on sequencer architecture, build, and the Automap-removal caveat.
- [Tape Op — 61SL MkIII](https://tapeop.com/reviews/gear/130/61sl-mkiii-keyboard-controller) — best on the real-world standalone-vs-DAW mode juggling and InControl track navigation gripes.
- [MusicRadar — SL MkIII review](https://www.musicradar.com/reviews/novation-sl-mkiii) — concise overview, size/lineup context.
- [MusicTech — SL MkIII review](https://www.musictech.com/reviews/novation-sl-mkiii-review/) — the "best of 2018?" framing and feature tour.
- [CDM — Novation's SL MkIII has it all](https://cdm.link/novations-sl-mkiii-has-it-all-sequencer-cv-midi-software-control/) — launch analysis; the Launchpad/Circuit/CV merger thesis.
- [Loopop — SL MkIII video review](https://loopopmusic.com/novation-sl-mk3-review-is-it-a-game-changing-controller) — the definitive deep-dive video walkthrough.
- [Sweetwater — owner reviews](https://www.sweetwater.com/store/detail/SLmk3-61--novation-61sl-mkiii-keyboard-controller-with-sequencer/reviews) — long-tail owner feedback.

## 11. Quirks / Known Issues / Firmware

The MkIII shipped in late 2018 feeling **underbaked**, and its reputation was repaired largely by firmware. Be accurate about the history:

- **Launch criticism.** Early units felt feature-thin against the price; the sequencer lacked depth at 1.0.
- **Firmware 1.2** ([Novation](https://novationmusic.com/en/news/sl-mkiii-firmware-update-12)) was the big one: added **6 micro-steps per step**, **doubled max gate to 32 steps**, made **aftertouch assignable to any CC**, added **NRPN** support, smoother encoder response, and pattern scrolling without deselecting the playing pattern.
- **Firmware 1.4** ([SynthAnatomy](https://synthanatomy.com/2020/06/novation-sl-mkiii-firmware-1-4-adds-new-inspiring-arpeggiator-sequencer-features.html)) added the deeper **arpeggiator** features (more types/chance) and further sequencer tools. The V2 user guide in this folder reflects the post-1.4 feature set.
- **Automap is gone.** The MkIII dropped Novation's old Automap plug-in auto-mapping; [SOS notes plug-in control is "significantly reduced without Automap."](https://www.soundonsound.com/reviews/novation-sl-mkiii) You get InControl/HUI for DAW transport+mixer, but not the deep per-plug-in mapping the MkII had.
- **Standalone ↔ DAW mode-switching is clunky** and the manual reportedly **misdocuments** Shift+Next/Prev track banking in InControl ([Tape Op](https://tapeop.com/reviews/gear/130/61sl-mkiii-keyboard-controller)).
- **USB-to-Logic timeouts.** At least one owner reported [persistent MIDI timeouts in Logic over USB that DIN connection avoided](https://www.sweetwater.com/store/detail/SLmk3-61--novation-61sl-mkiii-keyboard-controller-with-sequencer/reviews). *(Unverified at scale — anecdotal, not a confirmed widespread defect. For this rig it's worth knowing the DIN-out workaround exists if Logic-over-USB ever flakes.)*
- **No USB power** — always needs the 12V brick.
- **Faders aren't motorized or touch-sensitive**, so in some DAW modes moving a fader is "destructive" (jumps the value) unless Fader Pickup is on — and pickup is bypassed in InControl, where you inherit the DAW's behavior.
- **Templates need a computer** (Components) — no on-hardware template editing.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Keybed | 61-note semi-weighted, synth-action, individually sprung, velocity-sensitive |
| Aftertouch | Channel pressure (strip), CC-assignable (firmware 1.2+) |
| Pads | 16 RGB velocity-sensitive (8×2), hit + pressure |
| Controls | 8 encoders, 8 faders, 16 assignable buttons (×2 banks), pitch + mod wheels (RGB) |
| Screens | 5 RGB TFT |
| Sequencer | 8-track polyphonic, 16 steps × 6 micro-steps, gate to 32 steps, chance, 8 patterns/Part, 64 Sessions, 8 automation lanes/track |
| Arp | 8 types, octaves to 6, latch, per-step chance |
| Zones / Scales | 8 zones; 16 scale types + chromatic |
| MIDI DIN | 3× 5-pin: In / Out / Out2-Thru |
| USB | USB-B 2.0, class-compliant |
| CV/Gate/Mod | 2× CV pitch (0–7 V), 2× Gate, 2× Mod (−5/+5 V or 0/+5 V) + Clock Out, all 3.5 mm |
| Clock | MIDI 24 PPQN Rx/Tx (USB + both DIN); analog Clock Out 1/2/4/8/24 PPQN |
| Pedals | Sustain (TRS) + Expression (TRS) + Footswitch (TS), 1/4" |
| DAW control | InControl + Mackie HUI; Ableton/Logic/Reason scripts |
| Editor | Novation Components (web/standalone) |
| Power | 12 V DC, 1 A external PSU (center-positive); no USB power |
| Weight / dimensions (61) | 6.54 kg; 981 × 100 × 300 mm |

Sources: [user guide V2](manuals/SL%20MkIII%20User%20Guide%20V2%20English.pdf), [Novation 61SL MkIII product page](https://us.novationmusic.com/products/61sl-mkiii), [Novation CV guide](https://userguides.novationmusic.com/hc/en-gb/articles/25626767118994-Using-the-SL-MkIII-s-CV-and-Gate-connections).

## 13. Starting-Point Setups

Four named configurations for day one in this rig.

**(a) "Soft-synth master keyboard"** — the daily driver
- USB to the Mac; SL set to standard MIDI mode (not InControl).
- Part 1 → USB, MIDI ch.1; play Kontakt/Komplete/V Collection in Logic or Ableton.
- Velocity curve: Normal or Normal+. Aftertouch → CC1 (mod) or a filter CC.
- Zones off. Octave buttons to taste. This is the "I just want to play in a part" patch.

**(b) "Sequence the Elektron rig"** — DAW-less brain
- Standalone mode, MIDI Clock **Tx On**, both DIN + USB carrying clock.
- Part 1 → Digitakt (DIN1, ch.1), Part 2 → Octatrack (DIN1, ch.2), Part 3 → MPC (USB or DIN2, ch.3).
- Build patterns with micro-steps; use Random direction + 60–80% chance on one Part for generative motion. Mute/Solo to arrange live. Pattern-chain for song structure.

**(c) "CV control"** — the MIDI-to-CV bridge
- Part routed to CV/Gate 1 (and Mod 1). Calibrate pitch port first (A2/A4).
- Keybed or sequencer plays the CV mono voice; Mod 1 set to an expressive CC for filter/VCA.
- Clock Out → analog gear's sync in, PPQN matched to the destination.
- Pitch-bend-to-CV at ±2 semitones for playable bends.

**(d) "Play / program the VG-800"** — guitar-synth front end
- Part → DIN to VG-800's MIDI channel; Components template maps the 8 knobs to VG params.
- Keybed auditions VG patches; faders ride model levels; aftertouch → a VG mod CC.
- If clocking VG synced effects, SL as clock master.

## 14. Versus Alternatives

Where the 61SL MkIII wins or loses *for this studio*:

- **Arturia KeyLab 61 MkII** — the closest direct competitor and the one [CDM names](https://cdm.link/novations-sl-mkiii-has-it-all-sequencer-cv-midi-software-control/). KeyLab has CV/Gate too and arguably a nicer keybed and Analog Lab integration, but **no built-in polyphonic sequencer**. For a DAW-less / hybrid rig that wants to sequence the Elektrons standalone, the SL's 8-track sequencer is the deciding feature. Reach for KeyLab if you live entirely in the DAW; reach for the SL because this rig explicitly does not.
- **NI Komplete Kontrol S61 (MkII/MkIII)** — best-in-class for *NI/NKS* integration and the gorgeous high-res screens that browse Komplete by tag. But it is **DAW/computer-bound**, has **no standalone sequencer and no CV**. Since this rig owns Komplete 15, the KK is tempting — but it can't run the room DAW-less or talk CV. The SL is the more *self-sufficient* hub; the KK is the better *Komplete browser*. (They're not mutually exclusive — the KK would be a luxury add, not a replacement.)
- **Akai MPK261** — cheaper, solid keybed, good pads, deep DAW mapping. No sequencer of the SL's depth, no CV, no five-screen contextual labeling. A budget controller, not a hub.
- **Arturia KeyStep Pro** — *is* a powerful 4-track standalone sequencer with CV, but it's a 37-key slim controller, not a 61-key velocity-and-aftertouch performance keybed. It and the SL solve overlapping problems from opposite ends; the SL is the better *keyboard*, the KeyStep Pro the more *dedicated sequencer*.
- **Sequencer-keyboards generally (e.g., the SL's own Circuit sibling)** — the SL is the only box in this category that is simultaneously a real 61-key master keyboard, an 8-track poly sequencer, a CV source, *and* a HUI DAW surface. That four-in-one breadth is exactly why it earns the "control hub" slot here — and the price of that breadth is the mode-switching clunk and the computer-bound template editing covered in §4 and §11.

In this rig — DAW-less Elektrons + MPC, a deeply MIDI-clocked pedalboard, the VG-800 as a guitar-synth source, soft synths in two DAWs, and a need for the velocity keybed the OP-1 lacks — the 61SL MkIII is the right call over all of these specifically because it is the single device that **plays, sequences, clocks, and CV-bridges** the whole rig from one keybed. Nothing else owned does all four.

## Sources

- [Novation — 61SL MkIII product page](https://us.novationmusic.com/products/61sl-mkiii)
- [Novation — SL MkIII User Guides: CV and Gate](https://userguides.novationmusic.com/hc/en-gb/articles/25626767118994-Using-the-SL-MkIII-s-CV-and-Gate-connections)
- [Novation — SL MkIII Global settings](https://userguides.novationmusic.com/hc/en-gb/articles/25626782085266-SL-MkIII-Global-settings-menu)
- [Novation — SL MkIII Firmware Update 1.2](https://novationmusic.com/en/news/sl-mkiii-firmware-update-12)
- [Novation Components (editor/librarian)](https://components.novationmusic.com)
- [SL MkIII User Guide V2 (local PDF)](manuals/SL%20MkIII%20User%20Guide%20V2%20English.pdf)
- [Sound on Sound — Novation SL MkIII](https://www.soundonsound.com/reviews/novation-sl-mkiii)
- [Tape Op — 61SL MkIII Keyboard Controller](https://tapeop.com/reviews/gear/130/61sl-mkiii-keyboard-controller)
- [MusicRadar — Novation SL MkIII review](https://www.musicradar.com/reviews/novation-sl-mkiii)
- [MusicTech — Novation SL MkIII review](https://www.musictech.com/reviews/novation-sl-mkiii-review/)
- [CDM — Novation's SL MkIII has it all](https://cdm.link/novations-sl-mkiii-has-it-all-sequencer-cv-midi-software-control/)
- [Loopop — SL MK3 review](https://loopopmusic.com/novation-sl-mk3-review-is-it-a-game-changing-controller)
- [SynthAnatomy — SL MkIII Firmware 1.4](https://synthanatomy.com/2020/06/novation-sl-mkiii-firmware-1-4-adds-new-inspiring-arpeggiator-sequencer-features.html)
- [Sweetwater — 61SL MkIII (product + owner reviews)](https://www.sweetwater.com/store/detail/SLmk3-61--novation-61sl-mkiii-keyboard-controller-with-sequencer/reviews)
