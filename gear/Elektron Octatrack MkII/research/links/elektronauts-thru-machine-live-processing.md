https://www.elektronauts.com/t/help-with-ot-as-fx-processor/88200
elektronauts.com · Octatrack subforum · ongoing thread

# OT as a live external FX processor (guitar-pedal mode) — the exact recipe + the gotcha everyone misses

This is the rig-defining use: pedalboard stereo print → OT inputs → OT's filters/LFOs/2 FX blocks → out. The thread distills it.

## The setup
- Drop a **Thru machine** on a track. Set its **INAB** (or INCD) to the input pair you're feeding.
- **MIXER menu: set DIR for that input pair to 0.** DIR is the *dry direct monitor* path straight to the main outs. With DIR up you only hear DRY input. Set DIR = 0 so the ONLY path the input takes is THROUGH the Thru track (and therefore through that track's FX1/FX2/AMP). That's what makes it "wet / processed only."
- Put FX1/FX2 on the Thru track's two FX slots; assign LFOs to cutoff etc.

## THE GOTCHA (the single most-missed thing in the manual)
A configured Thru machine passes NO audio until the track is actually triggered. Two ways to engage it:
1. **Place a trig on step 1** of the Thru track → audio flows when the sequencer plays.
2. **Hold the track button + PLAY** → audio passes through even with the sequencer stopped (the "no track to free up / no trig" live trick — lets you monitor/process without running a pattern).

One user: "So important yet so simple and so easy to miss in the manual." Without this, people configure everything correctly and hear nothing and assume the unit is broken.

## Two routing methods (from the manual, restated by users)
- **DIR method** (MIXER, DIR AB = 127): pure direct monitor, zero track cost, but NO FX — just clean passthrough.
- **Thru-machine method** (DIR = 0, Thru on a track): input only exists through a track, so it gets FX, can be muted, scened, and resampled. **This is the one you want for processing the pedalboard.**

## Practical notes
- The Thru track can be recorded by its own (or another) track recorder while it plays → capture-the-wall + keep monitoring live.
- Because the input is now "inside" a track, scene/crossfader morphs and p-locks apply to the live guitar signal in real time.
