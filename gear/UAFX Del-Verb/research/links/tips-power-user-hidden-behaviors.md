https://help.uaudio.com/hc/en-us/articles/13621234251284-UAFX-Del-Verb-Ambience-Companion-Manual
help.uaudio.com (official manual, "Updated December 22, 2025") + MusicRadar/Guitar.com reviews · distilled 2026-06

# Power-user tips & hidden behaviors (manual-verified + review-confirmed)

## Kill-dry at max (parallel / aux trick)
- BOTH wet knobs kill the dry when fully clockwise: "When you rotate this knob fully clockwise, the signal becomes 100% wet — you only hear the delayed signal and the dry signal is muted (kill dry)" (Mix). Same for the Reverb knob: "fully clockwise … 100% wet … dry signal is muted (kill dry)."
- USE: run the Del-Verb on a parallel/aux send (mixer aux, Apollo send, or amp's parallel loop) and crank Mix/Reverb full CW to get a pure 100%-wet stereo ambience return with zero dry colour. This is the proper way to use it as a studio send reverb.
- BEWARE: on a normal series board, accidentally maxing either knob mutes your dry tone — surprising if you don't know it.

## Runaway audio survives bypass (manual: "Self-Oscillation/Runaway Audio")
- Tape EP-III and Analog DMM self-oscillate past ~3 o'clock feedback; Precision repeats indefinitely at max but does NOT self-oscillate.
- Quote: "When your sound is set to self-oscillate or repeat indefinitely with very high feedback, turning off the pedal does not stop the feedback. In Trails Off mode, it continues to run in the background and will return when you turn the pedal back on. In Trails On mode, it continues to play."
- KILL IT: "To quickly stop runaway audio, reduce Feedback to the minimum setting." Bypassing won't do it. Know this before a quiet section.

## Color = overdrive on Analog DMM (and what it does on the others)
- Per-model Color behavior (manual): Tape EP-III Color = record level; Analog DMM Color = INPUT GAIN, "Leave at noon to match hardware gain, increase beyond noon to add overdrive and harmonics"; Precision Color = delay TONE, "To the left, cuts treble. To the right, adds treble. At noon, tone is flat."
- USE: push Analog DMM Color past noon for grit/saturation on the repeats (a drive baked into the delay) — great for doom/dub feedback walls.

## The bipolar Mod knob (noon = OFF, two zones)
- Manual confirms the two-zone behavior per delay:
  - Tape EP-III: 0–noon = Mint/New tape, noon–max = Worn tape (a tape-condition crossfade, not a true mod).
  - Analog DMM: noon = off; LEFT half = Vibrato amount; RIGHT half = Chorus amount.
  - Precision: noon = off; LEFT half = Flanger; RIGHT half = Chorus (combines rate/depth/feedback/mix).
- Guitar.com confirms the DMM feel: "either sweet chorus or sickly vibrato, depending on where the modulation dial is set."
- USE: set noon for a clean repeat; nudge left or right for movement without leaving the delay page.

## Tap-tempo subdivisions are richer than the hardware shows
- Hardware tap only sets quarter-note tempo. The SUBDIVISION (Division) is a hidden parameter: 1/4, dotted-1/8, 1/8, 1/8-triplet, and TWO dual-rhythm modes (Dual 1/4 + dotted-1/8; Dual 1/4 + 1/8). Set it via the app or MIDI CC-25. Dotted-eighth + dual modes are where the ambient/U2 and multi-tap rhythms live.

## Switching engines auto-compensates long delay times
- Manual: "When switching between effect types when very long delay times are set … delay times are automatically adjusted to compensate for the maximum available length." (Tape maxes 700 ms, DMM 1068 ms, Precision 1500 ms — switch from Precision-at-max to Tape and it rescales rather than breaking.)

## Tape & DMM pitch-shift with time changes; Precision doesn't
- Tape EP-III (80–700 ms) and Analog DMM (110–1068 ms): "Delay pitch varies as delay time is changed" — turn the Time knob live for tape-warp pitch dives. Precision (120–1500 ms) is pitch-stable EXCEPT on voicings labeled "glide."

## Voicings are the real depth (no decay/tone/predelay on hardware)
- The missing reverb decay/tone/pre-delay and alternate delay characters live in app "Voicings" (factory sounds, e.g. "Symphonic Reverb," "Spring C Rotato," "Spring Tube Drive B"; MusicRadar/reviews report ~12 per engine for some). A selected voicing is saved per effect type and recalled when you switch to it; knob + tempo settings persist too. PLAN VOICINGS BEFORE A GIG — you can't fix a wrong tail on the hardware.
- MusicRadar's standout cons: "the lack of a Decay control on the Del-Verb is surprising," "no onboard reverb controls beyond level and type," "lacking onboard user presets."
