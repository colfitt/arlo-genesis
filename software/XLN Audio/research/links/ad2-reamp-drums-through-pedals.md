https://theproaudiofiles.com/reamping-drums-with-guitar-effects/
theproaudiofiles.com · Mark Marshall · 2015-05-13

# Reamping drums through guitar pedals / tape — directly applicable to AD2 stems

Not AD2-specific, but the canonical method. AD2 (multi-out, dry) is an ideal clean
source to reamp through the owner's pedalboards (Front→Middle→End/Tape) and tape
pedals (Big Time, Generation Loss).

## Signal flow
- Route the drum track/bus to a **dedicated hardware output** with a **reamp box**
  (he uses a **Radial Reamp JCR** — owner has a **Radial X-Amp** active reamper, same
  job). Reamp box → pedals → back into an interface input → record to a new track.
- **Avoid bus sends for the reamp path** — go direct out to reduce latency/phase mess.

## Phase / sync — the #1 gotcha
- "Sending a signal out and back in is going to result in a file that isn't 100%
  synced." Fixes:
  - Nudge the returned waveform **sample-by-sample** to realign to the original.
  - **Phase-invert** and null-test against the dry to check alignment (Logic Gain
    plugin or a console-flip; UAD users flip on the preamp).
  - Always **A/B reamped vs. dry before blending**.

## What to reamp (per-element, via AD2 multi-out)
- **Kick** through an overdrive that keeps low end (he used Creation Audio Grizzly
  Bass) — for this rig, a clean-ish drive pedal, not full fuzz, on the kick.
- **Snare** duplicated → distortion (Pro Co RAT-style) on the copy, blend under dry.
- **Whole drum mix** through a **tape/cassette pedal** (he used ZVEX Lo-Fi Junky) —
  this is exactly the **Big Time / Generation Loss** move: print the kit, run it
  through the tape pedal, blend back.

## Blend strategy
- **Parallel**: keep reamped signal LOWER under the dry, carve with EQ
  (HPF/LPF/mid-cut) so it adds grit/space without mud. Doom/shoegaze wants the dirty
  copy buried, not replacing the dry.

## Rig recipe (named gear)
1. AD2 multi-out → **room-mic stereo out (Pre Fader)** to a Logic aux.
2. Aux output → **Radial X-Amp** → Middle (texture) + End (Big Time / Generation
   Loss tape) pedalboards → interface input → new "room-reamp" track.
3. Phase-align, blend ~20-40% under the dry close mics. Wash the reamp return with
   VintageVerb if you want it even further back.
