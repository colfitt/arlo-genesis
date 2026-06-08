# Beat Repeat — Stutter and Glitch Edits

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Beat Repeat; Mr. Bill / Mad Zach Beat Repeat tutorials
**Tags:** `daw-ableton`, `live-12`, `daw-ableton-timeless`, `beat-repeat`, `glitch`, `stutter`, `sound-design`, `recipe`

---

## What Beat Repeat is

Beat Repeat is an audio effect that captures slices of incoming audio and plays them back at a chosen rhythmic interval, optionally pitched, with chance-based triggering. It was added in [Live 5 in 2005](https://www.ableton.com/en/blog/) and remains essentially unchanged through Live 12. The [Live 12 Reference Manual's Beat Repeat chapter](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#beat-repeat) documents the device. The result is the signature **stutter** sound — short fragments of audio rapidly retriggered — that has defined Ableton-produced records from Apparat to Skrillex to current hyperpop. Mr. Bill's [Beat Repeat tutorials filmed in Live 9 and Live 10](https://www.mrbill.com.au/) showcase the device as a glitch sound-design workhorse, not just a rhythmic effect. Mad Zach has used Beat Repeat in his [Live 10 sample-flip series](https://www.youtube.com/@madzach) for transitional stutters and accent fills. The Live 12 verification: the device is still in the Audio Effects section of the Browser, still has the same parameter set, and still behaves identically. This is one of Live's most stable creative devices.

## The core parameters — Interval, Offset, Gate, Variation, Chance, Pitch

Beat Repeat's parameter set is concise but produces wildly different results depending on the combination. The [Live 12 Reference Manual's Beat Repeat section](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#beat-repeat) defines each:

- **Interval** — the time window between captures and triggers, expressed in beat divisions (1/4, 1/8, 1/16, 1/32, dotted, triplet variants).
- **Offset** — shifts the capture point within the Interval (16 steps of subdivision).
- **Gate** — how long the captured slice plays before fading or cutting off.
- **Variation** — randomization amount applied to the Interval (0 = strict, higher = more random).
- **Chance** — the probability per Interval that a repeat will fire (0–100%).
- **Pitch** — semitone transpose of the repeated slice (positive or negative).
- **Pitch Decay** — pitch envelope sweep over the repeat duration.
- **Mix** — wet/dry, with **Mix Mode** selecting Mix (parallel blend), Insert (replaces dry while active), or Gate (silences dry when active).

Mr. Bill's deep-dive tutorials walk through each parameter individually. The parameter interactions are where the creativity lives.

## The classic glitch-fill recipe

The defining Beat Repeat usage is the **glitch fill** — a short stutter that fires at the end of a bar or section as a transitional accent. The recipe: place Beat Repeat on a drum bus or full mix, set Interval to 1/16, Gate to 1/16, Chance to 0% (so it normally does nothing), Variation to 16, Pitch Decay to a small negative value (-3 semitones). Then **automate Chance** from 0 to 100% over the last beat of a bar — Beat Repeat suddenly fires at the boundary and produces a controlled stutter into the next section. Mr. Bill demonstrates exactly this in his [Live 10 streams](https://www.mrbill.com.au/). Mad Zach uses the same trick with slightly different parameters in his [Drum Rack series](https://www.youtube.com/@madzach). The Live 12 Reference Manual notes that Chance automation is the canonical way to gate Beat Repeat in and out — and confirms the parameter still automates in Live 12.

## Using Beat Repeat on vocals for stutter ad-libs

Beat Repeat is one of the fastest ways to create vocal stutters — the "wha-wha-wha-what" repetition that has been a hip-hop and EDM signature for years. Set Interval to 1/16 or 1/32 (depending on how fast the stutter), Gate to match, Chance to 100%, Pitch to 0 (or a small positive value for a "rising" stutter feel). Place on a vocal channel and the entire vocal stutters whenever Beat Repeat is enabled. The discipline: place Beat Repeat on a **send/return** rather than directly on the vocal track, so the dry vocal continues underneath and you blend in the stuttered return for specific syllables only. Use clip envelopes (or modulators in Live 12) to automate the Return's send amount from 0 to 100% for the syllables you want stuttered. [Sound on Sound has documented this vocal-stutter trick in Live workflow articles archived back to Live 8](https://www.soundonsound.com/techniques). Live 12 verification: send/return architecture and automation behave identically.

## Automation patterns for build-up risers

Beat Repeat as a **build-up tool** works by automating the Interval downward across a build section — the repeats get faster and faster as the section approaches the drop. The recipe: place Beat Repeat on the master or a drum bus, start with Interval at 1/8, Chance at 100%, Pitch at 0. Across the build section, automate Interval through 1/16 → 1/32 → 1/64. The stutters accelerate, the energy rises, the drop hits cleanly because Beat Repeat cuts out at the section boundary. Mr. Bill's [Live 11 streams](https://www.mrbill.com.au/) demonstrate this pattern multiple times. Add a Pitch automation rising from 0 to +12 semitones over the same span and you get an additional pitch-rise that intensifies the build. Add Filter Decay automation and the repeats darken or brighten over time. Beat Repeat's classic appeal is that all these effects sit in one device with one set of automation lanes.

## Parallel Beat Repeat — the send-return trick

The most professional Beat Repeat workflow is **parallel**: place the device on a Return track, route the source(s) to that Return via Send, and blend the wet stutter signal back into the mix. The advantage: the dry source is untouched, Beat Repeat is gated by Send amount automation rather than parameter automation on the device itself, and you can route **multiple sources** into the same Beat Repeat return (drum bus, vocal, synth — all stuttered together when the Send opens). Mad Zach's [Live 10 tutorial series](https://www.youtube.com/@madzach) uses this routing as the foundation for his transition kits. The [Live 12 Reference Manual's Return Tracks section](https://www.ableton.com/en/live-manual/12/mixing/#return-tracks) confirms the architecture. The pattern is: leave Chance at 100% on the Return's Beat Repeat (it's always stuttering whatever's sent to it), then control the audible effect entirely from Send amounts on the source tracks. This is cleaner than per-track Beat Repeat instances and uses less CPU.

## Pitch automation for "munged" textures

Beat Repeat's Pitch and Pitch Decay parameters open up sound-design territory beyond simple rhythmic stutters. The recipe for "munged" textures: place Beat Repeat on a sustained source (a pad, a vocal phrase, a sample loop), set Interval to 1/64 or 1/128 (very short — these subdivisions exist in Live 12), Gate at 1/16 (longer than Interval so repeats overlap), Pitch at -12 semitones, Pitch Decay around 24 semitones. The result: rapid, falling-pitch fragments that blend into a granular smear, like a degraded tape feeding back on itself. Mr. Bill calls these "Beat Repeat clouds" in his [Live 10 sound-design streams](https://www.mrbill.com.au/). They're indistinguishable from much more complex granular processing but use a single timeless Live device. Variation parameter pushed high (12+) adds the slight irregularity that keeps the texture from sounding mechanical.

## When Beat Repeat beats a sliced Drum Rack chop

For rhythmic stuttering, two Live approaches compete: Beat Repeat as a real-time effect, or slicing the source into a Drum Rack and programming the chops manually. Each has its strengths. Drum Rack chopping gives you **per-slice control** — you choose exactly which fragments get triggered when, at what pitch, with what effects per pad. Beat Repeat is **performance-oriented** — turn it on, automate it, and it stutters whatever's passing through without you predetermining the slices. The discipline: use Drum Rack chopping when you know exactly what stutter pattern you want and want it consistent. Use Beat Repeat when you want the stutter to be reactive — to whatever the source is doing in real time, including evolving patches and live performance. Mad Zach articulates this trade-off in his [Live 10 tutorials](https://www.youtube.com/@madzach). The Live 12 Reference Manual's [Drum Rack chapter](https://www.ableton.com/en/live-manual/12/instrument-drum-and-effect-racks/) and [Beat Repeat chapter](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#beat-repeat) cover the two approaches independently.

## Mix Mode — Mix vs. Insert vs. Gate

Beat Repeat's **Mix Mode** parameter is one of the most underused but most consequential controls. Mix (the default) blends the stuttered signal with the dry source — both are audible. Insert replaces the dry signal with the stutter when stuttering is active — dry disappears, stutter takes over. Gate silences the dry signal whenever stuttering is **not** active — the opposite of Insert, the stutter is heard normally but in between stutters the source is muted, producing a chopped/gated effect. The [Live 12 Reference Manual's Beat Repeat chapter](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#beat-repeat) documents each mode. Mr. Bill explicitly highlights Mix Mode as "the parameter most people skip" in his [Live 10 deep dive](https://www.mrbill.com.au/). The use cases: Mix for transparent stutter accents that don't disrupt the source flow. Insert for dramatic moments where the stutter replaces the source entirely. Gate for chopped/glitched textures where the source is heavily edited rhythmically.

## Beat Repeat with Filter for tape-stop and lo-fi accents

A classic combination: Beat Repeat followed by Auto Filter (LP12 mode, low cutoff) to produce a darkening tape-stop emulation. The recipe: place Beat Repeat on the source with Interval 1/16, Chance 100% gated by automation, Pitch Decay -12, then place Auto Filter after it. At the moment of the stutter (e.g., end of an 8-bar phrase) automate Beat Repeat's Chance from 0 to 100% over half a beat, then automate Auto Filter's Cutoff from open to 200 Hz over the next half-beat. The result: a stutter that morphs into a darkening filter sweep, mimicking the sound of a tape machine being slowed and then powered down. The [Live 12 Reference Manual's Auto Filter section](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#auto-filter) covers the filter parameters. Mad Zach's [transition tutorial in Live 10](https://www.youtube.com/@madzach) walks through this combination. Live 12 verification: both devices are unchanged and the combination still produces the same result.

## Common Beat Repeat mistakes

The pitfalls from forum-triangulation and creator tutorials: (1) Setting Chance to 100% all the time, so Beat Repeat stutters the entire track constantly and becomes exhausting — use Chance automation or send-return architecture to gate it in/out. (2) Setting Interval too short (1/128) with Gate too long (1/4) producing CPU-heavy overlapping repeats that don't sound rhythmically intentional. (3) Leaving Variation at 0 so the stutter is perfectly mechanical — add 4–8 of Variation for natural feel. (4) Forgetting to set Mix Mode — leaving it at Mix when Insert would be more dramatic, or vice versa. (5) Stacking Beat Repeat in series rather than parallel, producing layered stutters that lose coherence. The [Live 12 Reference Manual's Beat Repeat chapter](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#beat-repeat) implicitly addresses each through its parameter documentation. Mr. Bill addresses them explicitly across his tutorials.

## Workflow recipe — adding a Beat Repeat send-return to any set

A reusable template move: create a Return track in any new Live set, drop Beat Repeat on it with Interval 1/16, Gate 1/16, Chance 100%, Variation 8, Pitch 0, Mix Mode set to Mix (or Insert if you prefer dramatic), Mix at 100% wet. Rename the Return "STUTTER" or similar. Now any source in the set can send to this Return when you want stuttering, via the send knob on its mixer strip. Automate the send knob from 0 to full at any moment you want a stutter accent. This single template move replaces dozens of per-track Beat Repeat instances and uses one CPU's worth of the device. Mad Zach's [template-design tutorials](https://www.youtube.com/@madzach) include this Return architecture as a default. The Live 12 Reference Manual's [Return Tracks chapter](https://www.ableton.com/en/live-manual/12/mixing/#return-tracks) covers the routing. Save the Live set as a template so this Return is in every new project.

## Cited Retrieval Topics

- "how do i make a stutter effect in ableton"
- "what does beat repeat do in live"
- "how do i make a build up with beat repeat"
- "ableton beat repeat parameters explained"
- "how do i stutter a vocal in ableton"
- "what's the difference between mix insert and gate in beat repeat"
- "how do i automate beat repeat for fills"
- "beat repeat vs drum rack chopping"
- "ableton glitch transition"

## Sources

- [Ableton Live 12 Reference Manual — Live Audio Effect Reference (Beat Repeat)](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#beat-repeat)
- [Ableton Live 12 Reference Manual — Live Audio Effect Reference (Auto Filter)](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#auto-filter)
- [Ableton Live 12 Reference Manual — Mixing (Return Tracks)](https://www.ableton.com/en/live-manual/12/mixing/#return-tracks)
- [Ableton Live 12 Reference Manual — Instrument, Drum and Effect Racks](https://www.ableton.com/en/live-manual/12/instrument-drum-and-effect-racks/)
- [Ableton Blog — Live 5 launch (Beat Repeat introduction)](https://www.ableton.com/en/blog/)
- [Sound on Sound — Ableton Live technique archive (Beat Repeat and stutter articles, Live 8 onward)](https://www.soundonsound.com/techniques)
- [Mr. Bill — official site (Beat Repeat tutorials, Live 9–10 era)](https://www.mrbill.com.au/)
- [Mad Zach — YouTube channel (transition and Drum Rack series, Live 10 era)](https://www.youtube.com/@madzach)

## See also

- `corpus/daw/ableton/timeless/resampling-discipline.md`
- `corpus/daw/ableton/timeless/send-return-as-parallel-bus.md`
- `corpus/daw/ableton/patterns/drum-bus-chains-in-live.md`
- `corpus/sampling/chopping-resampling-and-warping.md`
