https://docs.google.com/document/d/1K39_3D0UcjgCqGfXt4BLIpHa1x00A6FFlEhKsZ98xGI/mobilebasic
"Elektron Octatrack Master Reference" (community Google Doc) · anonymous compiler · ongoing

# LFO SPD/MULT cheat-table + 1:1 resample levels + flat-LFO fine-control

Concrete reference values that turn the OT's abstract LFO/level params into musical results — fills the "what number gives me one cycle per bar?" gap.

## LFO rate table — SPD + MULT for musical cycles (audio tracks, example @130 BPM)
| Cycles per bar | SPD | MULT |
|---|---|---|
| 0.25 (one cycle / 4 bars) | 64 | 1x |
| 0.5  (one cycle / 2 bars) | 32 | 1x |
| 1.0  (one cycle / bar)    | 16 | 127 |
| 4/3                       | 12 | 2x |
(Lower SPD + lower MULT = slower; these are the anchors for "slow triangle breathing the wall" in §2 — for a sub-bar drone breath use SPD≈32–64.)

## 1:1 / unity resample levels (no generation loss)
- **Flex record-track LEVEL = 127** (full), **AMP VOL = 0** for the record, **CUE VOL = 127** when overdubbing.
- Match a track's CUE volume to its track level for a true 1:1 capture ratio.
(Corroborates the existing "captured LEVEL = 127, master Comp MIX = 0" anti-attenuation rule.)

## Flat-LFO fine control (sub-tweak movement)
- Assign one LFO a **near-flat custom waveform (DESIGNER values 2–7)** at **DEPTH = 64**, then **modulate THAT LFO's params with a second LFO** → very small, slow parameter drift. Good for an almost-imperceptible filter/pitch wander on a drone (movement without obvious modulation).

## Memory note
- RAM for Flex + recorder buffers ≈ **85.5 MB**; a 4-bar pattern @130 BPM ≈ **7.4 s** of record reserve per track over the first 4 tracks (plan RESERVE LENGTH accordingly).

## Rig fit
Use the rate table to lock LFO-on-cutoff/STRT to the project grid (one slow cycle per 2–4 bars = the breathing wall). The flat-LFO trick is the "subtle wrongness" tool — drift a banjo loop's pitch by a hair so it never sits still.

PROVENANCE: community (compiled reference doc, cited). Rates are tempo-relative (example given @130 BPM); MULT "127" for 1.0 reads as the doc's notation — treat the column as relative anchors and verify on-box.
