https://www.chasebliss.com/support
Chase Bliss support / community-repeated troubleshooting wisdom · accessed 2026-06-03

# Universal Onward (and CB) troubleshooting rule: "turn all the dip switches OFF"

The single most-repeated piece of CB community/support troubleshooting wisdom, and it applies directly to the Onward because of how much of its behavior is buried in the 8 top-mounted Customize dips (DRY KILL, DUCK, SIDECHAIN, MANUAL, REVERSE, ½ SPEED, LATCH, MISO, SPREAD — all saved with presets):

> **If your pedal is doing odd things, the answer is probably in the dip switches — turn them all off, that will usually do it.**

Why it bites on the Onward specifically:
- The dip states are **saved into presets**, so a weird preset can silently carry MANUAL (no dynamic triggering — feels "dead"), DUCK/SIDECHAIN (channel pumping/dropping), MISO (mono→stereo), or a half-speed lo-fi state into the next song without you touching a knob.
- Combined with the **power-up gestures** (Dry Kill = hold Glitch on power-up; Trails = hold Freeze on power-up), it's easy to land in a state where "no dry / no sound / no trigger" looks like a fault but is actually saved config. See the ML10X thread (`morningstar-onward-ml10x-gotcha.md`) for a real instance fixed by factory reset.

**Recovery ladder for this rig:** (1) middle PRESETS position = live knobs, (2) all dips OFF, (3) check SENSITIVITY (hidden on SIZE) ~noon so it's actually triggering, (4) if still wrong, factory reset (CC56 or onboard gesture) and rebuild the preset.

(Honest flag: the "turn dips off" phrasing is community/support folk-wisdom surfaced via search, not a verbatim quote from a single attributable post; the underlying behavior — dips saved with presets, gestures on power-up — is verified in the manual/dossier.)
