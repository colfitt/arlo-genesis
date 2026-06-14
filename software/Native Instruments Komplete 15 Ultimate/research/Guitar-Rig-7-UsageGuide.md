# Guitar Rig 7 Pro — Usage Guide

NI's amp/cab sim that's really a **modular FX rack** — for this rig, an all-in-one box for
walls, lo-fi degrade, and processing **non-guitar** sources (synth pads, the banjo/baritone,
drums). NI's own framing: "a creative effect playground where you mix and match modules." The
rig value is the routing + the lo-fi/ambient component rack on a send, not the amps per se.

## 1. What Guitar Rig 7 is

`research/links/km-guitarrig-7-review-specs.md`, `research/transcripts/km-guitarrig-how-to-use-everything.md`
- **26 amps + matched cabs · 115 stomp/rack effects · VST3/AU/AAX + standalone.** The four new
  v7 **ICM amps** (machine-learning circuit modeling) score on feel; the older pre-ICM amps can
  sound "a bit polite."
- **Cab IR loader** — blend **up to 4 IRs**, each with level/pan/EQ, plus an **Auto-align**
  button that time-aligns the pulses so blended IRs don't phase-cancel. Loads custom IRs.
- **The FX rack spans far past guitar:** delays (**Replika GR**, **Psych Delay**, **Grain
  Delay**, Tape Echo), reverbs (**Replika Shimmer**, **Ice Verb** = "Radiohead-style
  modulation", Spring/Vintage), a full **lo-fi suite** (**Tape Wobble**, **Noise Machine**,
  **Vintage Vibrato**, **Color/Kolor** = 10 distortion algos lifted from iZotope Trash + a Bass
  Saver), modulation, filters, pitch, + mix tools (comps, Solid EQ, Ozone Maximizer module).
- **★ Routing (the load-bearing part):** `research/links/km-guitarrig-manual-routing-modifiers.md`
  - **Split Mix** = in-box parallel A/B (per-path pan + blend) — parallel grit-under-clean, no
    aux needed.
  - **Crossover Mix** = multiband split — **distort only the highs, keep lows clean.**
  - **Split M/S** = mid/side (wash the sides, keep the centre dry).
  - **Container** = group modules into one reusable multi-effect with **16 macros**.
  - **Modifiers** (LFO / Envelope / Step Sequencer / input-signal) assignable to **any knob** =
    automate chaos.
  - **Pre/Post-mix wet-dry** at the top → run GR as a **send/bus FX rack** (Pre-mix matches
    levels for distortion). Plus **Loop Machine Pro**, tuner, pre/post tape decks.

## 2. Using it for walls / lo-fi / ambient + on non-guitar sources

- **★ Walls (the distortion-LAST trick):** NI's own shoegaze guidance — push **feedback + wet
  high** so tails sustain, then put **distortion at the END of the chain** to crush the reverb
  tails together ("almost cracking from intensity") — the *inverse* of distortion-first, and GR
  can reorder freely in Signal Flow. `research/links/km-guitarrig-ni-shoegaze-blog.md`, `research/links/km-guitarrig-shoegaze-daw-guide.md`
- **Lo-fi/degrade:** stack **Color/Kolor (Trash dirt) + Tape Wobble (wow/flutter/Age/Scrape) +
  Noise Machine (hum/hiss/vinyl)** = "recorded to a really bad, misaligned cassette." Bass
  Saver / per-IR EQ / Crossover keep lows clear. `research/transcripts/km-guitarrig-how-to-use-everything.md`
- **Ambient (copyable NI settings):** Psych Delay 300–500 ms / fb ~40% / low mix, LFO on
  delay-time ~0.1 Hz; **Replika Shimmer ±12**; Choral→Phaser with Rate automated 0.3–0.7 Hz;
  Freak freq-shifter ~0.1 Hz / 50–100 Hz drift; Studio Reverb pre-delay ~80 ms. `research/links/km-guitarrig-components-ambient-settings.md`
