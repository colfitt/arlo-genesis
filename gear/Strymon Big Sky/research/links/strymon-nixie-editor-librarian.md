https://www.strymon.net/nixie-public-beta/  (+ /support/nixie/ and /gear-guide-backing-restoring-presets-bigsky-mobius-timeline/)
strymon.net · Strymon (official) · retrieved 2026-06-03

# Nixie — preset editor/librarian for the original Big Sky (Big Sky-specific)

NOTE: This is the ORIGINAL **Nixie** (Win/macOS) for TimeLine/BigSky/Mobius — NOT Nixie 2, which is for the newer MX/Volante/etc. generation. The original Big Sky uses original Nixie.

## What it does for Big Sky
- **Real-time bidirectional editing** — turn a knob on the pedal, the same knob moves in Nixie, and vice versa. Full on-screen editing of any machine parameter.
- **Drag-and-drop preset management** — drag single presets or entire collections in/out; reorder/organize for gig sets.
- **Drag presets straight from a web page into Nixie** — this is how the "This Week's Preset" / artist .syx patches get loaded. Strymon hosts Big Sky Bloom/Cloud/Hall/Plate/Shimmer/Swell preset files for direct import.
- **Instant backup/restore** of the whole pedal.
- **Multiple pedals connected at once** — no re-patching to move between TimeLine/Big Sky/Mobius.
- **Offline device mode** — explore/edit a Big Sky you don't physically have connected.

## Connection
- Requires a **MIDI-to-USB interface** from the pedal's MIDI IN/OUT to the computer. (No USB on the original Big Sky — MIDI only.)
- Backups stored at `Documents\Strymon\Nixie\Backup\Pedals` (Windows). Restore: Device menu → Restore Presets → pick backup by date/time → WRITE to device.
- **READ** loads presets from pedal into Nixie (discards unsaved edits); **WRITE** saves Nixie's state to the pedal.

## Rig action item
Use Nixie to **build and back up the H90-failover bank offline now**, then WRITE it to the pedal. Drag in the Strymon ambient .syx patches (Star Cloud / Bloombient / Falling Angel) as a starting library, reorganize to match the program-change numbers the Digitakt/controller fires for the H90.
