https://www.chasebliss.com/big-time + Big Time MIDI Manual + rig MIDI files
chasebliss.com + Big Time MIDI Manual + Mark Johnston deep-dive (YT 2kfrZbEbRY8) + rig clock/preset files · accessed 2026-06-03

# Big Time CENTERPIECE — minimal chains IN + OP-1 / Digitakt 2 / MPC integration

The owner's plan: keep the chain INTO Big Time tiny (a fuzz, maybe a glitch pedal) and integrate
it with the OP-1 Field, Digitakt 2, and MPC Sample so the one delay carries songs. This file is
the **wiring + gain-staging + clock/recall** how-to, grounded in gear actually owned.

> **[V]** = verified (product page / MIDI manual / captured transcript / repo MIDI files).
> **[R]** = first-principles reasoning from verified behavior (label honestly — new pedal).

---

## A) Minimal chain — FUZZ → Big Time

### Why fuzz BEFORE the delay (standard, and why it works here)
- **[R/standard]** Gain (fuzz) goes *before* time-based FX: the fuzz makes the big tonal
  statement and the delay repeats a fully-formed wall. Running fuzz *after* the delay distorts
  every repeat into mush — occasionally a deliberate lo-fi trick, but not the centerpiece move.
  (General pedal-order practice; EQD / JHS / Reverb signal-chain guides.)
- **[V]** Big Time's input is an **analog stereo preamp (COLOR) feeding an analog limiter
  (STATE)** — so it is *built* to be driven hard by a hot source. EAE explicitly designed the
  preamp to "sound good on guitar and bass and synthesizers and drum machines" and to be
  "pushed harder than a normal pedal" (Walkthrough/Secret Weapons). A fuzz in front is exactly
  the kind of hot, sustaining source the limiter wants to chew on.

### Gain-staging the fuzz so the wall feeds the delay without mud
- **[R] Keep COLOR modest when a fuzz is in front.** The fuzz already supplies saturation +
  sustain; COLOR then only needs to set how hard that hits the limiter. Too much COLOR + a hot
  fuzz = the limiter clamps/ducks and the repeats turn to porridge. Start COLOR low and bring it
  up until the repeats just begin to compress.
- **[V] Use STATE to decide what the fuzz wall does as it repeats:** **Compressed** keeps a fuzz
  wall articulate and stops runaway (safest under a sustaining fuzz); **Saturated/#!&%** lets the
  repeats break up further for doom. The **TEXTURE** alt tunes the amount (Secret Weapons).
- **[V] Tame mud with TILT EQ + the new repeats' VOICING.** Push **TILT up** to cut lows from a
  thick muff wall so the echoes stay defined (the EQ sits *ahead of* the feedback, so it also
  shapes repeat length — pushing lows up lengthens tails, cutting them tightens). VOICING =
  **Focus** "shaves highs+lows over time → focused floating repeats," ideal for keeping a fuzz
  wall from clouding (Secret Weapons, dossier §13).
- **[R] Level match into a stereo pedal:** the owned fuzzes are **mono** (MXR M173 108, EAE
  Longsword, EQD Hizumitas). Feeding IN-L only auto-engages Big Time's **MISO** (mono-in /
  stereo-out) mode — fine, and a clean way to fan a mono fuzz into a stereo delay field.

### Which owned fuzz for which centerpiece job
- **[V/profile] EQD Hizumitas** (Elk Big Muff Sustainar / Boris-Wata voiced, long sustaining
  wall) → **best for ambient/drone centerpieces.** Its endless sustain means you can hold one
  note and let Big Time's feedback + DIFFUSE build an oceanic bed. Its Filter knob (scooped↔
  thick mids) lets you pre-shape before the delay. **[R]** Pair with STATE Compressed so the
  sustain doesn't run away.
- **[V/profile] MXR M173 Classic 108** (BC108 silicon Fuzz Face, raw/vintage, gated-ish) → best
  for **spitty rhythmic** centerpiece parts; its dynamic, slightly gated decay reads as
  articulate fuzz stabs that Big Time's multi-tap CLUSTER can rhythmically echo. **[R]**
- **[V/profile] EAE Longsword** (high-gain RAT/OCD-family distortion + active EQ + 20 dB boost,
  same builder as Big Time) → **tightest, most controllable** drive; its active EQ + boost let
  you set the exact level slamming COLOR. Natural sibling tone-wise. **[R]** Use its EQ to
  pre-carve mud and its boost to push the limiter into compression on demand.

---

## B) Glitch pairing — Onward / Microcosm with Big Time

The rig owns two glitch boxes: **Chase Bliss Onward** (freeze + glitch sampler-looper) and
**Hologram Microcosm** (granular delay/looper/glitch, 44 engines).

