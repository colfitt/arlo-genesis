https://www.soundonsound.com/reviews/arturia-matrix-12-v
soundonsound.com · "Arturia Matrix-12 V" review · undated

Second pass of the SOS review focused on the bits NOT in the existing
`vc-pads-matrix12-sos-review.md` — practical sound-design, the full mod-source roster, the
Multi-mode patch recipe, and the hard CPU number.

## Full modulation-generator roster (per voice)
- **5 five-stage contour generators** (DADSR-style envelopes — the extra Delay stage = long,
  complex contours ideal for slow pad swells).
- **5 LFOs** with **noise and S&H** waveforms + cyclic waveforms.
- **1 dedicated vibrato generator** (the "6th LFO").
- **3 tracking generators** (reshape/bend any function — e.g. curve a mod response per-key).
- **4 ramp generators** (single-stage envelopes for any signal).
→ Routed via the **40-slot matrix, 27 sources → 47 destinations.**

## Multi-mode in practice (reviewer's own patch)
Built a patch playing **4-note polyphonically within a key range with two detuned instances
panned hard L/R**, plus separate soloing voices — i.e. assign Singles to zones with independent
detune/pan to get "subtle variations in voicing to quite extreme effects" and "superb rotating
and quasi-random voicing." Confirms the Voice/Multi page is where the lush, wide,
self-animating textures come from.

## Filter character
"15 filter types, dual VCA stages" took the original "into realms no previous analogue
polysynth had explored." The flexibility of the filter section is the standout for character.

## ★ CPU (the hard number for a Logic AU rig)
**~30% CPU idle**, but scaled acceptably — reviewer ran **all 12 voices in a complex Multi at
44.1kHz with no problems.** Takeaway: the Matrix-12 V2 has a high *baseline* cost even before
you play (the per-voice 5 LFOs + 5 envs are always running) → **freeze/bounce committed
Matrix-12 pads early**, and prefer 44.1kHz sessions / lower oversampling for big Multis.
