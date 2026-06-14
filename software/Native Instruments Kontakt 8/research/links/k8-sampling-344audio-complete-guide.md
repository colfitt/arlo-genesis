https://www.344audio.com/post/article-how-to-build-a-kontakt-instrument-a-complete-guide-for-composers-sound-designers-part-3
344 Audio · "How To Build A Kontakt Instrument — A Complete Guide for Composers & Sound Designers" (Parts 1–3) · blog tutorial

# 344 Audio complete-guide — the written reference (concrete values)

A three-part written guide. Part 1 = planning/recording (concept, velocity
layers, round robins — mirrors NI FIRST STEPS Ch.1). Part 3 holds the
load-bearing concrete settings:

## Wave Editor — looping for sustained/pad sounds
- Open the **Wave Editor**, enable the **"Sample Loop"** tab → a **gold locator**
  appears over the waveform.
- Two parameters drive the loop: **Loop Start/End** (which section repeats) and
  **Crossfade** (fade length for a smooth join).
- **Concrete pad example:** loop **between 0.25 s and 0.75 s** with a **fairly
  short crossfade of ~500 samples**. (Widen the region for more variation in the
  loop; lengthen the crossfade if the join is audible.)

## Round robins (anti–machine-gun)
- Put samples in **separate groups**, each holding its velocity layers.
- **Group Editor → Group Start Options → "Cycle Round Robin"**, then manually
  assign each group's **position in the round-robin chain** sequentially.

## Effects — the two FX locations
- **Post-Amp FX** (brown tab): compressors, limiters, EQ, saturation.
- **Insert FX** (beige tab): reverbs, delays, modulation, dimensional effects.
- (Kontakt 8 ships NI's full effect library inside — Replika delay, convolution
  reverb, tape saturation, Reaktor filters — so a finished instrument needs no
  third-party plugins.)

## Extras
- **Arpeggiators / sequencers**: Script Editor → "Sequencing" sub-folder
  (rate, swing, note order) — useful for generative drone movement.
- **KSP scripting**: Script Editor → the Kontakt Script Processor language for
  GUI + envelope control across all groups (covered in depth by the sibling
  `k8-engine-*` transcripts in this repo).

## Rig relevance
The 0.25–0.75 s / ~500-sample numbers are a fast, safe starting recipe for
turning a short captured texture (an MPC one-shot, a pedalboard swell) into a
sustaining pad without the long-loop ceremony. Round-robin groups are how you
keep a sampled banjo or a sampled drum hit from machine-gunning when played fast.

> Source: 344audio.com "Complete Guide" Parts 1 & 3. Part 1 fetch returned only
> the planning/recording stage; Part 3 yielded the concrete Wave-Editor / FX /
> round-robin values above. Distilled.
