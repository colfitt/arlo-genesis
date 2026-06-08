https://op-forums.com/t/op1-field-workflows-tips-tricks/24567
op-forums.com (op1.fun community) · multiple users (abyssody, scy1e, opsr, Heyes, Open_Bar) · Field-specific workflow thread

The dedicated OP-1 **Field** workflows thread — the one place where tips are confirmed against the Field's stereo path, 8 tapes, USB-C, and BLE MIDI rather than the OG. Highest-signal items:

## Tape / recording (rig-relevant)
- **Shift+Orange sets the PAN for recording to the tape track** (abyssody). Lets you record a mono source hard-panned L or R to effectively double your track count — Heyes demos this with mono guitars. DIRECTLY useful here: record the baritone/banjo (mono) panned hard left to one track, a second pass hard right, and you've got a wide stereo double out of two mono takes.
- **Reel fill indicator:** the reel selector shows a red fill = tape usage, so you can see where blank space is for sketching (scy1e).

## EQ/FX preservation when copying tracks (Open_Bar)
- To preserve EQ when copy/pasting a track: include an EMPTY track (record silence) in the loop selection before you copy, then **Shift+paste** on the destination track to carry the EQ values over. (Otherwise EQ is lost on paste.)

## MIDI sync to a DAW (opsr / Heyes) — for clocking the OP-1 to the rig
- On OP-1f: **Shift+Mic → USB**; **Shift+Com → 1 (MIDI)**, set MIDI Ch 1, Clock In, Notes In, Other In; on the Metronome page set the Ochre knob → **MIDI Sync**.
- In Logic Pro: File > Project Settings > Synchronization > MIDI > Destination = OP-1, enable Clock.
- To record MIDI regions back to tape: set Shift+Com to "both", Shift+Mic → USB, activate tape input + arm; select OP-1f as the interface in Logic and enable MIDI clock.

## External hardware over USB-C (Heyes)
- Sequencing from a Dato DUO: hold leftmost key on startup, connect USB-C; on OP-1f MIDI setup enable clock out / notes out / other out / timestamp on / velocity on; set BPM to Beat Match.
- **Wireless radio sampling:** plug a "KenTech Transmitter FM" into the audio OUTPUTS to broadcast a phone/tablet/computer signal, then sample it off the OP-1's FM radio receiver — a cable-free way to grab any audio source into the OP-1.

## Sequencers
- **Only Pattern and Sketch sequencers let you play live** over the running sequence while staying on the sequencer page (opsr).
- **Tombola ambient texture (Heyes):** chop a sampled vocal, feed into Tombola with the Phone effect modulated by a soft Element LFO at variable speeds — evolving background bed.
