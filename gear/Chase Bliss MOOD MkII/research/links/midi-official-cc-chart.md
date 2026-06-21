# Chase Bliss MOOD MkII — MIDI CC Chart

Source (primary, official): https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf (CBA ref 2023 - MD2; also mirrored locally at `manuals/MOOD+MKII_MIDI-Manual_Pedal_Chase+Bliss.pdf`)
Cross-check: https://midi.guide/d/chase-bliss/mood-mkii/

MIDI is received over a standard 1/4" TRS patch cable (5-pin MIDI -> ring-active TRS via the Chase Bliss MIDIBox; the MIDIBox is not included). Default MIDI channel is **2**; hold down both stomp switches at power-up to relearn the channel from the first incoming Program Change message. Presets recalled/saved via Program Change (PC 0 = "Live" mode matching current settings; 122 total slots; slot 1 = right preset-toggle position, slot 2 = left; empty slots recall nothing — there are no factory presets besides the two loaded in slots 1 & 2). To save, send a PC while holding both footswitches (or use CC111). Transcribed verbatim from the official MIDI manual.

MOOD MkII is a dual-engine pedal: a **Wet Channel** (left footswitch — Reverb / Delay / Slip) and a **Micro-Looper Channel** (right footswitch — Env / Tape / Stretch). Each channel has its own MODIFY knob and its own clock-division CC.

| CC | Parameter | Notes |
|----|-----------|-------|
| 1 | Modulation Wheel (Synth Mode) | 0-127; auto-connected in Synth Mode |
| 14 | Time (knob) | 0-127. When clock-synced (Tape mode), stepped: 1/32=0-12, 1/16=13-36, 8th-triplet=37-61, 8th=62-84, dotted-8th=85-110, qtr=111-128 |
| 15 | Mix (knob) | 0-127 |
| 16 | Length (knob) | 0-127. Synced (CC16, Tape mode only): x1/32=0-12, x1/16=13-36, x1/8=37-61, x1/4=62-84, x1/2=85-110, x1=111-128 |
| 17 | Modify — Wet Channel (knob) | 0-127 |
| 18 | Clock (knob) | 0-127. Stepped clock values: 2k=0-4, 3k=5-16, 4k=16-28, 6k=29-40, 8k=41-53, 12k=54-69, 16k=70-83, 24k=84-95, 32k=96-109, 48k=110-121, 64k=122-127 |
| 19 | Modify — Micro-Looper (knob) | 0-127. Tape mode speed: 4x Rev=0-4, 2x Rev=5-23, 1x Rev=24-42, 0.5x Rev=43-61, 0.5x Fwd=62-84, 1x Fwd=85-97, 2x Fwd=98-119, 4x Fwd=120-127. Stretch mode speed: No Stretch Rev=0-15, 1.5x Rev=16-30, 2x Rev=31-46, 4x Rev=47-60, Stalled=61-80, 4x Fwd=81-96, 2x Fwd=97-111, 1.5x Fwd=112-126, No Stretch Fwd=127 |
| 20 | Ramp Speed (knob) | 0-127 |
| 21 | Wet Channel Mode (toggle) | REVERB=0,1 / DELAY=2 / SLIP=>2 |
| 22 | Routing (toggle) | IN=0,1 / IN+micro-loop=2 / micro-loop only=>2 |
| 23 | Micro-Looper Mode (toggle) | ENV=0,1 / TAPE=2 / STRETCH=>2 |
| 24 | Stereo Width (hidden option) | 0-127 |
| 25 | Ramping Waveform (hidden option) | 5 stepped waveforms: 0-14 / 15-54 / 55-80 / 81-126 / 127 (manual prints the ranges without naming the waveforms) |
| 26 | Fade (hidden option) | 0-127 |
| 27 | Tone / hi-cut (hidden option) | 0-127 |
| 28 | Level Balance (hidden option) | 0-127 |
| 29 | Direct Micro-Loop (hidden option) | 0-127 |
| 31 | Sync direction (hidden option) | =0,1 / no sync=2 / =>2 |
| 32 | Spread (hidden option) | (Spread-)only=0,1 / both=2 / (Solo-)only=>2 |
| 33 | Buffer / Loop Length (hidden option) | Half (like MkI)=0,1 / Full=>1 |
| 51 | MIDI Clock Ignore (saved globally) | 0=ignore, >0=follow |
| 52 | Stop Ramping | 0=stop, >0=resume |
| 53 | Clock Division — Wet Channel (saved globally) | 0=1/32, 1=1/16, 2=8th-triplet, 3=8th, 4=dotted-8th, 5=qtr, 6=half, 7=whole |
| 54 | Clock Division — Micro-Looper (saved globally) | 0=1/32, 1=1/16, 2=8th-triplet, 3=8th, 4=dotted-8th, 5=qtr, 6=half, 7=whole |
| 55 | True Bypass Mode | 0=Standard Buffered Bypass, 1-127=True Bypass |
| 56 | Factory Reset | 0-127 |
| 57 | Octave Transpose (Synth Mode) | 12 semis=1, 24=2, 36=3, 48=4, 60=5, 72=6, 84=7, 96=8, 108=9 |
| 58 | Output Type (Synth Mode) | OPEN=0 / ON/OFF=1 / ADSR=>1 |
| 59 | Exit Synth Mode | >1 |
| 61 | Dip — Left Bank (Ramping/Expr): Time | off=0, on=1 or > |
| 62 | Dip — Left Bank: Modify (Wet) | off=0, on=1 or > |
| 63 | Dip — Left Bank: Clock | off=0, on=1 or > |
| 64 | Dip — Left Bank: Modify (Micro-Looper) | off=0, on=1 or > |
| 65 | Dip — Left Bank: Length | off=0, on=1 or > |
| 66 | Dip — Left Bank: Bounce | off=0, on=1 or > |
| 67 | Dip — Left Bank: Sweep | B=0, T=1 or > |
| 68 | Dip — Left Bank: Polarity | F=0, R=1 or > |
| 71 | Dip — Right Bank (Customize): Classic | off=0, on=1 or > |
| 72 | Dip — Right Bank: Miso | off=0, on=1 or > |
| 73 | Dip — Right Bank: Spread | off=0, on=1 or > |
| 74 | Dip — Right Bank: Dry Kill | off=0, on=1 or > |
| 75 | Dip — Right Bank: Trails | off=0, on=1 or > |
| 76 | Dip — Right Bank: Latch | off=0, on=1 or > |
| 77 | Dip — Right Bank: No Dub | off=0, on=1 or > |
| 78 | Dip — Right Bank: Smooth | off=0, on=1 or > |
| 80 | Attack (Synth Mode ADSR) | 0-127 |
| 81 | Decay (Synth Mode ADSR) | 0-127 |
| 82 | Sustain (Synth Mode ADSR) | 0-127 |
| 83 | Release (Synth Mode ADSR) | 0-127 |
| 84 | Portamento (Synth Mode) | 0-127 |
| 93 | Tap Tempo | any value >0 (see CC107). To exit tap-tempo mode, hold the footswitch and turn the TIME knob |
| 100 | Expression Over MIDI (EOM) | 0-127 |
| 102 | Bypass — Wet Channel (left footswitch) | off=0, on=1 or > *(manual labels both 102/103 "BYPASS"; wet/micro-looper split inferred from footswitch layout — see note)* |
| 103 | Bypass — Micro-Looper Channel (right footswitch) | off=0, on=1 or > *(see note)* |
| 104 | Hidden Menu (hold both footswitches) | off=0, on=1 or > |
| 105 | Freeze (hold left footswitch — Wet Channel) | off=0, on=1 or > |
| 106 | Overdub (hold right footswitch — Micro-Looper) | off=0, on=1 or > |
| 107 | Tap Tempo | any value >0 (also CC93) |
| 110 | MIDI Reset | 1-127. Resets: MIDI clock ignore OFF, octave transpose -+3 octaves, clock dividers to quarter note, portamento to 0, gate mode to 0 |
| 111 | Preset Save | 0-122 (value = target slot) |

