# Chase Bliss Clean — Deep Research

A working dossier for the Chase Bliss **Clean** as the first always-on pedal on Board 1, sitting between the Polytune 3 and the JHS Colour Box V2. The single most important thing to know up front, because the product name is misleading: **Clean is not a clean boost, a preamp, a DI, or a buffer. It is a creative, VCA-based, two-stage stereo compressor** with a dynamic EQ, swell engine, tape-style emphasis filters, and a noise gate — fully analog, MIDI-controllable, and built to be "played" rather than set-and-forget. In this rig it is the front-end dynamics tamer that catches the VG-800's modeled transients and the banjo's brutal attack/decay imbalance *before* any of that hits the Colour Box, the 108, or the Hizumitas, so the fuzz/drive wall downstream gets a consistent, level-controlled source instead of a spiky one. Everything below the manual-sourced sections is flagged manual-vs-web because web coverage of a pedal literally named "Clean" is noisy.

## 1. What It Actually Is

Clean is Chase Bliss's first dedicated compressor, released **November 1, 2024 at $399** ([Chase Bliss product page](https://www.chasebliss.com/clean); release date per [Chase Bliss / multiple outlets](https://www.guitarworld.com/news/chase-bliss-clean-compressor-pedal)). The manual frames the whole pedal as the answer to one question — *"Can clean be as fun as dirty?"* — the idea being to bring the touch-sensitivity and reactive, "alive" quality of a fuzz or overdrive to a clean signal via compression rather than distortion (Clean Manual, pp. 2-3, "Overview"). Chase Bliss's own framing: *"From tube-like sag, to drifting equalization, to softening swells. It also became a very sophisticated compressor along the way."*

Mechanically (Manual p. 4-5, "What's Inside"): it is an **original, VCA-based circuit, not a clone of any existing comp** (it is explicitly *not* an Ross/Dyna/OTA design). The signal path is **100% analog and true stereo**, with **two stages of compression**, **feedforward blending**, an **adaptive envelope follower**, a **dynamic EQ**, **emphasis filtering described as "cassette-style noise reduction,"** a **noise gate**, a **dry blend**, an **external sidechain**, and **physical modeling** that simulates "the organic fluctuations of a wobbling spring." It is the responsible utility that can also be sabotaged into an unstable, sputtering overdrive (the "Dusty" mode). For this owner, who runs a degraded/tape-ruined aesthetic, that dual nature is the whole point: it can glue the front end *or* it can be the first stage of intentional disrepair.

Where it solves a real problem in THIS rig: the sources feeding it are a Roland VG-800 (modeled amp/synth output) and a banjo with a GK-5 divided pickup. Neither produces a polite, guitar-shaped dynamic envelope. Clean exists to flatten that out — or color it — before the dirt.

## 2. Controls & Dip Switches

All of this is from the manual (pp. 10-19, 34-39), which is authoritative — the layout is dense and most web reviews simplify it.

**Top-row knobs / footswitch (the visible controls):**
- **Sensitivity (Ramp).** Sets the dynamic threshold — *"what too loud is."* Higher = more sensitive/more compression triggered; lower = only the loudest playing is affected. The most important knob; the manual tells you to watch the left LED and set this first for every instrument. When ramping is engaged, this knob's function changes to set ramp speed.
- **Wet.** Loudness of the processed (compressed) signal. "Able to apply a healthy boost." This is the make-up gain — the key to using Clean as a level-setter into the chain.
- **Dry.** Loudness of the unprocessed signal. Also boostable — this is the parallel/New-York-comp blend control.
- **Dynamics.** Amount of compression, and a *shape-shifting* control: it sweeps from gentle compression (1:1 → 2:1 → 4:1 → 10:1) through infinite-ratio **limiting** at noon, then into **Sag** in the last quarter (Manual pp. 24-27). More on this in §4.
- **Attack.** Compressor onset speed: fastest **0.5 ms** at minimum, slowest **300 ms** at max. Also sets the speed of motion-based EQ modes and Motion mode.
- **EQ.** One-knob dynamic EQ. CCW removes highs, CW removes lows; **noon = EQ off** (Manual pp. 14, 28-29). Three modes via the toggle below it.
- **Bypass footswitch.** Tap = on/off. **Hold = max out the Sag effect** (momentary "fall apart" gesture).
- **Presets footswitch.** Left/right positions store a preset, middle = live. Save by holding the relevant footswitch ~3 s (Manual p. 11).
- **AUX footswitch.** Engages the **Swell** (default momentary; latchable via the LATCH dip). Two swell modes: Dynamic (default) and Manual.

