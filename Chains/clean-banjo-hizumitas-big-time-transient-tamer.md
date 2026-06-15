---
type: chain
title: "Clean → Hizumitas → Big Time Banjo Transient Tamer"
date: 2026-06-15
artists: [Boris, Sufjan Stevens]
instrument: banjo (Gold Tone EBM-5 via GK-5 → VG-800)
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
---

# Clean → Hizumitas → Big Time Banjo Transient Tamer ⭐

The single best argument for putting Clean at the *front* of the board. A banjo is all attack and no sustain — a violent pluck spike, then it's gone in ~1.5 s. That spiky, decaying source is the worst thing you can feed a fuzz wall and a long delay: the fuzz only ever hears the transient, and the delay's repeats die before they can sing. Here Clean reshapes the banjo so it *sustains like a guitar note* — a long, even decay — BEFORE it hits the Hizumitas. Now the fuzz completes a note that's already singing, and Big Time's repeats inherit a steady source instead of a spike. The result is a banjo that holds, blooms into fuzz, and echoes out in long even tails.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch sheets carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

Gold Tone EBM-5 banjo (GK-5) → **VG-800 — "GK SETTING — EBM5 BANJO"** (clean modeled banjo source, real 5th-string drone in via NORMAL MIX) → **CB Clean — "Banjo Transient Tamer"** (slow attack, long release, Envelope Balance high) → **EQD Hizumitas — "Banjo Sustain Manufacturer"** (the singing fuzz wall) → **CB Big Time — "Banjo Singing Delay"** (IN-L auto-MISO, MODE Long, STATE Compressed) → amp / interface.

The only "real artist signal-order" invoked is the general **fuzz-before-delay** standard — a documented pedal-order best practice (EQD / JHS / Reverb signal-chain guides), not an artist-specific path. The novel move is the *compressor-before-fuzz* placement, which is the whole point of the chain.

## Per-unit

- **VG-800 — "GK SETTING — EBM5 BANJO":** the banjo-as-lead enabler — nothing downstream tracks until this calibration is dialed. Recall this GK profile and run the banjo essentially *clean* through the VG-800 (no synth model). Keep `NORMAL MIX ~20–40%` so the real, un-tracked 5th-string drone stays in the signal. Crucially, do **not** lean on a SOLO-synth `SUSTAIN 80–100` model here — the thesis of this chain is that *Clean*, not the VG-800, solves the sustain problem. Let the banjo arrive at Clean as a normal, spiky banjo so Clean has something to shape.
- **Clean — "Banjo Transient Tamer":** the heart of the chain. Re-LED `Sensitivity` first (banjo is bright but quiet in the control band — set HIGHER by the left LED; GK-5 per-string output ≠ a passive pickup). `Attack ~1:00` (slow, ~50–100 ms) lets the pick spike escape, THEN the limiter clamps. `Dynamics ~noon` (into limiting) for a sustained ceiling. `Release` toggle RIGHT (Slow 1.5 s) — this is what extends the decay into guitar-like sustain. Hidden `Envelope Balance` (EQ knob toward MORE) high so the compressor tracks the bright register and ignores the banjo's phantom lows. `Wet ~1:00 / Dry ~10:00` (light parallel keeps pick detail).
- **Hizumitas — "Banjo Sustain Manufacturer":** `Volume ~11:00 · Sustain 12:00 · Tone 1:00–2:00` (well into the bass-boost CW side — the CW sweep rolls off the banjo's piercing 2–4 kHz via the 3n3 HPF cap). This is the *opposite* tone move from a dark-guitar fuzz, because the banjo is the opposite problem. With Clean already evening the source, the Hizumitas now completes and saturates a note that's already singing rather than chasing a spike. If it still reads too bright after the wall, feed a darker VG-800 amp model upstream. Pre-shape the muff with the Filter knob (scooped ↔ thick) before the delay.
- **Big Time — "Banjo Singing Delay" (NEW):** `MODE Long`, `STATE Compressed`. Long because the source now sustains long enough to deserve long repeats; Compressed because it holds a sustaining fuzz together and stops the runaway you'd get from a hot muff into a long delay. `COLOR LOW ~25–35%` (the fuzz already supplies saturation — too much COLOR + hot fuzz clamps the limiter to porridge). `FEEDBACK ~45–55%` — deliberately lower than the "endless wall" patches, so the repeats *sing and decay* musically instead of self-oscillating into a drone. `TILT EQ` pushed slightly UP to cut muff low-mud, `VOICING Focus` to keep the line defined, `WET ~40%`, `CLUSTER ~30%`. This is a melodic singing delay, not a wall.

## Routing

Mono front board (VG-800 → Clean → Hizumitas, all mono) → **Big Time IN-L auto-engages MISO** (mono-in / stereo-out) — the clean way to fan a mono fuzz into a stereo delay field; stereo from Big Time onward. No clock needed — this is a played, free-running melodic delay, not a rhythmic one.

**Gain-staging is the whole game, and the order is the argument:** Clean limits and re-shapes the envelope FIRST → Hizumitas saturates a source that already sustains evenly → keep Big Time COLOR modest so the limiter doesn't clamp the hot fuzz to porridge. Putting the compressor *before* the fuzz is the unconventional move (most players compress after dirt) — but it's exactly why the fuzz "completes the note" instead of just amplifying a spike. Re-LED Clean's Sensitivity any time you change the VG-800 GK calibration or instrument. If the repeats muddy up, push Big Time TILT further UP before touching FEEDBACK.

## Sound

A banjo that no longer sounds like a banjo's *attack* — each pluck holds, blooms into a thick sustaining fuzz, and trails off in long even echoes that sing instead of stuttering. Melodic and singing up top, saturated and warm underneath, with a stereo delay halo. Pick sparse single notes and they ring like a bowed or e-bowed line.

**Taste-ref:** the banjo-as-lead / indie-folk lens (Sufjan-style banjo melody) reshaped through a doom/drone sustain aesthetic (Boris / Wata's Hizumitas sustaining-fuzz voice) — a folk instrument made to sustain and sing like an amplified guitar lead.

## Play

1. Recall the **GK SETTING — EBM5 BANJO** profile first; confirm the 4 main strings track.
2. Re-LED Clean's `Sensitivity` against the banjo, then play single melodic lines — feel the notes *hang* where a raw banjo would have died.
3. Let each note bloom into the Hizumitas, then trail out on Big Time. Play *sparser* than you think — the sustain and the repeats fill the space.
4. For a held bed, sustain one note and let Clean's limiting + the fuzz + the delay feedback stack into a slow swell; back FEEDBACK down to return to a clean singing delay.

## Sources

- **Basis:** designed integration; chains **VG-800 "GK SETTING — EBM5 BANJO"** + **Clean "Banjo Transient Tamer"** + **Hizumitas "Banjo Sustain Manufacturer"** + **Big Time "Banjo Singing Delay"**. The compressor-before-fuzz / banjo all-attack-no-sustain premise is documented in the Clean "Banjo Transient Tamer" sheet (`research/Clean-DeepResearch.md` §6 — Envelope Balance = "the banjo tool"; slow attack lets the transient escape, slow release + limiting extend decay). Banjo decays in ~1.5 s and the Hizumitas "completes the note" per the Hizumitas GearProfile and "Banjo Sustain Manufacturer" sheet. Fuzz→Big Time gain-staging (COLOR modest, STATE Compressed under sustaining fuzz, TILT up + Focus, MISO auto-engage) from `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A.
- `Research/Taste-Profile/taste-profile.md` (banjo-as-lead + doom/drone lenses)
