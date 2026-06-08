# Sampler, Simpler, Drum Rack, and Granulator III

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Simpler, Sampler, Drum Rack, Granulator III; Robert Henke's Granulator III documentation; Ableton Help Center articles on multisampling and slicing; Sound on Sound *Ableton Live 12: Granulator III*
**Tags:** `daw-ableton`, `live-12`, `device`, `sampler`, `simpler`, `drum-rack`, `granulator`, `sampling`

---

## The sampling family at a glance

Live ships four stock devices for playing back audio samples as instruments: **Simpler** (one-sample player, three modes), **Sampler** (full multi-sample instrument with modulation matrix), **Drum Rack** (16-pad-by-default container for sampler instances), and **Granulator III** (granular synthesizer). Simpler and Drum Rack ship with all editions; Sampler is Suite-only. **Granulator III** was [released in 2023 and requires Live 12 Suite](https://roberthenke.com/technology/granulator3.html) — it is *not* the same device as the older Granulator II (Live 9 era, Max for Live Essentials, Robert Henke). Both Granulator versions are still installable from the Ableton Packs page, but Granulator II is unlikely to receive further updates while Granulator III is the actively-developed current instrument. Live 12.1 additionally added a **Drum Sampler** instrument designed specifically for one-shots inside Drum Racks — newer than Simpler in One-Shot mode, with extra features. This file covers the four classic devices; cross-link `corpus/daw/ableton/editing/slicing-audio-to-midi.md` (planned) and `corpus/sampling/chopping-resampling-and-warping.md` for the broader chopping workflow.

## Simpler — three modes that cover most needs

[Simpler](https://www.ableton.com/en/manual/live-instrument-reference/) is Live's lightweight sample player, designed to load a single sample and offer essential controls. It has three modes selected by tabs at the top: **Classic** (the sample plays back as a chromatic instrument across the keyboard with sample-start, loop, filter, envelope, LFO, and velocity controls), **One-Shot** (the sample triggers from start to end on each note, no looping, no key tracking — this is the standard drum-pad / sound-effect mode), and **Slicing** (the sample is automatically chopped into segments and mapped across ascending MIDI notes starting at C1). The three modes share the same waveform display and basic envelopes, but each one optimizes the device for a different job. Simpler is what populates Drum Rack pads by default — drag a sample onto an empty pad and Live creates a chain with a Simpler in One-Shot mode loaded with that sample.

## Simpler's Slicing mode — four detection methods

[Slicing mode](https://www.ableton.com/en/manual/live-instrument-reference/) auto-chops the sample using one of four detection methods: **Transient** (Live's transient analysis detects the strongest hits — higher Sensitivity = more slices), **Beat** (slices at fixed musical divisions, e.g., 1/16 notes — useful for samples already on a tempo grid), **Region** (divides the sample into N equal slices regardless of content), and **Manual** (you place slice markers by hand). Each slice gets a MIDI note starting at C1 and ascending chromatically. The **Playback** chooser sets what happens when a note triggers a slice: One-Shot (play to next slice), Trigger (play to end), or Gate (play while note held). This is the fastest workflow in Live for getting a chopped break or vocal phrase into a playable instrument — drag the sample, click Slice mode, set Transient, done.

## From Simpler Slicing to Drum Rack

The Slicing mode is convenient but limited — every slice shares the same Simpler instance, filter, and envelope. For per-slice processing, right-click Simpler's title bar → **Slice to Drum Rack** (or Slice to New Drum Rack from the waveform context menu). This creates a Drum Rack with each slice on its own pad in its own Simpler instance, [giving independent effects, volume, panning, and tuning per slice](https://www.audeobox.com/learn/ableton/simpler-sampler-complete-guide/). The cost is CPU (16+ Simpler instances vs. one) but the gain is per-slice creative control — pitch one slice down for a sub, distort another for character. In the Drum Rack I/O section, select all pads and set **Choke** to None so overlapping samples (kick, hat, snare from different slices) can play simultaneously without truncating each other.

## Sampler — the full multi-sample instrument

[Sampler](https://www.ableton.com/en/manual/live-instrument-reference/) is Live's multi-zone, fully-modulated sampling instrument — Suite-only, and the device you reach for when Simpler runs out of capability. Sampler has six tabs: **Zone** (key/velocity/sample-select zones with crossfades), **Sample** (per-sample playback parameters, looping, warp), **Pitch/Osc** (a built-in modulator oscillator for AM/FM-style enrichment of the sample), **Filter/Global** (the same five filter circuit models as Wavetable: Clean, OSR, MS2, SMP, PRD), **Modulation** (the routing matrix), and **MIDI** (MIDI control assignments). The Zone tab is what makes Sampler "Sampler" — load a multisampled instrument (e.g., a piano with 88 samples across 8 velocity layers) and Sampler manages which sample plays for which note + velocity + zone. With key/velocity crossfades, transitions between samples are smooth rather than steppy.

## Sampler vs. Simpler — when each fits

A working rule: **Simpler** for chops, one-shots, slicing breaks, and quick playback of a single sample. **Sampler** for multi-sample instruments (real piano, multisampled drums with velocity layers, sustained instruments like strings or pads where pitch-shifting one sample wide across the keyboard sounds wrong), or for any patch that needs the full modulation matrix (multiple LFOs, multiple envelopes, MIDI sidechain to sample-start, polyphonic modulation of loop position). For most beat-making workflows, Simpler is the right pick — it's faster, lighter, and covers 80% of sampling needs. Reach for Sampler when you need realism (a chromatically pitched single sample sounds wrong outside ±5 semitones) or when you want extreme modulation (e.g., sample-start position modulated by LFO for granular-adjacent textures).

## Drum Rack — what it actually is

[Drum Rack](https://www.ableton.com/en/manual/instrument-drum-and-effect-racks/) is a container — not an instrument in itself. It exposes a 4×4 grid of 16 pads at a time but technically holds 128 chains (one per MIDI note). Each pad is a full chain that can contain any instrument (Simpler, Sampler, Operator, a synth, or a third-party VST) followed by any effects. Drag a sample onto an empty pad → Live creates a chain with a Simpler. Drag a folder of samples onto the Drum Rack → Live populates ascending pads with them. Each pad has independent volume, pan, sends, and macro mapping (up to 16 macros on the Rack itself in Live 12). The **I/O** strip on each chain exposes Audio To routing — you can send each pad to its own return / mixer track for parallel processing, sidechain triggering, or independent mix-bus handling.

## Drum Rack workflow tricks

A few patterns worth automatic-pilot:

- **Choke groups** in the chain list let you make hi-hat pads cut each other off (open hat chokes closed hat), modelling real drum behavior. Set Choke to a number — all chains with the same Choke number mutually cut each other.
- **Auto-Select** (small arrow bottom-left of the macro area) makes clicking a pad jump the chain list to that pad — speeds up tweaking.
- **Drag a clip onto a pad** to convert a loop into a one-shot slot — fast way to build a kit from existing audio loops.
- **Right-click a pad → Save** writes the pad's chain (Simpler + effects + macro settings) to the User Library for re-use. Building a personal library of go-to drum chains is one of the most underrated long-term productivity moves in Live.
- **Macro mapping** can target multiple pads' parameters at once — map a global "Snare Tune" macro to every snare pad's Simpler Transpose.

## Granulator III — the Live 12 granular synth

[Granulator III](https://www.soundonsound.com/techniques/ableton-live-12-granulator-iii) released in June 2024 with Live 12 (and updated through Live 12.x), is Robert Henke's complete redesign of the Granulator series. **Important: this is not the same device as Granulator II**, which is the Max for Live Essentials device dating back to Live 9. Both still exist — Granulator II is preserved for project compatibility — but Granulator III is the actively-developed instrument and the one to reach for in new sessions. Granulator III requires Live 12 Suite. The instrument has three grain playback modes: **Classic** (the closest match to Granulator II's behavior — two concurrent grains moving through the sample), **Loop** (a single grain crossfading at loop points, behaves closer to traditional looping sample playback with longer unaltered sections), and **Cloud** (up to 20 non-synced grains per channel, for thick monophonic textures and drones).

## Granulator III parameters and MPE

The instrument exposes streamlined controls: **Position** (where in the source sample grains are generated — formerly "FilePos"), **Scan** (a ramp-based modulator that moves Position automatically), **Grain Size** (2 ms to 2 seconds), **Shape** (grain envelope morphing — sharp percussive grains vs. smooth ones), **Transpose**, **Spread** (stereo detuning between grains), **Variation** (randomization across all grain properties — formerly "Spray" in Granulator II), and **Hold** (sustains the current grain selection indefinitely). The instrument includes dual envelopes, a multi-shape LFO with tempo-sync mode, and **dual SVF filters with nine modes**. **MPE** is first-class — per-note Slide, Pressure, and Note Pitch Bend can modulate any parameter via the matrix. **Capture** mode lets you record audio directly into Granulator III without needing a separate audio track + drag step. Granulator II had FM/AM/noise sections and a dedicated filter envelope; Granulator III deliberately drops these in favor of a cleaner modulation matrix and macro feel.

## Granulator patch-design starting points

**Cloud pad:** Cloud mode, Grain Size ~500 ms, Variation ~30% for natural texture, Shape smooth. Filter LP 24 dB at 4 kHz with slow LFO. Long attack/release on amp envelope. MPE Slide → Position for live "scrubbing" through the source.

**Granular bass:** Classic mode, short Grain Size ~30 ms, Variation low, Transpose -12. Filter LP at 200 Hz. Voice mono. Useful for "broken" bass tones from a melodic source sample.

**Glitch percussion:** Classic mode, very short Grain Size (~10 ms), high Variation (~60%) for randomized hits. Sample = a long vocal or instrumental phrase. Each note triggers a different "shard" of the source.

**Sustained drone:** Loop mode, Grain Size ~1 second, Hold engaged. Sample = a sustained orchestral or vocal note. Drone evolves as Position is automated slowly. MPE Press → Filter cutoff for expression.

## Granulator II vs. Granulator III — when to use which

Granulator II ships as a Max for Live device in [Max for Live Essentials](https://www.ableton.com/en/manual/max-for-live-devices/); Granulator III is a Live 12 Suite-bundled instrument with its own modern installer. Choose **Granulator II** only when: (a) you're opening an old project that already uses it, (b) you need its specific FM/AM/noise sections (which III dropped), or (c) you're on a pre-Live-12 system. Choose **Granulator III** for any new granular work in Live 12 Suite — MPE support, the three-mode design, the Capture workflow, the cleaner modulation matrix, and active maintenance all favor it. Don't mix references between the two when teaching workflow — their parameter names differ (Position vs. FilePos, Variation vs. Spray, etc.).

## CPU and freezing across the family

- **Simpler** is essentially free, even in dozens of instances.
- **Sampler** is mid-cost — multisampled instruments with active modulation matrices can add up. Freeze committed Sampler tracks on busy sessions.
- **Drum Rack** cost scales with the number of active chains. A 16-pad rack with Simpler+effect-stack on every pad is mid-cost; freezing the entire Drum Rack track is the standard move when commit is decided.
- **Granulator III** in Cloud mode with 20 grains and active modulation is the most CPU-hungry device in this family. Freeze aggressively; consider Bounce in Place (Live 12) for fully-committed grains.

## When to reach for which device — quick map

- Single sample, played back across the keyboard chromatically → **Simpler Classic**.
- Drum hit triggered by a MIDI note → **Simpler One-Shot** (default Drum Rack pad).
- Break or vocal phrase to chop and rearrange → **Simpler Slicing** → optionally **Slice to Drum Rack** for per-slice processing.
- Multisampled instrument (piano, strings, multi-velocity drum) → **Sampler**.
- 16-pad drum kit with independent chains → **Drum Rack** (with Simpler or any instrument per pad).
- Granular texture from a sustained source → **Granulator III** (Loop or Cloud mode).
- "Broken" granular percussion → **Granulator III** Classic mode with high Variation.
- One-shot specifically for a drum pad with modern features → **Drum Sampler** (Live 12.1+).

## Cited Retrieval Topics

- "what's the difference between simpler and sampler in ableton"
- "how do i slice a sample in ableton"
- "ableton drum rack basics how to make a kit"
- "granulator iii vs granulator ii ableton"
- "what version did granulator iii come out"
- "how to use sampler for multisample piano in ableton"
- "simpler slicing mode transient beat region manual"
- "ableton drum rack choke groups"
- "best ableton instrument for granular textures"
- "slice to drum rack vs slice to midi ableton"

## Sources

- [Live Instrument Reference — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/live-instrument-reference/)
- [Instrument, Drum and Effect Racks — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/instrument-drum-and-effect-racks/)
- [Robert Henke — Granulator III](https://roberthenke.com/technology/granulator3.html)
- [Ableton Pack — Granulator III](https://www.ableton.com/en/packs/granulator-iii/)
- [Sound on Sound — Ableton Live 12: Granulator III](https://www.soundonsound.com/techniques/ableton-live-12-granulator-iii)
- [Ableton Help Center — How To: Multisampling with Sampler](https://help.ableton.com/hc/en-us/articles/115001318670-How-To-Multisampling-with-Sampler)
- [Audeobox Learn — Ableton Simpler & Sampler Complete Guide](https://www.audeobox.com/learn/ableton/simpler-sampler-complete-guide/)
- [The Drum Broker Blog — Ableton Live 12.1 Drum Sampler](https://thedrumbrokerblog.com/hip-hop-drum-samples/ableton-live-12-1-drum-sampler/)
- [CDM — Robert Henke's Granulator III update for Live 12](https://cdm.link/robert-henkes-granulator-iii-update/)
- [Ableton Reference Manual — Max for Live Devices](https://www.ableton.com/en/manual/max-for-live-devices/)

See also: `corpus/sampling/chopping-resampling-and-warping.md`, `corpus/sampling/loop-based-arrangement.md`, `corpus/rhythm/drum-programming-by-genre.md`, `corpus/daw/ableton/devices/wavetable-drift-meld-synths.md`, `corpus/daw/ableton/editing/slicing-audio-to-midi.md` (planned), `corpus/daw/ableton/timeless/drum-rack-as-multizone-instrument.md` (planned)
