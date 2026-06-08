# Latency and Plugin Delay Compensation in Live

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Mixing, Plug-In Delay Compensation, External Audio Effect, Routing and I/O; Ableton Help Center — Delay Compensation FAQ, Reduced Latency When Monitoring FAQ, Viewing the Latency of a Plugin or Live Device, How to Reduce Latency While Monitoring
**Tags:** `daw-ableton`, `live-12`, `friction`, `latency`, `pdc`, `troubleshooting`

---

## What PDC Actually Does

Per the [Live 12 Mixing manual](https://www.ableton.com/en/live-manual/12/mixing/), Plug-in Delay Compensation (PDC) is the system that delays every track in the Set by the same amount as the longest plug-in latency chain so that all tracks remain in phase at the Main output. If a track has a lookahead limiter that introduces 5 ms of delay, every other track is delayed by 5 ms internally — your kick on track 1 and your snare on track 12 still hit at the same moment at Main, even though one path takes 5 ms longer than the other. PDC is on by default in Live 12 and runs invisibly. It's a separate feature from the Track Delay control; PDC handles plug-in-reported latency automatically, while Track Delay is a manual ±ms knob per track for human/acoustic/hardware misalignment. Per the [Ableton Delay Compensation FAQ](https://help.ableton.com/hc/en-us/articles/209072409-Delay-Compensation-FAQ), PDC is found at `Options → Delay Compensation` and should normally stay on.

## How to See What's Adding Latency

Per the [Ableton article on viewing plugin latency](https://help.ableton.com/hc/en-us/articles/360001820360-Viewing-the-latency-of-a-plugin-or-Live-device), with Delay Compensation on you can hover over a device's title bar to see the reported latency in samples and ms. This is the diagnostic — open a project that feels sluggish, walk the tracks, find the plug-in with the longest latency. Common offenders: brick-wall mastering limiters (lookahead can be 1.5–15 ms), iZotope Ozone and other multi-stage mastering chains (cumulative latency across modules), oversampled EQs and compressors with their oversampling toggled high, convolution reverbs and convolution-based devices. With Delay Compensation off, the per-device latency readout is unavailable — turn it back on to read latency numbers. Per the [Live 12 Mixing manual](https://www.ableton.com/en/live-manual/12/mixing/), Track Delay controls are unavailable when device delay compensation is deactivated, because Track Delay assumes the PDC baseline.

## Reduced Latency When Monitoring — The Tracking Toggle

Per the [Reduced Latency When Monitoring FAQ](https://help.ableton.com/hc/en-us/articles/209072249-Reduced-Latency-When-Monitoring-FAQ), this `Options` menu toggle bypasses PDC for monitored (record-armed or Monitor=In) tracks. The cost is that monitored tracks fall slightly out of sync with the rest of the playback during recording — but the benefit is that input-to-output latency drops to (buffer size + plug-in latency on the monitored track only), instead of (buffer + total PDC across the Set). For a tracking session where the master bus has a heavy mastering chain pushing PDC to 20+ ms, RLWM is the difference between playable and unplayable monitoring. Per Ableton, it's off by default and saved per-Set. It's a temporary toggle: turn on for tracking, turn off for mixing. Per Ableton's note, clicks can occur when arming/disarming with RLWM active because Live recomputes the per-track delay budget on the fly.

## Keep Latency (Live 12+) — Per-Track Recording Compensation

Live 12 added per-track Keep Latency buttons in the mixer. Per [Ableton Drummer's coverage of Keep Latency](https://blog.abletondrummer.com/how-to-use-keep-latency-in-ableton-live-12/), this is a different system from PDC and RLWM — it controls whether Live offsets the *recorded audio after the take* to compensate for round-trip interface latency. With Keep Latency off (default for most use cases), Live measures interface round-trip latency and slides the recorded clip earlier on the timeline by that amount so it lines up with the click the performer heard. With Keep Latency on, Live records the audio as-heard without compensation — appropriate when you're monitoring through external hardware whose own latency you've already aligned in the cue mix and you want the recording to match what the performer experienced. Show the buttons via `View → Mixer Controls → Track Options`. Keep Latency is per-track, not global.

## The Master Bus Lookahead Trap

The single most-common PDC complaint sequence: producer puts an iZotope Ozone or Pro-L mastering chain on Main, the lookahead introduces 5–15 ms of latency, every recording session afterward feels laggy because the entire Set is now delayed by that amount at the input monitor. The producer doesn't recognize the connection because Ozone has been on Main for weeks. The fix is either (1) bypass the master chain during recording (deactivate the device, not just bypass), (2) enable Reduced Latency When Monitoring during tracking, or (3) record into a Set that doesn't have the master chain and import the take. Per [Sound on Sound's coverage of PDC strategy](https://www.soundonsound.com/techniques/practical-techniques-and-strategies-mastering-ableton-lives-delay-compensation), professional Live workflows often keep tracking and mixing in separate Sets specifically to avoid PDC-induced monitoring latency.

## External Audio Effect — Hardware Insert Latency

Per the [Ableton article on external audio effects](https://help.ableton.com/hc/en-us/articles/360005113200-Using-external-audio-effects), the External Audio Effect device sends audio out a configured hardware output, back in a configured hardware input, and inserts the round-trip into the Live signal chain — useful for outboard compressors, hardware reverbs, modular synths used as effects. The Hardware Latency slider lets you tell Live how much *additional* delay the external hardware adds on top of the interface round-trip Live already knows about. If you have a digital reverb that adds 3 ms of internal processing latency, dial in 3 ms; PDC then delays every other track by that 3 ms so the externally-processed track stays in time. The standard calibration: send a click out through the External Audio Effect, record the return, measure the offset against the original click, enter the measured ms in Hardware Latency. Per multiple [user reports on the Ableton forum](https://forum.ableton.com/viewtopic.php?t=167273), uncalibrated External Audio Effect routing is a major source of timing drift on hardware-augmented sessions.

## External Instrument — MIDI Out + Audio In

The External Instrument device is the MIDI-equivalent of External Audio Effect — sends MIDI to external hardware, brings the audio back into Live as a track. Per the [Live 12 manual on External Instrument](https://www.ableton.com/en/manual/instrument-rack-and-drum-rack/), it has the same Hardware Latency slider for the same reason. The trap: the slider only compensates for the audio-return path; the MIDI-out path has its own latency (USB MIDI is typically 1–3 ms, DIN MIDI varies). For a tight hardware synth performance you may need to set Track Delay on the External Instrument track to a small negative value to pre-trigger MIDI ahead of the audio return.

## Group Track Latency Edge Case

Per the [Live 12 manual on Tracks](https://www.ableton.com/en/live-manual/12/grouping-tracks/), Group Tracks aggregate child tracks into a single bus. PDC handles them correctly in the general case, but child tracks with different plug-in latencies inside a Group can produce phase issues if you route audio out of a child track to another track via Audio From — the latency the listening track sees is the child's individual chain latency, not the aggregate Group latency. This is the classic "I sidechain'd my kick to my bass and the duck feels late" report. Live 12 handles most of this transparently, but the only definitive fix when sidechain timing feels wrong is to freeze the source track (the freeze prints the post-PDC alignment) or use Track Delay on the destination.

## Sidechain Compensation

Per the [Live 12 Compressor manual](https://www.ableton.com/en/manual/live-audio-effect-reference/), the Compressor's sidechain input is internally latency-compensated when you select another track as the sidechain source. In practice the Compressor's duck timing matches the source kick's transient regardless of plug-in chain differences between the two tracks. The exception is when the source track has lookahead processing of its own that PDC compensates for downstream — the compressor sees the *unprocessed* source, not the lookahead-processed source. For most ducking-the-bass workflows this is exactly right. The Envelope Follower modulator (Live 12+) follows a different convention: it taps the source track at the configured tap point (Pre FX, Post FX, Post Mixer) and modulates the destination parameter; tap points downstream of lookahead plug-ins will be PDC-compensated.

## How Live Reports Total Latency

Per the [How to Reduce Latency article](https://help.ableton.com/hc/en-us/articles/209072289-How-to-reduce-latency), `Live → Settings → Audio` shows the Overall Latency for the current configuration — input device latency + buffer size + output device latency. This is the round-trip floor. Anything you record arrives that-many-samples-late at Live's input regardless of what PDC does. Live offsets recorded audio backward by this measured amount (unless Keep Latency is on per-track). Driver Error Compensation in Audio Settings lets you fine-tune the offset if recorded takes still feel early or late after Live's automatic correction — record the click against itself through a loopback, measure any offset, enter as Driver Error Compensation. For most modern USB interfaces Live's automatic measurement is accurate to within a few samples.

## The Tracking-Versus-Mixing Discipline

A practical workflow that prevents most PDC headaches. (1) **Tracking sessions:** keep the master bus clean — no lookahead limiters, no Ozone, ideally no plug-ins at all on Main. Use Reduced Latency When Monitoring as belt-and-suspenders. Keep buffer at 128 samples or lower if the interface allows. Hardware monitor through the interface for zero-latency cue. (2) **Mixing sessions:** build the master chain freely. PDC handles everything. Buffer can go to 512 or 1024 samples since you're not tracking. (3) **Hybrid (in-the-box mixing with overdubs):** load the master chain on a deactivated state, enable Reduced Latency When Monitoring during the overdub passes, deactivate the master chain bypass and disable RLWM for the actual mix. This discipline keeps you from chasing 10–20 ms monitoring drift caused by your own mastering chain.

## What Not To Do

A few worth naming. (1) **Don't disable Delay Compensation globally** as a "fix" for monitoring latency — you'll lose phase alignment across the mix and Track Delay controls go inactive. Use Reduced Latency When Monitoring instead. (2) **Don't try to compensate for monitoring latency by dialing in negative Track Delay** on the monitored track — this affects playback as well as recording and breaks alignment elsewhere. (3) **Don't trust a sidechain compressor's timing when the source has lookahead processing upstream** — verify by ear or freeze the source. (4) **Don't run unnecessarily small buffers during mixing** — the interface tax in CPU is real and there's no need for sub-256 samples once you're not tracking. (5) **Don't forget that Keep Latency is per-track and per-Set** — copy a recording template Set to start new tracking sessions with all the latency toggles configured the way you want.

## Cited Retrieval Topics

- "ableton plugin delay compensation explanation"
- "ableton live recording feels late"
- "ableton lookahead limiter monitoring latency"
- "what is reduced latency when monitoring"
- "ableton keep latency vs reduced latency when monitoring"
- "ableton external audio effect hardware latency slider"
- "ableton sidechain ducking feels late"
- "ableton view plugin latency"
- "ableton driver error compensation"
- "ableton tracking session buffer size pdc"

## Sources

- [Ableton Live 12 Reference Manual — Mixing](https://www.ableton.com/en/live-manual/12/mixing/)
- [Ableton Live 12 Reference Manual — Routing and I/O](https://www.ableton.com/en/manual/routing-and-i-o/)
- [Ableton Live 12 Reference Manual — Live Audio Effect Reference](https://www.ableton.com/en/manual/live-audio-effect-reference/)
- [Ableton Live 12 Reference Manual — Grouping Tracks](https://www.ableton.com/en/live-manual/12/grouping-tracks/)
- [Ableton Help Center — Delay Compensation FAQ](https://help.ableton.com/hc/en-us/articles/209072409-Delay-Compensation-FAQ)
- [Ableton Help Center — Reduced Latency When Monitoring FAQ](https://help.ableton.com/hc/en-us/articles/209072249-Reduced-Latency-When-Monitoring-FAQ)
- [Ableton Help Center — Viewing the Latency of a Plugin or Live Device](https://help.ableton.com/hc/en-us/articles/360001820360-Viewing-the-latency-of-a-plugin-or-Live-device)
- [Ableton Help Center — Using External Audio Effects](https://help.ableton.com/hc/en-us/articles/360005113200-Using-external-audio-effects)
- [Ableton Help Center — How to Reduce Latency](https://help.ableton.com/hc/en-us/articles/209072289-How-to-reduce-latency)
- [Ableton Drummer — Keep Latency in Live 12](https://blog.abletondrummer.com/how-to-use-keep-latency-in-ableton-live-12/)
- [Sound on Sound — Practical Strategies for Ableton Live's Delay Compensation](https://www.soundonsound.com/techniques/practical-techniques-and-strategies-mastering-ableton-lives-delay-compensation)

See also: `corpus/daw/ableton/friction/monitoring-loop-fixes.md`, `corpus/daw/ableton/friction/cpu-optimization.md`, `corpus/daw/ableton/workflows/routing-input-output-sends-sidechain.md`, `corpus/recording/signal-flow-and-gain-staging.md`
