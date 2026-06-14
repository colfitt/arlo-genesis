https://logic-users-group.com/threads/routing-for-reamping-a-guitar-di-and-sending-to-hardware.11298/
logic-users-group.com · users bayswater, Cowboy4d2 · 2020-08

# Reamping a DI out to hardware (amp/pedalboard) in Logic — the pragmatic recipe

The forum consensus is to keep it simple rather than fight the I/O plugin:

## Workflow (bayswater + Cowboy4d2)
1. **Track the part dry through a DI** first (clean, no amp/sim). The dry DI is
   "extremely easy to edit — the pick attack and initial transient are easy to
   identify," so do all comping/slip-editing/cleanup on the DI while the
   performance is locked.
2. To reamp: **send the DI out an interface output → into the amp/pedalboard →
   mic or line back into an interface input.** Arm a NEW track on that input and
   hit record. "The dry track will play back and the re-amped track will record
   a few milliseconds later."
3. **Fix the offset after the fact** — nudge the reamped waveform in the editor
   to align its transient with the dry DI. (Only needed if the two must play
   together; for a standalone reamp it doesn't matter.)

## Latency reality (quoted)
- "There's no way to get rid of latency. On a typical re-amp signal path, the
  signal is going through **ADA conversion twice**, and that takes time. You can
  get latency pretty low, but not zero."
- Monitor the dry signal so the round-trip latency doesn't throw off playing.
  "If you set the buffer very low so latency is down to less than 10 ms, the
  latency you experience... will be roughly the same as standing 10 feet away
  from an amp."

## Two valid approaches
- **Simultaneous**: record dry + reamped on two tracks at once (monitor dry).
- **After-the-fact** (preferred for editing): print dry DI, edit it clean, then
  reamp out to the rig and record the wet return on its own track. This is the
  natural fit for the user's reamping-the-pedalboard workflow — and the manual
  nudge beats wrestling the I/O plugin's compensation for one-off reamps.

## When to use the I/O plugin instead
The I/O plugin (separate thread) auto-compensates and is better when you need
the reamped return to sit time-aligned in a mix automatically (e.g. parallel
outboard on a bus). For tracking a performance through the board, the
record-to-a-new-track + nudge method is simpler and just as good.
