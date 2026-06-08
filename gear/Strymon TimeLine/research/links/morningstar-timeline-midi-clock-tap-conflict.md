https://forum.morningstar.io/t/strymon-timeline-and-mc6-v2-tap-tempo-issue/2339
forum.morningstar.io · Morningstar Engineering user forum (James @ Morningstar + users) · thread

THE definitive community explanation of the TimeLine's most-confusing MIDI gotcha: tap tempo / MIDI clock vs per-preset BPM. Reinforced by sibling threads (`/resolved-midi-clock-problem-with-timeline/6321`, `/strymon-and-midi-clock-sets-weird-bpm-values/4492`).

## The problem (very common complaint)
A user assigns tap-tempo on the MC6. Tapping e.g. 108 BPM, then switching presets, makes EVERY subsequent preset adopt 108 BPM — overriding each preset's saved tempo. A 70-BPM preset now plays at 108. Or: after a few taps the tempo reverts to a previously-set BPM.

## Root cause (James @ Morningstar)
- The TimeLine has a **per-preset MIDI Clock setting** (`MIDICL`, in PARAMS since firmware 1.84): each preset decides whether it **follows incoming MIDI clock BPM** or **uses its own saved Preset BPM**.
- "The Timeline has a MIDI Clock setting for each preset, where it will determine whether that preset follows the MIDI clock BPM or the Preset BPM."
- An incoming MIDI-clock stream (or a global tap-tempo broadcast) cascades across presets BECAUSE those presets are set to follow MIDI clock.

## The fix (config, not a bug)
1. Edit each preset's `MIDICL`:
   - **Presets that should keep their saved tempo → MIDICL = OFF** (ignore incoming clock).
   - **Presets that should track the master clock / tap → MIDICL = ON.**
2. On the MC6, enable **"MIDI Clock Persist"** so clock runs continuously rather than stopping between presets.

## Related real bugs (not just config)
- One specific factory/user **dBucket preset was hardcoded to force 75 BPM** regardless of MIDI clock (separate thread `/6321`). Workaround = rebuild/avoid that preset.
- Editor bug: with "Show Tap Menu" = NO, BPM sent to the pedal was **doubled**; = YES sent correct tempo (`/4492`).

## For THIS rig (Digitakt 2 = master clock)
- The TimeLine is **always a clock slave — it receives but never sends MIDI clock.** Digitakt stays master.
- Set drone/free-running presets to **MIDICL = OFF** so a long ambient wash isn't yanked to the song tempo; set rhythmic delay presets (Dual/Edge, Pattern) to **MIDICL = ON** to lock to the Digitakt.
- Decide tap-vs-MIDI-clock per preset — don't broadcast a global tap that stomps every patch.
