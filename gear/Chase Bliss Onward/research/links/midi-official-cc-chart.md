# Chase Bliss Onward — MIDI CC Chart

Source (primary, official): https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/6667428b9de7197838995a79/1718043288825/Onward_MIDI-Manual_Pedal_Chase+Bliss.pdf
Cross-check: https://midi.guide/d/chase-bliss/onward/

MIDI is received over a standard 1/4" TRS patch cable (5-pin MIDI -> TRS via the Chase Bliss MIDIBox). Default MIDI channel is **2**; hold both footswitches at power-up to relearn the channel from the first incoming PC/CC. Presets recalled/saved via Program Change (PC 0 = "Live" mode; 122 total slots). Transcribed verbatim from the official MIDI manual.

| CC | Parameter | Notes |
|----|-----------|-------|
| 14 | Size (knob) | 0-127 |
| 15 | Mix (knob) | 0-127 |
| 16 | Octave (knob) | 0-127 |
| 17 | Error (knob) | 0-127 |
| 18 | Sustain (knob) | 0-127 |
| 19 | Texture (knob) | 0-127 |
| 20 | Ramp Speed (knob) | 0-127 |
| 21 | Error Type (toggle) | TIMING=0,1 / CONDITION=2 / PLAYBACK=3 or > |
| 22 | Fade (toggle) | LONG=0,1 / USER=2 / SHORT=3 or > |
| 23 | Animate (toggle) | VIBRATO=0,1 / OFF=2 / CHORUS=3 or > |
| 24 | Sensitivity (hidden option) | 0-127 |
| 25 | Balance (hidden option) | 0-127 |
| 26 | Duck Depth (hidden option) | 0-127 |
| 27 | Error Blend (hidden option) | 0-127 |
| 28 | User Fade (hidden option) | 0-127 |
| 29 | Filter (hidden option) | 0-127 |
| 31 | Error Routing (hidden option) | GLITCH=0,1 / BOTH=2 / FREEZE=3 or > |
| 32 | Sustain Routing (hidden option) | GLITCH=0,1 / BOTH=2 / FREEZE=3 or > |
| 33 | Effects Routing (hidden option) | GLITCH=0,1 / BOTH=2 / FREEZE=3 or > |
| 51 | MIDI Clock Ignore | 0=ignore, >0=follow |
| 52 | Ramp/Bounce (on/off) | off=0, on=1 or > |
| 53 | MIDI Sync Subdivision | whole=0, dotted-half=1, half=2, dotted-qtr=3, qtr=4, dotted-8th=5, 8th=6, 8th-triplet=7, sixteenth=8 |
| 56 | Factory Reset | 0-127 |
| 57 | Dry Kill | off=0, on=1 or > |
| 58 | Trails | off=0, on=1 or > |
| 61 | Dip — Left Bank: Size | off=0, on=1 or > |
| 62 | Dip — Left Bank: Error | off=0, on=1 or > |
| 63 | Dip — Left Bank: Sustain | off=0, on=1 or > |
| 64 | Dip — Left Bank: Texture | off=0, on=1 or > |
| 65 | Dip — Left Bank: Octave | off=0, on=1 or > |
| 66 | Dip — Left Bank: Bounce | off=0, on=1 or > |
| 67 | Dip — Left Bank: Sweep | B=0, T=1 or > |
| 68 | Dip — Left Bank: Polarity | F=0, R=1 or > |
| 71 | Dip — Right Bank: Miso | off=0, on=1 or > |
| 72 | Dip — Right Bank: Spread | off=0, on=1 or > |
| 73 | Dip — Right Bank: Latch | off=0, on=1 or > |
| 74 | Dip — Right Bank: Sidechain | off=0, on=1 or > |
| 75 | Dip — Right Bank: Duck | off=0, on=1 or > |
| 76 | Dip — Right Bank: Reverse | off=0, on=1 or > |
| 77 | Dip — Right Bank: 1/2 Speed | off=0, on=1 or > |
| 78 | Dip — Right Bank: Manual | off=0, on=1 or > |
| 93 | Tap Tempo | send any value (also CC 107) |
| 100 | EOM (Expression Over MIDI) | 0-127 |
| 102 | Freeze Bypass (footswitch) | off=0, on=1 or > |
| 103 | Glitch Bypass (footswitch) | off=0, on=1 or > |
| 104 | Alt Menu (hold both switches) | ALT exit=0, ALT enter=1 or > |
| 105 | Glitch Hold (hold left switch) | off=0, on=1 or > |
| 106 | Freeze Hold (hold right switch) | off=0, on=1 or > |
| 107 | Tap Tempo (alt) | send any value (also CC 93) |
| 108 | Retrigger Glitch | send any value |
| 109 | Retrigger Freeze | send any value |
| 111 | Preset Save | 0-122 |
