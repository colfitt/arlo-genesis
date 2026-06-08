Consolidated from community/blog/official sources (URLs inline below)
multiple · accessed 2026-06-03

# MOOD MkII — common pitfalls & gotchas (consolidated)

A single distilled gotcha list pulled from the hidden-options walkthrough video, the firmware clip, official tips page, Guitar.com, and the MkII-vs-V1 community writeups. Each item flagged verified vs community-reported.

## Level / gain-staging
- **The two channels are not auto-balanced; MIX won't fix it.** On V1 you literally couldn't balance wet vs micro-looper (only an internal trimmer). MkII fix = **LEVEL BALANCE hidden option (CLOCK knob in the hidden menu)**, not the front-panel MIX. If one channel buries the other, go there. [VERIFIED — hidden-options video + community]
- **DIRECT MICRO-LOOP causes an audible volume bump** as you blend clean micro-loop into the wet path. Re-check overall level after using it. [VERIFIED — hidden-options video]
- **DRY KILL turns MIX into a wet-only 0–100.** With DRY KILL on and MIX down, you get *silence* (no dry to fall back on). Expected, but surprising live. [VERIFIED — hidden-options video]
- **Fuzz upstream:** general CB/Drolo-channel caution — low-Clock downsampling + a hot fuzz feeding the always-listening looper can clip the capture. Keep input sane; CLOCK higher preserves low-end on bass/baritone (aggressive low-Clock thins fundamentals). [COMMUNITY/dossier-corroborated, not a hard CB warning]

## Feedback / runaway
- **Delay MODIFY at max self-oscillates / piles up like a looper.** That's the intended "looping echo" behavior, but it runs away into a wall fast — back MODIFY off ~1:00 for "piling repeats" without losing control. [VERIFIED — manual/dossier; Guitar.com notes the delay "piles up like a looper" at max]
- **Capturing through the wet effect bakes it in permanently.** The always-listening looper records whatever the wet/upstream signal is doing — capture through Reverb and the ambience is *in the loop forever* (the "Trail Catcher" effect). Plan the capture moment. [VERIFIED — manual/dossier]

## Stereo / bypass
- **SPREAD does not create stereo — it widens existing stereo.** If you expect mono→stereo, that's **MISO**, not SPREAD. [VERIFIED — hidden-options video: "it's NOT turning stereo on or off… just making it wider"]
- **Buffered bypass + trails is the default; true-bypass = tap both footswitches 3× (LEDs blink red).** BUT the **looper does not run in true-bypass.** Don't pick true-bypass if you rely on the always-listening capture. [VERIFIED — manual + hidden-options video]
- **Rig-specific:** Blooper immediately downstream is **mono**, so any MOOD stereo image collapses there. Wide stereo has to land later (Chroma/H90), or bypass Blooper. [rig dossier §5]

## Mode / dip interactions
- **FADE and NO DUB are mutually exclusive — "no dub, no fade."** Enabling NO DUB kills the FADE behavior. [VERIFIED — hidden-options video]
- **NO DUB "pseudo-live effect" requires overdub LEFT ON**, and tracking quality depends on CLOCK: *"the higher the CLOCK knob is turned up, the closer it will track your playing."* [VERIFIED — hidden-options video]
- **MIDI clock is IGNORED in MIDI Synth Mode**, and a stray MIDI Note auto-engages Synth Mode (turning CLOCK into pitch control) — so a loose Note from the Digitakt silently knocks MOOD out of clock sync. Exit via CC59 or by moving CLOCK. [VERIFIED — see the cb-stack MIDI deep-dive; do not re-derive here]
- **Firmware:** stock-1.0 MkII Stretch sounded different from the beloved MkI Stretch and *"confused people"*; **firmware 1.1 restores MkI Stretch inside Classic Mode.** Update at firmware.chasebliss.com. [VERIFIED — CB firmware-1.1 clip]
- **Presets: only 2** (left/right toggle); dip + hidden settings save per-preset, so a "misbehavior" preset (CLASSIC/SMOOTH/SPREAD on) and a "clean" preset can coexist — but that's your whole onboard preset budget. Use MIDI PC for more scenes. [VERIFIED — manual/dossier]

## Power
- **~270 mA draw, 9V center-negative.** Needs a beefy isolated supply slot; under-powering starves the always-listening DSP. [VERIFIED — manual]

## Sources
- https://www.youtube.com/watch?v=7BHsCIvyzLk (hidden-options/dip walkthrough)
- https://www.youtube.com/watch?v=PZPuwN85TOI (firmware 1.1)
- https://www.chasebliss.com/setting-the-mood (official tips)
- https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-mood-mkii/ (Guitar.com 9/10)
- https://www.sinesquares.net/musicgear/chase-bliss-mood-mkii-release (MkII-vs-V1 + clock noise)
- MIDI Synth-Mode caveat: Gear/Chase Bliss Blooper/research/links/cb-stack-clock-sync-per-pedal.md (do not duplicate)
