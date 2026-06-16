# Chase Bliss Clean — MIDI CC Chart

Source (official): Chase Bliss "Clean MIDI Manual" PDF — https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/6707595e5e6c8b1edaec6134/1728534882056/Clean_Midi+Manual_Pedal_Chase+Bliss.pdf (linked from https://www.chasebliss.com/manuals)
Cross-check: https://midi.guide/d/chase-bliss/clean/

Connection: Clean receives MIDI through a standard 1/4" TRS patch cable. A Chase Bliss MIDIBox converts 5-pin MIDI to TRS (MIDIBox not included).
Default MIDI channel: **2**. To change: hold both foot switches while powering up; the pedal adopts the channel of the first PC or CC message it receives.
Presets: saved/recalled via Program Change (PC). 122 total slots; slots 1 & 2 = the preset toggle (slot 1 = right, slot 2 = left). PC 0 = "Live" mode. Save = send PC while holding both foot switches.

| CC | Parameter | Notes |
|----|-----------|-------|
| 14 | DYNAMICS (knob) | 0–127 |
| 15 | SENSITIVITY (knob) | 0–127 |
| 16 | WET (knob) | 0–127 |
| 17 | ATTACK (knob) | 0–127 |
| 18 | EQ (knob) | 0–127 |
| 19 | DRY (knob) | 0–127 |
| 20 | RAMP SPEED (knob) | 0–127 |
| 21 | RELEASE (toggle) | FAST = 0,1 · USER = 2 · SLOW = 3 or > |
| 22 | MODE (toggle) | SHIFTY = 0,1 · MANUAL = 2 · MODULATED = 3 or > |
| 23 | PHYSICS (toggle) | WOBBLY = 0,1 · OFF = 2 · TWITCHY = 3 or > |
| 102 | BYPASS (foot switch) | off = 0 · on = 1 or > |
| 103 or 105 | SWELL (foot switch) | off = 0 · on = 1 or > |
| 104 | ALT MENU (hold both switches) | ALT exit = 0 · ALT enter = 1 or > |
| 106 | DYNAMICS MAX (hold right switch) | off = 0 · on = 1 or > |
| 100 | EOM (EXPRESSION OVER MIDI) | 0–127 |
| 111 | PRESET SAVE | 1–122 |
| 52 | RAMP/BOUNCE (ON/OFF) | off = 0 · on = 1 or > |
| 56 | FACTORY RESET | 0–127 |
| 61 | DIP — DYNAMICS (left bank) | off = 0 · on = 1 or > |
| 62 | DIP — ATTACK (left bank) | off = 0 · on = 1 or > |
| 63 | DIP — EQ (left bank) | off = 0 · on = 1 or > |
| 64 | DIP — DRY (left bank) | off = 0 · on = 1 or > |
| 65 | DIP — WET (left bank) | off = 0 · on = 1 or > |
| 66 | DIP — BOUNCE (left bank) | off = 0 · on = 1 or > |
| 67 | DIP — SWEEP (left bank) | B = 0 · T = 1 or > |
| 68 | DIP — POLARITY (left bank) | F = 0 · R = 1 or > |
| 71 | DIP — MISO (right bank) | off = 0 · on = 1 or > |
| 72 | DIP — SPREAD (right bank) | off = 0 · on = 1 or > |
| 73 | DIP — LATCH (right bank) | off = 0 · on = 1 or > |
| 74 | DIP — SIDECHAIN (right bank) | off = 0 · on = 1 or > |
| 75 | DIP — NOISE GATE (right bank) | off = 0 · on = 1 or > |
| 76 | DIP — MOTION (right bank) | off = 0 · on = 1 or > |
| 77 | DIP — SWELL AUX (right bank) | off = 0 · on = 1 or > |
| 78 | DIP — DUSTY (right bank) | off = 0 · on = 1 or > |
| 24 | HIDDEN — NOISE GATE RELEASE | 0–127 |
| 25 | HIDDEN — NOISE GATE SENS | 0–127 |
| 26 | HIDDEN — SWELL IN | 0–127 |
| 27 | HIDDEN — USER RELEASE | 0–127 |
| 28 | HIDDEN — BALANCE FILTER | 0–127 |
| 29 | HIDDEN — SWELL OUT | 0–127 |
| 31 | HIDDEN — ENVELOPE MODE | ANALOG = 0,1 · HYBRID = 2 · ADAPTIVE = 3 or > |
| 32 | HIDDEN — SHIFTY MODE | ASR SHIFTY = 0,1 · ENV SHIFTY = 3 |
| 33 | HIDDEN — SPREAD ROUTING | EQ = 0,1 · BOTH = 2 · VOL/COMP = 3 or > |

Note: "CC numbers are left to right as you look down over the top of the pedal. The left bank is labeled 61-68 and the right bank is 71-78." (DIP switch CCs are physically printed on the pedal.)
