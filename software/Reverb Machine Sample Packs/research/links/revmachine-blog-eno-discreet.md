https://reverbmachine.com/blog/deconstructing-brian-enos-discreet-music/

reverbmachine.com · Dan Tindall · captured 2026-06-11

# How Brian Eno Created "Discreet Music" — the long-delay self-generating system

## The core technique: Frippertronics (two-tape delay)
Two tape machines feeding each other: one plays back while recording onto the second,
creating a **self-perpetuating loop** where the feedback level sets the decay time.
Source = **EMS Synthi AKS** (mellow sine/triangle + a touch of saw), tone shaped by a
graphic EQ, with an Echoplex delay before the Frippertronics stage.

## Two autonomous sequences
Two looping melodic sequences of slightly different lengths (~31–34 s each). They drift
in and out of sync, "constantly form new combinations as they overlap" — the same
incommensurable-loops idea as Music for Airports, but generative from a synth sequencer.

## DAW recreation (copyable)
1. Two MIDI tracks, distinct melodic phrases.
2. **Different loop lengths** (e.g. 8 bars vs 5 bars) → phase drift.
3. **Long-delay plugin (5600+ ms) on a send, high feedback** = the tape-loop effect.
4. Route both sequences through that delay return.
5. Add a second short delay (~160 ms, high feedback) for extra ambience.
6. Low-pass filter + long attack/decay envelopes for softness.
"Evolving textures from minimal input, self-generating for hours."

## Rig application
The user owns **Arturia Synthi V** (the exact EMS Synthi) — use it as the source per
this article. The long-delay-on-a-send maps to a Valhalla Delay / Logic stock delay at
max time with high feedback, or hardware (Strymon TimeLine / CB Blooper as the
"two-tape" loop). Graphic-EQ tone-shaping → automate an EQ band on the loop return.
