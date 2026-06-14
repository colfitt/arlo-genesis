---
type: patch
title: Phrase-Sample Tempo-Locked Grains (hidden move)
device: Walrus Audio QI Etherealizer
date: 2026-06-14
description: Lock grain repeats to the delay/tempo for tempo-married glitch on a MIDI-clocked board — the official hidden building block where X-min syncs Phrase Sample to Delay time.
tags: [granular, hidden, tempo-sync, glitch, designed, signature]
hidden:
  X-min Phrase Sample sync: X knob fully minimum locks Phrase Sample to Delay time
controls:
  - { name: "Grain mode", type: switch, value: "Phrase Sample", options: ["Grain Cloud", "Phrase Sample"] }
  - { name: "Time", type: knob, value: "set to BPM / tap tempo" }
  - { name: "X", type: knob, value: "fully MINIMUM (syncs to Delay time)" }
  - { name: "Slot/Bank", type: knob, value: "Building block (apply over any grain patch)" }
---

# Phrase-Sample Tempo-Locked Grains (hidden move)

## Concept
Lock grain repeats to the delay/tempo for tempo-married glitch on a MIDI-clocked board. With grain in **Phrase Sample** and the **X knob fully minimum**, Phrase Sample syncs to the Delay time — rhythmically locked grains. Increasing X de-syncs the repetitions and it becomes chaotic.

## How to play it
1. Set grain mode to **Phrase Sample**.
2. Set Delay **Time** / tap tempo to your BPM.
3. Turn the **X knob fully MINIMUM** = Phrase Sample syncs to the Delay time.
4. Increase X to de-sync the repetitions (becomes chaotic).
5. MIDI-clock the Qi so Delay + Phrase Sample lock to the rest of the rig.

## Notes
- Official hidden building block, verified across multiple sources; the Reverb official demo confirms X-min sync.
- This is the engine that overlaps the Microcosm — use sparingly so they don't compete.

## Sources
- designed from walrus-marketing-patch-descriptions.md + dkdivedude-hands-on-blog.md + russo-music-routing-midi-clock.md + transcripts/mad-steex; reverb-official-demo confirms X-min sync
- Transformed from Pedalxly QI-Etherealizer-Patches.md (designed)
