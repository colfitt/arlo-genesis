https://www.airfixmusic.com/blog/how-to-use-separate-outputs-with-addictive-drums
airfixmusic.com · Martin Aubin · 2020-04-08

# How to use separate outputs with Addictive Drums (generic DAW walkthrough)

Covers Pro Tools / Cubase / Logic-style hosts. The transferable signal:

## The two output modes on each AD2 channel (the down-arrow menu)
- Click the **small arrow at the bottom of any drum channel** in AD2's mixer panel.
  You get a choice:
  - **Pre Fader** = bypass AD2's internal mixer for that channel (raw, before AD2's
    channel fader/FX) — cleanest source for downstream degrading.
  - **Post Fader** = retain AD2's channel settings (its EQ/comp/level) on the way out.
- Arrow goes **green** → AD2 auto-creates the send buses for that channel.

## Receiving-track recipe he uses
- Create **10 mono tracks** for individual drums (kick, snare, hats, toms…) and
  **3 stereo tracks** for **overheads, room mic, and a parallel-compression bus**.
- On each receiving track: **Input → Plug-in → Addictive Drums → [choose the drum
  source]**. Repeat for all.

## Why this matters for the rig
- The **Pre Fader** option is the move when AD2 is just a *clean source*: take the
  raw snare/room out pre-AD2-FX, then degrade it externally (RC-20, Decapitator,
  SketchCassette, Lossy, DS-10) on the DAW track.
- The dedicated **room-mic stereo out** is the one to wash with VintageVerb / send to
  the tape pedals — keep the close mics dry and punchy, drown only the room.
