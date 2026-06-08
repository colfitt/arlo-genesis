# Eventide H90 Harmonizer — Deep Research

A working dossier for the H90 as it lives at position six on Board 3 (End / Time → Tape) of a hex-pickup banjo/baritone rig. It sits after the Hologram Chroma Console and before the MXNHLT PORTA424, and it is the rig's primary reverb engine and its deep algorithmic time/pitch processor — the box that catches the sustained, degraded fuzz walls coming off Board 1 (EQD Hizumitas et al.) once they've been smeared by Board 2 and tape-warped by the Chase Bliss stack. It is also the reason three otherwise-excellent pedals (Strymon Big Sky, Strymon TimeLine, UAFX Del-Verb) are benched. This document is concerned with justifying that — with what the H90 actually leads on versus what merely overlaps — and with the specific quirks of feeding it banjo-via-VG-800 pitch material.

## 1. Lineage: H910 → H9 → H90

Eventide has been the harmonizer company since the **H910** of 1974 — the world's first commercially available digital pitch-shift/delay box, designed by Anthony Agnello, the one Tony Visconti described to Bowie and Eno as the device that *"fucks with the fabric of time"* (per [Valhalla DSP's H910 history](https://valhalladsp.com/2010/05/07/early-pitch-shifting-the-eventide-h910-harmonizer/)). The line ran H910 → H949 → the **H3000 Ultra-Harmonizer** (the studio standard Eno wrote Eventide a thank-you letter over, per [Vintage King's harmonizer history](https://vintageking.com/blog/eventide-harmonizer/)) → DSP4000 → H8000 → the rackmount **H9000**, and on the pedal side: TimeFactor / PitchFactor / Space → the **H9** (one algorithm at a time) → **H9 Max** (the full 52-algorithm library) → the **H90**.

The H90 is, per [Eventide's own marketing and Guitar.com's review](https://guitar.com/reviews/effects-pedal/eventide-h90-review/), the H9 Max brought into the 2020s. The manual ([User Guide v1.1.4, §1.1](manuals/EventideH90.pdf)) lists what's genuinely new:

- **Two algorithms at once, per Program** — routed in series or parallel and shaped independently. This is the headline change; the H9 was strictly one-at-a-time. It is why the H90 can be a *delay-into-reverb in one box* — the thing that benches the Del-Verb.
- **ARM-based architecture** replacing the H9's SHARC DSP, which gave Eventide the headroom to re-voice every legacy algorithm and write new ones (per [MusicRadar](https://www.musicradar.com/reviews/eventide-h90-harmonizer)).
- **SIFT** (Spectral Instantaneous Frequency Tracking) — a new low-latency *polyphonic* pitch-shift engine that tracks chords with near-zero tracking error. This underpins the Polyphony and Prism Shift algorithms and is the single most relevant new feature for a banjo/baritone-chord player.
- **62 algorithms shipping** (all 52 from the H9 Max plus 10 new: Bouquet Delay, Even-Vibe, Head Space, Instant Flanger, Instant Phaser, Polyphony, Prism Shift, SP2016 Reverb, WeedWacker, Wormhole).
- True spillover between Programs, instrument *or* line level operation, two mono inserts or one stereo insert anywhere in the chain, Dual Routing for two independent stereo signal paths, five push-turn encoders, two EXP/CTL inputs, full MIDI DIN + USB.

**Firmware has moved well past the bundled manual.** The shipped User Guide is v1.1.4 (62 algorithms). Subsequent free firmware has added substantially more. Two big drops: the **Harmonizer+ vocal suite** in **v1.10 (April 29, 2025)** — **VocalTune** (pitch correction + formant shift + EQ/comp/gate), **VocalShift** (3-voice pitch+formant harmonizer), **VocalShiftMIDI** (4-voice, MIDI-played) and **Quadravox+** (4-voice diatonic harmonizer), all ported from the flagship H9000 ([press release](https://www.eventideaudio.com/press-releases/eventide-expands-h90-pedals-capabilities-with-harmonizer-vocal-algorithms/)); and four **granular** algorithms (Cosmic Web, Glitch, GrainMod, Stutter) in the v1.12.x granular update (per [Synth Anatomy](https://synthanatomy.com/2025/12/eventide-h90-harmonizer-souped-up-h9-with-twice-the-power-more-algorithms-is-out-now.html) and [Sound On Sound](https://www.soundonsound.com/news/eventide-h90-h9000-granular-update)). The vocal algorithms aren't just for vocals — formant-shifting and diatonic harmonizing the banjo/baritone is a strong rig use (see the UsageGuide). *Flag the owner: keep H90 Control updated — several of the most rig-relevant algorithms postdate the PDF in this folder.* (The exact algorithm count beyond ~62 is firmware-dependent and not verified to a single number here.)

## 2. Controls & Architecture

The face plate has two push-turn encoders (**Select**, **Perform**), three **Quick Knobs**, four mode buttons (**Programs, Routing / Presets, Parameters**), three footswitches (**P/A/B**), and an OLED. The architecture is the thing to internalize, because it's a hierarchy, not a knob set ([§4 Terminology](manuals/EventideH90.pdf)):

- **List** — a bank of up to 99 Programs. There are un-editable Factory Lists and editable User Lists; the active List is your **Playlist**.
- **Program** — the top-level patch. Runs **two Presets at once**, plus Program-level Active/Bypass, In/Out gain, routing, inserts, Exp/Ctl mappings, a Program HotKnob, and three HotSwitches. The H90 runs one Program at a time; switching is instantaneous with spillover.
- **Preset (A and B)** — an Algorithm with a saved parameter set, plus its own Active/Bypass, gain, and HotKnob. The two Presets are the two simultaneous effects.
- **Algorithm** — the actual DSP module (Blackhole, Digital Delay, Polyphony, etc.).

**Routing** is set globally to one of two modes ([§6.2](manuals/EventideH90.pdf)):

- **Insert routing** — the two Presets run in **Series or Parallel**, and you get up to **two mono inserts (or one stereo insert)** placeable Pre-A, Mid (between A and B), Post-B, or in parallel — to loop an external pedal into the H90's signal path. Each insert has Send/Return level, Mix, Tails, **Latency (0–512 samples)**, and Polarity. *This is how the H90 could host, say, an external pedal inside one of its reverbs — not used in this rig today but worth knowing.*
- **Dual routing** — **two independent stereo paths**: Path 1 = Ins 1/2 → Outs 1/2, Path 2 = Ins 3/4 → Outs 3/4. Series/Parallel/Pre-Post per path. This is the wet/dry-wet and two-instruments-at-once mode.

**Play modes** ([§5](manuals/EventideH90.pdf)): **Select** mode (Program Select scrolls the whole Playlist; Bank Select chunks 99 Programs into 33 banks of three, one per footswitch) and **Perform** mode (the P/A/B footswitches become user-mapped performance controls — tap tempo, momentary active, the three HotSwitches, or algorithm-specific moves like Wormhole's **Warp**, Prism Shift's **Freeze**, Head Space's **Boil/Break**). The footswitch LEDs are color-coded: white = active/bypass, aqua = HotSwitch, blue = delay (repeat/feedback), red = pitch, green = modulation.

The **HotSwitches** matter for a one-player live rig: each Program gets three, and each can jump a *range* of parameters at once — "three additional Programs for the price of one," as the manual puts it. With the Strymon stack benched, this is how the H90 covers scene changes a Big Sky's presets would otherwise handle.

## 3. Sonic Character / Standout Algorithms

The H90's voice is *Eventide rack lineage in a pedal* — pristine, deep, and weighted toward the cosmic/experimental rather than the strictly natural. The standouts for this rig's drone/doom/shoegaze aesthetic (descriptions from the [Algorithm Guide, §10](manuals/EventideH90.pdf)):

- **Blackhole** (Reverb) — the famous one, born as a DSP4000 preset, then Eventide's Space pedal. Soft attack, lingering harmonic tail, a **Gravity** control (its decay), **Size** "from cartoonishly small to cosmically epic," and **Feedback** that sweeps clockwise to **Infinite** (infinite tail, still accepting input) then **Freeze** (locked, no input). This is *the* sustained-fuzz-wall catcher.
- **MangledVerb** (Reverb) — a non-standard stereo reverb fed *into distortion* (signal flow: Pre-Delay → Reverb → EQ → Distortion). Ranges from "a bow scraping a cello string to obnoxious mayhem," with **Wobble** (spooky detuning) and a Softclip/Overdrive control. Set Size ~15 to use it as a distortion-flavored effect. Pairs natively with the rig's degradation goal.
- **Shimmer** (Reverb) — twin pitch shifters in the reverb feedback path; "what guitars sound like in heaven." Pitch A/B in cents (1200c = octave), **Pitch Decay** with two Freeze modes (Pitch Freeze keeps the climb going while feeding the verb; Pitch+verb Freeze locks everything for soloing over). The textbook drone-shimmer wall.
- **Wormhole** (Reverb) — mega-sized tilting reverb measured in **light-years** with a **Warp** performance move; "How deep are you willing to go?" Stability/Stability-Rate give it the unstable-pitch character the rig loves.
- **SpaceTime** (Multi) — a whole rig in one Preset: Modulation + two Delays + Reverb, with the delays/reverb routable series *or* parallel via the Verb Lvl knob. Delays from the TimeFactor; reverb from the Space Plate + Ultra Reverb. Lets one Preset behave like a delay-and-reverb, freeing the other for pitch.
- **Polyphony** (Pitch) — the SIFT-based polyphonic shifter: massive organ-like chords, crystal effects, Auto-EQ to keep the shifted voices natural, independent panning in stereo, and a **Freeze** for pads you play over. Crucially **chord-capable** — see §6 on banjo.
- **Prism Shift** (Pitch) — polyphonic, generates 3 arpeggiated voices (Low/Mid/High) from a single chord across four arp types and up to 3 octaves. The most distinctive of the new algorithms.
- **Crystals** (Pitch) — the classic twin **reverse** pitch shifters + delay + feedback + reverb; climbing, cascading granular cascades.
- **Diatonic / Quadravox** (Pitch) — key/scale-aware harmonizers (Diatonic = 2 voices, Quadravox = 4), with a long scale list (Major, Minor, the modes, Harmonic/Melodic Minor, Whole Tone, Enigmatic, Neapolitan, Hungarian) and a **Learn** footswitch to set the key by playing a note. *Note: these are monophonic trackers — single notes/octaves only.*
- **H910 H949** (Pitch) — emulates the actual vintage boxes, glitch ("the glitch is back") and de-glitched splice types included.

Also aboard: every standard space — **Hall, Plate, Room, Spring, SP2016 Reverb** (the classic rack emulation, Vintage/Modern, Stereo Room/Room/Plate), **DualVerb** (two parallel studio reverbs), **DynaVerb** (reverb + Omnipressor dynamics, including dynamic reversal), **ModEchoVerb, Reverse Reverb, TremoloVerb** — plus the full delay (Vintage, Tape Echo, MultiTap, UltraTap, Reverse, Head Space, Bouquet, Ducked, Filter Pong, Band, Mod, Digital), modulation (Chorus, Flanger, Phaser, Rotary, Q-Wah, RingMod, Tricerachorus, Undulator, Harmadillo, etc.), distortion (CrushStation, PitchFuzz, Sculpt, WeedWacker), and synth (HotSawz, Synthonizer) categories.

## 4. Behavioral Notes

- **Latency / SIFT.** The polyphonic pitch engine is "low-latency" by Eventide's framing, not zero — there's a tracking buffer. For pad/chord/shimmer use this is inaudible; for tight rhythmic stabs you'll feel a hair more than an analog source. Not a problem at end-of-chain.
- **Spillover.** True spillover between Programs — the previous Program's reverb/delay tail decays naturally as the next loads ([§4.2](manuals/EventideH90.pdf)). For ambient performance this is essential and is something neither a single-engine pedal nor a hard preset-switch can do as gracefully.
- **Two-algorithm ceiling.** You get exactly two Presets per Program. There is no third simultaneous effect inside one Program. The whole live architecture is about choosing the right two and using HotSwitches/Performance moves to morph them.
- **Insert latency comb-filtering.** When you loop an external *digital* pedal through an insert at a non-0/100% mix, set the insert Latency (0–512 samples) to match, or you'll comb-filter. Analog pedals need 0. (Not in use in this rig yet, but relevant if the owner ever inserts, e.g., the benched Del-Verb as a travel utility.)
- **Stereo.** Four ¼" inputs / four ¼" outputs, all configurable instrument or line. Stereo throughout, which is mandatory at this point in the chain — everything from the CE-2W split onward is stereo L/R.
- **Bypass.** DSP bypass with selectable Tails per insert/Program; spillover requires the H90 to stay powered. Like every digital ambient box, total power loss kills the signal — see §8 on the Big Sky as the live backup.
- **Bluetooth** is on the panel but **not implemented** in current firmware (manual §2.1 note).

## 5. Signal-Chain Placement — the End Board ambient/pitch engine

In this rig the H90 is the **deep space and pitch processor at the end of the time domain**, sitting:

`… CB Blooper → Hologram Chroma Console → **Eventide H90** → MXNHLT PORTA424 → JHS 424 → Apollo/FOH`

- **After the Chroma Console** is correct. Chroma is the character/color/lo-fi smear box; it hands the H90 an already-degraded, modulated stereo signal. The H90 then does the *big* ambient and pitch work on top — Blackhole/Shimmer/Wormhole walls, Polyphony chords, SpaceTime delay-verb. You want the pristine, deep reverb engine *after* the dirt-and-character stages so the space wraps everything, not the other way around.
- **Before the PORTA424 / JHS 424 tape stage** is also correct and aesthetically the whole point: the H90's clean, hi-fi cosmic reverbs get *printed to tape* and degraded by the Tascam-Porta recreation and the JHS 424. The H90 supplies the pristine source the tape stage ruins — exactly the rig's "recorded-wrong, beautiful" thesis.
- **Stereo all the way.** The H90 receives stereo from the Chroma Console and sends stereo to the tape stage. Run it Insert/Series with both Presets stereo for the widest walls, or Dual routing if the owner ever wants a true wet/dry split into the tape chain.

**Why it benches three pedals:**

- **Strymon Big Sky** — *"H90 handles reverb. Sub-in if H90 down."* Fully justified. The H90's reverb stable (Blackhole, Shimmer, Hall, Plate, Room, SP2016, DynaVerb, MangledVerb, Wormhole, ModEchoVerb, Reverse, TremoloVerb, DualVerb, Spring) is broader and deeper than Big Sky's 12 machines, *and* it can run a reverb alongside a delay or a pitch effect in one box — which Big Sky cannot. The only honest case for the Big Sky is as a **failover**: it's the simplest one-knob reverb to drop in if the H90 dies on stage, and it draws far less power. Keep it boxed as the spare. (Verified: Big Sky is reverb-only single-engine; H90 is dual-engine.)
- **Strymon TimeLine** — *"Big Time + H90 delays cover the live needs."* Justified. The rig already has the **Chase Bliss Big Time** as its dedicated stereo delay earlier on Board 3; the H90 adds Vintage/Tape/MultiTap/UltraTap/Reverse/Mod/Digital delays *plus* SpaceTime (delay+reverb in one). Between the Big Time's character and the H90's algorithmic delays, the TimeLine's 200-preset delay workstation is redundant for live use. (The TimeLine would only re-earn a slot for its specific dTape/dBucket/Pattern voices, which Big Time + H90 substantially cover.)
- **UAFX Del-Verb** — *"Subsumed by H90. Travel board only."* The most clear-cut. Del-Verb is literally a delay-*and*-reverb-in-one-box pedal — exactly what one H90 Program does with Preset A = a delay algorithm and Preset B = a reverb algorithm (or SpaceTime alone). The H90 does it with vastly more algorithms, stereo, MIDI, and spillover. Del-Verb's only remaining value is as a tiny, low-power travel-board stand-in, which is precisely where the rig sheet files it.

## 6. Source-Specific Notes (banjo, baritone, VG-800, bass)

The interesting case is **pitch/harmonizer on a banjo**. The Gold Tone EBM-5 with a GK-5 into the VG-800 produces bright, fast-transient, low-mass signal — and by the time it reaches the H90 (end of chain) it has already been fuzzed, smeared, and tape-colored. Two H90 capabilities matter:

1. **Polyphony / Prism Shift (SIFT) for chords.** Old pitch shifters (and the H90's own **Diatonic/Quadravox**, which the manual flags as *monophonic — single notes and octaves only*) choke on banjo's fast rolls and multi-note clusters. The SIFT-based **Polyphony** and **Prism Shift** algorithms track chords with near-zero error, so a banjo-as-lead chordal phrase can be octave-stacked or arpeggiated into something orchestral. **Polyphony's "Inst Type: Percussive" mode** is specifically built to preserve transients and reduce latency on percussive sources — that's the banjo setting; use **Pitched** mode for larger intervals where smoothness beats attack.
2. **Banjo as harmonized lead.** For diatonic harmony lines (the "banjo-as-lead" idea), **Diatonic** with the **Learn** footswitch (set key by playing a note) gives in-key harmony — but only on **single-note** lead lines, given its monophonic tracker. Use Diatonic/Quadravox for melodic banjo leads, Polyphony/Prism Shift for chordal banjo. Both reward feeding the H90 the *cleanest* banjo tone available; if the upstream fuzz is too dense the trackers wander, so consider an H90 Program fed earlier or a cleaner VG-800 model when pitch-tracking is the goal.

- **Baritone Jazzmaster drones.** Home territory. Long Blackhole/Wormhole/Shimmer decays over a sustained baritone drone is the literal use case these algorithms were voiced for. The low fundamentals give the reverbs dense, stable material; **Infinite/Freeze** on Blackhole or Shimmer turns a single baritone chord into an evolving pad you play over.
- **Modeled VG-800 signal.** The H90 treats the VG-800's modeled amp/synth output as any line-level source — and the rig runs **line level** here, so set the relevant H90 inputs to Line (the back-panel LED grid shows which jacks are line). Synth/pad patches from the VG-800 fed into MangledVerb or ModEchoVerb produce the evolving, slightly-broken drones the aesthetic wants.
- **Bass (Jazz Bass).** Polyphony's Percussive mode and clean octave-down work well; for ambient bass, keep reverb Size moderate and use the **Low Band** shelving controls on Hall/Room/Blackhole to keep the tail from clouding the fundamental.

## 7. Famous Users (honest)

The honest framing: the H90 is new enough (2022) that its *own* artist mythology is still forming, but it inherits the deepest discography in effects history through its algorithms. Eventide's harmonizer heritage is genuinely legendary ([Vintage King](https://vintageking.com/blog/eventide-harmonizer/), [Reverb on the H3000](https://reverb.com/news/tech-behind-eventide-h3000-ultra-harmonizer)):

- The **H910** is on AC/DC's "Back in Black" intro, the descending snare on Bowie's *Low* (Visconti/Eno), the steel-drum effect on Led Zeppelin's "Bonzo's Montreux," and vocal-fattening on the Grateful Dead's *Steal Your Face*; Frank Zappa ran one in his guitar rig, and Elton John and Laurie Anderson used it live.
- The **H3000** became the studio pitch/modulation standard of the late '80s–'90s; **Brian Eno** wrote Eventide to thank them for it.
- The pedal line (H9/H9 Max) is a fixture on ambient, post-rock, and shoegaze boards. Eventide's [artist roster](https://www.eventideaudio.com/artists/) historically includes players like Pete Thorn and a deep bench of session/ambient guitarists; reviewers consistently frame the H90 as the "heart of the rig" ambient workstation rather than a one-trick pedal.

Treat the H90's pedigree as *the algorithms' pedigree* — when you run Blackhole or the H910 emulation, you're running the exact lineage that processed those records.

## 8. Live / Power / I/O

- **Power — read carefully, the rig sheet and GearProfile are both slightly off.** The H90 ships with a **12 VDC, center-POSITIVE, 5.5/2.5 mm** adapter. Per the manual's Tech Specs ([§B](manuals/EventideH90.pdf), corroborated by [Eventide's online specs](https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/appendix/specifications.html)) it draws **600 mA at 12 V** *or* **800 mA at 9 V**. So: the GearProfile's "9V-center-neg-700mA" is wrong on **three** counts — it is center-**positive**, and it needs **800 mA at 9 V** (not 700), or run it at 12 V for 600 mA. **Flag for the owner:** budget a dedicated high-current isolated outlet — at 9 V you need a true 800 mA+ slot (e.g. a Strymon Ojai/Zuma high-current port or the supplied brick); a typical 500 mA "digital" slot will not power it. Running it at the supplied **12 V is the safer, lower-current option** if the board's 12 V rail is available.
- **Audio I/O.** Four ¼" mono inputs, four ¼" mono outputs, all individually switchable **instrument or line** level. In this rig: stereo in (Ins 1/2) from the Chroma Console, stereo out (Outs 1/2) to the PORTA424, set to **line** level. Input impedance >600 kΩ (instrument) / 80 kΩ (line); output 220 Ω; max input +4 dBu (inst) / +14 dBu (line); 48 kHz, 24-bit AD/DA, 32-bit float DSP.
- **MIDI.** Full **5-pin DIN In and Out/Thru**, plus **MIDI over USB-C**. Channel 1–16, Receive Omni, Output mode Transmit/Thru/Off, selectable **clock source (DIN or USB)** so the H90 can slave to or master the rig's tempo. Program Change selects Programs; CCs map to virtually any parameter (Quick Knobs, HotKnobs, HotSwitches, Performance params, gains, mix). MIDI Global Control + Transmit let aux switches/expression pedals on the H90 *transmit* CCs to other pedals. This is a genuine strength in a MIDI-heavy rig — see §9.
- **EXP/CTL.** Two ¼" TRS jacks: up to two expression pedals, two 5 V CV sources, or up to six aux footswitches (or a combination). Global Pedal Control can pin an expression pedal to, e.g., a HotKnob across all Programs.
- **Presets/Programs.** 99 Programs per List, 33 banks of three; Factory + User Lists; Perform-mode footswitch remapping; spillover on Program change.
- **Footprint/weight.** 65 × 179 × 136 mm (2.5 × 6.5 × 5.25 in), 1.36 kg / 1.85 lb. Bigger than a standard pedal but small for what it replaces.

## 9. Pairing Recommendations (by name)

- **After the Chroma Console (its upstream neighbor):** let Chroma do character/color/lo-fi, let the H90 do the *big* space and pitch. Don't double reverbs — if Chroma's Space character is engaged, keep the H90's reverb Size/Mix in check, or vice versa.
- **Catching the sustained Hizumitas / EAE Longsword walls (Board 1):** a sustained fuzz wall is the ideal Blackhole/Shimmer/MangledVerb input — dense, stable, no transients to smear. Use **Blackhole Freeze** or **Shimmer Pitch Freeze** to lock a fuzz chord into an infinite pad and play over it. The Hizumitas dossier already names CrushedHall/Blackhole/MangledVerb as ideal partners; consistent here. (Note: "CrushedHall" is a community/preset name; the on-board reverb algorithm is **Hall** — the crushed/degraded character comes from pushing Hall hard or routing through MangledVerb.)
- **Versus OBNE Dark Star V3 (Board 2 pad reverb):** Dark Star is the *upstream, granular, smeared* pad-reverb that lives mid-chain and feeds texture forward. The H90 is the *downstream, hi-fi, controllable* master reverb. They're complementary, not redundant — Dark Star creates the bed; the H90 places it in a defined, automatable space and prints it. If they fight, pull Dark Star's mix back and let the H90 lead the ambient final.
- **Versus Walrus QI Etherealizer (Board 2):** QI is the mid-chain ethereal/harmonic texture box; the H90 is the end-chain space + intelligent pitch engine. Use QI for shimmer-ish *texture* early, the H90 for *structured* harmony (Polyphony/Diatonic) and the final reverb.
- **Versus CB Big Time (Board 3 delay):** Big Time owns the rhythmic/character stereo delay slot; let the H90's delays be *ambient* (UltraTap swells, Reverse, SpaceTime delay-verb) rather than competing for the rhythmic-eighths role Big Time already fills.
- **MIDI in the Chase Bliss stack:** the H90 should join the MIDI chain with the CB pedals (Generation Loss, Big Time, MOOD MkII, Blooper) and the Chroma Console. Slave the H90's clock to the rig's MIDI tempo (Clock Source: DIN), and use Program Change to recall H90 Programs in sync with CB preset changes. The VG-800's pitch-to-MIDI could even drive H90 parameters via CC, though tracking-driven control is best reserved for slow/pad moves.

## 10. Reviews & Demos (real links)

- [Premier Guitar — Eventide H90 review](https://www.premierguitar.com/gear/reviews/eventide-h90) — 4.4/5, $899; best on the dual-algorithm "lattices of sound," the H9000 heritage, and the learning curve.
- [Guitar.com — "Bringing the classic H9 into the 2020s"](https://guitar.com/reviews/effects-pedal/eventide-h90-review/) — best on what's new vs the H9 and the ARM re-voicing.
- [MusicRadar — Eventide H90 Harmonizer review](https://www.musicradar.com/reviews/eventide-h90-harmonizer) — strong on interface and the three play modes.
- [Sound On Sound — Eventide H90 Harmonizer review](https://www.soundonsound.com/reviews/eventide-h90-harmonizer) — studio-leaning, thorough on I/O and routing.
- [Tape Op — H90 review](https://tapeop.com/reviews/gear/158/h90-harmonizer-multi-effects-pedal) — recordist's perspective.
- [Guitar Pedal X — H90 "doubles down on the H9 Max"](https://www.guitarpedalx.com/news/gpx-blog/eventides-new-h90-harmonizer-multi-fx-workstation-essentially-doubles-down-on-the-h9-max-with-much-improved-interface-and-connectivity-and-with-10-new-algorithms-onboard) — best feature-by-feature H9-Max comparison.
- [Perfect Circuit — H90 review](https://www.perfectcircuit.com/signal/eventide-h90-harmonizer-review) — good algorithm walkthrough.
- [Eventide — H90 product page](https://www.eventideaudio.com/pedals/h90/) and [online manual/specs](https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/appendix/specifications.html).
- [YouTube — "THE AMBIENT GUITAR POWERHOUSE! Eventide Blackhole Reverb"](https://www.youtube.com/watch?v=OGBJ2esavik) — Blackhole-focused ambient demo (Blackhole pedal, same algorithm).
- [Vintage King — History of the Eventide Harmonizer](https://vintageking.com/blog/eventide-harmonizer/) and [Valhalla DSP — H910 history](https://valhalladsp.com/2010/05/07/early-pitch-shifting-the-eventide-h910-harmonizer/) — the lineage in §1/§7.

## 11. Mods, Quirks, Firmware, Known Issues

- **Firmware is the "mod path."** Unlike an analog pedal, the H90 gains capability via free firmware. Keep H90 Control current — the granular algorithms (Cosmic Web, Glitch, GrainMod, Stutter) and the expanded harmonizer set are *post-v1.1.4* and not in the bundled PDF. ([Sound On Sound](https://www.soundonsound.com/news/eventide-h90-h9000-granular-update), [KVR](https://www.kvraudio.com/news/eventide-updates-software-and-firmware-61841)). Granular processors are directly on-aesthetic for this rig.
- **Power confusion is the #1 real-world issue** — see §8. The center-positive 12 V adapter trips up players who assume 9 V center-negative; never feed it a standard 9 V center-negative pedal supply without confirming polarity and current. Several Eventide forum threads exist precisely on this ([H90 power draw & routing](https://www.eventideaudio.com/forums/topic/h90-power-draw-routing/)).
- **Two-algorithm ceiling** (§4) is a hard design limit, not a bug — plan Programs around the best two effects + HotSwitches.
- **Diatonic/Quadravox are monophonic** trackers; don't expect chordal harmony from them — use Polyphony/Prism Shift for chords (relevant to banjo, §6).
- **Some digital artifacts** in certain pitch voices at extreme settings (noted by Premier Guitar) — choose H949-2/Modern splice types or Pitched mode to minimize.
- **Bluetooth on the panel is non-functional** in current firmware.
- **Learning curve** is the consistent reviewer caveat — the payoff requires manual time. For a one-player live rig, build and label a small set of Programs rather than browsing factory presets on stage.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Stereo dual-algorithm multi-effects / harmonizer |
| Algorithms | 62 shipping (v1.1.4); more via firmware (granular + harmonizer additions) |
| Simultaneous effects | 2 Presets per Program (series or parallel) |
| Routing | Insert (2 mono / 1 stereo insert, Pre/Mid/Post) or Dual (two independent stereo paths) |
| Programs | 99 per List; 33 banks of 3; Factory + User Lists |
| Power | 12 VDC **center-positive**, 5.5/2.5 mm — **600 mA @ 12 V** or **800 mA @ 9 V** |
| Audio I/O | 4× ¼" in, 4× ¼" out; each switchable instrument/line; stereo |
| Input impedance | >600 kΩ (inst) / 80 kΩ (line); rec. load 10 kΩ |
| Output impedance | 220 Ω |
| Max input level | +4 dBu (inst) / +14 dBu (line) |
| Conversion / DSP | 48 kHz, 24-bit AD/DA, 32-bit floating-point DSP |
| MIDI | 5-pin DIN In + Out/Thru; MIDI over USB-C; clock source DIN or USB |
| Control | 2× EXP/CTL TRS (2 exp pedals / 2 CV / up to 6 aux switches) |
| Tuner | Built-in |
| Spillover | Yes, true spillover on Program change |
| Bypass | DSP bypass; selectable Tails per insert/Program |
| Dimensions | 65 × 179 × 136 mm (2.5 × 6.5 × 5.25 in) |
| Weight | 1.36 kg (1.85 lb) |
| Editor | H90 Control (Mac/PC, USB) |
| Bluetooth | On panel; not yet implemented |

Sources: [H90 User Guide §B Tech Specs](manuals/EventideH90.pdf), [Eventide online specs](https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/appendix/specifications.html).

## 13. Starting-Point Settings

Four named Programs to build first. Each is one Program = two Presets (A/B). Set the relevant H90 inputs/outputs to **line** level for this position in the chain.

**(a) Cavernous Blackhole drone** — single chord forever, oceanic
- Preset A: **Blackhole** — Mix 60–80%, Size 90+, Gravity right (long, dense), Feedback near **Infinite**, Mod Depth low, Low Level slightly down to keep the bottom clear.
- Preset B: **Hall** or **Room** at low mix for early-reflection body, or leave B bypassed.
- Routing: Series, B after A. Map **HotSwitch 1 → Blackhole Feedback to Freeze** for an instant locked pad. Feed it a sustained Hizumitas/baritone chord and play over the frozen tail.

**(b) Shimmer / pitch wall** — heavenly octave-up cathedral
- Preset A: **Shimmer** — Mix 50–70%, Pitch Shift A/B set just above/below 1200c (octave), Delay low, Decay high, Pitch Decay high. Use **Pitch Freeze** (performance) to lock the climb.
- Preset B: **Polyphony** at low mix for an octave-stacked body (Percussive mode if banjo-fed), or bypassed.
- Routing: Series. Map **HotSwitch → Shimmer Pitch+verb Freeze** for solo-over pads. The drone/doom shimmer wall.

**(c) Dual delay + reverb** — the Del-Verb replacement, in one Program
- Preset A: **Vintage Delay** or **Tape Echo** — Tempo Sync ON (slave to MIDI clock), dotted-eighth or quarter, moderate feedback, a little Mod.
- Preset B: **Blackhole** or **Plate** — Mix 30–50%, medium Size/decay.
- Routing: **Series, delay → reverb** (so repeats get verbed) — or Parallel if you want them independent. *Or* use **SpaceTime** alone in one Preset for delay+reverb and keep B free for pitch. This single Program is what benches the UAFX Del-Verb.

**(d) Harmonized banjo lead** — banjo-as-lead, in key
- Preset A: **Diatonic** (single-note leads) — set Key via the **Learn** footswitch while playing the root; Pitch A = +3rd/+5th in the song's scale; Delay low; Mix ~40–60% wet. *For chordal banjo use **Polyphony** (Percussive) or **Prism Shift** instead — Diatonic is monophonic.*
- Preset B: **Plate** or **Room** — short, tasteful, to seat the harmony in space.
- Routing: Series, pitch → reverb. Feed the cleanest available banjo tone (consider a less-saturated VG-800 model) so the tracker stays locked.

## 14. Versus Alternatives — why it earns its slot

- **vs Strymon Big Sky (benched, failover).** Big Sky is a brilliant *reverb-only, single-engine* box with 12 machines. The H90 has a deeper reverb stable *and* can run reverb + delay/pitch simultaneously *and* has full pitch/harmonizer DSP the Big Sky simply doesn't. Big Sky stays benched as the **low-power, drop-in failover** for "H90 down" nights — its one genuine advantage here is simplicity and a lighter power draw. Verdict: H90 leads decisively; Big Sky earns a spare slot, not a board slot.
- **vs Strymon TimeLine (benched).** TimeLine is the delay workstation; but the rig's dedicated delay is already the **CB Big Time**, and the H90 adds a full delay suite plus SpaceTime. Big Time (character/rhythmic) + H90 (ambient/algorithmic) cover the live delay needs without TimeLine's overlap. Verdict: justified bench; reconsider only if a specific TimeLine machine becomes essential.
- **vs UAFX Del-Verb (benched, travel only).** Del-Verb *is* a delay+reverb-in-one — a literal subset of one H90 Program (or SpaceTime). The H90 does it with stereo, MIDI, spillover, and dozens more algorithms. Verdict: cleanest bench of the three; Del-Verb's only role is the tiny low-power travel board.
- **vs Meris MercuryX / Strymon Cloudburst / Empress Reverb (not owned, for context).** The H90's differentiator over any single-engine ambient pedal is the *dual-algorithm + deep pitch + Eventide rack heritage* combination — it's a workstation, not a reverb. The trade is complexity and power draw.
- **vs the rig's own OBNE Dark Star V3 / Walrus QI / Hologram Chroma (kept).** These are *not* alternatives — they're upstream texture/character stages the H90 deliberately sits after. The H90 doesn't replace them; it's the structured, automatable, hi-fi space-and-pitch *finisher* before the tape stage.

In this rig — banjo/baritone, drone/doom/shoegaze, a MIDI-linked Chase Bliss/Chroma End Board, and a "print it to degraded tape" final stage — the H90 earns its slot precisely because it is the *one box* that (1) supplies pristine, deep, automatable reverbs the tape stage can ruin beautifully, (2) brings genuinely chord-capable polyphonic pitch/harmony to a banjo-as-lead concept, (3) runs two of those simultaneously with spillover, and (4) speaks MIDI fluently with the rest of the board. That combination is why it benches a Big Sky, a TimeLine, and a Del-Verb at once — each of those does a *part* of the H90's job, and none does more than a slice.

## Sources

- [Eventide H90 User Guide v1.1.4 (PDF in this folder)](manuals/EventideH90.pdf)
- [Eventide — H90 product page](https://www.eventideaudio.com/pedals/h90/)
- [Eventide — H90 online Tech Specs](https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/appendix/specifications.html)
- [Eventide — H90 Reverb algorithm docs](https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/algorithms/reverb.html)
- [Eventide forums — H90 power draw & routing](https://www.eventideaudio.com/forums/topic/h90-power-draw-routing/)
- [Eventide — Artists](https://www.eventideaudio.com/artists/)
- [Premier Guitar — Eventide H90 review (4.4/5, $899)](https://www.premierguitar.com/gear/reviews/eventide-h90)
- [Guitar.com — Eventide H90 review](https://guitar.com/reviews/effects-pedal/eventide-h90-review/)
- [MusicRadar — Eventide H90 Harmonizer review](https://www.musicradar.com/reviews/eventide-h90-harmonizer)
- [Sound On Sound — Eventide H90 Harmonizer review](https://www.soundonsound.com/reviews/eventide-h90-harmonizer)
- [Tape Op — H90 Harmonizer review](https://tapeop.com/reviews/gear/158/h90-harmonizer-multi-effects-pedal)
- [Perfect Circuit — Eventide H90 Harmonizer review](https://www.perfectcircuit.com/signal/eventide-h90-harmonizer-review)
- [Guitar Pedal X — H90 "doubles down on the H9 Max"](https://www.guitarpedalx.com/news/gpx-blog/eventides-new-h90-harmonizer-multi-fx-workstation-essentially-doubles-down-on-the-h9-max-with-much-improved-interface-and-connectivity-and-with-10-new-algorithms-onboard)
- [Synth Anatomy — H90 granular firmware update](https://synthanatomy.com/2025/12/eventide-h90-harmonizer-souped-up-h9-with-twice-the-power-more-algorithms-is-out-now.html)
- [Sound On Sound — H90 & H9000 granular update](https://www.soundonsound.com/news/eventide-h90-h9000-granular-update)
- [KVR — Eventide updates software and firmware](https://www.kvraudio.com/news/eventide-updates-software-and-firmware-61841)
- [Vintage King — History of the Eventide Harmonizer](https://vintageking.com/blog/eventide-harmonizer/)
- [Reverb — The Tech Behind the Eventide H3000](https://reverb.com/news/tech-behind-eventide-h3000-ultra-harmonizer)
- [Valhalla DSP — Early pitch shifting: the Eventide H910](https://valhalladsp.com/2010/05/07/early-pitch-shifting-the-eventide-h910-harmonizer/)
- [YouTube — Eventide Blackhole ambient demo](https://www.youtube.com/watch?v=OGBJ2esavik)
