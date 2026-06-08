---
title: "Reamping Fundamentals — DI Then Transform"
slug: reamping-fundamentals
type: technique
scope: technique
topic: reamping fundamentals (two-stage DI-then-transform workflow)
tags: [reamping, di, guitar, recording, creative-workflow, mk-gee]
aesthetic_stack: [mk-gee, bon-iver, lcd-soundsystem]
related:
  - corpus/artists/mk-gee-di-direct-philosophy.md
  - corpus/artists/bon-iver-vocal-layering-messina.md
  - corpus/artists/james-murphy-analog-synth-philosophy.md
status: seed
confidence: high
---

# Reamping Fundamentals — DI Then Transform

Reamping is a two-stage recording workflow: capture a clean direct-input (DI) signal first, then re-record (or "re-amp") that DI through a physical amplifier, pedalboard, or other effects chain later. It decouples the *performance* from the *tone*, so the tone becomes a mix decision rather than a tracking commitment. The technique is the engineering backbone of an entire modern aesthetic — mk.gee's DI-only guitars, Bon Iver's chamber-and-amp vocal treatments, LCD Soundsystem's analog-stomped synths — because it lets you treat any signal as raw material for transformation.

## What Reamping Actually Is

Reamping is "the process of feeding an already recorded signal into an amplifier, and then recording back to tape/daw the sound coming from the speaker(s)" [^5]. The clean DI is captured first, with no amp, no pedals, no commitment. Later — minutes or months later — that DI is sent back out of the interface, through a reamp box, into whatever amp/pedal/chamber rig you want, and a microphone (or another DI) captures the result onto a new track [^1][^3].

The two-stage flow:

1. **Stage 1 — DI capture.** Guitar (or vocal, or synth, or drum bus) goes through a DI box into the interface. You record a clean, unprocessed track [^1][^3].
2. **Stage 2 — Reamp.** The DI track plays out of the interface, through a reamp box, into an amp/pedals. A mic on the cab (or a line out) records the new sound onto a fresh track [^1][^3].

The DI track is preserved. You can reamp it again with a different rig tomorrow.

## Why Reamping Beats Committing at Tracking

When you commit tone at tracking you're gambling: the amp, mic, room, and pedal settings have to be right at the moment the player is in the zone. Reamping flips this. As one practitioner frames it, you "separate performance capture from tone experimentation" [^5]. The performance is locked; the tone is plastic.

Concrete creative wins documented across the guides [^1][^2][^3][^4][^5]:

- Try unlimited amp/mic/pedal combinations without asking the player to re-perform
- Move the mic, change the room, swap the cab — the take never changes
- Stereo-ize a mono performance by reamping the same DI twice through different rigs
- Print pedalboard tweaks dynamically during playback as a kind of performance pass
- Fix a bad amp choice from a remote/mobile session months later
- Develop microphone-placement intuition by A/B-ing positions against an identical source [^5]

This is why mk.gee tracks everything DI and transforms in the box and out-of-the-box afterward — see the [mk.gee DI philosophy](../artists/mk-gee-di-direct-philosophy.md) sibling for the extreme case.

## The Impedance and Level Problem (Why You Can't Just Plug DAW Output Into an Amp)

A guitar amp's input expects a high-impedance, instrument-level signal — what a passive pickup produces. An audio interface's output is a low-impedance, line-level signal (nominal +4 dBu in pro gear, -10 dBV in consumer). Plugging the interface straight into a guitar amp produces wrong impedance, wrong level, and frequently ground-loop hum [^3][^4].

A reamp box is the bridge. As Audient puts it plainly: "It is important to use a re-amp box because amps operate on a different impedance to what your audio interface is sending" [^3]. Pro Audio Files describes it as adapting "the balanced, low-impedance output from a DAW to match the unbalanced, high-impedance input requirements of guitar amplifiers and effects pedals" [^4].

Mechanically, a passive reamp box does this with a custom transformer that:

