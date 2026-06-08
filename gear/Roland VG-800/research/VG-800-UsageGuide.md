# BOSS VG-800 — Usage Guide

How to *actually* get great results from the VG-800 in this rig, to complement the spec/reference dossier in `VG-800-DeepResearch.md`. It's the **brain of Board 1** — every modeled, alt-tuned, synth, or MIDI source originates here before a fuzz touches it — and the whole premise is **banjo-as-lead**: turning the Gold Tone EBM-5 (via GK-5) into a doom baritone, an organ drone, a GR-300 synth lead, or an open-tuned acoustic while keeping the banjo's attack underneath. Two truths govern everything: **calibration (not a firmware download) is the tracking fix**, and **run it in LINE mode, mono, with onboard reverb/delay off** so the boards do the time/space.

> Captured this wave (second pass, 4 agents — the rig-central centerpiece treatment): 6 video transcripts + 15 distilled links + **2 rig-specific GK-5 calibration profiles** = 23 artifacts (see §10). All video attributions verified via yt-dlp. Four dossier corrections folded in (Tone Central vs Exchange; firmware-latency-claim refuted; FX-routing reality; GK-5 platform predates the VG-800). Coverage honesty: it's a Jan-2025 box — most calibration data comes from **GM-800** threads on the identical GK-5/Serial-GK platform.

---

## 1. Essential workflows

**Setup first (Marcus Curtis / Jared Gunston):** check firmware by holding **[EXIT]** on power-up (units shipped on v1.01 → update to **v1.02**: hold **[MENU]** on power-up → it mounts as a USB drive → copy the `.bin` → eject; then install the driver, then Boss Tone Studio). **Turn auto-off OFF** for studio use (defaults to 20 min). Set **OUTPUT SELECT = LINE/PHONES (Recording)** into the pedalboard — *not* a JC-120/Katana amp-return mode, which sounds harsh/wrong into a pedal front-end.

**Pickup height is make-or-break (the biggest practical finding).** Mount the GK-5 to **~1 mm string-to-pickup clearance, dead level, rock-solid (no tilt under playing).** Too low = flubby tone forcing you to gain up = hiss; too high (~3 mm) = string buzz + bad tracking. 1 mm fixes both ([jared-gunston-install-gig-presets](transcripts/jared-gunston-install-gig-presets.md)).

**GK-5 calibration — the reliable method** (path: **MENU → GK SETTING**, up to 10 saved profiles): **tune each string's SENS so the on-screen level bar reads ~75% on a normal pick** — this is the dependable target even though absolute numbers vary. Real-world direction (from the GM-800 GK-5 thread): the **default per-string SENS is often too hot**; **thin/high strings frequently need to go UP, fat/low strings DOWN** to stop the low-string wobble. Set per-string **DISTANCE** (pickup-to-saddle) and keep the **global GAIN low (~2)**. Save a profile per instrument ([vguitarforums-gk5-tracking-calibration](links/vguitarforums-gk5-tracking-calibration.md)). Detailed starting points for *this rig's* two instruments are in the calibration profiles: [`calibration-banjo-EBM5.md`](calibration-banjo-EBM5.md) and [`calibration-baritone-JM.md`](calibration-baritone-JM.md).

**Architecture reality (Gear Sounds):** the **[EFFECTS]** screen shows the chain as a pedalboard row, but it's **not** a free GX-style chain — only the **FX1–FX3** slots are freely movable and the **S/R loop can be placed anywhere**; **CHORUS/DELAY1/DELAY2/REVERB are fixed-position, on/off only.** **DIV = two parallel amp paths** (MODE SINGLE/DUAL, CHANNEL A/B, AB BALANCE centered at 50). **NORMAL MIX** blends the real magnetic pickup under the model. **CTL-1** is assigned per patch; **[▼]+[▲]** = tuner.

---

## 2. GK-5 calibration craft (banjo & baritone)

> Off-label honesty: GK tracking on a *banjo* is the dossier's premise, not a documented Boss workflow. The EBM-5 is a **solidbody electric banjo**, which makes GK-5 mounting physically feasible. Parameter names/ranges are verified from the Parameter Guide; banjo-specific *values* are calibrated inference — **verify by ear.**

