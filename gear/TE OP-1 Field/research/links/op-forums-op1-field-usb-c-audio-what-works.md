https://op-forums.com/t/op-1-field-audio-over-usb-c-what-works/22655
op-forums.com (op1.fun community) · multiple users · USB-C audio compatibility findings

What actually works for OP-1 Field audio over USB-C — the practical compatibility matrix the spec sheet doesn't give you. Relevant to streaming the OP-1 into the Apollo x8 / RME / Logic.

## As a USB DEVICE (OP-1f plugged into a computer/iPad as the host)
- "When the OP-1F is acting as a USB device for things like Ableton Live on the computer or Audiobus 3 on an iPad… it works as you'd expect for both input and output." So **straight into Logic/Live/iPad it's a normal 2-in/2-out class-compliant interface** — this is the clean path into the Apollo/RME setup.

## As a USB HOST (other gear plugged into the OP-1f)
- **Audio is one-way only:** when the OP-1f is the host it can RECEIVE audio in (e.g. from OP-Z, OG OP-1) but cannot send audio OUT to the connected device. Bidirectional audio OP-1f↔OP-Z is NOT available.
- **One device at a time** via USB — multiple instruments through a hub don't work (as of the thread).
- Confirmed working as host: OP-Z (MIDI + audio in only), OG OP-1 (MIDI + audio in), Elektron MC-101 (powers + communicates over one cable), iPad Pro (when iPad is host).

## Big gotcha
- **44.1 kHz ONLY — no 48 kHz.** This breaks USB audio interop with Elektron gear that wants 48 kHz. Plan tape/album work and DAW sessions around 44.1k if going over USB. (Matches the dossier's 44.1k/32-bit tape spec.)

## Rig takeaway
For the studio: OP-1f as a USB DEVICE into Logic / the computer = reliable clean digital capture (44.1k). Don't expect to host-and-stream into the Elektrons over USB. Analog 3.5mm→1/4" into the Apollo is the alternative if you want Unison preamp color or 48k sessions.
