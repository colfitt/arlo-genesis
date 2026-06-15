---
type: patch
title: Half-Time Drop Delay (Clean Base + AUX 0.5X)
device: Chase Bliss Big Time
date: 2026-06-15
description: "DOUG-designed performance delay — a clean modulated stereo delay that collapses to a half-rate, pitch-dropped lo-fi delay on a live AUX footswitch. Built around the documented AUX 'Fun mode' 0.5X half-time-drop hardware feature; the inverse of factory #7 Crushed Analog (which bakes 0.5X permanently ON)."
tags: [delay, clean, lo-fi, half-time, 0.5x, aux, performance, modulated, designed]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot — saved state keeps 0.5X OFF; the drop lives on the AUX switch" }
  - { name: "MODE", type: switch, value: "Long (736 ms–12.2 s; ~24 s with 0.5X — room for the drop to double the time)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Digital (limiter fully out of the way — clean, stable repeats; lo-fi comes from the drop, not baked-in saturation)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi (or Focus for a touch of body) — open/clean in the up-state so the collapse to lo-fi is dramatic", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (subtle) — the 'clean modulated' shimmer", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "0.5X", type: switch, value: "OFF in the saved patch — it lives on the AUX switch (the performance)", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "low ~25–30%" }
  - { name: "TIME", type: knob, value: "tapped / MIDI clock (push longer before dropping for a deeper sag)" }
  - { name: "CLUSTER", type: knob, value: "0" }
  - { name: "TILT EQ", type: knob, value: "noon" }
  - { name: "FEEDBACK", type: knob, value: "~35–45% (tidy 2–4 repeats, not a wall; pull this down first if the dropped state clutters)" }
  - { name: "WET", type: knob, value: "~40–45%" }
  - { name: "SPREAD", type: switch, value: "widen (subtle) for stereo", options: ["off", "widen", "ping-pong"] }
  - { name: "AUX-in floor footswitch", type: switch, value: "LEFT = 0.5X half-time drop (the performance), RIGHT = clear buffer" }
  - { name: "MODE button (hold)", type: button, value: "Panic reset → clean simple delay (≈ Factory #0) if a half-time tail runs away" }
---

# Half-Time Drop Delay (Clean Base + AUX 0.5X)

## Concept
A clean, gently modulated stereo delay whose entire character lives on a single live gesture: an external AUX floor footswitch wired to Big Time's 'Fun mode' LEFT = 0.5X half-time drop. In the up-state it's a tidy, full-bandwidth Digital-STATE delay with subtle Sine modulation. Stomp the AUX LEFT switch and the engine drops to half sample rate in real time -- bandwidth halves, delay time doubles, the running buffer pitches/sags down, and Big Time's built-in 12-bit reduction kicks in. The clean delay and the crushed half-time delay are the SAME patch; only the AUX switch changes. 0.5X is deliberately left OFF in the saved state so there is a real drop to perform -- the opposite design choice to factory #7 'Crushed Analog' (which bakes 0.5X permanently ON).

## How to play it
1. Save the clean version: MODE Long, STATE Digital, VOICING HiFi/Focus, MOTION Sine subtle, 0.5X OFF, COLOR ~25–30%, FEEDBACK ~35–45%, TILT noon. This is the up-state -- a tidy modulated stereo delay.
2. Plug an external AUX floor footswitch into Big Time's AUX-in jack. LEFT = 0.5X half-time drop; RIGHT = clear buffer.
3. Tap TIME (or slave MIDI clock) for steady repeats. Push TIME longer before you intend to drop -- the 0.5X doubling will stretch it further.
4. Perform the drop: stomp AUX LEFT mid-phrase. The engine halves its sample rate live -- bandwidth halves, delay time doubles, the buffer sags down in pitch, 12-bit crush engages. Hold the dropped state through the section.
5. Stomp AUX LEFT again to snap back up to the clean delay. Use AUX RIGHT to clear a long sagging tail that won't get out of the way.
6. Hold the center MODE button as a panic-reset to a clean simple delay if a half-time tail runs away.

## Notes
- Keep STATE Digital and COLOR low in the up-state on purpose -- if you bake in Saturated + 0.5X (the 'Crushed Analog' approach), there is no drop left to perform. The contrast IS the patch.
- 0.5X stays OFF in the saved state and lives entirely on the AUX switch. This is the key difference from factory #7 Crushed Analog (0.5X baked ON).
- Because Digital STATE = no limiter, watch level into your interface when dropped to 0.5X -- doubled-time repeats can pile up. Pull FEEDBACK down before COLOR if it clutters.
- Flip DRY KILL ON in Options if you want the wet kept out of the printed dry for a parallel/aux send; otherwise the dry-retained series path is the intended sound.
- MISO: mono-in to IN-L auto-engages mono-in/stereo-out.
- 🟣 HONESTY: all numeric fader/knob positions above are a **dialable recipe**, not factory-published — Chase Bliss publishes character, not numbers, and on preset recall the motorized faders override anything written here. The AUX Fun-mode 0.5X half-time-drop behavior itself is a sourced hardware feature, not invented.

## Sources
- 🟢 AUX-in 'Fun mode': LEFT = 0.5X half-time drop, RIGHT = clear buffer — `research/Big-Time-UsageGuide.md` §"AUX-in" (video / modwiggler).
- 🟢 0.5X = halve sample rate (doubles max delay time → ~24 s in Long) + 12-bit reduction (built-in generation-loss) — `research/Big-Time-UsageGuide.md` §0.5X (superbooth-snyder, video).
- 🟢 MODE ranges (Long 736 ms–12.2 s), Digital STATE = no limiter/clean, VOICING filter slopes (HiFi flat / Focus gentle bandpass) — `research/Big-Time-UsageGuide.md` §MODES/STATE/VOICING.
- 🟢 Hold MODE = instant clean reset — `research/Big-Time-UsageGuide.md` §Reset/panic (centerpiece).
- 🟣 DOUG-designed patch built around the documented Big Time AUX 'Fun mode' 0.5X half-time-drop hardware feature. Mechanics (0.5X, modes, Digital STATE, AUX behavior) are sourced; numeric fader positions are a dialable interpretation, not factory-published.
