https://op-forums.com/t/op-1-field-both-power-and-midi-over-usb-c/25896
op-forums.com (op1.fun community) · multiple users · the "charge + MIDI at the same time" problem

Field-specific gotcha thread: can you power AND pass MIDI/audio over the single USB-C port simultaneously? Short answer from the community: not reliably.

## The conflict
- "Whatever I tried, the OP-1 won't both charge and do MIDI."
- With a USB-C Y-splitter: "when the splitter passes charge, it won't also pass MIDI." Tried the MOGOOD USB-C Y-splitter — unreliable, MIDI failures + inconsistent charging.

## Workarounds people landed on
- **Two splitters** so each device gets its own charge and one USB channel is reserved JUST for MIDI (needs separate power sources). Clunky but works.
- **Bypass USB-C MIDI entirely:** use a "Cantrip / USB-C to TRS-A MIDI adapter" so charge stays on USB-C and MIDI goes over a TRS-A minijack. Cleanest fix.

## Rig takeaway
The OP-1f has ONE port. If you want it clocked to the rig AND topped up for a long session, plan for it: either run on battery (~24h, fine for most sessions) and use USB-C purely for MIDI/audio, or use a TRS-A MIDI adapter for clock so the USB-C port is free for charging. Don't expect a single cable to a powered USB hub to do both.