- Unbalances the signal (XLR/TRS → ¼" TS)
- Shifts impedance into the range guitar amps expect
- Provides galvanic isolation, killing ground-loop hum between the interface chassis and the amp chassis [^6][^7]

The Radial Reamp JCR — currently the canonical reference — publishes input impedance of 1,800 ohms and output impedance of 4,800 ohms, with a 20 Hz–20 kHz frequency response and total harmonic distortion of 0.001% at 1 kHz / 0 dBu input [^6]. The transformer is a custom-wound design that "naturally rounds out the tone" when hit harder, which is itself a sound [^7].

## Setting Reamp Output Levels — Don't Distort the Box

The single most common reamping mistake is overdriving the reamp box itself rather than the amp. The signal hitting the reamp box's input is line level — much hotter than what a guitar pickup outputs — so if you set the reamp box's output (which goes to the amp) too high, you get nasty front-end distortion that isn't your amp's tone, it's the transformer or the amp's input stage choking on a too-hot instrument-level signal.

Practical calibration from the working-engineer literature [^8]:

- Set the DAW send fader to unity (0 dB)
- Adjust the reamp box's variable output knob until the rig sounds like the guitar plugged in directly — same level, same touch response
- If you can't get there because the box is fully cranked and still too quiet, your DI was recorded too low; re-record DIs around -6 to -4 dBFS so you have headroom and don't need to max the reamp box [^8]
- If the box is too hot at minimum, attenuate at the DAW output

A useful calibration trick: send the DI through the reamp box, *back into* a DI box, and record that loop. Adjust the reamp box output until the looped track matches the original DI in level [^8]. Once unity is dialed, you know what your amp is hearing.

The same logic applies in reverse for active reamp boxes, which have gain stages instead of (or in addition to) transformers — you have one more place to clip, so watch the level meters at every stage.

## Reamping Non-Guitar Sources (The Fender Amp Trick)

Reamping isn't a guitar technique, it's a *signal* technique. The same box and workflow opens up vocals, synths, drums, and bus sends [^2][^5].

**Vocals.** Run a tracked vocal back out through a reamp box into a guitar amp, mic the cab, and you get the natural overdrive character of a tube amp on the voice — used famously on tracks like the Breeders' "Cannonball" and King's X's "The Big Picture" [^2]. Blend the reamped track with the dry vocal for a parallel-distortion effect. Justin Vernon's vocal processing on *22, A Million* — the "Messina" chain built by engineer Chris Messina — is a different system (Auto-Tune plus Eventide H8000 harmony), but the broader Bon Iver discography routinely runs vocals through amps and chambers, and the reamping mindset (track clean, transform later) is the same [^9].

**Synths.** Reamp a soft-synth or modular line through a real spring reverb tank, a vintage delay pedal, or a rotary speaker — sounds plug-ins still struggle to fully replicate [^2][^5]. James Murphy and the DFA studio approach treats analog signal-mangling as core to the LCD aesthetic; see the [James Murphy analog synth philosophy](../artists/james-murphy-analog-synth-philosophy.md) sibling.

**Drums.** Send a drum bus through a guitar amp or stomp compressor for parallel grit; Premier Guitar specifically mentions using a guitar compressor pedal as an outboard drum compressor via reamping [^2][^5].

**Anything.** Pianos, pads, bass DIs, sub-bass synths split high-and-low for selective distortion on the highs — the technique generalizes [^4][^5].

## Reamp Chambers and Room as Effect

A reamp output doesn't have to feed an amp. Feed it into a powered speaker in a stairwell, garage, tile bathroom, or empty room and mic the result. Roger Montejano lists "Verb Chamber Simulation — Feed signals through rooms to capture spatial characteristics" as one of the canonical 14 reamping moves [^5]. This is how you get reverb that no convolution IR captures — real air, real reflections, real spill from the HVAC.

## The mk.gee Workflow as the Extreme Case

mk.gee (Mike Gordon) is the most visible contemporary practitioner of an all-DI, transform-later philosophy: most guitar tracks on *Two Star & the Dream Police* are DI signals re-processed through effects-as-instruments, not committed amp tones. The reamping mindset — DI is the source, tone is the verb — is the architectural assumption of his whole production approach. See [mk.gee DI direct philosophy](../artists/mk-gee-di-direct-philosophy.md) for the Tascam Portastudio 424 and refusal-of-amp specifics. The generic technique covered here is what makes that workflow possible at all.

## Specific Reamp Boxes Worth Knowing

**Radial Reamp JCR.** The current reference. Passive, transformer-isolated, designed by Reamp inventor John Cuniberti and now manufactured by Radial. Custom-wound USA transformer, 1,800 Ω input / 4,800 Ω output, 20 Hz–20 kHz response, variable output level, three-position filter (tame highs / warm lows / bypass), phase invert, separate XLR and ¼" TRS inputs [^6]. Around $229 [^1].

**Radial Reamp (original Cuniberti) and Reamp Jr.** The Reamp trademark and patent originated with John Cuniberti, who built the first unit in 1993 to feed a guitar amp from a Studer 2" tape machine output — there was no commercial solution at the time, so he wound transformers and designed a circuit himself. He was granted the U.S. patent in 1999 and sold over 3,000 units over seventeen years before selling the patent, trademark, and business assets to Radial Engineering in January 2011 [^10]. The Reamp Jr was the budget passive variant in that original lineup.

**Little Labs Redeye.** Passive direct box / reamp box hybrid; a button toggles between DI mode and reamp mode. Includes phase reverse, ground lift, and level control on the reamp side. Multiple units daisy-chain via rear expansion jacks (four fit in 1U) [^11].

**Little Labs Redeye 3D Phantom.** Two UTC transformers allow simultaneous DI and reamp operation on the same chassis [^11].

**Little Labs PCP Instrument Distro.** Transformer-isolated one-in / three-out (expandable to five) guitar splitter, plus active line-level direct box (16 dB of gain), plus reamp section that accepts three +4 dBu balanced inputs which can be summed. Instrument input impedance is extremely high at 10 MΩ [^11]. The all-in-one rig for serious tracking rooms.

**Radial X-Amp.** Active reamper. Allows simultaneous dual-amp reamping with separate output levels — useful for stereo-by-rig-difference [^7].

**Creation Audio Labs MW1 Studio Tool.** Mentioned alongside Radial in the reamping literature as a respected purpose-built reamp box [^5].

For most use cases at home/project-studio scale, a passive Radial JCR or a Little Labs Redeye covers everything. The PCP and X-Amp are upgrades for multi-amp or multi-source workflows.

## Phase Awareness When Blending DI + Reamped

When you blend the original DI with a reamped version (or two reamped versions), phase relationships matter — mic distance on the cab, the latency of the reamp roundtrip, and any pedal buffering all shift phase. Adjust mic distance along the cap-of-speaker axis, nudge tracks in the DAW, or use a phase-alignment tool like the Little Labs IBP to dial in constructive vs. destructive summing [^4]. A well-aligned DI-plus-reamp blend gives you tight low end from the DI and harmonic character from the amp track.

## Practical Tracking Discipline

To make reamping actually work later, build the habit at tracking:

- Always run a DI in parallel with any amped guitar take — even when you love the amp tone, the DI is insurance and creative option
- Print DIs around -6 to -4 dBFS so you have reamp headroom [^8]
- Label tracks clearly (DI / amp / pedal-pre / pedal-post) so future-you knows what's what
- For pedalboards, consider printing both pre-pedalboard DI and post-pedalboard DI; the post-pedal version locks in performance-dependent effects (envelope filters, fuzz that responds to picking dynamics) while still letting you reamp into a different amp

## See Also

- [mk.gee DI direct philosophy](../artists/mk-gee-di-direct-philosophy.md) — the canonical extreme case: DI everything, refuse the amp, transform with effects-as-instruments via Tascam Portastudio 424 and outboard chains
- [Bon Iver vocal layering (Messina)](../artists/bon-iver-vocal-layering-messina.md) — Justin Vernon's real-time vocal-harmony rig, a related "transform the signal post-capture" philosophy
- [James Murphy analog synth philosophy](../artists/james-murphy-analog-synth-philosophy.md) — DFA's analog-mangling approach to synth signal flow
- [Oblique strategies and studio-as-instrument](./oblique-strategies-and-studio-as-instrument.md) — broader Eno-derived mindset of treating the studio as a compositional tool

## Cited Retrieval Topics

When a conversation touches any of these, this entry is relevant:

- "How do I reamp a guitar?" / "What is reamping?"
- "Why do I need a reamp box — can't I just send the DAW into the amp?"
- "Reamp box too loud / distorting / hum"
- "Best reamp box for home studio" / "Radial vs Little Labs reamp"
- "Reamping vocals through a guitar amp"
- "Reamping synths / drums / bus sends"
- "mk.gee-style DI workflow" / "transforming DI guitar after tracking"
- "Setting up a DI workflow for later reamping"
- "Impedance matching DAW to guitar amp"
- "Phase alignment between DI and reamped tracks"
- "Reamp chamber" / "using rooms as reverb via reamping"
- "John Cuniberti Reamp history" / "who invented reamping"

## Sources

[^1]: Premier Guitar — "How to Reamp Your Electric Guitar Tone" — https://www.premierguitar.com/diy/recording-dojo/reamp
[^2]: Premier Guitar — "Reamping Fun for the Whole Band" — https://www.premierguitar.com/articles/Reamping_Fun_for_the_Whole_Band
[^3]: Audient — "Easy Guide To Reamping" — https://audient.com/tutorial/reamping/
[^4]: Pro Audio Files — "Reamping Guitars" — https://theproaudiofiles.com/reamping-guitars/
[^5]: Roger Montejano — "What's Reamping? How to set it up and 14 ideas on how to use it" — https://rogermontejano.com/articles/what-s-reamping-how-to-set-it-up-and-14-ideas-on-how-to-use-it
[^6]: Radial Engineering — "JCR Specifications" — https://www.radialeng.com/product/jcr/specifications and https://www.radialeng.com/wp-content/uploads/2018/04/JCReamp-Manual.pdf
[^7]: Radial Engineering — "JCR FAQ" — https://www.radialeng.com/product/jcr/jcr-faq
[^8]: Gearspace / HomeRecording forum threads on reamp output level calibration — https://gearspace.com/board/so-much-gear-so-little-time/1264168-reamp-output-level-calibration.html and https://homerecording.com/bbs/threads/reamping-issue-level-too-low-radial-jcr-behringer-umc202hd.400808/
[^9]: Sound on Sound — "Inside Track: Bon Iver '22, A Million'" (Chris Messina vocal chain) — https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million
[^10]: John Cuniberti / Radial Engineering — Reamp invention history (1993 Studer prototype, 1999 U.S. patent, 2011 sale to Radial) — https://www.radialeng.com/blog/john-cuniberti-interview and https://en.wikipedia.org/wiki/John_Cuniberti
[^11]: Little Labs / Sweetwater product documentation — Redeye, Redeye 3D Phantom, PCP Instrument Distro — https://www.littlelabs.com/home and https://www.sweetwater.com/store/detail/PCP--little-labs-pcp-instrument-distro
