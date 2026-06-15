---
type: chain
title: "Lost & Found → Big Time Stacked Tape Degradation"
date: 2026-06-15
artists: [Boards of Canada, William Basinski]
instrument: guitar / synth
gear:
  - Chase Bliss Lost & Found
  - Chase Bliss Big Time
  - Chase Bliss MOOD MkII
---

# Lost & Found → Big Time Stacked Tape Degradation

A VHS-degraded, pitch-warped source feeding a saturated tape echo, then micro-looped — two-plus layers of deliberate "recorded-wrong" decay, each tape job split across its own box. The point of the split is to *avoid GenLoss-on-GenLoss mud*: Lost & Found **ages** the source (Gen Lite wow + crinkle), Big Time **repeats** it (saturated 0.5X echo), and MOOD **captures** the result into a micro-loop. COLOR on the Big Time stays low on purpose — the source is already hot coming out of the Gen Lite stage, and over-saturating a pre-degraded signal "sounds awful." This is a 🟣 DOUG-designed integration; no artist played this exact chain.

## Signal path

guitar / synth → **CB Lost & Found — "VHS Tape-Age (Gen Lite, Full Wet)"** (6B Gen Lite, single slot, MIX FULL, slow wow) → **CB Big Time — "Crushed Analog"** (Saturated · Warm · 0.5X ON · COLOR modest) → **CB MOOD MkII — "Balance Beam — degraded-but-in-tune Tape loop"** (Tape micro-loop, light grit) → out.

## Per-unit

- **CB Lost & Found — "VHS Tape-Age (Gen Lite, Full Wet)":** R slot = **6B Gen Lite** (a mini Generation Loss MkII), run as a single channel so it reads as believable tape, not per-side chorus. TIME pushed toward MAX = **slow wow** (the seasick VHS pitch-warp), MODIFY ~12:00–1:00 sets warble depth, ALT (failure/crinkles) ~10:00–11:00 for tape crinkle, BLEND toward Gen Lite ~2:00 sets the degrade amount, **MIX FULL** (Gen Lite wants full wet to read as real tape). **SPREAD OFF**, TRAILS on. This is the *aging* stage — it does the wow + crinkle so Big Time doesn't have to.
- **CB Big Time — "Crushed Analog":** factory starter for vintage echoes — MODE **Short** (dial to **Long** if you want longer sagging repeats under the loop), STATE **Saturated**, VOICING **Warm**, **0.5X ON** (the built-in 12-bit crush the concept asks for), COLOR **~45% / modest** (the source already arrives degraded — don't double-saturate), FEEDBACK ~45%, WET ~45%, TILT EQ slightly above noon to cut mud, MOTION Sine subtle. This is the *repeating* stage.
- **CB MOOD MkII — "Balance Beam — degraded-but-in-tune Tape loop":** Looper MODE **Tape**. Capture a phrase of the saturated echo, then **lower CLOCK gently** for grit/aliasing and **raise looper MODIFY** to bring the loop back up to its recorded speed — degraded-but-in-tune. Keep **CLASSIC OFF** and CLOCK only lightly down so MOOD adds *vibe*, not a fourth full tape-degrade pass. This is the *capture / micro-loop* stage. ROUTING IN+micro-loop so you can play fresh over the loop.

## Routing

Straight mono-or-stereo series, three boxes, no clock required (this is texture, not a rhythmic grid — though MOOD can take MIDI clock from the rig master if you want the loop length locked). **The whole game is splitting the two tape jobs across boxes and gain-staging so the degrade compounds without turning to porridge:**

1. **Lost & Found does the aging.** Gen Lite at full wet supplies the wow + crinkle + tape crush. Because Gen Lite is itself a mini Generation Loss, you do **not** also run a full Generation Loss in front — that's the GenLoss-on-GenLoss mud the concept is built to avoid.
2. **Big Time does the repeats, COLOR kept low.** The signal hitting Big Time is already hot and saturated, so COLOR sits ~45% — modest. Cranking it here just clamps a pre-degraded source into mush. STATE Saturated + Warm + 0.5X gives the murky vintage echo character *without* needing high COLOR.
3. **MOOD captures, lightly.** Balance Beam keeps the loop in-tune while adding aliasing vibe — the third "layer" of decay is the *act of looping the already-degraded echo*, not a third saturation stage. Keep CLASSIC off and CLOCK gentle so MOOD doesn't fight the upstream degrade.

If it gets muddy, pull Big Time COLOR down first (not up), then back off the Gen Lite BLEND — the two tape stages are where mud accumulates.

## Sound

A seasick, hot VHS-warped source that smears into a saturated tape echo and then settles into a slowly-decaying micro-loop — two-plus layers of deliberate "recorded-wrong" decay, each one doing one job cleanly so the whole thing degrades without collapsing into undifferentiated hiss. Taste-ref: Boards of Canada's wow-warped tape nostalgia / William Basinski *Disintegration Loops* — a captured loop that ages as it repeats.

## Play

Play a sustained chord or a slow synth pad into the Gen Lite stage and let the slow wow pull the pitch around. The Big Time repeats it back saturated and 12-bit-crushed at 0.5X. When you hear a phrase you like, **tap the MOOD Micro-Looper** to capture it, then play fresh material over the top while the captured loop ages underneath. For a deeper sag, push Big Time to MODE **Long**; for a more obviously "broken" loop, nudge MOOD CLOCK lower (but watch the mud). The discipline is restraint at the second box: keep Big Time's COLOR modest so the hot source stays legible through the decay.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Lost & Found — "VHS Tape-Age (Gen Lite, Full Wet)"** (created) + **CB Big Time — "Crushed Analog"** (factory #7, reused) + **CB MOOD MkII — "Balance Beam — degraded-but-in-tune Tape loop"** (reused). Splits the two tape jobs across boxes to avoid GenLoss-on-GenLoss mud; COLOR-modest-after-degrade gain-staging is documented in the Crushed Analog sheet ("over-saturating a pre-degraded source sounds awful").
- Gen Lite full-wet / SPREAD-off-for-real-tape recipe from the Lost & Found patch maps (BachelorMachinesTV Pt1/Pt2). Big Time Saturated/Warm/0.5X mechanics from `research/links/cb-big-time-factory-presets-recipes.md`. Balance Beam degrade-but-in-tune Tape loop from MOOD MkII manual p.33.
- Note: unpublished knob clock-positions in the created L&F patch are a dialable recipe (DOUG's interpretation), not factory-published numbers.
