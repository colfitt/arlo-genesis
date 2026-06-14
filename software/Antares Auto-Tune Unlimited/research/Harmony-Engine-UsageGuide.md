# Harmony Engine 4x — Usage Guide

Harmony Engine generates up to **4 real-time harmony voices** from one monophonic source —
and in this rig the source is as often the **banjo lead / baritone / synth** as a vocal. Its
killer moves for sustained walls: **MIDI-played harmonies** (chord-via-controller from the
61SL), the **Prismizer** smeared-choir technique (Glide + per-voice Throat), and **Freeze
Pitch** to lock a held choral chord under a moving lead. It expects a clean monophonic DI —
feed it anything polyphonic or pre-effected and it glitches (lean in, or clean up first).

---

## 1. Essential workflows

**A. Scale-Interval diatonic stack (fastest tasteful path).** Set **Input Vocal Range**
(or **Instrument** for banjo/synth) → Harmony Source = **Scale Interval** → set **Key/Root +
Scale** (e.g. F♯ minor) → solo-audition each voice's interval (a working engineer settled on
a **low 3rd an octave down + a higher voice**) → pan voices **hard L/R** → HPF + de-box + air
EQ on the output bus. Interval range is **16vb…16va (±2 octaves in scale steps)**.
[transcripts/harmony-engine-plugins-masters-deep-workflow.md; transcripts/harmony-engine-rachel-k-collier.md]

**B. Chord-Degree + automation (chord-following bed, no MIDI).** Harmony Source = **Chord
Degrees**, set Key/Scale → assign each chord to one of the **15 Harmony Preset buttons**
(rename them as real chord names) → **automate the preset / chord-degree** across the song.
[transcripts/harmony-engine-plugins-masters-deep-workflow.md]

**C. MIDI Omni / Chord-Via-MIDI (play the wall).** Harmony Source = **MIDI Omni**; play up to
**4 voices** from the 61SL (4 notes max = 4 voices).
**Logic AU routing (important):** put the source on an audio track set to **"No Output"** →
load Harmony Engine as an instrument under **"AU MIDI-controlled Effects"** → set its
**Side-Chain dropdown** to that audio track → record-enable the instrument track. A plain
insert only gives the non-MIDI modes.
[links/harmony-engine-logic-midi-routing.md *(triangulated — Antares help domain 403s; cross-confirmed vs Sage Audio)*]

**D. Prismizer wall (the signature).** MIDI Omni + **Glide (transition rate) cranked** (slow
portamento = the smeared sound) + per-voice **Throat Length** (short/down = glassy highs,
long/up = bodied lows) + the **Choir multiplier** to thicken past 4 voices. Helpers: a
Chord-Trigger + velocity-Randomizer MIDI FX upstream.
[links/harmony-engine-prismizer-sage-audio.md]

---

## 2. Signature settings — drone/choir walls

- **On vocals:** MIDI Omni, Glide high, **Pitch/Timing Variation moderate–high** (turns a
  stiff stack into a breathing ensemble), each voice a different **Throat Length**, **Choir
  ×8–16** per voice.
- **On banjo / baritone / synth:** Input Vocal Range = **Instrument**; raise **Tracking** if
  it won't lock, **lower** it if you get clicks/pops; clean **DI** source, no pre-effects;
  **Freeze Pitch** to lock a sustained choral chord under a moving lead (the manual literally
  describes "creating sustained chords underneath a lead").
- **Wide-wall recipe:** run a **stereo** instance (Pan only works in stereo), octave-up +
  octave-up intervals, hard per-voice pan, Choir multiplier on, reverb at the plugin → out to
  Valhalla.
[links/harmony-engine-official-user-guide.md; transcripts/harmony-engine-rachel-k-collier.md]

---

## 3. Power-user tips & hidden features

- **Per-voice strip** carries gender/**Throat**/vibrato/pan/level + its own **Choir**
  multiplier — so each of the 4 voices can be its own detuned ensemble (4 → dozens of voices).
- **Freeze Pitch** = a held drone chord that ignores the moving input — the single best
  "wall under a lead" trick.
- **15 renameable Harmony Preset buttons** are automatable — sequence a chord progression
  without MIDI.
