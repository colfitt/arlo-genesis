https://native-instruments.com/ni-tech-manuals/raum-manual/en/global-controls-and-freeze
native-instruments.com · RAUM manual (Global Controls & Freeze) · n.d. (accessed 2026-06)

# RAUM — Global controls & Freeze (official manual)

## ★ CORRECTION to the project navigator
**Freeze is available for the GROUNDED and AIRY algorithms ONLY — NOT Cosmic.** Direct
manual quote: *"The Freeze function is available for the Grounded and Airy algorithms."*
The existing nav line "Cosmic mode + Freeze = infinite drones" is **factually wrong about the
combination.** Infinite *Cosmic* drones come from **Feedback = 100% in the predelay path**
(see `raum-manual-predelay-filters.md`), not from Freeze. Freeze-drones are a Grounded/Airy
thing. Both routes give infinite sustain; they are different mechanisms. FLAG: nav needs this fix.

## Freeze — what it actually does
- Holds the reverb's current sound content for as long as it's active → turns RAUM into a
  **sound generator** (the tail sustains forever).
- Designed as a **performance element**, not set-and-forget. Catch a chord/wall, freeze it,
  play over the top.
- **When Freeze is ON, only the Size control still affects the sound** — every other reverb
  control greys out. So the *one* live gesture available during a freeze is riding **Size**.

## Global controls (centre section)
- **Reverb Algorithm** — Grounded (rooms) / Airy (halls) / Cosmic (abstract spaces).
- **Mix** — equal-power crossfade between dry input and effect. (For sends: Mix = 100% wet.)
- **Mix Lock** — preserves current Mix when switching presets (so preset-browsing on a 100%-wet
  send doesn't reset you to a dry-blended preset).
- **Reverb** — intensity of reverb added to the effect signal (separate from Mix; this is the
  "how much reverb vs. how much raw predelay/echo" balance).
- **Freeze** — the hold button.

## Freeze riser recipe (from NI's own guidance)
Size → 100%, activate Freeze, then **turn Size to the LEFT** = riser effect.
- **Density = Dense** → consistent wash of noise.
- **Density = Sparse** → dispersed, granular riser.
