---
type: patch
title: Ondes-Martenot Lead Delay
device: Chase Bliss Big Time
date: 2026-06-14
description: Track-B emulation of Jonny's Ondes-Martenot lead voice (Kid A) translated to banjo-as-lead — a gliding, swelling, singing single-note line over clean sustaining, ducking repeats.
tags: [taste-profile, radiohead, lead, banjo, vocal, compressed, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27" }
  - { name: "MODE", type: switch, value: "Long (long musical trails behind the lead)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (sagging trails that react to playing — duck under attack, bloom after)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Focus (defined, vocal-like)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine slow + shallow (vibrato/shimmer on the tails, the Ondes' bowed swell)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "0.5X", type: switch, value: "OFF", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "~35%" }
  - { name: "TIME", type: knob, value: "long (musical, dotted or quarter)" }
  - { name: "CLUSTER", type: knob, value: "low (~15% — clean single repeats, the line is the melody)" }
  - { name: "TILT EQ", type: knob, value: "noon → up (keep the lead present)" }
  - { name: "FEEDBACK", type: knob, value: "~50% (long singing trails)" }
  - { name: "WET", type: knob, value: "~40%" }
  - { name: "TEXTURE", type: knob, value: "~50% (alt — Compressed ducking, trails get out of the way of the attack)" }
  - { name: "DIFFUSE", type: knob, value: "low (alt under FEEDBACK)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
---

# Ondes-Martenot Lead Delay

## Concept
Track-B emulation of Jonny's Ondes-Martenot lead voice (Kid A: "How to Disappear Completely," "The National Anthem") translated to the banjo-as-lead — a gliding, swelling, singing single-note line over clean sustaining repeats. The Ondes is monophonic and voice-like, so CLUSTER stays low and the Compressed trails breathe around a single line, ducking under the attack and blooming after. **Designed-to-emulate** — no Big Time artist setting is documented, and Radiohead never used a Big Time.

## How to play it
1. Keep CLUSTER low (~15%) — clean single repeats; the *line* is the melody.
2. Pair with **CB Clean's Dynamic Volume Swell** so the banjo pluck swells in like the Ondes' intensity key.
3. Add portamento/glide on the VG-800 for the ribbon-glide character.
4. Let the long Compressed trails duck under the attack and bloom in the gaps.

## Notes
- The glide + swell come from upstream (VG-800 portamento + Clean swell); Big Time supplies the long, ducking, singing tail.
- MOTION Sine slow + shallow adds the vibrato/shimmer evoking the Ondes' bowed swell.
- Numeric fader positions are designed starting points; on recall the flying faders override these.

## Sources
- 🟣 designed from `Research/Taste-Profile/sources/kingofgear-radiohead-synths-ondes.md` (ribbon glide + intensity-key swell, "like singing") + Factory #3 Sagging Echoes character (Compressed ducking trails).
- Ref: Radiohead — Ondes Martenot leads on "How to Disappear Completely" & "The National Anthem" (Kid A, 2000): gliding, swelling, vocal-like monophonic lead.
- Transformed from Pedalxly Big-Time-Patches.md (designed)
