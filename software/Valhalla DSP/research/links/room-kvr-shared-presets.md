https://www.kvraudio.com/forum/viewtopic.php?t=339477
KVR Audio · Valhalla DSP Forum · "Post yer ValhallaRoom Presets" thread (Bronto Scorpio et al.) · ~2011–2014

# ValhallaRoom — real user-shared presets (concrete values)

Actual community presets posted to the official KVR Valhalla forum. Values are in the
plugin's **normalized 0–1 internal scale** (how the .xml stores them), not seconds/Hz —
treat as **relative starting points** (e.g. `decay=0.049` ≈ a longish-but-not-extreme
tail, `lateSize=0.9` ≈ near-max room, `diffusion=0` = sparse/slappy). Most useful as a
"someone aimed at this vibe and landed near these knobs" reference. Several lean dark /
grainy / modulated — i.e. squarely in this rig's lane.

## Dark / ambient / drone-leaning presets (by "Bronto Scorpio")
- **Oort Cloud** — *dark, grainy reverb.* mix 0.25 · decay 0.049 · predelay 0.05 ·
  HighCut 0.597 · earlyLateMix(Depth) 0.85 · lateSize 0.9 · lateModRate 0.192 ·
  lateModDepth 0.05 · **diffusion 0** (sparse, grainy). → a big, dark, slightly gritty
  space; diffusion at 0 keeps it textured rather than smooth.
- **Andromeda** — *ambient.* mix 0.4 · decay 0.059 · predelay 0.04 · HighCut 0.329 (dark) ·
  Depth 0.8 · lateSize 0.85 · **lateModDepth 0.7** (lush) · **earlySend 0.7** ·
  diffusion 0.5. → swelling, dark, heavily modulated ambient wash with early energy fed
  into the tail. The closest of these to a "drone bed."
- **Nerevar** — *very simple, long and grainy.* mix 0.3 · decay 0.099 (long) · predelay
  0.05 · HighCut 0.631 · **lateSize 1.0 (max)** · lateModRate 0.293 · diffusion 0.3. →
  the minimalist long-tail wall.
- **Mod Matrix** — *modulation-heavy, for pads & drums.* mix 0.2 · decay 0.001 (tiny) ·
  HighCut 0.732 · **lateModRate 0.394 + lateModDepth 0.5 + earlyModRate 0.697 +
  earlyModDepth 0.55** · diffusion 1.0. → almost no tail, all chorus/movement — a
  modulation texture, not a space. Good as a subtle shimmer-of-motion layer.
- **Gates Of Albion** — *"weird, modulated, gated" special effect,* not a real reverb.
  mix 0.3 · decay 0.007 · lateModRate 0.111 · lateModDepth 0.2 · **earlySize 1.0 +
  earlyCross 1.0** → uses the Early engine alone as a gated/widened effect (the Depth-0%
  Early-engine trick the draft flags).

## Big-hall preset (by xtrax / Den, ported from a Gearspace share)
- **Nostro Grand Hall** — mix 1.0 (full wet, send-style) · decay 0.031 · HighCut 0.336
  (dark) · **lateSize 1.0** · **earlySend 0.85** · diffusion 0.9. → large, smooth, dark
  hall with a strong early→late feed; a clean "big realistic wall" starting point.

## Takeaways for the guide
- **Diffusion is a real character control in practice:** the dark-ambient presets sit at
  **0–0.5** (grainy/textured), the hall presets at **0.9–1.0** (smooth). The "leave it at
  1.0" advice is for *clean* spaces; **drop it for grit.**
- Several presets pair **dark HighCut + high lateModDepth + earlySend up** — the recurring
  recipe for a moving, dark, swelling wall.
- Other contributors (moocher's AdamUs / WaterBaby / perturb / iniquity sets;
  peter.m.junior's "Sound 29" collection) posted banks but without inline parameter
  dumps in-thread.
