---
type: patch
title: Premier Guitar reference — fuzz at 100%, ride the volume
device: MXR M173 Classic 108 Fuzz
date: 2026-06-14
description: The textbook silicon-Fuzz-Face setup (Premier Guitar's Strat + '68 Bassman reference rig) — fuzz cranked, all dynamics done with the guitar volume pot for clean-to-filthy from one knob.
tags: [fuzz, fuzz-face, dynamics, volume-cleanup, community]
controls:
  - { name: "OUTPUT/VOLUME", type: knob, value: "5:00 (100%)" }
  - { name: "FUZZ/INPUT", type: knob, value: "5:00 (100%)" }
  - { name: "BUFFER", type: switch, value: "OFF (flip ON for more top end)", options: ["ON", "OFF"] }
---

# Premier Guitar reference — fuzz at 100%, ride the volume

## Concept
The textbook silicon-Fuzz-Face setup — fuzz cranked all the way, then do ALL dynamics with the guitar volume pot: clean-to-filthy from one knob. BUFFER OFF gives the "rich, darker, fuller" base voice the reviewer used; flip BUFFER ON if you need top end back. This is a reviewer's reference (Charles Saufley, Premier Guitar — Strat + '68 Bassman), cited as such — **NOT** an artist attribution.

## How to play it
1. OUTPUT/VOLUME 100% (5 o'clock), FUZZ/INPUT 100% (5 o'clock).
2. BUFFER OFF for the rich/darker/fuller base voice (flip ON for top end).
3. Do every dynamic move with the guitar's volume pot — roll down for near-clean, up for filth.

## Notes
- **RIG CAVEAT** — the guitar-volume cleanup that makes this patch work is **unavailable** from the GK-5→VG-800→Colour Box path (no passive pot in the loop; a buffer decouples the trick). To get it, plug a **passive SG or MIJ Jazzmaster into the FRONT of Board 1**, ahead of all buffers.
- Saufley also "doubled down with guitar tone attenuation" to darken; in-rig, do that darkening with the Hizumitas / VG-800 cab instead.
- This is a reviewer reference rig, **not** an artist credit — the silicon BC108 circuit is the Hendrix/Gilmour-era voice, but that's attributed to the circuit, never to this box.

## Sources
- Premier Guitar — Quick Hit MXR Classic 108 review, Charles Saufley (2018-06-21) — `research/links/settings-premierguitar-108-review.md` (https://www.premierguitar.com/gear/quick-hit-mxr-classic-108-fuzz-mini-review)
- Ref: Premier Guitar's test rig — Strat + '68 Bassman (reviewer reference, not an artist)
- Transformed from Pedalxly 108-Fuzz-Patches.md (community)
