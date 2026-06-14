https://www.youtube.com/watch?v=pIm8KfEA0HA
"Valhalla Delay In Depth Tutorial — How To Use Valhalla Delay" · spoken control reference (mirrors the official manual)

Distilled prose (auto-captions, cleaned; this video reads the official control list — used
here to confirm exact values). Paraphrased.

## Mix / global
- **MIX** — 0% dry, 100% wet, 50% equal. **MIX LOCK**: click the word "MIX" above the
  knob to lock the wet/dry while auditioning presets (so presets don't blow out your
  send balance — handy on a 100%-wet aux).
- **MODE** = base algorithm (Tape, BBD, Pitch, etc.). **ERA** = variations of the mode
  (higher-order filters, saturation smoothing, diffusion behaviour).

## Timing / routing
- **DELAY L/R**, **Sync** (ms / notes / dotted / triplet per side).
- **RATIO mode**: right delay = RATIO × left delay. **61.8% = "golden ratio pseudo-
  reverb"** (confirmed verbatim).
- **Repeat / Swell** (Quad): feedback from the last tap (Repeat) or from the **sum of all
  active taps (Swell)**. Swell = "resonant multi-head tape-echo sounds or pseudo-reverb."
- **FEEDBACK** goes to **200%** for howling self-oscillation. **WIDTH** −100…+100; **0%
  mixes L+R** (mono, strong flanging).

## Color / character
- **COLOR Drive** = input saturation (dB). **COLOR Age** = mode-specific artifacts:
  Tape = asperity noise + splice artifacts; HiFi = asperity noise (no splice); BBD =
  bucket-brigade chip noise; Digital = bit depth of the float converter; Ghost = asperity
  noise; Pitch = float-converter bit depth; RevPitch = bit depth.

## Diffusion (delay → reverb)
- **DIFF Amount**: 0% = off; **68% = a diffusion reverb that fades naturally (decay = the
  attack length)**; **91% = a "pure diffusion" reverb that doesn't need Feedback for its
  decay.**
- **DIFF Size** = span of the diffusion network relative to delay length. **Small = blurs
  the attack but still sounds like a delay; Large = transforms the delay into a
  reverberant sound.**

## Modulation
- **MOD Wow / Flutter** (Tape only) = depth of slower / faster random modulations; the
  *rate* is a function of the delay time (authentic tape behaviour).
- **MOD Rate / Depth** (HiFi/BBD/Digital) = random modulation in HiFi, periodic in
  BBD/Digital.

## Ghost / Pitch
- **FREQ Shift** (Ghost) = frequency shift of both channels in Hz. **FREQ Detune** = Hz
  offset between L/R: low = subtle stereo spread, higher = rapid auto-pan.
- **PITCH Shift** (Pitch/RevPitch) = semitones, both channels. **PITCH Detune** = cents
  offset L/R — "perfect for micropitch and doubling."

## EQ
- **EQ High / EQ Low** = high-cut / low-cut filter cutoffs **in the feedback path** (so
  each repeat gets progressively darker/thinner — the tape-echo "filtering into the
  distance" behaviour, and how you keep a long wash out of the mud).