**Banjo (the hard one)** — full profile in [`calibration-banjo-EBM5.md`](calibration-banjo-EBM5.md):
- Mount on the flat solidbody with the GK-5 shims so all 5 strings cross the element parallel. Audition **SCALE** (no banjo preset — try ST 648 mm vs LP 628 mm). Tune each string to the ~75% bar; wobble-fix order per string = **lower SENS → raise DISTANCE → lower global GAIN**.
- **The 5th-string drone problem:** it's short, hot, high-G, and may sit off-lane → mistracks. Give it its own low SENS; and when it won't behave, **mute the 5th from the model** (STRING LEVEL 5 = 0 / STRING MUTE 5) while keeping the *real* 5th drone via **NORMAL MIX** — usually the better musical result anyway. Realistic expectation: **the 4 main strings track for leads; the 5th is typically excluded from the model.**

**Baritone (easier)** — full profile in [`calibration-baritone-JM.md`](calibration-baritone-JM.md): set **SCALE** to LP 628 mm (or the longest preset); low strings want **lower SENS + higher DISTANCE** — the documented MusicRadar low-string wobble fix (lower SENS → raise DISTANCE → lower GAIN → SCALE up → pick nearer the bridge). Then exploit the VG-800's tunings for subterranean range without retuning the instrument.

---

## 3. Banjo-as-lead patch designs (the rig's whole premise)

Each keeps the banjo's attack envelope and is voiced to feed a specific downstream pedal by name. Build in Boss Tone Studio; keep the VG-800's REV/DLY off.

| Voice | Recipe | Into |
|---|---|---|
| **(a) Doom baritone wall** | INST **E.GUITAR (LP/335)** + **ALT TUNE −5/−7 STEP**, dark AMP1 (treble pulled), **NORMAL MIX ~30%** | MXR 108 → Hizumitas (Tone 1–2:00 to tame banjo brightness) → Longsword (gain backed off — the wall already saturates) |
| **(b) Organ / pad drone** | INST **SYNTH/ORGAN** (drawbar feet, big SUSTAIN) | Microcosm granular / Dark Star V3 smear / Blooper capture-and-layer |
| **(c) GR-300 / SOLO synth lead** | **SYNTH GR-300** (MODE V+D, ENV MOD for wah-envelope, **COMP SW ON** to extend decay) or **SOLO** (FILTER CUTOFF + big SUSTAIN) | the fuzz wall — poly GR-300 chords artifact through the Muff = a feature |
| **(d) Open-tuned / 12-string acoustic** | INST **ACOUSTIC (J-45/D-28)** + **12STR SW ON** + **ALT TUNE Open D/G**, kept pristine | bypass the dirt → Generation Loss → JHS 424 / PORTA424 to degrade |

**Handling banjo's fast decay** (the core problem for sustained patches), in priority order: **SLOW GEAR / SOUND HOLD** FX (violin-swell — removes the attack); the **INST SUSTAIN** parameter (ORGAN/SOLO/CRYSTAL/ACOUSTIC all have it); the **VIO (bowed)** model with LEAD EMPHASIS up; GR-300 **COMP SW ON**; and **volume swells** via an EXP pedal on FV1 (or a wave-pedal auto-swell). For *MIDI* sustain, use the **HOLD** types (§4).

---

## 4. Pitch-to-MIDI craft (drive the samplers from the banjo)

Set **System → GUITAR TO MIDI = ON**. **MONO mode** = one MIDI channel *per string* (consecutive channels, receiver in Mono/Mode-4) → the **Digitakt 2 / Octatrack / MPC** can map a different sound per banjo string with per-string bend; **POLY mode** = all strings on one channel, one timbre, simpler ([vguitarforums-guitar-to-midi](links/vguitarforums-guitar-to-midi.md)).

