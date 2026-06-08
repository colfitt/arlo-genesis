# Classic MIDI Effect Chains — Scale, Random, Note Length, Arpeggiator

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** [Live 12 Reference Manual — MIDI Effect Reference](https://www.ableton.com/en/live-manual/12/midi-effect-reference/); [Live 12 Reference Manual — Scale](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#scale); [Live 12 Reference Manual — Arpeggiator](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#arpeggiator); [Live 12 Reference Manual — Note Length](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#note-length); [Live 12 Reference Manual — Chord](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#chord); [Live 12 Reference Manual — MIDI Tools](https://www.ableton.com/en/live-manual/12/midi-tools/)
**Tags:** `daw-ableton`, `live-12`, `daw-ableton-timeless`, `midi-effects`, `generative`, `arpeggiator`, `recipe`

---

## The MIDI effect chain — what it is and where it lives

A **MIDI effect chain** in Live is a series of MIDI-effect devices placed on a MIDI track before its instrument. Incoming MIDI notes — from a controller, from a clip, from another track's routing — pass through the chain in left-to-right order, each device transforming the note stream in real time, before the modified output hits the instrument. The chain lives in the track's Device View when the track is selected, with MIDI effects on the left, the instrument in the middle, audio effects on the right. The classic Live MIDI effects family — Arpeggiator, Chord, Note Length, Pitch, Random, Scale, Velocity — predates Live 12's MIDI Tools sidebar by a decade and remains the right tool for **real-time, performance-oriented MIDI transformation** where the source clip notes stay untouched and the transformation regenerates every time playback hits the clip. The MIDI effects are documented in the [Live 12 Reference Manual MIDI Effect Reference](https://www.ableton.com/en/live-manual/12/midi-effect-reference/); the Live 12 MIDI Tools alternative is the destructive, clip-data-modifying approach covered in the C3 generators-and-transformations file.

## The Scale device — the safety rail of generative MIDI

The **Scale** MIDI effect maps incoming notes onto a chosen scale, forcing any pitch into the nearest scale tone. Its UI is a 12×12 grid where each row represents an incoming pitch class and each column represents an outgoing pitch class — you can edit the mapping by hand or load a preset scale. The device has a **Base** parameter (the root note) and a **Transpose** parameter (semitone shift after scale-mapping). The [Live 12 Reference Manual Scale entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#scale) documents the device. Scale is the foundation of any generative MIDI chain because it converts random/chromatic note streams into in-key output — without a Scale device at the end of the chain, the Random and Arpeggiator devices produce out-of-key output that has to be hand-edited. Drop Scale at the end of the chain (just before the instrument) and the entire generative output is guaranteed in-key. Live 12's project-wide **global Scale** (covered in C2) is a higher-level mechanism that affects more devices, but the Scale MIDI effect remains a per-track tool that overrides or supplements the project scale.

## The Random device — what it does and what it doesn't

The **Random** MIDI effect intercepts notes and randomizes their **pitch** (not velocity) by a controllable amount. Per the [Live 12 Reference Manual Random entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#random), it has four parameters: **Chance** (probability 0–100% that a given note gets randomized), **Choices** (number of possible random pitch offsets), **Scale** (the largest possible offset in semitones, -24 to +24), and **Sign** (positive, negative, or bipolar). Random is most musically useful when paired with a Scale device downstream — Random produces chromatic offsets, Scale snaps them back to the key. The classic generative chain is `Random → Scale → [instrument]` with Random's Scale parameter set to 2–7 semitones and Sign set to bipolar: notes get bumped up or down by a random amount, then quantized to the active key. The result is melodic variation that stays musical. Random alone is useful for occasional pitch wobble (Chance = low, Scale = 1) but for sustained generative melody you almost always want Scale downstream. Cross-reference the I10 velocity-randomization file for the velocity-randomization workflow (which uses the Velocity device, not Random).

## The Note Length device — articulation and stutter

The **Note Length** MIDI effect controls how long incoming notes are held before their note-off is sent. Per the [Live 12 Reference Manual Note Length entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#note-length), it has a **Length** parameter (the held duration, in beat divisions or milliseconds) and a **Sync** toggle. Two surprising uses. First, **trigger on note-off**: an option that flips the device into "fire a note when the input note ends" mode, useful for triggering envelopes or stutter patterns on key-release. Second, **gate-like articulation**: set Length to a short value (1/32 note or 50 ms) to convert held notes into stutters regardless of how long they're played. Drop after Arpeggiator to control how long each arpeggiated note lasts. Drop after Scale to enforce a staccato articulation on an entire MIDI part. Note Length is the unsung hero of generative chains because it controls one parameter no other MIDI effect touches — duration. Random changes pitch, Velocity changes dynamics, Note Length changes how long each note sustains.

## The Arpeggiator device — the workhorse generative tool

The **Arpeggiator** MIDI effect takes held notes (chords) and outputs them as a sequence of single notes following a pattern. Per the [Live 12 Reference Manual Arpeggiator entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#arpeggiator), key parameters: **Style** (Up, Down, Up-Down, Random, Chord Trigger, Converge, Diverge, etc. — defines the pattern), **Rate** (the speed, sync'd to tempo or freely timed), **Gate** (how long each note holds, 1–100% of the rate interval), **Steps** (how many octaves the pattern climbs before repeating), **Distance** (the interval added per step, allowing non-octave climbs), **Hold** (latch — held notes stay arpeggiating after release), and **Velocity** (decay/groove options for the arpeggiated output). Drop Arpeggiator first in the chain to convert chord input into single-note sequences, then transform downstream. The Arpeggiator's Style choices alone produce dramatically different musical outputs — Up is the basic ascending arp, Random is unpredictable, Chord Trigger turns held notes into a rhythmic chord pattern. The device is the foundation of almost every electronic music sound that involves moving single notes from a chord input.

## The Chord device — instant voicings

The **Chord** MIDI effect adds up to six pitch shifts on top of every incoming note, producing a chord from a single input pitch. Per the [Live 12 Reference Manual Chord entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#chord), each shift has a **Semitone** value (-36 to +36 relative to the input) and a **Velocity** scaling. To build a major triad from a single root note: leave shift 1 at 0 (the input), set shift 2 to +4 (major third), set shift 3 to +7 (perfect fifth). Now every input note plays as a triad. Chord stacked before Scale (and before Arpeggiator) produces "arpeggiated chord from a single key" patterns — press one key, hear an in-key arpeggio of the built triad. This is the Live equivalent of the EDM "chord keyboard" patches that turn one finger into a full voicing. The Chord device's six-shift limit caps it at sextad-density chords; for denser voicings, stack two Chord devices in series. Cross-reference [pop-chord-progressions-by-function.md](../../../harmony/pop-chord-progressions-by-function.md) for the harmonic principles.

## The Pitch device — global transposition

The **Pitch** MIDI effect transposes all incoming notes by a fixed semitone amount, with optional **Range** parameters that constrain the output to a specific pitch range (notes outside the range are dropped). Per the [Live 12 Reference Manual Pitch entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#pitch), the Range parameters are useful for limiting an instrument to its playable register — e.g., a bass synth that should only play C1 to C3. Pitch is the simplest MIDI effect, but stacked with the others it does useful things: a Pitch device after Arpeggiator transposes the entire arpeggio up or down by a fixed amount; a Pitch device after Random absorbs Random's wandering range into a controlled window. Use Pitch as the final clean-up device in a chain to make sure output sits in the right register for the destination instrument.

## The canonical generative chain — Scale → Random → Note Length

The classic generative MIDI chain for "in-key melodic random" lives in countless tutorials from 2012–2020. The order: drop a **single sustained input note** (a held MIDI clip on, say, the root), then chain `Random → Scale → Note Length → [instrument]`. Random offsets the input pitch by a random amount each retrigger; Scale snaps it back to the key; Note Length controls the articulation. Adjust Random's Scale parameter for the spread (small = melodic, large = wide), Sign for the direction, Chance for how often it varies. The output is a generative melody that stays in key and follows a consistent articulation. Tom Cosm and Mr. Bill have version-stamped tutorials covering this chain; the underlying mechanism is unchanged in Live 12. The musical caveat: the result is **random**, not **composed** — it's a sketching tool, not a finishing tool. Use it to generate raw material, then bake the output via the [MIDI Tools sidebar](https://www.ableton.com/en/live-manual/12/midi-tools/) Capture or by recording the device output to a new clip, then hand-edit the result into something musical.

## The "constrain the chaos" principle — Scale is the seatbelt

The discipline behind every multi-device MIDI chain is **constrain the randomness with Scale**. Random, Arpeggiator (in Random style), Chord (with weird intervals), and Pitch can all produce chromatic output. Without a Scale device near the end of the chain, that chromatic output hits the instrument and produces atonal mush. The fix is to always end the chain with Scale (or with the project's global Scale enabled in Live 12). When the chain produces output that should be in C minor and you hear wrong notes, the cause is almost always a missing or misconfigured Scale device. The [Live 12 Reference Manual Scale entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#scale) covers configuration. Live 12's global Scale feature (see C2 in this corpus) reduces but doesn't eliminate the need for a per-track Scale — global Scale only affects devices that opt in, so a track-level Scale device is still the safest seatbelt for generative chains.

## Arpeggiator + Random — evolving sequences

A useful pattern beyond the basic generative chain: `Arpeggiator → Random → Scale → [instrument]`, with a held chord as the input. Arpeggiator turns the chord into an in-time sequence; Random adds occasional pitch offsets; Scale keeps it in-key. The result is an arpeggio that occasionally jumps to a related scale tone before snapping back to the pattern — a more interesting output than a fixed arpeggio, but still rhythmically locked. Variation: drop a second Random with low Chance and Scale = 7–12 after the Scale device to occasionally jump octaves, producing sudden register shifts. The chain's strength is that the input is just a held chord — you don't need to write a melody; the chain generates one from the harmony. Useful in performance and in production sketching, but rarely the final part — bake the result and hand-edit.

## When to reach for the classic chain vs. Live 12 MIDI Tools

The classic MIDI effect chain and Live 12's MIDI Tools sidebar overlap in capability but differ fundamentally in **when the transformation happens**. The classic chain is **real-time** — incoming MIDI gets transformed on the fly during playback, the source clip stays untouched, and the output is regenerated every playback (so with Random in the chain, every play of the clip is subtly different). Live 12 MIDI Tools is **clip-data-modifying** — the transformation rewrites the clip's stored note data, the output is deterministic on every replay, and you can hand-edit the result. Use the classic chain when (a) you want generative variation that surprises you across replays, (b) you're performing live and want the source MIDI to remain editable in real time, (c) you want the same generative behavior across many clips on the same track without baking each one, or (d) you're mapping macros to MIDI effect parameters for live morphing. Use MIDI Tools when (a) you want a baked, hand-editable result, (b) you want a one-time transformation rather than ongoing generation, or (c) you want to combine generated material with hand-written notes in the same clip. The [C3 MIDI Generators and Transformations file](../live-12/midi-generators-and-transformations.md) covers the Live 12 side in full.

## Live performance — MIDI-effect racks and macro morphing

The performance-oriented use of MIDI effects is wrapping a chain in a **MIDI Effect Rack** and mapping its eight (or 16 in Live 11+) macros to key parameters across the devices. A typical performance rack: Arpeggiator's Rate on macro 1, Random's Scale on macro 2, Note Length on macro 3, Chord's third-shift Semitone on macro 4, Scale's Base on macro 5. Twist a single macro live and the whole rack morphs — speed up the arp, widen the random spread, change the articulation, modulate the voicing, transpose the key — without touching individual devices. Live 12's Rack expansion to 16 macros makes this even more powerful. Map the macros to a hardware controller (Push, an APC, a generic MIDI controller) and the rack becomes a live-playable generative instrument. The [Live 12 Reference Manual Racks section](https://www.ableton.com/en/live-manual/12/instruments-effects-and-racks/) covers macro mapping. This is Mr. Bill / Ill Gates territory — version-stamped tutorials from 2018+ show the workflow in detail.

## Order matters — chain placement effects

The order of devices in a MIDI effect chain changes the result dramatically. A few principles. **Scale should be last (or near-last)** so it snaps the final output to the key — putting Scale before Random means Random can push notes out of key again. **Arpeggiator first** when the input is chord — Arpeggiator needs the chord notes to arpeggiate; downstream devices then transform the resulting single-note sequence. **Chord before Arpeggiator** if you want every Arpeggiator output to be a chord triggered at that arp step (a chord-trigger pattern). **Note Length late** in the chain so it acts on the final-output note stream — Note Length first then Arpeggiator means Note Length operates on the input notes, not the arpeggio. The default reach for a generative chain: `Chord → Arpeggiator → Random → Note Length → Scale → [instrument]`. Tweak from there based on what you're trying to achieve. The [Live 12 Reference Manual MIDI Effect Reference](https://www.ableton.com/en/live-manual/12/midi-effect-reference/) doesn't prescribe order — that's craft, not documentation.

## Cited Retrieval Topics

- "how do midi effects work in ableton"
- "what is the scale midi effect in live"
- "ableton arpeggiator settings"
- "how do i generate a melody in ableton"
- "ableton chord device tutorial"
- "what order do midi effects go in live"
- "scale random note length chain ableton"
- "midi effects vs midi tools live 12"
- "ableton note length device"
- "midi effect rack macro mapping performance"

## Sources

- [Live 12 Reference Manual — MIDI Effect Reference](https://www.ableton.com/en/live-manual/12/midi-effect-reference/)
- [Live 12 Reference Manual — Scale](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#scale)
- [Live 12 Reference Manual — Arpeggiator](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#arpeggiator)
- [Live 12 Reference Manual — Random](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#random)
- [Live 12 Reference Manual — Note Length](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#note-length)
- [Live 12 Reference Manual — Chord](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#chord)
- [Live 12 Reference Manual — Pitch](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#pitch)
- [Live 12 Reference Manual — MIDI Tools](https://www.ableton.com/en/live-manual/12/midi-tools/)
- [Live 12 Reference Manual — Instruments, Effects and Racks](https://www.ableton.com/en/live-manual/12/instruments-effects-and-racks/)

## See also

- [corpus/daw/ableton/live-12/midi-generators-and-transformations.md](../live-12/midi-generators-and-transformations.md) — the Live 12 alternative (clip-modifying)
- [corpus/daw/ableton/live-12/scale-aware-midi-and-global-scale.md](../live-12/scale-aware-midi-and-global-scale.md) — the global Scale system
- [corpus/daw/ableton/timeless/velocity-randomization-and-humanization.md](./velocity-randomization-and-humanization.md) — Random + Velocity for humanization specifically
- [corpus/harmony/pop-chord-progressions-by-function.md](../../../harmony/pop-chord-progressions-by-function.md) — harmonic principles for the Chord device
- [corpus/melody/melodic-contour-and-motif-development.md](../../../melody/melodic-contour-and-motif-development.md) — melodic principles for generative output
