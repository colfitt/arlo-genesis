https://www.youtube.com/watch?v=E6ysy8RHmJY
DivKid · Novation SL MkIII with Eurorack Modular Synths // Sequencer, keyboard & controller · 2018-10-10

The CV/modular reference video — DivKid uses the SL MkIII purely as a CV/Gate/Mod + analog-clock brain for a Eurorack patch (Mutable Instruments Braids "Brds" and Elements granular). This is the best single source for the rig's "MIDI-to-CV bridge" role.

## Physical CV patching
- **Pitch out → 1V/oct (V/oct) in on Braids.**
- **Gate out → trigger input.**
- **Mod out → a modulation destination** (the "vowel"/timbre mod-in on Braids).
- He uses **two CV outputs**: CV-Mod 1 (mod wheel) and CV-Mod 2 (a recorded automation lane). Also uses **gates** and the **analog clock out** to generate rhythms, and pitch CV to modulate a kick.

## Building the rhythmic CV sequence
1. Clear the pattern. Start a pattern at e.g. **two steps**; punch in a quick rhythm on a single note (C) for a static rhythm.
2. **Assign the Mod wheel as a CV mod source**: in **Global**, CV-Mod Out 1 is set to **CC 1** (so the mod wheel's CC1 drives that CV output).
3. **Step-record mod CV**: hit record, hold a step, then move the **mod wheel** while holding — the step goes red to show it's automated. Play → that step now outputs the recorded mod CV.
4. **Live-record mod CV**: clear, hit record, simply move the mod wheel while it plays — captured as automation.
5. **Build a 4-bar pattern**: **Patterns → Duplicate** (press source pattern, then destination) to copy onto pattern 2; do it again for a 4th pattern, but change some notes and **step-record more mod-wheel moves** in Steps.
6. **Chain patterns**: Patterns view → press the patterns you want chained.

## The full patch (what the SL drives)
- Session 2; 4 chained patterns. **Part 1 = kick** (pitch CV), **Part 2 = snare/clap**, **clock out** generates a hi-hat/shaker (PPQN trick below), plus a **droning granular sample** driven by the mod wheel.
- Red key-LEDs above the keybed show which notes the sequencer is currently outputting as CV pitch.
- CV-Mod Out 1 (mod wheel) controls **position in the granular sampler/loop**; CV-Mod Out 2 controls **feedback** in the effects chain. The granular drone is side-chained — stopping the SL stops the side-chain in the modular.

## Clock-out trick for the hi-hat
- **Global → Clock Output PPQN**: MIDI is often 24 PPQN, but he sets it to **4 PPQN** to get a steady 16th-note (four-pulses-per-quarter) pattern straight off the clock out into a percussion trigger — no sequencer steps needed for that part.

## Gate-length as a modulation source (the musical takeaway)
- In **Options (Steps)** you see velocity, gate, and pattern. The little signal bars on the **gate** show step length.
- Because Braids/Elements respond to gate length, **varying per-step gate** creates complex tonal modulation: longer gates make notes **swell and breathe** through the reverb/delay; short gates **"ping"** the delay. He deliberately makes some steps very long (extending past the next step), which "ties gates together" and creates a fluttering, human, non-uniform groove. His framing: modulate gate length, not just pitch.

## Pattern length / sync per CV part
- **Options → Pattern**: change start/end point — yellow = active range, red = present-but-not-played steps. A 7-step pattern against the others creates the flutter at the loop boundary.
- **Per-pattern sync rate** here too (he shifts from 1/16 to 1/8 relative to the master clock). Each of the 8 parts (first two are his CV parts) can run different step lengths AND different clock rates for very complex polyrhythmic sequencing.
- Teases future videos on **polymetric patterns** (layering tracks of different lengths) and using the arpeggiator into modular.
