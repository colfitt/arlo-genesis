https://www.strymon.net/support/timeline/ + https://www.strymon.net/faq/timeline-firmware-update-troubleshooting-tips/ + forum.morningstar.io threads + Strymon DIG-vs-Dual FAQ
strymon.net (support/FAQ) + Morningstar forum + community · multi-source

Consolidated common pitfalls/gotchas the community trips over. Cross-checked against official FAQ where possible.

## Power
- **300 mA minimum at 9V. Never exceed 9V.** High draw — won't run off a Voodoo Lab **PP2+** outlets 5/6 (250mA max). Needs a high-current isolated output. Daisy-chaining invites ground-loop hum. This is a real reason it taxes a crowded board.

## Spillover / trails (the #1 most-tripped behavior)
- **~5-second rule:** trails only spill across a preset change if the current preset has been active **at least ~5 seconds**. Fast preset stomps **cut the tail.** Architectural (buffer), present since v1.23 — never removed.
- **Persist=ON forces BUFFERED bypass.** You can't have trails AND true bypass. If you want true bypass (relay), you give up spillover.
- Pre-1.58: trails got cut when bypassed in **FEEDBACK LOOP mode** (fixed). Pre-1.84: an audible glitch on dBucket→Dual(parallel) spillover (fixed).

## MIDI clock vs tap vs preset BPM (see dedicated midi-clock file)
- TimeLine **receives but never SENDS** MIDI clock — always a slave. It can't be the rig's clock master.
- Per-preset **MIDICL** (firmware ≥1.84) decides follow-clock vs use-saved-BPM **per preset**. A global tap/clock cascades across every clock-following preset and overwrites their tempos. Set free-running presets MIDICL=OFF.
- A specific dBucket preset was reported **hardcoded to 75 BPM** ignoring clock — rebuild it if you hit it.
- Editor bug: "Show Tap Menu = NO" could **double** the BPM sent to the pedal.

## Input level / hot signals
- Fed hot **modular / line-level** signals the TimeLine can **distort, drop a channel, or even mute.** Attenuate to instrument level. (In this rig the **VG-800's line-level out** is exactly this hazard — the EHX Effects Interface on the bench exists to match VG-800 line level → pedal instrument level before the TimeLine.) Max input +8dBu.

## Front-panel navigation / learning curve
- **Bank/preset scrolling needs two footswitches at once** (A+B), which is awkward live — the standard fix is an external MIDI controller (MC6 etc.) or MultiSwitch for one-press bank up/down. Deep params live behind knob-push menus; the **Nixie editor** is the sane way to build/organize presets (see nixie file).

## Looper
- Don't judge loop fidelity on old firmware — HF audio was poor pre-1.84 (fixed). Half-speed right-channel-only bug pre-1.58 (fixed). UNDO-with-no-overdub glitch pre-1.84 (fixed). dBucket-longest-delay-in-looper glitch fixed in **1.88** (the final fix).

## Firmware update process
- Updates go over **MIDI** (Nixie / Strymon updater). Updating through an audio-interface or keyboard MIDI port often **fails** — use a dedicated MIDI interface (UM-ONE / UX-16). Most "plug-and-play" interfaces fail for the high data rate.

## Feature it does NOT have (myth-buster)
- **No "Golden Ratio" tap division.** That's exclusive to the smaller **DIG** pedal. TimeLine tap divisions: whole, dotted-eighth, quarter, eighth, dotted-sixteenth, triplet, sixteenth, etc. — but no golden ratio. If a forum/blog says the TimeLine has golden ratio for "never-stepping" ambient repeats, it's wrong. (For non-stepping ambient washes on the TimeLine, use **Dual with a non-integer-feeling ratio** + high repeats, or **Pattern**, or the **infinite hold**.)

## HONESTY note
Most "TimeLine bug" posts you find are **stale** — fixed years ago. The owned unit on **1.88** has none of the looper/MIDI bugs above. Always confirm firmware before chasing a reported bug.
