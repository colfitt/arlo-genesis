Source: https://www.chasebliss.com/s/Brothers-AM_MIDI-Manual_Pedal_Chase-Bliss.pdf (official Chase Bliss "Brothers AM MIDI Manual", PDF; redirects to static1.squarespace.com/.../Brothers-AM_MIDI-Manual_Pedal_Chase-Bliss.pdf). Cross-checked against https://midi.guide/d/chase-bliss/brothers-am/ — both sources agree on every CC.

Transport: MIDI arrives over a standard 1/4" TRS patch cable (use the Chase Bliss MIDIBox to convert 5-pin DIN -> TRS; MIDIBox not included). Default MIDI channel: 2 (hold both stomp switches at power-up, then send a Program Change to set the channel to that message's channel). Presets: saved AND recalled via Program Change; 122 total slots; PC 0 = "Live" mode (follow knobs); slot 1 = right preset toggle, slot 2 = left. To save, send a PC while holding both footswitches.

Transcribed verbatim from the manual's "Brothers AM Control Change Channels" table.

| CC | Parameter | Notes |
|---|---|---|
| 14 | GAIN 2 | 0 - 127 (KNOBS) |
| 15 | VOLUME 2 | 0 - 127 (KNOBS) |
| 16 | GAIN 1 | 0 - 127 (KNOBS) |
| 17 | TONE 2 | 0 - 127 (KNOBS) |
| 18 | VOLUME 1 | 0 - 127 (KNOBS) |
| 19 | TONE 1 | 0 - 127 (KNOBS) |
| 27 | PRESENCE 2 | 0 - 127 (KNOBS; hidden control) |
| 29 | PRESENCE 1 | 0 - 127 (KNOBS; hidden control) |
| 21 | GAIN 2 TYPE | TOGGLE — BOOST = 0,1; OD = 2; DIST = 3 or > |
| 22 | TREBLE BOOST | TOGGLE — FULL SUN = 0,1; OFF = 2; HALF SUN = 3 or > |
| 23 | GAIN 1 TYPE | TOGGLE — DIST = 0,1; OD = 2; BOOST = 3 or > |
| 102 | CHANNEL 1 BYPASS | FOOTSWITCH — off = 0, on = 1 or > |
| 103 | CHANNEL 2 BYPASS | FOOTSWITCH — off = 0, on = 1 or > |
| 100 | EOM (EXPRESSION OVER MIDI) | 0 - 127 (OTHER) |
| 111 | PRESET SAVE | 1-122 (OTHER) |
| 61 | DIP: VOLUME 1 (LEFT BANK) | off = 0, on = 1 or > |
| 62 | DIP: VOLUME 2 (LEFT BANK) | off = 0, on = 1 or > |
| 63 | DIP: GAIN 1 (LEFT BANK) | off = 0, on = 1 or > |
| 64 | DIP: GAIN 2 (LEFT BANK) | off = 0, on = 1 or > |
| 65 | DIP: TONE 1 (LEFT BANK) | off = 0, on = 1 or > |
| 66 | DIP: TONE 2 (LEFT BANK) | off = 0, on = 1 or > |
| 67 | DIP: SWEEP (LEFT BANK) | B = 0, T = 1 or > |
| 68 | DIP: POLARITY (LEFT BANK) | F = 0, R = 1 or > |
| 71 | DIP: HI GAIN 1 (RIGHT BANK) | off = 0, on = 1 or > |
| 72 | DIP: HI GAIN 2 (RIGHT BANK) | off = 0, on = 1 or > |
| 73 | DIP: MOTOBYP 1 (RIGHT BANK) | off = 0, on = 1 or > |
| 74 | DIP: MOTOBYP 2 (RIGHT BANK) | off = 0, on = 1 or > |
| 75 | DIP: PRES LINK 1 (RIGHT BANK) | off = 0, on = 1 or > |
| 76 | DIP: PRES LINK 2 (RIGHT BANK) | off = 0, on = 1 or > |
| 77 | DIP: MASTER (RIGHT BANK) | off = 0, on = 1 or > |

Manual note: "CC numbers are left to right as you look down over the top of the pedal. The left bank is labeled 61-68 and the right bank is 71-77."
