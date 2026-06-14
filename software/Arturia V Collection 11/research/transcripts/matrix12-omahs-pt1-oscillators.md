https://www.youtube.com/watch?v=PY8tC82SQD0
One Man And His Songs (Anthony) · "Arturia Matrix-12-V Tutorial Pt.1 - The Oscillators" · 2022-08-19

Section-by-section deconstruction of Arturia's Oberheim Matrix-12 (1985 original = "the last
and most powerful" Oberheim, 12-voice multitimbral). Pt.1 = oscillators + the two amplifiers.
(Distilled from captions. Same channel already trusted in this repo for the Synthi guide.)

## Two VCOs (per voice)
- **VCO1**: saw / triangle / pulse (with **Pulse Width**, default 31 — most Matrix-12 controls
  run **0–63**, so 31 ≈ center). Frequency knob = whole semitones; Detune = fine cents.
- **VCO2**: same three waves **+ a white-noise generator** (full-spectrum, unfiltered). VCO2
  is also the **FM source** (see Pt.2) and the **hard-sync slave**.
- Master **Fine Tune** at the top (his came out of the box detuned −0.292 — a deliberate
  analog-drift touch; he sets 0.5 for a true C). Per-VCO Volume = a mini-mixer; balance the
  two rather than slamming both to 63.

## Hard sync
Turn VCO2's waves on, hit **Sync** → VCO1 becomes the *master/pitch* control and VCO2 becomes
a *tonal* control. Sweeping VCO1's Frequency while synced = the classic aggressive
sync-sweep timbre (the extra harmonics come from VCO2's wave being cut short and restarted by
VCO1). Great raw material to then filter/modulate.

## Analog non-repeatability (the texture seed)
The two oscillators **cycle independently** ("virtualized analog") — each keypress lands on a
slightly different phase, so the same note isn't bit-identical twice. "The beauty of analog —
like jumping on a moving train." This per-note variation is the foundation of why stacked
Matrix-12 voices feel alive (compounds with Multi-mode detune/pan, Pt. about voices).

## The two VCAs (a gotcha)
There are **two VCAs** at the end of the chain. You hear sound on note-on/note-off because
**VCA2 is gated by Envelope 2** (env→VCA2 is the default mapping). If you *delete* the Env2→VCA2
routing in the matrix, the patch goes silent even with VCA2 turned up — a classic "why is my
patch dead" trap. (Confirms: the mod matrix is load-bearing for basic sound, not just spice.)
