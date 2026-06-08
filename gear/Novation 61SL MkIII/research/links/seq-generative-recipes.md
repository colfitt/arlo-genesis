Synthesis: SL MkIII User Guide V2 mechanics applied to the drone/doom/shoegaze rig
Distilled from seq-manual-* files + firmware-1.4 features (this agent)

# Generative / aleatoric sequencer recipes (drone / degraded / evolving)

All recipes use only documented features: Pattern Direction (Forward/Backwards/Ping-Pong/Random), per-step Chance, Pattern Shift, the 6 micro-steps, Scale Snap/Filter, Sequence Transpose, per-Part independent arps, and varying Sync Rate per Part. Combine them so nothing repeats on the bar.

## Why these work
The SL never "randomises pitch" arbitrarily when Scales is on — **Random direction + Scale Snap/Filter keeps every chaotic note diatonic.** So you can let direction and chance run wild while staying in a chosen drone key. Per-Part independent Sync Rates + per-Part swing means tracks drift out of phase and re-converge → the slow "evolving wall" motion the rig wants.

## RECIPE A — "Never-repeating drone bed" (one Part, set-and-forget)
- One Part → your sustained source (VG-800 pad model, a soft-synth pad, Microcosm-fed loop, etc.).
- Steps: place 4–6 long notes (Gate 8–24 steps so they overlap into a chord wash). Sparse — empty steps are fine.
- Options → Pattern: **Direction = Random**, **Sync Rate = 1/8 or 1/4** (slow), **Start 1 / End 16**.
- Options → Chance: set the held notes to **40–70%** chance (varied per step) so the chord voicing reshuffles every pass.
- Scales: **On**, Root = song key, Type = Natural Minor / Dorian / Phrygian, **Mode = Snap**. Per-Part scale On.
- Result: a sustained, ever-reshuffling diatonic chord cloud that never resolves the same way.

## RECIPE B — "Phasing two-Part interplay" (the Steve-Reich / Eno drift)
- Part 1 and Part 2 → two related voices (e.g. baritone-VG drone + a high bell/pluck soft-synth).
- Same notes/scale on both, but **different Sync Rates**: Part 1 = **1/16**, Part 2 = **1/16T** (or 1/8 vs 1/8T). They start aligned and slowly phase apart over many bars, re-converging periodically.
- Add **Pattern Shift** on Part 2 (try 3–5) so its start/end nudge against Part 1.
- **Swing per-track:** swing ON for Part 2 only (e.g. 58%), OFF for Part 1 → the two grids breathe against each other.
- Chance ~80% on both so occasional dropouts keep it from locking into an obvious loop.
- Scales On + Snap on both → guaranteed consonant even as they drift.

## RECIPE C — "Glitch/degraded texture generator" (micro-steps + chance)
- One Part → a percussive/granular source (MPC sample chop, Octatrack slice, Chroma Console feeding back).
- On 3–4 steps, fill **multiple micro-steps** (the top-row buttons over the faders) with the same note → ratchet/glitch bursts.
- Set those ratchet steps to **Chance 30–60%** so the glitches fire irregularly.
- **Direction = Ping-Pong**, **Sync Rate = 1/16 or 1/32** for fast stutter.
- Use **Non-Quantised Record (Shift+Record)** to play in loose hits landing on the nearest 1/6 tick, then tidy in micro-steps view.
- Pair with a slow **automation lane** on a filter/CC (record one slow knob sweep, then disable record) so the texture morphs.

## RECIPE D — "Aleatoric arp wall" (per-Part arps)
- Hold a chord and latch it (**Latch**) on a Part with Arp = **Random**, **Octaves = 3–6**, **Chance ~60–80%**, **Gate 100%** (overlapping), Sync Rate 1/16.
- Run a 2nd Part's arp on the SAME held chord but **Type = Played, Sync Rate = 1/8T, Octaves = 2** → a second, slower aleatoric line.
- Scales On (Snap) → the random octave-spanning notes stay in key.
- Latch means it self-sustains hands-free; tweak Chance/Octaves live for a slowly mutating arpeggio wall.

## Performance / arrangement glue
- **Mute/Solo** Parts (yellow/blue soft-button rows) to bring layers in/out live.
- **Pattern Chains** (press 2+ pattern pads together) to sequence song sections; **Shift+select pattern** for instant audible blends.
- **Sequence Transpose with pads** (firmware 1.4, in Scale Settings) to shove the whole wall ±11 semitones live for swells/drops.
- **Cued Session Switch** (press a session pad while playing) to jump whole arrangements at the next pattern boundary.
