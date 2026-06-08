https://www.elektronauts.com/t/octatrack-live-overdub-looping/50025
elektronauts.com · Octatrack subforum · ongoing thread (+ "Overdubbing Pickup Machines" /54256, "Pick up machine help" /1649, "double tempo" /36461)

# Pickup machines (live looping) — the working recipe + the gotchas

Pickup machines are the OT's dedicated looper machine, hard-linked to a track recorder. They are the ONLY way to get true overdub: "you can't overdub when you use the non-pickup-machine recorder."

## Working settings for a tempo-synced loop
- **QREC = PLEN and QPLL = PLEN** (quantize record start / quantize playback to pattern length) → recording locks to the sequencer.
- **RLEN (RECORD setup 1) = 64** for a clean loop synced to sequencer BPM; set **PLEN (RECORD setup 2) to the same value** so the first ("master") pickup records without changing tempo after it loops, and overdub still works.
- For LONG loops: set RLEN to **MAX with ONE2 mode** enabled — but this requires **dynamic recorders** in the memory/RAM config.
- Start it live: with the sequencer running, **press A or B on the pickup track** — it starts recording on the next pattern cycle.

## Master vs overdub behavior
- The FIRST pickup recorded becomes the tempo "master" — it sets the loop length the others sync to. Subsequent pickups on other tracks warp to it.
- Overdub adds onto the existing buffer. Press to toggle overdub on/off.

## The gotchas (well-documented pain points)
- **"DUB ABORTED!"** error appears when overdub conditions aren't met (often a length/sync mismatch or trying to overdub a buffer that isn't set up for it). Match RLEN/PLEN and quantize settings.
- **Volume creep:** the sample can get LOUDER with each overdub pass — watch gain staging across dubs.
- **Sequencer must be STOPPED to (re)start some pickup recordings** in certain configs — a workflow constraint vs a real loop pedal.
- **Clearing a loop:** stop the pickup machine, load a different/empty loop file into its recording buffer, restart the pickup. That swap is also how you reset it.
- **Mem-config bug:** after switching to dynamic recorders for long loops, **power-cycle the OT** — there's a known bug where samples are silenced until you reboot.
- **Slave bug:** overdub is unreliable when the OT is MIDI-slaved (see thru-pickup-latency note) — run the OT as clock master for looping.

## Integration trick
A pickup recording can be loaded onto a **Flex** machine on a separate track; re-recording the pickup loop **auto-warps it onto the Flex track** — bridge from live-looping to sliceable/mangleable material.
