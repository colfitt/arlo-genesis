# Why Is My Track Silent — A Diagnostic Flow

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Routing and I/O, Computer Audio Resources and Strategies; Ableton Help Center — Monitoring in Ableton Live FAQ, Plug-ins Tips and Troubleshooting, Reduced Latency When Monitoring FAQ; Sound on Sound — Ableton Live monitoring and routing articles
**Tags:** `daw-ableton`, `live-12`, `friction`, `diagnostic`, `troubleshooting`, `monitoring`, `routing`

---

## The Decision Tree, Top Down

Live has more places a signal can disappear than any other major DAW because the routing matrix is more permissive. The fix is almost always one of seven things, and they form a decision tree. Walk it from top to bottom — earlier checks rule out cheaper failures before you start chasing plugins. Per the [Live 12 Routing and I/O manual](https://www.ableton.com/en/manual/routing-and-i-o/), every track has a four-section I/O strip plus a Monitor radio button, and silence almost always lives in one of those controls. The order: (1) audio device selected and engine on, (2) Main and track volume up, Track Activator on, (3) Monitor state vs. Arm state vs. playback, (4) Audio From / Audio To routing, (5) Mute/Solo and parent Group Track mute, (6) Freeze state and device-disabled state, (7) AU/VST scan failure or sample-rate mismatch. Each level below assumes the prior level has been ruled out.

## Step 1 — Audio Device and Engine

The cheapest checks first. Open `Live → Settings → Audio` (Cmd-Comma) and confirm the Audio Output Device is set to the interface you're actually monitoring through. If you swapped from headphones to monitors, plugged in an interface, or the OS handed audio to AirPods, Live will not auto-follow — its output device is sticky per Set. Confirm the Audio Engine indicator in the top-right of the Control Bar is on; per the [Live 12 Reference Manual](https://www.ableton.com/en/manual/computer-audio-resources-and-strategies/), the Audio Engine can be toggled off with `Cmd-Opt-Shift-E` and will silence the entire Set when off. The CPU Overload Indicator and the Audio Engine indicator live in the same top-right cluster and are easily confused. Cross-check by playing audio in another app (browser, system sounds) — if Live is silent but Spotify isn't, the issue is inside Live, not in macOS or the interface.

## Step 2 — Main, Track Volume, and Track Activator

The Track Activator is the yellow rectangle at the bottom of every track strip. Yellow means active; grey means deactivated, and a deactivated track is silent regardless of every other setting. Click to toggle. Per the [Rapid Flow troubleshooting guide](https://www.rapidflow.shop/blogs/news/no-sound-in-ableton), this catches a surprising number of "track is dead" reports because clicking accidentally during scrolling toggles it. Confirm the track fader is up; faders default to 0 dB but right-click → Reset returns to unity if it drifted to -inf. Confirm the Main track fader (rightmost in the mixer, labeled Main in Live 12; "Master" in Live 11 and earlier) is also up. The Main fader is the one global place to silence everything, and a stray Cue-versus-Main toggle on the Solo/Cue switch can route a track to headphones-only without you noticing.

## Step 3 — The Monitor / Arm / Playback Matrix

This is the single biggest source of "armed track is silent" reports in Live. Per the [Live 12 Routing and I/O manual](https://www.ableton.com/en/manual/routing-and-i-o/), the Monitor radio button has three states: **In** (always monitor the input, clips don't play through), **Auto** (monitor input when track is armed AND no clip is playing; otherwise play clips), and **Off** (never monitor input, only play clips). The trap: a record-armed audio track set to Monitor=Off will record audio you can't hear. A track set to Monitor=In will only play input, not the clip on disk — useful for an "aux" send architecture but confusing when you forgot you set it. Auto is the default and the right choice for almost every recording scenario. Per [LiveKeyboardist's monitor guide](https://livekeyboardist.com/monitorsettings/), if you want to record and hear what you're playing, set Auto and arm the track; the input plays while you record and the clip plays back when you stop.

## Step 4 — Audio From and Audio To Routing

The Audio From and Audio To choosers above the Monitor button decide where the signal arrives from and where it leaves. Per the [Live 12 manual on routing](https://www.ableton.com/en/manual/routing-and-i-o/), Audio From defaults to `Ext. In 1/2` on audio tracks and to `No Input` on MIDI tracks. Audio To defaults to `Main`. Common failure modes: Audio To pointing at `Sends Only` (the track sends to Returns but doesn't reach Main), Audio To pointing at a Return track or another track that itself is muted, Audio From pointing at the wrong interface input (mic plugged into input 3 but track listening to input 1), Audio To pointing at a hardware output bus the interface isn't routing to monitors. The `Sends Only` setting is the most-confusing one — it's not a mute, the meter still moves, the signal just never reaches the Main bus. Cycle through Audio To → Main and meter the Main; if level appears, the routing was the culprit.

## Step 5 — Mute, Solo, and Group Track Cascade

Solo is poisonous in Live because soloing one track implicitly mutes every other track that isn't grouped with it (or marked solo-safe via right-click). If a different track is soloed elsewhere in the project, your "silent" track is being implicitly muted. Per the [Live 12 manual on the Mixer](https://www.ableton.com/en/manual/mixing/), the Solo button is the orange S on each strip. Hold Cmd-click to add to the solo group rather than replace it. The Group Track cascade is the second trap: a track sitting inside a Group whose parent Group Track is muted will be silent even though its own Track Activator is yellow. Look at the parent Group's Activator — and if you've nested Groups (Live 11+ supports nesting), check all parents up the chain. The visual cue is subtle: a child track inside a muted Group shows full-brightness yellow, the parent shows grey.

## Step 6 — Freeze, Disabled Devices, and Crashed Plugins

A frozen track (snowflake icon, `Edit → Freeze Track`) plays the rendered freeze file, not the live device chain. If the freeze was rendered while the track was muted or while a device was deactivated, the freeze captures silence and continues to play silence even after the visual cause is gone. Unfreeze, fix the device state, refreeze. Per the [Ableton Help Center "Committing Audio in Live" article](https://help.ableton.com/hc/en-us/articles/22998838817820-Committing-Audio-in-Live), the freeze file lives in `Samples/Processed/Freeze` inside the project. A device deactivated via its title-bar yellow rectangle is bypassed in the chain — for most effects this just removes processing, but for instruments (Wavetable, Drift, Operator) and for sample-fed devices (Simpler, Sampler) deactivation produces silence. A third-party plugin that crashed mid-session will sometimes silently hang the chain; per the [Plug-ins Tips and Troubleshooting article](https://help.ableton.com/hc/en-us/articles/5232428442002-Plug-ins-Tips-and-Troubleshooting), deactivating and reactivating the device often restores audio without restarting Live.

## Step 7 — Sample-Rate Mismatch and AU/VST Scan Failures

The "everything looks right but nothing plays" tier. If the audio interface sample rate is set to 96 kHz in macOS Audio MIDI Setup but Live is at 48 kHz, the engine will run but audio may silently glitch or drop. Match the rates in `Live → Settings → Audio → In/Out Sample Rate` and Apple's Audio MIDI Setup utility. If the interface was swapped (AirPods to USB interface), Live may have lost the device handle entirely; click the Audio Output Device chooser to confirm the active device. Per the [Live 12 launch-without-plugins instructions](https://help.ableton.com/hc/en-us/articles/10814681680540-How-to-launch-Live-with-third-party-plug-ins-disabled), holding Opt while launching Live boots without scanning plug-ins — useful when a recently installed plugin is suspected of crashing the engine during instantiation. Crashed AU/VST scans can leave a track instrument empty; check the device chain for missing-plugin placeholders.

## External Instrument Latency and Plugin Latency

A subtler silent-track case is the External Instrument device, used to play an external MIDI synth and route its audio back into Live. Per the [Ableton article on external audio effects](https://help.ableton.com/hc/en-us/articles/360005113200-Using-external-audio-effects), the External Audio Effect (and External Instrument) device has a Hardware Latency slider that compensates for round-trip latency. If the MIDI From or Audio To assignments don't match the hardware actually connected, the device passes no audio. Inside-the-box: a lookahead-style plugin (mastering limiter with 5 ms lookahead, brick-wall limiter) introduces delay that Live's Plugin Delay Compensation handles transparently — except on a record-armed monitoring chain, where PDC introduces a noticeable monitoring delay. The fix is **Options → Reduced Latency When Monitoring**, which per the [Reduced Latency When Monitoring FAQ](https://help.ableton.com/hc/en-us/articles/209072249-Reduced-Latency-When-Monitoring-FAQ) bypasses PDC for monitored tracks so playing through plugins doesn't feel sluggish — but does not cause silence.

## The Cue Output Trap (Headphones-Only Routing)

Per the [Live 12 manual on the Cue Out](https://www.ableton.com/en/manual/mixing/), the Cue/Main switch on the Solo button can be set to send soloed tracks to the Cue Out (a separate headphone output) instead of Main. If Cue is selected and the Cue Out is routed to a bus your monitors aren't on, soloing a track sends its audio to the Cue Out only — the Main stays silent, you see meter movement on Main when other tracks play but not on the soloed one. This is the architecture working as designed for DJ pre-listen workflows. To fix: click the Solo/Cue switch to switch back to Solo mode. The switch sits at the top of the Master section in the Session view mixer.

## Send-Only Tracks and Return-Track Silence

Return tracks are a frequent source of "I added reverb and nothing happened." Per the [Live 12 manual on returns](https://www.ableton.com/en/manual/routing-and-i-o/), Return tracks receive signal only from the Sends knobs on other tracks — you cannot Audio From into a Return. If a source track's Send knob to that Return is at zero (or the Return itself has Audio To = Sends Only forming a loop), nothing reaches Main. The Pre/Post switch on each Send (right-click the Send knob → Pre or Post) decides whether the send is taken before or after the track fader; pre-fader Sends keep sending audio even when the source track fader is at -inf. A track with Audio To = Sends Only and zero Sends knobs up is the most silent track you can build in Live.

## The Quick-Triage Checklist

When ARLO is asked "why is my Live track silent," the fastest triage in order: (1) Is the Audio Engine indicator lit? (2) Is the Track Activator yellow and the Main fader up? (3) Is Monitor set to Off on a track you expect to hear input from? (4) Is Audio To set to Main or to a routing that ultimately reaches Main? (5) Is any other track soloed elsewhere in the Set? (6) Is the parent Group Track muted? (7) Is the track frozen with a bad freeze file? (8) Is a device deactivated or showing as missing/orange-error? (9) Did a sample-rate change happen? (10) Holding Opt while launching Live bypasses plugin scan — if Live plays audio there, the problem is plugin instantiation. Run the list in order. The fix is almost always in the first four checks.

## Common Live-Specific Traps Worth Naming

A few worth flagging. (1) **Monitor=Off on a record-armed track** during playback is the most-reported silence cause — you arm to record an external instrument, hear nothing, and assume the routing is wrong; it isn't, Monitor is just Off. (2) **Cue Out on the Master switch** instead of Solo silently steals headphone-routed audio. (3) **Frozen tracks with stale freeze files** — a freeze rendered while a clip was muted plays back silence even after you un-mute the clip; you must unfreeze and refreeze. (4) **Sends Only on Audio To** is often set deliberately for parallel-bus tracks and forgotten about. (5) **MIDI clips on audio tracks and audio clips on MIDI tracks** — Live 12 prevents most of this, but drag-mistakes still happen. (6) **Group Track muted at parent level** while child tracks show yellow Activators. (7) **External Audio Effect** with mismatched hardware routing produces silence with no error. Walk the seven steps and you catch all of these.

## Cited Retrieval Topics

- "why is my track silent in ableton"
- "no sound on armed track ableton live"
- "ableton live track plays but no audio"
- "what does monitor in auto off do in ableton"
- "ableton sends only no main output"
- "ableton live frozen track silent"
- "ableton third party plugin no sound"
- "ableton cue out vs main output silent"
- "ableton group track child muted"
- "ableton sample rate mismatch silent"

## Sources

- [Ableton Live 12 Reference Manual — Routing and I/O](https://www.ableton.com/en/manual/routing-and-i-o/)
- [Ableton Live 12 Reference Manual — Computer Audio Resources and Strategies](https://www.ableton.com/en/manual/computer-audio-resources-and-strategies/)
- [Ableton Live 12 Reference Manual — Mixing](https://www.ableton.com/en/manual/mixing/)
- [Ableton Help Center — Monitoring in Ableton Live FAQ](https://help.ableton.com/hc/en-us/articles/360006569179-Monitoring-in-Ableton-Live-FAQ)
- [Ableton Help Center — Reduced Latency When Monitoring FAQ](https://help.ableton.com/hc/en-us/articles/209072249-Reduced-Latency-When-Monitoring-FAQ)
- [Ableton Help Center — Committing Audio in Live](https://help.ableton.com/hc/en-us/articles/22998838817820-Committing-Audio-in-Live)
- [Ableton Help Center — Plug-ins Tips and Troubleshooting](https://help.ableton.com/hc/en-us/articles/5232428442002-Plug-ins-Tips-and-Troubleshooting)
- [Ableton Help Center — How to launch Live with third-party plug-ins disabled](https://help.ableton.com/hc/en-us/articles/10814681680540-How-to-launch-Live-with-third-party-plug-ins-disabled)
- [Ableton Help Center — Using external audio effects](https://help.ableton.com/hc/en-us/articles/360005113200-Using-external-audio-effects)
- [LiveKeyboardist — Monitor, In, and Off](https://livekeyboardist.com/monitorsettings/)
- [Rapid Flow — No Sound in Ableton](https://www.rapidflow.shop/blogs/news/no-sound-in-ableton)

See also: `corpus/daw/ableton/workflows/routing-input-output-sends-sidechain.md`, `corpus/daw/ableton/workflows/track-types-audio-midi-return-group.md`, `corpus/daw/ableton/friction/monitoring-loop-fixes.md`, `corpus/daw/ableton/friction/latency-pdc-gotchas.md`, `corpus/recording/monitoring-and-headphones.md`
