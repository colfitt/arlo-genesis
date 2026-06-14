https://forum.vintagesynth.com/viewtopic.php?t=77739
forum.vintagesynth.com · "Xpander/Matrix 12 tips and tricks" thread · undated

Hardware-owner programming wisdom for the Oberheim Xpander/Matrix-12 architecture (the exact
voice + mod-matrix engine Arturia models). The deepest practical-technique source.

## Modulator tricks (the evolving-pad core)
- **Self-modulation:** route an **envelope → an LFO's speed** so the LFO accelerates/
  decelerates over the note — living, non-static motion.
- **Nested modulation:** **LFO → another LFO's rate** (FM one LFO with another) → the modulator
  itself never repeats. (This is the Matrix-12-native way to do the universal "unsynced
  conflicting rates" evolving trick — but done *inside* the matrix, deeper than the Advanced
  panel.)
- **Lag/Tracking inputs:** the **Lag** processor smooths a CV source (turns a square LFO into a
  rounded/sine shape — instant glide/portamento and softened steps). **Tracking** generators
  remap a source per keyboard range (different mod behavior high vs low).

## Filter favorites
- The **3-pole low-pass often sounds better than the 4-pole** for general/pad use; reserve the
  **4-pole for FM patches.**
- The **high-pass filter is notably superior** to typical synth HPFs — useful for thinning a
  pad to sit under a banjo/baritone without mud.

## Voice / output
- Hardware had **6 individual outputs** → route voices to separate processing for parallel
  layered design. (In the plugin the analog = per-voice pan + Multi zones into the DAW; the
  spirit is "spread the 12 voices across space and processing.")
- **Multi-patch mode + per-voice panning** is repeatedly cited as what gives the synth its
  character.

## Philosophy
"Just because you could, it didn't mean you had to" — **simple patches often win**; restraint
beats max routings. (Reassuring for a drone rig: a few slow modulators on cutoff/pitch/pan is
enough; you don't need all 40 slots.)
