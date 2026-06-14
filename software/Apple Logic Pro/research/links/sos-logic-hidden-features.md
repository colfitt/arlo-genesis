https://www.soundonsound.com/techniques/logic-pro-useful-hidden-features
soundonsound.com · Stephen Bennett · 2022-04

# Logic Pro useful HIDDEN features (power-user gems, several rig-relevant)

## 1. Quick sampling via drag-and-drop (great for sampling the rig in)
- **Drag an audio file onto the TRACK LIST** (the track headers area), NOT the
  timeline. Logic offers to **create a Sampler instrument, or add to Drum
  Machine Designer or Alchemy** automatically. Fastest way to turn a recorded
  banjo/pedalboard/OP-1 take into a playable instrument.

## 2. External Instrument with audio input (hardware-as-VI, on one track)
- In External Instrument settings, tick **"Use External Instrument Plug-in"** to
  define BOTH the MIDI output port AND the audio return input at once — record
  the VG-800/S08/Elektron as if it were a virtual instrument. (See also
  musictech-hardware-synths-external-instrument.md.)

## 3. Virtual MIDI controllers in the Environment (control knobless/old gear)
- **MIDI Environment > Create Layer**, build a **Multi-instrument**, add custom
  faders/knobs, and assign CC numbers or **SysEx** in the Inspector. Lets you
  control hardware that has no physical controls (or deep SysEx params) right
  from Logic — useful for the VG-800's deeper parameters.

## 4. Hardware patch management by name
- Extract patch names (text file / MidiQuest), drop them into the **MIDI
  Instruments pane in the Environment**, then select patches **by name** from
  the track Inspector's Program section.

## 5. Import plug-in chains + regions from another project (template power)
- **Browser > Camera (Project) icon > All Files tab** → import plug-in chains,
  MIDI and audio regions from any other project. Build a "drone starter" chain
  once, pull it into any session.

## 6. Plug-in Manager sub-folders (tame a huge AU list)
- Rename plugins in **Plug-in Manager using colon notation** (`Synth:Analog`,
  `Synth:Digital`) to build a hierarchical folder structure in the plugin menu.
  Essential when you own Komplete + Arturia + Spitfire + Soundtoys as AUs.

## 7. Independent pan on Sends
- Send menu > **"Independent Pan" + "Sends on Faders"**: the send's pan moves
  independently of the track pan (e.g. dry centre, reverb send panned wide).
  Assign a **Key Command** to toggle Sends-on-Faders fast.

## 8. Track Automation Event List
- Key Command **"Track Automation Event List"** → edit automation timing/values
  numerically and precisely (better than dragging nodes for a slow Freeze morph).

## 9. Track Notes + MIDI Chase Notes
- Right-click track > add **Notes** component to jot per-track settings.
- **MIDI Chase Notes** makes long held notes sound even if you start playback
  mid-note — important for drone parts so a sustained note isn't silent when you
  drop the playhead into the middle of it.
