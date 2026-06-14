# Matrix-12 V2 — Usage Guide

The Oberheim Matrix-12 is the deepest evolving-texture machine in the bundle: **12 voices, 2
VCOs + 5 DADSR envelopes + 5 LFOs per voice**, a **15-mode filter**, and a **modulation matrix
of 40 slots (27 sources → 47 destinations, up to 6 modulators on one parameter).** For this rig
it's the patient drone/pad synth — set conflicting unsynced modulators and it never audibly
repeats — and its keyboard-tracked self-oscillating filter is a tuned drone tone in itself.
It's also the heaviest to program and ~30% CPU at idle, so **freeze early**.

---

## 1. Architecture (what you're steering)

- **Per voice:** 2 VCOs (saw/tri/pulse+PWM; VCO2 adds noise, is the FM source + sync slave) →
  15-mode filter → **2 VCAs**. ⚠️ **VCA2 is gated by Env2 — if you delete that matrix routing
  the patch goes silent** (the #1 "dead patch" trap). Controls run **0–63** (PW 31 = center).
- **Mod generators per voice:** 5 DADSR envelopes, 5 LFOs (incl. noise + S&H), vibrato gen, 3
  tracking gens, 4 ramp gens → the **matrix**.
- **15 filter modes:** 4 LP (1–4 pole), 3 HP, 2 BP, notch, **phase/all-pass (a built-in
  phaser)**, + 4 combo modes. Resonance to max **self-oscillates and tracks the keyboard** →
  playable tuned drone. Lore: **3-pole LP often beats 4-pole for pads**; the HP is unusually
  good for thinning a pad to sit under a lead.
- **FM** is hardwired to VCO2's triangle → gate to VCO1 (audio-rate pitch FM, bell/gritty) or
  to VCF (cutoff motion; slow VCO2 right down for irregular bubbling).
[transcripts/matrix12-omahs-pt1-oscillators.md; transcripts/matrix12-omahs-pt2-filters-fm.md; links/matrix12-sos-sounddesign-multimode-cpu.md]

---

## 2. Signature settings — evolving drones

- **Native "never-repeats" routing (deeper than the Advanced panel):** in the matrix set
  **LFO1 → LFO2's rate** (nested) and **an envelope → LFO1's rate** (self-modulation), then route
  those LFOs to cutoff / VCO detune / pan at slow **freerun** speeds (note-on doesn't reset) →
  cycles never align. Use the **DADSR delay stage** for long swells. [links/matrix12-vse-xpander-tips-tricks.md; links/matrix12-musicradar-character-notable-users.md]
- **Keyboard-tracked self-oscillating filter** as a drone tone layered under the oscillators.
- **24-oscillator wall:** all 12 voices on one zone, **Unison** mode, each voice slightly
  detuned + panned, some ±1 octave (12 voices × 2 VCOs = 24 osc). [transcripts/matrix12-glen-darcey-pt2-fx-voices-multi.md]

---

## 3. Rig-specific recipes

- **Into the degrade chain:** Matrix-12 pad → **Decapitator** (Punish for grit) → **SketchCassette
  / RC-20** (wow/wobble) → **Valhalla VintageVerb/Room** → **EchoBoy**. Pre-thin with the good HP
  filter so the pad sits under banjo/baritone without mud.
- **Single-note drone-chord under a lead (the Brecker "Original Rays" trick):** per-voice
  transpose builds a chord from one held note — Zone 1 root; Zone 2 +5/+4/+2; Zone 3 octave-down
  −5/−4/−2 → a sustained MIDI note voices the whole drone-chord while you play banjo on top. [transcripts/matrix12-glen-darcey-pt2-fx-voices-multi.md]
- **Wall:** the 24-osc unison recipe, or a Multi-mode 6+6 split with zone 2 detuned, spread
  across the stereo field (per-voice pan / Rotate) for self-animating width.
- **Logic AU / freeze:** loads under AU Instruments → Arturia. **~30% CPU at idle** (5 LFOs + 5
  envs/voice always run) → **freeze/bounce pads early**; 44.1 kHz / lower oversampling for big
  Multis. [links/matrix12-sos-sounddesign-multimode-cpu.md]

---

## 4. Notable users & techniques

**Steve Roach** (deep ambient/drone) and **The Orb** are the genuinely rig-relevant anchors;
also Vangelis, Brad Fiedel (Terminator), Michael Brecker, and "many a Hollywood sound
designer." **Honest flag: no shoegaze/doom/slowcore artist documented on a Matrix-12** —
relevance is by technique. [links/matrix12-musicradar-character-notable-users.md]

## 5. Pitfalls / gotchas
- **Env2→VCA2 is load-bearing** — don't delete it.
- High baseline CPU even idle → freeze early.
- Slowest synth in the bundle to program; "just because you could use all 40 slots didn't mean
  you had to" — a few slow modulators beat a maxed matrix.

## 6. Captured sources & QC
- Transcripts: `matrix12-omahs-pt1-oscillators`, `matrix12-omahs-pt2-filters-fm`, `matrix12-glen-darcey-pt2-fx-voices-multi`
- Links: `matrix12-sos-sounddesign-multimode-cpu`, `matrix12-vse-xpander-tips-tricks`, `matrix12-musicradar-character-notable-users` (builds on existing `vc-pads-matrix12-*`).

**QC:** the official Glen Darcey tutorial is for **V1** (UI/FX reskinned in V2; voice/Multi
architecture unchanged — flagged in-file). **V2-overhaul changelog is thinly documented** (modern
FX rack + UI confirmed, no detailed diff surfaced); Perfect Circuit's Matrix-12 article 403'd.
No drone/doom artist patch credit (technique-based).

## Sources
See §6. Originals: youtube.com (One Man And His Songs, Arturia/Glen Darcey),
soundonsound.com, forum.vintagesynth.com, musicradar.com. URLs on line 1.