- **Tame the banjo's spiky triggering:** **PLAY FEEL FEEL3–4** (or NO DYNA + NO-DYNA VELOCITY ~100 for uniform hits), **LOW VELO CUT 2–4** (kills false triggers), **DYNAMICS** for trigger-ease, **BEND RANGE 12–24**.
- **HOLD types are the fast-decay fix for MIDI:** HOLD1 keeps notes ringing across re-picks; HOLD4 = piano-damper behavior.
- **To make MIDI transmit the *retuned* pitches** (not the physical strings), set CONTROL ASSIGN → GUITAR TO MIDI → **ALT TUNE = ON**.
- **Musical uses:** banjo rolls triggering Digitakt drums; the baritone driving an Octatrack/soft-synth pad *under* a live banjo lead. **Latency** is sub-perceptible-but-nonzero (Boss publishes no ms figure — "zero latency" is marketing).
- **USB-C** carries guitar-to-MIDI out + multichannel audio return on one cable (drive MainStage, return audio through the VG outs); full "Re-Guitar" multichannel mode is **not** class-compliant — iOS needs USB GENERIC mode ([vguitarforums-usb-audio-software-instruments](links/vguitarforums-usb-audio-software-instruments.md)).

---

## 5. Patches & the Tone Exchange state (honest)

**Platform reality (dossier corrected):** the VG-800 is **NOT on Boss Tone *Central*** (no official curated bonus banks — the category 404s) but **IS on Boss Tone *Exchange*** (user sharing; `vg-800_guitar` + `vg-800_bass`). Browse/download a *memory* (one patch) or *liveset* (array) inside Boss Tone Studio, then **export to hardware** (not auto-pushed). **The user-patch ecosystem is essentially empty** for this 2025 box — VGuitarForums has only a general-discussion board, no Patch Exchange sub-board, and GT-1000 presets don't port cleanly (the VG-800's single natural-pickup path rejects "kitchen-sink" presets — rebuild manually). **For this rig, author from the factory presets + Tone Studio, not from downloads** ([boss-tone-exchange-vg800-supported](links/boss-tone-exchange-vg800-supported.md); [vguitarforums-vg800-patch-state](links/vguitarforums-vg800-patch-state.md)).

**Bank layout:** **20 banks × 3 factory presets + 30 user banks**, separate for guitar and bass modes; the factory convention is **CTL1 = the patch's performance toggle**. Named factory presets worth raiding (Sound on Sound, quoted): **"24-String Guitar"** (doubled jangle — the alt-tuned-12-string-into-tape template), the **B-Bender** preset (hold CTL1), and the **Organ/Leslie** preset (rotary ramps via CTL1 — the organ-drone template) ([soundonsound-vg800-factory-banks](links/soundonsound-vg800-factory-banks.md)).

> ⚠️ Avoid the **Guitar Chalk** "settings" page — its amp/synth names ("Brit Stack," "Lead Synth," etc.) **don't match any real VG-800 model**; it reads as templated/SEO content. Only its FX *proportions* are usable as directional sanity-checks ([guitarchalk-vg800-settings-caution](links/guitarchalk-vg800-settings-caution.md)).

---

## 6. Power-user tips & hidden features

- **Two amp paths (DUAL):** like the VG-99's Chain A/B — two amps + FX blocks, split by fretboard (low strings = one instrument, high = another) or blended (AB BALANCE). Current firmware restricts which models are selectable in DUAL.
- **Re-routable S/R loop** — place the stereo send/return anywhere in the chain (a post-NAMM addition).
- **Roll-your-own slow-gear:** the synth **RISE/FALL TIME** params build a poly slow-gear/auto-swell.
- **Fine-step editing:** hold the **[SELECT]** knob in and scroll for ±10 increments. **Knob-lock** (press two buttons) for stage safety.
- **Older GK pickups work** via the ~$199 13-pin→Serial converter (gig-proven backup).
- **Patch-organization scheme that works** (Jared Gunston): 7 tuning-banks × {clean / OD / high-gain / lead}, MIDI-PC-switched from an iPad/WIDI; built IR-free for Tone Exchange sharing.

---

## 7. Notable users (honest)

