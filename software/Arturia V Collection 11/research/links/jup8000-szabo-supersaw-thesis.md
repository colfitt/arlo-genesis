https://www.adamszabo.com/internet/adam_szabo_how_to_emulate_the_super_saw.pdf
adamszabo.com · Adam Szabo · "How to Emulate the Super Saw" (BSc thesis) · undated (~2010)

THE authoritative reverse-engineering of the JP-8000/JP-8080 supersaw. Recorded the real
hardware and analyzed it parameter by parameter. (Extracted from the PDF directly — WebFetch
choked on the binary, pdftotext succeeded.) Explains exactly what the Jup-8000 V's Supersaw +
Detune + Mix knobs are doing under the hood.

## The four findings (verbatim-grounded)
1. **Seven sawtooth oscillators.** The Supersaw = 7 detuned saws (one center + six side saws).
2. **DETUNE is NON-LINEAR.** "The detune curve of the seven oscillators is not linear and the
   detune values do not result in a proportional ratio of detune." → The first half of the
   Detune knob's travel barely spreads the saws (subtle, the **pad** region); near the top it
   spreads fast (the wide trance/lead region). Practical: for ambient pads keep Detune **low /
   in the lower third**; for screaming leads push toward max.
3. **MIX changes the side-vs-center balance, parabolically.** As you raise Mix: the **center
   oscillator drops in volume LINEARLY** while the **six side oscillators rise as a PARABOLA.**
   (Different from what Roland's manual implied.) → High Mix = the six detuned saws dominate =
   thickest/widest; low Mix = the center pitch dominates = more focused/cleaner. For a fat wall:
   raise Mix; for a defined pad pitch under a banjo lead: ease Mix back.
4. **Free-running random phase + a HPF.** The seven saws' phases are **strictly random** — each
   note-trigger seeds a random phase → that organic per-note variation (don't expect bit-
   identical attacks; this is desirable). There is a **high-pass filter at the fundamental
   harmonic** of each oscillator (its corner tracks the note frequency), there to fight
   aliasing — part of why a raw supersaw already sounds slightly thinned/bright at the bottom.

## Rig relevance
- The non-linear Detune is why "just a hair of Detune" = lush pad and "max Detune" = trance
  monster. Live in the low third for shoegaze/ambient walls.
- Free-running phase = the supersaw already has built-in non-repetition; stack it with an
  Advanced-panel Function/Random modulator for compounding evolution.
- The built-in HPF-at-fundamental means a supersaw wall leaves low headroom — good before
  Decapitator (won't mud up) but you may want to layer a sub/OSC2 saw an octave down for body.
