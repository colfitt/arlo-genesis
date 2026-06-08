https://www.youtube.com/watch?v=rZdrlpz3MOo
YouTube · "How to record Digitakt into Ableton Live via Overbridge 2.0 (Part one)" · Mr Charlie
NOTE: filmed on the ORIGINAL Digitakt (8 tracks shown), but every setup step is identical on the DT2 — only the track count (16, stereo) and channel map (42 inputs) differ. Captured for the workflow, not the track count.

# Distilled transcript — Overbridge → Ableton, dry stems + send-FX

## Connect & enable
- Install the Overbridge plugin from the Elektron site.
- Drag the **Digitakt Overbridge plugin onto a MIDI/instrument track** in Ableton. In the plugin header, **enable "sync clock and transport"** — "this is important, that's what keeps everything synchronized; when you press start/stop in Ableton it will start/stop the Digitakt."
- **Enable Delay Compensation** in the plugin ("make sure delay compensation is selected… now it'll compensate for delay").
- On the hardware: **SETTINGS → SYSTEM → USB CONFIG → select Overbridge.** "It won't work without that — this tells the Digitakt it needs to talk to the Overbridge plug-in via the USB cable."

## Record dry individual tracks
- The plugin appears as an audio source. On each audio track set the **input = Digitakt**, then choose **which track** (all 8 on the OG / all 16 on the DT2) — "you can record all of these simultaneously."
- The **Input** channel records whatever is plugged into the Digitakt's physical inputs (guitar/synth) — "you can use the Digitakt as an audio interface."
- Tip: you can **mute** the plugin's playback (preferred) or **switch it off** in the plugin so playback doesn't double with the live USB stream. Muting keeps the sequence running silently; the presenter prefers muting because the plugin view stays accessible in Ableton.

## The send-FX gotcha (key takeaway)
- Recording an individual track gives you the **DRY** sound — **no delay/reverb**. "On the Digitakt the delay and reverb are **send effects**… each individual track is the dry track."
- To capture a track **with its delay/reverb**, record the **Main/mix output** channel from the plugin (which carries the send FX). The demonstrated method: select the Digitakt's main/"records everything" output, then **mute every track except the one you want**, and record that full output so it includes the echoes/reverb.
- (Part two — not transcribed here — covers recording the FX busses on their own separate tracks. On the DT2 the 3 stereo FX busses are directly addressable in the 42-input Overbridge map; see the Overbridge link file.)

## DT2 deltas vs this OG video
- DT2 = 16 tracks, **stereo** stems (OG = 8 mono).
- DT2 Overbridge map = 42 inputs (Main L/R + 16 stereo tracks + 3 stereo FX busses + line in); default DAW view shows Main + 15 tracks until you reassign outputs in the OB app.
- Same dry-vs-send-FX behaviour applies.
