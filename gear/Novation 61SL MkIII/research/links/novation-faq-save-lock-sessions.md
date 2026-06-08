https://userguides.novationmusic.com/hc/en-gb/articles/25626797279378-SL-MkIII-Session-management
userguides.novationmusic.com · official Session-management KB · current
(KB 403 WebFetch — distilled from search snippets quoting the official text)

The Save-Lock / overwrite gotcha, with the actual procedure.

## Sessions = the save unit
- A **Session** = all 8 Parts × 8 patterns + templates + scales + arp + zones. **64 Sessions** total, recalled by pad.

## The overwrite risk
- Pressing **Save** again **saves in place** (overwrites the current slot). Selecting a **different Session pad while saving** writes to that slot and **overwrites whatever was there**. Fast, but easy to clobber work.
- Sessions can be **loaded remotely by Program Change on channel 16** (and Song Select). The danger: anything in the rig sending PC on ch.16 — a DAW, an Elektron, a sloppy template — can **switch the SL's active Session out from under you and lose unsaved edits.** In a heavily MIDI-meshed rig this is a genuine foot-gun.

## Save Lock (the protection)
- **Hold Shift + Save while powering on** the SL to enable **Save Lock** — blocks all Session saving. The **Save LED is OFF** when locked. The state **persists** if you power off with the power button.
- Use it for any Session you care about, or whenever the rig is live and PC-ch.16 traffic is flying around.

## Rig guidance
- Keep ch.16 **clear of Program Change** across the rig unless you are deliberately using it to recall SL Sessions. If the DAW or an Elektron transmits PC, make sure it's not on ch.16, or enable Save Lock.
- Because templates can only be built in Components and saving is destructive, treat a finished Session as precious: export/back up via **Components** (which also lets you rename Sessions) rather than relying on the 64 on-board slots.
