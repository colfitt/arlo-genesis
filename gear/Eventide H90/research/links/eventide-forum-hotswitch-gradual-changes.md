https://www.eventideaudio.com/forums/topic/h90-gradual-changes-via-hot-switches/
Eventide official forum · cestlamort (Q) / tbskoglund (Eventide staff, A) · Sept 1–2, 2025

# HotSwitches CANNOT ramp/gradual-morph — the definitive answer + workarounds

Direct user question: can a HotSwitch ramp a parameter gradually over ~0.25–1.5 s (the way an expression pedal sweeps reverb mix)?

**Official Eventide answer (tbskoglund, staff):**
> "Sorry, gradual changes are not possible with Hot Switches."

Follow-up confirmed: the HotKnob also can't be mapped to a switch for gradual changes —
> "Correct, the HotKnob can't be mapped to a switch for gradual changes."

So a HotSwitch is a hard SNAPSHOT jump (instant toggle between two parameter states), never a glide. If you want a timed sweep you need one of:

## Workarounds for gradual/ramped parameter changes
1. **Expression pedal or the HotKnob** — direct, manual, foot/hand-controlled sweep. The only fully on-board option.
2. **MIDI CC from a controller that sends a waveform/ramp** — e.g. a Morningstar (MC6/MC8) sending a sequenced/ramped CC stream into the H90's mapped parameter. This is the cleanest hands-free option for a MIDI rig.
3. **OBNE Expression Ramper V2** — dedicated pedal that generates one-shot expression sweeps into the H90's EXP input; dialing the Rate knob back from fully-CW adds "curvature to the one-shot response." Multiple forum users confirmed it works well; can also do LFO-style modulation, not just one-shots.
4. **Boss GT-1000 CORE** — has an internal virtual expression pedal you can trigger from a switch; it can target H90 parameters or send MIDI.

## Rig relevance (banjo/baritone End board)
For the drone/ambient use here, the practical takeaway: HotSwitches do INSTANT moves (Blackhole→Freeze, scale change, mix jump). For SLOW swells into a wall — e.g. ramping Blackhole Mix or Wormhole Size — use an expression pedal on EXP/CTL, or have the Digitakt 2 / a Morningstar send a ramped CC over MIDI. The H90 happily takes CC ramps for any mapped parameter.
