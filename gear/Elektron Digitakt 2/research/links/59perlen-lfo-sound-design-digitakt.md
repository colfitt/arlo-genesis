https://www.59perlen.com/post/3-ideas-use-lfo-digitakt
59perlen.com · 59 Perlen · 2021-03-15

# 59 Perlen — "3 ideas to use the LFO on Digitakt for sound design"

Three compact LFO patch recipes. OG-Digitakt-era (one LFO) but every recipe transfers to
the DT2 and improves with 3 LFOs. Values are partly relative ("very low") where the author
didn't post integers; the one hard number is the bit-crush speed. On-aesthetic for the
"recorded-wrong"/vintage-pitch-drift look this rig wants.

## Idea 1 — Living reverb (keeps a track from going static)
- **DEST = Reverb HPF** (the reverb send's high-pass)
- **SPD = very low**
- **DEP = mid-range**
- WAVE/MODE not stated → use SINE or TRIANGLE, FREE.
- Effect: the reverb tail's HPF constantly drifts so the wash never sits still.

## Idea 2 — Vintage pitch drift ★ (maps to "recorded-wrong")
- **DEST = Pitch**
- **SPD = low**
- **DEP = very low** (tiny — this is wobble, not vibrato)
- WAVE/MODE not stated → SINE or TRIANGLE, FREE, MULT low.
- Effect: "a constant pitch move that can bring the sound to life," an old/worn-tape feel.
  Author calls it the way to fake an old recording. Use on a sustained banjo/fuzz drone.

## Idea 3 — Rhythmic bit-crush
- **DEST = Bit Reduction**
- **WAVE = RANDOM**
- **SPD = 32** (synced to track speed)
- DEP not stated.
- Effect: the crush amount jumps around per step → moving digital grit.

NOTE: relative descriptors are the author's; integers given only for Idea 3 (SPD 32).
The vintage-pitch-drift recipe is the keeper for drone/doom drift. On DT2 run all three
at once (3 LFOs/track): LFO1 pitch drift, LFO2 reverb-HPF, LFO3 random bit-reduction.
