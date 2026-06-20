https://www.chasebliss.com/s/Big-Time_Manual_Chase-Bliss.pdf
Chase Bliss Big Time manual (p.39) + SonicState Superbooth John Snyder interview (line 22) · accessed 2026-06-19

# Technique: TILT EQ as a feedback-decay governor (not a static tone knob)

Big Time's TILT EQ does not sit at the output coloring the dry-plus-wet sum. It is placed **inside the feedback loop**, so it shapes how the repeats *evolve* over time — every pass through the loop is re-filtered. That makes TILT a control over repeat **length and thickness**, not just tone. This is first-party, so it's stated here without hedging.

## What it is

TILT tilts the spectrum around a pivot frequency set by **CROSSOVER**: turn one way to boost lows (cut highs), turn the other to boost highs (cut lows). Because the tilt lives in the feedback path:

> "placed WITHIN the feedback loop to shape how repeats evolve… cut highs or cut lows → effectively boosts the other band as the feedback loop reprocesses the audio over time." — Superbooth interview, line 22

So the band you boost gets *more* energy each pass; the band you cut bleeds off.

## How to use it as a governor

- **Boost lows (TILT below noon) = longer, thicker tails.** More low-frequency energy recirculates and survives more passes, so the delay sustains and fattens.
- **Cut lows (TILT above noon) = shorter tail / de-mud.** Low energy bleeds out of the loop faster, so repeats die sooner and the wash stays clean. The manual (p.39) frames this as a way to "cut the mud from your bass."
- **CROSSOVER sets the pivot** — i.e. where the tilt hinges, so you choose which part of the spectrum is governed.

The mental model: TILT is a **feedback-decay governor**. Think of it less as "tone" and more as "how much energy survives each recirculation, and in which band." It pairs with FEEDBACK (overall recirculation amount) — FEEDBACK sets how much comes back, TILT sets how it ages.

## Where it matters

This is relevant to every drone / wall / resonator patch: TILT doubles as a **ring-length / tail-length control**. In the MOD metallic-resonator use it governs how long the resonance rings; in long ambient washes it's how you keep a feedback bed from either collapsing too soon or muddying into a low-end pileup. Reach for TILT before touching FEEDBACK when the *character* of the decay is the problem, not the *amount*.

## Sources

First-party
- Chase Bliss Big Time manual — local `gear/Chase Bliss Big Time/manuals/Big+Time_Manual_Chase+Bliss.pdf` (byte-identical to official Squarespace PDF), TILT / CROSSOVER p.39 ("cut the mud from your bass")
- SonicState Superbooth — John Snyder / EAE interview; corpus transcript `gear/Chase Bliss Big Time/research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md`, line 22 (TILT placed within the feedback loop)

Corpus
- `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` (lines 55–57, TILT in-loop usage)
- `research/bloops/2026-06-19-chase-bliss-big-time-l2.md` (L2 digest — cross-cutting technique housekeeping lens)
