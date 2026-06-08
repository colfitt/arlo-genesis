https://www.elektronauts.com/t/live-looping-pickup-and-thru-device-and-audio-latency/106375
elektronauts.com · Octatrack subforum · ongoing thread

# Thru / Pickup machine latency + the slave-clock overdub bug

## Latency reality
- The OT adds latency both when **monitoring through a Thru machine** and when **recording**. It is real and measurable, not zero. Round-tripping audio out to a DAW (Ableton) and back through the OT compounds it — "I don't think it is technically possible that way without latency." For this rig the lesson is: **monitor THROUGH the OT to the mains, don't loop audio back to a computer** to avoid round-trip stacking.
- A/D + D/A conversion + processing buffer = a small fixed input-to-output delay. Fine as a live FX insert; problematic if you try to phase-align it against a dry path.

## The phasing trap (from the sibling "direct out vs recorder monitoring" thread)
- If you hear the DIR/direct-monitor path AND the recorder/Thru-monitor path at the same time, you get **doubling/phasing/flam** because the processed path is delayed vs the direct path. Pick ONE monitor path (set DIR to 0 if you're monitoring through the track) to avoid comb-filtering.

## Workarounds users cite
- Use the **CUE outs with their own track-delay setting** to time-compensate a path independently.
- Make the OT the **clock master** rather than slaving it — directly relevant to the next point.

## The slave-clock Pickup OVERDUB bug (important for clocking choice)
- **Pickup-machine OVERDUB does not work reliably when the OT is MIDI-SLAVED**, even when slaved to other Elektron boxes. Reported workaround: **make the Octatrack the MIDI clock master.** This is a real consideration for the rig's clocking topology — if you want live looping/overdub on the OT, it wants to be the master, not the slave.
