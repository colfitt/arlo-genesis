https://support.apple.com/en-us/102005
support.apple.com · Apple · Logic Pro User Guide (current)

# Sync external MIDI hardware (Digitakt / Octatrack / MPC) from Logic via MIDI clock

Logic is the clock MASTER, hardware sequencers follow. Settings are **per
project** — bake them into a template.

## Path
**File > Project Settings > Synchronization > MIDI tab.**

## Steps to send MIDI clock to a device
1. In the **Destination** column, pick the connected MIDI device from the
   pop-up (the device must already exist as a MIDI port — appears once the
   Digitakt/61SL/etc. is connected over USB-MIDI or via a MIDI interface).
2. Tick the **Clock** checkbox for that destination. (You can enable Clock for
   multiple destinations independently — e.g. Digitakt + 61SL simultaneously.)
3. **Delay [ms]** field per destination — NEGATIVE sends the clock EARLIER,
   positive later. Use this to nudge a device that's dragging/rushing against
   Logic's grid. (Concrete: if the Digitakt sounds a hair late, try -3 to -8 ms.)
4. Optional **PDC** checkbox = let plug-in delay compensation apply to the
   clock too.

## Clock Mode pop-up (how transport start is sent)
- **Pattern** — sends Start to external sequencers; you enter a pattern length
  in bars. (Good for pattern-based Elektron boxes.)
- **Song - SPP at Play Start and Stop / SPP / Continue at Cycle Jump** — uses
  Song Position Pointer so the hardware chases Logic's playhead, including on
  cycle jumps. (Best for the Octatrack/Digitakt arranger following the song.)
- **Song - SPP at Play Start and Cycle Jump** / **at Play Start only** —
  lighter SPP variants.

## Other transport sync
- **MTC** (MIDI Timecode) — tick per destination; for locking to video/another
  DAW.
- **MMC** (MIDI Machine Control) — transport control of external recorders;
  usually paired with receiving MTC from that same device.

## Rig note
The **Octatrack MkII has no USB MIDI** — you must run a 5-pin DIN MIDI cable
(via the Apollo/Babyface MIDI port or a USB-MIDI interface) for Logic clock to
reach it. Digitakt 2, MPC Sample, and 61SL MkIII all do USB-MIDI directly.
Elektron boxes do NOT transmit clock by default when acting as master — but
here Logic is master, so what matters is each box being set to receive
clock/transport (Digitakt: SYNC > Clock Receive + Transport Receive = ON).
