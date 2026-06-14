---
type: patch
title: Pickup-Machine Live Looper (banjo/baritone, master + slave)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Live-looping the banjo/fuzz wall as a sync-locked loop — overdub, re-pitch, reverse — looper-pedal behavior with timestretch sync (Cuckoo "Loopbox").
tags: [looper, pickup, banjo, clock-master, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 4 · Track 1 master Pickup, Track 2 slave Pickup (LEN = X2)" }
  - { name: "Track 1 machine", type: switch, value: "Pickup (double-tap [TRACK 1]; hard-linked to its recorder buffer)", options: ["Pickup", "Flex", "Static", "Thru"] }
  - { name: "REC SETUP 1 INAB", type: switch, value: "A B (or A for mono GK-5/VG-800)", options: ["A", "B", "A B", "-"] }
  - { name: "REC SETUP 1 INCD", type: switch, value: "-" }
  - { name: "REC SETUP 1 RLEN", type: knob, value: "MAX" }
  - { name: "REC SETUP 1 TRIG", type: switch, value: "ONE2" }
  - { name: "REC SETUP 1 SRC3", type: switch, value: "-" }
  - { name: "REC SETUP 1 LOOP", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "REC SETUP 2 FIN", type: knob, value: "0.063 (tiny fade kills loop-point clicks)" }
  - { name: "REC SETUP 2 FOUT", type: knob, value: "0.063" }
  - { name: "REC SETUP 2 AB", type: knob, value: "127 (direct-monitor input without MIXER DIR)" }
  - { name: "REC SETUP 2 QREC", type: switch, value: "OFF" }
  - { name: "REC SETUP 2 QPL", type: switch, value: "OFF (or PATTERN LENGTH for synced loops)" }
  - { name: "SRC MAIN PITCH", type: knob, value: "0 (MUST be 0 for overdub/replace)", options: ["0"] }
  - { name: "SRC MAIN DIR", type: switch, value: "FWD", options: ["FWD", "REV", "PIPO"] }
  - { name: "SRC MAIN GAIN", type: knob, value: "0" }
  - { name: "SRC MAIN OP", type: switch, value: "DUB", options: ["DUB", "GAIN"] }
  - { name: "SRC MAIN LEN (master)", type: switch, value: "OFF" }
  - { name: "Track 2 machine", type: switch, value: "Pickup (slave), same setup, SRC MAIN LEN = X2 (auto-locks to 2× master length + phase)" }
  - { name: "MEMORY RESERVE LENGTH", type: knob, value: "40 s (default 16 s) before long-loop sessions (needs power-cycle)" }
---

# Pickup-Machine Live Looper (banjo/baritone, master + slave)

## Concept
Live-looping the banjo or fuzz wall as a sync-locked loop with looper-pedal behavior plus timestretch sync — overdub, re-pitch, reverse. A master Pickup on Track 1 holds the loop; an optional slave Pickup on Track 2 (LEN = X2) auto-locks to twice the master's length and phase for a longer baritone drone bed.

## How to play it
1. **Track 1 = Pickup** (double-tap [TRACK 1] → Pickup; hard-linked to its recorder buffer).
2. RECORDING SETUP 1 ([FUNC]+[REC1]): **INAB = A B** (or A for mono GK-5/VG-800), INCD = −, **RLEN = MAX, TRIG = ONE2, SRC3 = −, LOOP = ON**.
3. RECORDING SETUP 2 ([FUNC]+[REC2]): **FIN = 0.063, FOUT = 0.063** (tiny fades kill loop-point clicks), **AB = 127** (direct-monitor input without MIXER DIR), QREC = OFF, QPL = OFF (or PATTERN LENGTH for synced loops).
4. SRC MAIN ([SRC]): **PITCH = 0** (MUST be 0 for overdub/replace), DIR = FWD, GAIN = 0, **OP = DUB**, LEN = OFF for master.
5. Play; **[REC1] start, [REC2] close** (loops immediately, OT BPM snaps); [REC1] again = overdub; [REC2] = stop overdub (loop keeps playing).
6. Click-free order: REC1 start → REC1 set-length+overdub → REC2 lock playing. **Triple-tap REC1 = record-while-erase.**
7. **Slave layer** (baritone drone 2× long): Track 2 = Pickup, same setup, SRC MAIN **LEN = X2** (auto-locks to 2× master length + phase).
8. Re-pitch: PITCH ±1 octave. DIR = REV / PIPO. GAIN + OP = GAIN = volume rides only (swells).
9. Sync the sequencer: [TRACK]+[TEMPO].
10. **MEMORY:** bump RESERVE LENGTH ([FUNC]+PROJECT>SYSTEM>MEMORY) to **40 s** (default 16 s) before long-loop sessions (needs power-cycle).

## Notes
- ⚠️ Pickup overdub misbehaves when OT is MIDI clock SLAVE — **OT must be clock master to live-loop.**
- Pickup loops can't be sequenced or p-locked.
- Settings from the manual-grounded recipe + Cuckoo tutorial.

## Sources
- Ref: Cuckoo "Loopbox" (community, verified)
- links/pickup-machine-live-loop-setup.md + transcripts/cuckoo-ot-pickup-machine-loopbox.md (Manual §9.3 p49-50, §17.1.4-5 p105-106, Appendix A.5 p121; youtube JnbQ8ichm54)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)
