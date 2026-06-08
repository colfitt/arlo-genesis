https://cdn.eventideaudio.com/manuals/h90/1.8.5/content/h90-control/edit.html
eventideaudio.com (official H90 documentation, H90 Control / Edit menu) · Eventide · firmware v1.8.5 docs · accessed 2026-06-03

# H90 Programs/Presets — terminology, file types, and how to import/export

Consolidated from the official H90 docs (Edit modes + H90 Control) and the Eventide forum's
Patchstorage sharing thread. This is the "how to GET programs and load them" reference.

## Terminology hierarchy (so the file types make sense)
- **List (Playlist)** — a bank of up to 99 Programs. Factory Lists are read-only; User Lists are editable.
  File extension: **`.lst90`**. (An H9's list, `.h9list`-style, can also be imported — see below.)
- **Program** — the top-level patch you select on the pedal; runs **two Presets at once** (A + B).
  File extension: **`.pgm90`**. This is the unit most Patchstorage downloads come as.
- **Preset (A / B)** — one Algorithm + saved parameters. Stored in the **Preset Library**; the
  Library filters by User-saved vs Factory, Favorites, Effect Type, and Algorithm.

## Importing into H90 Control (the desktop editor, Mac/PC over USB)
The reliable, batch-friendly path. Quoted from the official Edit-menu docs:

**Import a single Program (`.pgm90`)** — via the **three-dot (⋮) menu** in the Playlist:
> "Import Program. Load a new Program from a location on your computer."
Community phrasing of the same step (Eventide forum): *"right-click on an INIT Program in H90 Control"
and "select Import Program," then navigate to the downloaded file.* You can import into **any Program
List except the Factory List**. Tip from the forum: **User List 1 ships as a duplicate of the Factory
List**, so it's the safe place to overwrite/build into.

**Import a Program List (`.lst90` or an H9 list)** — in the **Playlist** section:
> "Import List. You can import a Program list created using H90 Control, or an H9 List created using H9 Control."
(One forum note: the import-list control is the *middle icon of the five in the bottom-left corner* —
hover to reveal "Import List," then pick the downloaded `.lst90`.)

**Export** (to back up or share your own):
> "Export Program. Save the Program to a location on your computer." (three-dot menu)
> "Export List. Save the Playlist to a location on your computer." (Playlist section)
> "Export the preset to a location on your computer." (three-dot menu in Preset Library)

## Saving/renaming a Preset ON THE PEDAL (no computer)
From the official Presets edit-mode doc:
- **Press and hold the Presets button** to open the save dialog.
- Move cursor: Select Knob or Quick Knob 1. Pick character: Perform Knob or Quick Knob 2.
- **Quick Knob 2 press** cycles character set (lowercase → uppercase → numbers → symbols).
- **Quick Knob 3 press** deletes a character. **Press Perform Knob to save**; Select Knob to cancel.
- Hard rule: **"Factory Presets must be renamed and saved as a new User Preset to the Library."**
  (Factory content is locked; you fork it.)

## Importing OLD H9 presets/lists into the H90
The H90 reads H9 lists directly (see "Import List" above) — so the **entire H9/H9 Max preset
ecosystem transfers**, which matters because the H90's own preset mythology is younger than the H9's.
Algorithms shared between the boxes map across; H90-only algorithms obviously won't appear in an H9 list.

## Where to GET programs (ranked for this rig — see separate capture files for detail)
1. **Patchstorage — Eventide H90 platform** (free, community): https://patchstorage.com/platform/eventide-h90/
   ~150 uploads / 350+ individual Programs and growing; `.pgm90` and `.lst90`. The richest free well.
   The grassroots effort was kicked off in the Eventide-forum "H90 PATCHSTORAGE" thread:
   https://www.eventideaudio.com/forums/topic/eventide-h90-patchstorage-share-your-presets-programs/
2. **Eventide Presets page** (official factory/artist sets): https://www.eventideaudio.com/presets/
3. **Paid packs** (worship/ambient-leaning, polished): Worship Tutorials, Gideon Boley (26),
   Jake Fauber "TeddyTones" (36), Jay Parmar (14 + free synth-strings) — see paid-packs capture file.

## On-aesthetic note (drone/doom/shoegaze, this rig)
For Blackhole/Shimmer/Wormhole walls + polyphonic pitch, the highest-signal free sources are
rustydutch's experimental/ambient lists and brock's "Music For…" granular-looper programs on
Patchstorage (separate capture file). Factory artist-flavored starting points live in rustydutch's
"Studio Box List" (separate capture file).
