# Boss VG-800 — Deep Research

A working dossier for the source-and-brain of Board 1. The VG-800 sits dead first in this rig — fed by a Baritone Jazzmaster (GK-5) and a Gold Tone EBM-5 electric banjo (GK-5) — and everything modeled, alt-tuned, hex-divided, or synthesized downstream originates here before a single fuzz or tape pedal touches it. It is a relatively new, lightly-documented product (launched 2025), so a lot of this document is built directly from the three Boss PDF manuals in the `manuals/` folder rather than from a developed body of web reviews; where coverage is thin I say so. One naming note up front: the GearProfile calls this a Roland, but the unit, the manuals, and the marketing all brand it **BOSS VG-800** under the V-Guitar Processor line (firmware © Roland Corporation, who own Boss).

## 1. Lineage — what it actually is

The VG-800 is the modern, pedalboard-sized continuation of Roland/Boss's **V-Guitar** line: VG-8 (1995) → VG-88 (2000) → VG-99 (2007), then a long gap. Per [Sound on Sound](https://www.soundonsound.com/reviews/boss-vg-800), it's "around half the width" of the VG-99 and more compact than the SY-300/SY-1000 synths that filled the interim. The crucial generational change is the pickup interface: where every prior V-Guitar used the **13-pin analog GK** connector (GK-2A/GK-3), the VG-800 uses **Serial GK** — a single 1/4" TRS jack carrying a *digital*, per-string datastream from the GK-5 pickup ([Boss GK-5 page](https://www.boss.info/us/products/gk-5/)). **The GK-5 / Serial-GK platform predates the VG-800** — it debuted with the **GM-800** guitar-synth (~2023); the VG-800 (Jan 2025) is a later host on the same platform (also shared by the SY-1000's newer pickup support). That matters for research: most real-world GK-5 calibration data lives in **GM-800** threads, not VG-800-native ones.

Position it this way: the **GP-10** was the budget V-Guitar (amp/COSM modeling + basic synth, 13-pin); the **SY-1000** is the synth-forward flagship (three engines, deep MIDI, still 13-pin in its base form); the **VG-800** is the *modeling-forward* box — it inherits the VG-99's "model the whole instrument, not just the amp" philosophy but in a stompbox with Serial GK and Dual Guitar/Bass tricks the older units didn't have. What's new vs the VG-99: Serial GK (faster, digital, no 13-pin breakout), Dual Guitar/Bass (two instrument models split by string or fret), a far larger modern effects library ("over 150 types" per [Boss](https://www.boss.info/global/products/vg-800/)) pulled from the GT-1000 generation, USB-C multichannel audio, and TRS MIDI. What it loses vs the VG-99/SY-1000: no onboard expression treadle, far fewer knobs, much smaller screen, and (relative to SY-1000) a thinner synth section.

## 2. Controls & architecture