## Notes / verification flags

- **Footswitch CC layout — CONFLICT between sources, resolve on hardware:** The MIDI manual lists CC102 and CC103 both only as "BYPASS" and CC105/CC106 only as "FREEZE"/"OVERDUB", without printing which is Wet vs Micro-Looper. The MAIN pedal manual confirms the LEFT footswitch is the Wet Channel (HOLD = Freeze) and the RIGHT footswitch is the Micro-Looper (HOLD = Overdub). **This table assigns CC102 = Wet/left bypass and CC103 = Micro-Looper/right bypass** by the first-listed/footswitch-order logic (FREEZE=CC105 → left/Wet, OVERDUB=CC106 → right/Micro-Looper). **However, midi.guide states the OPPOSITE: CC102 = Micro-looper bypass, CC103 = Wet-channel bypass (and CC105 = Wet freeze, CC106 = Micro-looper freeze).** Neither the manual labels nor midi.guide is unambiguous on the 102-vs-103 wet/looper split — treat this single mapping as UNRESOLVED and verify by ear on hardware before relying on it. (The CC numbers themselves, 102/103/104/105/106, are certain; only the wet/looper attribution is in doubt.)
- **Two MODIFY knobs:** MOOD MkII has a Wet MODIFY and a Micro-Looper MODIFY. CC17 = Wet MODIFY, CC19 = Micro-Looper MODIFY (the manual's "MODIFY *" stepped-value tables on pg.8 — Tape/Stretch mode speed — are keyed to CC19, the Micro-Looper modify). Left-bank dip CC62 = Wet Modify, CC64 = Micro-Looper Modify.
- **Synth Mode:** auto-engages on any incoming MIDI Note (no dedicated enter CC — "ENTER SYNTH MODE = NA, any value"); MIDI Notes drive the CLOCK knob in semitones; MIDI clock is ignored while in Synth Mode; exit via CC59 (>1) or by moving the Clock knob. Synth Mode settings are saved globally, not per-preset. Pitch Bend range = +/- 4 semitones (NA / any value). Mod Wheel = CC1.
- **Globally-saved CCs:** CC51 (clock ignore), CC53 and CC54 (clock divisions) are saved globally, not per-preset (per manual annotations).
- **Hidden-option value steps:** CC25 (Ramping Waveform) and CC31/CC32 use stepped/3-way ranges transcribed verbatim above; the manual's exact wording for CC32 splits Spread vs Solo across the low/high ends with "both=2" in the middle.
- **CC58 ambiguity:** In the Synth Mode Output Type section the manual gives ADSR as CC58 value "2-127" (pg.14) but the summary table lists "ADSR = >1" (pg.10). Treat ON/OFF=1 and ADSR=2 or greater.
