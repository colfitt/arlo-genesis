https://whylogicprorules.com/summing-vs-folder-stacks/ · https://gearspace.com/board/apple-logic-pro/940286-folder-stack-vs-summing-stack.html
whylogicprorules.com + gearspace.com · community · current

# Track Stacks: Summing vs Folder — for layering drone beds & summing the rig

Two kinds of Track Stack (select tracks > Cmd-Shift-D / right-click > Create
Track Stack). They look similar but behave very differently — pick the right one
or you limit your mix.

## Folder Stack
- Pure **organization** — groups tracks under one header. The folder channel
  gives basic fader/solo/mute over the group but does NOT create a real bus.
- No sub-mix routing; you can't insert one reverb that processes the whole group
  as a sub. Use for tidiness only (e.g. collapse 8 Digitakt stems).

## Summing Stack (the mixing one)
- Routes all contained tracks to a single **Aux (sub-channel)** — a real
  sub-mix bus. Insert FX on the summing aux to process the whole group
  (parallel comp, a shared reverb, bus saturation, SketchCassette on the whole
  texture group).
- Adjusting the Summing Stack fader changes level **after summing** — the
  individual track meters don't move (you're riding the sub, not offsetting each
  track). This is the "pro" behavior.
- Creating a Summing Stack auto-assigns a bus and builds the aux for you.

## Nesting limitation (gotcha)
"In Logic you can only nest another Folder Stack OR a Summing Stack inside a
**Folder Stack**" — you cannot freely nest summing stacks inside summing stacks.
Plan hierarchy accordingly (e.g. one Folder Stack holding several Summing
Stacks for sub-busing).

## Factory layered stacks worth stealing
The Library ships rich multi-track stacks — e.g. **"Blippy Waves"** (Arpeggiator
/ Synth Layers) and **"Parallel Universe"** (Synthesizer / Soundscape) — load
one to see a pro ambient layering/routing setup, then swap your own sources in.

## Rig recipes
- **Summing Stack per zone**: one for the "drone bed" (Sample Alchemy + pads),
  one for "rhythmic hardware" (Digitakt/MPC stems), one for "live guitar/banjo."
  Bus-process each, then sum to the master.
- Put the shared "recorded-wrong" chain (SketchCassette / Lossy / Tape) on a
  Summing Stack aux so a whole layer degrades together rather than per-track.
- Drop the 8 Digitakt Overbridge stems into a Folder Stack for tidiness, OR a
  Summing Stack if you want one bus reverb across the kit.
