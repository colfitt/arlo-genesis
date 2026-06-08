# Elektron Octatrack MkII — Usage Guide

How to *actually* get great results from the Octatrack in this rig, to complement the spec/reference dossier in `Octatrack-MkII-DeepResearch.md`. It is the rig's **live-mangling + resampling + 8-track-sequencing brain** — it lives downstream on the desk, eats the pedalboard's stereo print (fuzz walls, banjo loops, degraded tape), and re-sequences it into something the guitar never played. Three truths govern everything: **read Merlin's Guide before you touch it** (it's the box that punishes feature-by-feature learning); the **Thru machine turning the OT into a live stereo FX processor on the pedalboard is the killer rig integration**, and its real latency is **~1.5 ms** (the "OT latency" reputation is DAW buffer-stacking, not the box); and the **crossfader is the performance** — scenes morph a static drone into a played gesture.

> Captured this wave (second pass, 4 agents — the rig-central centerpiece treatment): **8 video transcripts + 40 distilled links = 48 artifacts** (see §12). All video attributions verified via `yt-dlp --print channel`. One dossier correction folded in (§7 artist list split into *verified* vs *name-dropped* — the standard lists over-attribute). Coverage honesty: the OT is the **single deepest subject on Elektronauts**, so written/forum/video coverage is excellent and easy to corroborate — but the deepest *official* video material (Dataline "Live Resampling," Thavius Beck's "Elektron 203") is **paywalled**, and free turnkey *projects* are scarce (the CF-card workflow discourages sharing; EZBOT's paid templates are the polished ones).

---

## 1. Essential workflows — tame the curve first

