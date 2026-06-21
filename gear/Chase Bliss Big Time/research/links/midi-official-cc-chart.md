# Chase Bliss Big Time — MIDI CC Chart

Source: official **Chase Bliss Big Time MIDI manual** (PDF, ref "CBA+EAE ref 2026 - BT001")
- https://www.chasebliss.com/s/Big-Time_MIDI-Manual_Chase-Bliss.pdf
- (resolves to) https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/69f2c7ade8d8811ba5f6456d/1777518509528/Big+Time_MIDI+Manual_Chase+Bliss.pdf

MIDI over standard **5-pin DIN** (IN + THRU). **Default MIDI channel 2.** To change channel: hold both footswitches at power-up; the pedal adopts the channel of the first PC/CC it sees.
Presets: **127 slots**, recalled via **Program Change**; an empty slot loads a default delay. Save a preset by sending a PC while holding both footswitches (PC# = slot), or via CC#27.

## Sliders
| CC | Parameter | Notes |
|----|-----------|-------|
| 14 | COLOR | 0–127 |
| 15 | TIME | 0–127 |
| 16 | CLUSTER | 0–127 |
| 17 | TILT EQ | 0–127 |
| 18 | FEEDBACK | 0–127 |
| 19 | WET | 0–127 |

## Buttons
| CC | Parameter | Notes |
|----|-----------|-------|
| 22 | SCALE | OFF=0, CHROMATIC=1, OCT+4+5=2, OCTAVE=3 OR > |
| 23 | MOTION | OFF=0, SINE=1, SQUARE=2, ENV=3 OR > |
| 24 | MODE | MOD=0, SHORT=1, LONG=2, LOOP=3 OR > |
| 25 | VOICING | HIFI=0, FOCUS=1, WARM=2, ANALOG=3 OR > |
| 26 | STATE | DIGITAL=0, COMPRESSED=1, SATURATED=2, #!&%=3 OR > |

## Alt Controls
| CC | Parameter | Notes |
|----|-----------|-------|
| 22 | SPREAD | OFF=0, ON=1 OR > (shares CC22 with SCALE) |
| 23 | 0.5X | NORMAL=0, 0.5X=1 OR > (shares CC23 with MOTION) |
| 24 | DIFFUSE TYPE | NORMAL=0, DOUBLE=1 OR > (shares CC24 with MODE) |
| 25 | +12 dB | NORMAL=0, +12 dB=1 OR > (shares CC25 with VOICING) |
| 32 | TEXTURE | 0–127 |
| 33 | RATE | 0–127 |
| 34 | DEPTH | 0–127 |
| 35 | CROSSOVER | 0–127 |
| 36 | DIFFUSION | 0–127 |
| 37 | DRY | 0–127 |

## Footswitches — Delay Modes
| CC | Parameter | Notes |
|----|-----------|-------|
| 102 | BYPASS (TAP RIGHT SWITCH) | OFF=0, ON=1 OR > |
| 103 | TAP / MOD ENGAGE (TAP LEFT SWITCH) | ANY |
| 106 | HOLD (HOLD LEFT SWITCH) | OFF=0, ON=1 OR > |

## Footswitches — Loop Mode
| CC | Parameter | Notes |
|----|-----------|-------|
| 102 | PLAY / STOP (TAP RIGHT SWITCH) | ANY |
| 103 | REC / PLAY / DUB (TAP LEFT SWITCH) | ANY |
| 104 | RECORD | ANY |
| 105 | PLAY | ANY |
| 106 | DELETE | ANY |
| 107 | STOP | ANY |

> **Mode-dependent shared CCs:** the footswitch CCs change role by MODE. **CC106 = HOLD (HOLD LEFT SWITCH) in delay modes, but DELETE in Loop mode.** Likewise **CC102** = BYPASS in delay / PLAY-STOP in Loop, and **CC103** = TAP/MOD ENGAGE in delay / REC-PLAY-DUB in Loop. Cite the role for the active mode, not the CC number alone.

## Other
| CC | Parameter | Notes |
|----|-----------|-------|
| 27 | SAVE TO SLOT | 0–127 (value = preset slot to save to) |
| 28 | SAVE TO CURRENT SLOT | ANY |
| 54 | TAP TEMPO SUBDIVISION | see Subdivisions table |
| 100 | EOM (EXPRESSION OVER MIDI) | 0–127 |
| 110 | THRU vs OUT | THRU=0, OUT=1 OR > (CC110 active = output MIDI clock, 60–240 bpm) |
| 111 | MIDI CLOCK IGNORE | FOLLOW=0, IGNORE=1 OR > |
| 112 | MIDI GLOBAL NOTES | OFF=0, CHANNEL=1, GLOBAL=1 OR > |

## Options Menu
| CC | Parameter | Notes |
|----|-----------|-------|
| 42 | PLAY/DUB | PLAY=0, DUB=1 OR > |
| 43 | SCALE IGNORE | OFF=0, ON=1 OR > |
| 44 | STEP | OFF=0, ON=1 OR > |
| 45 | TRAILS | OFF=0, ON=1 OR > |
| 46 | DRY KILL | OFF=0, ON=1 OR > |
| 47 | DRY CLEAN | OFF=0, ON=1 OR > |
| 48 | BALANCED/UNBALANCED | BALANCED=0, UNBALANCED=1 OR > |

## Subdivisions (CC54)
| Value | Subdivision |
|-------|-------------|
| 0 | SIXTEENTH |
| 1 | EIGHTH TRIPLET |
| 2 | DOTTED SIXTEENTH |
| 3 | EIGHTH |
| 4 | QUARTER TRIPLET |
| 5 | DOTTED EIGHTH |
| 6 | QUARTER |
| 7 | HALF TRIPLET |
| 8 | DOTTED QUARTER |
| 9 | HALF |
| 10 | WHOLE TRIPLET |
| 11 | DOTTED HALF |
| 12 OR > | WHOLE |
