https://www.strymon.net/faq/bigsky-firmware-download-revision-release-notes/
strymon.net · Strymon (official) · release-notes page (retrieved 2026-06-03)

# Big Sky (original) firmware revision history

Updates flashed over MIDI via Strymon's **Nixie** app. Last firmware for the original Big Sky is **v1.49**.

| Version | Date | Changes |
|---|---|---|
| **1.49** | Mar 2019 | Added support for MultiSwitch Plus. (Final original-Big-Sky firmware.) |
| **1.44** | Nov 2017 | **MIDI Clock moved from a GLOBAL setting to a PER-PRESET parameter** ("midi clock per preset functionality"). Added MIDI **THRU** mode (true passthrough); the old "ON" mode renamed **MERGE**. Compatible with Nixie 1.0. Fixed a MIDI-clock pulse-counting issue during the initial cycle. |
| **1.23** | Feb 2015 | Added MultiSwitch EXP controller support (TAP / Bank / Preset EXP modes). Added the **MIDICL** global parameter to enable/disable MIDI clock. Fixed display issues (invalid characters, decimal points). |
| **1.19** | Jun 2014 | Fixed Reverse coefficient calculation; minor bug fixes (archived; ported into 1.23). |
| **1.15** | Feb 2014 | **Added MIDI Clock** and a Level-test function. Fixed MIDI preset loading for presets >255. Fixed PARAM display text + MIDI controller for Tone and Mod Depth. |

## Notes / corrections for the dossier
- **MIDI Clock is per-preset since v1.44** — only presets that have the clock parameter set ON will follow incoming clock. This matters for the failover bank: clock-sync must be enabled on each preset that should track the Digitakt's tempo, it is NOT a global on/off after 1.44.
- The release notes here **do not mention the Reflections machine being added in a firmware update**. (The dossier states Reflections "was added in a firmware update after launch" — that claim is NOT corroborated by these official release notes and should be treated as **unverified**.)
- Confirm the unit is on **1.49** before trusting it as the H90 failover.
