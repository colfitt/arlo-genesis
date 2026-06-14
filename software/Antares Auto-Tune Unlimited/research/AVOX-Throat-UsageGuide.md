# AVOX Throat (Throat Vocal Designer) — Usage Guide

Throat is a **physical model of the human vocal tract** — reshape throat length/width, the
glottal pulse, breathiness, and formant frequencies. Its one trick that matters for this rig:
it **decouples formants from pitch**, so you can hold a banjo/baritone/synth drone dead steady
and morph only its *vowel/formant* colour — into hollow, nasal, gender-wrong, physically
impossible timbres. Reviewers warn it's hard to get *realistic* results; for drone/doom that
"false" zone **is** the target.

---

## 1. Control set (Throat Evo UI)

- **Vocal Range** — source-match selector.
- **Glottal voice-type** — Medium / louder-intense, by delivery.
- **Throat Precision — Subtle / Medium / Extreme** = "like Retune Speed, but for the throat"
  — the master how-wrong dial.
- **Pitch** — ±1 octave (an Evo addition; the old AVOX-2 Throat had no pitch shift).
- **Breathiness** + a **high-pass freq** under it — higher HPF = less original, more synthetic
  modelled tract.
- **Length** — stretch = lower/longer tract; shorten = small/raised.
- **Width** — wide = airy; narrow = nasal.
- **Glottal Model** pulse display (excitation thickness); **Level Matching**; Output/Bypass/Reset.
- **5-point graphical Throat-Shaping display:** node 1 = vocal cords, nodes 2–3–4 =
  passageway, node 5 = mouth/lips — drag positions/widths to re-voice by hand. The graph and
  the Length/Width knobs are the **same model** (one re-scales the other); this is where the
  impossible timbres live.
[transcripts/avox-throat-voice-actors-walkthrough.md; links/avox-throat-pitch-tract-modeling.md]

---

## 2. Signature sound-design settings

- **Vowel-locked drone colour:** hold pitch steady, push **Throat Precision → Extreme** + high
  breathiness-HPF so the synthetic tract dominates; sweep **Length** for a morphing vowel.
- **Honking nasal lead:** drag **node 5 (mouth) closed** + **Width narrow** → a vowel-locked,
  nasal banjo/baritone lead.
- **Impossible-tract pad:** extreme **Length** + dragged graph nodes on a sustained note →
  gender-wrong / inhuman pad.
[transcripts/avox-throat-voice-actors-walkthrough.md; links/avox-throat-pitch-tract-modeling.md]

---

## 3. Rig-specific recipes

- **Re-voice the banjo lead:** Precision Medium/Extreme, mouth node closed, Width narrow →
  "vowel-locked" honking lead. Clean mono DI.
- **Alien drone:** extreme Length + dragged nodes on a sustained banjo/synth → impossible-tract
  pad → chain into **Valhalla** for the tail.
- **Formant-morph automation:** automate Length or a graph node across a section for a slow
  vowel sweep on a held drone.
- **Logic AU:** mono insert; **print/freeze** (physical model + pitch-shift is CPU-heavier than
  static plugins).

---

## 4. Notable users & techniques
None documented in drone/doom/shoegaze/experimental — relevance is by **capability**.
Reviewers' consensus ("tricky to get realistic results / sounds false if pushed") is exactly
the creative invitation here. [links/avox-throat-musicradar-kvr-verdicts.md]

## 5. Common pitfalls / gotchas
- **Mono input only** — comp a clean single-note take; strums/double-stops won't track.
- **Old vs Evo:** AVOX-2 Throat had **no pitch shift** — ignore "just use Melodyne" forum
  advice aimed at the old version. Natural gender-swap is weak; perform in register instead.
- **CPU** — physical model + pitch-track → print/freeze in Logic. Subscription auth.

## 6. Captured sources
- `transcripts/avox-throat-voice-actors-walkthrough.md` (live Evo control + node-map tour)
- `links/avox-throat-pitch-tract-modeling.md` (full control set; formant-decoupled-from-pitch behaviour)
- `links/avox-throat-musicradar-kvr-verdicts.md` (reviewer + real-user honesty layer)

**QC:** these are obscure tools; content is thin and 100% pop-vocal-framed. Antares' own pages
are JS-walled → distilled via retailer/SoS/MusicRadar summaries + the captured live-UI video.
**No verified experimental-artist credit** — every recipe is by capability/technique.

## Sources
See §6. Originals: youtube.com (voice-actors walkthrough), antarestech.com/product/throat,
musicradar.com, kvraudio.com. URLs on line 1.
