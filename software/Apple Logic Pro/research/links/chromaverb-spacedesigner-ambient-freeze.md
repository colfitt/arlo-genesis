https://musictech.com/tutorials/using-chromaverb-logic-pro-x/ · https://www.production-expert.com/production-expert-1/when-do-you-use-space-designer-for-reverb-and-when-do-you-use-chromaverb-see-if-our-expert-panel-agrees-on-the-answer
musictech.com (Mark Cousins, 2018-05-11) + production-expert.com (expert panel, 2019-11-27)

# ChromaVerb vs Space Designer for ambient/drone, + the Freeze infinite-tail trick

## When to reach for which (expert panel: Vandeviver, Rothermich, Krantzberg, Chevalier)
- **Space Designer = convolution** (real impulse responses). "Set and forget,"
  natural glue/ambiance, realistic rooms for drums/vocals. **Higher CPU**
  (convolution). Good when you want a believable space and "move on."
- **ChromaVerb = algorithmic.** "Much lower CPU." Greater creative control —
  special-effect tails, "a sound I can't describe," emotion. The **Damping EQ**
  lets resonant frequencies die away faster. This is the drone/shoegaze pick.

## ChromaVerb concrete settings (Cousins)
- Drum-tight starting point: **Size ~40%, Decay ~0.87 s.**
- **Pre-Delay tempo-synced** to a 1/16 note for rhythmic reverb; Decay can also
  **tempo-lock** to a subdivision.
- **Damping EQ** shapes color over time (e.g. cut lows so tails get brighter
  as they decay).
- **Distance** parameter "blurs" by moving the virtual mics back — useful for
  smeared, far-away walls.
- **Algorithms** set the base character: Theatre, Dark Room, Smooth Space,
  Reflective Hall. "Smooth Space" / "Dark Room" suit drone beds.

## The Freeze infinite-ambient trick (THE key drone move)
- ChromaVerb has a **Freeze** button. Pressing it "suspends" the reverb at the
  exact moment you hit it — it holds whatever was feeding the reverb as a
  constant pad-like tone until you un-freeze. (Like the held wash behind Kate
  Bush, "Running Up That Hill.")
- **Automate the Freeze button** so the infinite tail becomes a dynamic,
  arrangeable element — freeze on a chord, ride it under the next section,
  release it.
- For walls: long Decay (the tutorials note you can push decay toward ~30 s for
  a "wash"), Freeze, then **Bounce in Place** the held tail to commit it as a
  texture stem.

## Rig note
ChromaVerb Freeze + a long Decay is the software analog of the user's hardware
sustain pedals (CB MOOD/Big Time, Microcosm). Print the frozen wash to audio,
then re-degrade it through SketchCassette/Lossy or reamp it out through the
Apollo into the End/Time→Tape board.
