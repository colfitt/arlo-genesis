Manual: SL MkIII V2 (Parts/Templates/Clock) + VG-800 Reference Manual p.21 + VG-800 Parameter Guide pp.40–42, 51 (CONTROL ASSIGN, MIDI SETTING)
Novation manual + Boss VG-800 manuals (local: Gear/Roland VG-800/manuals/)

# RECIPE — Play & configure the Boss VG-800 from the 61SL

## The physical link
- VG-800 has **TRS MIDI IN/OUT** (not full-size DIN). Use a **BMIDI-5-35** TRS↔5-pin-DIN cable: **SL DIN Out → VG-800 MIDI IN**. (Boss BMIDI-5-35/1-35/2-35 are the correct cables.)
- Alternatively USB-C from VG-800 to Mac and route via DAW — but for "SL plays VG directly," use the DIN→TRS link so audio stays on its own path.

## VG-800 side — make it receive (Parameter Guide p.51, MIDI SETTING)
- **RX CHANNEL = Ch1–16** — pick a channel for the VG-800 (say **Ch4**); match the SL Part's channel.
- **RX PC MAP = FIX** (or PROG) — so incoming **Program Change** selects VG memories. (PROGRAM MAP BANK1–2 lets you remap PC#→memory if you want.)
- For clock-follow: **SYNC CLOCK = MIDI** (sync to MIDI clock at the MIDI jack) or **MIDI-AUTO** (sync when clock present, else internal).

## VG-800 side — map incoming CCs to parameters (CONTROL ASSIGN, Parameter Guide p.40)
The VG-800 has **16 assign slots (ASSIGN 1–16)**. For each: **SOURCE = MIDI CC# (CC#1–CC#31 or CC#64–CC#95)**, **TARGET = any VG parameter**, plus **MIN/MAX** range (MIN>MAX inverts). So the SL's knobs/faders don't hit fixed VG CCs — **you choose** which incoming CC drives which VG param on the VG itself. Pick CC numbers in the CC#1–31 / 64–95 windows (avoid CC#0/32 bank, CC#120–127 mode messages).

## SL side — Components Template + Part
1. In **Components**, build a Template: assign the **8 encoders / 8 faders** to CCs **within CC#1–31 and CC#64–95** (e.g. enc1=CC#20 → VG amp gain, fader1=CC#21 → FX1 level, aftertouch→CC#22 → a mod depth). Set **Low/High** to scale. Add **Buttons** as PC or CC toggles for FX on/off.
2. Send template to SL; **Shift+Sessions** → assign it to a Part.
3. Part **Channel = Ch4** (match VG RX CHANNEL); **Destination = DIN** (the DIN going to the VG via BMIDI-5-35).
4. On the VG-800, in CONTROL ASSIGN, point ASSIGN 1..n SOURCE=those same CC#s, TARGET=the params you want.

## Play it
- **Keybed** plays the VG's INST/SYNTH models (GR-300, organ, the acoustic/banjo/sitar models) without picking up the baritone/banjo — the SL is the "audition the VG patches" keyboard. Set the Part to the VG's RX channel.
- **Program Change** from a Template button or the SL's PC mechanism switches VG **memories** (RX PC MAP=FIX).
- **Faders** ride model/FX levels; **aftertouch→CC** drives a mod-depth target.
- **Clock:** SL **MIDI Clock Tx On** + VG **SYNC CLOCK = MIDI/MIDI-AUTO** → VG's tempo-synced delays/mod follow the SL.

## Gotchas
- VG-800 GUITAR-TO-MIDI is a *separate* path (VG → MIDI out, banjo/baritone pitch-to-MIDI). That's the VG feeding the SL/Elektrons, not the SL playing the VG — don't conflate the two directions.
- Keep VG **RX CHANNEL** and SL Part **channel** identical or nothing moves.
- No factory Components template for the VG-800 — this is a build-your-own.
