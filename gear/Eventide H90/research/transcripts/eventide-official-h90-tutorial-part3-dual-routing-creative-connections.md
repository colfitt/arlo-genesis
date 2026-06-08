https://www.youtube.com/watch?v=0G_WtfUatSc
Eventide Audio · Eventide H90 Tutorial - Part 3: Dual Routing & Creative Connections (Joe Cozzi) · 2023-08-16 · 32:16

The routing/connectivity half of the official video manual: Insert vs Dual mode, two-instrument and 4-cable-method setups, and wet/dry/wet rigs. Cleaned to prose.

## Two global routing modes
- **Insert mode** — two algorithms in series or parallel, with up to two mono insert loops or one stereo loop.
- **Dual mode** — two fully independent signal paths (process two mono or stereo sources at once); NO insert loops available.

Change in System Settings > Global > Routing (second option, page 1; turn quick knob 2). Switching prompts you to confirm rear connections and mutes audio. Important gotcha: **Dual mode enables a separate Playlist and separate factory/user lists** — Programs built for Insert mode cannot be used in Dual mode and vice versa.

## Dual mode signal flow
Two paths shown left-to-right. Path 1 = Ins 1/2 → Outs 1/2; Path 2 = Ins 3/4 → Outs 3/4. The first quick knob sets five algorithm positions: both in series on Path 1, both parallel on Path 1, one algorithm on each path, both parallel on Path 2, both series on Path 2. Dual mode is denoted by two HORIZONTAL parallel lines between the algorithm icons (vs the arrow=series / vertical-lines=parallel of Insert mode). Each path runs mono (In/Out 1 for Path 1, In/Out 3 for Path 2), stereo (1/2 and 3/4), or mono-in/stereo-out or stereo-in/mono-out. Mono in must use In 1 (Path 1) / In 3 (Path 2) — feeding only In 2 or In 4 gives undesired results. The H90 is NOT a 4-in/4-out mono device.

Example (two instruments): guitar to Path 1 (In 1 → Out 1, set instrument level), keyboard to Path 2 (In 3 → Out 3, set line level); each path gets its own algorithm. Add Out 2 / Out 4 for mono-in/stereo-out (H90 auto-adjusts to stereo). For a mic, use a preamp first — Eventide's MixingLink (65 dB gain, phantom power, an instrument in with 20 dB pad, an effects loop, a 2-amp out and a DI/XLR out) is recommended; in Dual mode you have no inserts, so the MixingLink's own loop lets you add outboard effects before/after the H90 path.

## Connecting to an amp's effects loop (Insert mode, simplest)
Amp FX Send → H90 In 1; H90 Out 1 → amp FX Return. Usually set In 1 / Out 1 to LINE level. You get two algorithms (series/parallel) plus inserts, but all H90 effects land after the amp's preamp.

## Four-cable method (pre/post)
Lets you place effects before AND after the amp's preamp.

Insert-mode 4CM: guitar → In 1; Out 3 → front of amp; amp FX Send → In 3; Out 1 → amp FX Return. Think of Insert 1 as the amp preamp — algorithms can sit before it, after it, or split (one front + one loop), and a second insert can add another outboard pedal anywhere. Downside: if the insert (or its cable) bypasses/drops, you can lose signal entirely — harder to troubleshoot.

Dual-mode 4CM (preferred for reliability): guitar → In 1; Out 1 → front of amp; amp FX Send → In 3; Out 3 → amp FX Return. Path 1 = front-of-amp algorithms, Path 2 = loop algorithms. Treat the H90 as two separate pedals. Set Path 1 (In/Out 1) instrument level, Path 2 (In/Out 3) line level for most amps. Drawback: no inserts — but you can place real pedals before/after each path, and with a MIDI loop switcher each path can be its own loop (some switchers reorder/parallel loops).

## Wet/dry and wet/dry/wet
Wet effects must have **Kill Dry ON** so the wet amp gets no dry signal. To split: place an insert FIRST in the chain as a splitter with insert **Mix = 0%** (only then does it act as a splitter). Guitar → In 1; Out 3 → dry amp; Out 1 → wet amp. Dry pedals go before the H90; both algorithms after the insert handle the wet chain. Note: in true wet/dry(/wet) rigs it's not advised to put two wet effects in series (e.g. a fully wet delay into a fully wet reverb) — use parallel or the program-mix blend approach instead.
