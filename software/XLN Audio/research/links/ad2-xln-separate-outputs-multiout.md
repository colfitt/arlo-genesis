https://support.xlnaudio.com/hc/en-us/articles/22338657251101-Addictive-Drums-2-Separate-Outputs
xlnaudio.com (official support) · XLN Audio · accessed 2026-06-11 (page itself returns 403 to bots; content triangulated from XLN PDF + search-indexed text + Airfix/Ableton-forum mirrors)

# AD2 Multi-Out / Separate Outputs — the core routing feature

Multi-out = assign each drum (or sub-group) of AD2 to its own DAW track so you can
EQ/compress/sidechain/DEGRADE each drum independently. This is THE feature for the
owner's "degrade individual drums" goal.

## Instantiate the multi-out plugin variant
- AD2 ships as several plugin variants. Load the **Multi-Output** version, NOT the
  stereo one: typically "Addictive Drums 2 (4x Stereo, 10x Mono)" or similar in the
  instrument list. (Logic exposes these as separate AU entries; Ableton as separate
  device entries.) If you load the plain stereo version you only get one output.

## Turn on per-channel routing INSIDE AD2 (the down-arrow)
- Open AD2 → **Kit** page (or **Mixer** view). Each drum channel has a small
  **down-arrow [↓]** at the bottom of its channel strip.
- Click the arrow on every channel you want on its own output. **Arrow turns green**
  = that channel is now sent to a discrete output instead of the AD2 stereo master.

## CRITICAL GOTCHA — routed channels BYPASS AD2's master channel
- "When you route a channel from AD to a separate channel in your DAW, it will no
  longer go through the Master channel in AD2." Any **Master-bus FX, master EQ, or
  master compression inside AD2 is bypassed** for routed drums.
- Practical consequence: if you've dialed in glue/character on AD2's master, you will
  NOT get the same sound after going multi-out. Two options:
  1. Do all your glue/character DOWNSTREAM in the DAW (preferred for this rig — that's
     where RC-20 / Decapitator / SketchCassette / DS-10 live anyway).
  2. Or keep the kit on AD2's master and only route a couple of drums out.
- The **Delerb (FX1/FX2) sends and the Bus channel are also internal** — decide
  before routing whether you want AD2's reverb baked in or want dry stems to wash
  externally with VintageVerb/Room.

## Audio vs. instrument tracks
- The receiving DAW tracks are **aux/audio tracks fed FROM the AD2 instrument**, not
  new instrument instances. One AD2 instance feeds all the separate outs.
