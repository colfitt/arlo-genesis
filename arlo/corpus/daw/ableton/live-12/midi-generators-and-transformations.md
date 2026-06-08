# MIDI Generators and Transformations (Live 12)

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** [Live 12 Reference Manual — MIDI Tools](https://www.ableton.com/en/live-manual/12/midi-tools/); [Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/); [All new features in Live 12](https://www.ableton.com/en/live/all-new-features/); [Live 12.1 is Out Now](https://www.ableton.com/en/blog/live-121-is-out-now/); [MIDI Tools and Device Updates FAQ](https://help.ableton.com/hc/en-us/articles/11535349458588-MIDI-Tools-and-Device-Updates-in-Live-12-FAQ)
**Tags:** `daw-ableton`, `live-12`, `live-12-feature`, `midi-generators`, `midi-transformations`, `generative`, `principle`

---

## What MIDI Tools are — and where they live

Live 12 added a MIDI Tools sidebar to the MIDI editor that hosts two families of operations: **Generators** create new notes from scratch, **Transformations** modify existing notes. Both are accessed from the right side of the MIDI editor when a clip is selected (the icons appear in the clip-detail view's sidebar) and operate either on the entire clip or on a selection of notes within it. The [Live 12 Reference Manual MIDI Tools section](https://www.ableton.com/en/live-manual/12/midi-tools/) is the canonical list and behavior reference. The big behavioral choice is the **Auto Apply** toggle: on by default, it shows the result immediately and updates as you change parameters; off, it lets you tweak parameters without overwriting the original notes until you click Apply. Auto Apply off is the safer default for working into a clip you don't want to lose.

## The Generators — what each one does

The current Live 12 Generators set, per the [Live 12 Reference Manual](https://www.ableton.com/en/live-manual/12/midi-tools/), is:

- **Stacks** — adds individual chords or builds chord progressions within the active scale, by scale degree (I, ii, iii, IV, V, vi, vii°, etc.). The scale-degree workflow means changing the project's scale automatically retunes the progression.
- **Rhythm** — generates a note pattern according to the set parameters (density, syncopation, accent), repeated to fill a time selection. Useful for percussion programming and rhythmic toplines.
- **Seed** — randomly generates notes within specified pitch, length, and velocity ranges. Each "seed" value is reproducible — same seed, same notes — so good outputs can be saved and revisited.
- **Shape** — generates a sequence of notes within a pitch range distributed along a defined contour curve (arch, descending, ascending, custom). The melodic-contour generator.
- **Euclidean** — a Max for Live generator that creates notes based on Euclidean rhythms for up to four voices, controlled by step count, fill count, and rotation. Classic Euclidean rhythm tool.

Note that "Arp" appears in the *Transformations* list as **Arpeggiate**, not as a Generator. The C3 row in the original prompt rows speculated about "Arp" as a generator; the current manual lists it as a transformation. Verify against the [Live 12 Reference Manual MIDI Tools page](https://www.ableton.com/en/live-manual/12/midi-tools/) when claiming Arp behavior.

## The Transformations — what each one does

The current Live 12 Transformations list, per the [Live 12 Reference Manual](https://www.ableton.com/en/live-manual/12/midi-tools/):

- **Arpeggiate** — splits a chord or note selection into arpeggiated notes following a chosen pattern (up, down, up-down, random, scale-aware modes).
- **Chop** — divides selected MIDI notes into up to 64 parts. Creates rhythmic subdivisions of held notes.
- **Connect** — generates new notes that fill the gaps between existing notes, with randomized timing/pitch placement. Good for runs and connective phrasing.
- **Ornament** — adds ornamental notes (grace notes, flams) to the start of selected notes.
- **Quantize** — moves or stretches selected notes according to a quantization grid. Live 12's quantize is more flexible than the classic Edit menu version — variable swing, groove-locked quantize, partial quantize.
- **Recombine** — rearranges position, pitch, duration, or velocity for a selection of notes. Shuffle/scramble for melodic exploration.
- **Span** — transforms note durations using three articulation modes: legato, tenuto, and staccato.
- **Strum** — adjusts the start times of notes in a chord following a shape curve set by the Strum parameters. Up-strum, down-strum, custom curves.
- **Time Warp** — transforms note positions according to a speed curve, useful for accelerating or decelerating a passage.
- **Velocity Shaper** — a Max for Live transformation that shapes velocities of selected notes using an adjustable envelope.
- **Glissando** (Live 12.1+, MPE) — connects the pitch of one note to the next along a pitch bend curve. MPE-only.
- **LFO** (Live 12.1+, MPE) — uses an LFO to set the value of one of three MPE parameters (pitch bend, slide, pressure) per note.

The original row referenced "Shape" as a transformation; in the current manual, Shape is a *Generator*. The original row listed "Velocity Shaper" — confirmed. Time Warp is in the list. The list keeps evolving; check C7 (the changelog file) for additions after Live 12.4.

## Destructive apply vs preview

The Auto Apply toggle is the critical decision. With Auto Apply **on**, the moment you pick a Transformation, the clip's notes are rewritten in place — change a parameter, the notes update; pick a different Transformation, the notes change again. This is fast for browsing but means you can lose the original by accident. With Auto Apply **off**, the Transformation runs in preview mode — the notes show the proposed change but the underlying clip data isn't touched until you press the Apply button. The preview mode is the right default for any clip you've spent effort on. Generators behave similarly: Auto Apply off lets you scrub through Seed values or Shape contours before committing. The [MIDI Tools FAQ](https://help.ableton.com/hc/en-us/articles/11535349458588-MIDI-Tools-and-Device-Updates-in-Live-12-FAQ) confirms this and is worth bookmarking for users who lost work to surprise Auto Apply behavior.

## When to reach for Generators vs. Transformations

The mental model is the page on the left of the MIDI Tools sidebar: **Generators** start from nothing (or replace a selection wholesale), **Transformations** take what's there and modify it. If you have an empty clip and want a chord progression, use the Stacks Generator. If you have a chord progression and want it arpeggiated, use the Arpeggiate Transformation. If you have a topline and want a different rhythmic feel, use Recombine or Time Warp. The Generators are often best as a starting point — Seed produces raw material, then Quantize/Span/Recombine refine it. A common workflow is Seed → Quantize → Span → Recombine: random raw notes get snapped to the grid, given articulation, then shuffled into a usable melody.

## Scale-aware behavior — generators that respect the project scale

When the project has a global Scale set (see C2), Generators that produce pitched content honor it. **Stacks** is the obvious case — it generates by scale degree, so the output is always in-scale. **Shape** can be set to constrain its pitch range to scale notes only. **Seed** has a scale-aware mode that limits its random pitches to the active scale. **Euclidean**, being rhythmic, doesn't have scale behavior. **Rhythm** is similarly pitch-agnostic. The scale-degree generation is the workflow shift: before Live 12, generative tools produced chromatic output that needed a Scale device downstream; now they produce in-key output natively. Cross-reference: C2 covers the global Scale model in full.

## When to reach for these vs. the classic MIDI-effects chain

The Live-11-and-earlier generative workflow used MIDI-effect device chains: Scale → Random → Note Length → Arpeggiator → Chord, dropped on a track in front of an instrument. That chain is **real-time and non-destructive** — incoming MIDI gets transformed on the fly, the source notes aren't modified. The Live 12 MIDI Tools workflow is **clip-modifying** — Transformations and Generators write into the clip's note data. The two workflows coexist and have different strengths. Use real-time MIDI effects when you want the same generative behavior across many clips, when you're performing live and need the source MIDI to remain editable, or when the transformation should respond to a controller in real time. Use MIDI Tools when you want concrete, editable notes in the clip that you can hand-tweak afterward. Cross-reference: I11 covers the older MIDI-effect chain workflow.

## Generative patterns the Generators make easy

A few high-leverage generative recipes that the Live 12 Generators make trivial:

- **Random-walk topline** — empty MIDI clip, Seed Generator with a narrow pitch range (one octave), velocity range 80–110, Auto Apply off, scrub the Seed value until something interesting appears, Apply. Add Span (legato) or Connect to soften it.
- **Chord progression from a scale degree string** — set project scale, Stacks Generator with degrees "I vi IV V," chord voicing "triad," Apply. The progression is in-key, and changing the global scale instantly retunes it.
- **Euclidean hat patterns** — empty MIDI clip on a Drum Rack closed-hat pad, Euclidean Generator with steps 16, fill 7, rotation 2 — produces a syncopated 16th-note pattern. Layer with another Euclidean on a different pad with steps 16, fill 5, rotation 5 for polyrhythmic interest.
- **Melodic arch with a contour curve** — Shape Generator with an arch contour, pitch range one octave, 8 notes per bar, scale-locked. Produces a rising-then-falling topline that sits in the key.
- **Scramble-existing-melody for B-section** — selection of notes, Recombine Transformation, rearrange pitches but lock durations. Same rhythm, different melody.

## Cited Retrieval Topics

- "what midi generators ship with ableton live 12"
- "what midi transformations are available in live 12"
- "how do i make a chord progression with the stacks generator in live 12"
- "what's the difference between auto apply on and off in live 12 midi tools"
- "how do i make a euclidean rhythm in live 12 without a third-party plugin"
- "how do i scramble a melody to make a new variation in live 12"
- "what's the difference between midi tools and midi effect devices in live 12"
- "is arpeggiate a generator or transformation in live 12"
- "how do i make a random melody that stays in key in live 12"
- "what does the chop transformation do in live 12"

## Sources

- [Ableton Live 12 Reference Manual — MIDI Tools](https://www.ableton.com/en/live-manual/12/midi-tools/)
- [Ableton — Live 12 Release Notes](https://www.ableton.com/en/release-notes/live-12/)
- [Ableton — All new features in Live 12](https://www.ableton.com/en/live/all-new-features/)
- [Ableton Blog — Live 12.1 is Out Now](https://www.ableton.com/en/blog/live-121-is-out-now/)
- [Ableton Help — MIDI Tools and Device Updates in Live 12 FAQ](https://help.ableton.com/hc/en-us/articles/11535349458588-MIDI-Tools-and-Device-Updates-in-Live-12-FAQ)
- [CDM — Ableton Live 12: a guide to everything that's new](https://cdm.link/ableton-live-12-everything-new/)
- [Sonic Bloom — Ableton Live 12 Announced: New Devices & Features in Depth](https://sonicbloom.net/ableton-live-12-announced-new-devices-features-depth/)

## See also

- `corpus/daw/ableton/live-12/scale-aware-midi-and-global-scale.md` (C2 — the scale model the Generators consume)
- `corpus/daw/ableton/live-12/modulators-shaper-lfo-envelope-follower-note-modulator.md` (C1 — modulator devices vs. MIDI Tools)
- `corpus/daw/ableton/timeless/classic-midi-effect-chains-scale-random-notelength.md` (I11 — the older real-time MIDI-effect generative workflow)
- `corpus/harmony/pop-chord-progressions-by-function.md` (chord progressions by function)
- `corpus/melody/melodic-contour-and-motif-development.md` (melodic contour theory for Shape generator)
- `corpus/rhythm/drum-programming-by-genre.md` (rhythmic patterns to seed Euclidean generation)
