https://valhalladsp.com/2011/05/23/valhallaroom-tips-and-tricks-gated-reverbs/ + https://valhalladsp.com/2011/05/23/valhallaroom-tips-and-tricks-short-drum-rooms/ + https://valhalladsp.com/2011/05/04/valhallaroom-early-reflections-versus-early-energy/ + https://valhalladsp.com/2023/11/20/valhallaroom-updated-to-2-0-0-new-space-lo-cut-controls/
Valhalla DSP (Sean Costello) "Tips and Tricks" blog series + v2.0.0 Space · 2011-2023

# ValhallaRoom — Early-engine tricks (depth, gating, Space drones)

## The Depth = 0% world (Early reverb on its own)
Setting **Depth to 0%** mutes the Late tail and exposes the **Early reverb** alone — the underused half of the plugin and a genuine sound-design space.

### Gated reverb (early-only)
- **Depth 0%** · **Predelay 0.0 ms** · **Early Diffusion 100%** · **Early Size ≈ 150 ms** (this sets the gate length) · High Cut to taste.
- Produces the percussive, time-defined 80s gated-drum tail (densified by diffusion, no natural decay). Add **Early Mod Rate/Depth** for chorused movement inside the gate.

### "Just early reflections" depth bed
- Community/ambient tip: for a sense of room **without a tail**, keep **Depth at 0%** and **Early Size small (< ~40 ms)** with some Diffusion. Sits a dry source in a believable small space — perfect as the *placement layer* under a separate long Late-reverb send. (This is the "depth bed" idea: Early-only Room for placement, then VintageVerb/long Room for the wall.)

## Early Energy vs Early Reflections (why it stays smooth)
Costello's distinction: ValhallaRoom's "early" stage isn't a sparse set of discrete taps like many reverbs — at high Diffusion it's dense **early energy** that won't turn metallic on vocals/drums. That's why you can crank Diffusion to 1.0 and keep Early Size large without the usual ringing — the foundation of its "always smooth, no harsh ring" reputation.

## Short drum rooms (the tight "glue" recipe)
- Small **Early Size** + small **Late Size** + short **Decay** (~0.3-0.8 s) + Diffusion high + a touch of Predelay. Tightens a dry source into a believable small room — the opposite end from the ambient walls, useful as parallel "glue" on drums/banjo to give them a place to sit.

## Space (v2.0.0) — drones from the Early engine
The **Space** control adds feedback around the predelay + early reflections. **Above ~60% the early reflections become their own self-feeding reverb.** Combined with a longish Early Size, high Early Mod Depth, and Diffusion, you can build a **lush modulated wash entirely from the Early section** — a different texture than the Late tail (more echo-y / metallic-resonant / diffuse depending on settings). A new, distinct route to evolving ambient beds; ships with a "SpaceScratchpad" preset to learn it. **★ the closest Room comes to a self-oscillating / blooming drone source.**
