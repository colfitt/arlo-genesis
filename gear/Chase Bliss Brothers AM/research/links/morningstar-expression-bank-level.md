https://forum.morningstar.io/t/expression-control-via-midi-for-chase-bliss-am-brothers/11209
forum.morningstar.io · Morningstar User Forum (Chase Bliss subforum) · accessed 2026-06-14

# Brothers AM external-control gotcha: expression rules live at the BANK level

A Morningstar MC-controller user troubleshooting expression-over-MIDI / omniport control of the Brothers AM. The one load-bearing, concrete takeaway (the rest of the existing CC map is already covered in `midi-preset-integration-cb-stack.md`):

## Concrete findings
- **Expression rules must be set at the BANK level, not the preset level.** User's own resolution: *"the omniports were configured correctly but I was trying to set the expression rules in the preset instead of the bank."* → If an EXP-ramp patch (e.g. swelling GAIN 1 into Channel 2) isn't responding, this is the first thing to check on a Morningstar controller.
- **Cabling to feed EXP/CV over the controller's omniport:** a **TRS-to-TRS cable with the omniport set to "Ring Active"** works on current units; alternatively a **TS-to-TRS cable with "Tip Active"** (custom). Matches the AM's floating-ring TRS external-control convention.
- **Two-CC-from-one-pedal trick:** put both target CCs in the Expr.1 preset, then use *"Select Exp Message"* to choose which CC the single expression input drives — i.e. one EXP input can address GAIN 1 *or* VOL 2 depending on the selected message.
- No new per-parameter CC numbers stated here beyond the uniform CB-stack map already captured (knobs CC14–20, etc.).

## Rig relevance
For the ramped-drone patches (EXP/CV → GAIN 1 with MASTER on): if running the AM off the rig's MIDI/EXP controller rather than a plain expression pedal, set the expression rule at the **bank** level. Honest flag: this is a controller-side config note, not a new AM tone setting.
