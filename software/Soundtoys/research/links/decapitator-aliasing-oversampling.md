https://gearspace.com/board/music-computers/1385528-why-its-worth-upsampling-decapitator-reaper.html
gearspace.com + kvraudio.com · "Why it's worth upsampling Decapitator in Reaper" + KVR "Is it really the bees knees?" + "Digital distortion and aliasing (Proof)"
NOTE: Gearspace/KVR 403 direct fetch — distilled from search snippets, flagged.

# Decapitator — aliasing & oversampling (the main technical gotcha)

- **Decapitator has NO internal oversampling.** Being a hard analog-style
  saturator, it generates aliasing that folds back as inharmonic high-frequency
  junk.
- **Sample-rate behavior:** noticeable aliasing at 44.1k / 48k; **at 96k aliasing
  is virtually gone; no further improvement at 192k.** So the practical fix is
  running the plugin (or the whole session) at ~88.2/96k, or using a host wrapper
  that oversamples just this plugin (e.g. Reaper's per-FX oversampling, or the
  ~2024+ Soundtoys host-level oversampling if available).
- **Harshness cautions:**
  - "Too harsh even on default settings" is a common complaint — usually too much
    Drive into bright material.
  - **Using Decapitator on many tracks stacks the aliasing/harshness** — can get
    "serious" even at 96k. Be deliberate about how many instances.
  - Counter-intuitive warning: adding saturation to "fix" harsh high-frequency
    material can *add* harshness (the aliasing sits up top).
- **How to stay clean:** **low Mix, attenuate highs (High Cut + Steep), and stick
  to styles A / E / N** (the smoother console/preamp models) — "with a very low mix,
  attenuated highs, and mode A/E/N you won't have a harsh sound."
- **Aesthetic flip:** for a degraded/lo-fi rig, the "crusty" aliased sound at 44.1k
  can be a *feature* — gritty digital nastiness on top of analog drive. Use on
  purpose, not by accident.
