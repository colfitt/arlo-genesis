# UAFX Del-Verb — Per-Model Controls, Footswitch Modes & Trails

Settings-facet reference (knob behavior + footswitch/trails). For the **MIDI CC map, snapshot workflow, and UAFX 2.0 connection details**, see Agent 2's dedicated files: `midi-official-manual-cc-chart.md`, `midi-ua-unlock-usb-midi.md`, `midi-morningstar-forum-delverb-implementation.md`, `midi-soundonsound-uafx20-review.md`. This file only summarizes the MIDI bits that bear directly on *settings recall* and avoids duplicating the CC table.

Sources: [Del-Verb manual](https://help.uaudio.com/hc/en-us/articles/13621234251284-UAFX-Del-Verb-Ambience-Companion-Manual) (control-detail tables, from the bundled PDF), and the captured demo transcripts.

## Per-model control behavior (from manual control-detail tables)

| Mode | Delay Time | Pitch w/ time? | Feedback | Color | Mod (bipolar; noon = off) |
|---|---|---|---|---|---|
| **Tape EP-III** | 80–700 ms | **Yes** | self-oscillates past ~3 o'clock | tape **record level** (noon = unity; past noon = drive on repeats) | **New tape (left) ↔ Worn tape (right)** |
| **Analog DMM** | 110–1068 ms | **Yes** | self-oscillates past ~3 o'clock | **input gain** (noon = hardware unity; past noon = overdrive + harmonics) | **Vibrato (left) / Chorus (right)** |
| **Precision** | 120–1500 ms | **No** (except "glide" voicings) | repeats *indefinitely* at max but does **NOT** self-oscillate | **tone** (left = cut treble, right = add treble, noon = flat) | **Flanger (left) / Chorus (right)** |

- **Reverb side:** single **Reverb** knob = wet mix (full CCW = no reverb; full CW = 100% wet / **kill dry**). 3-way toggle = Spring '65 / Plate 140 / Hall 224. **No decay/tone/pre-delay/dwell on hardware — those are voicing-only** (see `voicing-list-official.md`).
- **Mix knob (delay):** full CW = 100% wet / kill dry.
- **Self-oscillation / runaway:** survives bypass (runs in background in Trails Off; keeps playing in Trails On). To kill: drop Feedback to minimum.

## Footswitch modes (set in UAFX Control app)
| Mode | Left FS | Right FS | Notes |
|---|---|---|---|
| **Delay \| Reverb** *(factory default)* | toggle Delay on/off | toggle Reverb on/off | No tap tempo. LED lit = effect active. |
| **Effects \| Tap Tempo** | toggle BOTH delay+reverb | tap quarter-note tempo (tap 2+×) | Right LED blinks at tempo. |
| **Delay \| Tap Tempo** | toggle Delay on/off | tap tempo | **Reverb always on**, leveled by the Reverb knob. |

> **Known design gripe (Guitar Bonedo, Matheus Barros, Thomann all flag it):** you **cannot have a dedicated tap-tempo switch AND independent reverb on/off at the same time.** No "hold for tap" option exists. For this rig's travel use, **Delay | Tap Tempo** is usually the right pick (reverb runs as an always-on wash, left foot toggles delay, right foot taps).

## Trails (app-selectable)
- **Trails Off:** delay+reverb stop immediately on bypass. *(In Delay|Reverb mode, switching off one effect in Trails Off does NOT stop the other from ringing out.)*
- **Trails On:** tails ring out naturally after bypass.
- Input is **always analog dry-through**; output is **always buffered**, both modes.

## MIDI, only as it affects settings recall (full detail in Agent 2's midi-* files)
- Del-Verb = **CC only, no Program Change** → no pedal-side preset recall; a "snapshot" is a CC bundle living in the controller.
- **Send order: bypass → effect-select (CC14 delay / CC15 reverb) → all other params**, ~50 ms apart. Changing the effect-select CC reverts the pedal to its physical knob positions, so every parameter CC must be re-sent *after* the select. (This is why a recalled sound needs the full CC stack each time.)
- Connection: pedal is a **USB device** over USB-C (no DIN); needs a controller with a **USB host port** (e.g. Morningstar MC-Pro) connecting **directly, no computer**, or a computer/DAW, or a DIN controller via a USB-MIDI host converter.
- Voicing assignments are **stored in the pedal** (Thomann) and ride with the type select — so pre-load 6 voicings in-app and the CC recall reproduces the full sound phone-free.
