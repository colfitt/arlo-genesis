# CS-80 V4 — Usage Guide

Arturia's Yamaha CS-80 — **the** lush brass/string/pad-wall synth, and the most
expressive in V Collection. For this rig it's the centerpiece evolving wall under
banjo/baritone: dual-layer architecture, per-voice **polyphonic aftertouch**, and the
**ribbon controller** that give it an orchestral, breathing quality static synths
can't. (Sibling pad polysynths — Jup-8, Matrix-12, Prophet-VS, Solina — are mapped in
`Arturia-Navigator.md`.)

## 1. Architecture (the dual-layer is everything)

Two complete parallel chains — **Voice I and Voice II** — each with its own oscillator,
resonant **high-pass + low-pass** filters (12 or 24 dB/oct), and contour generator; a
**Mix** fader balances them (those HP+LP pairs ×2 = the famous "4 filters"). Build a pad
by treating them as two stacked sub-synths (detune one, octave one, brighten one).
Waveforms: triangle / **rising-ramp "saw"** / pulse / noise, combinable — the **"squared
sawtooth"** is what makes this THE brass/string synth. `research/links/vc-pads-cs80-sos-review.md`

**The contour is NOT ADSR** — it's **IL / AL / A / D / R** (Initial Level, Attack Level,
Attack time, Decay, Release): you set a starting level *and* an attack-peak level, which
is why its swells breathe differently. `research/links/vc-pads-cs80-sos-review.md`

**Global modulation:** one **sub-oscillator = a global LFO** (sine/saw/square/noise/
random) routable to pitch / cutoff / tremolo / **pan** — the pad-movement source. A
**ring modulator** (speed + amount + own A/D env) adds metallic/sci-fi edges. `research/transcripts/vc-pads-cs80-sub-oscillator-aftertouch.md`

**What V4 added:** a **3-slot / 15-type FX engine** (Tape Delay, chorus, reverb,
MultiBand Comp; series/parallel), **3 multi-segment envelopes + a Modulation Mixer**,
resizable GUI, MPE, MTS-ESP, 200 presets — the path to slow evolving pads without an
external LFO. `research/links/vc-pads-cs80-v4-whats-new-arturia.md`

## 2. The expressive secret — per-voice touch asymmetry

Velocity + **polyphonic aftertouch** are set **independently per oscillator** via Touch
Response. The famous *Blade Runner Blues* preset's whole trick is "quite different
velocity/AT settings for each of the two synth lines" — that asymmetry is what makes the
wall sound orchestral rather than static. The **ribbon controller** does the descending
pitch slides (Vangelis's signature). `research/links/vc-pads-cs80-blade-runner-blues-preset.md`, `research/links/vc-pads-cs80-blade-runner-reverbmachine.md`

## 3. Signature settings & presets (copyable)

**The "classic pad" (Jon Audio, exact values — free preset linked in his video):** `research/transcripts/vc-pads-cs80-classic-pad.md`
- **Voice I** = triangle; **HP ~47**, **LP ~144**, **LP res ~0.444**; filter contour
  Attack **3.66** / Decay **4.57** / Release **1.93**; amp env Attack **4.47** / Sustain
  max / Release **816**.
- Copy Voice I → **Voice II** (down-arrow tone-selector), set **Voice II +1 octave**,
  **Mix ~504**; **Portamento 0.15**.
- **Sub-osc LFO speed 4.69 → pan ~0.464**, AND map it to the **mod wheel** so motion only
  blooms when you push it.
- FX: internal **Tape Echo** (1/4 sync, intensity 350) + **Chorus 21.6**, dry/wet ~36.8
  → then **Valhalla VintageVerb** ("Dirty Plate") on a send.
- **Pro touch:** map the **Brilliance + Resonance** offset knobs to sliders for
  expressive real-time cutoff sweeps. `research/transcripts/vc-pads-cs80-tips-good-patches.md`

**Huge brass-pad wall (the Vangelis):** both voices on saw/squared-saw, Voice II +1 oct,
slow IL/AL/ADR swell, sub-osc LFO → pan + cutoff on the mod wheel, **per-voice asymmetric
velocity/AT**, ribbon for slides → internal Tape Echo + Chorus → Valhalla on a send +
EchoBoy. The *Blade Runner Blues* / Schilling presets are ready starting points. `research/links/vc-pads-cs80-blade-runner-reverbmachine.md`

## 4. Rig-specific recipes

- **The wall under banjo:** the classic-pad recipe above, held low, banjo-as-lead on top,
  the whole thing into Valhalla + EchoBoy; add **Decapitator** for grit or
  **SketchCassette** to re-degrade.
- **Expressive swells:** put aftertouch on cutoff per-voice and *play* the dynamics with
  a poly-AT controller (the 61SL MkIII) rather than automating — the CS-80's reason to
  exist.
- **CPU:** high unison/oversampling bites — **freeze the pad** once committed.

## 5. Best learning resources

1. **Jon Audio — "CS-80 V4 classic pads"** + **"Tips For Good Patches"** — the only
   fully-numeric copyable patches + the Brilliance/Resonance mapping trick. ★
2. **Reverb Machine — Vangelis "Blade Runner" deep-dive** — the definitive "Tears in
   Rain" deconstruction + recreation chain.
3. **One Man And His Songs — CS-80 V Ep.4 (Sub-Oscillator)** — clearest LFO + aftertouch
   routing.

## 6. Pitfalls / gotchas

- **It's an expression instrument** — without per-voice velocity/AT asymmetry it sounds
  flat; that asymmetry is the magic. `research/links/vc-pads-cs80-blade-runner-blues-preset.md`
- **CPU-heavy** with unison/oversampling → freeze.
- The contour's **IL/AL** (not ADSR) trips people up — set the start *and* peak levels.

## 7. Captured sources

**Transcripts (4)** — `research/transcripts/`: vc-pads-cs80-classic-pad (exact patch) ·
vc-pads-cs80-tips-good-patches (Brilliance/Resonance mapping) ·
vc-pads-cs80-sub-oscillator-aftertouch (global LFO + AT) · vc-pads-cs80-expressive-modwheel.
**Links (4)** — `research/links/`: vc-pads-cs80-blade-runner-reverbmachine (Vangelis
deep-dive) · vc-pads-cs80-blade-runner-blues-preset (per-voice asymmetry) ·
vc-pads-cs80-sos-review (architecture) · vc-pads-cs80-v4-whats-new-arturia.

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first
line = the original URL). Primary: Jon Audio, Reverb Machine, Sound on Sound, Arturia,
One Man And His Songs. **Honesty flag:** the raw Blade Runner patch numbers aren't
published (it ships as a free preset) — the Jon Audio classic-pad values are the concrete
copyable recipe.
