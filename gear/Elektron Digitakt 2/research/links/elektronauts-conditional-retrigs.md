https://www.elektronauts.com/t/simple-tip-conditional-re-trigs/57273
elektronauts.com · community thread (lindefelt, Hawk) · 2018→ (technique still current on DT2)

# DT/DT2 — Conditional re-trig trick (fills that only fire sometimes)

A retrig recipe that gates the roll itself behind a trig condition, so a fill/riser only
happens on some passes — useful for hands-free drone/doom build-ups (cf. the LAST/NOT-LAST
transitions already captured). Technique-level (no integers posted), but the step logic is
concrete.

## The trick (lindefelt)
1. Set up a **retrigging trig as usual** (TRIG page 2: RETRIG on, set RATE/LEN).
2. Add a **trig condition** to that retrig trig (e.g. `1:4`, `FILL`, `25%`).
3. On the **PRECEDING trig**, set a **retrig RATE that lands ON the conditional trig's step**.
4. Result: when the condition is **TRUE**, you get the dense retrig roll; when it's **FALSE**,
   the preceding trig's own retrig simply plays the "normal" hit instead — no gap.

## Alternative within-track stutter (Hawk)
- Duplicate the step onto the next beat, **slam its micro-timing fully LEFT**, and set a
  **PRE / false condition** on it → a tight near-flam stutter without a real retrig rate.
- Cross-track version: route the roll to a second track and gate it with a **NEI** (neighbor)
  or **FILL** condition.

NOTE: no RATE/LEN/VFAD integers were posted — only the conditional-on-the-retrig logic. Use
with the existing retrig values (RATE = subdivision, LEN = step count, VFAD = ±fade). For the
rig: put a fast retrig riser on a FILL/1:4 condition so the DT2 throws occasional swells into
the wall while both hands ride the Microcosm/H90.