- **Glide / transition rate** is the Prismizer lever: slow = the smeared choir-of-one.
[links/harmony-engine-official-user-guide.md; links/harmony-engine-prismizer-sage-audio.md]

---

## 4. Notable users & techniques

- **The Prismizer** is the documented artist technique — **Bon Iver** (*22, A Million*),
  **Frank Ocean**, **Francis and the Lights**: MIDI-played harmonies + heavy Glide = a smeared
  choir-of-one. This is the closest documented credit to the rig's "wall" aesthetic and works
  on instrument drones too. [links/harmony-engine-prismizer-sage-audio.md]
- **Rachel K Collier** (electronic/sync producer) — real productions using both subtle beds
  and big climactic stacks from the same plugin. [transcripts/harmony-engine-rachel-k-collier.md]

---

## 5. Rig-specific recipes

- **Played choral drone bed (61SL):** MIDI Omni routing (workflow C) → hold a chord → Freeze
  Pitch → Choir-multiply each voice → into **Valhalla VintageVerb** (long, hall). A breathing
  vocal-less choir from the keyboard.
- **Harmonize the banjo lead:** Instrument input, Scale-Interval, a 3rd-below + octave-above,
  hard-panned → instant 3-part banjo. Clean DI only.
- **Thicken a synth drone into a wall:** Scale-Interval octaves + Choir multiplier + high
  Variation → smeared shimmer → Valhalla.
- **Degrade path:** print the harmonized wall, then RC-20 / SketchCassette on the bounce
  (don't fight pitch-tracking with pre-degradation).
- **Logic AU:** EQ / Choir / reverb belong on the **instrument** channel in the MIDI routing
  (workflow C).

---

## 6. Best learning resources

- **Official Harmony Engine User Guide PDF** — authoritative modes/ranges (`links/harmony-engine-official-user-guide.md`).
- **Sage Audio — Prismizer how-to + on-instruments** — the wall technique + honest instrument
  findings (`links/harmony-engine-prismizer-sage-audio.md`, `harmony-engine-on-instruments-sage-audio.md`).
- **Plugins Masters** (deep Pro-Tools workflow) + **Rachel K Collier** (working producer) —
  the two captured video walkthroughs.
- **Justin Elmo** HE tutorial — the existing `transcripts/antares-harmony-engine-full-tutorial.md`.

---

## 7. Common pitfalls / gotchas

- **Non-vocal sources can distort** — the engine reads vocal ADSR/timbre; strings/piano fail,
  guitar/banjo give "synth-like + glitch" artifacts (lean in or clean up). [links/harmony-engine-on-instruments-sage-audio.md]
- **Clean prep is mandatory** — no reverb/comp/distortion before it; guitar = **DI, not amp**.
- **Phase cancellation** when blending harmonies with the dry — **mute/lower the dry** to push
  the synthetic layer forward.
- **Logic MIDI modes** require the AU-MIDI-controlled-Effect + side-chain + "No Output" source
  routing; a plain insert only gives non-MIDI modes.
- **4 voices max** in MIDI Omni; pitch-tracking + choir-multiply is **CPU-heavy → print/freeze**.
- **Mono input** — comp a single-note take.

## 8. Captured sources
- `transcripts/harmony-engine-rachel-k-collier.md`, `transcripts/harmony-engine-plugins-masters-deep-workflow.md`
- `links/harmony-engine-official-user-guide.md`, `harmony-engine-prismizer-sage-audio.md`, `harmony-engine-on-instruments-sage-audio.md`, `harmony-engine-logic-midi-routing.md`
- Built on existing `transcripts/antares-harmony-engine-full-tutorial.md` (Justin Elmo).

**QC:** official PDF extracted cleanly (high confidence on ranges/modes). The Logic
MIDI-routing file is **triangulated/labeled** (Antares help 403s; cross-confirmed vs Sage
Audio — steps explicit and consistent). Prismizer artist credits are documented; otherwise
no drone/doom/shoegaze-specific credit. The "guitar works better with chords than single
notes" claim mildly contradicts the monophonic framing (author drives via MIDI/Chord-Trigger
and treats artifacts as the aesthetic) — flagged in that file.

## Sources
See §8 for local captures. Originals: youtube.com (Rachel K Collier, Plugins Masters),
antarestech.com PDFs + help, sageaudio.com. URLs on line 1 of each file.
