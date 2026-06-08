# Chase Bliss Onward — Deep Research

A working dossier for a pedal that currently lives **on the bench, not on a board.** The Onward is a stereo dynamic sampler — Chase Bliss's Freeze-and-Glitch capture engine — and in this rig it is benched with the explicit rationale written on the rig sheet: *"Sampling covered by OP-1 + Octatrack + Blooper."* So most of this document is concerned with a different question than an on-board pedal's would be: not "where does it sit in the chain," but "is the bench decision correct, and what would it take to earn a slot back." The short version up front: the bench call is defensible but not airtight — the Onward does one thing (hands-free, dynamics-triggered freeze/glitch that plays *while you play*) that none of the three pedals/boxes named in the rationale actually replicate.

## 1. Lineage: Cooper FX Outward → Chase Bliss Onward

The Onward is not a fresh-sheet Chase Bliss design — it's the second life of **Tom Majeski's discontinued Cooper FX Outward.** Majeski folded Cooper FX into Chase Bliss in 2020 (the deal that brought the Generation Loss and Chroma Console lineages with it), and the Onward is described as "a really smart Tom Majeski pet project / extrapolation from his former Cooper FX Outward Pedal" by [Guitar Pedal X](https://www.guitarpedalx.com/news/gpx-blog/chase-blisss-latest-onward-dynamic-sampling-device-is-a-really-smart-tom-majeski-pet-project--extrapolation-from-his-former-cooper-fx-outward-pedal). Specifically, it "extrapolates and expands on the Envelope-based sampling prowess" of the Outward — the Outward had an Envelope mode that sampled what you played and triggered it from your dynamics, and the Onward takes that single mode and builds an entire pedal around it. The purple-tinted graphics on the enclosure are Chase Bliss's visual cue for the Cooper FX provenance.

It was announced at **Superbooth 2024** and shipped as a standard release in June 2024 at **$399 / €469** ([MusicRadar](https://www.musicradar.com/news/chase-bliss-onward), [Chase Bliss product page](https://www.chasebliss.com/onward)). Tom Majeski, Joel Korte, and Zack Bramble are the names attached to its development and demos.

**The key conceptual distinction — and why it matters for the bench question — is that the Onward is *not a looper.*** A looper records a fixed buffer on a footswitch press and plays it back on a clock. The Onward is a **dynamic envelope sampler**: per the [manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf) (p. 20), "Whenever Onward detects sound at the input, it samples that sound. If there was already a sample, it replaces it instead of resampling." It is *primarily a dynamic effect* — it listens to your pick attack and re-captures continuously, hands-free, so the sampled material is always tracking what you just played rather than a frozen phrase you committed to. That difference is the whole ballgame for the overlap analysis in section 5.

## 2. Controls, Dip Switches & Sample Manipulation

The face is two parallel channels — **Glitch** (repeating, rhythmic, lo-fi chops) and **Freeze** (sustaining, pad-like) — plus three knob-rows that shape them. All from the [manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf):

**General (p. 8–9):**
- **MIX** — balance between dry input and Onward (controls both Freeze and Glitch). When ramping is engaged this knob's job changes to ramp speed.
- **SIZE** — length of the Glitch sample and the master timing reference for the whole pedal. SIZE controls the *subdivision* when MIDI clock-synced. Both Shape and Error timing are linked to SIZE.
- **GLITCH / FREEZE footswitches** — tap to engage; **hold to lock and preserve the current sample** so you can play overtop without replacing it.
- **PRESETS** — left/right footswitch positions store a preset; middle is live. Two onboard presets (122 more via MIDI).

**Effects section (p. 10–11, 30–31):**
- **OCTAVE** — blends a second voice; left half = half-speed/lower-octave, right half = double-speed/upper-octave. Noon = off.
- **TEXTURE** — pushes Onward into distortion. Left half = sample-rate reduction (digital "seasoning"); right half = soft-clipping overdrive with compression. Noon = off. **Secret tone:** a hidden EQ lives behind this knob in Hidden Options.
- **ANIMATE toggle** — left = vibrato (rate set by SIZE), center = none, right = chorus (slow, fixed, atmospheric).

**Shape section (p. 12–13, 32–33):** how it moves.
- **SUSTAIN** — hold time before sounds fade. Max = infinite hold until you re-trigger. Doubles as a **repeat-count selector** on the Glitch side (1x–16x).
- **FADE toggle** — fade in/out (crossfade) time: SLOW (swell-y), USER (custom value set in Hidden Options), FAST (immediate).

**Error section (p. 13, 34–37):** randomization/variation.
- **ERROR knob** — chance and intensity of errors occurring.
- **TYPE toggle** — TIMING (changes sample size → rhythmic variation on Glitch, churning synth-like motion on Freeze), CONDITION (mutes + sample-rate shifts; adds sparseness/bite), PLAYBACK (destabilizes speed and direction — 2x/4x, reversed).

**The white "Customize" dip switches on top (p. 40–41)** — saved with presets:
| Dip | Function |
|---|---|
| **MISO** | Mono In, Stereo Out — splits a mono input into stereo |
| **SPREAD** | Widening + stereo movement tied to the Error effects |
| **LATCH** | Footswitches latch instead of momentary |
| **SIDECHAIN** | Freeze dips in volume when Glitch resets (pumping) |
| **DUCK** | Both channels dip when input audio is present (dynamic ducking) |
| **REVERSE** | Glitch plays in reverse |
| **½ SPEED** | Halves Glitch record quality → doubles sample length, lo-fi |
| **MANUAL** | Disables dynamic triggering; footswitch tap = sample, hold = infinite hold, double-tap = disengage |

There are also **Hidden Options** (hold both footswitches — p. 14–17): Sensitivity (on SIZE), Balance (on MIX), Duck Depth (on OCTAVE), User fade value (on SUSTAIN), Error Blend (on ERROR — mixes all three error types), EQ (on TEXTURE — clockwise thins/removes lows, counter-clockwise darkens), plus per-section **Routing** toggles (TYPE/FADE/ANIMATE) that isolate Error, Shape, or Effects to *one channel only*. **Hidden Gestures** (p. 18–19): tap-tempo (double-tap both), Dry Kill (hold Glitch on power-up), Trails (hold Freeze on power-up).

## 3. Sonic Character — What It's Good At

The Onward is two voices that you steer with your hands:

- **Freeze** is the more conventional half — captures and sustains a single moment into "a soft, floating pad" ([manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf) p. 22). It "can be used to make droning background ambience, or a supportive harmonizing voice, or to turn your instrument into a synth." This is the doom/drone-friendly side.
- **Glitch** is the more interesting half by most reviewers' reckoning — it samples and repeats *small chunks* of audio (max ~1 second record time, SIZE-controlled), producing "dynamic loops, strange echoes, and of course, glitches" (p. 26). Pre-cursive, stuttering, rhythmic, lo-fi.

The defining sonic trait per [Guitar.com's hands-on review](https://guitar.com/reviews/effects-pedal/hands-on-chase-bliss-onward-review/): "no matter what side you're on, this pedal will jump in volume depending on the dynamics of your pick attack." The reviewer reaches for an Ed O'Brien comparison on the Freeze side ("sustaining glitchy ambient pad-like chords that aren't overbearing") and, paired with a Strymon BigSky, got "luscious dreamscapes reminiscent of Minus The Bear's Dave Knudson scoring a Sigur Rós album." That is squarely the owner's drone/shoegaze target. The honest caveat from the same review: the pedal is "not for everyone," and with both channels running at once the result can become "chaotically immersive" but hard to place in a conventional song.

The "you get what you give" principle runs through the whole thing ([manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf) p. 23): soft/sparse playing yields smooth shapeless pads; fast/intense playing yields spikier sounds with audible repetition. The instrument *is* the macro control.

## 4. Behavioral Notes — Capture, Re-trigger, Stereo, Clock

- **Capture is automatic and continuous.** It samples on detected input and *replaces* the existing sample rather than stacking — unless you **hold a footswitch to lock** the current sample, which lets one channel stay frozen while the other keeps following you. That two-state behavior (one steady, one dynamic) is the core trick.
- **Sensitivity matters.** The threshold for what counts as a trigger is set by the hidden Sensitivity option (on SIZE); "around noon will work best in most cases" ([manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf) p. 14). With a hot, transient-rich source (banjo via GK-5, modeled VG-800 output) you'll want to tune this.
- **Stereo is real.** Stereo I/O with analog dry-thru; SPREAD and the Error section generate genuine stereo movement (errors occur on one channel or another). MISO splits a mono guitar into stereo.
- **Clock sync is via MIDI.** With MIDI clock present, SIZE sets the subdivision — so the Glitch repeats lock to tempo. MIDI requires a **Chase Bliss MIDIbox** to convert the signal to the 1/4" TRS jack ([manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf) p. 45). There is no internal tap-to-clock-out; tap-tempo is manual (double-tap both footswitches).
- **MANUAL mode** turns it into a more traditional, footswitch-controlled sampler if you don't want dynamic triggering at all.

## 5. Bench Placement — Why It's Off the Board (and When It Goes On)

The rig sheet's stated reason: **"Sampling covered by OP-1 + Octatrack + Blooper."** Let's be honest about whether that's true, device by device, because the overlap is shallower than the one-liner suggests:

- **TE OP-1 Field** — a portable all-in-one sampler/synth/4-track. It samples, but it is a *destination instrument* you play deliberately, not a real-time effect in a guitar chain that re-captures from your pick dynamics. Zero overlap with hands-free, play-along sampling. It covers "sampling" the way a DAW covers "delay" — technically yes, functionally no.
- **Elektron Octatrack MkII** — the deepest sampler the owner has, and the one that genuinely *can* do live-input sampling and re-triggering. But it's a studio/centerpiece box driven from a sequencer and pads, not a pedal you stomp into a stereo loop. It overlaps on capability, not on workflow.
- **CB Blooper** — the closest real overlap, and it's already on Board 3. Blooper is a **looper**: you commit a loop on a footswitch, then stack modifiers and layers. The Onward is the *opposite philosophy* — it never asks you to commit; it samples continuously off your dynamics and plays *alongside* you. Blooper makes loops you build; Onward makes accompaniment that follows. They are complementary, not redundant.

So the bench rationale is defensible at the level of "I already own enough boxes that record audio," but it slightly overstates the case: **none of the three do dynamics-triggered, hands-free freeze/glitch in a stereo guitar chain.** The thing the Onward uniquely offers — play a chord, get an instant evolving pad + a rhythmic glitch chop that tracks your attack, with no footswitch dance — is not covered by OP-1, Octatrack, or Blooper.

**When it earns a slot back:**
1. **Board 2 (Texture), after Microcosm / before Dark Star V3.** This is its natural home. The owner's middle board is the granular/smear board; the Onward's Freeze pad + Glitch stutter would feed Dark Star's reverb-smear beautifully and overlaps far less with that board than it does with Board 3's looper.
2. **Studio capture rig.** As a stereo, MIDI-clockable, preset-recallable sampler it's a perfect "play a part, instantly get an evolving ambient bed" tool printed to the Apollo x8 — exactly the kind of move the rig's tape-print aesthetic (PORTA424 → JHS 424 → Apollo) is built for.
3. **Hands-free live ambient.** The single biggest live argument for the Onward over the OP-1/Octatrack is that it needs *no hands and no eyes* — it just follows your dynamics. For a solo drone/shoegaze set where the player can't go fiddle with an Octatrack, that's decisive.

Verdict on placement is in section 14. Short form: bench is fine *for now* because Board 3 is already a 4-Chase-Bliss logjam, but the Onward is the strongest bench candidate to swap onto **Board 2**, not a true redundancy.

## 6. Source-Specific Notes (this rig's instruments)

- **Banjo (Gold Tone EBM-5 + GK-5 → VG-800):** banjos have a fast, percussive attack and fast decay — which is *exactly* what the Onward's dynamic triggering is built to exploit. Each plucked note re-samples; the Glitch side turns banjo rolls into rhythmic stutter beds, and the Freeze side sustains a banjo chord into a pad it can't naturally hold. Tune Sensitivity (on SIZE) carefully — the GK-5's hot, transient per-string output will over-trigger at noon; back it toward LESS. This is arguably the most compelling source for the pedal in the whole rig: it makes the banjo do something it physically cannot (sustain), which is the owner's "banjo-as-lead / sustained walls" aesthetic in one box.
- **Baritone Jazzmaster (magnetic + GK-5 → VG-800):** low, dense source. Use OCTAVE on the left (half-speed/octave-down) for the "Sub Synth" doomy bed the manual describes (p. 24). Freeze + max SUSTAIN = infinite low drone.
- **Modeled VG-800 output:** the Onward sees the VG-800's summed stereo line out — a fully-formed modeled amp/synth signal. It will sample whatever the VG-800 hands it, including COSM synth/pad patches, so you can freeze a guitar-synth pad and glitch it. Watch input level: the EHX Effects Interface (on the bench) exists precisely to reconcile VG-800 *line* level to pedal *instrument* level, which is the right buffer in front of the Onward if line level over-drives its input/triggering.
- **Bass (Fender Pro Jazz):** Freeze + octave-down makes sub drones; Glitch with ½ SPEED dip on for longer, lo-fi rhythmic bass chops.

## 7. Famous Users (honest)

The Onward is new (mid-2024), so there's no deep artist mythology yet. Verified sightings, per [Equipboard](https://equipboard.com/items/chase-bliss-audio-onward) and Chase Bliss's own promo: it's on **Balsac the Jaws of Death**'s (GWAR) board and on **Austin Hull**'s board, and **Courtney Swain** (Bent Knee) demoed it for live vocals and ambient textures. Chase Bliss's launch demos feature Joel Korte, Tom Majeski, and Zack Bramble. Beyond that, it's largely an ambient/experimental-guitarist and modular-curious crowd so far — no single artist has claimed it as a signature voice the way Wata owns the Hizumitas. **(Flag: artist list is thin and partly promo-sourced; treat as indicative, not exhaustive.)**

## 8. Live / Power / I/O

- **Power:** 9V DC center-negative, **~200 mA** ([manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf) p. 2; [product page](https://www.chasebliss.com/onward)). This is a hungry digital pedal — budget a 250 mA+ isolated supply slot. Higher than most of the analog board.
- **I/O:** Stereo in / stereo out (TRS for stereo, TS for mono), **analog dry-thru.** MISO dip splits mono→stereo.
- **Bypass:** selectable **true / buffered bypass**; Trails available (hold Freeze on power-up) so effects fade rather than cut.
- **MIDI:** PC, CC, Clock Sync via 1/4" TRS — requires a **Chase Bliss MIDIbox** adapter ([MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/6667428b9de7197838995a79/1718043288825/Onward_MIDI-Manual_Pedal_Chase+Bliss.pdf)). 122 MIDI presets + 2 onboard.
- **CV / Expression:** EXP/CV jack (TRS expression or TS CV, 0–5V — **negative or over-voltage can damage the pedal**, per [manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf) p. 44). The same jack can take a normally-open momentary footswitch to externally trigger Glitch. Any knob can be assigned to CV/exp via the dip-switch routing.
- **Enclosure:** Chase Bliss's larger dual-footswitch format (same family as Blooper / Generation Loss). **(Flag: exact dimensions not published on the product page; not web-verified — confirm against the physical unit.)**

## 9. Pairing Recommendations (by name)

- **vs / with Blooper (Board 3):** Don't think redundancy — think relay. Use the Onward to *generate* an evolving pad/glitch off your playing, then commit the good bits into Blooper to layer and modify. Onward = source, Blooper = builder.
- **vs MOOD MkII (Board 3):** MOOD is a micro-looper/granular smear that's always running against your live signal — closest cousin in spirit. The Onward is more *musical/melodic* (it samples discrete events and harmonizes/octaves them); MOOD is more *textural mush*. If anything the Onward would let you retire MOOD's micro-loop duties, not the reverse.
- **vs Microcosm (Board 2):** Microcosm is granular phrase-looping with preset rhythmic patterns; the Onward is dynamics-driven and hands-free. Run **Onward → Microcosm** and you get evolving capture feeding granular re-processing — a deep ambient pipeline. This is the single best on-board home for it.
- **Into Dark Star V3 / QI Etherealizer (Board 2):** the Onward's pad output is a perfect input for spectral reverb smear. Freeze a chord, let Dark Star drone it out.
- **Into H90 / BigSky (bench):** reviewers specifically loved Onward → BigSky; on this rig, Onward → H90 hall/shimmer is the studio move.
- **In front of it:** the **VG-800** (modeled tones to sample) and **EHX Effects Interface** (level matching) are the right upstream. A drive (Brothers AM, Hizumitas) before it gives the sampler grittier raw material.

## 10. Reviews & Demos (real links)

- [Guitar.com hands-on review](https://guitar.com/reviews/effects-pedal/hands-on-chase-bliss-onward-review/) — best written review; "most accessible Chase Bliss pedal," the BigSky pairing, the "not for everyone" caveat.
- [Guitar World news/overview](https://www.guitarworld.com/news/chase-bliss-onward) — "glitching and freezing heaven for guitarists of all styles."
- [MusicRadar — Superbooth 24 announcement](https://www.musicradar.com/news/chase-bliss-onward) — release context, "simply plug in and start doing what you do."
- [Guitar Pedal X — Cooper FX Outward lineage piece](https://www.guitarpedalx.com/news/gpx-blog/chase-blisss-latest-onward-dynamic-sampling-device-is-a-really-smart-tom-majeski-pet-project--extrapolation-from-his-former-cooper-fx-outward-pedal) — the only good writeup of the Outward → Onward genealogy.
- [Pedal of the Day feature](https://www.pedal-of-the-day.com/2024/07/13/chase-bliss-onward-dynamic-sampler/) — solid plain-language overview.
- [Delay Dude review](https://delaydude.de/en/english-review-chase-bliss-onward-effect-pedal/) — "absolute recommendation for fans of unusual glitch and freeze sounds."
- [Chase Bliss official demo — Onward Dynamic Sampler](https://www.youtube.com/watch?v=UtGwQ6OfZNk) — Joel/Tom/Zack walkthrough.
- [Chase Bliss Onward — main launch video](https://www.youtube.com/watch?v=ozK-TgxIq8c).
- ["Onward and Synth — Does it work?"](https://www.youtube.com/watch?v=VVvOXdazaOY) — directly relevant to the VG-800/synth-source question.
- [Demo 5: Why Buy This?](https://www.youtube.com/watch?v=VMxExzUHq7w) — Chase Bliss's own "is this for you" pitch.

## 11. Mods, Quirks, Firmware

- **Firmware is user-updatable** via Chase Bliss's web-based [Bliss Programmer](https://firmware.chasebliss.com/) and the open-source [CBA Firmware Interface Program](https://github.com/chasebliss/cba-firmware-interface-program). Worth checking for updates before deploying — Chase Bliss ships behavior/bug fixes post-launch.
- **CV/EXP voltage is fragile:** 0–5V only; negative or higher voltage **can damage the pedal** ([manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf) p. 44). Use the right cable (floating-ring TRS-to-TS for CV).
- **MIDI needs the MIDIbox** — there's no DIN jack; budget for the adapter if you want it in the owner's Chase Bliss MIDI-clock ecosystem.
- **Quirk, not a bug:** dynamic triggering means it can re-sample at moments you didn't intend if Sensitivity is off. Lock a footswitch (hold) or use MANUAL mode for predictability.
- **No reported reliability issues** — standard Chase Bliss build quality, preset/dip-switch state saved across power cycles. Dry Kill and Trails are remembered preferences set by power-up gestures.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Stereo dynamic envelope sampler (Freeze + Glitch channels) |
| Power | 9V DC center-negative, **~200 mA** |
| I/O | Stereo in / stereo out (TS mono, TRS stereo); analog dry-thru; MISO mono→stereo |
| Bypass | Selectable true / buffered; Trails optional |
| MIDI | PC, CC, Clock Sync via 1/4" TRS (requires Chase Bliss MIDIbox) |
| Presets | 2 onboard + 122 via MIDI |
| CV / Expression | 1 jack, 0–5V (negative/over-voltage damages pedal); ext. Glitch footswitch |
| Ramping | Bounce (LFO) + Ramp (one-shot) on any knob via dip switches |
| Controls | MIX, SIZE, OCTAVE, TEXTURE, ERROR, SUSTAIN; ANIMATE/FADE/TYPE toggles; 8 dip switches |
| Max sample (Glitch) | ~1 sec (doubled with ½ SPEED dip) |
| Dimensions | Large CB dual-footswitch enclosure (exact figures unverified) |
| Price (launch) | $399 / €469 |
| Released | June 2024 (announced Superbooth 24) |
| Lineage | Cooper FX Outward (Envelope mode), Tom Majeski |

Sources: [Chase Bliss product page](https://www.chasebliss.com/onward), [manual](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf).

## 13. Starting-Point Settings

Named scenarios to get going. Knob positions are clock-face.

**(a) Instant Eno** — sprawling ambient bed; the manual's flagship patch (p. 25)
- MIX noon, SIZE ~2 o'clock, OCTAVE noon, ERROR ~10, SUSTAIN max, TEXTURE noon
- TYPE = Timing, FADE = Slow, ANIMATE = Chorus. Play slowly and patiently; samples fade in. Freeze-forward, oceanic. Pair into Dark Star / H90.

**(b) Sub Synth (baritone/bass doom)** — doomy lower-register synth (manual p. 24)
- OCTAVE fully left (half-speed/octave-down), SUSTAIN high, FADE slow, TEXTURE noon, ANIMATE off
- Hold Freeze to lock an infinite low drone. Best on baritone JM or Jazz bass.

**(c) Auto-Repeater (banjo glitch)** — rhythmic stutter bed off banjo rolls (manual p. 29)
- Glitch engaged, SIZE ~11, SUSTAIN low (so repeats fade out cleanly), FADE = Fast, ERROR center (Condition) for sparseness
- Tune Sensitivity toward LESS for the hot GK-5 signal. Pre-cursive banjo loops that track your picking.

**(d) Living Pad / Dancing Drone** — locked infinite pad with motion (manual p. 24, 37)
- Hold Freeze to lock infinite pad, then ERROR ~11 with TYPE = Playback for momentary pitch/direction shifts; ANIMATE = Chorus
- A frozen chord that never quite sits still. The shoegaze wall in one footswitch.

## 14. Versus Alternatives — and Is the Bench Decision Right?

**Direct conceptual competitors (most the owner already has):**
- **CB Blooper** — looper, commit-based, on-board. Complementary, not equivalent (section 5). Onward generates; Blooper builds.
- **CB MOOD MkII** — always-on micro-looper/granular. Closest live-feel cousin; muddier and more textural where Onward is more melodic/harmonic. Onward could subsume MOOD's role more easily than vice versa.
- **Hologram Microcosm** — granular phrase looper with rhythmic presets, on Board 2. Different engine (preset patterns vs dynamic capture); they stack beautifully in series.
- **Old Blood Noise Parting** — glitch/sampler on Board 2; overlaps the Glitch side's stutter character but lacks the Freeze pad and the dynamic-pad workflow.
- **Outside the rig:** Gamechanger Plus Pedal (sustain/freeze), EHX Freeze/Superego (freeze-only), Red Panda Tensor (sampler/pitch), Boss SL-2 Slicer. The Onward's differentiator vs all of these is the **two-channel dynamic capture + deep Error/Shape/routing + stereo + MIDI** in one box.

**Is the bench call right?** Mostly, with one asterisk. The rig sheet's logic ("sampling covered") holds at the inventory level: this player owns an Octatrack and an OP-1 Field and a Blooper, and Board 3 is already four Chase Bliss pedals deep — adding a fifth there would be gratuitous. **For Board 3, benching the Onward is correct.** But the rationale misreads the Onward slightly: it is not a redundant looper, it's a *hands-free dynamics-triggered freeze/glitch* tool that none of the named devices replicate in a stereo pedal workflow. The right move isn't "keep it benched forever" — it's **"swap it onto Board 2 (Texture), placed Onward → Microcosm → Dark Star,"** where it would do something the middle board can't currently do (instant evolving pads off your playing) and overlap far less than it does on the looper-heavy end board. Failing that, it's a near-ideal studio capture box printed to the Apollo. **Verdict: bench it off Board 3 — yes; write it off entirely — no. It's the strongest bench candidate to promote, and its truest home is the granular middle board, not the looper end board the rationale compares it against.**

## Sources

- [Chase Bliss — Onward product page](https://www.chasebliss.com/onward)
- [Onward manual (PDF, local)](manuals/Onward_Manual_Pedal_Chase-Bliss.pdf)
- [Onward MIDI manual (PDF)](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/6667428b9de7197838995a79/1718043288825/Onward_MIDI-Manual_Pedal_Chase+Bliss.pdf)
- [Guitar Pedal X — Onward / Cooper FX Outward lineage](https://www.guitarpedalx.com/news/gpx-blog/chase-blisss-latest-onward-dynamic-sampling-device-is-a-really-smart-tom-majeski-pet-project--extrapolation-from-his-former-cooper-fx-outward-pedal)
- [MusicRadar — Superbooth 24 announcement](https://www.musicradar.com/news/chase-bliss-onward)
- [Guitar.com — Onward hands-on review](https://guitar.com/reviews/effects-pedal/hands-on-chase-bliss-onward-review/)
- [Guitar World — Onward overview](https://www.guitarworld.com/news/chase-bliss-onward)
- [Pedal of the Day — Onward Dynamic Sampler](https://www.pedal-of-the-day.com/2024/07/13/chase-bliss-onward-dynamic-sampler/)
- [Delay Dude — Onward review](https://delaydude.de/en/english-review-chase-bliss-onward-effect-pedal/)
- [Equipboard — Onward (artist sightings)](https://equipboard.com/items/chase-bliss-audio-onward)
- [Chase Bliss Bliss Programmer (firmware)](https://firmware.chasebliss.com/)
- [CBA Firmware Interface Program (GitHub)](https://github.com/chasebliss/cba-firmware-interface-program)
- [Chase Bliss official Onward demo (YouTube)](https://www.youtube.com/watch?v=UtGwQ6OfZNk)
- [Chase Bliss Onward launch video (YouTube)](https://www.youtube.com/watch?v=ozK-TgxIq8c)
- [Onward and Synth — Does it work? (YouTube)](https://www.youtube.com/watch?v=VVvOXdazaOY)
- [Onward Demo 5: Why Buy This? (YouTube)](https://www.youtube.com/watch?v=VMxExzUHq7w)
