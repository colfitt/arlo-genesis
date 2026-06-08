https://www.eventideaudio.com/forums/topic/h90-freeze-a-sound/
Eventide official forum · tbskoglund + Brock (Eventide staff) · Feb 2023 – May 2024

# Freezing a sound on the H90 — the drone/pad-hold reference

The single most important capability for this rig's "lock a wall and play over it" goal. Which algorithms freeze, and how:

## Algorithms with a Freeze/Infinite
- **Blackhole** — Freeze happens with **Feedback turned fully clockwise**. Brock: *"It's still in there. In BlackHole, Freeze happens with Feedback turned all the way clockwise."* Note the nuance: *"There's still a 'sweet spot' to hit between Freeze & Infinite. Sometimes, it doesn't behave like it should."* (i.e. Infinite = infinite tail still accepting input; full-CW = locked Freeze; the transition zone can be finicky — dial carefully.)
- **Polyphony** and **Prism Shift** — both have a dedicated **Freeze Performance Parameter**. tbskoglund: *"Yes, 2 of the new algorithms Polyphony and Prism Shift have a freeze performance parameter."*
- **Prism Shift caveat:** *"The High and Low voices will freeze, the Mid voice does not."* (Brock, Apr 17 2024) — so a frozen Prism Shift pad keeps the mid voice live/playable.
- **Shimmer** — has Pitch Freeze and Pitch+verb Freeze modes (per the dossier/algorithm guide).

## Mapping Freeze
- Assign Freeze as a **Performance Parameter to a footswitch** in Perform mode — **latching OR momentary (M)** via aux switch or MIDI CC (tbskoglund, May 23 2024).
- Because Freeze is a Performance Parameter, it **persists independently of HotSwitch toggles** (see the HotSwitch mutual-exclusivity file) — you can freeze a wall and still flip HotSwitches under it.

## Playing over a frozen pad
- Serial routing lets you process the sustained/frozen signal further; you can also insert-loop external gear to treat the frozen pad.

## Rig relevance
This is the core drone move: feed a sustained Hizumitas/baritone chord into **Blackhole (Feedback full CW = Freeze)** or **Shimmer (Pitch+verb Freeze)** or **Polyphony (Freeze)**, lock it as an infinite pad via a momentary/latching footswitch, and play the banjo/baritone over the top. Map Freeze to an aux switch so the player triggers it hands-free. For a frozen-but-still-playable harmonized pad, use **Prism Shift** (High/Low freeze, Mid voice stays live).
