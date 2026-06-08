https://www.strymon.net/using-midi-control-pedals-2/  (+ midi.guide CC map; Morningstar & Squarp community threads)
strymon.net / midi.guide / forum.morningstar.io / squarp.community · multiple · retrieved 2026-06-03

# Big Sky MIDI clock → Pre-Delay sync (and gotchas)

## How it works (official)
- With **MIDI Clock = ON**, Big Sky follows external MIDI clock to control **PRE-DELAY on all machines EXCEPT Magneto and Nonlinear, where it controls DECAY (delay time)** instead.
- It's a **per-preset** parameter (since fw 1.44) saved independently — only presets with the parameter ON respond to clock. Enable it on each preset you want locked to the Digitakt.
- Tempo→value example (official): "sending 120 BPM MIDI clock to BigSky → 500 ms of PRE-DELAY."
- Global on/off lives in **GLOBLS → MIDI CL** (set OFF to make the pedal ignore incoming clock entirely).

## CC map reference
- Full CC/NRPN map at midi.guide/d/strymon/bigsky/ — every knob and machine parameter is addressable; program change recalls across the 300 presets (3 MIDI banks of 128).

## Community gotchas (real threads)
- **Morningstar MC6 MkII — Tap Tempo / Pre-Delay issue** (forum.morningstar.io/t/mc6-mkii-tap-tempo-reverb-predelay-issue/4632): tap-tempo and incoming MIDI clock can fight over Pre-Delay; common fix is to set the Big Sky to **not accept MIDI clock** (MIDI CL = OFF) on presets where you'd rather tap or set Pre-Delay by hand.
- **Squarp Pyramid — MIDI "PLAY" + clock resets Big Sky time settings** (squarp.community/t/.../8833): a MIDI transport **PLAY** message followed by clock can **reset the Big Sky's (and Volante's) time/pre-delay** to the clock-derived value, clobbering a hand-dialed Pre-Delay. **Rig relevance:** the Digitakt 2 is the clock master — when it starts/stops, expect Pre-Delay on clock-enabled presets to snap to tempo. If you want a fixed Pre-Delay on a drone patch, leave MIDI CL OFF for that preset.
- **Ableton/Push → Big Sky + Timeline** (gearspace.com/.../1135049): general DAW-clock jitter/handshake complaints; isolate clock source, avoid merging multiple clocks.

## Infinite/Freeze via MIDI (Morningstar thread 10875)
- To replicate the press-and-hold INF/FREEZE from a MIDI controller: program a **Press action on footswitch-down and a Release action on footswitch-up** for momentary hold, OR use **Toggle Mode** (position 1 = press-down, position 2 = press-up) to make the freeze **latch** until pressed again. No dedicated CC was cited — it emulates the physical footswitch hold.
