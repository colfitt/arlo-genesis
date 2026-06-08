https://www.vguitarforums.com/smf/index.php?topic=38106.0
vguitarforums.com · "Boss VG-800 Documentation" thread (Elantric/mod, HitechGuitar) + Roland Knowledge Base · 2025

Power-user setup notes, output/tuner modes, and pitfalls.

## Output / connection mode (critical for THIS rig)
- The GK-5 (or GK-5B bass) is **required** for any modeling. Plug a normal guitar into GUITAR INPUT and you get a plain amp/FX processor only — no INST models.
- Going into a pedalboard/interface (not a real amp's return), use the **LINE/PHONES (Recording)** output mode. The amp-return modes (JC-120 / Katana power-amp return) are voiced to drive a real amp and sound wrong into the front of a pedal chain. (Corroborates MusicRadar's *"amp models into a real amp = harsh, digital"* finding — go LINE/direct.)
- Output is stereo (L/PHONES + R/MONO); for a mono front-of-chain run **R/MONO only**.

## Tuner modes (affects what gets tuned)
Per Roland KB — MENU → TUNER:
- **MULTI mode:** tuner ignores the GUITAR INPUT signal (tunes via GK only).
- **SINGLE mode:** tunes the GUITAR INPUT only when no GK input is present.
- **TT mode:** for True-Temperament-fretted instruments.
Pick the mode that matches whether you're tuning the divided pickup or the magnetic input.

## Memory / patch terminology + Tone Studio gotcha
- **Memory** = a single patch; **Liveset** = an array/bank of patches.
- **Boss Tone Studio imports do NOT auto-write to the hardware.** You must use **"Export to VG-800"** to commit a patch permanently, or you'll lose edits.

## Cable gotchas
- GK socket needs a **Serial GK (BGK-series) cable** — NOT a standard 1/4" guitar cable and NOT a 13-pin cable. BGK is Serial-GK-only and not interchangeable with audio cables.
- **MIDI** uses **Type-A TRS-to-5-pin DIN** adapters (BOSS BMIDI series) — get the polarity right.

## Alt-tuning ↔ MIDI interaction (gotcha)
- **HitechGuitar (June 2025):** when ALT TUNING is enabled it **affects the MIDI OUT** — this contradicts docs that imply independent operation. If you want MIDI to follow the tuning, set CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE = ON; if you want raw physical pitches out, leave it OFF. Know which you're doing.

## Other documented pitfalls (cross-thread)
- **No onboard expression treadle** and **no controls on the GK-5** (older GK-2/3 had S1/S2 + a volume knob) — wire an EV-30/FV-500 to a CTL/EXP jack to recover hands-on synth-balance/morph control.
- **Auto-off defaults to ~20 min** — disable for studio sessions.
- **GK-5 cable is slightly short** for some rear-body mounts; **GK-5 won't fit traditional Tele bridges** with raised side plates (irrelevant for Jazzmaster + banjo, but note it).
- **Calibration is the whole game** — default SENS wobbles low strings; fix it in GK SETTING, don't wait for firmware (see firmware-lore and gk5-tracking files).
