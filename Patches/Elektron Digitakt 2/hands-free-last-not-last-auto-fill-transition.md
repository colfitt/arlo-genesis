---
type: patch
title: Hands-Free LAST / NOT-LAST Auto-Fill Transition
device: Elektron Digitakt 2
date: 2026-06-14
description: The box plays its own fills/risers on a queued pattern change, freeing both hands to ride pedals during a wall-of-sound build — DT2 LAST / NOT LAST conditionals.
tags: [conditional, transition, workflow, hands-free, community, signature]
controls:
  - { name: "Conditional access", type: switch, value: "Hold a trig → conditional knob on the TRIG page (DT2-only conditionals)" }
  - { name: "Fills/risers/kicks", type: switch, value: "Put on LAST trigs (fire only on the final pass before the cued switch)" }
  - { name: "Drops", type: switch, value: "Put on NOT LAST trigs" }
  - { name: "Step-1 riser workaround", type: switch, value: "PATTERN CHAIN (PATTERN → FUNC+YES for chain → e.g. p1 ×2, p2 ×2 → PLAY)" }
  - { name: "Subtract trigs", type: switch, value: "NOT x:y (e.g. NOT 2:3)" }
---

# Hands-Free LAST / NOT-LAST Auto-Fill Transition

## Concept
Frees both hands for the Microcosm / H90 / Chroma build during transitions: the box plays its own fills/risers on a queued pattern change. Put extra fills/risers/kicks on LAST trigs (fire only on the final pass before the cued switch) and trigs to drop on NOT LAST. Cue the next pattern and the transition plays itself on that last pass.

## How to play it
1. DT2-only conditionals (hold a trig → conditional knob on the TRIG page). Build a main pattern + a next ("chorus") pattern.
2. In the main pattern: put extra fills/risers/kicks on LAST trigs (fire only on the final pass before the cued switch); put trigs to drop on NOT LAST.
3. Cue the next pattern → the transition plays itself on that last pass.
4. Gotcha: trigs on early steps (1–2) won't fire on the cued pass; for a riser that starts on step 1 use a PATTERN CHAIN instead (`PATTERN` → `FUNC`+`YES` for chain → e.g. p1 ×2, p2 ×2 → `PLAY`).
5. Also `NOT x:y` subtracts trigs (e.g. `NOT 2:3`).

## Notes
- Frees hands for the Microcosm / H90 / Chroma build during transitions.
- Two patterns in a bank; chain for step-1 risers.

## Sources
- `research/transcripts/hexwave-dt2-new-conditional-trigs.md` (yt `DLi1B6ia-_M`)
- `research/links/elektronauts-dt2-overlooked-features.md` (t/213177)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