**Read [Merlin's Guide](https://www.elektronauts.com/t/a-polished-version-of-merlins-ot-guide-here/42860) first** — "the manual that explains the manual." It builds the OT from first principles and fixes the confusions that sink people ([links/merlin-guide-key-teachings.md](links/merlin-guide-key-teachings.md)). The mental models that matter:

- **Parts hold the SOUND; patterns hold the SEQUENCE.** A Part = machine assignments + FX + scenes + track params + LFOs + which samples are assigned; a pattern is just trigs/p-locks/length/tempo that *points at* a Part. **"I tweaked one knob and every pattern changed" = you edited the shared Part.** Hierarchy: **Set → Project → Bank (16/project) → 4 Parts + 16 Patterns per bank**. Save Parts and Projects deliberately — only the active bank survives power-off otherwise.
- **Flex vs Static:** **Flex = sample in RAM** (the malleable one — live buffers, loops you slice/timestretch/scrub); **Static = streamed from the CF card** (long material to 2 GB — backing drones). Same mangle params, different storage.
- **Sample SLOTS vs the 8 RECORDER BUFFERS — the distinction that unlocks resampling.** You don't record "into a slot"; you record into a track's **recorder buffer** (RECORDER1–8, at the top of the Flex slot list), then assign that buffer to a Flex machine to play/mangle it.
- **The 3-stage gain model** (why "it's not getting louder"): **AMP-page VOL** (per-trig, p-lockable) → **track LEVEL** (the channel fader) → **scene XVOL/XLV** (crossfader-morphed) → main MIX. If a change isn't doing what you expect, you're at the wrong stage.
- **Start small:** one track, one sample, one pattern; get the LEVEL/AMP/FX flow on a single Flex machine before adding tracks; **use scenes to evolve a Part rather than constantly switching patterns** ([links/elektronauts-parts-banks-patterns-model.md](links/elektronauts-parts-banks-patterns-model.md)).

**Sampling basics** ([transcripts/cuckoo-ot-tutorial-02-sampling.md](transcripts/cuckoo-ot-tutorial-02-sampling.md)): crop to a zero-crossing (white square; hold **[FUNC]** to snap); **QUICK CREATE SLICE GRID** → SLICES on → keyboard = SLICE mode; **TIMESTRETCH=AUTO** (short=off, long=on; force off for vari-speed); **CALCULATE BPM FROM SECTION** locks a free loop to project tempo. Two saves: SAVE AND ASSIGN SAMPLE per buffer, then PROJECT → SAVE.

---

## 2. Live-mangle the pedalboard — Thru machines (the centerpiece)

The rig-defining role: the pedalboard's stereo fuzz wall flows live through the OT's FX and the crossfader morphs clean ↔ destroyed. Full recipe in [links/rig-recipe-mangle-fuzz-wall.md](links/rig-recipe-mangle-fuzz-wall.md), setup in [links/thru-machine-live-fx-setup.md](links/thru-machine-live-fx-setup.md).

- **Routing:** pedalboard stereo print (Board 3's 424/PORTA424 stage L/R) → OT **inputs A/B**; **MIXER DIR AB = 0** (DIR up = dry passthrough that *bypasses the FX blocks*); AB GAIN so the `<REC>` LEDs sit healthy, not clipping.
- **Track 1 = Thru machine, INAB = A B**, one sample trig on step 1 — **the Thru track passes no audio until triggered** (the gotcha everyone hits); alternatively hold **[TRACK 1] + [PLAY]** to process with the sequencer stopped. The Thru *track* (not raw DIR) is the goal because only it gets the two FX blocks, scenes, mutes, and is sampleable.
- **FX:** FX1 = multimode filter / Lo-Fi, FX2 = **Echo Freeze Delay** (tempo-synced); **LFO 1 → FX1 cutoff**, slow triangle = the wall breathes.
- **Need more than 2 FX?** Stack **Neighbor machines** on tracks 2/3/4 (Neighbor can't sit on track 1 or 5) → up to **8 serial FX** on the live wall. Neighbor is **series when routed to MAIN, parallel/phasing when routed to CUE** — route intermediate stages to MAIN ([links/elektronauts-neighbor-machines.md](links/elektronauts-neighbor-machines.md), [links/int-ot-effects-processor-neighbor-chain.md](links/int-ot-effects-processor-neighbor-chain.md)).
- **Latency truth:** OT input→output is **~1.5 ms / 64 samples** — inaudible for live playing. The infamous "OT latency" complaints are DAW round-trip buffer stacking, not the hardware. Monitor *through* the OT and **pick one monitor path** (don't run DIR-dry + Thru-processed together → comb-filter phasing) ([links/elektronauts-thru-pickup-latency.md](links/elektronauts-thru-pickup-latency.md)).

---

## 3. Pickup machines — live-loop the rig

Capture banjo/fuzz-wall loops live, synced to the project, then re-pitch/slice them ([links/pickup-machine-live-loop-setup.md](links/pickup-machine-live-loop-setup.md), [transcripts/cuckoo-ot-pickup-machine-loopbox.md](transcripts/cuckoo-ot-pickup-machine-loopbox.md)).

- **RECORDING SETUP** for looping the banjo (EBM-5 → GK-5 → VG-800): **INAB = A B, RLEN = MAX, TRIG = 1 2 (ONE2), LOOP = ON, FIN/FOUT = 0.063, AB = 127** (direct monitor), PITCH = 0 / DIR = FWD / **OP = DUB**; **QREC/QPLL = PATTERN LENGTH**. First loop = master (sets the length), the rest are slaves at LEN factor **X1 (phase-locked) / X2 (double)**.
- **Overdub order that avoids clicks:** REC1 to start → REC1 again to set length + overdub → REC2 keeps it playing. **Triple-tap REC1 = record-while-erase.** Long loops need **dynamic recorders** — bump **RESERVE LENGTH** (PROJECT → SYSTEM → MEMORY) above the 16 s default (changing the mem config needs a power-cycle).
- **Hands-free foot control** (the OT is on the desk while you play standing) — MIDI note map on the auto channel: **C60 = rec/overdub, E64 = play/stop, B71 = sync-seq-to-loop, A69/G#68 = prev/next track** ([links/pickup-foot-control-rig.md](links/pickup-foot-control-rig.md)).
- **⚠️ The clock rule:** Pickup overdub is unreliable when the OT is **MIDI-slaved** — **if you live-loop, the OT must be clock master** ([links/elektronauts-pickup-machine-looping.md](links/elektronauts-pickup-machine-looping.md)).

---

## 4. Resampling & the master track

Sample the pedalboard print, slice it, and re-sequence it into something the guitar never played ([links/resample-the-rig-master-track.md](links/resample-the-rig-master-track.md), [transcripts/ezbot-ot-fastest-resampling.md](transcripts/ezbot-ot-fastest-resampling.md)).

- **Set Track 8 = MASTER** (PROJECT → CONTROL → AUDIO) — global FX/level glue on the whole mix (incl. DIR inputs), no cue out, unaffected by mutes.
- **The fast capture:** **[FUNC]+[REC]** → REC SETUP → **SRC3 = T8** (whole mix) *or* **DESTINATION = CUE** (selective stem); deselect inputs A–D; **QUANTIZE RECORD = PATTERN LENGTH**; hit **[REC3]**. Then **[FUNC]+[REC3]** → EDIT/SAVE THIS RECORDING. For live capture use a **one-shot recorder trig (FUNC+TRIG)**, not a continuous one.
- **Re-sequence it:** QUICK CREATE SLICE GRID, then **CREATE RANDOM LOCKS** and/or **STRT + PITCH p-locks** to scatter the wall/banjo into a new line. Buffers are **volatile — Save** (SAVE AND ASSIGN). BPM-sync via ATTRIBUTES ORIGINAL TEMPO + TSTR = AUTO.
- **⚠️ Master-compressor trap:** resampling through track 8 re-compresses (audible level jump). Resample via **CUE**, or scene-lock the master Comp **MIX = 0**. Always set the captured track **LEVEL = 127** to avoid generation-loss attenuation ([links/elektronauts-resampling-master-track.md](links/elektronauts-resampling-master-track.md)).

---

## 5. Scenes + crossfader — the performance

Scene A = clean, Scene B = changes (hold **[SCENE B]** + tweak any param to lock it); the fader interpolates every locked param, and **scene locks override p-locks during a fade** so transitions stay smooth ([links/rig-crossfader-scenes-performance.md](links/rig-crossfader-scenes-performance.md), [transcripts/voltagectrl-ot-crossfader-demystified.md](transcripts/voltagectrl-ot-crossfader-demystified.md)).

- **Equal-power, no center dip:** lock **XLV/XVOL** opposite per track — Track 1 XLV = MAX@A / MIN@B, Track 2 XLV = MIN@A / MAX@B → A = clean wall only, B = mangled capture, center = blend.
- **Named moves:** drone swell, filter sweep, **stutter/collapse**, clean↔destroyed capture, A/B two-feed mix, and **slice-morph** (STRT SL1 ↔ SL16).
- **Controlled randomness:** scene-lock an LFO's **depth** (random/square shape) onto filter cutoff/pitch — chaotic but always musical.
- **Beat-repeat:** a master delay with **LOCK ON, SEND → 0, FEEDBACK up** (127 = infinite freeze). **Leapfrog trick:** reassign the off-side scene mid-fade to walk through many states from one fader throw. **DELAY CONTROL** keyboard mode rides delay time live.

---

## 6. Signature techniques & shared projects

**Off-the-shelf projects** ([links/template-ultimate-ot-fx-performance-mixer.md](links/template-ultimate-ot-fx-performance-mixer.md), [links/project-sharing-hubs.md](links/project-sharing-hubs.md)):
- **EZBOT "Performance Mixer / Ultimate FX Template"** — the best off-the-shelf match for this rig's goal (OT as live FX mixer for the pedalboard): **64 FX across 4 Parts (Space/Build/Crush/Party), 2 loopers, comp per input pair A/B + C/D, freeze-delay on tracks 1 & 5, sidechain**, unity-gain captures. Paid (Ko-fi/Patreon).
- **EZBOT "Hyper FX Template"** — punch-in FX as an instrument (Beat Repeat/Stutter/Stretch ×4, Master Looper, tape-stop, Reverse). Requires RECORD QUICK MODE.
- **Honest reality:** free turnkey OT *projects* are scarce — the reliable polished ones are paid. Free value = recipes + **sample chains**: build `chain.wav` + its companion `.ot` slice file with **DigiChain** (free, web) or **OctaChainer** (free desktop) ([links/samplechain-tools-roundup.md](links/samplechain-tools-roundup.md), [links/samplechain-octachainer-tool.md](links/samplechain-octachainer-tool.md)).

**Copyable signature techniques** ([links/patch-signature-techniques.md](links/patch-signature-techniques.md)): Cortini's "32 samples → a whole set via scene + PTCH"; Panda Bear's "7 stems + track 8 master, DJ the stems"; Stimming's OT-as-mixer (A/B + C/D, **Thru DIR=0 vs straight DIR=127**); Mumdance's one-shot live build; Surgeon's hands-on/no-menu (external knob box). **Ambient/drone** ([links/template-ambient-drone-looping-techniques.md](links/template-ambient-drone-looping-techniques.md), [links/elektronauts-drone-ambient-recipes.md](links/elektronauts-drone-ambient-recipes.md)): CHAIN BEHAVIOUR silence-off, **polymetric track lengths at 30–60 BPM**, click-avoidance via long-attack env / a silent Pickup loop / external reverb (per-track FX cut when the Part changes).

---

## 7. Power-user tips & hidden features

- **LFO on STRT** scrubs through a sample/chain for endless variation; **slide trigs on RATE** = tape-stop / PIPO vari-speed ([links/elektronauts-hidden-features-tricks.md](links/elektronauts-hidden-features-tricks.md)).
- **The dice** (**[TRACK PARAM] + [YES]**) randomizes the page — instant happy-accidents that fit the aesthetic.
- **Crossfader → retrig:** RTIM steps are chromatic semitones; map retrig to the fader for pitched stutters.
- **Hold [SCENE B] + tap scene pads** to play scenes like keys.
- **PART RELOAD** to undo a jam and snap back to the saved Part.
- **Conditional / probability trigs + micro-timing** on the Thru track gate the incoming wall rhythmically (the stutter variant of §2).

---

## 8. Notable users & techniques (honest)

The OT has a **genuine, deep live-performance following** — unusual for a sampler this hard — skewing techno/experimental/ambient. The well-documented anchors (verified — see [links/artist-verification-roundup.md](links/artist-verification-roundup.md)):
- **Alessandro Cortini** (NIN) — crossfader+scenes for chords from ~32 Buchla samples ([links/artist-alessandro-cortini.md](links/artist-alessandro-cortini.md)).
- **Panda Bear** — two units, "DJ the stems" live ([links/artist-panda-bear-dj-the-stems.md](links/artist-panda-bear-dj-the-stems.md)).
- **Stimming** — rebuilt his live show around two OTs, one as the mixer ([links/artist-stimming-dual-octatrack.md](links/artist-stimming-dual-octatrack.md)).
- **Mumdance** — 100%-live one-shot track-building with a TR-909 ([links/artist-mumdance-live-improv.md](links/artist-mumdance-live-improv.md)). **Surgeon** — OT foundation + Faderfox ([links/artist-surgeon-live-techno.md](links/artist-surgeon-live-techno.md)). **Kangding Ray** — *mostly verified*.

> ⚠️ The standard online lists over-attribute. **Name-dropped without evidence** (don't repeat as fact): The Haxan Cloak, Terence Fixmer, Jacques Greene, Shifted, Paul Birken, James Ruskin & Mark Broom; **Karenn** is flagged as possibly abandoned. Dossier §7 has been patched to reflect this.

---

## 9. Rig-specific recipes & pairings

- **Live-mangle the fuzz wall** → §2 + [links/rig-recipe-mangle-fuzz-wall.md](links/rig-recipe-mangle-fuzz-wall.md). Sustained fuzz/drone is *ideal* OT food (dense, no transient gaps) — freeze-delay and filter sweeps stay smooth.
- **Loop the banjo and re-sequence it** → §3/§4 + [links/rig-recipe-loop-resequence-banjo.md](links/rig-recipe-loop-resequence-banjo.md): Pickup-capture a banjo phrase, slice-grid it, CREATE RANDOM LOCKS → a line the banjo never played, under a live lead.
- **OT as the rig's master sampler/mixer** → [links/rig-recipe-ot-master-sampler-mixer.md](links/rig-recipe-ot-master-sampler-mixer.md): inputs A/B + C/D as channels, Thru tracks with FX, track 8 master glue, scenes for live mix moves.
- **Clock & MIDI topology** → [links/clock-topology-ot-61sl-digitakt.md](links/clock-topology-ot-61sl-digitakt.md), [links/clock-ot-sequences-vg800-cb.md](links/clock-ot-sequences-vg800-cb.md): the OT is **DIN-only (no USB MIDI / no Overbridge)** — one OUT carries clock + transport + 8 MIDI tracks. **Default: OT as clock master**, daisy-chained Digitakt 2 → CB stack → Microcosm/Chroma/H90 → VG-800; **slave it when the 61SL MkIII conducts** (ties to the 61SL's `int-recipe-elektrons-mpc`). OT MIDI tracks sequence the VG-800 (notes/PC/CC) and automate CB pedal CCs. Channel hygiene: audio-track ≠ MIDI-track ≠ slaved-gear channels; don't double-sequence.
- **Reamp / print loop** → [links/int-reamp-print-loop-apollo-babyface.md](links/int-reamp-print-loop-apollo-babyface.md): balanced mains + an independent **cue-out** stem to the Apollo x8 / Babyface; hardware-direct reamp (~1.5 ms) beats a DAW round-trip for live work.

---

## 10. Best learning resources

- **Merlin's Guide** — [the on-ramp](links/merlin-guide-key-teachings.md), read first. **Cuckoo** — the canonical video series: [Tutorial #1 basics](transcripts/cuckoo-ot-tutorial-01-basics.md), [#2 sampling](transcripts/cuckoo-ot-tutorial-02-sampling.md), [Loopbox/Pickup](transcripts/cuckoo-ot-pickup-machine-loopbox.md), [Arranger/song mode](transcripts/cuckoo-ot-arranger-song-mode.md).
- **EZBOT** — best *current* performance educator + the widely-used paid templates: [resampling method](transcripts/ezbot-ot-fastest-resampling.md), [techno templates](links/artist-ezbot-templates-techno.md). **VoltageCtrlRtv** — [crossfader/LFO performance](transcripts/voltagectrl-ot-crossfader-demystified.md).
- **For this rig specifically:** [Y thee Asinine's guitar Thru→Neighbor×3→Pickup×2→Master layout](transcripts/ythee-ot-ambient-guitar-looper-fm3.md) is the closest published match to the intended use; [Ron Cavagnaro's "OT as live mixer"](transcripts/cavagnaro-ot-as-mixer-thru-machine-basics.md) is the tightest Thru primer (MkI, but identical engine).
- **Elektronauts** — the deepest written resource on the planet for this box ([Thru](links/elektronauts-thru-machine-live-processing.md), [Pickup](links/elektronauts-pickup-machine-looping.md), [Neighbor](links/elektronauts-neighbor-machines.md), [resampling](links/elektronauts-resampling-master-track.md), [hidden features](links/elektronauts-hidden-features-tricks.md), [clock](links/elektronauts-midi-clock-master-slave.md)). *(Deepest official video — Dataline "Live Resampling," Thavius Beck "Elektron 203" — is paid; not captured.)*

---

## 11. Common pitfalls / gotchas

- **Thru passes no audio until triggered** — put a trig on step 1, or hold [TRACK]+[PLAY] ([links/elektronauts-thru-machine-live-processing.md](links/elektronauts-thru-machine-live-processing.md)).
- **Edit one Part, every pattern sharing it changes** — Parts are shared; **sample slots are project-wide** (reassigning a slot changes it everywhere). Save deliberately; only the active bank survives power-off ([links/elektronauts-parts-banks-patterns-model.md](links/elektronauts-parts-banks-patterns-model.md)).
- **Master-compressor re-compresses on resample** (level jump) → resample via CUE or master Comp MIX = 0; set captured LEVEL = 127.
- **Pickup overdub misbehaves when slaved** → OT must be clock master to live-loop; "DUB ABORTED" + volume creep across dubs are the known pickup quirks.
- **Neighbor can't be on track 1 or 5**; route intermediate FX stages to MAIN (CUE = parallel/phasing).
- **DIR-dry + Thru-processed at once = comb-filter phasing** — pick one monitor path (DIR = 0).
- **Buffers are volatile** — unsaved recordings die on power-off; back up the **CF card before any OS update**, and **never update before a gig**.
- **OS is frozen at 1.40** (Dec 2020 — the last feature update: MIDI Trig Modes, Tempo-per-Pattern, the dice, multi-trig p-lock, Trig Preview); 1.40C ships on current units with no user-facing changes ([links/elektronauts-os-firmware-state.md](links/elektronauts-os-firmware-state.md)).

---

## 12. Captured sources

**Transcripts** (`research/transcripts/`, 8):
- `cuckoo-ot-tutorial-01-basics.md` — the canonical 58-min on-ramp (record→slice→scene→crossfader→freeze→save).
- `cuckoo-ot-tutorial-02-sampling.md` — crop/zero-cross, TIMESTRETCH=AUTO, CALCULATE BPM, two-stage save.
- `cuckoo-ot-pickup-machine-loopbox.md` — definitive live-looping (REC1/REC2 semantics, master/slave, RESERVE LENGTH).
- `cuckoo-ot-arranger-song-mode.md` — song mode rows, "slice everything," 8-arrangement limit.
- `ezbot-ot-fastest-resampling.md` — fastest resampling (REC3, master vs CUE, LEVEL=127).
- `voltagectrl-ot-crossfader-demystified.md` — scene-locked LFOs + beat-repeat via delay LOCK.
- `ythee-ot-ambient-guitar-looper-fm3.md` — the rig's blueprint: Thru→Neighbor×3→Pickup×2→Master guitar layout *(mostly a demo; routing is the payload)*.
- `cavagnaro-ot-as-mixer-thru-machine-basics.md` — tight "OT as live mixer" Thru primer (MkI, identical engine).

**Links** (`research/links/`, 40) — grouped:
- **Forums / Merlin (`elektronauts-*`, `merlin-*`, 13):** merlin-guide-key-teachings · elektronauts-thru-machine-live-processing · elektronauts-thru-pickup-latency · elektronauts-pickup-machine-looping · elektronauts-crossfader-scene-tricks · elektronauts-neighbor-machines · elektronauts-resampling-master-track · elektronauts-project-templates · elektronauts-os-firmware-state · elektronauts-hidden-features-tricks · elektronauts-midi-clock-master-slave · elektronauts-parts-banks-patterns-model · elektronauts-drone-ambient-recipes.
- **Rig integration (`thru-*`, `pickup-*`, `resample-*`, `clock-*`, `int-*`, `rig-*`, 13):** thru-machine-live-fx-setup · int-ot-effects-processor-neighbor-chain · rig-recipe-mangle-fuzz-wall · pickup-machine-live-loop-setup · pickup-foot-control-rig · rig-recipe-loop-resequence-banjo · resample-the-rig-master-track · clock-topology-ot-61sl-digitakt · clock-ot-sequences-vg800-cb · rig-crossfader-scenes-performance · int-reamp-print-loop-apollo-babyface · rig-recipe-ot-master-sampler-mixer.
- **Projects / artists (`template-*`, `samplechain-*`, `project-*`, `patch-*`, `artist-*`, 14):** template-ultimate-ot-fx-performance-mixer · template-ambient-drone-looping-techniques · template-elektronauts-project-templates-thread · samplechain-tools-roundup · samplechain-octachainer-tool · project-sharing-hubs · patch-signature-techniques · artist-alessandro-cortini · artist-panda-bear-dj-the-stems · artist-stimming-dual-octatrack · artist-mumdance-live-improv · artist-surgeon-live-techno · artist-ezbot-templates-techno · artist-dataline-resampling-tutorial · artist-verification-roundup.

## Sources

All claims above cite a captured file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Octatrack-MkII-DeepResearch.md`](Octatrack-MkII-DeepResearch.md); the manual is in `manuals/`.

> **Honest coverage notes:** the richest wave yet on the written side — the OT is **Elektronauts' deepest subject**, so forum/Merlin coverage is excellent and cross-corroborated, and free YouTube fundamentals (Cuckoo) + performance (EZBOT, VoltageCtrl) + a guitar-processing blueprint (Y thee Asinine) are strong. **Gaps:** the deepest *official* video (Dataline "Live Resampling," Thavius Beck "Elektron 203 Advanced Sampling") is **paywalled** and not captured; free turnkey *projects* are scarce (the polished ones are EZBOT's paid templates — captured by spec, not the paid files); a couple of old project download links are stale. **Latency** (~1.5 ms / 64 samples) is a well-regarded single Elektronauts figure (Elektron publishes no official input-latency spec) — directionally reliable and consistent across two independent agents. **Dossier correction:** §7's artist list over-attributed — split into *verified anchors* (Cortini, Panda Bear, Stimming, Mumdance, Surgeon; Kangding Ray mostly) vs *name-dropped/unverified* (Haxan Cloak, Fixmer, Greene, Shifted, Birken, Ruskin & Broom; Karenn possibly abandoned). All 8 video attributions yt-dlp-verified — no mis-credits this wave.