### Glitch → Big Time (stutter/granular INTO the delay) — the default
- **[R]** Put the glitch box **before** Big Time and the delay smears the stutters/grains into
  rhythmic or ambient tails — the glitch supplies the *event*, Big Time supplies the *space*.
  Onward's **glitch side** ("angular, repeating sounds") feeding Big Time's CLUSTER multi-taps
  layers stutter-on-stutter; Onward's **freeze side** ("soft smooth pad that ebbs and flows")
  makes a sustained source for Big Time to wash out (Onward review). Microcosm's granular engines
  into Big Time = granular cloud → delay diffusion.
- **[V] Clock them together** so the glitch timing and delay subdivision lock to the same grid —
  Onward syncs GLITCH timing to MIDI clock, Microcosm auto-engages on MIDI Start, Big Time locks
  its TIME subdivision (see §C). All three on one clock = a coherent rhythmic glitch-delay.

### Big Time → glitch (delay INTO the glitcher) — the alternate
- **[R]** Reverse it and the glitch box **re-chops Big Time's repeats**: freeze a Big Time
  cascade into Microcosm/Onward and granularize/stutter the echo itself. This is the same logic
  as the dossier's Big Time → MOOD micro-loop pairing (§5/§9). Pick one direction per song; both
  feeding each other risks runaway.

### The lean philosophy (fewer pedals, deeper use)
- **[V]** Big Time alone already spans "chorus, flanger, reverb, dirt, compressor/limiter,
  delay, looper" (Secret Weapons). So the honest minimal centerpiece chain is **one drive +
  Big Time + (optionally) one glitch** — three boxes that between them cover dirt, time, space,
  pitch, and stutter. Everything else is recall (presets) and the samplers feeding in. Variety
  comes from Big Time's STATE/VOICING/MODE/SCALE/CLUSTER permutations, not from more pedals.

---

## C) Integration — OP-1 Field / Digitakt 2 / MPC Sample

Big Time is marketed as **"the perfect centerpiece for a synth setup"** thanks to **balanced +
unbalanced stereo I/O** — it's meant to take line-level sources, not just guitar **[V]**.

