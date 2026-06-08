https://www.musicradar.com/how-to/how-to-use-the-novation-sl-mkiii-midi-controller-with-your-daw-and-a-hardware-synth
musicradar.com · MusicRadar how-to · (DAW + hardware-synth walkthrough)

# Driving external hardware from the SL — practical routing workflow

The core real-world workflow for using the SL as a brain for external synths/gear (distilled; routing names verified against the manual's MIDI Ports section):

1. **Set the Part destination to DIN.** Shift + Sessions → select the Part → set the **DIN** rotary to **1** (or 2/Both). Connect the SL's MIDI Out (DIN 1) → the hardware's MIDI In with a 5-pin cable.
2. **Confirm the DIN channel.** Each Part has its own MIDI channel (rotary 6 / third screen). Set the hardware synth to receive on that same channel (ch.1 is the simplest for a single device).
3. **Multi-destination trick:** a Part can send to USB *and* DIN at once. To stop a hardware synth from doubling a software instrument, **toggle the Part's DIN destination Off** while leaving USB On (DAW-only), and back On when you want the hardware.
4. **Clock:** to make the SL the master for synced hardware, Global → **MIDI Clock Tx = On** (24 PPQN to USB + both DIN). To follow the hardware instead, **MIDI Clock Rx = On** and feed clock from only one port.

## Host MIDI ports exposed over USB (manual p.28, for DAW integration)
- **Inputs to host:** `MIDI` (Parts routed to USB), `InControl` (DAW comms via InControl/HUI), `From DIN 1` (SL as a USB↔DIN MIDI interface).
- **Outputs from host:** `MIDI` (host → Parts, to record into the sequencer), `InControl`, `To DIN 1 / To DIN 2` (host MIDI forwarded straight out the DIN ports, untouched), `To CV/Gate` (host MIDI → CV: **MIDI ch.1 → CV/Gate 1, ch.2 → CV/Gate 2**; CCs matching the Mod CC# → Mod ports).

## Standalone-vs-DAW reminder (manual + reviews)
The standalone Sequencer/Sessions world and the InControl DAW world are a hard toggle — pick one transport per session. Pressing **InControl** enters DAW mode; press it again (or any other view button) to leave.
