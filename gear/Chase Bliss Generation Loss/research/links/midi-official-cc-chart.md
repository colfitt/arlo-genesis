# Chase Bliss Generation Loss MKII — MIDI CC Chart

Source: Official Chase Bliss "Generation Loss MK II MIDI Manual" PDF (CBA ref 2022-GEN02)
- https://cb2k22.squarespace.com/s/Generation-Loss-MKII_MIDI-Manual_Pedal_Chase-Blisspdf.pdf
- (redirects to) https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/66ce2cac7e80902784dee836/1724787900355/Generation-Loss-MKII_MIDI-Manual_Pedal_Chase-Bliss.pdf.pdf
- Cross-check: https://device.report/manuals/chase-bliss-generation-loss-mkii-midi-manual

**Connection:** Gen Loss receives MIDI through a standard 1/4" TRS patch cable. A Chase Bliss MIDIBox converts 5-pin DIN MIDI to TRS (not included). **Default MIDI channel: 2** (re-learns channel from first Program Change after holding both stomp switches at power-up).

**Presets (Program Change):** Save = send a PC while holding BOTH foot switches (e.g. PC 45 saves to preset 45). Recall = send a PC. 122 total slots. Slot 1 = right preset-toggle slot, Slot 2 = left preset-toggle slot. PC 0 = "Live" mode (matches pedal's current physical settings).

## KNOBS
| CC | Parameter | Notes |
| --- | --- | --- |
| 14 | WOW | 0–127 |
| 15 | VOLUME | 0–127 |
| 16 | MODEL / LP | 0–127 (model select — see MODELS CC#16 value table below) |
| 17 | FLUTTER | 0–127 |
| 18 | SATURATE / GEN | 0–127 |
| 19 | FAILURE / HP | 0–127 |
| 20 | RAMP SPEED | 0–127 |

## TOGGLES
| CC | Parameter | Notes |
| --- | --- | --- |
| 21 | AUX | 1, 2, 3 |
| 22 | DRY | 1, 2, 3 |
| 23 | NOISE | 1, 2, 3 |

## SWITCHES
| CC | Parameter | Notes |
| --- | --- | --- |
| 102 | BYPASS / ENGAGE | Pedal off = 0, Pedal on = 1 or > |
| 103 | AUX | Pedal off = 0, Pedal on = 1 or > |
| 104 | ALT (both switches hold) | ALT enter = 0, ALT exit = 1 or > |

## AUX SWITCH (external aux switch jacks)
| CC | Parameter | Notes |
| --- | --- | --- |
| 105 | LEFT SWITCH | off = 0, on = 1 or > |
| 106 | CENTER SWITCH | off = 0, on = 1 or > |
| 107 | RIGHT SWITCH | off = 0, on = 1 or > |

## OTHER
| CC | Parameter | Notes |
| --- | --- | --- |
| 100 | EOM (EXPRESSION OVER MIDI) | 0–127 |
| 111 | PRESET SAVE | 1–122 |
| 24 | AUX ONSET TIME | 0–127 |
| 26 | DSP BYPASS | True bypass = < 64, DSP bypass = > 64 |
| 27 | HISS LEVEL | 0–127 |
| 28 | MECHANICAL NOISE LEVEL | 0–127 |
| 29 | CRINKLE AND POP LEVEL | 0–127 |
| 32 | INPUT GAIN | 1 = Line level, 2 = Instrument level, 3 = High gain |
| 52 | RAMP / BOUNCE (ON/OFF) | off = 0, on = 1 or > |
| 16 | MODELS | model select (same CC as MODEL knob; see value table) |

## DIP SWITCHES — LEFT BANK (labeled 61–68)
| CC | Parameter | Notes |
| --- | --- | --- |
| 61 | WOW | off = 0, on = 1 or > |
| 62 | FLUTTER | off = 0, on = 1 or > |
| 63 | SAT / GEN | off = 0, on = 1 or > |
| 64 | FAILURE / HP | off = 0, on = 1 or > |
| 65 | MODEL / LP | off = 0, on = 1 or > |
| 66 | BOUNCE | off = 0, on = 1 or > |
| 67 | RANDOM | off = 0, on = 1 or > |
| 68 | SWEEP | B = 0, T = 1 or > |

## DIP SWITCHES — RIGHT BANK (labeled 71–78)
| CC | Parameter | Notes |
| --- | --- | --- |
| 71 | POLARITY | F = 0, R = 1 or > |
| 72 | CLASSIC | off = 0, on = 1 or > |
| 73 | MISO | off = 0, on = 1 or > |
| 74 | SPREAD | off = 0, on = 1 or > |
| 75 | DRY TYPE | off = 0, on = 1 or > |
| 76 | DROP BYP | off = 0, on = 1 or > |
| 77 | SNAG BYP | off = 0, on = 1 or |
| 78 | HUM BYP | off = 0, on = 1 or > |

## MODELS — CC #16 values (model select)
| Value | Model |
| --- | --- |
| 0 | (bypass / no model icon) |
| 15 | CPR-3300 Gen 1 |
| 24 | CPR-3300 Gen 2 |
| 33 | CPR-3300 Gen 3 |
| 43 | Portamax-RT |
| 53 | Portamax-HT |
| 62 | CAM-8 |
| 72 | DICTATRON-EX |
| 82 | DICTATRON-IN |
| 91 | FISHY 60 |
| 101 | MS-WALKER |
| 111 | AMU-2 |
| 127 | M-PEX |
