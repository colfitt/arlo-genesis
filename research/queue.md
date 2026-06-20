# Bloop queue

> Ranked research targets. `/bloop` reads the top unchecked **bloop-worthy** entry as a
> candidate, but you always pick. Check a box `[x]` when its bloop is done. Add your own
> targets anywhere — this file is yours to edit.
>
> Seeded: 2026-06-19 by `bloop-gapscan` (8 agents, 59 devices assessed, 10 bloop-worthy).
> The dominant gap: **MIDI-capable gear with no captured CC chart** — ARLO has no control
> surface for those devices. Format template for CC charts: copy Strymon TimeLine / CB Onward.

---

## Completed / in progress

- [x] **Chase Bliss Big Time — layer 1** (2026-06-19) · creative/lineage dive → promoted 3 corrections + 4 new patches (36→40) + GearProfile fill + 8 staged chunks. Digest: `bloops/2026-06-19-chase-bliss-big-time.md`.
- [x] **Chase Bliss Big Time — layer 2** (2026-06-19) · resolved Env mechanics, upgraded the resonator patch, scoped lineage→dialing, fixed 2 more TRS chains. Promoted 2 chain fixes + 2 patch refinements + 3 new link files + 3 link updates + 14 chunks. Digest: `bloops/2026-06-19-chase-bliss-big-time-l2.md`.
- [ ] **Chase Bliss Big Time — layer 3** (seeds, deferred) · (a) transcribe the Object Worship "Goes BIG TIME" launch episode (audio-only) to confirm/refute the BIM benchmark in Snyder's own words; (b) confirm Env pitch direction on hardware (DEPTH above/below TIME); (c) re-sweep owner recipes once units are widely in hand (late June+); (d) reconcile `big-time-env-divebomb-lead.md` "continuous TIME-clock follower" framing vs the manual's transient-triggered description.

## Bloop-worthy (do these)

