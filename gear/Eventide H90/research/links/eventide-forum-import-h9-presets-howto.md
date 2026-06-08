https://www.eventideaudio.com/forums/topic/how-to-import-h9-presets-to-h90/
Eventide official forum · dirkserries (Q) / tbskoglund (Eventide staff, A) · Mar–June 2024
(Plus general import mechanics corroborated across H90 Control docs)

# Importing H9 presets/lists into the H90 — steps + the real limitations

## Steps
1. **Export from H9 Control:** Presets List tab → top-right dropdown Menu → **"Export preset list"** → save to desktop.
2. **Import to H90 Control:** in the Playlist section use the **Import List** button (the middle of the 5 icons under the current List, on the Parameters/Edit tab; "#7 in the manual"). Name the new list; it appears as a selectable H90 Playlist.
3. **Individual presets:** on the Parameters or Presets tab, click the **3 vertical dots** next to the loaded preset name to browse/load either H9 preset format.

## What import produces
- A new List is created where **each H9 preset becomes a Program with a THRU algorithm in the second (B) slot.** So an H9 single-effect preset lands as Preset A = the effect, Preset B = THRU (pass-through). You then have a free B slot to add a second algorithm — this is the upgrade path.

## The real LIMITATIONS / gotchas
- **Cannot import H9 lists while the H90 is in Dual Mode.** Staff: *"Currently you cannot import H9 lists when the pedal is in Dual Mode but we are looking into the option to allow this."* (tbskoglund, June 10 2024). Switch to Insert/single routing to import.
- **Import was broken in older H90 Control** — use **v1.7.6 or later**; earlier versions failed silently. (If imports "do nothing," update first.)
- **Expression/ribbon mappings don't carry cleanly** — per the megathread, a user importing ~200 H9 presets had to **manually reassign expression-pedal ranges** (the H9 ribbon/expression assignments don't map 1:1).
- USB-only connection to H90 Control (Bluetooth not implemented).

## H9-vs-H90 reality check
- The H90 contains **all 52 H9 Max algorithms** plus the 10 new ones; legacy algorithms were re-voiced (sounds "cleaner, clearer," more headroom per Brock).
- The big win: every imported H9 preset can gain a SECOND simultaneous effect (fill the THRU B slot).
- Watch: parameter-name quirks carried from the Factor pedals (Chorus "Intensity" = mix; Flanger "Intensity" = feedback).

## Rig relevance
If the owner has an H9/H9 Max library, migrate it: export lists, import into H90 Control (NOT in Dual Mode, v1.7.6+), then upgrade favorites by adding a reverb/pitch in the empty B slot. Re-check any expression-pedal assignments after import.
