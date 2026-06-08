Manual: SL MkIII User Guide V2, p.15–17 (+ firmware 1.4 notes)
Novation manual · firmware 1.4 added per-part arp + arp chance

# Arpeggiator (Arp)

## On/off + latch
- **Turn Arp on/off:** hold **Shift + Arp**. Arp button = white when on. Held keys arpeggiate.
- The **Sequencer routes to the Arp**: when recording, held keys record as long notes; with Arp on those long notes route back through the Arp on playback.
- **Latch:** press **Latch** to toggle. Held notes sustain; note-offs delay until you release all arp notes and play new one(s). Latch works **whether Arp is on or off** (latch alone = continuous MIDI note → useful for external arps or sustained synth patches). **Latch applies only to the selected Arp destination Part.**

## Arp settings (press Arp without Shift)
Screens show: **Part · Type · Gate · Sync Rate · Octaves · Velocity · Length · Chance.**

- **Arp Part:** Arp arpeggiates **one Part at a time** (default 'Selected Part'). Soft buttons can send the arpeggiated pattern to Parts 1–8 to audition on different elements. (Firmware 1.4: each of the 8 Parts has an **independent per-part arpeggiator** for polyrhythmic layering.)
- **Type (8):** **Up** (default), **Down**, **Up/Down 1** (no repeated top/bottom), **Up/Down 2** (top/bottom repeated), **Random**, **Played** (in play order), **Chord** (all held notes as a chord each step).
- **Gate:** length of arp notes, **1%–100%** of one arp step (default 100%). Tracks Sync Rate + tempo so % stays consistent.
- **Sync Rate:** **1, 1/2, 1/2T, 1/4, 1/4T, 1/8, 1/8T, 1/16 (default), 1/16T, 1/32, 1/32T.**
- **Octaves:** **1–6** (default 1). Repeats the sequence up by octaves. Out-of-range notes correct into the top octave (G#6–G7), no duplicate notes.
- **Velocity:** **1–127** fixed, or **Played** (default, inherits played velocities).
- **Length:** arp pattern length in steps, **1–16** (default 16). A step's musical length = the Sync Rate.
- **Arp Pattern (rhythm):** after pressing Arp, each pad = a step in the arp pattern. **Toggle pads on/off** to set the rhythm (bright = plays, dim = silent; white cursor sweeps). Only affects timing, not note order.
- **Chance:** per-step probability **0%–100%** for any of the 8 arpeggiators (firmware 1.4). 0% = never, 100% = always. Set via encoders in the Arp Settings menu.

## Octave × Type interactions (reference)
- Up/Down 1 & 2 → plays the full octave range up before coming down.
- Played → plays first octave in played order before repeating up octaves.
- Random → notes randomised across the whole octave range, every note random.
- Chord → held notes repeat per octave setting upward (e.g. Octaves=3 → chord at pitch, +1 oct, +2 oct, then repeat).
