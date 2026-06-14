https://support.native-instruments.com/hc/en-us/articles/209558589-Using-Kontakt-as-a-Multi-timbral-Instrument-in-Logic-Pro-X
NI support + ADSR (https://www.adsrsounds.com/kontakt-tutorials/how-to-use-a-multitimbral-instance-of-kontakt-in-logic-pro-x/) + SoundOnSound · distilled · current

# One Kontakt instance, many MIDI channels (multitimbral) in Logic

**Why:** run several instruments inside ONE Kontakt (saving RAM/instances) but drive each from its own Logic track. Pairs with multi-output so each also gets its own mixer channel/FX.

**Setup A — the easy way (Logic's checkbox):**
1. New Tracks dialog → **Software Instrument** → check **Multi-timbral** → enter the number of parts (up to 16).
2. Logic creates that many sub-tracks; each is one Instrument inside Kontakt on its own MIDI channel.
3. Kontakt **auto-increments the MIDI channel** for each instrument you add — you don't set it manually.
4. Combine with the **Multi-Output (16×Stereo)** instance + aux tracks (see logic-multiout file) to mix each part separately and add per-part FX.

**Setup B — Environment multi-instrument (power-user):** put up to 16 instruments in one Kontakt instance, each on its own MIDI channel; create a **multi-instrument object** in Logic's Environment and cable it to the Kontakt channel object → 16 arrange tracks all feeding the single instance.

**Caveats:**
- MIDI **CC** automation in multitimbral instances is fiddly in Logic — CC can bleed across channels or be hard to record per-part; many users keep heavily-automated instruments on their own single instance instead.
- The classic tradeoff: **one multitimbral instance = lower RAM/instance overhead but everything on one CPU core**; **separate instances = more cores used + cleaner automation but more overhead.** For drone work (few voices, long notes) one multitimbral instance is usually fine; for dense layered sessions, split to instances per the Impact Soundworks multicore advice.

**Rig recipe (ambient layering):** load a Spitfire string pad on ch.1, a LABS texture on ch.2, a granular drone on ch.3 in ONE Kontakt; multi-out them to three Logic auxes; hold a chord across all three from a single MIDI region copied to three tracks (or stack tracks) → instant evolving wall, each layer independently EQ'd/reverbed.
