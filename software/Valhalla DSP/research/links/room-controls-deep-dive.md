https://valhalladsp.com/2011/05/02/valhallaroom-the-high-level-sliders/ + https://valhalladsp.com/2011/05/18/valhallaroom-the-early-controls/ + https://valhalladsp.com/2011/05/04/valhallaroom-early-reflections-versus-early-energy/ + https://valhalladsp.com/2023/11/20/valhallaroom-updated-to-2-0-0-new-space-lo-cut-controls/ + https://splice.com/blog/valhalladsp-valhallaroom-huge-reverb-in-a-compact-interface/
Valhalla DSP (Sean Costello) blog + Splice walkthrough · 2011-2023

# ValhallaRoom — every control, what it does, useful values

## The dual engine (the core concept)
ValhallaRoom = **two stereo-in/stereo-out reverbs in series-ish parallel: an EARLY reverb and a LATE reverb.** The **Depth** knob is the crossfader between them. This is the single biggest difference from VintageVerb (one processor) and the source of Room's "depth/placement" realism.
- **Early reverb** = the first reflections / room signature / sense of distance & placement. Can do subtle short bursts up to gated reverbs ~1 s.
- **Late reverb** = the diffuse decaying tail / body. Natural decays **0.1 s – 100 s**.

## High-level sliders (top row)
- **Mix** — dry/wet, sine/cosine equal-power crossfade so level stays constant. On a send/aux run **100% wet**.
- **Predelay** — delays the onset of BOTH early and late reverb (ms). "Establishes the size of the room — moves the walls in/out." Classic trick: tape echoes added 15-30 ms before chamber/plate reverbs. Adds space between source and tail → clarity. *Workhorse rule: keep 0-20 ms if unsure (0-10 safest); past ~50 ms it's a slapback.*
- **Decay** — the high-level decay (RT60) for the **Late** reverb, based on mid frequencies. The Bass/High Mult controls then bend the lows/highs around it.
- **High Cut** — −12 dB/oct lowpass (Hz). **3000-7500 Hz is optimal for most larger rooms**; higher for chambers/plates/bright digital. Also subjectively pushes a source "further back" by tightening it.
- **Lo Cut** (added v2.0.0) — stereo low **shelving** filter that progressively cuts lows as the cutoff rises. "A less bass-heavy sound, easier to integrate into a modern mix." (Long-awaited — pre-2.0 you had to EQ the return for this.)
- **Depth** — early/late balance, equal-power. **0% = Early only** (close, placement, reflections), **100% = Late only** (the body/tail). Simulates mic distance / close-mic vs room-mic blend.

## Early section controls
- **Early Size** — duration of the early energy (ms). **10-50 ms** = early reflections of a small space / stereo widening; **50-100 ms** = a compressed room; **>100 ms** = gated-reverb territory. (Workhorse: it does attack+decay for the early reflections in one knob; dial it FIRST — it's the biggest determinant of perceived size.)
- **Early Cross** — stereo cross-mixing of early energy. 0% = no L/R mixing (preserves input image); higher = more cross-mix + more echo density. (Both presenters: subtle.)
- **Diffusion** — echo density of the early reverb. Low = distinct individual reflections (delay/slap-like); high = smeared wash. **Unusually, high Diffusion does NOT go metallic on vocals/drums — leave it at 1.0 for most purposes.**
- **Early Mod Rate / Depth** — chorus on the early reflections. **0.25-0.5 Hz warms the sound; 1-2 Hz adds a string-ensemble effect.** Higher depth = bigger spaces / vintage-digital emulation; lower = realistic.
- **Early Send** — routes early reflections INTO the late reverb. 0 = the two run parallel; 1.0 = max. Trick: Early Size 150 ms+ with Send 1.0 = slow cathedral-like onset; smaller Early Size + full Send = denser tails. (It feeds the early "epic delay" into the late body.)
- **Space** (added v2.0.0, Early tab) — feedback around the predelay + early reflections. Default 0% = original behavior; audible ~25%; **above ~60% the early reflections become their own independent reverbs.** Makes "diffuse modulated echoes, realistic short decays, metallic early resonances, lush modulated reverbs." *★ NEW drone tool: you can build a whole modulated reverb from the EARLY section alone with Space — a self-feeding wash distinct from the Late tail.*

## Late section controls
- **Late Size** — size of the late space = the BODY of the reverb. Bigger = more expansive + more audible internal delay/echo. Default ~15. (Workhorse: keep at 15 and shape with Early Size if unsure.)
- **Late Cross** — stereo coupling of the tail; low = keep input image, high = L/R spread/intermingle. (On Sulaco, this is what moves the stereo image.)
- **Late Mod Rate / Depth** — chorus on the tail; controls how "wishy-washy"/lush it sounds. **~0.5 Hz smooths artifacts in the decay; above 1 Hz adds lush chorusing.** Full depth detunes the tail heavily.
- **Late Diffusion** — density of the late tail.

## The frequency-dependent decay (bottom row) — the bloom-shaping engine
Three-band decay control that bends the global Decay per frequency band:
- **Bass Xover (Hz)** — splits low from mid. Everything below it is scaled by **Bass Mult**.
- **Bass Mult (×)** — multiplies the Decay time for the lows. **0.5× = lows decay in half the time** (e.g. 10 s Decay → 5 s lows); **2× = lows ring twice as long** (→ ~20 s). **Set Bass Mult < 1 to keep long tails out of the mud; > 1 for a blooming, swelling low-end drone.**
- **High Xover (Hz)** — splits mid from high; everything above it scaled by **High Mult**.
- **High Mult (×)** — multiplies the Decay for the highs. <1 = dark/closing tail; **>1 = the highs ring LONGER than the body → a rising, shimmer-adjacent sheen on the tail (the closest Room gets to a "shimmer" trick — push High Mult above 1 with a high-ish High Xover).**
