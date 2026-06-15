---
type: patch
title: Chaos Catcher (Reverb-Stretch Capture)
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "DOUG-designed catch-and-resolve stage for the lost-found-random-event-mood-capture chain — sits downstream of a constantly-mutating source (Lost & Found random-rolled via CC114) and smears each pass into a coherent, blooming, freezable reverb-tail bed. Mode/behavior character sourced from existing MOOD patch sheets + manual; clock-face knob positions are an unpublished dialable recipe."
tags: [reverb, stretch, granular, capture, freeze, drone, ambient, designed, signature]
dips:
  LATCH: on (freeze holds hands-free — no need to keep your foot down)
  TRAILS: on (toggling the effect mid-performance won't drop the captured wash)
controls:
  - { name: "Wet MODE", type: switch, value: "Reverb (long/blooming) — the catch-and-smooth stage", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Looper MODE", type: switch, value: "Stretch (grainy time-smear capture) — or Env for a more reactive, attack-carved capture", options: ["Env", "Tape", "Stretch"] }
  - { name: "CLOCK", type: knob, value: "low (recipe) — grainier swallow; dial by ear" }
  - { name: "Wet TIME", type: knob, value: "long bloom, to taste (move while frozen)" }
  - { name: "Wet MODIFY", type: knob, value: "to taste, long-tail character (move while frozen)" }
  - { name: "MIX", type: knob, value: "~noon (recipe) — captured wash sits with the dry" }
  - { name: "LEFT footswitch (Wet / freeze)", type: button, value: "HOLD to FREEZE the current bloom into an infinite bed; LATCH lets it hold hands-free" }
---

# Chaos Catcher (Reverb-Stretch Capture)

## Concept
A granular catch-and-resolve stage built to sit downstream of an unpredictable, constantly-mutating source (here the Lost & Found being random-rolled via CC114) and tail it into coherent space. The Reverb wet provides the musical landing while the Stretch (or Env) looper granulates and time-smears the incoming texture, hiding the seams between source mode-jumps. Freeze a great pass into an infinite bed on cue. The point is: unpredictable input, musical output — capture the chaos and bloom it.

## How to play it
1. Set Wet MODE = **Reverb** (long/blooming), Looper MODE = **Stretch** (or **Env** for attack-reactive capture), **CLOCK low** for a grainier swallow, **MIX ~noon**.
2. Enable **LATCH** and **TRAILS** so the freeze holds hands-free and toggling won't kill the wash.
3. Feed it the mutating source (e.g. Lost & Found random-rolled) and let the Reverb+Stretch smear each pass into a coherent tail rather than passing the chaos through raw.
4. When a combination lands that you love, **HOLD the LEFT (Wet) footswitch** to freeze the bloom into an infinite bed; let the source keep mutating underneath or kill it and play over the held capture.
5. Freeze **after** a source re-roll settles, not during the jump, or you capture a transient artifact instead of the texture.

## Notes
- Designed (DOUG) capture stage — clock-face values are dialable starting points, not published numbers.
- Stretch MODIFY at MAX outputs **no effect**; the usable capture range is MAX→noon (noon = frozen grain). Use **Env** instead if you want dynamics/attack to carve the bed.
- Keep upstream level controlled (e.g. Lost & Found GLUE) so a harsh random combo doesn't slam the MOOD input on freeze.
- Stereo in/out preserves upstream SPREAD width into the bloom; narrow at the source if you want a tighter capture.

## Sources
- Patches/Chase Bliss MOOD MkII/freeze-pad.md (LEFT-FS freeze, LATCH/TRAILS dips, move knobs while frozen)
- Patches/Chase Bliss MOOD MkII/stretching-101-frozen-grain-wall.md (Stretch capture, MODIFY MAX→noon = frozen, low CLOCK = grainier, MODIFY MAX = no effect)
- Patches/Chase Bliss MOOD MkII/reverb-stretch-sprawling-epic.md (Reverb-over-Stretch sprawling grainy bed pairing)
- Patches/Chase Bliss MOOD MkII/reverb-env-dynamic-interactive.md (Reverb + Env, attack carves the wash — alt capture mode)
- MOOD MkII manual (Wet Channel freeze; Looper modes)
- DOUG-designed integration patch (no artist source) — built for the lost-found-random-event-mood-capture chain as the MOOD's catch-and-resolve role
