https://www.hologramelectronics.com/pages/microcosm-firmware
hologramelectronics.com (official) · cross-referenced with community version-check posts · firmware v1.13, May 2022

# Firmware lore — there is NO "2.0"; latest is v1.13, plus the version-check trick

## Latest version & the "2.0" myth
- **Latest public firmware = v1.13, released May 2022.** Pedals shipped **June 2022 or later already have it.**
- **There is no Microcosm "firmware 2.0."** Hologram's only public lineage is the v1.1x line (v1.1 announced via their Facebook in 2020/21, iterating to v1.13). Any reference to a "Microcosm 2.0 firmware" or "2.0 new effects" is **inaccurate** — Hologram's later development went into the *Chroma Console*, a separate product, not a Microcosm v2. Flag and reject any "2.0" claim.

## How to check your firmware version (the hidden diagnostic)
1. Enter **Global Configuration**: hold **Shift (the selector/TIME button) + Phrase Looper footswitch** together for ~2 seconds — the LEDs start "dancing/blinking."
2. **Tap the Reverse button 3 times rapidly.**
3. Read the LED pattern:
   - **v1.13 (latest):** Mosaic, Haze, Tunnel **and** Strum LEDs all illuminate.
   - Fewer/different LEDs = an older build → update.

## How updates are installed
- **Browser-based WebMIDI updater** on Hologram's firmware page (requires a MIDI interface connected to the pedal), OR
- **download a `.syx` SysEx file + instructions** and transfer via any SysEx-capable utility.
- No MIDI interface → contact Hologram support.

## Community firmware fix worth knowing
- After ANY firmware update, **do a full factory reset** — community reports (Elektronauts) say this clears loop-transition pops/clicks that otherwise persist post-update.

## What earlier firmware fixed (community-reported, honest)
- Early v1.1-era builds had **erratic onset triggering** on the onset-detection engines (Strum / Arp / Glitch firing inconsistently); later builds tightened detection. Wet-signal/volume handling was also improved over the line. If a pedal is on an early v1.1, these symptoms are likely firmware, not hardware — update it.
