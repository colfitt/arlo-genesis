---
type: patch
title: Bass Compression with EQ Low-Cut
device: Chase Bliss Clean
date: 2026-06-15
description: "Bass Fox's stored bass preset — straightforward, musical compression with a touch of high end shaved off via the tilt EQ, mid attack, mid release and a fairly high compression amount: a clean bass leveler. The hidden Envelope Balance high-pass on the control signal keeps a low B from choking the engine (the recurring bass gotcha). Demonstrated values are 'mid/fairly-high' descriptors, not exact clock positions — dial from the recipe."
tags: [compression, bass, leveler, everyday, low-b, community]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
hidden:
  Envelope Balance (EQ knob): "toward MORE (high-pass the control signal) so a low B / boomy lows don't over-trigger the engine — set for 5-string / low-B sources"
controls:
  - { name: "Sensitivity", type: knob, value: "by the left LED at playing volume (Bass Fox's preset stored ~middle) — approximate, dial by ear" }
  - { name: "Dynamics", type: knob, value: "fairly high, ~10:00-noon (substantial, even compression; 10:00 is roughly 4:1 per the manual)" }
  - { name: "Attack", type: knob, value: "mid" }
  - { name: "EQ", type: knob, value: "slightly CW (Manual mode) to shave a little high end" }
  - { name: "Wet", type: knob, value: "up (mostly compressed)" }
  - { name: "Dry", type: knob, value: "to taste" }
  - { name: "Release", type: switch, value: "Mid (User 650ms)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
---

# Bass Compression with EQ Low-Cut

## Concept
Bass Fox's stored bass preset is a no-drama bass leveler: a fairly high compression amount for substantial, even gain control, a mid attack and mid release that stay musical, and the tilt EQ nudged clockwise (Manual mode) to remove just a little high end. The result is "warm, full bodied, punchy" with extra spice in the mids. The key bass move lives in Hidden Options: Envelope Balance is set toward MORE, high-passing the control signal so a low B doesn't over-trigger the compressor — the recurring bass gotcha. Clean "handles low B strings without choking" once Envelope Balance is dialed in.

## How to play it
1. Set Sensitivity by the left LED at playing volume (Bass Fox's preset was roughly mid — treat as a starting point and dial by ear).
2. Set Dynamics fairly high (~10:00–noon) for substantial, even compression.
3. Attack mid; Release toggle MIDDLE (User / 650 ms).
4. Turn the EQ slightly CW (Manual mode) to shave a little high end.
5. For a 5-string / low-B bass: hold both footswitches and set the EQ knob (now Envelope Balance) toward MORE so the low B doesn't choke the compressor. Audio is unaffected — only the control signal is high-passed.

## Notes
- AVOID Sag on bass — it favors higher frequencies and reacts poorly to low end (compressorpedalreviews / community consensus).
- Envelope Balance is the published fix for low B / boomy lows over-triggering the engine; set it toward MORE for low-B sources.
- Clean "handles low B strings without choking"; tone here is "warm, full bodied, punchy" with "extra spice in the mids" (compressorpedalreviews).
- HONESTY: the demonstrated positions are "mid / fairly-high" descriptors from Bass Fox's preset, NOT exact published clock positions. Treat all values as a dialable recipe and set by ear / by the LED. The only firm number is the manual's ~4:1 at 10:00 on Dynamics.
- All CUSTOMIZE dips OFF; Envelope Balance is set on the Hidden Options page (hold both footswitches).

## Sources
- `research/transcripts/bassfox-quincas-moreira-studio-tool-sidechain.md` (Bass preset 2: simple compression, removing a little high end with EQ, mid attack, mid release, fairly high compression; Sensitivity stored ~middle)
- `research/links/compressorpedalreviews-clean-deep-dive.md` (Envelope Balance recommended for 5-string bass; handles low B without choking; warm/punchy/extra mids; avoid Sag on bass)
- `research/links/community-clean-value-and-bass-consensus.md` (use Envelope Balance for low B / boomy lows; avoid Sag on bass)
- talkbass.com/threads/new-compressor-by-chase-bliss-clean.1661320
- Provenance: demo:Bass Fox (stored bass preset) + specialist gotcha (compressorpedalreviews / TalkBass) — descriptive values only, dial from recipe
