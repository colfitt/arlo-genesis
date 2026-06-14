https://support.spitfireaudio.com/en/articles/11816113-midi-cc-chart-for-spitfire-audio-libraries
Spitfire Audio Help Centre · "MIDI CC Chart for Spitfire Audio Libraries" + Cells FAQ notes

Reference for the Spitfire-app plugin player (Cells / LABS / Originals all share it). Plus the official capture/bounce guidance.

## MIDI CC chart (plugin libraries — Cells/LABS/Originals)
- **CC1** — Modulation (**Dynamics**): transitions between dynamic layers. *Primary expression control.*
- **CC11** — Expression: sample volume, independent of plugin volume.
- **CC21** — Vibrato.
- **CC18** — Tightness (how tight short techniques play).
- **CC16** — Speed/Tightness (legato interval timing).
- **CC17** — Release (extends sample decay/tail). *Useful for longer drone tails.*
- **CC19** — Reverb amount (plugin libraries only).
- **CC7** — Volume · **CC10** — Pan · **CC64** — Sustain.
- **CC22–27** — Microphone signals (library-dependent).

## Capturing the generative output (from Cells FAQ / Spitfire support)
- **"Bounce any saved Cells tracks to audio before installing updates"** — to prevent changes to saved Scale-mode intervals across versions. (Implication: the generated result is reproducible enough to commit to audio, and you *should*, to lock it.)
- **"Played mode will now work in offline / non-realtime bounce."** — i.e. the generative engine survives an offline freeze/bounce, so you can render the evolving texture to audio rather than only printing in real time.

→ Practical capture path: record the MIDI you play → the engine generates deterministically per note → freeze/bounce to audio (offline OK) → or lift the surprise melodies into MIDI for another instrument (per Ólafur's own quote).
