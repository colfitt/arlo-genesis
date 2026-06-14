https://www.elektronauts.com/t/reliably-lock-lfo-start-point/162628
elektronauts.com · community thread (Lauli, Humanprogram, others) · 2021–2022

# DT/DT2 — Reliably locking an LFO start point (phase reset)

The fix for "my random/triangle LFO sounds different every time I hit play." Needed for the
EZBOT/DROWNED drone recipes where you want one LFO free-running for evolution but ALSO want
a clean phase reset at bar 1 so loops are repeatable. OG thread; the param names (LFO mode
TRG/FREE/HALF/ONE, the LFO.T trig flag, SYNC) are the same on DT2.

## Method 1 — free-run + a 1ST-condition reset trig (Lauli, "works pretty reliably")
- Default LFO **MODE = FREE** (so it evolves across the pattern).
- Drop a **trigless/yellow trig at step 1**, **trig condition = 1ST**, with **LFO.T enabled
  on the TRIG page** for that trig only.
- P-lock on that step: **MODE = TRG** + the **start phase (SPH)** to the cycle position you
  want. → the LFO retriggers to a known phase on the first pass, then free-runs after.

## Method 2 — TRG by default, disable per-trig (inverse of M1)
- LFO **MODE = TRG** at pattern start.
- **Disable LFO.T** on the TRIG page for most trigs (so they don't retrigger it).
- A **yellow trigless trig at step 1 with LFO.T p-locked ON** does the single clean reset.

## Method 3 — leave FREE, lock SYNC on the first real trig (Humanprogram)
- All trigs **MODE = FREE**.
- On the **first regular trig**, p-lock the LFO **mode to SYNC** → that hit starts/aligns the
  LFO while the rest let it run on.

## Known limitation (OP, unresolved in thread)
- Methods 1 & 2 can **fail when you switch INTO the pattern while the machine is already
  running** (the LFO doesn't re-phase on a live pattern change). Workaround if it matters:
  use a **pattern CHAIN** so the switch happens at a bar boundary.

NOTE: param abbreviations — **SPH = LFO Start Phase**, **LFO.T = the LFO-trig flag on the
TRIG page**. These let you have evolution AND repeatability in the same pattern.
