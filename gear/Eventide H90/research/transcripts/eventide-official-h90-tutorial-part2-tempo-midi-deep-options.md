https://www.youtube.com/watch?v=tfd3wQHzxcA
Eventide Audio · Eventide H90 Tutorial - Part 2: Tempo, MIDI & Deep Options (Joe Cozzi) · 2023-08-16 · 47:29

The MIDI/tempo/control half of the official video manual. Most rig-relevant content: how the H90 slaves to or masters MIDI clock, output modes, and PC offset. Cleaned to prose; the back half (covered briefly) goes deeper into per-parameter CC mapping, EXP calibration, and aux-switch wiring.

## Tempo menu (hold Presets + Parameters)
Three tempo SOURCE modes:
- **Program** (default) — internal tempo is whatever was saved with the Program; every Program on the Playlist can have its own BPM. Set with the first quick knob, the first footswitch in this menu (LED blinks the BPM), a global tap-tempo aux switch, or the P/A/B tap performance parameters.
- **Global** — one tempo for all Programs; it persists as you change Programs regardless of each Program's saved tempo. Caution: set lists rarely share one BPM, so this isn't always desirable.
- **MIDI clock** — tempo is taken from external MIDI clock only; no onboard adjustment, and tap-tempo switches/aux switches are ignored. Choose whether clock comes from the 5-pin DIN input or USB in System Settings > MIDI (second page, Clock Source).

## Tempo Sync (per preset)
All time-based effects can follow tempo, but the preset's Tempo Sync must be ON. Toggle by pressing Presets + Parameters once (a metronome icon appears by the HotKnob indicator). Off = delay times shown in ms and LFO rates in Hz (manual values, ignores global/program/MIDI tempo). On = times/rates shown as subdivisions, following the BPM. A program-level tempo-sync toggle is just a shortcut to flip both presets at once. If an algorithm has more than one delay, tapping syncs all its delays to the same time. In Perform mode you can still change a non-tempo-synced preset's times/rates by mapping the Tap performance parameter, but it won't follow the Program's BPM.

## MIDI (System Settings > MIDI)
Page 1:
- **Channel** — the channel the H90 receives and transmits on.
- **Receive Omni** (default off) — receive across all 16 channels while transmitting only on the set channel.
- **Output mode** — governs the DIN MIDI Out jack:
  - **Transmit** — H90 generates and sends Program Change, Controller Change, and MIDI clock to downstream devices. DIN MIDI IN is NOT passed through. Best when the H90 acts as a controller/master. (Example: an H9 on the H90's MIDI out, set to the same channel or Omni, follows the H90's Select/Bank program searches.)
  - **Thru** — passes received DIN MIDI through to downstream devices and responds to commands on its channel; also responds to and passes on MIDI clock. Does NOT pass USB-input MIDI and does NOT generate its own commands. Best when the H90 is controlled by a MIDI switcher.
  - **Off** — no MIDI sent downstream.

Tap tempo is transmitted only when tempo Source is Global or Program. If Source is MIDI clock, the H90 only RESPONDS to incoming clock and will not transmit tempo.

Page 2 (Clock Source): choose DIN or USB for incoming MIDI clock. The H90 ignores clock unless tempo Source = MIDI clock. Critical routing fact: **only MIDI clock received at the DIN input can be passed downstream to the DIN MIDI Out** — USB clock is never forwarded to DIN, and for pass-through Output mode must be Thru, with downstream devices set to receive clock. For PC/CC: the H90 responds to PC and CC at USB, but only Program Change can be forwarded to DIN MIDI Out (Output mode = Transmit). The H90 does not respond to or transmit Program Change number 0.

**PC offset.** The MIDI spec uses 0–127 (PC 0 = program 1, off by one). The H90 natively uses 1–127 (PC 1 = Program 1) so default PC offset = 0 means it responds to PC 1–127 and ignores PC 0. Set PC offset = 1 to shift incoming PC up by one (so PC 0 reads as PC 1, matching the traditional spec). The same offset is applied to PC values the H90 transmits to downstream devices.

Page 3 — **MIDI Global Control.** Assign CC numbers to functions across all Programs (parallel to Global Pedal Control for aux/expression). MIDI convention: value 0–63 = off, 64–127 = on (simplified: 0 = off, 127 = on). For commands like increment/decrement program or mode toggle, value 127 executes, 0 does nothing. Many functions have a momentary "(m)" variant: a non-momentary active/bypass TOGGLES on any value ≥64 (127 flips state, 0 does nothing); the momentary version triggers bypass with value <64 and active with ≥64 (one button for off, another for on — no toggling). Available for Programs, Preset A, Preset B, and all three HotSwitches.

## Expression / aux switches (EXP/CTL)
System Settings > I/O page 3 designates each port as expression pedal or aux switch (up to 3 buttons), or routes a 0–5 V CV (set Pedal 1/2 to Exp 1/2). Aux switches: Pedal 1 = switches 1–3, Pedal 2 = switches 4–6. Connect the pedal/switch before plugging into the input so the H90 senses the load. Calibrate an expression pedal in I/O page 3 (Calibration > On, sweep heel-to-toe until you see a 0–100 range). Erratic sweeps usually mean wrong cable (some pedals need TS, others TRS), an internal dip switch/pot reversing the sweep, or a device-specific (non-universal) pedal. Eventide recommends a 10k–25k linear potentiometer; higher values compress the range at one end. A port cannot be both expression and aux at once — a pedal with a built-in switch may need both EXP ports. Calibration mode also displays which switch number (1–3 / 4–6) each aux button is: tip = switch 1/4, ring = switch 2/5, tip+ring = switch 3/6. The H90 accepts momentary, normally-open aux switches.

## MIDI expression
You can drive parameters from an expression pedal connected to a MIDI controller (e.g. a Morningstar MC6 Pro port set to "expression", sending CC data — e.g. CC 11 on channel 1). Then assign H90 parameters to that CC on a program or global basis (Parameters > category > hold the quick knob, set control source to the CC number).
