https://blog.native-instruments.com/bitcrushing/
blog.native-instruments.com · NI Blog · "What is bitcrushing?"

# Bite + bitcrushing (NI Blog) — distilled

Bitcrushing = degrade signal quality via two processes:
- **Sample-rate reduction** — fewer amplitude values/sec. Dropping 44.1 kHz lower introduces **aliasing errors that distort the higher frequencies** (the gnarly metallic top end).
- **Bit-depth reduction** — fewer possible amplitude values. A **4-bit** signal = only **16 possible values** → noisy, quantized, gritty vs 24-bit.

**Bite** implements both, plus **Pre and Post filters** (so you can sculpt before/after the crush — e.g. tame the aliasing top end after the fact).

## Concrete Bite recipes from the article
- **Lo-fi drums:** sample rate down to **12 kHz**, filters opened to ~22.1 kHz.
- **Max noise:** bit depth down to **6** bits.
- **Degradation sweep:** automate sample rate from **44.1 kHz → 300 Hz** for a progressive fall-apart (great for transitions/risers, and for "this wall is collapsing" doom moves).
- **Dubstep bass texture:** sample rate to **1.47 kHz**.

Adds vintage character, lo-fi sheen, and dramatic degradation sweeps (Daft-Punk-style atmospheric transitions cited).

## Rig relevance (drone/doom/shoegaze)
- Put Bite as an **insert on a sustained wall / banjo lead** for a degraded-tape edge.
- **Automate the sample-rate sweep** under a held drone for a "tape disintegrating" arc.
- Use the **Post filter** to roll off the harsh aliasing so the grit reads as warmth, not fizz.
