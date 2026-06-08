# FM and Wavetable Synthesis

**Scope:** synthesis
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Gordon Reid, *Synth Secrets* (Sound on Sound, 1999–2004); Welsh's *Synthesizer Cookbook*; Native Instruments Massive / Massive X manuals; Yamaha DX7 documentation
**Tags:** `synthesis`, `FM`, `wavetable`, `principle`, `recipe`

---

## The Core Idea of FM Synthesis

Frequency-modulation (FM) synthesis uses one oscillator (the **modulator**) to vary the pitch of another oscillator (the **carrier**) at audio rate. When the modulation rate moves from sub-audio (LFO-style vibrato) into the audible range — roughly above 20 Hz — the ear stops hearing pitch wobble and starts hearing new harmonic partials called **sidebands**. The math underneath, formalized by John Chowning at Stanford in the early 1970s, is that for a sine carrier at frequency *fc* modulated by a sine at frequency *fm*, sidebands appear at *fc ± n·fm* for integer *n*, with amplitudes governed by Bessel functions of the modulation index ([CCRMA Stanford — FM synthesis](https://ccrma.stanford.edu/guides/planetccrma/FM_synthesis_on.html)). The practical takeaway is that you can build complex, harmonically rich timbres from just two sine waves, without the heavy harmonic content sawtooths and squares require. Chowning licensed the technique to Yamaha, which shipped it as the DX7 in 1983 — the synth that defined 1980s pop ([Yamaha Synth — FM Basics](https://yamahasynth.com/learn/reface/fm-basics-reface/)).

## Carrier-to-Modulator Ratio and Why It Matters

The frequency *ratio* between modulator and carrier — usually written **M:C** — determines whether the resulting sidebands fall on harmonic frequencies (musical, tonal sounds) or inharmonic ones (bells, metallic percussion). Integer ratios (1:1, 2:1, 3:1, 3:2) put every sideband on a harmonic of the fundamental, producing tonal results similar to natural instruments. Non-integer ratios (3.14:1, 7.83:1) scatter sidebands at inharmonic intervals, producing the metallic, bell-like, gong-like sounds FM is famous for ([Jacob Vosmaer — Yamaha FM Pitch Ratios](https://blog.jacobvosmaer.nl/0050-fm-pitch-ratios/)). The **modulation index** (the amount knob, often labeled "Level" on the modulator) controls how many sidebands appear and how loud they get. Low index gives a sound close to the pure carrier; high index spawns dozens of partials and can quickly turn harsh. The interplay of ratio (chooses *which* partials) and index (chooses *how many*) is the entire FM patch-design space ([Sound on Sound — More On Frequency Modulation](https://www.soundonsound.com/techniques/more-frequency-modulation)).

## Operators, Algorithms, and the DX7 Architecture

The DX7 ships with six **operators** — each operator being a sine oscillator plus a dedicated envelope generator. The way those six operators are wired together is called an **algorithm**, and the DX7 offers 32 fixed algorithm topologies that the programmer chooses from ([JonDent — Yamaha DX7 Operators & Algorithms](https://djjondent.blogspot.com/2019/10/yamaha-dx7-algorithms.html)). In any algorithm some operators are **carriers** (their output reaches the audio output) and others are **modulators** (they feed another operator's frequency input). A simple two-operator stack — one modulator feeding one carrier — produces a single FM voice. Stacking three or more operators in series, or routing several modulators in parallel into one carrier, multiplies the sideband count and lets you build evolving, multi-layered timbres. Algorithm 5 (three parallel two-op stacks) is the classic FM electric-piano routing; Algorithm 1 (a five-operator stack feeding one carrier, with an operator on feedback) is used for aggressive lead and bass patches ([Reverb Machine — Exploring the DX7](https://reverbmachine.com/blog/exploring-the-yamaha-dx7-pt2/)).

## Classic FM Sound #1: The Electric Piano

The DX7 electric-piano patch is so iconic it appeared on roughly 40% of Billboard Hot 100 number-one singles in 1986 ([Wikipedia — Yamaha DX7](https://en.wikipedia.org/wiki/Yamaha_DX7)). The basic recipe uses Algorithm 5 (three parallel two-operator stacks) — one stack synthesizes the tonal body (often a 1:1 carrier-modulator ratio for a saw-like body), one stack adds a low-frequency thump for the hammer attack, and the third stack uses a high-ratio modulator (often around 14:1) to produce the metallic "tine" bell that defines the Rhodes-style attack ([Pianoo — Yamaha DX7 FM Piano](https://pianoo.com/fm-piano-sound/); [Attack Magazine — FM Electric Piano](https://www.attackmagazine.com/technique/tutorials/fm-electric-piano/)). Velocity routes to modulator level on the tine stack so harder hits produce more brightness — without that, the patch sounds flat and synthy. Decay times on the carrier envelopes drop quickly to a low sustain, mimicking the natural ring-and-decay of struck tines.

## Classic FM Sound #2: Bell and Mallet Tones

FM is the easiest way to synthesize a believable bell because bells are physically inharmonic — their overtones don't line up on integer multiples — and FM with a non-integer ratio matches that behavior directly. A two-operator bell patch uses a sine carrier, a sine modulator at a high non-integer ratio (4:1 to 7:1 or higher), and an envelope on the modulator that decays faster than the carrier — so the bright "ping" attack fades quickly while the pure-tone tail rings on ([Sound on Sound — Synthesizing Bells](https://www.soundonsound.com/techniques/synthesizing-bells)). Tubular bells, glockenspiel, vibraphone, and metallic gong sounds are all variations on this single recipe with different ratios and envelope shapes. Welsh's *Synthesizer Cookbook* covers similar territory by harmonic analysis: a real bell has dense, inharmonic, fast-decaying partials, and FM gets there in two operators where additive would need ten.

## Classic FM Sound #3: FM Bass

FM bass leans on a stack with a single carrier and one or two modulators at integer ratios (1:1, 2:1) to get a harmonically dense saw-or-square-like fundamental, then uses operator feedback for additional sideband density and aggressive growl ([Azure Hills Music — Understanding FM Synthesis on the DX7](https://azurehillsmusic.com/understanding-fm-synthesis-on-the-yamaha-dx7/)). Velocity routed to modulator level gives expressive bite. The DX7's "Bass 1" preset and innumerable 80s pop and house records ride this template — it cuts through a mix because the upper sidebands occupy the 1–5 kHz "presence" zone where subtractive saw basses tend to get filtered away. FM bass is especially useful when you want the punch of a saw bass but with a tighter, less smeared low end than a Moog ladder filter delivers.

## Operator Feedback and Why It Matters

Most FM architectures let one operator feed its own output back into its frequency input — **self-modulation**, or feedback. With feedback at zero, an operator outputs a sine. As feedback rises, the operator's output progressively transforms toward a sawtooth-like waveform with increasing harmonic content ([RobSonic — Demystifying FM Synthesis](https://robsonic.org/demystifying-fm-synthesis-rich-tones-from-simple-operators/)). This is how FM synths produce saw-style timbres without ever leaving the sine domain — and it's a key tool for adding edge to lead and bass patches without stacking more operators. The trade-off is that high feedback amounts can quickly tip into noise-like instability; it's a steeper knob than modulation index.

## Wavetable Synthesis: Tables of Single-Cycle Waves

A wavetable is a sequence of **single-cycle waveforms** stored adjacently in memory. The oscillator plays one cycle at the playback pitch as it would any waveform, but the programmer can *move* between adjacent cycles in the table via a **position parameter** (Serum labels it "WT POS"; Massive calls it "Wt-position") ([Native Instruments — What is Wavetable Synthesis?](https://blog.native-instruments.com/what-is-wavetable-synthesis/); [Wikipedia — Wavetable Synthesis](https://en.wikipedia.org/wiki/Wavetable_synthesis)). The position knob is a continuous-control parameter, so as it changes you hear the timbre morph from frame to frame — usually with interpolation between adjacent frames to avoid stepping artifacts. Wavetables can contain anything from a smooth saw-to-square morph (a handful of frames) to ripped formant-sweeps from vocal samples (hundreds of frames). The PPG Wave (1981) was the first commercial wavetable synthesizer; Massive (2007), Serum (2014), Vital (2020), and Massive X (2019) are the modern descendants ([Perfect Circuit — Making Waves: the PPG System](https://www.perfectcircuit.com/signal/ppg-system)).

## Wavetable Position as a Modulation Target

The defining move of wavetable synthesis is routing a modulator to the position knob. A slow LFO (0.1–0.5 Hz) on position produces continuously evolving timbre — the staple of cinematic pads. An envelope on position lets the patch open into a different waveform as the note progresses, useful for plucks that ring out into shimmer. Velocity on position lets harder hits select a brighter frame ([Native Instruments — Massive X Wavetable Oscillators](https://native-instruments.com/ni-tech-manuals/massive-x-manual/en/wavetable-oscillators)). The Native Instruments Massive manual specifically recommends a slow triangle LFO on wavetable position to simulate oscillator drift and add long-form movement ([MusicRadar — How to Master Wavetable Synthesis](https://www.musicradar.com/news/master-wavetable-synthesis)). Multiple modulators on the same position knob — say an LFO plus an envelope plus mod-wheel — give the patch hand-played expressiveness layered onto automated motion.

## Wavetable for Evolving Pad Textures

The classic wavetable pad recipe combines slow position movement with slow filter movement and chorus. Setup: a wavetable oscillator on a smooth morphing table (something like "BasicShapes" or "Vocal Ah-Oh" in Serum), slow LFO (0.1–0.3 Hz) on wavetable position, a second slow LFO (slightly different rate, intentionally desynced) on low-pass filter cutoff, long attack and release on the amp envelope, and stereo chorus on the output ([MusicRadar — How to Master Wavetable Synthesis](https://www.musicradar.com/news/master-wavetable-synthesis)). Adding a second wavetable oscillator detuned by 5–10 cents and panned wide thickens the sound without phase issues. The two LFOs at different rates ensure the patch never repeats — it's the same principle that makes PPG-style "icy pad" patches feel alive across long held notes ([Perfect Circuit — Making Waves: the PPG System](https://www.perfectcircuit.com/signal/ppg-system)).

## Hybrid Synthesis: Wavetable Oscillator → Subtractive Filter

Modern wavetable plugins are almost always **hybrid** — a wavetable oscillator front end feeding a subtractive filter and amp stage. This combines wavetable's harmonic flexibility with the familiar filter movement that defines subtractive sound design ([Native Instruments — Oscillator Section](https://www.native-instruments.com/ni-tech-manuals/massive-manual/en/oscillator-section)). The PPG Wave itself was hybrid: digital wavetable oscillators routed into analog 24 dB/oct VCFs and VCAs, which is part of why its pads sound warm rather than brittle. Serum, Massive, Vital, and the Korg Wavestate all follow this pattern. Practically, this means the standard subtractive vocabulary (cutoff, resonance, envelope amount on filter, LFO on cutoff) still applies; the wavetable just gives you a richer raw material to filter than a static saw or square. A common move: morph the wavetable position from a thin frame to a fat frame while simultaneously opening the filter — the patch transforms in two dimensions at once.

## Phase Distortion and Other FM-Adjacent Techniques

A few synthesis techniques are close relatives of FM and worth distinguishing. **Phase distortion** (Casio CZ series, 1984) bends the read-rate of a sine wave to produce variable-harmonic waveforms with FM-like spectra but different control feel. **Phase modulation** (PM) is what Yamaha's "FM" synths actually do internally — modulating the phase of a sine rather than its frequency — and the audible result is similar enough that the industry calls it all FM ([Yamaha Synth — FM Basics](https://yamahasynth.com/learn/reface/fm-basics-reface/)). **AM (amplitude modulation)** and **ring modulation** modulate the carrier's amplitude rather than its frequency; the sidebands appear at *fc ± fm* (ring mod removes the carrier itself). These techniques live in the same neighborhood as FM and many modern synths (Serum, Bitwig's Polymer, Phase Plant) expose them as additional oscillator-modulation modes worth learning if FM feels too restrictive.

## When to Reach for FM vs. Wavetable vs. Subtractive

A working sound-design heuristic:

- **Subtractive** is fastest for sounds with a clear analog reference — Moog-style basses, 70s pads, brass and string sections, acid lines.
- **FM** is fastest for inharmonic, metallic, glassy, or 80s-Rhodes timbres. It's also strong for FM bass and clavinet sounds where you need bite without much filtering.
- **Wavetable** is fastest for evolving, morphing pads, complex leads with movement built in, and dubstep-style growl basses where the wavetable position itself is the LFO target.

Most modern hybrid synths (Serum, Phase Plant, Massive X, Vital) let you combine all three: wavetable oscillators with optional FM between them, routed into a subtractive filter section. The frameworks aren't competitive — they're complementary tools, and a working producer's toolkit usually includes one of each ([Native Instruments — What is Wavetable Synthesis?](https://blog.native-instruments.com/what-is-wavetable-synthesis/); [Sound on Sound — Synth Secrets series](https://www.soundonsound.com/series/synth-secrets-sound-sound)).

## Cited Retrieval Topics

- "how does fm synthesis work"
- "what's the carrier and modulator in fm"
- "how do i make a dx7 electric piano sound"
- "fm synthesis bell sound ratio"
- "what's an algorithm on the dx7"
- "what is a wavetable"
- "how do i use wavetable position as a modulation target"
- "difference between fm and wavetable synthesis"
- "what does operator feedback do in fm"
- "how do i make an evolving pad in serum"

## Sources

- [Sound on Sound — Synth Secrets series index](https://www.soundonsound.com/series/synth-secrets-sound-sound)
- [Sound on Sound — More On Frequency Modulation](https://www.soundonsound.com/techniques/more-frequency-modulation)
- [Sound on Sound — Synthesizing Bells](https://www.soundonsound.com/techniques/synthesizing-bells)
- [Yamaha Synth — FM Basics](https://yamahasynth.com/learn/reface/fm-basics-reface/)
- [CCRMA Stanford — FM Synthesis](https://ccrma.stanford.edu/guides/planetccrma/FM_synthesis_on.html)
- [Jacob Vosmaer — Yamaha FM Pitch Ratios](https://blog.jacobvosmaer.nl/0050-fm-pitch-ratios/)
- [JonDent — Yamaha DX7 Operators & Algorithms](https://djjondent.blogspot.com/2019/10/yamaha-dx7-algorithms.html)
- [Azure Hills Music — Understanding FM Synthesis on the DX7](https://azurehillsmusic.com/understanding-fm-synthesis-on-the-yamaha-dx7/)
- [Reverb Machine — Exploring the Yamaha DX7](https://reverbmachine.com/blog/exploring-the-yamaha-dx7-pt2/)
- [Wikipedia — Yamaha DX7](https://en.wikipedia.org/wiki/Yamaha_DX7)
- [Wikipedia — Wavetable Synthesis](https://en.wikipedia.org/wiki/Wavetable_synthesis)
- [Attack Magazine — FM Electric Piano](https://www.attackmagazine.com/technique/tutorials/fm-electric-piano/)
- [Pianoo — Yamaha DX7 FM Piano Sound](https://pianoo.com/fm-piano-sound/)
- [RobSonic — Demystifying FM Synthesis](https://robsonic.org/demystifying-fm-synthesis-rich-tones-from-simple-operators/)
- [Native Instruments Blog — What is Wavetable Synthesis?](https://blog.native-instruments.com/what-is-wavetable-synthesis/)
- [Native Instruments — Massive Manual: Oscillator Section](https://www.native-instruments.com/ni-tech-manuals/massive-manual/en/oscillator-section)
- [Native Instruments — Massive X Manual: Wavetable Oscillators](https://native-instruments.com/ni-tech-manuals/massive-x-manual/en/wavetable-oscillators)
- [MusicRadar — How to Master Wavetable Synthesis](https://www.musicradar.com/news/master-wavetable-synthesis)
- [Perfect Circuit — Making Waves: the PPG System](https://www.perfectcircuit.com/signal/ppg-system)
