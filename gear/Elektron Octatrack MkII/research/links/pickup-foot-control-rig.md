Manual: Octatrack MkII User Manual, §17.1.5 (p.106), §16.5 note (p.103), Appendix C MIDI note mappings (p.137)
Elektron manual

# Hands-free Pickup looping — MIDI foot control (the live banjo/guitar looper)

Because the OT lives on the desk but you're playing banjo/guitar standing up, drive the Pickup machines from a **MIDI foot controller** sending notes on the OT **auto channel** (PROJECT > MIDI > CHANNELS > AUTO CHANNEL). This is the practical way to loop the rig live without reaching the unit.

## Wiring
- Foot controller **MIDI OUT → OT MIDI IN** (5-pin DIN).
- Foot controller sends on the **auto channel** (set in PROJECT > MIDI > CHANNELS).
- AUDIO NOTE IN = STANDARD (default) so incoming notes map to the Pickup transport.

## Note mapping (auto channel) — drives the *active track's* Pickup machine
| Pedal | MIDI note | Function (= panel key) |
|---|---|---|
| 1 | **C (60)** | Combo-record / overdub toggle (= [REC1]) — samples enabled sources |
| 2 | **E (64)** | Play / stop toggle (= [REC2]) |
| 3 | **B (71)** | Sync sequencer to active Pickup loop; start at next loop wrap |
| 4 | **A (69)** | Move active track focus to **previous** track |
| 5 | **G# (68)** | Move active track focus to **next** track |

So: step on **track-prev/next** to choose which loop you're recording, **C** to start/overdub, **E** to close/stop, **B** to lock the sequencer to it.

## CC alternative (pedals that only send CC)
If the controller sends only CCs, send **CC 59 to the auto channel** — it's interpreted as a note-on, with the CC *value* = the MIDI note number. e.g. CC59 value 60 = combo-record. Useful for an expression/aux switch jack.

## Rig recipe — "loop the banjo, hands-free"
1. Pickup machines on tracks 1 + 2 (setup per pickup-machine-live-loop-setup.md; INAB = A for a mono GK-5/VG-800 feed, or A B for stereo).
2. Foot controller on the auto channel, mapped as above.
3. Track 1 active → play a banjo phrase → **pedal 1** start, **pedal 2** close. Loop runs; OT BPM snaps to it.
4. **Pedal 5** → track 2 → play a counter-line → **pedal 1/2** → a second loop (set LEN=X2 for a longer slave bed).
5. **Pedal 3** → the OT sequencer now rides the loop, so any programmed Flex/MIDI parts (drums, VG-800 pad) lock to the banjo you just played.

## Rig peers that can be the foot controller
- A dedicated MIDI footswitch, or
- The **Novation 61SL MkIII** can send notes/CC from its pads/keys on a chosen channel (set that = OT auto channel) if it's within reach, or
- Any of the MIDI-equipped CB/Microcosm/H90 pedals are NOT note senders — use a real MIDI foot controller for this.
