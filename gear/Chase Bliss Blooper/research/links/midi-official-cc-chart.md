Source: https://blooper.chasebliss.com/midi/docs/midi-manual.pdf (official Chase Bliss "MIDI CONFIGURATION" manual, transcribed from the PDF). Cross-checked against https://midi.guide/d/chase-bliss/blooper/.

MIDI is carried over the 1/4" TRS TAP/MIDI jack via a Chase Bliss Audio MIDIBox "Ring Active" port (TRS Type B / ring-active). The MIDIBox is not included with the pedal. Default MIDI channel is 2 (change by holding both stomp switches at power-up, then sending the first PC on the desired channel). Blooper is a "zero-based" MIDI pedal: loops 1-16 are saved/recalled with Program Changes 0-15.

| CC | Parameter | Notes |
|----|-----------|-------|
| 1 | RECORD | 0 = off, any value >0 = on |
| 2 | PLAY | 0 = off, any value >0 = on |
| 3 | OVERDUB | 0 = off, any value >0 = on |
| 4 | STOP | 0 = off, any value >0 = on |
| 5 | UNDO | 0 = off, any value >0 = on |
| 6 | REDO | 0 = off, any value >0 = on |
| 7 | ERASE | 0 = off, any value >0 = on |
| 8 | HOLD SWITCH B | 0 = off, any value >0 = on |
| 11 | MULTI-CONTROL | 1:Record, 2:Play, 3:Overdub, 4:Stop, 5:Undo, 6:Redo, 7:Erase |
| 14 | VOLUME | Range 0-127 (full CCW = 0, full CW = 127) |
| 15 | LAYERS | Range 0-127 (full CCW = 0, full CW = 127) |
| 16 | REPEATS | Range 0-127 (full CCW = 0, full CW = 127) |
| 17 | MOD A (knob) | Range 0-127 (full CCW = 0, full CW = 127) |
| 18 | STABILITY | Range 0-127 (full CCW = 0, full CW = 127) |
| 19 | MOD B (knob) | Range 0-127 (full CCW = 0, full CW = 127) |
| 20 | RAMP | Range 0-127 (full CCW = 0, full CW = 127) |
| 21 | MOD A (toggle) | Range 1:Left, 2:Center, 3:Right |
| 22 | LOOPER MODE | Range 1:Left, 2:Center, 3:Right |
| 23 | MOD B (toggle) | Range 1:Left, 2:Center, 3:Right |
| 24 | PREVIEW / SAVE-LOAD | Range 1:Left, 2:Center, 3:Right |
| 30 | MOD A (engage) | 0 = Off, any value >0 = On |
| 31 | MOD B (engage) | 0 = Off, any value >0 = On |
| 51 | MIDI CLOCK IGNORE | 0 = ignore clock, >0 = listen for clock |
| 52 | RAMPING ON/OFF | 0 = ramping off, >0 = ramping on |
| 54 | NOTE DIVISIONS | 0:Whole, 1:Half, 2:Dotted, 3:Quarter, 4:Eighth, 5:Triplet, 6:Sixteenth, 7:Thirty-second |
| 100 | EXPRESSION | Range 0-127 (full CCW = 0, full CW = 127) |

Program Change: PC 0-15 recall loops 1-16 (zero-based). While in loop mode (center toggle), holding the right stomp switch while sending a PC saves the current loop to that slot.
