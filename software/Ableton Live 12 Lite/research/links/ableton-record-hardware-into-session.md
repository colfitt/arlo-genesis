https://help.ableton.com/hc/en-us/articles/209774265-Using-hardware-synthesizers-with-Live
https://www.ableton.com/en/manual/recording-new-clips/
ableton.com (via search) · Ableton (official) · accessed 2026-06-07

# Recording the pedalboard / hardware into Live Session clips

All edition-agnostic — works fully in Lite (within its 8-in/8-out limit). This is
the core of the hardware-front workflow: capture the board/banjo/synths as Session
clips, then perform/loop them.

## Audio path (recording the pedalboard or any audio source)
1. Cable hardware audio out → an input on the **Apollo x8** or **Babyface Pro
   FS**.
2. New **Audio track** (Cmd-T). Set its **Audio From** to that interface input
   (mono or a stereo pair). Set **Monitor** appropriately (Auto / In).
3. **Arm** the track (the Arm/record-enable button). With Auto monitoring + armed,
   input passes through the track's device chain so you hear it live.
4. Record into a **Session clip** (click a clip-slot record button) — capture
   takes as launchable clips, perfect for loop/scene performance.
- Live **auto-compensates round-trip latency** so recordings land tight. Enable
  **"Reduced Latency When Monitoring"** if live monitoring feels laggy.

## MIDI + audio in one track (External Instrument device — for the VG-800/synths)
- The **External Instrument** device lives on a single MIDI track: it sends MIDI
  OUT to the hardware synth and RETURNS its audio into the same track's chain.
- One track does both directions — tidy, and crucial under Lite's 8-track cap.
- Use it to play the VG-800 / OP-1 / Digitakt from Live's MIDI clips while
  monitoring/recording their audio in place.

## Interface routing notes for this rig (8-in/8-out Lite ceiling)
- Lite exposes **8 mono ins / 8 mono outs** — plenty for a few board feeds + a
  stereo synth return, but you can't address all of an Apollo x8's I/O at once.
  Pick the 8 channels that matter (e.g. board L/R, banjo, a synth stereo pair).
- For reamping back OUT to the board, route a track's **Audio To** to an
  interface output feeding the Radial X-Amp → pedalboard, then re-record the wet
  return on another armed track.

## Rig takeaway
Lite is a fully capable capture/looper for the board: arm an audio track on an
interface input, record Session clips, build scenes. The 8 in/out cap is the only
ceiling and it's generous for a front-of-chain hardware rig.
