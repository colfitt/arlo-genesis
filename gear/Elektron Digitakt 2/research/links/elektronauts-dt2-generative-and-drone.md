Sources (two threads):
https://www.elektronauts.com/t/share-your-ideas-for-random-generative-processes-on-the-dt-2/217473
https://www.elektronauts.com/t/drowned-for-digitakt-ii-drone-preset-pack/220614
elektronauts.com · community threads · 2024

# Digitakt II — Generative / Random Processes & Drone Recipes

The most rig-relevant facet: evolving, never-quite-repeating patterns and drone construction. Two threads distilled.

## Generative / random thread (DT2-era)
- **LFO → Sample Slot for random sequences** (djadonis206). Load a bank/track with several percussion (or texture) samples, scatter trigs, then assign an LFO to the SAMPLE SLOT destination. The LFO walks through sample slots so each pass plays a different sample on each step → random sequences/melodies/ideas. Pair a RANDOM LFO waveform for true unpredictability.
- **Sample chain on GRID machine + random LFO → grid slot** (bibenu). Build a sample chain, load it into the GRID machine, then drive the grid-slice position with a random LFO. Add "random pitches" via a "not-very-careful p-locked twist of the note encoder."
- Cross-ref: trig conditions (percentage probability, X:Y ratios, NEI neighbor, FILL, LAST/NOT-LAST) layered on top of the above are the standard way to keep a 4-bar loop from repeating for 16+ bars.

## DROWNED! drone preset pack — creator's actual method (the gold)
The pack author spells out the DT2 drone technique (verbatim):

> "all LFO work on DTII is either slow LFOs modulating Filter and sometimes Pitch to make them evolve for even longer periods of time, or Random LFOs with slow Slews to add some unpredictability."

More from the creator:
- Source samples are "seamless loops" with "a slowly evolving character baked into them already" — i.e. start with already-moving loops, then add slow modulation on top, don't rely on the synth engine to create all the motion.
- Presets "make heavy use of DTII's 3 LFOs per track."
- "Some presets use [the] Comb Filter of DTII" for metallic/resonant motion.
- Source samples "have some stereo content" — feed the stereo engine real stereo material.
- Philosophy: "the pack's real character comes from the source samples, and the DTII work done on top of them is only one way to skin a cat."

## Practical drone recipe for THIS rig (synthesized from the above)
1. Sample a long, sustained baritone/fuzz-wall or banjo-drone print (stereo, post-board) as a seamless-ish loop.
2. STRETCH or GRID machine, single held trig over a 128-step pattern.
3. LFO1: slow triangle → FILTER cutoff. LFO2: slow → PITCH (tiny depth) for drift. LFO3: RANDOM waveform + slow SLEW → filter or sample-start for unpredictability.
4. Comb+ filter (key-tracked) for shimmer/metallic motion when wanted.
5. Heavy Supervoid Reverb send; chorus + reverb in parallel rather than chorus→reverb (avoids the mono-collapse — see send-FX file).
6. Print to the Apollo, or route the single track over USB/Main back into the texture boards (Microcosm / H90 / Chroma Console).

NOTE: the generative thread itself was light on numeric values (it points to EZBOT's "Generative Sample Chains" video — captured separately in transcripts/). The DROWNED creator quotes are the most concrete drone guidance found in the community.
