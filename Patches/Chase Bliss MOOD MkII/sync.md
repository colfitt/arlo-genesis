---
type: patch
title: SYNC (in-time captures, clock-lockable)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: Tie one channel's timing to the other for in-time captures, clock-lockable to MIDI (Big Time / Blooper / Digitakt) — a hidden option set via the Wet MODE toggle.
tags: [hidden, sync, midi-clock, looper, rig-integration, factory, signature]
hidden:
  SYNC (Wet MODE toggle): LEFT = Micro-Looper synced to Wet (loop length set by Wet TIME) · MIDDLE = unsynced · RIGHT = Wet synced to Micro-Looper (Wet TIME steps in rhythmic relation to the loop)
controls:
  - { name: "LEFT + RIGHT footswitches (hidden access)", type: button, value: "HOLD both (LEDs green), then move the Wet MODE toggle" }
  - { name: "MIDI clock (CC51 follow / CC53 div wet / CC54 div loop)", type: switch, value: "feed clock to lock to Big Time / Blooper / Digitakt" }
---

# SYNC (in-time captures, clock-lockable)

## Concept
Tying one channel's timing to the other; capturing rhythmic ideas in time, then committing downstream (Blooper). A hidden option: hold **both footswitches** (LEDs green), then move the **Wet MODE toggle**. **LEFT** = Micro-Looper synced to Wet (loop length set by Wet TIME — great for in-time capture). **MIDDLE** = unsynced. **RIGHT** = Wet synced to Micro-Looper (Wet TIME steps in rhythmic relation to the loop). Combine with MIDI clock to lock to Big Time / Blooper / Digitakt.

## How to play it
1. **Hold both footswitches** until the LEDs go green (hidden-options mode).
2. Move the **Wet MODE toggle**: LEFT = loop follows Wet, MIDDLE = unsynced, RIGHT = Wet follows the loop.
3. For external lock, feed MIDI clock from the rig master (send CC51>0 to follow; CC53 = wet division, CC54 = loop division).
4. Capture in time, then commit downstream to Blooper.

## Notes
- ⚠️ MIDI clock is **ignored in Synth Mode**, and a stray MIDI Note auto-engages Synth Mode — watch this when the Digitakt sequences it (CC51 clock-follow, CC53/CC54 divisions).

## Sources
- manual p.17; chasebliss-mood-mkii-video-manual-pt2.md; MOOD-MkII-UsageGuide.md §5
- Transformed from Pedalxly MOOD-MkII-Patches.md (factory)
