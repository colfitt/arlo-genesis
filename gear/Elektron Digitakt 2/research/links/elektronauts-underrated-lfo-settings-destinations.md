https://www.elektronauts.com/t/what-are-your-underrated-lfo-settings-destinations/241235
elektronauts.com · community thread (multiple users) · 2025

# DT2 — "Underrated LFO settings / destinations" (concrete recipes)

The most parameter-specific LFO thread found for the DT2 era. Each post names DEST +
WAVE + MULT + MODE + DEP. These transfer directly to the rig's drone/percussion work.
Quoted settings below; author handles in parentheses.

## Recipe 1 — Rhythmic distortion on static pads (mistcollector)
- **DEST = SRR amount** (sample-rate reduction)
- **WAVE = SQUARE**
- **MODE = TRIG**
- Purpose: "great rhythmic distortion variation on otherwise static pad/ambient samples."
- Enhancement: add a **second LFO modulating the SPEED multiplier** of that square LFO →
  the distortion rhythm itself drifts. (Stacking LFO2 → LFO1 speed is the trick.)

## Recipe 2 — Hi-hat dynamics / groove (mistcollector)
- **DEST = AMP attack**
- **WAVE = SINE**
- Purpose: "Instant groove and dynamics" on a static hi-hat sample — the attack breathes
  so repeated hits stop sounding machine-gunned.

## Recipe 3 — Polymetric muting (mistcollector) ★ the standout
- **DEST = AMP volume** (or **FILTER frequency**)
- **WAVE = SQUARE**
- **MULT = 512 or 1k** (very high)
- **SPEED = random, NON-whole number** (e.g. not 8/16/32 — deliberately off-grid)
- **MODE = HOLD**
- **DEP = high**
- Purpose: the square wave gates trigs on/off so certain hits silently drop out in a
  **polymetric / non-repeating** way. With a non-integer speed it never lines up with the
  bar → a 4-bar loop mutes itself differently for many bars. Drone-rig use: gate a
  sustained banjo/fuzz layer in and out without sequencing it by hand.

## Other posted destinations (concept-level, wave noted)
- **(ds0)** Grid machine on a melodic sample + LFO → **slice/grid position**, "various
  shapes" — scans through the sample chain melodically.
- **(Catastrophone)** **RANDOM** wave → **sample SELECTION (slot)** = round-robin across
  several similar samples (e.g. 4 banjo plucks) for organic per-hit variation.
- **(Humanprogram)** **HOLD + RANDOM** → **DEC / ATK / REL** = "humanizing percussion
  samples" (each hit gets a slightly different envelope).
- **(survivors-guide)** **EXPONENTIAL one-shot LFO → BIT REDUCTION** = transient
  enhancement (the crush hits hard on the attack then opens up). Separately, **TRIANGLE
  LFO → sample ENDPOINT or STARTPOINT** = phase-scanning a sustained sample.

NOTE: depth/speed exact integers given only where quoted (MULT 512/1k). The HOLD-mode
square gate and the random→sample-slot round-robin are the two most reusable. Manual
confirms MULT can multiply current tempo OR a fixed 120 BPM, and "Try SPD 8, 16 or 32 to
sync the LFO to straight beats" — so a non-whole speed is intentionally un-synced.
