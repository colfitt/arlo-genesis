https://www.elektronauts.com/t/advanced-techniques-for-parameter-locking-sample-changes-per-step/171663
elektronauts.com · community thread (Doug, re5et, motokobis) · 2023

# DT/DT2 — P-locking / LFO-driving sample changes per step (sound-pool scanning)

How to make ONE track walk through a bank of samples — the core "random melody / round-robin
/ amen-rearrange" move. Complements the existing generative-and-drone link (djadonis206's
LFO→slot tip) with the exact scaling caveat and the repeatable-scan setup.

## Recipe 1 — Random LFO → sample SLOT (Doug)
- Lay your target samples in **consecutive slots**.
- Assign the **middle sample** of that run to the track (so the LFO can swing both ways).
- **LFO: WAVE = RANDOM, MODE = TRIG, DEST = sample slot.**
- **DEP** sets how many slots it spans — and there's a **scaling quirk**: for **7 samples,
  set depth to about "2.9"** (not 7), because the slot-select scaling isn't 1:1. Dial depth
  until it lands inside your run without overshooting.

## Recipe 2 — Repeatable scan with a RAMP LFO (re5et)
- **WAVE = RAMP**, **BPM-synced**.
- **Enable LFO retrig (LFO.T) on step 1; disable LFO.T by default** on the others → the scan
  restarts cleanly every loop instead of drifting.
- **DEP** = how far across the slot list it scans; start sample = first slot of your run.
- Tuning trick: **temporarily point the LFO DEST at sample START** so you can SEE the LFO's
  speed/width move on the waveform display, then switch DEST back to **sample slot** once it
  looks right.

## Recipe 3 — Record a manual knob sweep (motokobis)
- In live record, **turn the sample-select knob by hand at varying speed** — the DT records
  it as per-step p-locks that override the trig's base sample. Editable afterward.

## Add variation on top (general)
- Sprinkle **conditional / yellow trigs (NOT on step 1) or FILL trigs** that re-fire the LFO
  reset sporadically → controlled randomness without losing the overall scan.

NOTE: the **DEP ≈ 2.9 for 7 samples** figure is the load-bearing concrete value (scaling is
non-linear). On DT2 use one of the 3 LFOs for the slot scan and keep the other two on
filter/pitch. Pairs with banjo round-robin: 4 real banjo plucks in consecutive slots +
RANDOM-TRIG LFO at the right depth = a never-identical lead voice.
