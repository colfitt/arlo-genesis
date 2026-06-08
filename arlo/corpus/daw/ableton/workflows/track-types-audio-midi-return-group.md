# Track Types in Live — Audio, MIDI, Return, Group

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Mixing, Routing and I/O, Live Concepts; Ableton Help Center — Delay Compensation FAQ, Reduced Latency When Monitoring FAQ
**Tags:** `daw-ableton`, `live-12`, `workflow`, `track-types`, `routing`, `principle`

---

## The Five Track Types in Live 12

A Live Set is built from five track types: Audio, MIDI, Return, Main (formerly "Master" before Live 11), and Group. Per the [Ableton Live 12 Mixing manual](https://www.ableton.com/en/manual/mixing/), Audio and MIDI tracks are the only ones that host clips. Group Tracks are summing containers — they cannot hold clips but they have a full mixer strip and can host effects. Return Tracks receive their input from track Sends and cannot hold clips. The Main Track is the final destination for everything; there is exactly one per Set, and it cannot hold clips either. The single rule that organizes all of this: only Audio and MIDI tracks play clips; everything else is a signal-flow container that processes whatever is routed into it. Confusing track type with what a track can do is the most common new-user mistake in Live. The macOS shortcuts to create them: `Cmd-T` (Audio), `Cmd-Shift-T` (MIDI), `Cmd-Option-T` (Return), `Cmd-G` (Group selected tracks).

## Audio Tracks — What They Can Do

Audio tracks accept audio input (from your interface, from another track, from the "Resampling" pseudo-input, or from "No Input"), host audio clips, and run audio devices. Per the [Ableton Live 12 Routing and I/O manual](https://www.ableton.com/en/manual/routing-and-i-o/), the four routing menus per Audio track are Audio From, Monitor (In/Auto/Off), Audio To, and the channel pair. Audio tracks can run instrument racks only if they come after a hosted MIDI source from another track — in practice, Audio tracks for audio, MIDI tracks for instruments. Audio tracks are the only place audio clips live, the only place warped audio is edited, and the only target for "record from another track" workflows (Audio From a track → Monitor In → arm → record). One under-used feature: an Audio track set to Audio From `<another track>`, Monitor In, output `Sends Only`, is a parallel processing bus that can sidechain to its own devices (something a Return track cannot do — see below).

## MIDI Tracks — What They Can Do

MIDI tracks accept MIDI input, host MIDI clips, run MIDI effects, and host one instrument that converts MIDI to audio downstream. The instrument is the conversion point: anything before it sees MIDI, anything after it sees audio. Per the [Ableton manual on working with instruments and effects](https://www.ableton.com/en/manual/working-with-instruments-and-effects/), the In/Out section of a MIDI track shows MIDI From / Monitor / Audio To. There is no Audio From on a MIDI track because the source is the instrument's audio output. MIDI tracks can route their output to other MIDI tracks (sending MIDI through processing chains), or to external MIDI ports. One important constraint per the [Ableton manual on accessing the MIDI output of a VST plug-in](https://help.ableton.com/hc/en-us/articles/209070189-Accessing-the-MIDI-output-of-a-VST-plug-in): "Live merges all MIDI channels to one channel when being routed internally from track to track" — you cannot use separate MIDI channels for separate tracks via internal routing.

## Return Tracks — The Parallel Bus

Return tracks are Live's parallel-effects buses. Every Audio, MIDI, and Group track has a Send knob per Return (labeled A, B, C... by default), and turning a Send sends a portion of that track's audio to the Return for parallel processing. Return tracks can host any audio device — reverbs, delays, parallel compressors, saturators — and the wet output mixes with the dry source on the Main bus. Per the [Live 12 Mixing manual](https://www.ableton.com/en/manual/mixing/), each Return track has a Pre/Post toggle that determines whether the Send taps the track before or after its volume fader. Pre-fader sends are useful for cue mixes and for sends that should be independent of the dry level (a reverb that stays wet when you mute the dry). Post-fader sends (the default) are the normal mixing case where the reverb amount follows the source volume.

## The Return Track Sidechain Limitation

Return tracks cannot be sidechain destinations for plugins on themselves. The reason is architectural: a Compressor's sidechain input pulls from a routing menu that lists Audio and Group tracks but not the Return the device is sitting on, and third-party VSTs with sidechain inputs also can't be addressed from outside a Return per multiple [Ableton forum reports](https://forum.ableton.com/viewtopic.php?t=171229). The workaround is the "pseudo-Return" pattern: instead of a Return track, create an Audio track, set Audio From to the source you want, Monitor In, output to Sends Only or to Main. Now the parallel bus is a regular Audio track and any sidechain destination is reachable. This pattern unlocks parallel compression with kick-fed ducking, sidechained reverb returns, and any other "parallel-bus that responds to a key signal" architecture. The cost is one extra track in the project and slightly more routing thinking; the gain is the full sidechain matrix.

## Group Tracks — Summing and Bus Processing

Group Tracks are summing containers: select N tracks, hit `Cmd-G`, and the selected tracks now live inside a Group with a single mixer strip that sums their output. The Group strip can host any audio device, so this is where drum-bus compression, vocal-bus EQ, and instrument-stem glue compression live. Per the [Live 12 Mixing manual](https://www.ableton.com/en/manual/mixing/), Group Tracks cannot host clips themselves and they cannot be the input of another track's Audio From — but you can route an Audio track to Audio From the Group, and you can sidechain to a Group. Group Tracks accept their own automation. The Unfold button (a triangle on the Group header) shows or hides the contained tracks. Renaming, color-coding, and reordering Groups works exactly like a regular track.

## Nested Groups (Live 11+)

Live 11 added the ability to nest one Group inside another Group, and Live 12 preserves this. Practical use: a `Drums` group containing `Kicks`, `Snares`, `Hats`, `Percs` sub-groups; a `Vocals` group containing `Lead`, `BVs`, `Adlibs` sub-groups. Each sub-group has its own bus processing; the parent group has its own bus processing on top. Per the [Ableton forum on nested groups](https://forum.ableton.com/viewtopic.php?t=250314), nesting depth is limited only by your screen real estate — each level adds header height. Return tracks still cannot be placed inside a Group at any nesting level; this is the longstanding constraint Live users have asked Ableton to lift since Live 10. Drag-and-drop a track into a Group's header area to add it; drag it out to the main track list to remove it without ungrouping the whole.

## The Main Track

Every Live Set has exactly one Main Track (renamed from "Master" in Live 11 and unchanged in Live 12). All Audio, MIDI, Return, and Group tracks default to outputting to Main. The Main strip is where you put the 2-bus chain — Glue Compressor, EQ, Limiter — and the final fader is the project's master level. Per the [Live 12 Mixing manual](https://www.ableton.com/en/manual/mixing/), effects on Main provide "mastering-related functions, such as compression and/or EQ." Main also hosts the Scene Tempo/Time-Signature controls in Session View (Live 12 feature, enabled via `View → Scene Tempo and Time Signature`). The Main track cannot be renamed, deleted, duplicated, or grouped. Its position in the mixer is fixed at the far right. One non-obvious detail: any audio effect on the Main bus contributes to Main's reported latency, and that latency is compensated by Live's [PDC system](https://help.ableton.com/hc/en-us/articles/209072409-Delay-Compensation-FAQ) when monitoring.

## Routing Permutations Worth Knowing

The Audio From / Audio To menus enable several patterns that don't have direct equivalents in Logic or Pro Tools. Audio From another track pulls that track's signal pre-FX (the default) or post-FX (use the `Post FX` sub-option in the chooser). This means you can build a parallel processing chain anywhere: new Audio track → Audio From `Bass`, Post FX → Monitor In → arm → record. Audio To routes the track's output to any destination — including another track's input (so a chain of audio tracks can process in series before hitting Main), a Return track's input directly (rare but legal), or "Sends Only" (signal goes only to whatever Sends are turned up, and doesn't hit Main directly). The [Ableton Live 12 Routing manual](https://www.ableton.com/en/manual/routing-and-i-o/) is the canonical reference.

## Track-Type Gotcha — Resampling

Live exposes a pseudo-input called `Resampling` on every Audio track's Audio From menu. Selecting it makes the track listen to Main's pre-Main-FX output — i.e., whatever the whole mix sounds like before the master bus chain. Arm the track and record, and you've printed a bounce of the current project into a clip on that track. This is the classic Live resampling workflow that predates dedicated bounce features. Live 12 retains it unchanged; the modern alternative is Bounce in Place (see `corpus/daw/ableton/workflows/freeze-flatten-consolidate-bounce.md`). Resampling is still useful when you want a free-running bounce of a session play, or when you want to feed your own master output back into a new track for sound design.

## Latency and Plugin Delay Compensation per Track Type

Per the [Delay Compensation FAQ](https://help.ableton.com/hc/en-us/articles/209072409-Delay-Compensation-FAQ), Live automatically compensates "audio, automation, and modulation by offsetting all tracks by the required amount to keep them in sync with each-other." Delay Compensation is on by default in `Options → Delay Compensation` and should stay on. Group Tracks that contain latency-inducing devices contribute that latency to their parent path; this is normally invisible. Where it bites is during live monitoring of an armed track: per the [Reduced Latency When Monitoring FAQ](https://help.ableton.com/hc/en-us/articles/209072249-Reduced-Latency-When-Monitoring-FAQ), latency on a Group track that the monitored track feeds into is not bypassed by `Reduced Latency When Monitoring`. Live 12 added `Keep Latency` per-track settings exposed via the mixer's Track Options — when set to off, Live compensates for latency even with Monitor set to In or Auto, which fixes MIDI-input latency on instrument tracks that have heavy plugin chains.

## Practical Patterns

A working-default track layout for a Live 12 production: Audio tracks for vocals, guitars, and printed loops, grouped into `Vocals` and `Instruments` Groups. MIDI tracks for drums (Drum Rack), bass, keys, and synths, grouped into a `Drums` Group and a `Synths` Group. Three or four Return tracks: `Short Verb`, `Long Verb`, `Slap Delay`, optionally `Parallel Comp`. Main Track with `Glue Compressor + EQ Eight + Limiter` only. Color-code Groups (red for drums, blue for vocals, purple for synths, green for bass) so the mixer reads at a glance. Use nested Groups when a section has more than five tracks. Never put a Return inside a Group; if you need that pattern, build a pseudo-Return Audio track instead. When sidechaining matters, pseudo-Returns are also the answer.

## Cited Retrieval Topics

- "what's the difference between audio midi return group tracks in ableton"
- "can return tracks be sidechained in ableton live"
- "how do i nest group tracks in ableton 12"
- "ableton group track latency"
- "ableton main track vs master track"
- "how do i route audio from one track to another in ableton"
- "ableton resampling input how does it work"
- "create return track ableton shortcut macos"
- "ableton live 12 keep latency setting"
- "what is sends only in ableton"

## Sources

- [Mixing — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/mixing/)
- [Routing and I/O — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/routing-and-i-o/)
- [Live Concepts — Ableton Reference Manual Version 12](https://www.ableton.com/en/live-manual/12/live-concepts/)
- [Working with Instruments and Effects — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/working-with-instruments-and-effects/)
- [Delay Compensation FAQ — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/209072409-Delay-Compensation-FAQ)
- [Reduced Latency When Monitoring FAQ — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/209072249-Reduced-Latency-When-Monitoring-FAQ)
- [Accessing the MIDI output of a VST plug-in — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/209070189-Accessing-the-MIDI-output-of-a-VST-plug-in)
- [Return-tracks sidechain limitations — Ableton Forum (triangulation)](https://forum.ableton.com/viewtopic.php?t=171229)
- [Nested Groups in Live 11+ — Ableton Forum (triangulation)](https://forum.ableton.com/viewtopic.php?t=250314)

See also: `corpus/mixing/eq-fundamentals.md`, `corpus/recording/signal-flow-and-gain-staging.md`
