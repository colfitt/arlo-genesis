https://www.youtube.com/watch?v=JnbQ8ichm54
True Cuckoo · Octatrack Loopbox (Pickup Machine) Tutorial · 2016-02-21

How to turn the Octatrack into a loop-pedal-style live looper using **Pickup machines**, including the memory gotchas and a hands-free MIDI footswitch rig. This is the most directly rig-relevant Cuckoo video for looping a guitar/banjo/vocal live.

## Setup: a dedicated listening (Thru) channel
- New project: `[FUNC]` + `PROJECT` → CHANGE → CREATE EMPTY PROJECT → name "loop".
- Sources: two mics (piano + vocal) split to a Zoom recorder and into the OT inputs. **A/B** and **C/D** are stereo pairs. **DIR (direct monitor) only works in stereo** — a single mic in input D alone monitors only in the right ear.
- Solution — a permanent listening channel: set **track 7 = THRU machine**. (Double-tap PLAYBACK opens the machine menu; if you're in the sample list, exit and press LEFT to reach the machine list: PICKUP / NEIGHBOR / THRU / FLEX / STATIC.) On the Thru machine choose the input: `C` (right only), `C+D` (both summed to **mono**), or `D` (D only mono). He picks **C+D** to fold both mics to mono. A Thru track only passes audio while it's *playing* — press-and-hold track 7 + play to keep it on; double-tap STOP mutes all channels (and the input monitor).
- Gain each input in the MIXER until levels are healthy (he lands ~+30 on the mic). Leave DIR off (it would force stereo).

## Recording-level gotcha (critical)
- The **listening/Thru channel volume = the level that gets recorded**, NOT what DIR monitoring suggests. He records something deafeningly loud because input GAIN was high while the listening channel was low. Fix: turn the **listening channel up to max** to hear the true record level, then tune input GAIN down in the mixer (he ends ~20).

## Recording settings for a looper
- `[FUNC]` + `[REC]` opens the recording-setup page; the other rec page has more.
- INAB = OFF, INCD = **C** (just that mic), RECORDING LENGTH = MAX.
- **TRIG = 1 2** (the important one): with this, REC1 starts recording, REC1 again sets the loop length but keeps recording (overdub), and REC2 stops/sets length.
- Other page: QUANTIZE RECORDING = OFF, **QUANTIZE PLAYBACK = PATTERN LENGTH** (this is what keeps loops synced).

## The Pickup machine + the two REC buttons
- Double-tap PLAYBACK on track 1 → set machine to **PICKUP** (the loop box).
- Two record buttons with overlapping jobs:
  - **REC1** = start recording.
  - **REC1 again** = set the loop length but **keep recording** (overdub mode).
  - **REC2** = continue *playing* the loop.
- **Avoiding clicks:** press **REC1 first**, then REC1 again to set length while still recording, then REC2 to keep playing. Setting length with REC2 directly cuts a ringing tone off hard → audible click. So: REC1 to start → REC1 to set-length-and-overdub → REC2 to lock the loop playing.
- **Triple-tap REC1 = record while ERASING** the existing buffer (a long-echo / wipe behavior). The on-screen icon shows a **plus (recording)** vs an **X (recording-while-erasing)**.

## Master / slave loops + length multiplier
- Set up track 2 as a second Pickup machine (INCD = C). **The first track you record becomes the MASTER; tracks 2, 3... are SLAVES synced to it.** The master is shown by two top pixels / a stripe in its display. Stop and restart a slave loop and it re-enters in sync.
- The Pickup machine has a **length factor (X)**: X1 = default master length, **X2 = twice as long** (record a 2-bar vocal over a 1-bar piano loop). Recording on a slave mid-bar still lands in sync because QUANTIZE PLAYBACK = PATTERN LENGTH. Two play-head arrows show: the second arrow = the track currently recording.
- Tempo is set/adjusted **on the fly** by the first loop (he lands at 140 BPM); the looper does not need the timeline running at all.

## MEMORY: reserve length (the thing that bites everyone)
- Pickup loops live in **RAM** and cannot exceed reserved memory → "RECORDING MEMORY FULL." Default reserve is **16 s**.
- Fix: `[FUNC]` + `PROJECT` → SYSTEM → MEMORY (a bar shows usage). Raise **RESERVE LENGTH** (he sets **40 s**) → `YES`. Warning: "playback will be stopped, unsaved record buffers will be lost" — `YES`. The OT resizes the buffer files. Do this *before* a long-loop session.

## Mixing a pre-made loop in (Flex + timeline sync)
- Load a drum loop: track 5 → FLEX machine → press RIGHT into the slot list → select a slot → RIGHT to browse the card → `YES` to load (`[FUNC]` + `YES` previews while browsing).
- Pickup loops ignore the timeline, but a Flex loop needs the **timeline** to start on the downbeat. Tempo is already synced; to start the timeline locked to a loop: hold the master Pickup track + `[TEMPO]` to **SYNC TO** that pickup, then play — the timeline starts in sync, and you can trigger the Flex loop in time.

## Freeze-delay vocal trick (on the Thru channel)
- On track 7's FX2 = **delay**, double-tap → turn **LOCK ON**. When **SEND = 0** the delay freezes/locks its buffer and loops it on the feedback; crank **FEEDBACK** to max to sustain. While it loops you can change the delay **TIME** for pitch/rhythm play.
- Live-control it via **DELAY CONTROL** keyboard mode: `[FUNC]` + down → DELAY CONTROL; with GRID off, keys 9–16 map to tracks with a locked delay, letting you ride the delay time per track live. "Use it with a subtle touch."

## Hands-free: MIDI footswitch
- A USB footswitch → USB-to-MIDI host (he uses a Sebble/Mode Machine USB host powered by a USB power bank) → MIDI into the OT. Maps: note **60 (C)** = record, note **64 (E)** = play/next, and a middle switch = **SYNC TO TEMPO** of the record buffer.
- The footswitch controls the **active track** via the OT's AUTO CHANNEL — set it in `[FUNC]` + `PROJECT` → MIDI → CHANNELS → AUTO CHANNEL (match the footswitch's MIDI channel, he used 9).
- Once the timeline has started, the "play" footswitch gains double-duty (waits, then triggers) — so it both loops and launches the timeline.
- To slave other gear: `[FUNC]` + `PROJECT` → MIDI → SYNC → send CLOCK + TRANSPORT so external devices follow the looper's tempo.

## Rig relevance
This is the blueprint for live-looping the banjo/baritone through the OT: a Thru listening channel folding the pedalboard print or a mic to mono, Pickup machines with TRIG=1 2 and QUANTIZE PLAYBACK = PATTERN LENGTH for clean overdubs, RESERVE LENGTH bumped to 40 s+ for long drone loops, and a MIDI footswitch so both hands stay on the guitar. The freeze-delay vocal trick is the "capture a fragment and sustain it" move applied to a played phrase.
