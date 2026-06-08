https://www.strymon.net/manuals/BigSky_UserManual_RevD.pdf  (+ TGP spillover-via-switchers thread, official preset notes)
strymon.net (manual) / thegearpage.net · multiple · retrieved 2026-06-03

# Spillover, Persist, Freeze vs Infinite — behavior + the #1 community gotcha

## Two different trail features (commonly confused)
- **PRSIST (Persist, per-preset):** keeps THAT preset's tail alive when *that same preset* is bypassed. Turning Persist ON **forces analog buffered bypass** for that preset (you lose true bypass).
- **SPLOVR (Spillover, global):** lets the current preset's wet tail **spill into the NEXT preset you select**.

## The 5-second gotcha (most-cited pitfall)
- **The current preset must have been active for at least ~5 seconds before spillover will carry into the next preset** (a buffer-architecture limitation). Change presets faster than that and the tail **cuts off**. Bites anyone switching patches quickly. Plan patch changes (and stage cues) around this; for the failover bank, don't expect instant-flick spillover between scenes.

## Freeze vs Infinite (per-preset HOLD parameter, hold a footswitch to trigger)
- **INFNTE (Infinite Sustain):** freezes the wash AND each new note you play **adds to / builds up** the frozen drone.
- **FREEZE (Reverb Freeze):** freezes the wash in place and lets you **play new notes over the top WITHOUT adding** to the held drone.
- **For drone/doom: FREEZE is usually the keeper** (stable held wall + clean lead over it). INFNTE is for building an ever-thickening drone.
- Hold can be emulated/latched from a MIDI controller (momentary press/release, or Toggle Mode to latch) — see strymon-midi-clock-predelay-sync.md.

## Other documented gotchas
- **Bypass LED goes dark when bypassed** — can't see which preset is loaded (SOS confirmed). Live recall relies on memory or the MIDI controller's display.
- **Magneto/Nonlinear remap the front knobs:** PRE-DELAY → Feedback, DECAY → Time. Reaching for "pre-delay" by muscle memory on these two machines does something else.
- **Spillover across patches via external switchers (TGP):** to keep trails when an outboard switcher changes loops/patches, you must keep the Big Sky's signal path intact (buffered/Persist) — true-bypass switching upstream kills the spilled tail. Manage trails with MIDI program change to the Big Sky itself rather than a relay switcher cutting it out.
- **Factory ships with banks 00A–33A duplicated into the next two MIDI banks**; re-init to defaults via power-up holding **A+C** if the preset map looks wrong.
