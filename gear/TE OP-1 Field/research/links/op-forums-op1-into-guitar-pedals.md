https://op-forums.com/t/hooking-your-op-1-up-to-guitar-pedals/2837
op-forums.com (op1.fun community) · multiple users · running OP-1 OUTPUT into guitar pedals

THE thread for this rig's signature OP-1 trick: OP-1 audio out → guitar pedals (fuzz/reverb/delay) and back. Directly validates the planned OP-1 → EHX Effects Interface → Board 1 path.

## Cabling
- **1/8" TRS → 1/4" TS** cable: "just get a 1/8" to 1/4" cable and go at it" for mono into a pedal.
- For STEREO pedals: a **3.5 mm TRS → dual 1/4" TS** breakout preserves the OP-1's stereo image (the whole point of the Field's stereo path — don't collapse it to mono).

## The core problem: level/impedance mismatch
- Synth/OP-1 puts out **line level**; guitar pedals expect **instrument level**. One user: "synth (putting out line level signal) and pedal (wants a guitar level signal)" → can sound "too farty/muddy/quiet," ESPECIALLY into fuzz and distortion.
- **Fix:** a re-amp / line→instrument box. Thread names the Radial **ProRMP**. >>> In THIS rig the **EHX Effects Interface (FXI)** is exactly this line↔instrument bridge — it's the correct front-end for OP-1 → fuzz board, and it's already on the bench. <<<

## What works
- Strymon pedals (BigSky, TimeLine, El Capistan) sound great BUT can "overload" from studio/line-level signals — manage input level (drop OP-1 master volume / pad the input).
- **Avoid mono-only pedals** — they "negate its track panning and stereo image." (Matters for the Field; keep the chain stereo where possible.)
- Working chains reported: wah → OCD → comp → Moog Ring Mod → El Capistan → looper; also Avalanche Run + Instant Lofi Junky.

## Rig takeaway
OP-1 Cluster/Dimension drone → EHX FXI (line→instr) → Board 1 (MXR 108 fuzz / Longsword) → smear through Microcosm/Dark Star = the OP-1 getting "played" through the guitar rig. Keep it stereo; watch the input level into fuzz; pad if it farts out.
