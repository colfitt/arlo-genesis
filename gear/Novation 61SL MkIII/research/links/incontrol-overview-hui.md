Manual: SL MkIII User Guide V2, pp.29–31 (InControl + HUI)
Novation manual

# InControl + HUI — what DAW control you get, and the fallback

## Two modes, one button
Press **InControl** to enter DAW-control mode (exits the standalone sequencer world — it's a hard toggle, see dossier §4). Press InControl again, or any other view button, to leave it. There is a dedicated host port: the **"SL MkIII InControl" / Port 2** (a.k.a. MIDIIN2/MIDIOUT2 on Windows) used only for DAW communication; the plain **"SL MkIII MIDI" / Port 1** carries note/Part MIDI.

## Native InControl vs HUI
- **InControl** = Novation's protocol with **dedicated DAW scripts** for **Ableton Live, Logic Pro, Reason** (and supported via InControl: Pro Tools, Cubase, Reaper). Gives the richest control.
- **HUI** = Mackie-HUI emulation fallback for any HUI-capable DAW (Steinberg/Cubase, Pro Tools, Reaper-partial). The SL waits for a HUI **Heartbeat** from the DAW; no heartbeat for 3 s → drops back to InControl mode.

## DAW Feature Support matrix (from the manual)
| Feature | Pro Tools | Cubase | Reaper | Logic | Reason | Ableton |
|---|---|---|---|---|---|---|
| Faders → Volume | Y | Y | Y | Y | — | Y |
| Encoders → Pan | Y | Y | Y | Y | — | Y |
| Select / Mute / Solo / Arm track | Y | Y | Y | Y | — | Y |
| Rewind / FF | Y | Y | No | Y | Y | Y |
| Stop / Play / Record / Loop | Y | Y | Y(no loop) | Y | Y | Y |
| Track left/right | Y | Y | Y | Y | Y | Y |
| Track **Name** on screens | No | No | No | **Y** | No | **Y** |
| Save / Undo | Y | Y | — | Undo only | — | Y |
| Encoders → Sends (Groups A–E) | Y | Y | — | Y | — | Y |
| Metronome | No | No | No | **Y** | **Y** | **Y** |
| **Clip Control** | — | — | — | — | — | **Y (Ableton only)** |
| **Device Control** | — | — | — | **Y** | **Y** | **Y** |
| Smart Controls | — | — | — | **Y (Logic only)** | — | — |
| Count-in | — | — | — | **Y** | — | — |

**Takeaway for this rig:** Ableton is the most capable (clip launch is Ableton-exclusive; device control + metronome + track names). Logic is close (device control, Smart Controls, count-in, track names) but **no Save, no clip launch**. Reason has device control but no fader volume/pan (N/A column).

## HUI control layout (generic fallback)
- **8 faders** = channel volume; the fader *past* the last DAW track = main output fader.
- **8 encoders** = pan; press **Options** → encoders become **send levels** (banks A–E via page up/down).
- **Right soft buttons** = Mute / Solo, **page up** to reach **Arm**.
- **Track Left/Right** = bank 1 channel; **Shift + Track L/R** = jump a whole bank of 8.
- **Transport** (L→R): Rewind, Fast-Forward, Stop, Play, Loop on/off, Arm/Record.
- **Shift + soft buttons**: Button 01 = Undo (flashes = Redo available in PT); Buttons 2/3 = Pre/Post-roll; Button 08 = Save.

## Key limitations (read before relying on it)
- **No Automap.** The MkIII dropped Novation's old per-plugin auto-mapping; you get transport+mixer+generic device banking, **not** deep auto-mapped plugin control. Soft-synth param control is via the DAW script's device banking (Ableton/Logic/Reason) or you build a standard-MIDI Template and use the plugin's own MIDI-learn.
- **Fader Pickup is bypassed in InControl** — the SL inherits the DAW's pickup behaviour, so moving a fader can jump a value (faders aren't motorized/touch-sensitive). Fader Pickup (Global) only helps in standalone/Template mode.
- Manual reportedly **misdocuments** Shift+Next/Prev track banking direction (Tape Op) — verify on-unit.
- Anecdotal **USB-to-Logic MIDI timeouts**; DIN connection avoids it (dossier §11). Not confirmed widespread.
