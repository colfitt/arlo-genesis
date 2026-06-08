https://cdn.shopify.com/s/files/1/0920/2928/8752/files/MC_manual_WEB.pdf
hologramelectronics.com · Microcosm Owner's Manual (© 2020 Hologram Electronics) · §7 Saving Presets, §8 MIDI

# Microcosm presets — banks, saving, loading, and how sharing actually works

Authoritative facts pulled from the official manual PDF (text extracted locally). This is the
canonical reference for the "how banks/management work" question.

## The 16 user slots + 4 color banks
"Microcosm's User Preset section has **16 save slots, organized into 4 color coded banks (Red,
Yellow, Green, and Blue)**." User Presets "will retain any parameters and loops that were
active at the time of saving. Any overdubs will be 'mixed down' into a single loop file so
that additional overdubs can be layered on top in future performances."

**Global Configuration settings are NOT saved with User Presets** (so stereo-in, bypass mode,
Hold toggle/momentary, MIDI channel etc. are global, not per-preset). The User bank lives at
the end of the Preset Selector rotation, after the 11 effect banks.

## Saving (3 steps, verbatim)
1. "Hold down the Preset Selector until the Indicator Lights flash blue. This indicates that
   the settings and recorded phrase have been copied."
2. "Cursor will blink to indicate copied material. Turn to the desired User Preset slot and
   hold down the Selector again to save the preset." (Click the Selector to cancel.)
3. "Indicator Lights will flash blue as information is stored… all of the pedal's current
   parameters and any recorded phrases will be saved." Note: "Longer recording times may take
   longer to save than presets with shorter loops."

## Loading / previewing / overwriting
- Load: scroll to the User bank, scroll to a slot. "Knob position does not necessarily reflect
  the actual settings when using saved presets" — touch a knob and it jumps to the physical
  position.
- **Preview before overwrite:** while settings are copied (Step 1), the pedal still operates
  and loads presets, so you can audition a slot's loop/effect before overwriting it.
- **Overwrite / save-in-place:** saving to an occupied slot replaces it; re-save to the same
  slot to update in place.
- **Copy a loop out of a preset:** idle over a User Preset, hold Selector until lights flash
  (loop copied), navigate to an effect, hold again — the loop loads into the live effect
  section. *User Preset settings do NOT transfer to the live effect section — only the loop —
  and the transferred loop overwrites any loop currently present.*

## CRITICAL: there is NO preset export / backup / sharing format
The manual's MIDI section (§8) documents **only**: Control Change (CC) map, a Program
Change / Preset chart, MIDI Clock, and Thru. **There is no SysEx preset dump, no preset
backup, and no preset file format.** SysEx on the Microcosm is used **only for firmware
updates**. Practical consequences:
- You **cannot** share a `.syx` patch file the way you can with, e.g., a Strymon or Empress
  pedal. Presets live on the device only and are lost on factory reset.
- "Sharing a preset" therefore means **publishing the recipe** (engine + variation + knob
  positions + Global Config), which the recipient dials in by hand. This is why commercial
  "preset packs" (see Tone Shepherd) are sold as settings sheets / instructions, not files.
- Back up your own work by **photographing the panel** and writing down engine+variation+knob
  clock-positions per slot. There is no on-device or computer backup path.

## MIDI Program Change → preset map (for recalling slots from a controller)
Sending a PC message switches between the 44 effect variations and 16 user presets:
- PC #1–4 ARP A-D · #5–8 INTERRUPT · #9–12 BLOCKS · #13–16 GLIDE · #17–20 SEQ ·
  #21–24 MOSAIC · #25–28 HAZE · #29–32 TUNNEL · #33–36 STRUM · #37–40 PATTERN · #41–44 WARP
- **#45–48 USER BANK 1 (A–D) · #49–52 USER BANK 2 · #53–56 USER BANK 3 · #57–60 USER BANK 4.**
So the 16 user slots are addressable as PC #45–60 — useful for recalling specific frozen-drone
or rhythmic-arp presets from the rig's MIDI controller / clock master.

## Organizing the 16 slots (suggested convention for this rig)
The banks are just color labels — no enforced category — so impose your own scheme. A sensible
layout for a drone/doom/shoegaze board:
- **Red bank** = frozen-drone beds (Tunnel B, Haze A) ready for Hold Sampler.
- **Yellow bank** = rhythmic / tempo-synced engines (Mosaic D, Arp, Pattern) to lock to MIDI clock.
- **Green bank** = smear/wash engines (Haze B, Warp B, Glide A) feeding the Etherealizer/Dark Star stage.
- **Blue bank** = looped banjo/built-composition presets (Mosaic A with a saved loop).