**Three center toggles (3-way each):**
- **Release** — LEFT Fast (50 ms) / MIDDLE user-adjustable (default 650 ms) / RIGHT Slow (1.5 s).
- **Mode** (EQ mode) — LEFT **Shifty** (EQ shifts when you play, past the Sensitivity threshold) / MIDDLE **Manual** (classic fixed EQ) / RIGHT **Modulated** (EQ auto-modulates as you play).
- **Physics** — LEFT subtle wobble / MIDDLE normal stable / RIGHT twitchy, unstable. Models the spring behavior that lets the envelope drift and sputter.

**CONTROL dip bank (8, top of pedal, Ramping/automation — Manual pp. 36-37):** Dynamics, Attack, EQ, Dry, Wet, Bounce, Sweep, Polarity. Engaging Bounce + a knob's dip modulates that knob continuously (LFO-style); Ramp does a one-time movement. Sweep sets top/bottom of the range; Sensitivity becomes the ramp-speed control.

**CUSTOMIZE dip bank (8 — Manual pp. 34-35):**
- **MISO** — Mono In, Stereo Out (splits a mono input to stereo).
- **SPREAD** — independent stereo processing of EQ/comp/swell per channel for stereo widening (even from mono).
- **LATCH** — footswitches latch instead of momentary.
- **SIDECHAIN** — use the 1/8" sidechain input to trigger compression from an external source.
- **NOISE GATE** — gate that mutes between notes (Sensitivity sets threshold, Dynamics sets release in this mode).
- **MOTION** — special "motion mode" modulating compression amount (Dynamics = depth, Attack = rate).
- **SWELL AUX** — changes AUX footswitch to trigger single tempo-synced swells.
- **DUSTY** — turns the second-stage limiter into a crumbly overdrive across wet *and* dry signals.

**Hidden Options (hold both footswitches — Manual pp. 16-19):** re-purposes the knobs for Swell In/Out times, Gate Threshold, Gate Release, User Release value, Envelope Balance (HPF on the control signal so it ignores bass / responds to highs), Envelope Type (Analog / Adaptive / Combo), and Spread Routing (assign SPREAD to EQ or to volume-based effects).

That is a lot of pedal. The takeaway for the rig: most of this can be saved into the **2 onboard presets** and recalled, so the complexity is a setup cost, not a per-gig cost.

## 3. Sonic Character / What "Clean" Means Here

"Clean" here means **studio-grade, character-capable compression**, not "transparent utility." The manual claims studio-grade analog parts and Tape Op's review confirms it has "substantial headroom and character options rather than transparent compression… a creative outboard tool rather than a conventional utility compressor" ([Tape Op](https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal)). It *can* be set transparent (low Dynamics, feedback side, EQ at noon = bypassed), and Tape Op notes the lower-ratio range is "subtle and transparent compression." But it can also "get nasty" — the same review's phrase — via Sag, Dusty, and Modulated EQ.

So for the front-end role: dial it transparent and it is effectively a clean leveler + optional make-up boost via Wet. The emphasis filtering (the "cassette-style noise reduction" stage) gives it a slightly hi-fi'd, tightened top end even when set clean — useful for the banjo's harsh upper mids. There is no inherent "color" you're forced to accept the way a Ross-style comp adds a mid bump; the EQ is opt-in (noon = off).

## 4. Dynamic Behavior

This is the deepest part of the pedal (Manual pp. 24-27, "Dynamics"). Each stereo channel is **two compressors in series: Stage One (shape-shifting compressor) → Stage Two (variable hard limiter)** — a real studio trick where the flexible first stage does the musical work and the second stage catches anything that slips through.

