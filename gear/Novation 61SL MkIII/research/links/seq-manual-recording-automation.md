Manual: SL MkIII User Guide V2, p.11–12
Novation manual

# Live record, momentary record, quantise, automation, mute/solo

## Live Record
- Press **Record** on the Transport to enable live recording. Press Record while playing to **punch in.**
- If transport stopped: press **Record**, then **Play** to begin.
- While recording, notes played on the keyboard or from **MIDI (USB and DIN)** record into the sequence.
- From MIDI, a Part records **only notes on its own selected MIDI channel**; notes also forward to the Part's output whether recording or not.
- **Quantise behaviour (default ON):** `note on` events quantise to the **playing pattern's Sync Rate**; `note off` events quantise to the **nearest 24 PPQN tick.** The sequencer loops each pattern chain so you **overdub** as it repeats.
- Set Pattern Settings + chain length **before** recording to fit your performance.

## Momentary Record
- **Hold Record** while the sequencer plays → records only **while held.** Release to stop recording and leave the sequencer playing. (Punch-in by hold.)

## Record Quantise — Non-Quantised Record
- **Shift + Record** toggles Record Quantise. 5th screen briefly shows status.
- When **disabled**, live notes record to the **nearest Tick (1/6th) of a step** → looser, more human feel.
- Edit the recorded positions in **Micro-steps view** (see seq-manual-micro-steps.md).

## Automation (8 lanes per track)
Automatable Template controls: **Rotary Knobs, Faders, Soft Buttons, Pads (press/release & pressure), Pitch & Mod Wheels, Pedals.**
- Move a control while recording → its LED/screen lights **red** and it overwrites existing automation as the transport advances. Recorded/played back at **24 PPQN** regardless of the pattern's Sync Rate.
- **Disable record ASAP** so you don't overwrite when the pattern loops.
- **Up to 8 automation lanes per Track.** 5th screen warns **"Automation lanes full for part"** when no lanes remain.
- **Cannot** automate: rotaries/controls assigned to song position. Pads/buttons that output **note** messages record as **notes**, not automation.
- **Show which controls have automation:** hold **Clear** → controls with automation in the current pattern light. Move one while still holding Clear to **clear its automation** in that pattern.
- **Automation view:** Patterns view → **Options**. Each control type + named automated controls show as "lanes." Soft buttons select Track. Hold Clear + turn a control's rotary to clear that lane.
- **Manual step automation:** with sequencer **stopped**, press Transport **Record**, press a pad (= Step Edit mode, auditions the step), move a control to assign that value to the step, then **disable record** before releasing. Only the **most recent** control value is stored per step → to capture a momentary button/pad *press*, turn off record or select a new step to record the release first.

## Mute / Solo Parts
- In Sequencer view, click the soft arrow far-right (left of "61SL MkIII" label) → Mute/Solo view.
- **Mute:** top row of **yellow** soft buttons. Muted Part outputs no MIDI but you can still play keys / audition pads for it.
- **Solo:** bottom row of **blue** soft buttons. Soloing silences all non-soloed Parts (unless already muted). A silenced Part's Mute button **pulses yellow.**
