https://valhalladsp.com/2010/12/01/valhallashimmer-tips-and-tricks-adjusting-the-reverb-envelope/
+ https://valhalladsp.com/2010/08/30/introducing-valhallashimmer/
valhalladsp.com · Sean Costello · official "Adjusting the reverb envelope" + "Introducing ValhallaShimmer"

Two official posts: how to shape the swell/attack, and the cascade-instances trick for
chords / near-infinite drones.

## Reverb envelope = slow swells & fade-in pads
- **Diffusion sets the attack shape:**
  - Low Diffusion = discrete echoes that gradually build into reverb.
  - **0.5–0.618 = the reverb "slowly fades in"** (the slow-swell / pad-bloom range — this
    is the setting for an ambient swell that rises into the wall).
  - 0.8–0.91 = a relatively quick attack.
- **Size** fine-tunes the attack TIME and tonal color, working with Diffusion.
- **Feedback** controls decay length AND pitch-shift intensity.
- The controls interact **exponentially**: "combining Feedback with Diffusion results in
  echoes building exponentially in density." High Diffusion (~0.9) alone makes the decay
  "considerably longer than the delay length"; layering Feedback on top → **near-infinite
  sustain pads.** (This is the closest thing to a Freeze — push Diffusion ~0.9 + high
  Feedback for a wall that effectively holds.)

## Cascade multiple instances (the designer's headline trick)
- Costello: Shimmer "works well with cascading multiple instances, both from a signal-
  processing perspective and in terms of the low CPU consumption."
- His own demo: **FOUR instances in series with different pitch-shift values — ±12, ±7,
  ±5 semitones** → builds a stacked harmonic chord shimmer (octave + fifth + fourth) that
  a single instance can't make. ★ This is how you get a "symphonic" rising shimmer rather
  than one climbing octave — chain them, each adding an interval.

## Design intent
Built "from the ground up for ambient work… not good for realistic reverbs, and never
intended to make real reverbs." A reverb for BIG sounds (concert halls → Taj Mahal →
Halls of Valhalla), prioritising lush evolving ambiences and CPU efficiency over realism.
Eno/Lanois/U2 shimmer is the explicit reference aesthetic.
