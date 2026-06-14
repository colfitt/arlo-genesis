---
type: patch
title: Slow-ambient drone setup (tempo + tape down, long env, Hold)
device: TE OP-1 Field
date: 2026-06-14
description: A performance setup for long sustained ambient drone beds — tempo and tape speed down, long attack/release envelope, and the Hold sequencer latching a low note while you solo the banjo above it.
tags: [drone, ambient, sustained, performance-setup, hold-sequencer, community, signature]
hidden:
  Tempo (Blue knob, metronome page): way down
  Tape speed (White knob, metronome page): down
controls:
  - { name: "Engine", type: switch, value: "any synth with long attack + long release", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "T2 Attack", type: knob, value: "long" }
  - { name: "T2 Release", type: knob, value: "long" }
  - { name: "Sequencer", type: switch, value: "Hold", options: ["Pattern","Tombola","Endless","Finger","Sketch","Arpeggio","Hold"] }
  - { name: "Hold BLUE (break point)", type: knob, value: "set break point" }
  - { name: "Hold GRAY (transpose in key)", type: knob, value: "as needed" }
  - { name: "Hold GOLD (poly/mono)", type: switch, value: "poly or mono", options: ["poly","mono"] }
---

# Slow-ambient drone setup (tempo + tape down, long env, Hold)

## Concept

A performance setup for long sustained ambient drone beds — aimed straight at the drone/doom/sustained-wall aesthetic. Pull tempo and tape speed down, give the synth a long attack + long release, then latch a low note with the Hold sequencer and solo the banjo above the held drone. This is the canonical "banjo-as-lead over a latched drone" move.

## How to play it

1. On the **metronome page**, pull **Tempo** down (Blue knob) and **tape speed** down (White knob).
2. Pick any synth with a **long ATTACK + long RELEASE** (T2 envelope).
3. Switch the sequencer to **Hold**: BLUE sets the break point, latch a low note as a drone.
4. GRAY transposes in key; GOLD toggles poly/mono.
5. Solo the banjo (or a lead voice) above the held drone.

## Notes

- This is a performance setup, not a single saved patch — pair it with any drone patch above (drone1–6, planks, cluster_pad).
- Concrete control map is on disk; envelope values are qualitative ("long").

## Sources

- Gear/TE OP-1 Field/research/links/github-ratbag98-op1tips-distilled.md + transcripts/adg-op1-field-full-walkthrough-for-owners.md + UsageGuide §1/§5
- Transformed from Pedalxly OP-1-Field-Patches.md (community)
