https://valhalladsp.com/2017/05/06/valhallavintageverb-1-7-1-chaos-reigns/
valhalladsp.com · Sean Costello · 2017-05-06 (Chaotic modes) + product-page color-mode notes

Deep detail on the Chaotic (tape) modes and the 3 color modes — the two features that matter most for the degraded/tape drone aesthetic.

---

## The CHAOTIC modes — "what if old-school digital reverbs were made with tape delays?"

Sean Costello's design intent and behavior:
- **Saturation & pre/de-emphasis** modeled on tape delays, with a HIGHER internal drive level than the other modes. This analog-style processing actually REDUCES ringing in the decay tail (clarity, not mud).
- **Modulation noise**: digital quantization noise is replaced by tape modulation noise → a broader, more broadband spread of frequencies as the reverb decays.
- **Chorusing**: uses "chaotic" modulation mimicking the wow / flutter / tape-crinkle noise of worn tape loops. Produces FEWER random pitch shifts than standard random-walk modulation.
- **Chaotic Chamber** adds signal-dependent diffusion parameters → a clearer-sounding tail.
- Lineage: Chaotic Hall ≈ Dirty Hall structure + chaos; Chaotic Chamber ≈ Smooth algorithms with analog artifacts swapped in for digital ones. (Chaotic Neutral added later, 2019: chaos on a colorless architecture — "sounds like the input.")
- Forum note (Delta Sign, KVR): Chaotic Chamber's saturation "glues the source and reverb together" — great for cohesive ambient textures.

**Takeaway for the rig:** Chaotic Hall / Chaotic Chamber are the tape-flavored ambient/drone tail modes — long decays that stay clear, with built-in tape wow/flutter and saturation. Pair with 1970s color for maximum degraded character.

---

## The 3 COLOR modes (the era artifact control)

- **1970s** — DARK, noisier modulation. Reproduces the reduced bandwidth of the earliest digital reverberators: **10 kHz max output frequency**, internally **downsampled** to recreate lower-sample-rate artifacts. The modulation is dark and noisy and can produce strange/random sidebands on sustained notes. → THE choice for the degraded, lo-fi, "recorded-wrong" drone aesthetic; sustained drones provoke its weird sidebands.
- **1980s** — still funky/dark, noisier modulation, BUT runs at **full bandwidth/sample rate** → brighter than 1970s, and produces different artifacts because it's at full rate. Early-digital vibe with more sparkle.
- **Now** — no downsampling, full bandwidth, bright, clean modulation. The transparent/modern setting (use when you want the space without the era grit).

Practical: color is often subtle on percussive/short sounds but becomes obvious on long sustained tails — exactly the drone/wall use case — because that's where the 1970s downsampling + noisy modulation generate sidebands and grain. Flip 70s/80s/Now on a held note to hear it.