### [ ] 1 · Chase Bliss MOOD MkII · `gear` · **high**
- **Path:** `gear/Chase Bliss MOOD MkII`
- **Why:** Flagship texture/looping anchor, MIDI-clock-slaved, but `midi:true` + no CC chart (every sibling — Onward/Clean/GenLoss — has one). ARLO can't drive it.
- **Focus:** Capture the official CC chart (CC# → parameter) into `research/links/midi-official-cc-chart.md`, matching the Onward format. Source: bundled MOOD manual PDF + Chase Bliss midi.guide page.
- **Open questions:**
  - Exact CC# for front-panel knobs (Time, Modify, Mix, Loop, MOOD blend) and dual-engine (L/R) params?
  - Which CCs select Loop vs Delay/Reverb modes and DIP-switch hidden options? Per-engine clock-multiplier CCs?
  - Does it follow the standard CB PC preset map + CC bypass scheme? Is the CC table in the PDF or only on midi.guide?

### [ ] 2 · Roland VG-800 · `gear` · **high**
- **Path:** `gear/Roland VG-800`
- **Why:** Deepest, most rig-critical device — the first-slot guitar "brain." `midi:true`, 0 CC/NRPN refs for 150+ params. Official Parameter Guide PDF is **on disk** → extraction, not hunting.
- **Focus:** Extract CC/NRPN map (effects, INST, amp, MEMORY MIDI) + GUITAR-TO-MIDI channel/HOLD/bend settings from `VG-800_parameter_eng02_W.pdf`.
- **Open questions:**
  - Are model params addressed by CC, NRPN, or SysEx — which need SysEx vs simple CC?
  - PC/bank scheme for recalling user MEMORY patches over MIDI?
  - GUITAR-TO-MIDI: which channels do the six strings transmit on; configurable bend-range / HOLD-type values?

### [ ] 3 · Elektron Octatrack MkII · `gear` · **high**
- **Path:** `gear/Elektron Octatrack MkII`
- **Why:** Master sampler/mixer/looper brain with deep MIDI control (track params, scenes, crossfader, machines), `midi:true` / no CC chart. GearProfile is a ~546-byte stub despite 48 links.
- **Focus:** Capture CC chart (audio-track params, crossfader/scene morph, FX1/FX2, machine CC#) + fill the GearProfile role/signature-uses stub.
- **Open questions:**
  - CC# for crossfader + scene A/B morph (the performance moves ARLO would automate)?
  - Which CCs map audio-track playback (pitch, start, length, rate) vs FX1/FX2 per machine?
  - Clock master or slave in this rig — does that change which CCs ARLO sends vs receives?

### [ ] 4 · Elektron Digitakt 2 · `gear` · **high**
- **Path:** `gear/Elektron Digitakt 2`
- **Why:** Clock/sequencer hub with extensive per-track CC control, `midi:true` / no CC chart. GearProfile is a ~545-byte stub despite 31 links.
- **Focus:** Capture CC implementation chart (synth/sample engine, filter, LFO, FX/send, mixer CC#) + fill GearProfile stub.
- **Open questions:**
  - CC# for the DT2 sound engine (amp/filter/LFO) vs the FX send/master block?
  - Which CCs control per-track sample playback + the mixer/compressor?
  - Clock master for the rig? CCs on MIDI tracks vs audio tracks?

### [ ] 5 · Walrus Audio QI Etherealizer · `gear` · **high**
- **Path:** `gear/Walrus Audio QI Etherealizer`
- **Why:** Strongly documented (46KB) but `midi:true` / no CC chart — official table sits on **page 5 of the on-disk manual PDF**, only paraphrased in prose. (Note: expression flag already correct — do NOT touch.)
- **Focus:** Extract CC chart (CC#, parameter, value/range) from manual p.5 + PC preset map + channel-assign procedure. Fill role-in-rig (grain-freeze pad → reverb).
- **Open questions:**
  - Exact CC# + ranges for Flow/Mix/Tone/Space, engine-mode selector, Freeze, oscillation?
  - PC preset map + procedure to set MIDI receive channel?
  - Bypass + Tap on dedicated CCs? Does Freeze latch or momentary over MIDI?

### [ ] 6 · OBNE Parting · `gear` · **high**
- **Path:** `gear/OBNE Parting`
- **Why:** Generative delay/reverb, MIDI-clock-syncable, deep 45KB research — but the CC table is genuinely uncaptured (only CC 27 Volume + CC 102 channel documented; §12 just *claims* full CC).
- **Focus:** Capture full CC map (Rate, Depth, Shape, Chance, Smear, Glitch, Dissolve, Time, Filter, Mix + switches, PC presets, clock-mode CCs).
- **Open questions:**
  - CC# for the generative controls (Chance, Smear, Glitch, Dissolve) — the pedal's character?
  - Which CC selects clock mode; tempo mult/div values?
  - PC preset count/scheme; CCs for bypass + routing/trails switches?

### [ ] 7 · Strymon Big Sky · `gear` · **high**
- **Path:** `gear/Strymon Big Sky`
- **Why:** Designated H90 MIDI failover — its whole value depends on PC/CC recall. CC table is only a **pointer** to midi.guide, not transcribed. Failover bank can't be pre-mapped without it.
- **Focus:** Transcribe full CC/NRPN map + 300-preset PC/bank scheme. Source: midi.guide/d/strymon/bigsky + Strymon manual.
- **Open questions:**
  - PC/bank scheme across 300 presets (CC#0 bank-select boundaries)?
  - Which CCs select the 12 reverb machines + per-machine PARAM/decay/mix?
  - CCs for global controls (infinite hold/sustain, kill-dry, bypass) for the failover role?

### [ ] 8 · OBNE Dark Star V3 · `gear` · **high**
- **Path:** `gear/OBNE Dark Star V3`
- **Why:** MIDI preset reverb (Board-2 terminus). CC data exists in prose (~11 CCs) but not as a structured chart ARLO can consume. (Note: midi flag already correct — do NOT re-fix.)
- **Focus:** Normalize the prose CC list into a complete structured chart (all knobs + switches/routing/trails + PC presets) + fill GearProfile role/signature-uses.
- **Open questions:**
  - Beyond the ~11 named knob CCs, which cover switches (routing, trails, pitch mode) + bypass?
  - 127-preset PC scheme — is bank-select needed?
  - Are the two Pitch CCs (16/17) continuous or stepped intervals over MIDI?

### [ ] 9 · Hologram Chroma Console · `gear` · medium
- **Path:** `gear/Hologram Chroma Console`
- **Why:** Anchor texture pedal with a **partial** CC chart — the primary-knob rows (TILT/RATE/TIME/AMOUNT×4/MIX) and v1.04 per-module bypass/engage CCs are NOT transcribed. Targeted top-up.
- **Focus:** Complete the existing chart from `chroma-console-midi-cc-implementation-manual.md` / on-disk manual.
- **Open questions:**
  - Actual CC# for TILT/RATE/TIME, the four AMOUNT knobs, MIX?
  - Which CCs added in v1.04 for per-module bypass/engage — one per module slot?
  - Are PRE/POST routing + dual-bypass also CC-addressable?

### [ ] 10 · Neural DSP — Parallax X · `software` · medium
- **Path:** `software/Neural DSP`
- **Why:** The one genuine thin-multi-product **software** gap. The 14KB UsageGuide covers 2 of 3 owned plugins; Parallax X (installed bass-amp plugin) has **0 mentions**.
- **Focus:** Document Parallax X — amp/cab/FX architecture + 2-3 rig recipes (sub-bass drone walls, baritone low-end, reamping DI bass); how it complements Nolly X.
- **Open questions:**
  - Parallax X signal chain (amp models, cab/IR, built-in FX) — which controls matter for ambient/drone bass?
  - Concrete starting settings for a sub-bass drone wall vs defined baritone low-end?
  - How to divide low-end duties between Parallax (bass) and Nolly X (baritone)?

---

## Low priority / optional polish

- **[ ] 11 · Strymon Iridium** (`gear`) — near-complete CC list already inline; benched amp/cab modeler. Optional: promote inline list → full table (incl. fw1.19 CC#9 volume).
- **[ ] 12 · Chase Bliss Lost & Found** (`gear`) — only CB pedal missing the standard `midi-official-cc-chart.md`; MIDI Manual PDF on disk. Transcribe to match sibling format. (Don't chase artist/recipe coverage — corpus correctly notes none exists yet for this Sept-2025 small-batch run.)
- **[ ] 13 · Hologram Microcosm** (`gear`) — anchor; CCs already documented but live in prose. Optional consolidation into one chart file.
- **[ ] 17 · Eventide H90** (`gear`) — best-documented device; CC info scattered across links. Optional consolidation for parity with TimeLine/Onward.

---

## Chores (NOT bloops — flag/data hygiene)

- **[x] Big-Time MIDI-connector sweep** (done 2026-06-19) — all genuine instances fixed: `two-clock` (L1), `frozen-bed` + `onward-glitch` (L2). `clean-big-time-mood-dry-lead` was a **false positive** — its "TRS" refers to MOOD's MISO audio jacks, not Big Time MIDI. Corpus now clean of the error.
- **[ ] Strymon Deco V2** — `ccChart:0` is a **false negative**; a complete CC 0-100 table + 300-preset scheme already exists in `links/strymon-deco-v2-manual-revd-secondary-midi.md`. Flip the flag / normalize filename. No research.
- **[ ] Corpus-wide ccChart false-negative sweep** — Deco V2 proves the heuristic mislabels. Re-scan for other devices whose chart exists but flag says 0.
- **[ ] Batch GearProfile fill** — nearly every GearProfile has unfilled "Why I have it" / "Signature uses" placeholders while the content sits in DeepResearch. A single batch pass clears this corpus-wide (Digitakt 2 + Octatrack MkII stubs are the worst — fold into ranks 3-4).

---

## Not in queue (verified well-documented — for reference)

Strymon TimeLine, CB Blooper/Onward/Big Time/Brothers AM/Clean/Generation Loss = reference-standard CC charts (use TimeLine/Onward as the format template). Non-MIDI drives/fuzzes/utilities correctly have no CC gap. OP-1 Field + MPC Sample are note/clock sources, not CC surfaces. Software is healthy (18/19 correctly shaped).
