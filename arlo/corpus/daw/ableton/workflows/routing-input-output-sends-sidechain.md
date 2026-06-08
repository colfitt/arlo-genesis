# Routing in Ableton Live — Input, Output, Sends, Sidechain

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Routing and I/O, Mixing; Ableton Help Center — Setting up a virtual MIDI bus, Using external audio effects, Sidechaining a third-party plug-in
**Tags:** `daw-ableton`, `live-12`, `workflow`, `routing`, `sidechain`, `principle`

---

## The Four Routing Menus, Stated Once

Per the [Ableton Live 12 Routing and I/O manual](https://www.ableton.com/en/manual/routing-and-i-o/), every clip-hosting track has four routing menus stacked in the I/O section: Audio/MIDI From (input), Monitor (In/Auto/Off), Audio/MIDI To (output), and the destination channel chooser below. The I/O section is hidden by default; show it with `Cmd-Option-I` on macOS or via the mixer view triangle at the bottom-right of the Live window. Return tracks have only the output pair (input comes from Sends). The Main Track has only the output pair (to your audio interface or to an export). Memorize the position: From-and-Monitor on top, To-and-channel on the bottom. This stays constant whether you're in Session or Arrangement, and the menus behave identically regardless of view. Most Live routing confusion is people looking at the wrong menu — the To menu is on the bottom, not the top, and the channel below it changes meaning depending on which destination you pick.

## Audio From — Where Audio Tracks Get Their Signal

For an Audio track, the Audio From menu picks the source. Choices per the [Live 12 manual](https://www.ableton.com/en/manual/routing-and-i-o/) include `Ext. In` (your audio interface inputs, with the channel chooser below selecting 1/2, 3/4, mono channels, etc.), `Resampling` (the pre-Main-FX mix of the whole project), `No Input`, or any other track in the project. When you pick another track as the source, the channel chooser below offers `Pre FX`, `Post FX`, and `Post Mixer` — three tap points along that source track's signal path. Pre FX takes the dry signal before any devices. Post FX takes the wet signal after devices but before the fader. Post Mixer takes the signal after the fader, after volume and pan. This three-tap structure is the basis of every internal routing trick in Live: parallel processing chains, sidechain key signals, sub-bus printing, re-amping a track through guitar pedals on a parallel path.

## Monitor — In / Auto / Off

The Monitor menu has three states with precise behaviors per the [Live 12 Routing manual](https://www.ableton.com/en/manual/routing-and-i-o/). `Auto` (the default) monitors the input only when the track is armed and not playing a clip — this is the right state for normal tracking. `In` monitors permanently regardless of arm or playback; per the manual, "this setting effectively turns the track into what is called an 'Aux' on some systems," which is exactly the pattern needed for a parallel processing bus that pulls from another track. `Off` never monitors; useful when you're tracking with external monitoring or when you want a clip to play back unaffected by the live input. The Monitor setting interacts with the new Live 12 `Keep Latency` per-track option exposed in the mixer's Track Options — when Monitor is In and Keep Latency is off, Live compensates for plugin delay through the monitored chain.

## Audio To — Where the Track Output Goes

The Audio To menu sets the destination. Default is `Main`, which sends to the Main Track. You can route to your interface outputs directly (`Ext. Out` plus a channel pair below), to another track's input (any Audio or Group track in the project), to a Return track's input directly, or to `Sends Only`. `Sends Only` is the special case: the track's main output is muted to Main, and signal only reaches the Master via whichever Returns you've turned up Sends to. This is how you build a wet-only effect bus (audio goes to a reverb Return, which mixes to Main, but the dry source never hits Main itself), or a stem-printing track that only feeds a specific submix. Routing a track to another track's input means the destination track must have Monitor In (or be armed and playing) for the audio to pass through.

## MIDI From and MIDI To

On MIDI tracks, the From and To menus carry MIDI rather than audio. MIDI From defaults to `All Ins` — all enabled MIDI input ports plus the computer keyboard. You can constrain to one source, one channel, or another MIDI track's output (so a MIDI track's clip can drive an instrument on a different track). MIDI To defaults to `No Output` if the track has an instrument (because the audio output is what matters then) or to whichever destination you set explicitly. To send MIDI to a hardware synth, pick the MIDI port in the To menu and the channel below. To send MIDI to another track's instrument, pick that track and the channel `Track In`. Per the [Ableton Help Center](https://help.ableton.com/hc/en-us/articles/209070189-Accessing-the-MIDI-output-of-a-VST-plug-in), "Live merges all MIDI channels to one channel when being routed internally from track to track" — internal MIDI routing collapses to a single channel, which matters when you're driving a multitimbral plugin and expected to split by MIDI channel.

## Send-and-Return Architecture

Send knobs live on every Audio, MIDI, and Group track, one per Return Track. Turning a Send routes a copy of that track's signal to the Return for parallel processing. The Return's effects (reverb, delay, parallel compressor) wet up the source, and the Return's own fader controls how much wet returns to Main. Per the [Live 12 Mixing manual](https://www.ableton.com/en/manual/mixing/), each Return's Send has a Pre/Post toggle visible in the mixer's expanded view: Pre taps before the source's volume fader (cue mixes, send-amount independent of dry level), Post taps after (the default; reverb amount follows source volume). A working starter configuration: Return A = Short Plate Reverb (Hybrid Reverb on a short plate IR), Return B = Long Hall Reverb, Return C = 1/8th-note Slap Delay (the unified Delay with Modulation off), Return D = Parallel Compression bus (Glue Comp pinned at -8 dB GR for vocal/drum glue).

## Sidechain Routing — The Classic Way

Almost every Live dynamic device has a Sidechain section, revealed by clicking the arrow at the top-left of the device. Inside, enable the Sidechain switch and pick a source in the Audio From chooser. Per the [Live 12 Compressor reference](https://www.ableton.com/en/manual/routing-and-i-o/) and confirmed by [tutorials on Live 12 sidechain workflow](https://magneticmag.com/2025/12/sidechaining-in-ableton-12/), the source picker offers any track or Group, with a Pre FX / Post FX / Post Mixer tap point chooser identical to the main Audio From menu. The Sidechain EQ section above filters the key signal — useful for keying off only the low fundamental of a kick (HPF off, peak at 60 Hz) rather than the whole kick spectrum. The classic ducking move is Compressor with sidechain Audio From `Kick`, Pre FX, ratio 4:1, threshold low enough to hit on every kick, fast attack, release tuned to 1/16th or 1/8th of the bar. The Live 12 update to sidechain UI (improved visual feedback per [Icon Collective's Live 12 sidechain guide](https://www.iconcollective.edu/sidechaining-in-ableton-12-a-comprehensive-guide)) didn't change the routing — just the readability.

## Sidechaining Third-Party Plugins

Per the [Ableton Help Center on sidechaining third-party plug-ins](https://help.ableton.com/hc/en-us/articles/209775325-Sidechaining-a-third-party-plug-in), Live does not expose third-party VST/AU sidechain inputs in the same Sidechain section as stock devices. The workaround is the Audio To routing trick: on the key-signal track (e.g., the kick), set Audio To to the track containing the third-party plugin, and pick the plugin's sidechain channel in the channel chooser below. The plugin must expose its sidechain as a separate channel pair for this to work — most modern compressors do, including FabFilter Pro-C2, Pro-MB, Waves SSL G-Master, and similar. For older plugins without a dedicated sidechain input pair, no workaround exists in Live; you either find a stock-device equivalent or use the [Envelope Follower modulator](https://www.ableton.com/en/manual/modulators/) (Live 12+) on the destination parameter directly.

## External Hardware — Insert and Return Architectures

Per the [Ableton Help Center on external audio effects](https://help.ableton.com/hc/en-us/articles/360005113200-Using-external-audio-effects), the External Audio Effect device (Live Standard and Suite only) acts as a hardware insert. Drop it in a device chain at the point you want hardware processing, set the device's output channels to the interface outputs that go to the hardware, set the input channels to the interface inputs that return from the hardware, and Live routes a round-trip. The device's Latency control lets you nudge for the analog round-trip delay; Live's PDC handles the rest. For hardware on a Return Track (a hardware reverb on Return B, for example), the same External Audio Effect goes on that Return. For external instruments — MIDI out plus audio in — use the External Instrument device on a MIDI track: it sends MIDI out one of the interface's MIDI ports and pulls audio back from a specified input pair, with the MIDI track's audio output behaving as if the hardware were a virtual instrument.

## Virtual MIDI on macOS — The IAC Driver

Per the [Ableton Help Center on virtual MIDI buses](https://help.ableton.com/hc/en-us/articles/209774225-Setting-up-a-virtual-MIDI-bus), macOS ships with the IAC (Inter-Application Communication) Driver as part of Audio MIDI Setup. Open Audio MIDI Setup, `Window → Show MIDI Studio`, double-click the IAC Driver, check "Device is online," and click + to add as many virtual buses as you need. Each bus appears as a MIDI port in Live's `Preferences → Link, Tempo & MIDI` pane. Enable Track In, Track Out, Sync, or Remote per bus as needed. Practical uses: route MIDI from Live to another DAW or to a standalone instrument app like Ableton's own Note iOS app, route MIDI from a hardware controller routing app (Bome MIDI Translator, Kosmonaut) into Live, or split MIDI inside Live to drive a slave plugin host. Restart any DAW that was open before you added new IAC ports — most apps only scan MIDI devices at launch.

## Resampling and Sends-Only Bus Patterns

The `Resampling` input plus the `Sends Only` output, used together on a new Audio track, build a "tap and parallel-process the whole project" bus. Set Audio From to Resampling, Audio To to Main (not Sends Only — Resampling already taps everything), Monitor Off, and drop devices on the track. Arm to record a bounce of the project including those devices. Alternatively, use `Sends Only` on a regular source track to feed a Return chain without sending the dry signal to Main — useful when you want a vocal to live entirely in its plate reverb rather than appearing dry in the mix at all. Per the [Sound on Sound external-audio article](https://www.soundonsound.com/techniques/using-external-audio-ableton-live), this is the same pattern used to route audio to outboard hardware that doesn't have a dry/wet on its own.

## Live 12 Routing — What's New, What Isn't

Live 12 did not overhaul the routing model. The four-menu structure is unchanged from Live 11. What did change: the Sidechain sections on stock dynamics devices got a UI refresh with clearer source displays and an integrated meter for the key signal, the `Keep Latency` per-track option appeared in the mixer's Track Options for monitoring-latency control, and the new Envelope Follower modulator (Live 12+, see [Modulators manual](https://www.ableton.com/en/manual/modulators/)) gave an alternative to traditional sidechain compression — instead of routing a key signal into a Compressor, you place an Envelope Follower modulator on the track and map it to any parameter (a volume, a filter cutoff, a Send level). For classic ducking the Compressor sidechain is still typically the right tool; for creative modulation the new modulators are usually cleaner.

## Cited Retrieval Topics

- "how do i route audio between tracks in ableton 12"
- "ableton live sidechain compressor setup"
- "what does sends only mean in ableton live"
- "ableton resampling how to use"
- "ableton hardware insert external audio effect"
- "macos iac driver ableton midi routing"
- "what does pre fx post fx mean in ableton routing"
- "ableton third party plugin sidechain not working"
- "ableton live 12 keep latency setting"
- "how do i send midi between tracks in ableton"

## Sources

- [Routing and I/O — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/routing-and-i-o/)
- [Mixing — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/mixing/)
- [Modulators — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/modulators/)
- [Setting up a virtual MIDI bus — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/209774225-Setting-up-a-virtual-MIDI-bus)
- [Using external audio effects — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/360005113200-Using-external-audio-effects)
- [Sidechaining a third-party plug-in — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/209775325-Sidechaining-a-third-party-plug-in)
- [Accessing the MIDI output of a VST plug-in — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/209070189-Accessing-the-MIDI-output-of-a-VST-plug-in)
- [Using External Audio In Ableton Live — Sound on Sound](https://www.soundonsound.com/techniques/using-external-audio-ableton-live)
- [Sidechaining in Ableton 12: A Creative Guide — Magnetic Magazine](https://magneticmag.com/2025/12/sidechaining-in-ableton-12/)
- [Sidechaining in Ableton 12: A Comprehensive Guide — Icon Collective](https://www.iconcollective.edu/sidechaining-in-ableton-12-a-comprehensive-guide)

See also: `corpus/mixing/compression-fundamentals.md`, `corpus/rhythm/kick-bass-relationship.md`, `corpus/recording/signal-flow-and-gain-staging.md`
