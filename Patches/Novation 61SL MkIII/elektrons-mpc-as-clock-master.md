---
type: patch
title: Elektrons + MPC as Clock Master (DAW-less brain)
device: Novation 61SL MkIII
date: 2026-06-14
description: Run the room DAW-less — SL = clock master + 8-track poly sequencer driving Digitakt 2, Octatrack MkII and Akai MPC Sample at once, each on its own Part/channel/destination, one Play/Stop starts everything.
tags: [clock-master, sequencer, daw-less, elektron, mpc, community]
controls:
  - { name: "World/Mode", type: switch, value: "Standalone", options: ["Standalone", "InControl"] }
  - { name: "MIDI Clock Tx", type: switch, value: "On (24 PPQN to USB + both DINs)", options: ["On", "Off"] }
  - { name: "Part 1 (Digitakt2)", type: knob, value: "Destination DIN1, Ch1 (match DT AUTO/track channel)" }
  - { name: "Part 2 (Octatrack MkII)", type: knob, value: "Destination DIN1 or DIN2, Ch2 (match an OT track channel)" }
  - { name: "Part 3 (MPC Sample)", type: knob, value: "Destination USB or DIN2, Ch3" }
  - { name: "Templates", type: knob, value: "Load FACTORY Components templates for Octatrack and Digitakt (ship in library)" }
  - { name: "Tempo", type: knob, value: "40–240 BPM (Tempo button)" }
  - { name: "Pattern length", type: knob, value: "16-step; micro-steps (6/step) for triplet/glitch; gate to 32 for held notes" }
  - { name: "Generative Part", type: switch, value: "One Part on Random direction + 60–80% Chance; pattern-chain the others", options: ["Random+Chance", "Pattern-chain"] }
  - { name: "Mute/Solo per Part", type: button, value: "Yellow top / blue bottom soft buttons (arrange live)" }
  - { name: "Session Slot", type: knob, value: "Session slot 4" }
---

# Elektrons + MPC as Clock Master (DAW-less brain)

## Concept
Running the room DAW-less: the SL is clock master + 8-track poly sequencer driving Digitakt 2, Octatrack MkII and Akai MPC Sample at once, each on its own Part / channel / destination, with one Play/Stop starting the whole rig. Uses the factory Components templates for Octatrack and Digitakt (verified to ship) so encoders/buttons map to those boxes' known CCs out of the box.

## How to play it
1. WORLD = standalone, MIDI Clock Tx = On (24 PPQN to USB + both DINs).
2. PARTS (Shift+Sessions): Part1 → Digitakt2, Destination DIN1, Ch1 (match DT AUTO/track channel); Part2 → Octatrack MkII, Destination DIN1 or DIN2, Ch2 (match an OT track channel); Part3 → MPC Sample, Destination USB or DIN2, Ch3.
3. Load the FACTORY Components templates for Octatrack and Digitakt (they ship in the library).
4. ON EACH BOX: Clock Receive = On, Transport Receive = On.
5. TEMPO: SL Tempo button, 40–240 BPM.
6. SEQUENCING: 16-step patterns; micro-steps (6/step) for triplet/glitch runs; gate to 32 steps for held notes; one Part on Random direction + 60–80% Chance for generative motion; pattern-chain the others for structure; Mute/Solo per Part (yellow top / blue bottom soft buttons) to arrange live.
7. WHO-SEQUENCES-WHOM: decide per song — if SL sequences them, set the boxes to play incoming MIDI notes and DON'T run their internal patterns on the same tracks (double-sequence chaos).
8. EXPRESSIVE PARTS: route out the SL's 2nd DIN directly, NOT through the Digitakt (DT doesn't pass pitch-bend/mod-wheel through; Elektron seqs cap at 4 notes/step).

## Notes
- Uses factory templates (verified to ship).
- Alt master: set an Elektron or the MPC as clock source, SL Clock Rx On fed from ONE source — never Tx AND Rx at once.
- Don't double-path clock (USB+DIN).

## Sources
- research/links/int-recipe-elektrons-mpc.md + research/links/elektronauts-digitakt-sl-mk3-workflow.md + DeepResearch §13(b) + UsageGuide §9; factory OT/DT templates.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (community)
