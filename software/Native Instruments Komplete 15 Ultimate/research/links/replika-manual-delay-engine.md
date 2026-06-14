https://native-instruments.com/ni-tech-manuals/replika-xt-manual/en/delay-section
native-instruments.com · Replika XT manual (Delay Section) · n.d. (accessed 2026-06)

# Replika XT — the delay engine: feedback, sync, ducking, routing (official manual)

## Feedback — the wall engine
- *"Feedback levels of 100% and above are possible, allowing the delay repeats to build up until
  the point of self-oscillation."* → above 100% = runaway/self-oscillating wall (FLAG: watch gain).

## Time / Sync
- **Max delay time = 4000 ms** (e.g. synced 2/1 at 120 BPM).
- Modes: **milliseconds / Straight / Dotted / Triplet**. SYNC follows DAW tempo automatically.

## Ducking (keeps the source clear under heavy echoes)
- **Sensitivity** (threshold) · **Amount** (gain reduction strength) · **Release** (recovery) ·
  **Reduction** (meter). → dial this in for banjo/baritone plucks that need to punch through a
  feedback wash; the dry note ducks the echoes, echoes swell back in the gaps.

## Pattern (rhythmic / multi-tap)
- **Shuffle / Feel / Accent** for rhythmic manipulation.
- ★ CPU FLAG: *"The functions in the Pattern menu require additional delay lines to be calculated
  in the background, which increases the CPU load."*

## Routing — Single vs Dual
- **Single** — true stereo; **Standard** or **Ping Pong**.
- **Dual** — two independent delays **A / B**, **Serial or Parallel**. → Serial = delay-into-delay
  (e.g. Tape → Diffusion); Parallel = two textures at once (rhythmic tap + wash). The dual engine
  is how you build the "delay → reverb-wash" inside ONE Replika instance.
