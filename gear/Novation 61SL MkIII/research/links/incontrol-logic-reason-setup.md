Manual: SL MkIII User Guide V2, pp.35–37 (Logic Pro X, Reason)  +  novationmusic.com/downloads
Novation manual

# InControl setup — Logic Pro & Reason

## Logic Pro (script auto-installs)
Setup:
1. Download/run the SL MkIII installer from **novationmusic.com/downloads** (installs the Logic control-surface script).
2. SL is then **auto-detected** in Logic. If not:
   - Logic Pro menu → **Control Surfaces → Setup**.
   - **New → Install** → pick **Novation 61SL MkIII** (or 49SL) → **Add**.
   - Set both **input and output port = "SL MkIII InControl"** port.
   - Close the Control Surface window.

What you get:
- **Track Select** = soft button under the track name (names show on screens).
- **Faders** = track volume (LED above shows level). **Options → Pans** = encoders control pans.
- **Options → Sends** = encoders control **Bus levels**; Up/Down arrows pick which send — up to **4 sends**.
- **Soft buttons (above faders)** = Mute/Solo; **down arrow** → Record Arm / Input Monitoring.
- **Options → Shortcut**: Undo, Redo, Count-In (toggle), Metronome (toggle).
- **Device Control** + **Smart Controls** supported (Logic-exclusive among these). Count-in supported.
- **Transport**: Rewind, FF, Stop, Play, Cycle on/off, Record.
- Limitations: **no Save**, **no Pre/Post-roll**, **no clip launch** (that's Ableton-only).
- Known anecdote: USB MIDI timeouts in Logic on some units — DIN connection is the workaround (dossier §11).

## Reason (auto-detect)
1. Connect SL via USB.
2. Reason → **Preferences → Control Surfaces** → **Auto-detect Surfaces**.
3. Enable **"Use with Reason"** and **"Novation SL MkIII SL MkIII From DIN 1"**.

What you get:
- **Track Left/Right** move through Reason's sequencer tracks; loading a new Instrument auto-assigns the SL to it. For **Effects/Utilities**, right-click the rack device → "Create Track for…", then select that track.
- **Encoders** = device params (name+value on screens). **Faders** = device params too (e.g. Europa: fader 1 = Osc1 level). **Soft buttons 1–24** navigate inside devices (Redrum channels 1–8, Mixer 14:2 channels, Kong drum select via pads).
- **Pitch/Mod wheels, Sustain pedal, keybed** all play/modulate Reason instruments. **Option** button toggles metronome; **Up/Down** left of pads change presets.
- Note: in the InControl matrix Reason shows **N/A** for fader-volume/pan/select — its model is device-param control, not a HUI mixer.

## Rig note
Logic and Ableton are the two DAWs this rig uses. Logic = good transport/mixer/device control + Smart Controls; Ableton = the same plus clip launch. Reason is documented for completeness; not in the active rig.
