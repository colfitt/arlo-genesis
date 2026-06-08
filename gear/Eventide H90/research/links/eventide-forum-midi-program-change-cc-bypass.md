https://www.eventideaudio.com/forums/topic/h90-simple-midi-program-change-help/
Eventide official forum · dirtybuck (Q) / coirbidh_99 (A) · Jan 7, 2023
(Plus PC Offset + PC/CC timing from the official MIDI docs https://cdn.eventideaudio.com/manuals/h90/1.7.1/content/system-menu/midi.html)

# MIDI: PCs change Programs; use a CC to toggle Active/Bypass

## The core gotcha (H9 users hit this)
On the H90, **Program Changes are RESERVED for loading Programs** — you cannot "toggle a program on/off" with a PC the way some H9 workflows did. To bypass/engage, you map a **CC** to the Active/Bypass parameter:

> "Go to System → MIDI → Global Control and assign a CC to P Act/Byp. PCs on the H90 are reserved for changing programs." — coirbidh_99, Jan 7 2023

Working implementation (dirtybuck):
- Map a MIDI footswitch to a chosen CC#.
- **CC value 64 = engage**, **value 1 = disengage** (i.e. >63 on, <64 off).

## Two behavior notes from this thread
- The Act/Bypass-via-CC behavior worked **in Perform mode**.
- In a multi-pedal MIDI chain, set the H90's MIDI output mode to **"Thru"** (not "Transmit") so it passes messages to downstream pedals.

## PC numbering + PC/CC timing (from official MIDI docs)
- By default the H90 transmits/receives **PC 1–100**. Enabling **PC Offset** switches it to **0–99**. If your controller numbers programs from 0, set PC Offset so the numbers line up across devices.
- **PC+CC timing for scene recalls:** send the **Program Change on press**, the **CC values on release**, and **hold ~1 second between** so the Program has time to load before the CCs arrive. Sending CCs too fast after a PC can land them before the new Program is ready. (Confirmed reliable: a PC followed by 3 CCs to 3 different params.)

## Rig relevance
For the Digitakt 2 / Chase Bliss MIDI chain: use **PC to recall H90 Programs** (scene units), and dedicated **CCs to toggle Active/Bypass** and to nudge mapped parameters. Build your controller so the PC fires on press and CCs on release with a beat of hold — important when changing scenes live mid-song. Set H90 MIDI Out = Thru if the H90 sits mid-chain feeding other MIDI pedals.
