# Strymon Big Sky — Deep Research

A working dossier for a pedal that does not currently sit on a board. In this rig the Big Sky lives **on the bench**, and it lives there for one clean reason: the [Eventide H90](https://www.eventideaudio.com/pedals/h90/) on Board 3 already runs all the reverb, with the OBNE Dark Star V3 and Walrus QI Etherealizer covering pad/ambient duty on Board 2. The rig sheet is blunt about it — *"H90 handles reverb. Sub-in if H90 down."* So this document is less about whether the Big Sky is good (it is, famously so) and more about exactly what it loses to the H90, what it keeps, and how to wheel it onto the board fast when the H90 falls over mid-set. It is the **designated reverb failover**, and a designated failover is only worth anything if the failover patches are already built. Most of this is about that.

## 1. Lineage: blueSky → Big Sky → Big Sky MX

Strymon's reverb story runs in three acts. The **blueSky** (2010) was the single-machine spring/room/hall reverb that established the house sound — pristine, deep, slightly hi-fi. The **Big Sky** (released late 2013) was the flagship escalation: 12 reverb "machines," 300 presets, full MIDI, an analog dry path, stereo I/O, and the SHARC DSP horsepower to run reverbs nobody else was attempting on a pedal. It won [SonicState's Best Effect Pedal of 2013](https://www.strymon.net/bigsky-reviews/) and effectively defined the "ambient reverb workstation" category for a decade.

The third act matters for placing *this* unit. In 2023 Strymon shipped the **[Big Sky MX](https://www.strymon.net/product/bigsky-mx/)** — a "tri-core 800MHz 32-bit floating-point ARM" rebuild with **dual reverb engines** (two reverbs in series/parallel/split), seven new algorithms on top of the originals, user-loadable impulse responses, and an OLED screen replacing the old LED display ([guitar.com review](https://guitar.com/reviews/effects-pedal/the-big-review-strymon-bigsky-mx/), [Premier Guitar](https://www.premierguitar.com/gear/reviews/strymon-bigsky-mx)). Notably, the MX **dropped the Reflections machine** and the standalone Cab Filter, trading them for IR loading and the dual-engine routing.

The unit in this collection is the **original Big Sky**, not the MX — confirmed by the bundled manual being **Rev D (05.24.19)**, which documents 12 machines including Reflections and the rear-panel Cab Filter switch, neither of which exist on the MX. The original is a single-engine, LED-display, SHARC-based unit. That generational fact is relevant to the failover discussion: the original Big Sky runs **one reverb at a time**, where the H90 it's replacing can run two algorithms in parallel. (Flag: I did not physically inspect the firmware screen; the generation call is from the manual revision and feature set.)

## 2. Controls and the 12 Machines

Front panel, per the [manual](manuals/BigSky_UserManual_RevD.pdf):

- **VALUE** — fine Decay adjustment; scrolls presets when a bank/name is displayed; **push** for the PARAMETER menu, **hold** for GLOBAL.
- **DECAY** — reverb tail length (RT60). Range is machine-dependent (see below).
- **PRE-DELAY** — 0 to 1.5 s gap between dry and reverb onset. On **Nonlinear and Magneto this knob becomes Feedback** instead.
- **MIX** — analog dry ↔ wet balance; 100% dry at min, 100% wet at max, 50/50 at the 3:00 position.
- **TONE** — high-frequency content of the tail. Noon is "balanced"; lower = darker/warmer, higher = bright and crisp.
- **PARAM 1 & 2** — assignable to any menu parameter of the active machine (hold VALUE, turn a PARAM knob to bind).
- **MOD** — modulation depth; subtle at low settings (delay-line movement), overt at high (modulates the tank input).
- **A / B / C footswitches** — engage/bypass presets in the current bank; **hold for Infinite Sustain or Freeze** (selectable per preset); A+B steps bank down, B+C steps bank up.

The 12 machines (the brief lists "Chamber" — the actual 12th machine in this generation is **Reflections**; there is no Chamber machine):

| Machine | One-line character | Key parameters | Decay range |
|---|---|---|---|
| **Room** | Studio-to-nightclub spaces | Low End, Size (Studio/Club), Diffusion | 200mS–20S |
| **Hall** | Concert/Arena, diffuse, warm | Low End, Mid, Size (Concert/Arena) | 500mS–20S |
| **Plate** | Fast-building, no room cues | Low End, Size (Small/Large) | 500mS–20S |
| **Spring** | Surf/spaghetti-western tank | Low End, Dwell (Clean/Combo/Tube/Overdrive), # Springs (1/2/3) | 800mS–10S |
| **Swell** | Auto volume-swell into verb | Low End, Rise Time, Mode (Wet/Dry) | 500mS–20S |
| **Bloom** | '90s slow-blooming ambient | Low End, Length, Feedback | 500mS–20S |
| **Cloud** | Late-'70s huge ambient wash | Low End, Diffusion | 1.00S–50S |
| **Chorale** | Vocal choir pad | Vowel, Resonance (Mild/Med/High) | 500mS–20S |
| **Shimmer** | Pitch-shifted octave/interval verb | Shift 1, Shift 2, Amount, Mode (Input/Regen/In+Reg), Low End | 500mS–20S |
| **Magneto** | Multi-head tape echo verb | Low End, Diffusion, Heads (3/4/6), Spacing (Even/Uneven); knobs become Delay Time + Feedback | 200mS–1.5mS* |
| **Nonlinear** | Gated/reverse/ramp special FX | Low End, Shape, Diffusion, Late Decay/Level, Mod Speed; knobs become Time + Feedback | 50mS–2S |
| **Reflections** | 250-tap psychoacoustic small room | Low End, Loc Y, Loc X, Shape (Square/Rect/Oblong) | 133mS–400mS |

*Magneto's displayed range in the manual reads "200mS — 1.50mS" which is a manual typo for the delay-time scaling; treat it as the multi-head delay range.

## 3. Sonic Character / Standout Machines

The Big Sky's signature is **clean, dimensional, slightly hi-fi space** — the opposite of a dark spring box. The four machines worth caring about for this rig's drone/doom/shoegaze aesthetic:

- **Shimmer** — the famous one. Two tunable pitch-shifted voices (anything from an octave down to two octaves up) fed back into the tank. **Mode** is the deep control: *Input* shifts before the tank (cleaner, single-rise), *Regen* shifts the tank's own output (cascading), *In+Reg* does both for the full majestic build. With +1 Oct and Oct+5th and high Amount you get the textbook ascending-cathedral wall. Manual's own trick: −10 cents / +10 cents in Input mode with Mod off yields a beautifully detuned reverb.
- **Bloom** — a slow-rising "bloom generator" feeding a reverb tank, with a unique **Feedback** parameter that lets the bloom portion run far longer than the displayed tail. High Length + high Feedback + high Mod = "a gorgeous spectrum of sweeping resonant harmonics" (manual). This is the right machine for a sustained chord that grows *after* you stop playing.
- **Cloud** — late-'70s-style enormous ambient wash, the longest decay on the pedal (**up to 50 seconds**). At low Diffusion the attack is grainy/mesmerizing on transients; cranked it smooths into a pad. Manual sums it up: "can take any modest guitar or synth sound and turn it into a gorgeous ensemble." Made for banjo and VG-800 pads.
- **Magneto** — multi-head tape-echo reverb. PRE-DELAY becomes Feedback, DECAY becomes the last head's delay time; **3/4/6 heads** with Even/Uneven spacing, and the Mod knob acts as a wow-and-flutter generator. This is the most "broken/degraded" of the machines and the closest in spirit to the rig's tape-print philosophy — though the Board 3 tape chain (PORTA424, JHS 424) covers that ground differently.

## 4. Behavioral Notes

- **Spillover/trails.** Two flavors. Per-preset **Persist** (PRSIST) keeps a preset's trail alive when *that* preset is bypassed — and forces analog buffered bypass when on. Global **Spillover** (SPLOVR) lets a preset's wet tail spill into the *next* selected preset. Important caveat from the manual: *the current preset must be active for at least 5 seconds before spillover works* (buffer architecture). Plan patch changes around that.
- **Freeze vs. Infinite.** Hold a footswitch to trigger, set per-preset via the HOLD parameter: **INFNTE** (Infinite Sustain — each new note adds to the held wash) or **FREEZE** (Reverb Freeze — holds the sustain, lets you play new notes over the top without adding to it). For drone work, Freeze is the keeper.
- **Stereo.** True stereo in/out. LEFT in/out for mono. The dry path is **analog, never converted to digital** (zero-latency dry).
- **MIDI.** Deep. Full CC map for every knob and machine parameter, program change across 300 presets (grouped into 3 MIDI banks of 128), MIDI clock (controls Pre-Delay on most machines, Decay on Magneto/Nonlinear), MIDI Thru/Merge, and preset dump. This is what makes it a viable H90 failover under MIDI control (Section 5).
- **Cab Filter.** Rear-panel switch adds a speaker-response curve for running direct to PA/interface/headphones — relevant if it's ever last in the chain rather than into an amp.

## 5. Bench Placement — Why It's Benched, and the Failover

**Why it's off the board.** The H90 on Board 3 is the rig's reverb brain. It runs **two algorithms simultaneously** (parallel or series), drawing from **14 reverb-type algorithms** — Blackhole, DualVerb, DynaVerb, Hall, MangledVerb, ModEchoVerb, Plate, Reverse, Room, SP2016 Reverb, Spring, Shimmer, TremoloVerb, Wormhole ([H90 algorithm guide](https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/algorithms/index.html)). Several of those (Blackhole, Shimmer, MangledVerb, Wormhole) directly overlap the Big Sky's signature territory, and the H90 can pair a reverb with a *delay or pitch* algorithm in the same box — which the Big Sky cannot. On top of that, Board 2's **Dark Star V3** delivers smeared pad reverb and the **QI Etherealizer** delivers ambient texture. So the reverb job is triple-covered. A single-engine Big Sky would be redundant. The bench is the correct call.

**Where it genuinely beats the H90.** Two things. (1) **One knob per function.** The Big Sky's front panel is Decay/Pre-Delay/Mix/Tone/Mod with two assignable PARAMs — no menu diving, no scene management. Under stage pressure that immediacy is exactly what you want from an emergency unit. (2) **The analog dry path** and the specific voicing of Cloud/Bloom/Shimmer, which some players (and reviewers) still prefer to Eventide's "thicker" reverbs ([forum sentiment](https://sevenstring.org/threads/eventide-h9-vs-strymon-bigsky.296013/)). It is not a downgrade in *quality* — it's a downgrade in *count and routing*.

**The sub-in scenario.** If the H90 dies mid-set, the Big Sky is the drop-in. To make that real:

1. **Physical:** patch it stereo into the H90's slot on Board 3 (stereo L/R in and out). It draws 300 mA — make sure the failover power slot can supply it (the H90 needs more; a freed H90 slot will easily cover the Big Sky). Cab Filter **OFF** (it's going into the tape chain / amp, not direct).
2. **MIDI:** put it on the same MIDI channel the rig was sending H90 program changes on, and **pre-build a failover preset bank** whose program-change numbers line up with the H90 PCs your controller already fires. The Big Sky responds to standard PC across its 300 presets; map a handful of your most-used reverb scenes (see Section 13) to those incoming numbers so the existing footswitch/controller cues still land.
3. **Spillover ON** globally so trails carry across preset changes — but remember the **5-second** rule before spillover engages.
4. Accept the one real loss: you get **one reverb at a time**, so any patch that relied on the H90 running *two* reverbs (or reverb + delay) collapses to a single machine. Pick the dominant one.

A failover that isn't pre-mapped is just a paperweight in a panic. The work is building the bank *now*, not on stage.

## 6. Source-Specific Notes

- **EBM-5 banjo (GK-5 → VG-800).** Bright, transient, low-mass signal. The Big Sky's **Tone** knob below noon plus **Cloud** or **Bloom** turns banjo plucks into sustained ambient mass — Cloud's low-Diffusion grain actually flatters banjo transients rather than smearing them away. For the "banjo-as-lead" idea, **Swell (Dry mode)** with a short Rise time gives an auto-volume-swell that hides the banjo's percussive attack entirely.
- **Baritone Jazzmaster.** Home turf for big reverb. Watch **Low End** on Hall/Cloud — baritone fundamentals plus a cranked Low End parameter get muddy fast; pull Low End back and lean on Tone. Magneto with 6 heads is excellent on baritone single-note lines.
- **Modeled VG-800.** Because the VG-800 outputs a modeled, often-already-processed signal, the Big Sky is just adding the room. Cloud and Bloom take a VG-800 pad and make it enormous (manual literally calls out "modest guitar or synth sound → gorgeous ensemble"). If running the VG-800's own modeling, keep Cab Filter OFF.
- **Bass (Jazz Bass).** Plate (Small) or Room with low Mix and Low End pulled down keeps the bottom defined. Avoid long Cloud/Hall tails on bass unless you want wash, not note.

## 7. Famous Users

Honest version: the Big Sky's reputation is **ubiquity, not a single signature artist**. From 2013 onward it became the default ambient/post-rock/shoegaze reverb workstation, and it's documented across [Strymon's own ambient-artist features](https://www.strymon.net/artists-feature-ambient-music/) and countless touring boards — but it's the kind of pedal that's *everywhere* rather than *the* pedal of one named player. Strymon's published pedalboard features include artists like **Madi Diaz** and **Jean-Philip Grobler (St. Lucia)** running Strymon reverb. I could **not** verify specific high-profile names (John Mayer, The Edge, Mogwai, etc.) using *this* model specifically — Mayer's documented Strymon reverb is the NightSky, not the Big Sky ([Guitar World](https://www.guitarworld.com/news/john-mayer-solo-tour-pedalboards-2023)). **Flag: famous-user claims for the Big Sky specifically are weakly sourced; its real fame is category-defining ubiquity, which is well documented.**

## 8. Live / Power / I/O

- **Power:** 9VDC center-negative, **300 mA minimum** (verified — [manual spec page](manuals/BigSky_UserManual_RevD.pdf), [Sweetwater](https://www.sweetwater.com/sweetcare/articles/getting-started-with-the-strymon-bigsky/)). Never exceed 9V. This is a high-draw digital pedal — it needs a dedicated 300 mA+ isolated slot, not a daisy chain.
- **I/O:** Stereo in / stereo out (LEFT for mono), EXP jack, MIDI In/Out (5-pin DIN), Cab Filter switch.
- **Bypass:** Selectable **True Bypass** (relay) or **Analog Buffered Bypass** (with trails). Persist forces buffered bypass when on.
- **EXP:** Expression pedal (multi-knob simultaneous control via EP SET per preset), or a Strymon MiniSwitch/MultiSwitch for tap/bank/preset (set via EXP MD global).
- **Presets:** 300 (100 banks × A/B/C), all rewritable, MIDI-recallable.
- **Dimensions:** 6.75" W × 5" D × 1.87" H — a large-format box. On the bench it costs real board space, another reason it's not boarded full-time.

## 9. Pairing Recommendations (by name)

- **vs. H90 (Board 3):** the unit it replaces. Not a co-resident; a substitute. Build the failover bank to mirror your H90 reverb scenes (Section 5/13).
- **vs. Dark Star V3 (Board 2):** the Dark Star is a *smeared, lo-fi, drone* reverb — voiced toward decay and grit. The Big Sky is *clean and dimensional*. They're complementary, not redundant; if you ever boarded the Big Sky alongside the Dark Star, run the Big Sky for the pristine pitched/ambient layer (Shimmer, Cloud) and let the Dark Star do the dirty pad.
- **vs. QI Etherealizer (Board 2):** the QI is an ambient/granular texture box. Big Sky Cloud + QI stacked would be excessive in normal operation — fine for a one-off studio wall, not a live patch.
- **If ever boarded:** it belongs at the **end of the time section on Board 3**, where the H90 currently sits — after delays (Big Time/Gen Loss), before the tape print (PORTA424/JHS 424), stereo. Cloud/Bloom want to be the *last* spatial stage so the delays feed into them.
- **Into the tape chain:** Cab Filter OFF; let the PORTA424/424 do the coloration. The Big Sky's clean dry path is exactly what the tape stage wants as a source.

## 10. Reviews & Demos

- [Premier Guitar — Strymon Big Sky review](https://www.premierguitar.com/gear/reviews/strymon-big-sky-review) — the standard written review; "pristine, dimensional soundscaping power."
- [Sound on Sound — Strymon Big Sky](https://www.soundonsound.com/reviews/strymon-big-sky) — best on the analog-dry-path-with-programmable-mix as a "world first," and the no-menu-diving UI.
- [MusicRadar — Strymon BigSky](https://www.musicradar.com/reviews/guitars/strymon-bigsky-591554) — solid overview.
- [Guitar Chalk — BigSky reverb pedal review (bought & tested)](https://guitar-chalk.medium.com/strymon-bigsky-reverb-pedal-review-bought-tested-27303f7acfe7) — long-term owner perspective.
- [Guitar World — Big Sky review](https://www.guitarworld.com/magazine/review-strymon-big-sky-reverb-pedal).
- [Strymon's own BigSky video playlist](https://www.youtube.com/playlist?list=PLvwSyyxvV5CQHlJfJKqOiLUW3SJ89dqwL) — per-machine demos straight from the source.
- For the upgrade question: [guitar.com BigSky MX big review](https://guitar.com/reviews/effects-pedal/the-big-review-strymon-bigsky-mx/) and [DeathCloud BigSky MX vs BigSky](https://deathcloud.com/blogs/info/strymon-bigsky-mx-vs-bigsky-which-reverb-should-you-get) — relevant only if you ever consider replacing this unit.

## 11. Mods, Quirks, Firmware

- **Firmware.** Last original-Big-Sky firmware is **v1.49 (March 2019)** ([Strymon release notes](https://www.strymon.net/faq/bigsky-firmware-download-revision-release-notes/)). Updates were done over MIDI via Strymon's **Nixie** app (Win/macOS) — back up presets, detect device, flash firmware. The platform is mature/stable; no further development on the original (Strymon's reverb R&D moved to the MX). Make sure this unit is on 1.49 before trusting it as a failover.
- **Reflections** *may* have been a firmware addition rather than an original-launch machine — **unverified**: Strymon's published release notes (v1.15+, Feb 2014 on) don't document it being added, and it couldn't be confirmed either way, so it could equally be an original machine. Either way it's the one machine the MX later dropped, so on the original it's a small point of distinction.
- **Quirks:** the 5-second spillover rule (Section 4) bites people who change presets too fast. Magneto/Nonlinear remap PRE-DELAY→Feedback and DECAY→Time, which surprises anyone reaching for those knobs by muscle memory. The factory ships with presets 00A–33A duplicated into the next two MIDI banks — re-init to defaults via power-up holding A+C if needed.
- No hardware mods of note; it's a sealed digital workstation, not a moddable analog circuit.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Generation | Original Big Sky (not MX); manual Rev D, 05.24.19 |
| Reverb machines | 12 (Room, Hall, Plate, Spring, Swell, Bloom, Cloud, Chorale, Shimmer, Magneto, Nonlinear, Reflections) |
| Presets | 300 (100 banks × A/B/C), all rewritable |
| Simultaneous engines | 1 (vs. H90's 2) |
| Power | 9VDC center-negative, **300 mA min** (do not exceed 9V) |
| Input impedance | 1 MΩ |
| Output impedance | 100 Ω |
| Signal to noise | 115 dB typical |
| A/D & D/A | 24-bit 96 kHz |
| Frequency response | 20 Hz – 20 kHz |
| Max input level | +8 dBu |
| Dry path | Analog, zero-latency (never digitized) |
| I/O | Stereo in / stereo out, EXP, MIDI In/Out, Cab Filter switch |
| Bypass | True Bypass (relay) or Analog Buffered Bypass (trails) |
| Dimensions | 6.75" W × 5" D × 1.87" H |
| Warranty | 1 year (Strymon, non-transferable) |
| Last firmware | v1.49 (March 2019), via Nixie over MIDI |

Source: [manual spec page](manuals/BigSky_UserManual_RevD.pdf), [Strymon BigSky product page](https://www.strymon.net/product/bigsky/).

## 13. Starting-Point Settings

Knob positions clock-face, looking down at the pedal.

**(a) H90-Failover "default verb"** — the everyday reverb the H90 normally provides
- Machine: **Hall (Concert)** · Decay: ~3.5s · Pre-Delay: 9:00 · Mix: 10:00 · Tone: 12 · Mod: 11 · Low End: centered, Mid: flat
- Save as preset 00A. Map to the program-change number your controller fires for the H90's main reverb. This is the "nothing's broken, you'd barely notice" patch.

**(b) Drone wall** — sustained, oceanic, freeze-capable
- Machine: **Cloud** · Decay: 20s+ · Pre-Delay: 12 · Mix: 1:00 · Tone: 11 · Mod: 1:00 · Diffusion: high · HOLD = FREEZE
- Hold the footswitch to freeze a chord, play over the top. The drone/doom anchor patch.

**(c) Shimmer cathedral** — ascending pitched wall, shoegaze lead bed
- Machine: **Shimmer** · Shift 1: +1 Oct · Shift 2: +Oct & 5th · Amount: 2:00 · Mode: IN+REG · Decay: ~8s · Mix: 12 · Tone: 1:00 · Mod: 12
- For banjo-as-lead: pull Mix to 11:00 so the shimmer sits behind the line, not on top of it.

**(d) Broken tape verb** — degraded, rhythmic, for the print chain
- Machine: **Magneto** · Heads: 6 · Spacing: Uneven · Decay (delay time): ~300mS · Pre-Delay (feedback): 1:00 · Low End: 10:00 · Mod: 1:00 · Mix: 11:00
- The closest the Big Sky gets to the rig's tape aesthetic. Feed it into PORTA424/424 for compounding wear.

## 14. Versus Alternatives — Big Sky vs H90, and the Verdict

**Big Sky vs. H90 (the only comparison that matters here):**

- **Algorithm count/routing:** H90 wins decisively — 14 reverb algorithms *plus* the ability to run two effects at once (two reverbs, or reverb + delay/pitch). The original Big Sky runs **one machine at a time**.
- **Immediacy:** Big Sky wins — true one-knob-per-function, zero menu diving ([Sound on Sound](https://www.soundonsound.com/reviews/strymon-big-sky)). The H90 is deeper but slower to operate live.
- **Voicing:** a wash. Some prefer Strymon's clean/dimensional character and analog dry path; some prefer Eventide's thicker, more aggressive reverbs. Neither is "better" — they're different flavors at the same quality tier.
- **Footprint/power:** both large, both hungry; the Big Sky's 300 mA fits comfortably in a freed H90 slot.

**Other reverb workstations** (Meris MercuryX, Empress Reverb, GFI Specular Tempus) are all credible — but irrelevant to this rig, because the failover decision isn't "what's the best reverb pedal," it's "what backs up the H90 with the least friction." The Big Sky is *already owned*, MIDI-controllable, single-knob-fast, and stereo. That makes it the right failover regardless of how the broader market shakes out.

**Verdict on the bench/failover call: correct, and well-chosen.** Benching the Big Sky is right — a single-engine reverb is redundant when the H90 runs two algorithms and Board 2 adds pad/ambient reverb on top. But it's the *ideal* thing to bench *as the designated failover*: it's the only off-board pedal that can credibly stand in for the H90's reverb under MIDI control with stage-fast operation. The only real exposure is that it can't replicate H90 patches that run two reverbs at once — those degrade to a single machine. The one piece of homework that turns this from a theoretical backup into a real one: **build the failover preset bank now** (Section 13), aligned to the program-change numbers your controller already fires, and confirm the unit is on firmware v1.49. A backup you haven't pre-mapped is not a backup.

## Sources

- [Strymon — BigSky Multi Reverb product page](https://www.strymon.net/product/bigsky/)
- [Strymon — BigSky User Manual Rev D (bundled PDF)](manuals/BigSky_UserManual_RevD.pdf)
- [Strymon — BigSky Firmware Revision Release Notes (v1.49)](https://www.strymon.net/faq/bigsky-firmware-download-revision-release-notes/)
- [Strymon — BigSky MX Multi Reverb product page](https://www.strymon.net/product/bigsky-mx/)
- [Strymon — Artists Feature: Ambient Music](https://www.strymon.net/artists-feature-ambient-music/)
- [Strymon — BigSky reviews/awards roundup](https://www.strymon.net/bigsky-reviews/)
- [Sweetwater — Getting Started With the Strymon BigSky (300 mA, 300 presets)](https://www.sweetwater.com/sweetcare/articles/getting-started-with-the-strymon-bigsky/)
- [Eventide — H90 Harmonizer product page](https://www.eventideaudio.com/pedals/h90/)
- [Eventide — H90 Algorithm Guide (reverb list)](https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/algorithms/index.html)
- [Premier Guitar — Strymon Big Sky review](https://www.premierguitar.com/gear/reviews/strymon-big-sky-review)
- [Sound on Sound — Strymon Big Sky review](https://www.soundonsound.com/reviews/strymon-big-sky)
- [MusicRadar — Strymon BigSky review](https://www.musicradar.com/reviews/guitars/strymon-bigsky-591554)
- [Guitar World — Strymon Big Sky review](https://www.guitarworld.com/magazine/review-strymon-big-sky-reverb-pedal)
- [Guitar Chalk — Strymon BigSky review (bought & tested)](https://guitar-chalk.medium.com/strymon-bigsky-reverb-pedal-review-bought-tested-27303f7acfe7)
- [guitar.com — Strymon BigSky MX big review (generation comparison)](https://guitar.com/reviews/effects-pedal/the-big-review-strymon-bigsky-mx/)
- [Premier Guitar — Strymon BigSky MX review](https://www.premierguitar.com/gear/reviews/strymon-bigsky-mx)
- [DeathCloud — BigSky MX vs BigSky](https://deathcloud.com/blogs/info/strymon-bigsky-mx-vs-bigsky-which-reverb-should-you-get)
- [SevenString.org — Eventide vs Strymon BigSky voicing thread](https://sevenstring.org/threads/eventide-h9-vs-strymon-bigsky.296013/)
- [Guitar World — John Mayer 2023 pedalboards (NightSky, not BigSky)](https://www.guitarworld.com/news/john-mayer-solo-tour-pedalboards-2023)
- [Strymon — official BigSky video/demo playlist](https://www.youtube.com/playlist?list=PLvwSyyxvV5CQHlJfJKqOiLUW3SJ89dqwL)
