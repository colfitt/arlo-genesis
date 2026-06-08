Manual: SL MkIII User Guide V2, p.6–9
Novation manual

# Steps view — entering & editing notes per step

## Entering notes
- **Select the Track/Part** with the soft buttons directly below the screens.
- **Add notes (method 1):** press and **hold a pad** (= a Step), then press the **key(s)** you want that step to trigger. Poly — multiple keys = a chord on that step.
- **Add notes (method 2, reverse):** press and **hold the key(s)** first, then tap any **pads** to populate them with those notes.
- **Live record:** press **Record** on the Transport to play notes/automation in live (see seq-manual-recording.md).
- **Remove a note:** press and **hold a pad** → the keys with notes light **red**; press those key(s) to remove. (If Transport is stopped, holding a pad plays the step's notes out to the Part at their stored velocities.)
- **Clear a whole step:** hold **Clear** + press a Step (briefly red) → removes all note + automation data on that step. Works whether transport runs or is stopped.
- **Copy a step:** hold **Duplicate** + press a pad to copy, keep holding Duplicate + press destination pad(s) to paste. **Paste erases the destination, not adds to it.**
- **Copy steps between Tracks:** hold Duplicate, press a pad, change Tracks (Duplicate still held), press pads to paste. **Automation data does NOT copy between tracks.**

## Per-step parameters — Options menu (Steps view → Options)
Press **Options** in Steps view → soft buttons select **Velocity / Gate / Chance / Pattern**. Press Options again to exit.
- **Set all steps at once:** in Velocity/Gate/Chance menu, **hold Shift + turn encoder 1** to set that value for all steps in the pattern (only affects steps that have notes).
- Steps 1–8 show on screens (2 per screen, top pad row). **Up/down arrows** left of screens page to steps 9–16 (bottom pad row).

### Velocity
- Turn the **knob above a step** to set velocity **1–127** (fine precision).
- The screen shows the **highest** velocity of all notes on a step (multiple velocities may exist).
- Multi-note steps **snap to one uniform value** when you turn the knob — the SL favours/snaps toward higher values. (e.g. notes at 25 & 89, turn right → both snap to 90+; turn left → both snap to 88 or lower.) After snapping, **new notes added to that step adopt the group velocity.**

### Gate
- Turn the **knob above a step** to set gate length.
- **Range: up to 32 steps** (notes can be longer than the pattern). Default = **1 step.**
- Gate is measured as **steps + sixths**: each step = **6 fractions** ("2 steps ■■■" etc.). 5 white boxes on screen show the fraction count.
- Gate is a MIDI note-length only — a 16-step gate won't *stretch* a short hi-hat sample; it just holds the MIDI note 16 steps long.

### Chance (probability)
- Turn the **knob above a step** to set chance the step plays, per step.
- 50% = equal chance all-or-none of that step's notes play.
- **0% = the step never plays → use as a step-mute without deleting notes.**
