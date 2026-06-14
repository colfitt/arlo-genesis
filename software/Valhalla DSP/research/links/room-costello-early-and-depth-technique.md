https://valhalladsp.com/2011/05/18/valhallaroom-the-early-controls/ + https://valhalladsp.com/2011/05/02/valhallaroom-the-high-level-sliders/ + https://valhalladsp.com/2011/05/25/valhallaroom-tips-and-tricks-realistic-concert-halls/
valhalladsp.com · Sean Costello · 2011-05 (Early Controls, High Level Sliders, Realistic Concert Halls posts)

# ValhallaRoom — Costello's Early / Depth / decay technique (community-facing recipes)

The settings facet already has the *taxonomy*. This file captures the **actionable Early-engine recipes and the mic-distance mental model** Costello spells out — the stuff that turns "the Depth knob is misunderstood" into concrete moves.

## Depth = a mic-distance crossfade, not an intensity knob (the clearest framing)
- Depth uses a **sine/cosine (equal-power) crossfade** between Early and Late. Costello: the levels of the two engines were carefully **normalized so output level stays balanced across virtually the whole Decay range** — so moving Depth changes *character/distance*, not loudness.
- The intended metaphor: **"simulates moving a microphone further away from the source, or (more accurately) controlling the mix between close mikes and room mikes."** Low Depth = close mics (placement, attack), high Depth = room mics (the body/tail). This is the single best way to explain it to someone who thinks Depth = "more reverb."
- **50% is the canonical starting point** for early/late ratio.
- The drum-room use: **lower Depth to emphasize early reflections → keeps drum attack present without a long tail.**

## The Early Size → Early Send recipe table (verbatim ranges)
Costello's explicit Early Size cheat-sheet:
- **10–50 ms** — small-room early reflections, *or* a wider stereo image with no strong decay (the "widen, don't wash" trick).
- **50–100 ms** — impression of a **"compressed" room**, like the attack was squashed by a limiter or tape saturation (great for a glued, slightly-gated drum/room feel).
- **150 ms+ with Early Send = 1.0** — a **slow onset to the Late reverb** → simulates very large halls/cathedrals **and adds clarity to the input** (the swelling cathedral bloom; matches the draft's "slow cathedral onset").

Early Send recipes:
- **Early Size 10–50 ms + Early Send 1.0 → a dense Late reverb** (early energy thickens the tail's echo density without coloring it).
- **Early Size 20–50 ms + Early Send full + Early Diffusion max → a diffuse onset of reverberation** (smooth wash-in, no discrete slaps).
- **Early Size 70–100 ms + Early Send 0.0 + small Late Size + Depth 0.5 → a small space with a compressed attack** (parallel early/late, tight).

## Diffusion: leave it high
- Diffusion sets Early echo density. **High Diffusion will NOT go metallic on vocals/drums** — "feel free to keep Diffusion at 1.0 for most purposes." (Confirms the draft's "stays smooth" claim from the horse's mouth.)

## Modulation rates (for the tail)
- **0.25–0.5 Hz** — warms the sound / smooths decay artifacts.
- **1–2 Hz** — adds a **"string ensemble" chorusing** effect (the lush, EMT250-style move).
- **Set Early + Late Mod Depth = 0.0 for realistic rooms;** raise for the chorused/ensemble character.

## Decay & High Cut framing
- **Decay = RT60** (mid-frequency-based); the Bass Mult / High Mult multipliers in the Late section scale the lows and highs *around* that mid time.
- **High Cut 3000–7500 Hz = the sweet spot for larger rooms;** higher settings emulate chambers/plates and brighter digital reverbs. Real rooms can go as dark as **5000 Hz**.

## Realistic concert-hall settings (the surgical realism move)
From the Concert Halls post — values that make a big space sound real instead of artificial:
- Decay **1.6–2.1 s** · Predelay **25–35 ms** · Early Size **20–50 ms** · Early Send **full** · Early Diffusion **max** · High Cut **4500–7000 Hz** · Late Size **> 0.5**.
- **★ Late High Xover ~2–4 kHz + Late High Mult significantly BELOW 1.0** — i.e. the highs decay *shorter* than the body. This is the realism key: real halls lose highs fastest. (Note: this is the *inverse* of the draft's "shimmer-ish rising tail," where High Mult > 1 makes highs ring longer. Both are valid; <1 = realistic, >1 = airy/ethereal.)
- Late Cross **>0 and <1.0** · Early Mod Depth **0** for realism · Late Mod Depth **>0**, Late Mod Rate **0.25–1.0 Hz**.

## Short-drum-room values (the gated/tight end)
- Predelay **15–30 ms** · Decay **0.3 – ~1 s** · High Cut **5000 Hz (dark)** or **6–9 kHz (bright)** · Depth **50%** · **Late Size ≤ 0.5 → highest initial echo density** · Late Bass **≤ 1.0×** (lower = clearer decay).
- Early Size **50–100 ms** for "a slight amount of **gated** sound."
