# Strymon TimeLine — Deep Research

A working dossier for a pedal that is currently **on the bench**, not on the board. In this drone/doom/shoegaze rig the TimeLine's delay duties are already covered twice over: the Chase Bliss Big Time handles primary stereo delay on Board 3, and the Eventide H90 covers algorithmic delay + reverb in the same End Board. The rig sheet says it plainly — *"Big Time + H90 delays cover the live needs."* So this document does two jobs: it documents what a flagship 12-machine delay workstation can actually do, and it argues honestly about why it sits in the drawer — and the specific failures or studio sessions that would put it back in the signal chain.

## 1. Lineage: What the TimeLine Is

The TimeLine launched in 2011 as Strymon's flagship delay — the time-domain counterpart to the BigSky reverb (2013) and the Mobius modulation box. Where most delay pedals give you one circuit, the TimeLine ships **12 distinct delay "machines,"** several of which are direct descendants of Strymon's single-purpose boxes: the **dTape** machine is the sliding-head tape engine at the heart of the [El Capistan](https://www.strymon.net/product/timeline/), and **dBucket** is the bucket-brigade emulation from the company's analog-delay work, all running on a high-performance **SHARC DSP** with an analog dry path and 24-bit/96kHz converters ([MusicRadar review](https://www.musicradar.com/reviews/guitars/strymon-timeline-523567), [Premier Guitar review](https://www.premierguitar.com/gear/strymon-timeline-pedal-review)).

The 12 machines are: **dTape, dBucket, Digital, Dual, Pattern, Reverse, Ice, Duck, Swell, Trem, Filter, Lo-Fi.** On top of those it stacks **200 presets** (100 banks × A/B), a **30-second looper**, full MIDI, stereo I/O, and an expression input. Firmware has matured over a decade; the current and final shipping version is **Rev. 1.88 (April 2020)**, which patched a DSP-bandwidth edge case when running dBucket at its longest delay time inside the looper. Earlier landmark revisions added looper Undo/Redo and 100%-wet recording (v1.23), preset spillover "trails" (v1.23), per-preset MIDI clock plus MIDI THRU/MERGE (v1.84), and MultiSwitch Plus support (v1.87) ([Strymon firmware release notes](https://www.strymon.net/faq/timeline-firmware-revision-release-notes/)). The unit owned here ships with the Rev H manual (09.17.2021), which matches the 1.88 feature set.

This is, in short, a delay workstation — the kind of pedal that on most boards would be the *only* time-based effect because it can be twelve of them.

## 2. Controls & the 12 Machines

The front panel is eight knobs plus the TYPE encoder and three footswitches (A / B / TAP). The top row — **VALUE, TIME, REPEATS, MIX** — and bottom row — **FILTER, GRIT, SPEED, DEPTH** — change function per machine, which is the whole trick. Per the [Rev H manual](manuals/TimeLine_UserManual_RevH.pdf):

- **VALUE** — fine delay-time adjust; **push** to enter the per-machine PARAMS menu, **hold** for the GLOBALS menu.
- **TIME** — coarse delay time (display toggles ms/BPM).
- **REPEATS** — feedback / number of repeats.
- **MIX** — analog wet/dry blend; ~3 o'clock is 50/50.
- **FILTER** — repeat-filter shape: flat at minimum, progressively darker, analog-EQ curve around noon, tape-like EQ at max. (Becomes **Tape Age** on dTape, **bucket filter** on dBucket.)
- **GRIT** — progressively adds distortion/artifacts; intensity scales with input level. (Becomes **Tape Bias** on dTape, **Bucket Loss** on dBucket.)
- **SPEED / DEPTH** — modulation-LFO rate and intensity (Tape Crinkle / Wow & Flutter on dTape).
- **TYPE** — selects machine; **push** toggles bank/time display; **hold** to SAVE.

Every machine also exposes deep PARAMS (Tap Division, Boost ±3dB, Persist/trails, Name, EP Set, Tap Mode, MIDI Clock on/off) plus its own machine-specific menu. The twelve, briefly:

- **Digital** — crystal-clear voiced digital; PARAMS add Smear, switchable High Pass (off → 900Hz), Repeat Dynamics. Modern-to-'80s clean delay.
- **Dual** — two delay lines, series or parallel, second locked to the first by a selectable ratio (1/8 up to 8/1). The U2/Edge dotted-eighth + quarter trick lives here.
- **Pattern** — 16 selectable rhythmic/ping-pong repeat patterns; pattern 16 is an early-reflection "reverb" trick with Smear maxed.
- **Reverse** — input-triggered reverse so the backwards swell is predictable and repeatable.
- **Ice** — slices the input and pitches the chunks from −1 oct to +2 oct (full interval menu); BLEND, SLICE size, Smear. Shimmer/crystalline territory.
- **Duck** — dynamic delay that sidechains to your playing (Sensitivity, Release, Normal/GATE feedback).
- **Swell** — auto-volume-swell attack (Rise Time 0.10–4.0s) for stealthy ambient pads.
- **Trem** — tremolo synced to the repeats; selectable LFO shapes, speed as a ratio of delay time.
- **Filter** — sweeping resonant filter on the repeats, pre or post delay, with selectable Filter-Q up to 10.
- **Lo-Fi** — creative destruction: sample-rate down to 750Hz, bit depth down to 4-bit, "dVinyl" dust/scratch noise, and eight gadget filter shapes (Victrola, AM radio, cell phone, intercom…).
- **dTape** — sliding-head tape emulation: Tape Speed (Normal/Fast), Low End Contour, and the four re-mapped knobs (Tape Age, Tape Bias, Tape Crinkle, Wow & Flutter) that let you dial in a perfectly serviced deck or a chewed-up one.
- **dBucket** — analog BBD emulation: Single (one 4096-stage chip, 40–400ms) or Double (two chips, 80–800ms), with Filter and Bucket Loss controlling the warm/fuzzy degradation.

## 3. Sonic Character / Standout Machines

For *this* aesthetic — degraded textures, sustained walls, banjo-as-lead — the standout machines are not the pristine ones. **dTape** and **dBucket** are the home base: dTape with Tape Age clockwise, Tape Bias low, and Wow & Flutter cranked produces the seasick, smearing repeats that fit a shoegaze wall; dBucket Single with Bucket Loss at 3 o'clock collapses into the warm, fuzzy garbage-can decay of the earliest analog delays. **Lo-Fi** is the secret weapon — sample-rate aliasing, 4-bit crush, and dVinyl static turn a clean repeat into a broken-transmission artifact, which is exactly the "recorded wrong" character the rig is built around. **Ice** delivers the shimmer/crystalline drone color, and **Pattern 16 / Swell** can fake reverb-adjacent ambience without a reverb engine. Where the Big Time is a focused, characterful single-circuit delay and the H90 is a hi-fi algorithmic monster, the TimeLine's edge is **breadth of grime in one box** — twelve flavors of decay, several of them ugly on purpose.

## 4. Behavioral Notes (looper, spillover, stereo, MIDI)

- **Looper** — 30s, pre or post delay (GLOBALS → LP LOC), with a dedicated looper mode (hold TAP). Record/overdub on A, play/re-trigger on B, stop on TAP. Firmware 1.23+ adds Undo/Redo and 100%-wet recording; Reverse, Half-Speed, Undo, Redo are reachable via MIDI or an external MultiSwitch. Looper Exit can be PLAY (keep looping in background) or STOP.
- **Spillover / trails** — the Persist PARAM and GLOBALS → SPLOVR let wet repeats spill across preset changes. **Important quirk:** the buffer architecture requires the current preset to be active **at least 5 seconds** before spillover works — fast preset stomps will cut the tail. Persist=ON also forces analog **buffered** bypass.
- **Stereo** — true stereo in/out. Pattern and Dual (parallel) spread taps across L/R; unplug the R output and the stereo field sums to mono automatically.
- **MIDI** — full implementation: every knob and PARAM has a CC, 200 presets via Program Change across two MIDI banks (Bank 0 = 00A–63B, Bank 1 = 64A–99B), MIDI clock sync, MIDI THRU/MERGE, looper control via notes or CCs, and preset dump/backup.
- **Feedback loop** — a rear switch can insert an external pedal into the delay feedback path (otherwise set to stereo).
- **Bypass** — globally selectable True Bypass (relay) or analog Buffered Bypass; with trails you're on buffered.

## 5. Bench Placement — Why It's Off the Board (and When It Subs In)

**The honest case for the bench is strong.** The End Board already runs two capable time engines: **CB Big Time** (Automatone stereo delay) as the primary delay color, and the **Eventide H90** providing algorithmic delay *and* reverb in one stereo box with deep MIDI. Between them, the live needs are met — and notably the TimeLine's *Strymon siblings* are benched for the same logic (BigSky because the H90 covers reverb, Iridium because the VG-800 covers amp/cab modeling). The board's philosophy is clearly **one strong instance per job, not redundant coverage**, and the TimeLine's twelve machines are mostly duplicated in spirit by what's already deployed:

- Tape/analog delay grime → dTape/dBucket overlap with Big Time's character and the Generation Loss + JHS 424 + PORTA424 tape stages already printing the signal.
- Shimmer/pitch delay → Ice overlaps H90 pitch+delay algorithms.
- Ambient/granular smear → covered by Microcosm, Dark Star V3, QI Etherealizer, Chroma Console.
- Looper → MOOD MkII and Blooper already own the looping role on Board 3.

So the TimeLine is genuinely redundant in the *current* configuration. That's the bench rationale, and it's correct.

**When it WOULD sub in — three real scenarios:**

1. **Failover.** The H90 is the single most complex, most relied-upon box in the rig (delay + reverb + pitch). If it dies on a session or a gig, the TimeLine is the natural drop-in for the delay half — it covers far more delay ground than Big Time alone, and it can fake reverb-adjacent space via Swell, Pattern 16, and Ice while BigSky (the dedicated reverb sub) handles the rest. The bench note for BigSky already encodes this "sub-in if H90 down" thinking; the TimeLine is the matching delay failover.
2. **Dedicated looper.** If a piece needs a *second, independent* 30s looper running pre- or post-delay alongside the MOOD/Blooper — e.g., layering a banjo drone loop under a live take — the TimeLine's looper is a clean, MIDI-controllable second machine with Reverse and Half-Speed.
3. **Second delay color in the studio.** When tracking, the bench-is-a-feature constraint disappears. The TimeLine can be patched in for a *specific* machine the board doesn't have — Lo-Fi destruction, Trem-synced delay, Filter-sweep delay, or a dual-ratio Edge pattern — without retasking Big Time or the H90 mid-session.

Verdict preview: the bench decision is **right for the live board** and **wrong for the studio rack** — this pedal earns its keep off-board, in failover and tracking roles, not in the live signal chain.

## 6. Source-Specific Notes (banjo, baritone, modeled VG-800, bass)

- **Banjo (Gold Tone EBM-5 → GK-5 → VG-800).** Bright, transient, low-mass signal. The per-machine **High Pass** PARAM (off → 900Hz) is the relevant control here — set it 100–200Hz on dTape or Digital to stop banjo repeats from booming or piling up as ice-pick stacks. **Swell** is the standout for banjo-as-lead: a Rise Time matched to the delay time turns plucked banjo into bowed-sounding pads. **dTape** with Wow & Flutter up smears the banjo's fast decay into something more sustained.
- **Baritone Jazzmaster.** Lower fundamentals want the High Pass to clean up low-string mud; dBucket Single's natural bandwidth roll-off is flattering here, and Dual (parallel) gives baritone riffs rhythmic motion across L/R.
- **Modeled VG-800.** The TimeLine sees the VG-800's summed line-level output after COSM modeling — there's no per-string separation left to exploit, and the EHX Effects Interface on the bench exists precisely to match VG-800 line level to pedal instrument level if the TimeLine is patched in. The 1 MΩ input and +8dBu max input handle the hotter modeled signal cleanly. Synth/pad COSM patches into Ice or Lo-Fi are where the drone aesthetic pays off.
- **Bass (Jazz Bass).** dBucket and the High Pass make the TimeLine bass-friendly — keep MIX low, use dBucket Single for warm analog repeats that don't fight the low end, and the analog dry path means zero latency on the fundamental.

## 7. Famous Users (honest)

The TimeLine has real, deep history — it became a near-default flagship delay across worship, ambient, and post-rock scenes after 2011. Its most-cited association is **U2's The Edge–style dotted-eighth delay**, which the **Dual** machine nails directly; Strymon even publishes [common Dual-delay ratio settings](https://www.strymon.net/faq/timeline-dual-delay-common-ratio-settings/) and the community has documented "Streets"/"Where the Streets Have No Name" patches extensively ([U2 Guitar Tutorial Forums](https://forum.u2guitartutorials.com/archive/index.php/t-2579.html), [theFretBoard discussion](https://www.thefretboard.co.uk/discussion/93520/strymon-delay-most-like-u2)). It's a documented staple on countless touring boards (John Mayer, ambient/worship players, post-rock acts) and won [Premier Guitar's Premier Gear award at 5/5](https://www.strymon.net/timeline-receives-the-premier-gear-award/). Unlike the Hizumitas (one artist's signature), the TimeLine's fame is *ubiquity* — it's the delay that ended up on everyone's board, which is part of why a player chasing a distinctive degraded aesthetic might deliberately bench it in favor of the more idiosyncratic Big Time + Chase Bliss tape stages.

## 8. Live / Power / I/O

- **Power:** 9VDC center-negative, **300 mA minimum** required — high draw; never exceed 9V. This is a notable power-budget line item and one practical reason it's not casually stacked onto an already-crowded board.
- **I/O:** Stereo in (LEFT = mono), stereo out (LEFT = mono); RIGHT IN/OUT double as feedback-loop return/send when the rear switch is set to FEEDBACK LOOP.
- **EXP:** TRS expression pedal (any knob, or multiple knobs simultaneously via EP SET), or external TAP (MiniSwitch), or MultiSwitch for bank/preset/looper.
- **MIDI:** 5-pin in/out, full CC + PC + clock + dump.
- **Presets:** 200, recallable by encoder, footswitch, or MIDI; powers up in MIDI Bank 0.
- **Bypass/spillover:** global True or Buffered Bypass; trails/spillover require ~5s of preset-active time before they engage.
- **Build:** anodized aluminum, 5" deep × 6.75" wide × 1.87" tall.

## 9. Pairing Recommendations (by name)

- **vs CB Big Time** — these are complementary, not redundant, *if* you board both: run **Big Time first** as the characterful primary, TimeLine second for a *different* machine (Lo-Fi, Trem, Filter sweep) the Big Time can't do. In the live rig, the Big Time wins the single slot on personality and footprint; the TimeLine is the deeper toolbox you reach for in the studio.
- **vs Eventide H90** — the H90 is the direct functional overlap and the reason the TimeLine is benched. If both ran, dedicate the TimeLine to *delay-only destruction* (dTape/dBucket/Lo-Fi) and let the H90 own delay+reverb combos and pitch. As failover, the TimeLine replaces the H90's delay half.
- **If boarded** — End Board, after Big Time, before the H90 / tape-print stages (Generation Loss, PORTA424, JHS 424), so its repeats get printed to tape — exactly where the current End Board chain wants time effects to sit.
- **As a dedicated looper** — patch post-Microcosm/Dark Star so it loops already-textured signal; sync via MIDI clock to the rest of the MIDI'd board (Generation Loss, MOOD, Chroma Console, Microcosm).
- **Into ambient/granular** — TimeLine Swell or Ice → Dark Star V3 / QI Etherealizer makes oceanic drones; the analog dry path keeps the source intact underneath.

## 10. Reviews & Demos

- [Premier Guitar — Strymon TimeLine review (Premier Gear, 5/5)](https://www.premierguitar.com/gear/strymon-timeline-pedal-review) — best written overview; covers dTape/dBucket pedigree.
- [MusicRadar — Strymon TimeLine review](https://www.musicradar.com/reviews/guitars/strymon-timeline-523567) — strong on the dTape "knackered Echoplex" controls and dBucket BBD options.
- [MusicRadar — Hands-on with the Strymon TimeLine](https://www.musicradar.com/guitartechniques/hands-on-with-the-strymon-timeline-pedal-552264) — practical walkthrough.
- [Delicious Audio — Strymon TimeLine review](https://delicious-audio.com/pedal-review-strymon-timeline/) — pedal-nerd perspective.
- [Strymon — official TimeLine product page](https://www.strymon.net/product/timeline/) — machine list and feature spec.
- [Strymon — Dual Delay common ratio settings (U2/Edge)](https://www.strymon.net/faq/timeline-dual-delay-common-ratio-settings/) — the dotted-eighth recipe.
- [Strymon TimeLine U2 delay demo (YouTube, stilwel)](https://www.youtube.com/watch?v=Q1q0DcSWsW0) — Dual machine for Edge tones.

## 11. Mods / Quirks / Firmware

- **Firmware is mature and frozen.** v1.88 (April 2020) is the last release; there is no V2 / no expanded machine set coming. Update via Strymon's updater ([release notes](https://www.strymon.net/faq/timeline-firmware-revision-release-notes/)). Confirm the owned unit is on 1.88 — earlier units lack per-preset MIDI clock, MIDI THRU/MERGE, and the looper improvements.
- **5-second spillover rule** — the single most-tripped-over behavior: trails won't spill if you change presets faster than ~5s after engaging one.
- **Persist forces buffered bypass** — turning trails on changes the bypass mode automatically; if you want true bypass, you give up spillover.
- **GRIT volume shift** — wet level changes with GRIT and input strength; compensate with MIX. dBucket/dTape re-map GRIT to Bias/Bucket-Loss, which behave differently.
- **dBucket + looper + longest delay** — the exact DSP-bandwidth case v1.88 patched; pre-1.88 firmware can glitch there.
- **No internal mods** — this is a closed digital platform; all "modding" is firmware + deep PARAMS. No 18V trick, no clipping swaps.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Power | 9VDC center-negative, 2.1mm barrel |
| Current draw | **300 mA minimum** (never exceed 9V) |
| Delay machines | 12 (dTape, dBucket, Digital, Dual, Pattern, Reverse, Ice, Duck, Swell, Trem, Filter, Lo-Fi) |
| Presets | 200 (100 banks × A/B) |
| Looper | 30 seconds, pre/post delay |
| Input impedance | 1 MΩ |
| Output impedance | 100 Ω |
| Signal-to-noise | 115 dB typical |
| A/D & D/A | 24-bit / 96kHz |
| Frequency response | 20Hz–20kHz |
| Max input level | +8dBu |
| Signal path | Analog dry path (zero-latency dry) + SHARC DSP wet |
| I/O | Stereo in / stereo out (or feedback-loop send/return) |
| MIDI | Full in/out (CC, PC, clock, dump, looper) |
| Expression | TRS EXP (pedal / tap / MultiSwitch) |
| Bypass | True (relay) or Analog Buffered (selectable; trails on buffered) |
| Firmware (current) | Rev. 1.88 (April 2020) |
| Dimensions | 5" deep × 6.75" wide × 1.87" tall |
| Warranty | 1 year (non-transferable) |

Sources: [Rev H user manual](manuals/TimeLine_UserManual_RevH.pdf), [Strymon product page](https://www.strymon.net/product/timeline/), [firmware release notes](https://www.strymon.net/faq/timeline-firmware-revision-release-notes/).

## 13. Starting-Point Settings

Knob/PARAM starting points for this rig. Clock-face positions looking down at the pedal.

**(a) Degraded tape wall** — shoegaze/doom smear (dTape)
- Machine: dTape · TIME: dotted-eighth or to taste · REPEATS: 2–3 o'clock · MIX: 12–1
- Tape Age (FILTER): 1–2 o'clock · Tape Bias (GRIT): 9–10 · Wow & Flutter (DEPTH): 2 · Tape Crinkle (SPEED): 1
- Low End Contour: slightly toward bass · High Pass: 80–120Hz for baritone. Let chords ring.

**(b) Broken transmission** — Lo-Fi destruction for banjo/synth
- Machine: Lo-Fi · TIME: 400–600ms · REPEATS: 2 · MIX: 12
- Sample Rate: 5–8kHz · Bit Depth: 8-bit · Vinyl: static, mid · Filter Shape: 6 (antique telephone) or 7 (cell phone)
- Pair after VG-800 pad patches → Dark Star for drone.

**(c) Shimmer drone** — Ice for banjo-as-lead pads
- Machine: Ice · Interval: +Octave (or +Octave & 5th) · Slice: MEDIUM · BLEND: toward Dry side
- REPEATS: 3 o'clock · MIX: 11–12 · DEPTH: 9–10 for movement · High Pass: 160Hz
- Swell into notes with the guitar volume; the Ice signal "floats in" as repeats regenerate.

**(d) Edge / failover delay** — clean dual delay if subbing for the H90 (Dual)
- Machine: Dual · CONFIG: parallel · TIME 2: 2/3 or 3/4 (dotted-eighth + quarter feel) · REPEATS: 11–12
- MIX: 11 · Filter: noon · Grit: min · Tap Division: dotted-eighth. Tap in the song tempo or sync MIDI clock.

## 14. Versus Alternatives — and the Bench Verdict

- **vs Chase Bliss Big Time (on-board primary delay)** — Big Time wins the live slot on *character per square inch*: it's an Automatone with motorized faders, a specific voice, and a smaller footprint, and it's already integrated into the End Board's MIDI'd workflow. The TimeLine wins on *breadth* — twelve machines vs one circuit — which is exactly why it belongs in the studio rack, not competing for Big Time's single live slot.
- **vs Eventide H90 (on-board algorithmic delay+reverb)** — the H90 is the direct reason for the bench. It does delay *and* reverb *and* pitch in one stereo box with deeper, more modern algorithms and a more flexible routing engine. The TimeLine can't combine reverb into the same instance the way the H90 does. Live, the H90 is the correct single box; the TimeLine's only live argument is **failover** if the H90 goes down.
- **vs BigSky / Iridium (benched siblings)** — same family logic: each is benched because a single on-board box already owns its job (H90 for reverb, VG-800 for modeling). The TimeLine is the *delay* member of that benched-Strymon trio.
- **vs Boss DD-series / Empress Echosystem / Meris LVX** — the TimeLine is the workstation standard the others are measured against; the LVX is its modern successor in flexibility. None of that matters here, because the question isn't "best delay" — it's "does this rig need a 13th time effect," and the answer for the *live* board is no.

**Verdict on the bench decision:** Correct — for the live board. The rig already runs Big Time (primary delay character) and the H90 (algorithmic delay + reverb) on Board 3, with tape-grime and looping covered by Generation Loss, JHS 424, PORTA424, MOOD MkII, and Blooper. Adding a 300 mA, twelve-machine delay workstation into that would be redundant coverage and a real power/space tax for no new *live* capability. The TimeLine's value in *this* rig is precisely as a bench pedal: the **H90 delay-failover unit**, a **second independent looper**, and a **studio-only source of machines the board lacks** (Lo-Fi, Trem, Filter-sweep, Ice). Keep it benched, keep it on 1.88, and reach for it in the studio and in emergencies — not on the live board.

## Sources

- [Strymon — TimeLine product page](https://www.strymon.net/product/timeline/)
- [Strymon — TimeLine firmware revision release notes (v1.88)](https://www.strymon.net/faq/timeline-firmware-revision-release-notes/)
- [Strymon — TimeLine support](https://www.strymon.net/support/timeline/)
- [Strymon — Dual Delay common ratio settings (U2/Edge)](https://www.strymon.net/faq/timeline-dual-delay-common-ratio-settings/)
- [Strymon — TimeLine receives the Premier Gear award](https://www.strymon.net/timeline-receives-the-premier-gear-award/)
- [Premier Guitar — Strymon TimeLine review](https://www.premierguitar.com/gear/strymon-timeline-pedal-review)
- [MusicRadar — Strymon TimeLine review](https://www.musicradar.com/reviews/guitars/strymon-timeline-523567)
- [MusicRadar — Hands-on with the Strymon TimeLine pedal](https://www.musicradar.com/guitartechniques/hands-on-with-the-strymon-timeline-pedal-552264)
- [Delicious Audio — Strymon TimeLine review](https://delicious-audio.com/pedal-review-strymon-timeline/)
- [U2 Guitar Tutorial Forums — Strymon TimeLine and U2](https://forum.u2guitartutorials.com/archive/index.php/t-2579.html)
- [theFretBoard — Strymon delay most like U2](https://www.thefretboard.co.uk/discussion/93520/strymon-delay-most-like-u2)
- [Strymon TimeLine U2 delay demo (YouTube)](https://www.youtube.com/watch?v=Q1q0DcSWsW0)
- [Equipboard — Strymon TimeLine](https://equipboard.com/items/strymon-timeline-delay-pedal)
- TimeLine User Manual Rev H (09.17.2021) — local: `manuals/TimeLine_UserManual_RevH.pdf`