Front panel ([Quick Start](manuals/VG-800_eng01_W.pdf), p.2): a 132×64-ish LCD, **[OUTPUT LEVEL]** knob, three mode buttons (**[INST]**, **[EFFECTS]**, **[MENU]**), **[◄][►]** page buttons, **[EXIT]**, five **[1]–[5]** parameter knobs plus a **[SELECT]** knob, two footswitches (**[▼][▲]** for memory up/down) and one **[CTL 1]** assignable footswitch. Two combos worth memorizing: **[▼]+[▲]** = tuner, **[▲]+[CTL 1]** = FX BYPASS (hear only the raw INST model). It is knob-and-menu deep; everyone agrees the [Boss Tone Studio editor](https://bosstonecentral.com/) is the sane way to build patches.

The signal architecture (Reference Manual, p.2) is the important part. A "memory" runs:

`INST → (NORMAL mix) → FV1 → FX1 → FX2 → DIV → [CMP→AMP1→EQ1→NS1] // [DS→AMP2→EQ2→NS2] → MIX → FV2 → FX3 → CHO → DLY1 → DLY2 → S/R → REV → MST`

- **INST block** — the modeling engine. Selects an instrument type and (optionally) alternate tuning. This is the thing that makes the VG-800 not just a multi-FX.
- **NORMAL** — your guitar's actual magnetic pickup, blendable alongside the model.
- **DIV / two parallel chains** — the signal splits into two amp/EQ/noise-suppressor paths (each with its own AMP1/AMP2 modeling, EQ, gate) and recombines at MIX. DS in path B is a dedicated distortion block.
- **FV1/FV2** foot volumes, **FX1–FX3** three freely-assignable effect slots, **CHO** chorus, **DLY1/DLY2** two delays, **S/R** the stereo send/return loop, **REV** reverb, **MST** master.

Effects routing is **more constrained than a GT-/GX-style "free chain," corrected 2026-06:** the three **FX1–FX3** slots are freely assignable/movable and the **stereo S/R loop can be placed anywhere** in the chain (a spec added after NAMM), but **CHORUS / DELAY1 / DELAY2 / REVERB are fixed-position blocks (on/off only)** — you cannot freely reorder them like a GX-10. A stereo-collapsing block downstream (e.g. ACOUSTIC RESONANCE) will silently kill upstream per-string PAN edits. The INST models: **E.GUITAR** (Strat/Tele/LP/P-90/ES-335/L-4/Rickenbacker 360/Danelectro/wide-range/fretless), **ACOUSTIC** (Martin D-28/000-28, Gibson J-45/B-25, Guild D-40, nylon, **RESO** dobro, **BANJO**, **SITAR**), **AC BASS**, **E.BASS** (Jazz/Precision/StingRay/Rickenbacker/Thunderbird/Höfner violin/fretless), **DUAL GUITAR** & **DUAL BASS** (two models combined), **VIO GUITAR/VIO BASS** (bowed-string/swell character), and **SYNTH** (GR-300 emulation, ANALOG GR for bass, SOLO lead, FILTER BASS, CRYSTAL, ORGAN) (Parameter Guide, pp.4–17, 29).

## 3. Sonic character — what the modeling is good and bad at

Honest read from the manuals plus the two substantial reviews:

**Good.** The acoustic and 12-string modeling is the consistent standout. [MusicRadar](https://www.musicradar.com/guitars/guitar-pedals/boss-vg-800-v-guitar-processor-review) singled out the 12-string sims as good enough to nail QOTSA's "Song for the Dead/Mosquito" jangle, and called the **distorted bass** "unbelievably fat" and the **Leslie/organ** tones convincing. Sound on Sound loved the **GR-300 synth lead** ("brought back many happy memories") and the rotary-on-organ pairing. The electric-guitar models are competent and the per-string alt tuning is genuinely seamless — no warble on moderate shifts.

**Bad / caveats.** Boss's own *amp* modeling is the weak link: MusicRadar ranks it below Neural DSP and Line 6, and notes that running the VG-800's amp models *into a real guitar amp* produces "a very harsh, digital sound" — so go direct (Line/Phones output mode) or use FX BYPASS and feed real amps the raw model. The **sitar** "wouldn't have fooled Ravi Shankar" (SoS). Single-coil models can sound quieter/cleaner than the real thing because the hex pickup rejects hum (SoS). And there's no hiding that it's a digital instrument: extreme pitch-shifts and dense polyphonic synth patches show artifacts.

For this rig, "bad" is mostly upside. The harsh-digital-into-an-amp problem is irrelevant when the model is going into a fuzz wall, and the artifacts on extreme shifts are exactly the "recorded-wrong" texture the boards are built to exploit.

## 4. Dynamic & tracking behavior — latency and glitches

Serial GK is the headline: Boss markets it as **"latency-free performance"** with "no lag or latency" ([Boss](https://www.boss.info/global/products/vg-800/)), and both reviewers back the *feel* — SoS reports "no discernible latency," MusicRadar says tracking is "fantastic overall... a very rare moment when anything goes wrong," handling smashed open chords, two-step bends, and pinch harmonics in pitch. **Note honestly: Boss publishes no latency figure in milliseconds, and neither review measured one — the "zero latency" language is marketing/subjective, not a spec.** Treat sub-perceptible-but-nonzero as the realistic assumption, as with any pitch-tracking system.

Tracking is not plug-and-play. MusicRadar needed sensitivity tweaks to kill "wobble" on the low strings before tracking settled; the per-string **SENS** and **DISTANCE** calibration (GK SETTING, up to 10 saved profiles) is mandatory setup, not optional. A web search snippet referenced low E/A-string latency being addressed in a later firmware, but the **official changelog only lists v1.02 (Jan 2025): "Support for Boss Tone Studio" + "improved system stability"** ([Boss support](https://www.boss.info/us/support/by_product/vg-800/updates_drivers/b7a22a85-27e9-4473-a842-68ed73b939ca/)) — so I can't verify a dedicated tracking-latency fix; flag as unconfirmed. Glitches concentrate where you'd expect: large pitch intervals, fast tremolo-picked transients on low strings, and polyphonic synth. The GUITAR-TO-MIDI block has **HOLD types, PLAY FEEL, NO-DYNA velocity, and low-velocity cut** parameters specifically to tame triggering (Parameter Guide, p.43).

## 5. Signal-chain placement — why it's first in THIS rig

It has to be first, and not by preference — by physics. The GK-5 is a *divided* pickup; the VG-800 is the only box in the rig that can read it. Nothing can come before it. The summed mono-ish model/synth output then feeds **Polytune 3 → CB Clean → Colour Box V2 → MXR 108 → Hizumitas → ...**. Consequences:

- **By the time signal leaves the VG-800, hex separation is gone.** It outputs a normal (stereo-capable) instrument-level signal. No downstream pedal sees per-string data. Per-string processing must happen *inside* the VG-800 (its two parallel amp paths, per-string EQ/pan/level, Dual Guitar split).
- **CB Clean immediately downstream is correct.** The VG-800 outputs line/instrument level; CB Clean buffers and sets a clean reference into the dirt section. (The bench EHX Effects Interface exists precisely to reconcile the VG-800's line output with instrument-level pedals if levels misbehave — keep it in mind if the front of the chain sounds thin or clips.)
- **Stereo question.** The VG-800's OUTPUT is stereo (L/PHONES + R/MONO), and CHO/DLY/REV inside it are stereo. But Board 1 is mono until the CE-2W stereo split. So either run the VG-800 in mono (R/MONO only — the manual's mono rule) into the front chain, or keep its internal time/space minimal and let the boards do stereo. Given this rig prints everything through Board 3's stereo tape stage, running the VG-800 **mono with its onboard reverb/delay off** and letting the dedicated pedals do the work is the cleaner architecture. Save the VG-800's stereo for direct-to-Apollo experiments.
- **Output mode matters.** Set OUTPUT SELECT to **LINE/PHONES (Recording)** when going into the pedalboard/Apollo, not one of the amp-return modes (JC-120/Katana return) — those are voiced for plugging into a real amp's return and will sound wrong into the front of a pedal chain.

## 6. Source-specific behavior

**Baritone Jazzmaster + GK-5.** Home turf, with one wrinkle: it's a baritone, so the GK-5's per-string tracking is reading lower fundamentals than a standard guitar. Set **SCALE** appropriately in GK SETTING and calibrate **SENS/DISTANCE** carefully — low, slow strings are where wobble appears (exactly what MusicRadar hit). The baritone's native range plus the VG-800's **ALT TUNE / ±12 STEP / DROP** tunings means you can reach genuinely subterranean tunings without retuning the instrument. Magnetic + model blend (NORMAL MIX) lets you keep the real Jazzmaster's character under the model.

**Gold Tone EBM-5 banjo + GK-5.** This is the unusual and interesting one. Hex tracking on a *banjo* is off-label — banjos have extremely fast attack, fast decay, a high-tension 5th (drone) string, and bright transient content with little sustain. The GK-5 doesn't care that it's a banjo; it tracks per-string pitch like any string. Expect: (1) the **5th string** (short, drone) needs its own SENS/DISTANCE attention and may mistrack on the GK if the pickup geometry doesn't sit cleanly under it; (2) banjo's fast decay means synth/sustain patches will retrigger or gate audibly — use the GUITAR-TO-MIDI **HOLD** types or INST sustain to lengthen notes; (3) the banjo's brightness pushes the modeling hard, so darker amp/INST models tame it. The payoff for this rig is huge: a banjo can become a **doom baritone, an organ drone, a GR-300 synth lead, or an open-tuned acoustic** while keeping the banjo's attack envelope underneath — "banjo-as-lead" made literal. This is the single most rig-specific reason the VG-800 sits first.

**Modeled vs synth patches into a fuzz/wall chain.** A modeled-amp or acoustic patch hits the MXR 108 → Hizumitas → Longsword chain as a normal saturated/clean signal and fuzzes predictably. **Synth/pad/organ patches are the wildcard:** continuous waveforms turn into massive distorted drones (ideal), while polyphonic GR-300 chords will artifact heavily through a Muff — which is a feature for the "broken" aesthetic, not a bug.

## 7. Famous users

Honestly: **few notable adopters yet.** This is a 2025 product with no developed artist mythology — there's no VG-800 equivalent of "Wata's pedal." The broader V-Guitar lineage has heritage users (Andy Summers, Pat Metheny and Robert Fripp with Roland guitar synths; John Petrucci/Adrian Belew era GR/VG work), but attaching any of them to the VG-800 specifically would be invention. Treat the user base as early-adopter V-Guitar enthusiasts (the [VGuitarForums](https://www.vguitarforums.com/smf/index.php?board=514.0) community) rather than marquee names. Flagged: no verified famous VG-800 users at time of writing.

## 8. Live / power / I/O notes

- **Power:** runs on a standard Boss 9V supply (PSB-1U included); the DC IN jack *is* the power switch (plug = on). Off-mode draw 0.1 W. Boss doesn't publish operating current draw in the Quick Start; **budget a generous isolated 9V slot and verify draw before relying on a daisy-chain — unverified mA figure.** It's a digital box, so it wants clean, ample current.
- **Pickup connector:** GK IN is **Serial GK (1/4" TRS)** — requires a dedicated **BGK** serial cable (BGK-3/15/30); never a standard guitar or 13-pin cable. GK OUT chains a second Serial GK device.
- **I/O:** GUITAR INPUT (normal jack, blendable), **mono-in concept but stereo-out** (OUTPUT L/PHONES + R/MONO; use R/MONO only for mono), stereo TRS SEND/RETURN loop, two CTL/EXP jacks (FS-5U/FS-6/FS-7 footswitches or EV-30/FV-500/EV-5 expression pedals), **TRS MIDI IN/OUT** (BMIDI-5-35 cable), and **USB-C** for multichannel audio + USB-MIDI + the editor.
- **MIDI:** sends PC/bank/CC on memory changes (MEMORY MIDI), receives PC/CC to be controlled by H90/Blooper/etc., and crucially does **GUITAR-TO-MIDI** — per-string pitch-to-MIDI on separate channels (MONO mode) or one channel (POLY), with bend range, hold modes, and dynamics. That means the rig's Baritone JM or the *banjo* can drive the Octatrack, Digitakt, MPC, or a soft-synth.
- **No onboard expression treadle** — a real live limitation vs the VG-99/SY-1000. Add an EV-30 or FV-500 to the CTL/EXP jack for wah/volume/morph.
- **Auto-off** defaults to 20 min — turn it off for studio use.
- **Footprint:** 173 × 135 × 63 mm, 920 g. Compact for what it does.

## 9. Pairing recommendations (this rig's pedals, by name)

- **Modeled amp / electric model → MXR 108 → Hizumitas:** the canonical front-of-chain move. Build the model dark (Tweed/AC-style, treble pulled) so the banjo/baritone brightness doesn't ice-pick the fuzz. The Hizumitas's clockwise Tone then does the rest.
- **Synth pad / organ drone → Hologram Microcosm / CB Blooper / Walrus Etherealizer:** continuous synth waveforms are perfect granular/looper food. Capture a GR-300 or ORGAN drone in the Blooper and layer it; let the Microcosm granularize a sustained pad. This is the "sustained source for the End Board" role the Hizumitas dossier describes, but generated cleanly inside the VG-800.
- **Alt-tuned acoustic / 12-string model → CB Generation Loss → JHS 424 / PORTA424:** model a jangly open-tuned 12-string, print it degraded through the tape stage. The VG-800's clean acoustic model gives the tape pedals something pristine to ruin.
- **VIO (bowed) model → OBNE Dark Star V3 / Etherealizer:** the swelling, attackless VIO character into a smear reverb is a drone-machine. Pair with the instrument's volume knob for double swells.
- **Per-string Dual Guitar split → stereo CE-2W → Deco V2:** put a clean model on the low strings and a fuzz-ready model on the high strings (or pan them), then spread across the stereo split. Wide, layered, one-instrument-sounds-like-two.
- **Pitch-to-MIDI → Digitakt 2 / Octatrack / H90:** trigger samplers or MIDI-clock effects from the banjo. Niche but uniquely available here.

## 10. Reviews & demos (real links)

- [Sound on Sound — Boss VG-800 review](https://www.soundonsound.com/reviews/boss-vg-800) — the most technical written review; lineage, I/O, model coverage, GR-300, MIDI.
- [MusicRadar — Boss VG-800 review](https://www.musicradar.com/guitars/guitar-pedals/boss-vg-800-v-guitar-processor-review) — best on tracking calibration, 12-string/bass strengths, and the amp-modeling critique.
- [Boss — official VG-800 product page](https://www.boss.info/global/products/vg-800/) — model counts, "over 150 effects," 150 memories/mode, Dual functions.
- [Sound on Sound — Fitting a Boss GK-5 Kit](https://www.soundonsound.com/techniques/fitting-boss-gk-5-kit) — pickup install, the relevant context for the banjo/baritone mounts.
- [Premier Guitar — VG-800 demo, NAMM 2025 (YouTube)](https://www.youtube.com/watch?v=ek1dcVAYBH8) — first-look video demo.
- ["The Boss VG-800 Setup and Demo" (YouTube)](https://m.youtube.com/watch?v=tIY4F3b0zDA) — setup + tone walkthrough.
- [VGuitarForums — VG-800 board](https://www.vguitarforums.com/smf/index.php?board=514.0) — the deepest real-world user discussion (tracking, firmware, Serial GK). *(Note: it's a general-discussion board only — there is no VG-800 Patch Exchange sub-board yet, unlike the VG-99/VG-8 boards.)*
- **Patch platforms (corrected 2026-06):** the VG-800 is **NOT on Boss Tone *Central*** (bosstonecentral.com — the Boss-curated "Extra Collection" banks; the VG-800 category 404s, so no official bonus banks yet). It **IS on Boss Tone *Exchange*** ([bosstoneexchange.com](https://bosstoneexchange.com/) — user-to-user sharing; live `vg-800_guitar` + `vg-800_bass` slugs), where you browse/download a *memory* (one patch) or *liveset* (array) inside Boss Tone Studio and then export to hardware. Community upload count is likely sparse for a 2025 box (couldn't be machine-read — JS-rendered). The editor itself is **Boss Tone Studio**.

## 11. Mods / quirks / firmware / known issues

- **Calibration is the whole game.** Default sensitivity wobbles on low strings (MusicRadar); the per-string SENS/DISTANCE setup is non-negotiable, especially for a baritone and a banjo.
- **Firmware:** latest is **v1.02 (Jan 16 2025)** — adds Boss Tone Studio support + "improved system stability"; **the official changelog lists no v1.03+** ([Boss support](https://www.boss.info/us/support/by_product/vg-800/updates_drivers/...)). The "low-E/A latency fixed in a later firmware" claim is **refuted** — community research (VGuitarForums) traced it to a **cross-product mixup with the GM-800's v1.10 update**; the VG-800 firmware thread is actually about a macOS unzip snag (extract `VG-800_UPA_up.bin`). **Calibration, not a download, is the tracking fix.**
- **No onboard expression pedal**, no controls on the GK-5 (older GK-2/3 had S1/S2 + volume); you lose hands-on synth-balance control unless you wire an EXP pedal.
- **Tele bridge incompatibility:** the GK-5 won't fit traditional Telecaster bridges with raised side plates (SoS) — irrelevant here (Jazzmaster + banjo) but worth knowing.
- **Amp-model-into-real-amp = harsh digital** (MusicRadar). Go direct / Line mode.
- **GK-5 cable is slightly short** for rear-mounting on some bodies (MusicRadar).
- No hardware mods are a thing yet — it's a sealed digital unit. "Mods" here means firmware + Tone Studio patches, not soldering.

## 12. Spec sheet

| Spec | Value |
|---|---|
| Type | V-Guitar modeling/synth processor (Serial GK) |
| Brand | BOSS (V-Guitar Processor); firmware © Roland Corporation |
| Launched | January 2025 |
| Pickup interface | Serial GK, 1/4" TRS digital (GK-5 guitar / GK-5B bass; BGK serial cable required) |
| Instrument models | E.guitar, acoustic, banjo, sitar, reso, nylon, AC/E bass, Dual Guitar/Bass, VIO, synth (GR-300, ANALOG GR, SOLO, FILTER BASS, CRYSTAL, ORGAN) |
| Amp models | JC-120, Twin/Deluxe/Tweed Bassman combos, AC30, Marshall 1959, Mesa Recti, Matchless, Orange, Bogner, Ampeg/Markbass/Darkglass bass + MDP "X-" high-gain series |
| Effects | "Over 150 types"; 37 distortion models (BD-2, OD-1, SD-1, TS-808, DS-1, Klon Centaur, Proco RAT, etc.) |
| Alt tuning | Open D/E/G/A, Drop D–A, D-MODAL, NASHVL, 4TH, ±12 STEP, USER per-string, HARMONY mode, 12-string sim |
| Memories | 150 (guitar mode) + 150 (bass mode); 20 factory banks + user banks |
| Tuner | Single / Multi / TT (True Temperament) modes, 435–445 Hz |
| Inputs | GK IN (Serial GK TRS), GUITAR INPUT (1/4") |
| Outputs | L/PHONES + R/MONO (1/4" TRS, stereo; mono via R/MONO) |
| Loop | Stereo TRS SEND/RETURN |
| MIDI | TRS MIDI IN/OUT; PC/CC/bank send+receive; GUITAR-TO-MIDI pitch-to-MIDI (mono per-string / poly) |
| USB | USB-C: multichannel audio interface + USB-MIDI + editor |
| Control | CTL 1 + 2× CTL/EXP jacks (FS-5U/6/7, EV-30/FV-500/EV-5); no onboard treadle |
| Power | Boss 9V (PSB-1U); DC-IN = power switch; off-mode 0.1 W (operating mA not published) |
| Dimensions / weight | 173 × 135 × 63 mm / 920 g (2 lb 1 oz) |
| Editor | Boss Tone Studio (Mac/Win), Boss Tone Central / Tone Exchange |
| Firmware (verified) | v1.02 (Jan 2025) |
| Price | ~$650–$715 US / £599–£605 (pedal only); ~$1,000+ with GK-5 + cable |

Sources: [Boss VG-800 page](https://www.boss.info/global/products/vg-800/), [Boss GK-5 page](https://www.boss.info/us/products/gk-5/), Reference & Parameter manuals in `manuals/`, [Sound on Sound](https://www.soundonsound.com/reviews/boss-vg-800), [MusicRadar](https://www.musicradar.com/guitars/guitar-pedals/boss-vg-800-v-guitar-processor-review).

## 13. Starting-point patch scenarios (this rig)

Build these in Boss Tone Studio; remember the model feeds the *front* of Board 1, so leave the VG-800's REV/DLY mostly off and let the boards do time/space.

**(a) Banjo lead — "banjo-as-lead"**
- Source: EBM-5 + GK-5. INST: E.GUITAR (P-90 or LP) *or* SYNTH/SOLO for a synth-lead voice.
- Calibrate the 5th-string SENS carefully; LEAD EMPHASIS up if using VIO/SYNTH.
- NORMAL MIX low (let the model dominate the banjo attack). Amp model dark.
- Downstream: into Hizumitas (Tone 1–2 o'clock to tame brightness) → wall. Or clean → Microcosm.

**(b) Doom baritone — sustained low wall**
- Source: Baritone JM + GK-5. INST: E.GUITAR (LP/335) + ALT TUNE Drop or −5/−7 STEP for subterranean tuning.
- Dual Guitar optional: clean model low strings, dirty-ready model high strings.
- AMP1 dark/mid-forward; NORMAL MIX ~30% for real-pickup body.
- Downstream: MXR 108 → Hizumitas → Longsword, then stereo to End Board reverbs.

**(c) Synth-pad drone**
- Source: either instrument. INST: SYNTH (GR-300 or ORGAN), VOLUME for swell.
- HARMONY or fixed tuning; minimal NORMAL MIX. Internal slow chorus optional.
- Downstream: Etherealizer / Dark Star V3 / Blooper capture → infinite drone. Expect glorious artifacts when it hits the fuzz.

**(d) Alt-tuned acoustic / 12-string**
- Source: Baritone JM + GK-5. INST: ACOUSTIC (J-45 / D-28) + 12STR SW on, or ALT TUNE Open D/G.
- BODY/RESONANCE moderate; keep it pristine (this is the clean source the tape stage wants).
- Downstream: bypass the dirt, run clean → Generation Loss → PORTA424 / JHS 424 to degrade.

## 14. Versus alternatives — why it earns the first slot here

- **vs Boss SY-1000:** the SY-1000 is the synth flagship — three engines, deeper synthesis, more I/O, onboard expression — but bigger, pricier, and (in base form) still 13-pin GK. For a rig where the *job* is "turn a banjo into other instruments and feed a fuzz/tape chain," the VG-800's modeling-forward voicing, Serial GK, and pedalboard size fit better. If the rig were synth-*centric*, the SY-1000 would win. It isn't — it's texture-centric, and the VG-800's models are the right tool.
- **vs Boss GP-10:** the GP-10 is the cheaper, older, 13-pin V-Guitar with weaker effects and synth. The VG-800 beats it on Serial GK tracking, effects count, Dual functions, and modern modeling. No reason to choose the GP-10 here except budget.
- **vs Strymon Iridium (on the bench):** the Iridium is amp+IR only — no pitch tracking, no alt tuning, no synth, no instrument modeling. It models *amps* arguably more naturally than the VG-800 (Boss's amp section is the VG-800's weak point). But it can't turn a banjo into an organ or retune per string. In this rig the VG-800 owns cab/amp duty *because* it also owns everything the Iridium can't — and the rig design explicitly benches the Iridium for exactly this reason. If you only wanted a great direct amp tone, the Iridium would be the pick; you want a shape-shifter, so it isn't.
- **vs a plain magnetic pickup straight into the chain:** no contest for the rig's purpose — a magnetic pickup gives you one instrument, one tuning, no synth, no MIDI. The VG-800 is the entire premise of Board 1. The only thing the magnetic pickup does better is *being* the real instrument with zero tracking caveats — which is why NORMAL MIX exists, so you can keep that under the model.

**Bottom line:** the VG-800 earns first-slot not by being the best amp modeler (it isn't) but by being the only box that reads the GK-5, generates the alt-tuned/modeled/synth/MIDI source material this rig is built to mangle, and does it in a pedalboard-sized, Serial-GK, latency-imperceptible package. It's the brain; everything downstream is the wreckage.

## Sources

- [BOSS — VG-800 product page](https://www.boss.info/global/products/vg-800/)
- [BOSS — GK-5 Divided Pickup](https://www.boss.info/us/products/gk-5/)
- [BOSS — VG-800 Updates & Drivers (firmware v1.02)](https://www.boss.info/us/support/by_product/vg-800/updates_drivers/b7a22a85-27e9-4473-a842-68ed73b939ca/)
- [BOSS — VG-800 announcement press release (2025)](https://www.roland.com/us/company/press_releases/2025/BOSS-Announces-VG-800-V-Guitar-Processor/)
- [Sound on Sound — Boss VG-800 review](https://www.soundonsound.com/reviews/boss-vg-800)
- [Sound on Sound — Fitting a Boss GK-5 Kit](https://www.soundonsound.com/techniques/fitting-boss-gk-5-kit)
- [MusicRadar — Boss VG-800 V-Guitar Processor review](https://www.musicradar.com/guitars/guitar-pedals/boss-vg-800-v-guitar-processor-review)
- [Premier Guitar — VG-800 demo, NAMM 2025 (YouTube)](https://www.youtube.com/watch?v=ek1dcVAYBH8)
- ["The BOSS VG-800 Setup and Demo" (YouTube)](https://m.youtube.com/watch?v=tIY4F3b0zDA)
- [VGuitarForums — BOSS VG-800 General Discussion](https://www.vguitarforums.com/smf/index.php?board=514.0)
- [Boss Tone Central — VG-800 (editor / patch sharing)](https://bosstonecentral.com/)
- [Sweetwater — Boss VG-800 product/specs](https://www.sweetwater.com/store/detail/VG800--boss-vg-800-v-guitar-processor-for-guitar-and-bass)
- VG-800 Quick Start, Reference Manual, Parameter Guide (local `manuals/` — primary source for architecture, INST/effect/amp model lists, alt tuning, GUITAR-TO-MIDI, GK SETTING, I/O)
