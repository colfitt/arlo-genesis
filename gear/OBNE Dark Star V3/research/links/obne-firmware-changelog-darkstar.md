https://firmware.oldbloodnoise.com/
firmware.oldbloodnoise.com · OBNE official updater · fetched 2026 (current)

Authoritative Dark Star (Stereo / V3) firmware changelog, verbatim from OBNE's web updater. NOTE: the dossier lists V3.0Q as latest — the updater now shows a NEWER version, V3.0R. Update the dossier.

VERSION HISTORY (verbatim)
- V3.0J — "Initial production version"
- V3.0K — "Fixed pot override issue on initial preset recall"
- V3.0L — "Improved processing speed and memory storage routines"
- V3.0M — "Fixed issue where unity pitch would not be recalled correctly from preset"
- V3.0Q — "Fixed new pitch recall issues from 3.0M, improved factory reset"
- V3.0R — "Fixes issue where restart of external MIDI controlling device would halt MIDI communication until restart of OBNE device"  ← LATEST

FIRMWARE LORE / WHAT THIS MEANS
- A cluster of early fixes (K, M, Q) are all PITCH / PRESET-RECALL bugs — i.e. presets recalling the wrong pitch values. For a preset-driven board this matters; stay current.
- V3.0R is the MIDI-stability fix: before R, if your external MIDI controller (e.g. a MIDI brain on the pedalboard) was power-cycled/restarted, MIDI comms to the Dark Star would HANG until you also restarted the Dark Star. Directly relevant to any rig running a board-wide MIDI controller. Recommend V3.0R for this rig (was previously documented as "keep it on Q").
- Updates are over USB-C via this page (Chrome/WebSerial-style browser updater).