The **Dynamics** knob sweep:
- **First half — Compression.** Classic ratios increasing from 1:1 up through ~10:1. Lower part of the range = subtle/transparent; clamps harder toward noon.
- **Noon — Limiting (∞:1).** Sensitivity now sets the absolute ceiling. As you push past noon, the pedal **blends from feedback compression to feedforward limiting** — feedback being "natural, smooth, relaxed," feedforward being "precise, snappy, aggressive." Tape Op specifically calls out this smooth feedback-to-feedforward blend as a standout ([Tape Op](https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal)).
- **Last quarter — Sag.** Beyond compression, into simulated overloaded-tube behavior: "Your signal falls out, falters, and sputters as you play harder." This is the tube-sag voice, and holding the bypass footswitch maxes it momentarily.

**Boost range:** Wet and Dry knobs each "apply a healthy boost," so Clean *can* deliver unity-or-above output and act as a level-setter — but it is a compressor's make-up gain, not a dedicated clean-boost circuit. Realistically you'll set Wet for the front-end level you want into the Colour Box.

**Does it stay clean into the fuzzes?** Yes, by design, if you keep Dynamics below noon and Dusty/Sag off. The whole pitch is touch-sensitive cleanliness. But the owner should note: a *compressor in front of fuzz* changes how the fuzz reacts — see §5. **Physics** (manual p. 13) lets you deliberately destabilize the envelope (wobble/sputter) — that's the intentional-disrepair lever for this rig's aesthetic.

## 5. Signal-Chain Placement — Why First

Order: `VG-800 → Polytune 3 → CB Clean → Colour Box V2 → MXR 108 → Hizumitas → Brothers AM → Longsword → Oxford → BF-3 → Somersault → CE-2W → Deco`.

Clean is first (after tuner) for sound reasons:

- **Compression belongs before dirt when you want consistency.** Putting Clean ahead of the Colour Box and the fuzzes means it levels the *source* before saturation, so the fuzz wall gets an even drive level whether the owner is picking softly or digging in. Comp-after-fuzz only controls output level; comp-before-fuzz controls how hard the fuzz is *hit*, which is what you want when the source is unpredictable (modeled VG-800 / banjo). This is the textbook reason for slot one.
- **It sets the front-end level for the entire chain.** Wet knob = the master input trim into the Colour Box's preamp. Get this right and the rest of the board's gain staging is stable.
- **The 108 Fuzz Face caveat.** Silicon Fuzz Faces (the MXR 108) are notoriously sensitive to what's in front of them — they want a high-impedance, un-buffered source for the classic cleanup-from-guitar-volume trick. Clean is true bypass but, when ON, its VCA output is a low-impedance, line-ish, *already-compressed* signal. Note, though, that the **Colour Box V2 sits between Clean and the 108**, so the 108 is already seeing the Colour Box's buffered/transformer output regardless. Net: Clean isn't what's "ruining" the 108's input — the Colour Box is the dominant influence there. If the 108 ever sounds gated/thin, that's the buffer-in-front issue, not Clean specifically.
- **Don't over-compress into fuzz.** Heavy compression before a Big-Muff-style pedal (Hizumitas) can make the fuzz sound flat and remove the dynamic "bloom." For the doom wall that's often fine; for anything that needs to breathe, keep Dynamics low (compression, not limiting) when the Hizumitas is engaged.
- **Why not put it last?** Tape Op uses Clean as an end-of-chain *stereo mix bus* compressor and it excels there — but in THIS rig the End Board already prints through the PORTA424/JHS 424 tape stages, and the owner wants Clean shaping the *instrument's* touch response, not gluing the final stereo mix. Front slot is correct for the stated goal.

## 6. Source-Specific Notes

- **VG-800 (modeled / divided source).** Clean is setting level for COSM-modeled output, not a raw pickup. Modeled amp signals already have their own compression baked in; stack Clean lightly (low Dynamics) or you'll double-compress and squash the model's feel. The **Sensitivity** knob is critical here because the GK-5's per-string output level differs from a passive pickup — set Sensitivity by watching the left LED at real playing volume (Manual p. 9), don't assume guitar settings transfer. For VG-800 synth/pad patches, Clean's swell and Motion modes can turn sustained modeled drones into evolving textures before they even reach the time/texture boards.
- **Banjo (Gold Tone EBM-5 + GK-5).** This is where Clean earns its slot. Banjo has violent attack and very fast decay — the classic "all transient, no sustain" problem. Clean's two-stage comp slows the attack (set Attack slower, ~50-100 ms, to let the pick spike through then clamp) and the limiter + slow Release (1.5 s) extends the perceived decay, making banjo notes behave more like guitar notes before they hit the fuzz. Use **Envelope Balance** (Hidden Options) to filter lows out of the control signal so the comp reacts to the banjo's bright register, not phantom low end. This is the single best argument for Clean being first.
- **Baritone Jazzmaster.** Lots of low-end energy; the opposite problem. Here you may *want* Envelope Balance the other way (full-range) so the comp tames the boomy low strings, and a faster Attack to catch the baritone's slower, heavier transients. Clean tightens the low end before the Colour Box adds its girth.

