https://www.audiothing.net/blog/how-to-make-creative-convolution-reverbs-irs/
audiothing.net · AudioThing · "How to make Creative Convolution Reverbs and IRs" · 2017-08-18
(+ designingsound.org "Using Convolution Reverb For Designing Lo-Fi Sounds" 2018-10-11)

The "recorded-wrong" convolution angle. Kontakt has a built-in **Convolution**
effect that loads CUSTOM impulse responses (WAV) — so any of these IRs can live
inside the instrument and smear it into a degraded textural space.

## The core idea
- A convolution reverb stamps the character of its IR onto your sound. Feed it a
  WEIRD IR (not a room) and your dry sample inherits that strangeness → instant
  lo-fi / textural / "wrong" space.
- **Rule:** the IR should be **untuned and noise-like** (broadband). Pitched/
  harmonic IRs "amplify some frequencies too heavily" and the IR's own footprint
  becomes too obvious. Noise = good IR; a chord = bad IR.

## What to use as IRs (beyond real spaces)
- **Everyday objects / noise:** a bag of cereal poured, a match striking, metal,
  cardboard, a car trunk, contact-mic'd object vibrations.
- **Lo-fi recordings:** IRs captured through vintage mics / cheap gear → bakes the
  degraded character in (the designingsound piece's whole point).
- For THIS rig: **a pedalboard reverb/spring tail, a tape-hiss swell, a banjo
  scrape, a field recording** can each be rendered to a short WAV and used as an IR.

## Concrete IR prep steps (from the AudioThing walkthrough)
- **Trim** the IR: use Start to cut initial lag, End to cut excess tail.
- **Fades:** short Fade-In + longer Fade-Out (avoids clicks / unnatural onset).
- **Pitch the IR DOWN** (up to ~8×) → **thicker, longer, more ambient** texture.
- **High-pass** the IR to kill boomy low-end the convolution adds.
- Run **100% wet** (no dry) for a fully-immersed, "this was recorded somewhere
  wrong" wash.
- EQ post-convolution if low-end still builds up.

## In-Kontakt application
- Put **Convolution** as a Group/Instrument insert, load your custom IR. Stack
  with the lo-fi-adjacent Kontakt FX (Lo-Fi, Cabinet, Tape Saturator, the Stomps)
  for a degraded, "recorded-wrong" sustained bed.
- Convolving a clean drone with an object/metal IR = unusual textures you can't
  get from a normal reverb (e.g. layering with cymbal/metal IRs for metallic
  shimmer on a banjo drone).

### Takeaway for the rig
This is the cheapest route to the degraded aesthetic INSIDE the sampler: capture
your own pedal tails / tape hiss / scrapes as short WAVs, prep them (trim, fade,
pitch down, HP), and load them as IRs in Kontakt's Convolution effect → every
note plays back through your own broken little space.
