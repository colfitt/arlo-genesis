DISK VERIFICATION — local plugin Info.plist + bundle-id inspection (2026-06-10)
local · researcher facet-agent · 2026-06-10

## CRITICAL FINDING: "Nudistort" is NOT a Devious Machines product

The plugin installed in `Software/Devious Machines/` is **Nudist Audio Nudistort**,
mis-filed under "Devious Machines" — the same `scan_plugins.py` brand-grouping bug
that previously mis-filed Pure LoFi (Arturia) and DS-10 Drum Shaper (XLN).

### On-disk proof
- AU: `/Library/Audio/Plug-Ins/Components/Nudistort.component`
- VST3: `/Library/Audio/Plug-Ins/VST3/Nudistort.vst3`
- `CFBundleIdentifier = com.NudistAudio.Nudistort`  (BOTH AU and VST3)
- AU Info.plist `name` string = **"Nudist Audio: Nudistort"**
- AU `description = Nudistort`, `manufacturer = Manu` (4-char AU manu code)

### Vendor confirmation
- Devious Machines' product catalog (deviousmachines.com) lists: Infiltrator 2,
  Duck 2, Bass Focus, Pitch Monster, Texture, **Multiband X6**, UrsaDSP Boost
  (+ Infiltrator/Texture expansions, Pro Effects Bundle 2). **No "Nudistort" and
  no "Nudistort 2" exists.** Devious Machines' multiband product is **Multiband X6**,
  a *compressor*, not a distortion.
- **Nudistort is by Nudist Audio** (nudistaudio.com), a separate small developer.
  Their other product is **Fermenter** (2025). $40 (often $32 on sale).

### Implication for the research brief
The task brief described "Devious Machines Nudistort 2 — multiband distortion,
EDM/sound-design-leaning." That framing came from the mis-attribution. The ACTUAL
installed plugin is Nudist Audio Nudistort: a creative/experimental distortion +
delay + modulation mangler (NOT multiband, NOT a compressor, no "version 2").
This file documents the correction; the rest of the research targets the real
Nudist Audio Nudistort.

### Repo follow-up suggested (for orchestrator)
- Move `Software/Devious Machines/` contents → `Software/Nudist Audio/`
  (folder currently holds ONLY Nudistort; once moved, "Devious Machines" is empty
  and not actually installed at all).
- The `scan_plugins.py` "key off bundle-id manufacturer" fix should already map
  `com.NudistAudio.*` → "Nudist Audio"; verify it ran / re-run the scan. The
  CONTENTS.md note "Auto-generated from scan_plugins.py" suggests the folder was
  created before the fix landed, hence the stale "Devious Machines" grouping.
