https://www.elektronauts.com/t/octatrack-digitakt-digitone-best-way-to-connect/84027
elektronauts.com · community thread (multiple users) · ongoing
Also: MusicRadar "Ditch the laptop: all-Elektron setup" (https://www.musicradar.com/how-to/ditch-the-laptop-how-to-make-music-with-an-all-elektron-hardware-set-up) · Elektronauts DT II vs OT Mk2 (213888) · live-rig thread 243685

# The Digitakt II ↔ Octatrack MkII combo — clock, audio, role division

The canonical two-box Elektron studio. Roles are complementary, not overlapping.

## Role division (consensus)
- **Digitakt II** = drums + focused groove, fast kit-building, **MIDI sequencing/clocking of the whole rig** (the pedals, VG-800), 16 audio-or-MIDI tracks. The box you finish beats on.
- **Octatrack MkII** = deep real-time **mangler / audio hub**: 4 inputs, two FX per track, **true independent time-stretch + pitch-shift** (the DT2 is repitch/playback-rate only), scenes + crossfader, live audio processing. The box you perform and destroy with.
- Workflow: **DT2 holds the beat → feed DT2 (or its stems) into the OT for mangling/summing.**

## Clocking (who is master)
- **Default: Digitakt = clock master, Octatrack = slave.** Rationale from the thread: the DT2 (and Digitone) "can lock different tempi per pattern by nature," so letting the DT2 master preserves **per-pattern tempo** that the OT's single-project tempo/arranger doesn't replicate identically.
- Wiring for that default: **DT2 MIDI OUT → OT MIDI IN.** DT2: CLOCK SEND + TRANSPORT SEND ON. OT: in PROJECT > MIDI > SYNC, **CLOCK RECEIVE + TRANSPORT RECEIVE ON** (and CLOCK/TRANSPORT SEND off).
- **Invert when the OT's arranger drives a live set:** OT master (OT MIDI OUT → DT2 MIDI IN), DT2 = CLOCK/TRANSPORT RECEIVE ON. The MusicRadar all-Elektron guide shows the OT mastering: OT MIDI out → other machines' MIDI in, clock-send on OT, clock-receive on the rest.
- The OT can also sequence the DT2 over MIDI (e.g. OT controlling DT2 on channels 1–8) while clocking it — useful if you want the OT as the single brain.

## Audio routing
- **Simplest mangle path:** DT2 **OUT L/R → OT IN A/B** (one stereo input). Set an OT track to a **Thru machine** to monitor/FX the DT2 live, or a **Flex/Pickup machine** to sample/loop it, then crush with OT scenes + crossfader.
- **Save an OT input:** if a Digitone (or other source) is in the chain, route DT2 → Digitone inputs → Digitone OUT → OT IN A/B so the DT2+DTN share one OT stereo input "and leaves one stereo input free on the OT for whatever might come." OT becomes the **audio hub / summing + FX device** for the whole signal flow; its main OUT → Apollo x8 / Babyface.
- Keep the DT2's **send FX dry** into the OT if you want the OT to be the sole FX colour, or print them if you want the DT2 character baked in.

## Overbridge vs audio for the pair
- Only one Elektron box streams over a given USB Overbridge session cleanly per app instance; in a DT2+OT rig people typically **Overbridge the DT2** (multitrack stems into the DAW) and take the **OT via analog** into the interface, OR run both as analog into the Apollo/Babyface and skip Overbridge for the OT. The OT MkII's Overbridge support is more limited than the DT2's — treat the OT as an analog audio hub and let the DT2 be the USB-streamed box. (See Overbridge file; confirm current OT Overbridge status against Elektron's compatibility page before relying on OT multitrack USB.)

## TL;DR recipe
1. DT2 MIDI OUT → OT MIDI IN. DT2 = clock+transport master; OT = receive.
2. DT2 OUT L/R → OT IN A/B; OT Thru/Flex machine to process; OT main OUT → interface.
3. DT2 = groove/drums + sequences the pedals; OT = live mangle, time-stretch, scenes, crossfader, summing.
4. Flip master to OT only when the OT arranger leads a performance.