**No verified famous VG-800 user exists** (mid-2026) — Boss launched it without an endorser; NAMM demos are Boss specialists/reviewers. **Heritage/lineage only — do NOT attribute to the VG-800:** Pat Metheny (the Roland **GR-300** the VG-800's GR-300 INST emulates), Andy Summers, Robert Fripp / Adrian Belew, John Petrucci — all *older* Roland GR/VG gear. Useful as "the tradition this box continues," never as endorsers ([vg800-artists-honest-none](links/vg800-artists-honest-none.md)).

---

## 8. Rig-specific recipes & pairings

- **Model → MXR 108 → Hizumitas:** build the model **dark** (Tweed/AC, treble pulled) so banjo/baritone brightness doesn't ice-pick the fuzz; **NORMAL MIX ~20–40%** keeps the real attack/5th-drone/Jazzmaster body under the model.
- **Synth pad / organ drone → Microcosm / Blooper / QI Etherealizer:** continuous synth waveforms are perfect granular/looper food — generate a clean GR-300/ORGAN drone inside the VG-800 and let the End Board chew it.
- **Alt-tuned 12-string → Generation Loss → JHS 424 / PORTA424:** the clean acoustic model gives the tape stage something pristine to ruin.
- **VIO (bowed) → Dark Star V3 / QI:** attackless swell into a smear reverb = a drone machine; double the swell with the instrument volume.
- **Dual Guitar split → CE-2W stereo split → Deco V2:** clean model on the low strings, fuzz-ready on the high strings (or pan them), spread across the stereo split.
- **Pitch-to-MIDI → Digitakt 2 / Octatrack / MPC / H90:** trigger samplers and MIDI-clock effects from the banjo (uniquely available here).
- **Level backstop:** the bench **EHX Effects Interface** is the level-bridge if the VG-800's LINE output is too hot/thin for the instrument-level dirt section.

---

## 9. Best learning resources

- **Marcus Curtis Music** — [the deepest guitar-synth-ecosystem channel](transcripts/marcus-curtis-setup-and-demo.md): firmware/driver/install + GK compatibility + factory-patch tour.
- **Gear Sounds** — [the deepest hands-on menu deep-dive](transcripts/gear-sounds-full-tutorial.md): the DUAL-path + fixed-block + save workflow.
- **JaredGunstonTV** — [real gigging install/workflow](transcripts/jared-gunston-install-gig-presets.md): the 1 mm pickup-height lesson + MIDI-PC patch scheme.
- **Premier Guitar** — [official NAMM first-look](transcripts/premier-guitar-namm-2025.md). **Juca Nery** — [factory-patch catalog + per-patch CTL-1](transcripts/juca-nery-creative-tool-patch-tour.md). **Brett Kingman** — [credible pro "how I'd use it"](transcripts/brett-kingman-how-id-use-it.md) *(no captions — notes)*.
- **VGuitarForums VG-800 board** — the deepest written resource ([calibration](links/vguitarforums-gk5-tracking-calibration.md), [main thread](links/vguitarforums-vg800-main-thread.md), [GUITAR-TO-MIDI](links/vguitarforums-guitar-to-midi.md), [firmware](links/vguitarforums-firmware-lore.md), [vs SY-1000/GP-10/VG-99](links/vguitarforums-vs-sy1000-gp10-vg99.md)). **Sound on Sound** + **MusicRadar** = the two substantive reviews.

---

## 10. Common pitfalls / gotchas

- **Calibration is the whole game** — default sensitivity wobbles on low strings; per-string SENS/DISTANCE setup is mandatory (and the *only* tracking fix — there's no firmware latency patch).
- **Amp-models-into-a-real-amp = harsh digital** — go LINE/PHONES (direct), or FX-BYPASS and feed real amps the raw model.
- **FX routing is constrained** — only FX1–3 + the S/R loop move; CHO/DLY/REV are fixed on/off. A stereo-collapsing block downstream silently kills upstream per-string PAN.
- **No onboard expression treadle / disputed GK-5 controls** — add an EV-30/FV-500 for wah/volume/swells. *(Note: my agents disagreed on whether the GK-5 has S1/S2 switches — the dossier says no, one video claimed the install kit does; verify on the physical pickup.)*
- **Serial GK only** — the GK IN needs a BGK serial cable, never a guitar or 13-pin cable; the GK-5 won't fit traditional Tele bridges (irrelevant here) and its cable is slightly short for some rear mounts.
- **Tone Studio export** — edits must be explicitly "Export to VG-800" or they're lost; **ALT TUNE affects MIDI out** (set the assign if you want physical-string MIDI).
- **Banjo is off-label** — the 5th string usually won't track cleanly in the model; plan to exclude it and keep it via NORMAL MIX.
- **Auto-off ~20 min** (turn off for studio); operating mA not published (give it a generous isolated slot).

---

## 11. Captured sources

**Rig-specific calibration profiles** (`research/`):
- `calibration-banjo-EBM5.md` — full GK SET profile (slot 1): per-string SENS method, the 5th-string-drone workarounds, SCALE/DISTANCE/GAIN starting points.
- `calibration-baritone-JM.md` — full GK SET profile (slot 2): low-string wobble fix, subterranean tuning, shared MIDI logic.

**Transcripts** (`research/transcripts/`):
- `gear-sounds-full-tutorial.md` — Gear Sounds — deepest hands-on navigation; fixed-block + DUAL-path + save.
- `marcus-curtis-setup-and-demo.md` — Marcus Curtis Music — firmware/driver/install + GK compat + factory tour *(the dossier's tIY4F3b0zDA, correctly attributed to Marcus Curtis)*.
- `jared-gunston-install-gig-presets.md` — JaredGunstonTV — the 1 mm pickup-height lesson + gig MIDI automation.
- `premier-guitar-namm-2025.md` — Premier Guitar — official architecture rundown.
- `juca-nery-creative-tool-patch-tour.md` — Juca Nery — factory-patch catalog + per-patch CTL-1.
- `brett-kingman-how-id-use-it.md` — Brett Kingman — pro "how I'd use it" *(no captions — notes)*.

**Links** (`research/links/`):
- `vguitarforums-gk5-tracking-calibration.md` — per-string SENS method (~75% bar), DISTANCE, false-trigger params.
- `vguitarforums-vg800-main-thread.md` — hidden features, gotchas, GT-1000/VG-99/SY-1000 verdicts.
- `vguitarforums-guitar-to-midi.md` — mono vs poly, consecutive channels, ALT-TUNE-to-MIDI, HOLD/velocity.
- `vguitarforums-usb-audio-software-instruments.md` — USB audio + MIDI round-trip routing, class-compliant vs Re-Guitar.
- `vguitarforums-firmware-lore.md` — v1.02-only; the latency-fix claim refuted (GM-800 mixup); the `.bin` unzip gotcha.
- `vguitarforums-vs-sy1000-gp10-vg99.md` — owner comparison verdicts.
- `vguitarforums-gotchas-output-modes.md` — output/tuner modes, cable rules, Tone Studio export gotcha.
- `vguitarforums-vg800-patch-state.md` — no Patch Exchange board yet; memory-vs-liveset terminology.
- `boss-tone-exchange-vg800-supported.md` — VG-800 (Guitar & Bass) IS on Tone Exchange; download mechanism.
- `boss-tone-central-no-vg800.md` — VG-800 NOT on Tone Central (no official curated banks).
- `soundonsound-vg800-factory-banks.md` — bank structure + named presets (24-String, B-Bender/CTL1, Organ-Leslie).
- `guitarchalk-vg800-settings-caution.md` — five recipes, flagged LOW reliability (fake model names).
- `vg800-artists-honest-none.md` — no verified VG-800 artist; GR-300/V-Guitar lineage = heritage only.
- `boss-gk-series-ultimate-guide.md` — the divided-pickup mechanism + GK-5 install/shims.
- `goldtone-ebm-5-pickup-config.md` — confirms solidbody banjo (mount feasibility) + 5th-string geometry.

## Sources

All claims above cite a captured file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`VG-800-DeepResearch.md`](VG-800-DeepResearch.md); manuals are in `manuals/` (Quick Start, Reference, Parameter, BTS).

> **Honest coverage notes:** good video + forum coverage for a 2025 box, but **no dedicated GK-5-calibration video, no banjo video, and no deep Tone Studio patch-build video exist** — those live in the manuals and the VGuitarForums board. Most calibration specifics are inherited from **GM-800** threads (identical GK-5/Serial-GK platform), flagged throughout. Banjo use is off-label, so the calibration *numbers* and 5th-string strategy are reasoned inference (verify by ear); the parameter names/ranges are manual-verified. Reddit/gearspace/thegearforum 403'd; VGuitarForums + BOSS support carried the load. **No user-patch ecosystem and no famous users exist yet** — author your own, honestly.
