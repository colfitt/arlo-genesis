https://gearspace.com/board/apple-logic-pro/1126016-arturia-v5-crashing-logic-all-over-place.html
gearspace.com + forum.reasontalk.com + Arturia FAQ · CPU/stability lore

THE RECURRING TRUTH: Arturia's V instruments are gorgeous but historically CPU-
HEAVY. Multiple V plugins on a project will tax the CPU; the standard advice is
to FREEZE / bounce-in-place tracks once a part is committed.

WORST OFFENDERS (community consensus):
- The AUGMENTED series is the CPU hog — Augmented Strings and Augmented Voices
  in particular are called out as among "the most CPU-intensive plugins ever
  used." They layer two full sample+synth engines + per-layer FX, hence the cost.
- High unison counts (up to 18 oscillators) and oversampling multiply load on
  the analogue-modelled synths (CS-80 V, Jup-8 V4, Modular V, Matrix-12).

LOGIC-SPECIFIC MITIGATIONS:
- Freeze (snowflake) the Arturia track after you like the part — biggest win.
- Lower the instrument's internal oversampling/quality where exposed.
- Use the STANDALONE app to design the sound (no host overhead), then load the
  preset in the AU and freeze.
- Watch the per-core meter (Logic CPU is per-thread): one heavy Arturia instance
  can pin a single core even when the overall meter looks fine.
- Bounce long evolving drone/pad parts to audio early — you rarely need to keep
  re-rendering a 2-minute wash live.

STABILITY: older crashes were largely AU-validation / Rosetta-mismatch issues;
keeping ASC + the plugins updated and running native arm64 resolves most.