- **★ Non-guitar (the point for this rig):** demonstrated on drums (EQ+comp+Maximizer; Tape
  Wobble + Noise Machine to destroy), bass (Psych Delay + Vintage Vibrato + Tape Wobble "until
  it stops sounding like a bass"), keys, and a **vocal loop glitched** with sequencer-driven
  Beat Slicers + Gator. NI: "works great on vocals... and on a master bus." `research/transcripts/km-guitarrig-beyond-guitar-production.md`, `research/links/km-guitarrig-izotope-5-mixing-techniques.md`

## 3. vs the rig's other amp/FX tools

`research/links/km-guitarrig-vs-neural-dsp.md`
- **GR amps vs Neural DSP vs Iridium:** Neural wins pure realism/high-gain feel; **GR is the
  chameleon** (versatility + modular chains + experimental design, cheaper). Cross-source
  verdict: "besides high-gain, the tonal quality is not that different." Reach for **Neural**
  when you know the exact amp; the **Iridium** stays the committed front-end you print; reach
  for **GR to build an elaborate degraded chain in one window** (especially on non-guitar).
- **GR FX vs Valhalla / EchoBoy / Decapitator:** the dedicated boxes are deeper on their one
  job (the ambient-swell recipe literally uses GR for the amp bed, EchoBoy for delay, Valhalla
  for reverb). **Reach for GR as the all-in-one rack** when you want amp + cab + dirt + mod +
  lo-fi + parallel/multiband routing in a single send instance. Its Color/Kolor overlaps
  Decapitator but GR wraps it in amp/cab + lo-fi + routing. `research/transcripts/km-guitarrig-ambient-swells-recipe.md`

## 4. Copyable recipes

1. **Ambient-wall (banjo/baritone):** EQ (HPF ~150 / LPF ~6 k) → **clean amp (Reverb Delight,
   low gain)** + matched cab/room → Psych Delay (300–500 ms, fb 40%, LFO on time) → **Replika
   Shimmer +12** → big reverb (~2.8 s, ~40% wet, mod up). Sparse chord voicings keep the wall
   defined.
2. **Lo-fi degrade chain:** source → **Color/Kolor** (Bass Saver up) → **Tape Wobble** (Age +
   Scrape) → **Noise Machine** (vinyl/hum) → optional amp last to crush. Automate Tape Wobble wow.
3. **Banjo → shoegaze wall (distortion-last):** banjo → modulation/Psych Delay → big reverb
   (long tail) → **fuzz/Color/Chainsaw at the END** to crush the tails → print via Tape Deck
   Post or a Logic bounce.
4. **Creative FX rack on a synth pad (send/bus):** insert on an aux, **Pre-mix** wet-dry;
   **Split Mix** A clean / B (Color + **Crossover** dirt on highs only) → Split M/S widen →
   reverb; **LFO on the Split blend** = auto-pan; macro the whole thing in a **Container**.

## 5. Best learning resources

1. **NI — "How to use everything in Guitar Rig 7 Pro" (1:16)** — *the* deep reference (every
   module, routing, IR auto-align, macros, lo-fi, non-guitar). ★
2. **NI — "Beyond guitar"** — 5 ways on non-guitar (the sequencer-glitch vocal chain).
3. **Learning Music Skills — "Ambient guitar swells"** — exact GR-clean + EchoBoy + Valhalla
   recipe (the rig-tool-split blueprint).
4. **iZotope — "5 techniques for mixing with Guitar Rig 7 Pro"** — the FX-rack-on-everything
   bible. (Groove3 courses are the deepest paid option.)

## 6. Pitfalls / gotchas

- **Older non-ICM amps can sound "polite"** — favor the four new ICM amps for feel, or use GR
  for FX and amp elsewhere (Neural/Iridium).
- **Effect order matters under ICM** — use Signal Flow to reorder; the distortion-last trick is
  deliberate.
- **No named drone/shoegaze artist** surfaced using GR (artist presets skew rock/metal) —
  relevance is by technique.

## 7. Captured sources

**Transcripts (4)** — `research/transcripts/`: km-guitarrig-how-to-use-everything ·
km-guitarrig-beyond-guitar-production · km-guitarrig-ambient-swells-recipe ·
km-guitarrig-7-pro-walkthrough.
**Links (7)** — `research/links/`: km-guitarrig-izotope-5-mixing-techniques · km-guitarrig-ni-shoegaze-blog
· km-guitarrig-shoegaze-daw-guide · km-guitarrig-vs-neural-dsp · km-guitarrig-manual-routing-modifiers
· km-guitarrig-components-ambient-settings · km-guitarrig-7-review-specs.

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first line =
the original URL). Primary: NI tutorials/blog + manual, iZotope, Learning Music Skills,
review/comparison articles. **Honesty flags:** some ambient settings are from NI's own
(promotional) blog (flagged in-file); the Ambient Online forum thread 404'd (corroborated by
the ambient-swells transcript); the deepest courses (Groove3) are paywalled.
