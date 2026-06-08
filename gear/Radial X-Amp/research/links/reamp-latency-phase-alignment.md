https://forum.fractalaudio.com/threads/reamping-how-to-correct-latency-of-reamped-track.95514/
fractalaudio.com / kemper-amps.com / forum.cockos.com (Reaper) · community engineering consensus · ongoing threads

Digest of the well-established reamp **round-trip-latency / phase-alignment** technique, distilled from several modeler/DAW forums (Fractal, Kemper, Reaper/Cockos). General reamp engineering that transfers directly to the X-Amp loop — the X-Amp itself is analog and adds no meaningful latency; the delay is the **interface round trip** (DAW → D/A → X-Amp → rig → mic/return → A/D → DAW), so the reamped take always lands slightly LATE versus the original DI. Fix it once, reuse the number.

## Why it happens
- Every reamp pass adds a **constant round-trip delay** = output (D/A) latency + return (A/D) latency + buffer. It's consistent for a given sample rate + buffer, so it's a fixed offset, not a drift.
- A misaligned reamp print against the original DI causes **phase cancellation / comb filtering** if you blend them — the classic "nasty phase / hollow" reamp problem.

## How to measure the offset (loopback method — most reliable)
1. **Loopback test:** route the dry DI out → X-Amp → straight back into an interface input (skip the rig, or with the rig — the rig latency is negligible vs. the converter round trip). Record it.
2. Zoom way in, line up a **clear transient/spike** in the recaptured track against the same transient in the original DI, and **read off the sample difference**.
3. That sample count is your **nudge / recording-offset value** — apply it to every reamp pass at that sample rate + buffer.
- Reference figures people report: e.g. **528 samples ≈ 12 ms @ 44.1 kHz** (illustrative — measure your own). One Apollo+X-Amp user found a **64-sample buffer** put alignment "pretty much spot on."

## Three ways to apply the correction
1. **Manual transient alignment** — zoom in on a loud transient (a deliberate string-pop/click at the head of the take helps) and slide the reamped clip back until the transients stack. Quickest one-off.
2. **DAW recording-offset / nudge** — enter the measured offset as a negative recording delay (or nudge the clip by N samples). Best when reamping many tracks the same way.
3. **DAW "External FX / hardware insert"** — patch the X-Amp+rig as an external-effect insert (Logic Pro's I/O plugin, Cubase, Pro Tools, Reaper). The DAW **pings the loop, measures latency, and compensates automatically** — the most precise, hands-off method, and it lets you reamp in real time as a printable insert.

## Keep it consistent
- Use the **same sample rate AND buffer size** for every reamp pass so the offset stays identical (relevant when stacking multiple passes of the same DI to build a wall — see the rig's layering workflow). If you change the buffer, re-measure.

## Rig fit
- This is the companion to the Apollo guide's reamp section (`Gear/UA Apollo x8/research/links/uadforum-xamp-reamp-thread.md`), which already notes the 64-sample/"spot on" result and the feedback-loop avoidance. Stay consistent: measure once, nudge, keep the buffer fixed across stacked passes.
- For Logic Pro specifically, the **I/O plugin** as a hardware insert gives automatic round-trip compensation — the cleanest way to keep many X-Amp passes phase-locked to the dry DI.
