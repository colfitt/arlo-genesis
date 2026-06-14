https://www.youtube.com/watch?v=rpL_0rlLjSk
Flo of Music · How to use Valhalla Vintage Verb? · 2023-11-13

The single clearest control-by-control walkthrough of VintageVerb found. Explains every knob in plain language — especially the Bass Mult/Bass Freq multiplier behavior and the damping high-shelf, which most demos gloss over.

---

Reverb is an essential plug-in you use on all your tracks. There are many stock reverbs (covered in other tutorials), but today we look at Valhalla VintageVerb, a reverb used on the majority of my projects. I'll teach you exactly what all the knobs do so you can try them on your tracks.

**COLOR** — the first button. Three options: 1970s, 1980s, and Now. Each shows a description below when selected:
- **Now**: "no downsampling, full bandwidth, bright, clean modulation" — a very bright reverb.
- **1980s**: "no downsampling, full bandwidth" but with **dark, noisier modulation**.
- **1970s**: also dark, noisier modulation, AND it is **downsampled** with the bandwidth limited to **10 kHz** — there is a frequency change there. Choose based on the song; for a pop song with vocals I'd probably choose Now.

**MODE** — right next to color. Currently Concert Hall; click it and you get all the different modes/algorithms. Pick e.g. Plate and you get a description: "fast and diffuse attack, bright tone, fast build of echo density, chest modulation." Read the description as you change modes and pick the one that fits the track.

**PREDELAY** — the moment the dry signal comes into the plug-in, when does the reverb kick in? After 15 ms or a much later time like 112 ms? Determined by predelay.

**MIX** — once predelay is set, how much reverb do you want to hear? At 23%, only 23% of the reverb merges with the dry signal. At 100%, the entire reverb is heard along with the dry signal.

**DECAY** — how long you hear the reverb. Ranges from 2 seconds to as long as **70 seconds**. (Color/Mode/Predelay/Mix/Decay are also on Logic's stock reverb; the rest of the knobs are why you'd reach for VintageVerb as a third party plug-in.)

**DAMPING** — two sets: high frequency and bass frequency.
- **High Frequency**: dial a frequency (e.g. set from 6,000 Hz down to 3,100 Hz). From that frequency you apply a **high shelf**. Kept at 0 dB = no change. If the reverb is giving too much high frequency, do a high shelf cut — e.g. -4 dB at 3,100 Hz attenuates the higher reverb content. You can go as low as **-24 dB**, which is almost like a high cut.
- **Bass Frequency** works differently. Set decay to a round number like 2 s. Select a bass frequency (e.g. 290 Hz) and a multiplier knob. If the multiplier is **1.5**, it multiplies into the decay: 1.5 × 2 s = 3 s. So below the bass frequency you hear a **longer** reverb (3 s) while the rest stays at 2 s. (Set below 1.0 to make the bass decay shorter than the rest — keeps mud out of long tails.)

**SHAPE**:
- **Size**: lower percentage = small room, higher = bigger room; the reverbs differ accordingly.
- **Attack**: the initial attack of the reverb. Lower attack % = the reverb acts immediately, you get the initial reverb sound right away. Higher attack % = takes longer to have that attack (slow swell).

**DIFFUSION** — early diffusion and late diffusion are like the reflections. They set how long it takes those reflections to reach your ear. With both very short/low it almost sounds like a delay (you get the ambient sound but sparse, like discrete repeats). With both high you hear the reflections really well; the tone of the reverb changes accordingly.

**MODULATION** — like a chorus effect. Increase/decrease depth and change rate; you'll hear a chorus effect on the reverb tail, just like Logic's stock chorus but working on the reverb, not the dry signal.

**EQ** — two knobs: high cut and low cut. Usually I tell people to add a low cut after the reverb (reverb accumulates low frequencies that eat headroom); here it's built in. Cut below ~80 Hz, and high-cut if you want.

**Presets** — lots to choose from (Ambiences, Room, etc.). Changing color to 1980s changes how it sounds (dark and noisier modulation) while the knobs stay the same.

**Workflow**: I normally don't add reverb directly on the channel strip; I put it on a **bus/return**. Mix sometimes at 100% with the send controlling the amount, or send everything and control with mix — it works both ways. It boils down to how you use reverb. A really good reverb that gives natural tones to your song.
