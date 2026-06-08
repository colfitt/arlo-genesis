https://help.uaudio.com/hc/en-us/articles/13621234251284-UAFX-Del-Verb-Ambience-Companion-Manual
help.uaudio.com (OFFICIAL manual) · Universal Audio · "Updated December 22, 2025" (NEWER than the dossier's Nov 2025 ref)

# Del-Verb MIDI CC chart + official "send in this order" rule (from the manual PDF / online manual)

The dossier predates this; the manual now has a dedicated "Del-Verb MIDI CCs" section. This is the AUTHORITATIVE CC map for building snapshots.

## Official message ORDER (manual, "Sending multiple CCs")
"If you are sending multiple CCs in order to make multiple changes to a sound, send MIDI messages in the following order:"
1. **Bypass / unbypass**
2. **Effect select**
3. **All other changes**
"Sending the effect selection first allows the pedal to load the initial algorithm, then make the changes to the CCs you specify. If messages are sent out of order, the pedal may not reflect your intended changes."
→ This is the official confirmation of the Morningstar-forum "WYSIWYG" gotcha: select FIRST, parameters AFTER.

## CC map (from the manual's chart; values verified off the PDF)
| CC | Parameter | Range | Notes |
|----|-----------|-------|-------|
| 12 | FS Left | 0,1 | 1 toggles the footswitch |
| 13 | FS Right | 0,1 | 1 toggles the footswitch |
| 14 | Delay Select | 0–2 | 0 = Tape EP-III, 1 = Analog DMM, 2 = Precision |
| 20 | Reverb Bypass | 0,1 | 0 = Bypass, 1 = Unbypass. "always only bypasses Reverb regardless of footswitch mode" |
| 22 | Mix (delay) | 0–127 | delay mix; 127 = kill dry |
| 24 | Feedback | 0–127 | delay repeats |
| 25 | **Division** (tap subdivision) | 0–5 | 0 = 1/4, 1 = dotted 1/8, 2 = 1/8, 3 = 1/8 triplet, **4 = Dual 1/4 + dotted 1/8, 5 = Dual 1/4 + 1/8** |
| 27 | Mod | 0–127 | Tape EP-III: 0–63 = Mint tape, 64–127 = Worn tape. Analog DMM: 0 = off, 1–63 = Vibrato, 64–127 = Chorus. Precision: 0 = off, 1–63 = Flanger, 64–127 = Chorus |
| 28 | Reverb (level) | 0–127 | reverb mix; 127 = kill dry |

NOTE: The chart also includes a **Reverb Select** (3-position, Spring/Plate/Hall) and likely a **Delay Time** CC and **Color** CC above this excerpt — Morningstar forum confirms **CC-15 = Reverb Select**. Full enumerated map is in the UAFX Control app's CC page and the "USB MIDI with UAFX Pedals" manual.

## Power-user gold buried in the CC chart
- **CC-25 Division = tap-tempo subdivisions you cannot set from the hardware knobs.** Beyond 1/4, dotted-1/8, 1/8, 1/8-triplet, there are TWO **dual-rhythm** modes (Dual 1/4 + dotted-1/8, and Dual 1/4 + 1/8) — multi-tap/rhythmic-echo patterns. On a bare pedal you only get whatever the tap sets; via MIDI (or the app) you unlock dotted-eighths and dual subdivisions. This is the single most useful "hidden" delay feature for ambient/dub work.
- **CC-20 Reverb Bypass is independent of footswitch mode** — you can MIDI-toggle reverb on/off even in Delay|Tap-Tempo mode where the footswitch can't.

## MIDI channel / clock
- Manual defers channel + PC + CC assignment to the separate "USB MIDI with UAFX Pedals Manual." MIDI channel is set per-pedal in UAFX Control.
- Tempo-dependent effects sync to external MIDI Beat Clock (UAFX 2.0).

## Confirmed spec (manual, p. spec sheet)
- Power: Isolated 9VDC, center-negative, **400 mA min**, 2.1×5.5 mm; must be **LPS-compliant**.
- I/O: 2×¼" TS in (in2 = stereo R), 2×¼" TS out (out2 = stereo R). In Z = 500 kΩ mono / 1 MΩ stereo; out Z = 500 Ω. Max in 12.2 / out 12.1 dBu. 20 Hz–20 kHz ±1 dB.
- USB-C "for registration and firmware updates via computer" (and post-2.0, USB-MIDI). Bluetooth v5 for app.
- Height 2.56 in / 6.5 cm. FCC ID 2AXKQ2029.
