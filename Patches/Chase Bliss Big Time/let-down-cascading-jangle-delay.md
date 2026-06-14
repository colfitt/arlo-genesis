---
type: patch
title: "Let Down" Cascading Jangle-Delay
device: Chase Bliss Big Time
date: 2026-06-14
description: Track-B emulation of Radiohead's "Let Down" (OK Computer) — one banjo/guitar arpeggio line becomes a shimmering multi-tap cascade faking the doubled-octave, 5/4-vs-4/4 Steve Reich Spector wall.
tags: [taste-profile, radiohead, jangle, cascade, multi-tap, designed, signature]
hidden:
  CC54 subdivision: "dotted-8th vs the song's 4/4 (or a 5-against-4 tap to fake the 5/4 Reich phasing)"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27" }
  - { name: "MODE", type: switch, value: "Short", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (keeps the dense cascade articulate, Spector-wall glue without mush)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi (or Focus) — keep the jangle bright and chimey", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine subtle (gentle tape-style shimmer on the layers)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "0.5X", type: switch, value: "OFF (this one stays clean/bright)", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "~30–35% (modest after Gen Loss — bright repeats, not saturated)" }
  - { name: "TIME", type: knob, value: "dotted-8th vs 4/4 (or 5-against-4 tap for the 5/4 Reich phasing)" }
  - { name: "CLUSTER", type: knob, value: "~45–55% (multi-tap = the doubled/tripled arpeggio layers from one line)" }
  - { name: "TILT EQ", type: knob, value: "above noon (cut mud, keep the chime)" }
  - { name: "FEEDBACK", type: knob, value: "~40% (cascade rings on, doesn't wash out)" }
  - { name: "WET", type: knob, value: "~40%" }
  - { name: "TEXTURE", type: knob, value: "low (alt — clean)" }
  - { name: "DIFFUSE", type: knob, value: "low-mid (alt — a little air)" }
  - { name: "RATE", type: knob, value: "subtle (alt under TIME)" }
  - { name: "DEPTH", type: knob, value: "subtle (alt under CLUSTER)" }
  - { name: "SPREAD", type: switch, value: "ping-pong (the L/R doubling that reads as stacked-layer width)", options: ["off", "widen", "ping-pong"] }
---

# "Let Down" Cascading Jangle-Delay

## Concept
Track-B emulation of the OK Computer marquee — Jonny's cascading arpeggio doubled an octave up plus a third Jazzmaster layer into a Phil-Spector wall. One banjo/guitar arpeggio line feeds a shimmering multi-tap cascade. Compressed keeps the dense cascade articulate (Spector-wall glue without mush); HiFi/bright keeps the jangle chimey — the opposite of the lo-fi patches. **Designed-to-emulate** — no Big Time artist setting is documented, and Radiohead never used a Big Time.

## How to play it
1. Feed a single banjo arpeggio (GK-5 → VG-800); the taps build the octave-stack illusion.
2. Set TIME to **dotted-8th vs the 4/4**, or a **5-against-4 tap** to fake the 5/4 Reich phasing — the taps deliberately don't line up with the pulse.
3. Clock-lock to DT2/MPC via CC54 for the grid.
4. For the real doubled-octave layer, print an octave-up copy on Blooper (see Blooper TB2) and run both into this.
5. Run into a long hall (H90/Big Sky) = the St Catherine's ballroom.

## Notes
- The 5-against-4 tap is the trick that gives "two clocks that refuse to agree."
- HiFi/bright is intentional — this is the one patch that resists the degrade tie-breaker because the *jangle* is the hook.
- Numeric fader positions are designed starting points; on recall the flying faders override these.

## Sources
- 🟣 designed from `Research/Taste-Profile/sources/poeticwax-let-down-wall-of-sound.md` (doubled-octave + 3-layer + 5-vs-4 phasing) + manual control reference (SPREAD ping-pong, CC54 subdivision, Compressed state for dense-mix articulation).
- Ref: Radiohead — "Let Down" (OK Computer, 1997): doubled/tripled cascading arpeggios, 5/4-vs-4/4 Steve Reich phasing, Spector wall.
- Transformed from Pedalxly Big-Time-Patches.md (designed)
