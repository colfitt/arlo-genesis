https://www.strymon.net/faq/using-strymon-impulse-manager-with-iridium/
strymon.net · Strymon official FAQ · undated (current as of 2026)

# Custom IR loading workflow + gotchas (authoritative)

**File spec (hard requirement):** Iridium loads only **24-bit / 96 kHz WAV** files, **mono or stereo**, **up to 500 ms** in length. Files that don't meet all three criteria are **rejected by Impulse Manager** (won't even appear as loadable). This is the #1 gotcha — most third-party IR packs ship 24/48 or 44.1 and must be sample-rate converted to 96k first, or you buy the 96k variant.

**Cab-slot architecture:** 9 cab slots total (3 per amp: a/b/c × Round/Chime/Punch). Each slot holds **2 mono IRs (LEFT + RIGHT) OR 1 stereo IR**. You drag-drop compatible WAVs from the left-hand Impulse Responses browser into the LEFT / RIGHT / Mono section of a slot.

**Per-cab tone editing (hidden depth):** Click the Info button (circled "i") on a selected slot → sliders for **LEVEL, TREBLE, BASS** per cab. By default they're locked across both channels; **un-check "Match left channel"** to set LEFT and RIGHT independently. This lets you trim a too-bright IR or balance an L/R pair without re-rendering the WAV.

**Collections:** "Save Collection" snapshots all 9 slots as a named set. Stored on disk at `/Users/[username]/Documents/Strymon/collections` (Mac & Windows). Factory + vendor collections (OwnHammer/Celestion/cabIR/Valhallir) ship expandable so you can pull individual factory IRs back. **SYNC CHANGES** writes edits to pedal memory — must click before disconnecting USB or changes are lost.

**Rig note:** for the bass-DI use (Jazz Bass + AMP DISABLE), load a bass-cab WAV here; for the JHS Colour Box V2 / external-preamp use, the slot just needs a good guitar cab IR since the amp stage is bypassed.