### Feeding each sampler's output INTO Big Time (levels)
- **[V] OP-1 Field → Big Time:** the OP-1's OUT is **line level** and goes "farty/muddy/quiet"
  straight into instrument-level gear, so route **OP-1 → EHX Effects Interface (line→instrument)
  → Big Time** (the rig's confirmed line-matching path; OP-1 guide §5/§7). Keep it stereo.
  **[R]** Or — because Big Time accepts **line-level/balanced** input and has a **1 MΩ input +
  selectable balanced I/O** + a **DRY CLEAN / KILL DRY** option — you can often feed the OP-1
  more directly than into a fuzz; use **+12 dB** (alt) only if the source is quiet.
- **[V/R] Digitakt 2 / MPC Sample → Big Time:** both put out healthy line level. Feed their
  main (or a selected track/pad) out into Big Time's stereo ins. On the DT2 you can route **one
  track out** (Overbridge "selective USB audio output" or analog outs) so only that part hits
  the delay. **[R]** Set Big Time COLOR low for line sources (they're already hot) and use
  **DRY KILL** (Options) so Big Time returns wet-only into a parallel/aux path — cleanest for a
  centerpiece send.

### Clock-sync — Big Time in the rig's MIDI clock (verified CCs)
- **[V] Big Time takes MIDI on a native 5-pin DIN** (no MIDIBox needed — unlike the other CB
  pedals). Digitakt DIN MIDI OUT → Big Time MIDI IN directly; Big Time **THRU** can hub onward.
- **[V] Digitakt 2 as clock MASTER → Big Time as slave** (the rig's default): DT2 `MIDI CONFIG >
  SYNC` → CLOCK SEND + TRANSPORT SEND ON. On Big Time, **CC111 = MIDI CLOCK IGNORE**
  (FOLLOW = 0, IGNORE = 1+) and **CC54 = subdivision** (0–12 = 1/16…whole). Clock behavior
  depends on SCALE: in **Off/Chromatic** it snaps delay TIME to the incoming quarter note (bend
  TIME without losing tempo); in **Oct+4+5/Octave** quarter-note sits at slider center and you
  move to musical subdivisions above/below.
- **[V] Big Time as clock MASTER → the rig** (when its sequenced SCALE/MOTION pattern should
  drive the groove): set **CC110 = MIDI OUT (OUT = 1+)**; clock range **60–240 BPM** (auto-
  subdivides if out of range). Then the Digitakt/MPC and the CB stack follow Big Time's echoes.
  **Pick ONE master — never loop clock.**
- **[V] ⚠️ MPC Sample:** on fw 1.2.1 the **AC50 distorts kicks/bass when SLAVED to external
  clock** — run the **MPC as master** (and let Big Time follow via CC111) **or** verify a 1.3.x
  fix before slaving it. (MPC guide §5/§7.)

### Recall Big Time presets in time, alongside the samplers
- **[V]** Big Time = **10 onboard + 127 via MIDI** presets; **PC# recalls a slot, PC 0 = LIVE
  (follow the faders)**. Save over MIDI via **CC27** (value = slot #) or **CC28** (save to
  current slot) — hands-free.
- **[V] Whole-stack scene from the DT2/MPC:** put Big Time on the **shared CB channel (default
  ch.2)** and save the *same preset number* per song-section across the CB pedals; one **Program
  Change** from a DT2 MIDI track (fired on pattern change or a trig) jumps Big Time + the whole
  CB board to that section at once. Use distinct channels only if you need per-pedal CC
  automation simultaneously. (cb-stack-preset-scene-recall.)
- **[R] Centerpiece flow:** map song sections (verse/chorus/build) to Big Time presets 1–4, lay
  the matching Program Changes on the Digitakt timeline → the delay re-voices itself through the
  arrangement hands-free while you play over it.

### Rhythmic delay locked to the groove
- **[V/R]** With Big Time following DT2/MPC clock at a chosen CC54 subdivision (dotted-8th,
  16th, etc.), set MODE Short + CLUSTER for multi-taps + STATE Compressed → the delay multi-tap
  pattern locks to the sampler groove. Or p-lock Big Time's knob CCs from the DT2 (COLOR=CC14,
  TIME=CC15 … WET=CC19) for grid-quantized, evolving delay moves even where its own ramp would
  free-run.

### Resampling Big Time back INTO the samplers (generation-loss)
- **[V] OP-1 Field:** sample Big Time's wet output via the EAR/line-in (or out-in loopback),
  drop into the synth/drum sampler, re-print on a Porta/Vintage tape → stacked degradation.
  ~20 s sampler cap; bounce-volume +8 to match (OP-1 guide §1/§5). **[R]** Freeze a Big Time
  drone (hold RIGHT FS), sample the held bed, then play it chromatically on the OP-1.
- **[V] Digitakt 2:** `SAMPLE` → INPUT = MAIN INPUT (or L/R) → record Big Time's output → slice
  (Grid/Slice) → random-LFO → Comb filter → bit-crush → resample again ("recorded-wrong" loop,
  DT2 guide §1/§5). ⚠️ Disable `TO MAIN` while resampling re-amped audio or it feeds back.
- **[V] MPC Sample:** Sample Record → Source = rear inputs (Big Time out) → Chop→Transients →
  re-sequence the slices → bake with vintage emulator/LoFi via **Resample** (⚠️ resample is
  silent on the first try — do it twice; MPC guide §1/§7). DJ-Shadow logic: capture *your* Big
  Time textures as a sample bank nobody else has.

### Handoff chain (sketch → finish), all centered on Big Time
- **[R]** OP-1 sketch → resample into MPC for the beat → Digitakt sequences/clocks the part →
  all of it streams **through Big Time** (as a stereo aux/insert) for the unifying delay
  character → resample the Big Time-treated result back to taste. One delay, the whole song's
  glue.

## Sources
- https://www.chasebliss.com/big-time + https://www.gearnews.com/chase-bliss-big-time/ ("centerpiece for a synth setup," balanced I/O, modes, presets)
- Big Time MIDI Manual (CC110 clock OUT, CC111 clock ignore, CC54 subdivision, CC27/28 save, CC14–19 sliders) — chasebliss.com
- Gear/Chase Bliss Blooper/research/links/cb-stack-clock-sync-per-pedal.md · cb-stack-midi-trs-and-midibox.md · cb-stack-preset-scene-recall.md (verified CB clock/preset model)
- Gear/Elektron Digitakt 2/research/.../rig-dt2-clock-sync-pedals-verified.md (DT2 master, per-pedal sync table)
- OP-1 / DT2 / MPC usage guides (§ integration, levels, resampling) — Gear/TE OP-1 Field/, Gear/Elektron Digitakt 2/, Gear/Akai MPC Sample/
- Owned-pedal profiles: Hizumitas, MXR M173 108, EAE Longsword, CB Onward, Hologram Microcosm (GearProfile.md)
- Captured transcript: centerpiece-mark-johnston-big-time-secret-weapons-deep-dive.md (STATE/VOICING/TILT/COLOR behavior, preamp "sounds good on synths/drum machines")
- Pedal-order practice: reverb.com / jhspedals.info / earthquakerdevices.com signal-chain guides (fuzz-before-delay standard)
