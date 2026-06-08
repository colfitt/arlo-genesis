https://www.strymon.net/support/nixie-2/
strymon.net · Strymon (manufacturer) · current (Nixie 2, supports original Big Sky)
+ companion FAQ: https://www.strymon.net/faq/how-do-i-import-a-preset-with-nixie-2/
+ Nixie 2 manual: https://www.strymon.net/manuals/Nixie_v2_UserManual_RevA.pdf
+ update post: https://www.strymon.net/nixie-2-update/

## What Nixie 2 is
Strymon's free preset editor / librarian / firmware updater (Mac + Windows 10/11).
Replaces the original Nixie (which was the only way to flash the Big Sky to firmware
v1.49). For the Big Sky specifically it does: **backup/restore the whole pedal**,
**organize and rename presets**, **create/edit presets from the computer with full
parameter access**, **import/export individual presets**, and **flash firmware**.

## The preset SHARING format = .syx (SysEx)
> "Presets for our pedals are stored as **.syx (sysex) files** that can be imported or
> exported using Nixie 2."

This is the universal currency for Big Sky preset sharing — every community pack, blog,
forum, and Discord trades .syx files. Each .syx can be a single preset or a bank dump.

## How to IMPORT a preset (FAQ, quoted)
> "click **file → presets → import preset →** then select the .syx file you want to add."

Once imported, the preset appears under "BigSky" in the LIBRARY list (left side of
Nixie 2); from there you drag/write it to a slot on the pedal.

## Connecting a Big Sky (NO USB — this is the catch)
The original Big Sky has 5-pin DIN MIDI only, no USB, so Nixie 2 talks to it through a
**MIDI interface**. Strymon's support page is explicit:

- Recommended interfaces: **Roland UM-ONE MKII**, **iConnectivity mio XC**, **Strymon Conduit**.
- "Plug-and-play" cheap MIDI cables are **not recommended** (reliability issues).
- Wiring: interface MIDI OUT → Big Sky MIDI IN; Big Sky MIDI OUT → interface MIDI IN.
- In the Big Sky **GLOBLS** menu set: **MIDI PA = ON**, **MIDI CT = ON**, **MIDI TH = MERGE**, **MIDI ST = OFF**.
- Launch Nixie 2 → pedal auto-detects.

(This rig owns a **Strymon Conduit**-class need anyway; any of the three named interfaces
works. The Eventide H90's USB does NOT help the Big Sky — Big Sky must go through DIN MIDI.)

## Sharing ecosystem reality check
- Nixie 2's "sharing" is **import/export of .syx files** plus the marketing line
  "Download user created presets online and create your own to share with friends."
- I could **not** confirm a built-in in-app cloud browser / official central preset
  exchange inside Nixie 2 for the original Big Sky. Sharing in practice = you obtain a
  .syx from a blog/store/forum/Discord and import it. (Flag: unverified whether a
  first-party in-app library exists for the original Big Sky; the BigSky **MX** got
  free first-party "Preset Pack 1" downloads, but that's the MX, not this unit.)
- Strymon also publishes free official .syx packs (e.g. "This Week's Preset" downloads,
  and MX preset packs) — but the original Big Sky's restore/backup file and "This Week's
  Preset" .syx files are the first-party freebies that apply here.

## Backup before flashing / before importing
Always back up the pedal (whole-unit dump) in Nixie 2 before importing/overwriting —
imported presets overwrite the target slot. Confirm firmware **v1.49** (last for the
original) while connected; Nixie 2 handles the flash.
Ref: https://www.strymon.net/gear-guide-backing-restoring-presets-bigsky-mobius-timeline/