## 7. Famous Users (Honest)

Too new (Nov 2024) for a developed user mythology. Chase Bliss's roster overlaps the ambient/experimental world — Andy Othling (Lowercase Noises) is a long-standing Chase Bliss demo artist associated with Mood, Blooper, and Generation Loss ([Equipboard](https://equipboard.com/pros/andy-othling)) — but **I could not verify any specific notable artist citing the Clean as a signature piece.** Treat any "famous users" claim for this pedal with suspicion at this date. Its real reputation so far is among studio/compression nerds and the Chase Bliss faithful, which is the honest answer.

## 8. Live / Power / I/O Notes

- **Power:** 9V DC, center-negative, **~300 mA** (Manual p. 6; [Chase Bliss](https://www.chasebliss.com/clean)). This is a *hungry* digital-control/analog-path pedal — give it a 300 mA+ isolated supply slot, not a daisy-chain. Many supplies only deliver 100 mA per port; budget for a high-current output.
- **I/O:** True stereo. Mono, stereo, or mono→stereo (MISO dip). Dual stereo jacks; the manual notes you may need TRS-to-dual-TS cables for stereo (Manual p. 6). In this rig Clean runs mono at the front of Board 1 (stereo doesn't begin until the CE-2W later), so its true-stereo and SPREAD features are dormant here unless the owner re-purposes it. (Worth noting: Clean *could* be redeployed end-of-chain as a stereo bus comp if the rig ever changes — Tape Op's preferred use.)
- **Bypass:** True bypass, momentary or latching (LATCH dip).
- **MIDI:** TRS MIDI in, requiring a **Chase Bliss MIDIbox** to convert standard MIDI to the TRS jack (Manual p. 38-39). Supports **PC and CC** — full control of every knob, toggle, and the Hidden Options. **2 onboard presets, up to 122 via MIDI** ([Chase Bliss](https://www.chasebliss.com/clean)). The MIDI/AUX jack doubles as an external-footswitch input (any normally-open momentary on a TS cable controls AUX/swell automatically — Manual p. 39).
- **CV / Expression:** Separate EXP/CV jack. CV range 0-5 V — **the manual explicitly warns that higher or negative voltage can damage the pedal** (Manual p. 38). Set the controlled knob(s) and range via the ramping dip switches.
- **Sidechain:** 1/8" TS sidechain input for external-trigger compression (sync the comp/swell/gate to a drum machine or other instrument).

**The Chase Bliss MIDI ecosystem (relevant — owner has many CB pedals):** The owner runs Brothers AM, Lost & Found, Generation Loss, Big Time, MOOD MkII, Blooper (and benched Onward). All speak the CBA MIDI-over-TRS protocol via MIDIbox/Midibox-style routing, and Chase Bliss pedals like Blooper/MOOD MkII can receive MIDI clock. **I could not confirm from the manual or web that Clean itself receives or transmits MIDI clock / participates in a tempo-sync bus** — Clean's tempo-relevant features (tempo-synced swells via SWELL AUX) imply clock support, but treat that as unverified. What *is* certain: a single MIDIbox + MIDI controller (the owner has a Morningstar-class setup implied by this many CB units) can recall Clean presets alongside Brothers AM, Generation Loss, etc., for whole-board scene changes. [Web note: CB MIDI clock behavior confirmed for Blooper/MOOD MkII per Morningstar forum, not specifically for Clean.]

## 9. Pairing Recommendations (This Rig, By Name)

- **Into the Colour Box V2 (immediately after).** This is the key division of labor — see §14. Clean handles *dynamics and level*; the Colour Box handles *tone color and preamp drive*. Set Clean transparent (low Dynamics, EQ at noon) and let the Colour Box do the EQ/saturation. Don't fight them: if you want front-end EQ, use the Colour Box's full EQ, not Clean's one-knob EQ, and keep Clean's EQ at noon (off).
- **Into the MXR 108 / Hizumitas.** Light compression before fuzz = consistent fuzz drive. For the doom wall, push Sensitivity up so even quiet picking triggers full saturation downstream (compression makes the fuzz feel "always-on huge"). For dynamic playing, back Dynamics down so the fuzz still responds to your attack.
- **Sag/Dusty as a pre-dirt texture.** Engage Dusty or hold-for-Sag and you get a crumbly, sputtering source feeding the Hizumitas — stacked degradation, on-brand for the rig. Use sparingly; it's a flavor, not a default.
- **MIDI scene recall with Brothers AM / Generation Loss / Big Time / MOOD MkII / Blooper.** One controller PC message can flip Clean's preset (e.g., "transparent leveler" → "Dusty pre-fuzz") at the same instant it changes Brothers AM channels and Generation Loss programs. This is the strongest ecosystem argument for keeping Clean MIDI-wired even though it lives at the front.
- **Swell into the texture boards.** Clean's Dynamic/Manual Swell can volume-swell the source *before* it reaches the Microcosm, Dark Star V3, and the End Board's Blooper/MOOD — feeding pre-swelled material into granular/loop pedals makes them sound intentional. This is a sleeper use given the owner's drone aesthetic.

## 10. Reviews & Demos (Real Links)

- [Chase Bliss — official Clean page](https://www.chasebliss.com/clean) — authoritative specs, $399, feature list.
- [Tape Op — Clean Stereo Compressor review](https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal) — best studio-context written review; stereo mix-bus use, feedback/feedforward, sidechain tricks.
- [Guitar World — "make clean guitar as fun as overdriven guitar"](https://www.guitarworld.com/news/chase-bliss-clean-compressor-pedal) — launch interview, concept framing.
- [Sonic State — Clean: Creative Compressor](https://sonicstate.com/news/2024/10/11/chase-bliss-clean-creative-compressor/) — launch overview.
- [Gearnews — Chase Bliss Clean: Revolutionary Compression](https://www.gearnews.com/chase-bliss-clean-revolutionary-compression/) — feature breakdown.
- [Pedal of the Day — Clean Creative Compressor](https://www.pedal-of-the-day.com/2024/11/17/chase-bliss-clean-creative-compressor/) — overview + demo.
- [Compressor Pedal Reviews — Clean review](https://www.compressorpedalreviews.com/post/chase-bliss-clean-compressor-review) — compression-specialist deep dive.
- [Delicious Audio — Chase Bliss Clean Stereo Compressor](https://delicious-audio.com/chase-bliss-clean/) — concise spec roundup.
- [The Guitar Channel — Clean sound-only demo](https://theguitarchannel.biz/2025/02/clean-chase-bliss-creative-compressor-sound-only-demo/) and [compression demo](https://theguitarchannel.biz/2025/04/clean-chase-bliss-compression-demo/) — ears-only and tweak demos.
- [KVR Audio — Clean deep-dive review thread](https://www.kvraudio.com/forum/viewtopic.php?t=620754) — user-level deep dive.

## 11. Mods / Quirks / Firmware / Known Issues

- **All the "weird" is built in, not a mod.** Sag, Dusty, Physics, Motion, Modulated EQ, Swell — these are the intended sabotage modes. There's no obvious analog-mod target the way there is on a fuzz; it's a digitally-controlled analog pedal, so behavior changes come via firmware/dip/MIDI, not soldering.
- **Quirk — no ratio detents.** No marked ratio positions; you set the Dynamics sweep by ear and the left LED ([Tape Op](https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal)). Same with Sensitivity — every instrument needs its own setting (the GK-5 banjo and a passive Jazzmaster will not share a Sensitivity setting).
- **Quirk — Sensitivity is instrument-dependent and interactive.** The manual repeatedly warns to re-set it per source and watch the LED. With a divided GK-5 source this matters more than usual.
- **Complexity is the main criticism.** Multiple reviews note that if compression already confused you, this pedal is "hard work" ([compressor review summary](https://www.compressorpedalreviews.com/post/chase-bliss-clean-compressor-review)). Mitigated by presets.
- **CV input is fragile.** Stay within 0-5 V; negative/over-voltage can damage it (Manual p. 38).
- **Power.** The ~300 mA draw catches people out; under-powering causes dropouts. **No 18 V trick** — it's a 9 V pedal.
- **Firmware:** Chase Bliss pedals are field-updatable; check chasebliss.com for Clean updates. No widely reported failures as of mid-2026 — it's too new for a track record, but Chase Bliss build quality and support (help@chasebliss.com, per Manual p. 42) are well regarded.

## 12. Spec Sheet

| Spec | Value | Source |
|---|---|---|
| Type | Creative VCA compressor (original circuit, not a clone) | Manual p. 4 |
| Signal path | 100% analog, true stereo | Manual p. 4-5 |
| Compression | Two-stage (shape-shifting comp → variable limiter) per channel | Manual p. 24 |
| Dynamics range | 1:1 → 10:1 comp → ∞:1 limiting → Sag; feedback↔feedforward blend | Manual p. 24-26 |
| Attack | 0.5 ms – 300 ms | Manual p. 13 |
| Release | 50 ms / user (default 650 ms) / 1.5 s | Manual p. 13, 17 |
| EQ | One-knob dynamic EQ (HPF/LPF), 3 modes: Shifty/Manual/Modulated; noon = off | Manual p. 14, 28 |
| Extras | Swell (2 modes), noise gate, Dusty overdrive, Motion, Physics, emphasis filters | Manual p. 30-35 |
| Presets | 2 onboard, up to 122 via MIDI | Manual p. 11; [Chase Bliss](https://www.chasebliss.com/clean) |
| MIDI | TRS MIDI via Chase Bliss MIDIbox; PC + CC; controls all knobs/dips/Hidden Options | Manual p. 38-39 |
| CV / EXP | EXP/CV jack; CV 0-5 V (do NOT exceed / no negative voltage) | Manual p. 38 |
| Sidechain | 1/8" TS external sidechain input | Manual p. 34, 38 |
| Bypass | True bypass, momentary or latching (LATCH dip) | Manual p. 34; [Chase Bliss](https://www.chasebliss.com/clean) |
| Power | 9V DC, center-negative, ~300 mA | Manual p. 6; [Chase Bliss](https://www.chasebliss.com/clean) |
| Price / release | $399 USD / November 1, 2024 | [Chase Bliss](https://www.chasebliss.com/clean), [Guitar World](https://www.guitarworld.com/news/chase-bliss-clean-compressor-pedal) |

## 13. Starting-Point Settings (This Rig)

Knob positions are clock-face. These are starting points; Sensitivity always needs a per-instrument set against the left LED.

**(a) Transparent front-end leveler** — the default always-on setting, feeding the Colour Box
- Sensitivity: set by ear/LED at playing volume · Dynamics: 10-11 (gentle compression, below noon) · Wet: 12-1 (unity to slight boost) · Dry: off or 9 · Attack: 11 · Release: middle (650 ms) · EQ: noon (off) · Mode: Manual · Physics: middle (stable) · all CUSTOMIZE dips off.
- Goal: even out the VG-800/banjo level before any dirt, no audible coloration. Save to a preset.

**(b) Banjo transient tamer** — for the EBM-5 + GK-5 lead work
- Sensitivity: higher (banjo is bright/quiet-in-control-band) · Dynamics: 12 (limiting) · Attack: 1 o'clock (slow, let the pluck through) · Release: right (1.5 s, extend decay) · Wet: 1 · Dry: 10 (parallel, keep pick detail) · EQ: noon · Hidden: Envelope Balance toward "More" (ignore lows).
- Goal: banjo notes that sustain like guitar notes into the fuzz wall.

**(c) Always-on huge fuzz feeder** — slam the Hizumitas/108 evenly
- Sensitivity: high · Dynamics: 12-1 (hard limiting) · Wet: 1-2 (hot) · Dry: off · Attack: 9 (fast) · EQ: noon · Physics: middle.
- Goal: even quiet picking triggers full downstream saturation — the doom wall stays "always massive."

**(d) Dusty pre-dirt sputter** — intentional disrepair before the fuzzes
- Engage DUSTY dip · Dynamics: 2 o'clock (into Sag) · Sensitivity: high · Physics: right (twitchy) · Wet: 12 · Dry: 11 (let the dust bleed through) · Mode: Modulated (drifting EQ).
- Goal: a crumbly, faltering source feeding the Hizumitas — stacked degradation on-brand for the rig. Recall via MIDI alongside a Brothers AM/Generation Loss scene.

## 14. Versus Alternatives — and Why It Earns First Slot

**Vs. a clean boost / preamp (what the brief first assumed it was):** Clean is *not* primarily either. A Colour Box V2 — sitting right after it — already *is* the preamp/EQ/coloration stage. So the division of labor is clean: **Clean = dynamics + level + (optional) sabotage; Colour Box = tone color + preamp drive + full EQ.** If you wanted a transparent boost only, a simple clean boost would be cheaper and smaller — but it wouldn't tame the banjo/VG-800 transients, which is the actual front-end problem. Clean earns the slot because it solves a dynamics problem a boost can't.

**Vs. conventional comps (Keeley Compressor Plus, Origin Cali76, Walrus Deep Six, Empress Compressor):** Those are better choices if you want a *set-and-forget transparent comp* and nothing else — cheaper, simpler, lower current draw, and the Cali76/Empress are arguably more "studio-transparent." Clean wins when you want (1) the same comp to *also* be a swell/EQ/overdrive/texture device, (2) true-stereo and MIDI preset recall integrated with the rest of the CB board, and (3) the Sag/Dusty character that fits a degraded aesthetic. For this owner — deep in the Chase Bliss MIDI ecosystem, running an unpredictable modeled/banjo source, chasing tape-ruined textures — Clean is the right tool precisely *because* it's more than a comp. A Cali76 would tame the dynamics and stop there; Clean tames them and then offers a second life as a front-end texture box recallable by MIDI alongside Brothers AM and Generation Loss.

**Why first slot, summarized:** compression-before-dirt gives consistent fuzz drive from an inconsistent source; the Wet knob sets the master input level for the whole board; the banjo/VG-800 transient problem is best solved at the very front before any saturation locks it in; and the Colour Box right behind it means Clean never has to do tone-shaping, so it can stay in its lane as the dynamics/level/texture anchor.

## Sources

- [Chase Bliss — Clean (official product page)](https://www.chasebliss.com/clean) — specs, price, release framing.
- Chase Bliss — *Clean: A Field Guide* (the printed manual in this repo, `manuals/Clean_Manual_Pedal_Chase+Bliss.pdf`) — **primary source of truth** for all controls, dip switches, signal flow, MIDI/CV/I/O, and modes.
- [Tape Op — Clean Stereo Compressor review](https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal)
- [Guitar World — Chase Bliss Clean compressor launch interview](https://www.guitarworld.com/news/chase-bliss-clean-compressor-pedal)
- [Sonic State — Clean: Creative Compressor](https://sonicstate.com/news/2024/10/11/chase-bliss-clean-creative-compressor/)
- [Gearnews — Chase Bliss Clean: Revolutionary Compression](https://www.gearnews.com/chase-bliss-clean-revolutionary-compression/)
- [Pedal of the Day — Clean Creative Compressor](https://www.pedal-of-the-day.com/2024/11/17/chase-bliss-clean-creative-compressor/)
- [Compressor Pedal Reviews — Clean review](https://www.compressorpedalreviews.com/post/chase-bliss-clean-compressor-review)
- [Delicious Audio — Chase Bliss Clean Stereo Compressor](https://delicious-audio.com/chase-bliss-clean/)
- [The Guitar Channel — Clean sound-only demo](https://theguitarchannel.biz/2025/02/clean-chase-bliss-creative-compressor-sound-only-demo/)
- [KVR Audio — Clean deep-dive review thread](https://www.kvraudio.com/forum/viewtopic.php?t=620754)
- [Equipboard — Andy Othling (Chase Bliss artist context)](https://equipboard.com/pros/andy-othling)
- [Morningstar forum — Chase Bliss external MIDI clock (Blooper/MOOD context, not Clean-specific)](https://forum.morningstar.io/t/external-midi-clock/6209)
