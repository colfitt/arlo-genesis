https://www.manualslib.com/manual/3657983/Roland-Boss-Vg-800.html
manualslib.com (mirror of BOSS VG-800 Parameter Guide, eng02) · Roland Corporation · 2025 — distilled from local `manuals/VG-800_parameter_eng02_W.pdf`, pp.15–17

THE authoritative parameter-by-parameter source for the SYNTH (INST) engines. The
factory presets are just saved combinations of these blocks, so these are the concrete
"patch ingredients" + the manual's own voicing tips (MEMO notes = factory-grade recipes).
All parameter NAMES and RANGES are manual-verified; the recipes below quote the manual's
MEMO tips verbatim where noted.

=== GR-300 / ANALOG GR (synth lead — the Pat-Metheny-lineage voice) ===
Parameters (exact, p.15):
- MODE: VCO (sawtooth only) / V+D (hexa-VCO + hexa-distortion together) / DIST (square only)
- COMP SW: OFF, ON  — "If this is 'ON', the decay time of the hexa-VCO will be extended."
  (THIS is the sustain-extender for banjo's fast decay — quoted in the UsageGuide.)
- CUTOFF: 0–100  — filter cutoff (harmonic content)
- RESONANCE: 0–100
- ENV MOD SW: OFF / ON (high→low wah on pick) / INV (low→high reverse wah)
- ENV MOD SENS: 0–100 (raise = wah triggers on weaker picking)
- ENV MOD ATTACK: 0–100 (raise = slower wah attack)
- PITCH SW: OFF, A, B (switches between two pitch-shift amounts; applies to hexa-VCO only)
- PITCH A / PITCH B: -12 to +12 semitones
- FINE A / FINE B: -50 to +50
- DUET SW: OFF, ON — "a sawtooth wave at the same pitch as the original sound will be
  added to the hexa-VCO, making the sound richer."
- SWEEP SW / SWEEP RISE 0–100 / SWEEP FALL 0–100 (glide time on PITCH SW change; 0 = instant)
- VIBRATO SW / VIBRATO RATE 0–100 / VIBRATO DEPTH 0–100
- LOW CUT: FLAT, 20.0 Hz–16.0 kHz   HIGH CUT: 20.0 Hz–16.0 kHz, FLAT
- (*1 params valid only when MODE = VCO or V+D)

*** THICK-SYNTH RECIPE (manual MEMO, verbatim) ***
"By setting the hexa-VCO's pitch shift to a PITCH setting such as +/-12 (an octave up/down),
+/- 7 (a perfect fifth), or +/-5 (a perfect fourth), you can create thick, synthesizer-like
sounds. By setting PITCH FINE to about '+/-5' to slightly skew the pitch shift of the
hexa-VCO, you can give the sound greater depth."
→ Concrete patch: MODE V+D, DUET SW ON, PITCH SW A, PITCH A = +12 (or +7 / +5), FINE A +5,
  COMP SW ON (long decay for drone), ENV MOD SW ON for the envelope-wah lead.

=== SOLO (mono lead synth) ===
- FILTER CUTOFF: 0–100 (brightness)
- FILTER RESO: 0–100
- TOUCH SENS: 0–100 (filter moves with picking; 0 = static filter)
- COLOR: 0–100 (harmonic emphasis on hard picking)
- SUSTAIN: 0–100 ("Larger values will result in longer sustain." — the banjo-decay fix)

*** SOLO SETUP RECIPE (manual MEMO, verbatim) ***
"To make adjustment easier, set FILTER CUTOFF to 100 and FILTER RESO and TOUCH SENS to 0,
then gradually increase the COLOR setting as you play the guitar/bass."

=== FILTER BASS (mono bass synth) ===
- FILTER CUTOFF 0–100, FILTER RESO 0–100, TOUCH SENS 0–100
- FILTER DECAY: 0–100 ("speed at which the filter stops"; lower value = faster; needs
  TOUCH SENS not too low)
- COLOR: 0–100 (low-range strength)

=== CRYSTAL (bell/glass attack synth — the shimmer pad voice) ===
- ATTACK LENGTH: 0–100 (decay of attack portion; smaller = shorter attack)
- MOD TUNE: 0–100 (tuning of attack modulation)
- MOD DEPTH: 0–100 (depth of attack modulation; larger = deeper undulation)
- ATTACK LEVEL: 0–100   BODY LEVEL: 0–100
- SUSTAIN: 0–100 (longer = longer drone)

=== ORGAN (drawbar + Leslie voice — the organ-drone template) ===
Nine drawbars, each 0–100:
- FEET 16 (1 octave below fundamental)
- FEET 5+1/3 (perfect 5th above)
- FEET 8 (= fundamental pitch)
- FEET 4 (1 octave above)
- FEET 2+2/3 (octave + 5th above)
- FEET 2 (2 octaves above)
- FEET 1+3/5 (2 oct + major 3rd above)
- FEET 1+1/3 (2 oct + 5th above)
- FEET 1 (3 octaves above)
- SUSTAIN: 0–100
→ Drone recipe: heavy FEET 16 + FEET 8 + FEET 4 (classic full drawbar), SUSTAIN high,
  then engage a ROTARY FX (FX1/2/3:ROTARY has RATE SLOW + RATE FAST, latched on CTL1).

Confidence: HIGH — primary manufacturer parameter manual; ranges + MEMO recipes quoted verbatim.
NOTE: factory presets store specific *values* for these params; the manual gives the params +
the voicing recipes, which is what's needed to author the rig's banjo-as-lead synth patches.
