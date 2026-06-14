---
type: patch
title: Banjo-as-Lead Clean
device: UAFX Del-Verb
date: 2026-06-14
description: An articulate, un-smeared lead voice for banjo (Gold Tone GK-5 → VG-800) — a warm 140 Plate (or long-predelay "Lush Recall") rounds the attack while a short Precision slap keeps fast rolls clear. Sufjan-style fingerpicked banjo bed.
tags: [clean, lead, banjo, plate, articulate, indie-folk, designed, signature]
controls:
  - { name: "Reverb Model", type: switch, value: "Plate 140", options: ["Spring '65", "Plate 140", "Hall 224"] }
  - { name: "Reverb voicing (app-assigned)", type: switch, value: "Studio standard Plate A (~3.0 ms, warm, rounds attack) OR Lush Recall (140 Plate A, short decay + 250 ms pre-delay)" }
  - { name: "Reverb", type: knob, value: "10:00–11:00" }
  - { name: "Delay Model", type: switch, value: "Precision", options: ["Tape EP-III", "Analog DMM", "Precision"] }
  - { name: "Delay voicing (app-assigned)", type: switch, value: "Default Precision (clean, pitch-stable)" }
  - { name: "Delay Time", type: knob, value: "≈120–180 ms (slap)" }
  - { name: "Feedback", type: knob, value: "minimum" }
  - { name: "Mix", type: knob, value: "≈9:00" }
  - { name: "Color", type: knob, value: "slight right (Precision tone +treble for clarity)" }
  - { name: "Mod", type: knob, value: "noon (off)" }
  - { name: "Trails", type: switch, value: "ON", options: ["ON", "OFF"] }
---

# Banjo-as-Lead Clean

## Concept
Banjo is bright and transient-dense, so the goal is ambience that flatters without smearing. A warm 140 Plate rounds the pluck attack (no spring ice-pick), and a clean, pitch-stable Precision slap keeps fast rolls articulate where Tape or DMM would smear them. "Lush Recall" with its 250 ms pre-delay is the secret weapon: the dry pluck speaks first, *then* the plate blooms behind it.

## How to play it
1. Pre-assign in the app: Reverb toggle "Studio standard Plate A" (or "Lush Recall") on Plate 140, Delay toggle "Default Precision" on Precision.
2. Keep Feedback at minimum and Time short (≈120–180 ms) for a single supportive slap.
3. Play fingerpicked rolls — the plate rounds the attack while the slap doubles it cleanly.
4. For maximum lead clarity, switch the reverb voicing to "Lush Recall" so the dry pluck speaks before the bloom.

## Notes
- **AVOID Spring '65 on banjo** — it adds 2–4 kHz splash / ice-pick to an already bright source.
- The "Lush Recall" 250 ms pre-delay is the key trick for lead clarity.
- Color is nudged right for treble clarity (Precision Color = tone); keep Mix low (≈9) so it stays a lead, not a wash.

## Sources
- designed from UsageGuide §3/§6 (Plate flatters banjo, Spring ice-picks it) + UA Preset & Voicing Lists ("Lush Recall," "Studio standard Plate A") + DeepResearch §6 — `research/links/tips-anatomyoftone-gig-workflow.md`, `research/links/voicings-new-names-uasupport.md`, `research/links/settings-midi-and-controls.md`
- Ref: Banjo-as-lead aesthetic; indie-folk (Sufjan-style fingerpicked banjo bed)
- Transformed from Pedalxly Del-Verb-Patches.md (DOUG-designed)
