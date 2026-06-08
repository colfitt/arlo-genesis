https://www.vguitarforums.com/smf/index.php?topic=38806.0
vguitarforums.com · "VG-800 with Software Instruments" thread (arkieboy, Elantric, HitechGuitar) · June 2025

Using the VG-800 over USB-C as a combined audio + MIDI interface to drive software instruments (MainStage, soft-synths) and return audio.

## Core routing concept
- **arkieboy (June 18, 2025):** *"Audio and MIDI can be routed through the USB cable from the VG-800 to your laptop, so you can use the guitar-to-MIDI on the VG-800 to control MainStage, and output the audio back to the VG to be output at the main outs."*
- One USB-C cable carries: GUITAR-TO-MIDI out (drives the soft-synth) AND multichannel audio (soft-synth audio returns into the VG-800 and out its main outs). Round-trip in a single cable.

## USB audio options — read the README
- **Elantric (June 21, 2025):** *"REVIEW the various USB AUDIO OPTIONS on VG-800. And review the README file in the USB DRIVER zip file — reveals audio channel assignments for your OS."* The channel map (which DAW input = dry/wet/per-path) is OS-specific and documented in the driver zip, not the manual.
- There are **multiple USB audio modes.** The highest-quality "Re-Guitar" multichannel mode is **NOT class-compliant** — to get class-compliant audio on iOS/Android you must switch to **USB GENERIC mode**, which **disables the highest-CPU Re-Guitar USB setting** (Elantric, page 5 of main thread). So: full multichannel needs the Boss driver on Mac/Win; iPad gets a reduced mode.

## Alt-tune + MIDI gotcha (carries over)
- Same as the GUITAR-TO-MIDI thread: to make the soft-synth receive RETUNED notes, enable **CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE = ON**. Otherwise MIDI sends physical-string pitches while audio is shifted.

## External MIDI controllers
- arkieboy confirms a **Paint Audio MIDI Captain** can be merged with the VG-800's guitar-to-MIDI stream (foot control + pitch-MIDI together).

## Rig takeaway
For the Pedalxly setup: a single USB-C to the studio Mac lets the banjo/baritone drive a soft-synth and return its audio through the VG-800's outs into the front of Board 1 — no extra interface needed at that stage. Use the Boss driver on Mac for full multichannel; check the driver README for the exact channel assignments before patching in the DAW.
