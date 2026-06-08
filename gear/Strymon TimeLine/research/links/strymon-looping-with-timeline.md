https://www.strymon.net/looping-with-strymon-timeline/
strymon.net · Strymon (official) · undated guide

Official deep-dive on the TimeLine's 30s looper. The cleanest reference on the looper's quirks and the pre/post and exit behaviors that trip people up.

## Entering / running the looper
- **Hold TAP** to enter Looper mode (front-panel footswitches re-map).
- Footswitches in looper mode: **Record → Overdub → Play → Stop**.
- 30 seconds at normal speed; **Half-Speed doubles record time to 60s** (and drops the loop an octave).

## LP LOC — pre vs post delay (the routing decision)
- **Pre-delay:** "Record your dry signal and affect the recorded signal with the delay sounds." Loop is captured clean, then the live delay machine processes the playback. You can change the delay machine/settings AFTER recording and the loop re-colors live.
- **Post-delay:** "Record the delay sounds to the loop" — the wet repeats are baked into the recording.
- For drone work this is the key creative fork: pre-delay = a clean banjo/baritone loop you can then smear with dTape/Lo-Fi live; post-delay = freeze a fully-wet textured bed.

## LPEXIT — what happens when you leave looper mode
- **PLAY:** "Loop continues playing when you exit looper mode" — lets you change presets / play live over a sustaining loop. This is the ambient-layering setting.
- **STOP:** loop halts on exit (default).

## MIDI-only looper functions (not on the 3 footswitches)
- **Reverse** (toggle) and **Half-Speed** (toggle) are reachable only via MIDI or a MultiSwitch — see the CC list. Plus **Undo-to-initial-loop** and **Redo**.

## Quirks worth flagging
- Looper HF audio fidelity was poor on early firmware; **fixed in v1.84** — on a benched unit confirm 1.88 before judging loop quality.
- Half-Speed "right-channel-only" bug existed pre-1.58; fixed.
- Repeated UNDO with no overdubs glitched playback pre-1.84; fixed.
- The dBucket-longest-delay-in-looper DSP glitch is the last documented bug, fixed in **1.88**.

## Rig use (benched-as-second-looper role)
Set **LP LOC = pre**, **LPEXIT = PLAY**: loop a clean banjo drone, exit, then play baritone over it through the H90 while the TimeLine sustains the bed. A clean MIDI-controllable second looper alongside MOOD MkII / Blooper.
