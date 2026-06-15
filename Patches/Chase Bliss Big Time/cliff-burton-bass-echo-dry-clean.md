---
type: patch
title: Cliff Burton Bass Echo (DRY CLEAN)
device: Chase Bliss Big Time
date: 2026-06-15
description: "DOUG-designed bass / Bass VI delay terminator built around DRY CLEAN — the analog dry-thru bypasses Big Time's input preamp so a sustaining Hizumitas bass fuzz turns into slow compressed stereo echoes while the clean bass fundamental stays tight and uncolored underneath. Directional choices sourced from Big-Time-DeepResearch.md (DRY CLEAN for bass-forward material, TILT up to cut bass mud, Compressed under sustain); numeric faders are a dialable recipe."
tags: [bass, bass-vi, delay, dry-clean, compressed, fuzz-wall, stereo, designed, signature]
dips:
  DRY CLEAN: "ON (Options menu — dry bypasses preamp, clean bass fundamental)"
  DRY KILL: "OFF (use ON only for wet-only out with the dry coming off the amp)"
controls:
  - { name: "Input routing", type: knob, value: "Hizumitas (mono) -> IN-L, which auto-engages MISO (mono-in/stereo-out)" }
  - { name: "MODE", type: switch, value: "Long", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (safe self-osc state — holds the sustaining bass fuzz together)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm or Analog (flatters the dark bass tone)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off (or very subtle Sine)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "DRY CLEAN", type: switch, value: "ON (Options menu — tap both footswitches; dry bypasses the preamp so the bass fundamental stays clean)", options: ["off", "on"] }
  - { name: "DRY KILL", type: switch, value: "OFF (ON instead = wet-only out, dry coming off the amp)", options: ["off", "on"] }
  - { name: "0.5X", type: switch, value: "OFF", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "~30-40% (recipe — fuzz already saturates; bring up only until repeats just thicken, no further)" }
  - { name: "TIME", type: knob, value: "long, by feel (recipe — no clock; sustained not rhythmic)" }
  - { name: "CLUSTER", type: knob, value: "low-mid ~30% (recipe)" }
  - { name: "TILT EQ", type: knob, value: "pushed UP — cut low mud from the repeats (noon = no effect; up cuts lows)" }
  - { name: "FEEDBACK", type: knob, value: "~55-60% (recipe — slow stacked echoes, below runaway)" }
  - { name: "WET", type: knob, value: "~40-45% (recipe)" }
  - { name: "SPREAD", type: switch, value: "widen (stereo space)", options: ["off", "widen", "ping-pong"] }
  - { name: "MODE button (hold)", type: button, value: "Panic reset -> clean delay if anything runs away" }
---

# Cliff Burton Bass Echo (DRY CLEAN)

## Concept
A bass / Bass VI delay built around DRY CLEAN: the analog dry-thru bypasses Big Time's input preamp so the clean bass fundamental stays tight while only the wet repeats saturate. Fed by a sustaining Hizumitas bass fuzz (the 'Cliff Burton vibes' voice), it turns a held low note into slow, compressed stereo echoes that thicken the low end without muddying the root. Compressed STATE holds the sustaining fuzz together (no runaway); TILT pushed UP cuts the low-mud out of the repeats; COLOR stays modest because the fuzz already supplies the saturation.

## How to play it
1. Run Hizumitas (mono) -> IN-L, which auto-engages MISO (mono-in/stereo-out).
2. Tap both footswitches to open the Options menu and turn DRY CLEAN ON so the dry bass fundamental bypasses the preamp.
3. Set MODE Long, STATE Compressed, VOICING Warm/Analog; TILT pushed UP to cut low mud from the repeats.
4. Hold a sustained low note and let the compressed echoes stack into stereo space.
5. Bring COLOR up only until the repeats just begin to thicken — no further (too much COLOR + a hot fuzz clamps the limiter to porridge).
6. Dig in vs. play gently to ride the dynamics: the clean fundamental stays put while the wet wall swells around it.
7. Hold MODE (2s) to panic-reset to a clean delay if anything runs away.

## Notes
- DRY CLEAN is the whole point: it removes COLOR/preamp from the DRY path only, so the wet repeats stay gained-up/saturated while the dry bass stays clean and tight — the documented bass-forward Big Time move.
- TILT push UP cuts lows (noon = no effect; push down cuts highs); on round bass content this stops saturated repeats from piling on low-mid mud.
- Compressed STATE is the 'safe' self-oscillation state — it holds itself together, ideal under a sustaining fuzz; swap to Saturated for a grittier, less-controlled repeat.
- Keep COLOR modest — too much COLOR + a hot fuzz makes the limiter clamp 'to porridge'.
- For a pure wet echo bed with the dry coming straight off the amp, use DRY KILL (wet-only out) instead of DRY CLEAN.
- HONESTY: COLOR / CLUSTER / FEEDBACK / WET / TIME are a dialable recipe — no published source documents Big Time on bass with these exact faders. Only the directional/behavioral choices (DRY CLEAN keeps the bass fundamental clean, TILT up cuts bass mud, Compressed holds sustain, COLOR modest under fuzz) are sourced; dial the faders by ear.

## Sources
- 🟣 DOUG-designed integration. Directional/behavioral choices sourced from `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` §"Bass (Jazz bass) / SG / Jazzmaster" (line 78): *"DRY CLEAN (dry bypasses preamp) keeps a clean bass fundamental while only the repeats saturate — useful if Big Time is ever used on bass-forward material."*
- `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` §2 Options menu (line 36): DRY CLEAN = dry bypasses the preamp (tap both footswitches, manual p.40); §3 (line 21): TILT EQ push up to cut lows; §6 (line 75): TILT up to "cut the mud from your bass" (manual p.39).
- `gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A: COLOR-modest under sustaining fuzz, STATE Compressed under sustain, MISO auto-engage on IN-L.
- Upstream source this patch is designed to receive: `Patches/EarthQuaker Devices Hizumitas/cliff-burton-bass-fuzz.md` (the bass-fuzz voice).
- Numeric fader positions are a designed recipe with no published values for a Big Time bass patch — dial by ear.
