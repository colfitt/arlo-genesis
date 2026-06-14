https://www.youtube.com/watch?v=XhDq5g4j--I
One Man And His Songs (Anthony) · "Arturia Matrix-12-V Tutorial Pt.2 - Filters & FM" · 2022-08-22

The 15-mode multimode filter + the FM (frequency-modulation) section that ties oscillators to
the filter. (Distilled from captions.)

## The 15 filter modes (the Matrix-12's headline feature)
Click the "4P LPF" label (or turn the knob) to cycle all **15 modes**:
- **4 low-pass** (1-pole → 4-pole). 4-pole = steepest slope (most dB/oct discarded); 1-pole =
  gentlest. (Matrix-12 counts in **poles**, not dB/oct — unusual terminology.)
- **3 high-pass** (= low-cut; more poles = steeper).
- **2 band-pass** (inverse of a notch — a peak/mountain; cuts either side of the corner).
- **Notch** (2-pole) — scoops a V around the corner; Resonance reshapes the notch.
- **Phase / all-pass** — *nothing is actually attenuated*; uses phase cancellation around the
  corner to drop frequencies. "Phasers use this type of filtering" — so this mode IS a
  built-in phaser-flavor (great for shoegaze swirl).
- **4 "combo" modes** at the top — e.g. **phase + low-pass** combined → two effects at once
  (some combos self-oscillate readily).

**Vocabulary note (matters for the manual):** the Matrix-12 calls the cutoff frequency the
**"corner point."** Resonance is the resonant peak at that corner.

## Resonance / self-oscillation
Resonance to max → self-oscillation (filter generates its own sine). Distinctive here:
**resonance TRACKS the keyboard** — the self-oscillation pitch follows the note you play
(many analogs give a single static squeal instead). So you can play the self-oscillating
filter as a tuned tone/drone. Push it for "violent nasty" texture.

## FM (frequency modulation) — ties OSC↔filter
FM section is hardwired to use **VCO2's triangle wave** as the modulator (regardless of which
VCO2 waveforms are lit — stated in the manual, not shown on the panel). Two destinations via a
gate switch:
- **→ VCO1 (gate set to VCO):** VCO2's triangle modulates VCO1's *pitch* at audio rate =
  true FM timbres (bell/metallic/gritty). Turn FM **Amount** up from 0 to dial it in.
- **→ VCF (gate set to "VCF"):** modulates the *filter cutoff* instead. Subtle at audio rate;
  slow VCO2 way down (low note) and it becomes an audible bubbling/grasping movement on the
  cutoff — a living, irregular filter wobble for evolving texture.

## Rig takeaway (inferred)
The **phase/all-pass + combo modes** give a shoegaze phaser/swirl inside the synth before any
FX. The **keyboard-tracking self-oscillating filter** is a playable drone source. **FM→VCF at
slow rates** = irregular cutoff motion to layer with the matrix LFOs for a never-static wall.
