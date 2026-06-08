https://www.youtube.com/watch?v=7HuHyHSX8d8
YouTube · "Generation Loss MKII Latency: How Bad Is It? And How to Fix It." · (synth-focused reviewer) · accessed 2026-06-03

# Gen Loss MkII LATENCY — actually MEASURED (resolves the dossier's "unverified" flag)

Full cleaned transcript: `research/transcripts/genloss-latency-prose.txt`. This is the single best source of HARD numbers on a spec the dossier (§4, §8) lists as "unpublished / unverified." The reviewer measured round-trip latency with a DAW latency-compensation plugin (Pipeline) and subtracted the interface baseline (27.54 ms).

## The measured numbers (on ORIGINAL firmware, pre-latency-mod)
- **Wet signal (effect on): ≈25 ms** total latency.
- **Dry signal (analog thru / Dry blend): ≈9 ms.**
- **Wet-vs-dry difference: ≈16 ms** — this is the real gotcha.
- Even in **soft/DSP bypass** there's already added latency (~36.4 ms round trip incl. interface vs 27.54 baseline).

## What it means in practice (quoted/paraphrased)
- "The latency will be **imperceptible if you're using the pedal on synths with any attack at all** or really any melodic source that doesn't have significant transients."
- "But if you're using it on something like super punchy synth bass, a plucky guitar riff, or a drum loop, the latency can be obvious and in some cases unacceptable."
- The **16 ms wet/dry gap is the bigger problem**: mixing in the Dry blend on percussive material gives "an obvious doubling / phasing / flaming" on the kick transient. "You can't bring in the dry signal and get phase-coherent results." → On drums the internal Dry blend is "kind of out the window."
- BUT he notes the whole point is wow/flutter pitch modulation, which "throws all those measurements out the window" anyway — once Wow/Flutter are up, the wet signal is moving, so a few ms of wet/dry skew is moot. He concludes 25 ms is "negligible" for synth/melodic/ambient use, which is what the pedal is built for.

## The studio fix
- **Don't use the pedal's own Dry blend for phase-critical/percussive parallel processing.** Instead run it as a **DAW hardware insert** with a latency-compensation plugin (Pipeline in Studio One; most DAWs have an equivalent), keep the pedal **100% wet**, and blend the dry **in the DAW** where latency comp keeps it phase-coherent. Then you can blow up drums with Saturate+Model and tuck them under the clean kit.
- His wish-list: CB "should have intentionally delayed the dry signal in the pedal to line up with the wet" — i.e. accept the 24 ms and align dry to it for in-box parallel use. (CB's actual answer was the **low-latency firmware mod** — see `cb-mods-page-genloss-latency-bass.md`.)
- **Live:** no fix — "you're just kind of stuck with the latency." For this rig that's fine: it's an ambient/drone End-Board opener feeding delays, not a transient-critical lead.

> RIG TAKEAWAY: with banjo (fast staccato attack) the ~25 ms is at the edge of perceptible on dry plucks, but Gen Loss here is used to SMEAR/SUSTAIN the banjo (high Wow/Flutter), which masks it entirely. Don't rely on the internal Dry: Unity blend for tight parallel/percussive work — and if percussive tightness ever matters, flash the low-latency 1.1.0 firmware.
