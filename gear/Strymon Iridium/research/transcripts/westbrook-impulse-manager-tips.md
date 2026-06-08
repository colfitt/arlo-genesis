https://www.youtube.com/watch?v=SpsO9cB6EOI
Michael W. Westbrook · Strymon Iridium Impulse Manager: Tips and Tricks with IR's · 2021-01-28

The deepest practical tutorial on the Impulse Manager software and on getting the most out of Iridium's stereo IR system. ~12 min. This is the key "load custom IRs / use it as a convolution box" reference.

## Impulse Manager basics
- Left column = browse your computer for 3rd-party / custom 24-bit 96 kHz WAV IRs (up to 500 ms). Right side = the 9 Strymon factory Cab slots + your saved Collections.
- Drag-and-drop an IR into the LEFT, RIGHT, or MONO (center) section of a Cab slot. After editing, hit SYNC CHANGES to write to the pedal.
- Build a COLLECTION: drop in your chosen IRs and "Save Collection" — recall later.
- Per-slot/per-side INFO ("i") button gives a LEVEL trim plus general TREBLE and BASS adjustment for each IR. Use these to BALANCE mismatched IRs so switching cabs on the pedal stays in the same loudness/tone ballpark.

## The stereo IR superpower (the headline depth)
- Iridium is stereo, so each cab slot can hold a DIFFERENT mono IR on LEFT vs RIGHT — effectively building a custom 2x12 with two different speakers (e.g. Greenback on the left, Celestion Alnico Gold on the right), or the SAME speaker captured with TWO different mics (e.g. SM57 on one side, Royer 121 on the other). Gives a wider, fuller stereo image with more frequency separation.
- Balance caveat: a brighter speaker/mic on one side leans the image to that side — use the per-side level/treble/bass trim to re-center it. A ribbon (121) side is darker/bassier than a dynamic (57) side, so trim accordingly.
- For MONO use (or to avoid phase issues), drop ONE IR into the CENTER (mono) slot — same IR both sides; more direct, focused, centered tone, and you still keep the stereo ROOM effect.

## Phase warnings
- Even an "in-phase" IR can have specific frequencies that cancel when blended L/R. Mixing IRs from DIFFERENT manufacturers often does NOT combine well (phase mismatch). Mixing IRs from the SAME manufacturer is generally safe to blend.

## Wide-stereo DIY IR trick (for playing alone)
- In a DAW, take a mono IR, DELAY it 9 ms (Haas), consolidate to a 500 ms grid (Iridium's max IR length), and load that delayed version on one side + the original on the other. Creates a very wide stereo image that feels great solo. NOTE: do NOT do this if the signal will be summed to mono — it causes phase cancellation; pointless in mono.

## Unorthodox amp+cab pairings he likes
- AMERICAN-style (Fender) speaker IRs on the PUNCH (Plexi) model set clean → a cool clean sound that sits between American and British voicing.
- ROUND model with an American speaker on one side + a British speaker on the other → hybrid voicing. "There are no rules" mixing IRs and speaker types.

## Relevance to this rig
- This is exactly the path to use Iridium as a general convolution loader: load any 24/96 WAV up to 500 ms (bass cabs, etc.), trim per-side, build Collections, SYNC. Combined with AMP DISABLE (firmware 1.32+) it becomes a stereo IR box for non-guitar sources (e.g. the Jazz Bass with a bass-cab IR).
