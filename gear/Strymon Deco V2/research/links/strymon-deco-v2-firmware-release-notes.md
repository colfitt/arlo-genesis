https://www.strymon.net/faq/deco-v2-firmware-revision-release-notes/
strymon.net · Strymon (official) · "Deco v2 Firmware Revision Release Notes"

Authoritative V2 firmware changelog. Update via USB-C using Nixie 2.2.0 (for v1.33+) or older Strymon Update app. The fixes here directly corroborate real-world community gotchas.

## v1.33 — November 2024 (latest as of research)
- Added Nixie 2.0 compatibility (requires Nixie 2.2.0 to flash).

## v1.22 — September 2023
Fixes:
- **"Sweeping the SATURATION knob from maximum to minimum quickly results in a loud momentary volume burst."** ← This was a real bug. Validates the community "it's a gain device, watch the volume" warnings — early units could spike. FIX is in firmware, so KEEP FIRMWARE CURRENT if you ride the Saturation knob live.
- Press-and-hold audio functions (Auto-Flange) could engage unintentionally with fast footswitch activation.
- Presets with MIDI Clock Tap Division settings failed to recall those settings.
New:
- Added **MIDI CC# 25 for Clock Division** (the mult/div CC documented in the Rev D manual — so it's a post-launch addition).

## v1.20 — August 2022
Fixes:
- **"Pedal locks up and loses audio output after random MIDI Program Change message."** ← notable bug for a MIDI-heavy rig. If running PC-per-song, be on v1.20+ at minimum (ideally latest).
- MIDI Clock divisions setting was not saved with presets.
New:
- **Auto-Flange press-and-hold now works even when the Doubletracker is bypassed** (originally you had to have the doubletracker engaged). Means you can keep the doubletracker off and still grab the momentary through-zero flange as a transition.

## Rig takeaway
This rig is MIDI-recallable and uses the Deco as an always-on saturation/glue voice you may ride. Both classes of fix (Saturation volume-burst; MIDI PC lockup) matter here — update to v1.33. The CC#25 clock-division capability only exists on v1.22+.
