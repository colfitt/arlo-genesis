https://forum.ableton.com/viewtopic.php?t=205893
https://www.modwiggler.com/forum/viewtopic.php?t=209225
https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/1020319-struggling-keep-hardware-sync-ableton.html
forum.ableton.com / modwiggler / gearspace (via search) · accessed 2026-06-07

# Tightening Live's MIDI clock — the buffer-size + dedicated-port fix

The concrete numbers behind why Live's MIDI sync feels loose and how to make it
acceptable. Edition-agnostic (applies to Lite).

## The buffer-size relationship (the key finding)
- MIDI clock jitter is directly tied to **audio buffer size**. Lower buffer =
  tighter clock.
- Measured: lowering ASIO buffer toward **~3 ms** killed audible sloppiness in
  slaved machines; Elektrons then held to a **max ±0.2 BPM** wobble.
- Practical target: run the project at **64 samples (or less)**. One user on a
  Focusrite 18i20 at 64 samples (≈4.04 ms in/out) got "nearly perfect" sync.
- This needs CPU headroom — so freeze/bounce heavy tracks BEFORE you rely on
  tight clock-out (relevant under Lite, where you'd resample texture tracks to
  audio anyway).

## Dedicated MIDI port for clock
- Don't share the clock port with note/CC traffic — heavy MIDI data adds jitter.
- An **audio interface's built-in MIDI DIN can itself add jitter**; a dedicated
  external MIDI box (or DIN-sync box) is steadier than the interface's MIDI jacks.

## The Elektron-specific tuning step
- In Live, click **EXT** and adjust **Sync Delay** (NOT Track Delay) in prefs to
  align the slaved Elektron to Live's beat.

## When you need it rock-solid
- **E-RM Multiclock** (or similar) clocks the computer + all hardware from one
  master over DIN/analog/USB — the definitive cure for Live's flaky MIDI timing.
  Overkill for drone/ambient, worth it for tight multi-machine rhythmic sets.

## Rig takeaway
For the Digitakt 2 / Octatrack MkII / MPC Sample: run Live at 64-sample buffer,
plug the Elektrons in via a dedicated/DIN path (not a hub, ideally not the
interface's own MIDI jacks if they jitter), set Sync on the clock port only, and
tune Sync Delay with EXT. Expect ±0.2 BPM at best — fine for ambient, add an
E-RM if you need machine-tight grooves.
