http://op-101.blogspot.com/2011/09/cluster-description.html · https://op-forums.com/t/creating-pads-using-chorus-effect-pan-and-detune/5764 · https://www.sinesquares.net/musicgear/teenage-engineerin-op-1-field-6-month-review · https://www.attackmagazine.com/technique/hardware-focus/unwrapping-an-unsung-hero-of-fm-synthesis-perhaps-exploring-the-op-1-field-op-1-og/
op-101 blog (anon, 2011) · op-forums (Skywalkman et al.) · SINESQUARES (6-month review) · Attack Magazine (FM deep-dive) · accessed 2026-06-14

# OP-1 engine PARAMETER MAPS + a concrete chorus-pad recipe (for building drone patches by hand)

The numeric `knobs` arrays aren't exposed by op1.fun, so to *build* a drone/pad patch by ear you need to know what each encoder does. These are the per-engine encoder maps + one fully-concrete community pad recipe. Use with the engine/octave/FX/LFO targets in the drone & bass captures.

## CLUSTER engine encoder map (op-101 blog — JP-8000-supersaw-style)
- **Blue = "# of Waves"** — number of detuned oscillators stacked, 1 (min) → "several" (max). More = thicker wall. Max it for a drone.
- **Green = "Wave Envelope"** — a lowpass-filter cutoff ganged to an A/D envelope. CCW = fast downward sweep; CW = slower upward sweep; dead zone at center. Set CW for a slow-blooming pad.
- **White = "Spread"** — depth of pitch DRIFT; how far each oscillator wanders independently. More spread = wider, more detuned chorus/shimmer.
- **Orange = "Unitor"** — rate at which the pitches wobble/drift around.
> Author flags these as educated guesses ("fumbling in the dark"); TE manual only says "multi-layered oscillator cluster." Reliable in aggregate / directionally.

**Drone recipe from the map:** Cluster, Blue (waves) ~max, Green (wave env) toward CW for slow bloom, White (spread) high for a wide detuned wall, Orange (unitor) low-moderate so it drifts slowly. Octave -1/-2 for doom weight. → matches `tlorach/Bass` and `planks/windswept/cluster_pad`.

## VOLTAGE engine notes (SINESQUARES 6-month review)
- "Biting, aggressive AM synth — sounds like high-voltage sparks at all times. Great for harsh leads, but **surprisingly good for evolving sounds, like all AM synths, due to rich harmonic content from the generated sidebands.**"
- Encoder detail: **Ochre = sub-oscillator octave** (center = unison with main; 0–6 transposes sub up to ±3 octaves), **Grey = sub-osc detune + ring-mod amount** between main and sub. → drop the sub for sub-octave doom; ring-mod for metallic dissonant texture.
- Backs the `celestial` (voltage +1 punch) and `bass face` (voltage -1 nitro) patches.

## FM engine encoder map (Attack Magazine)
- **Blue** = level of all non-Base operators (min/CCW = pure sine; raise for FM harmonics).
- **Beige/Ochre** = frequency set (the operator ratios; "varies wildly, harmonic→discordant even between adjacent values").
- **Grey** = algorithm select (1 of 9 operator routings).
- **Orange** = detune (extreme inharmonic / movement). → for FM bells/drones (cf. Andreas Roman's "Tombola on FM bells").

## CONCRETE chorus-pad recipe (op-forums, user Skywalkman) — fully specified
Two-pass tape double for a wide chorused pad (no FX slot used):
1. Make a pad on the **Cluster** engine (long attack + long release on the T2 envelope page: Blue=Attack up, Orange=Release up).
2. Record it to **tape track 1, panned hard RIGHT**.
3. `Shift + Metronome` → set **Cents = +20** (detune up 20 cents).
4. Record the SAME pad to **tape track 2, panned hard LEFT**, starting at the same position.
5. Playback = a wide chorus from the ±20-cent detune across the stereo field.
- **"Sweet spot imo is 20 or -20"** (Skywalkman). This is the rig-native wide-stereo-double move (cf. `[Shift]+Orange` pan-to-tape in the existing guide) made into a tuned chorus.

## ENVELOPE encoder map (official TE guide — applies to ALL engines, T2 page)
- **Blue = Attack, Green = Decay, White = Sustain, Orange = Release.** Long Blue + long Orange = the pad/drone foundation on any engine.

> Honesty flag: Cluster encoder labels are the op-101 community reverse-engineering, not TE docs; FM/Voltage maps are from named reviews; the ±20-cent chorus recipe and "20/-20 sweet spot" are quoted from the op-forums thread. The T2 ADSR mapping is official.
