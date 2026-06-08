https://www.chasebliss.com/brothers-am
chasebliss.com + reusable cb-stack refs · Chase Bliss · 2025 / accessed 2026-06

# MIDI / preset integration of Brothers AM into the CB stack

The AM folds into the same Chase Bliss MIDI/preset scheme as the rest of the rig's CB pedals — do NOT re-derive; cite the two reusable references below.

## What the AM exposes
- **MIDI: PC + CC over every parameter**, **CV over all knobs**, **expression**, ext footswitch. **4 onboard presets** (2 banks via the BANK dip) + **up to 122/128 via MIDI** (chasebliss.com). All controls (incl. dip states) are **preset-saveable** — dip settings save with presets.
- **MIDI is NOT native 5-pin/USB** — it arrives over the same **ring-active 1/4" TRS** jack the rest of the TRS-MIDI CB pedals use; you need the **Chase Bliss MIDIbox** (DIN→TRS) to feed it. ⚠️ Documented gotcha: it's easy to forget to **power the MIDIbox**.

## How it joins the stack (CITE these — already verified for the whole CB board)
- **TRS-MIDI wiring + MIDIbox:** `/Users/cfitt/Dev/Pedalxly/Gear/Chase Bliss Blooper/research/links/cb-stack-midi-trs-and-midibox.md`
  - One MIDIbox drives up to **4** CB TRS pedals; ring-active jumpers; needs its own 9V. The AM is one more TRS pedal on a MIDIbox port.
- **Preset / scene recall:** `/Users/cfitt/Dev/Pedalxly/Gear/Chase Bliss Blooper/research/links/cb-stack-preset-scene-recall.md`
  - Every CB pedal recalls a preset by **Program Change** on its MIDI channel (default **ch.2**); **PC 0 = Live (follow knobs)**; save = send PC while holding both footswitches. The **uniform CC map** applies: knobs **CC14–20**, toggles **CC21–23**, footswitches **CC102/103**, hidden/alt **CC104**, **dips = CC61–68 / CC71–78**, expression-over-MIDI **CC100**.
  - **Whole-stack "scene" (Strategy A):** put the AM on the shared channel and save the **same preset number** as the other CB pedals for a song → one PC from the Digitakt 2 recalls the AM's drive preset alongside the rest of the board.

## Rig-specific AM moves over MIDI/CV
- Assign **EXP or CV → GAIN 1 or VOL 1** (CONTROL dip bank) to **ramp the push into Channel 2** during a drone; with the **MASTER** dip on, the ramp adds saturation without a level spike.
- Flip **HI GAIN / MASTER / BANK** dips remotely via their CC numbers (CC61–68 / CC71–78) inside a scene.
