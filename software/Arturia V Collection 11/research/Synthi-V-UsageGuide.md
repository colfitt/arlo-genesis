# Synthi V — Usage Guide

Arturia's EMS Synthi AKS — the **pin-matrix drone/noise/sound-design** machine (the
Floyd / Eno / Radiophonic Workshop lineage). For this rig it's the in-the-box source for
unstable-pitch walls, self-oscillating-filter drones, and "recorded-wrong" noise beds
under banjo. Its sweet spot is "evolving electronic timbres and harsh effects," not clean
emulation.

## 1. The engine + the pin matrix (the brain)

3 oscillators (waveform mix) + white-noise + an **18 dB/oct self-resonating filter** with
soft distortion + ring mod + a loopable **AD** envelope shaper + S&H + the **XY joystick**
+ a spring-reverb output stage. `research/links/vc-drone-synthi-sos-vc7-review.md`

**The pin matrix** — click a cell to drop a pin; **rows = sources, columns =
destinations.** Arturia's version uses **5 pin types** (color-coded fixed attenuators at
**100/75/50/25 %**) + **grouping pins** that drive several destinations from one source. So
modulation *depth* is set physically by which color pin you place — **a drone is literally
built by where the pins land.** `research/links/vc-drone-synthi-www2004-guide.md`

**Vintage / Modern switch:** Vintage = modelled oscillator drift/instability (drone gold —
slow beating, unstable-pitch walls). **Stay in Vintage** for "recorded-wrong." `research/links/vc-drone-synthi-sos-vc7-review.md`

**The joystick = a hand-played drone-swell controller:** assign X/Y to any matrix
destinations (Arturia's example: "X slowly detunes OSC2, Y opens the VCF" — swell a drone
by hand), then **animate + loop the joystick** for hands-free vector-style evolution. `research/links/vc-drone-synthi-arturia-sounddesign.md`, `research/transcripts/vc-drone-synthi-synthanatomy-firstlook.md`

**What Arturia added (upper panel):** osc sync, S&H, **five function generators** (loopable
multi-stage env/LFO shapes — the hands-free evolving-drone engine), an extra syncable LFO, a
**7×4 modulation matrix** on top of the pinboard, **dual sequencers** (256-event + 32-step),
and a **3-slot / 10-type FX section** (spring reverb, chorus, stereo delay). `research/transcripts/vc-drone-synthi-catsynth-demo-tut-p1.md`

## 2. Copyable drone/noise recipes

`research/links/vc-drone-synthi-arturia-sounddesign.md`
- **★ Self-oscillating sine drone (simplest wall):** push **filter resonance into
  self-oscillation**; play one low note. Add a **25% pin from a looped slow function
  generator → filter freq** for slow pitch breathing. Spring reverb up; Vintage mode for
  drift. → under banjo, then EchoBoy.
- **Unstable-pitch noise wall:** Vintage mode; mix all 3 oscillators slightly detuned + the
  noise generator into the filter; a **grouping pin** so one random source (S&H) jitters OSC
  pitch + cutoff at once; joystick X = OSC2 detune, Y = cutoff (animate + loop); ring-mod one
  pair for a metallic edge.
- **Metallic inharmonic bed:** ring modulation (Arturia's own "secret weapon") between two
  oscillators → into the filter → spring reverb.

## 3. Rig integration

Layer the drone/noise bed under banjo/baritone, then into **Valhalla** (long) + **EchoBoy**;
**Decapitator/SketchCassette** to re-degrade. The looped function generators + animated
joystick let it evolve hands-free while you play the banjo over the top.

## 4. Best learning resources

1. **CatSynth TV — "Synthi V Demo & Tutorial Part 1"** — best intro: history, pin matrix,
   editing.
2. **SYNTH ANATOMY — "Synthi V First Look"** — the added function generators + joystick
   animation.
3. **Sound on Sound (V Collection 7 review, Synthi section)** — pin types + dual sequencers.

## 5. Pitfalls / gotchas

- **It's a sound-design instrument, not a play-a-melody synth** — embrace patch-and-explore;
  "hit record, find the happy accident."
- **Vintage mode drifts on purpose** (that's the drone value); Modern = stable when you need
  it.
- The pin matrix is the whole interface — depth = pin color, routing = pin position.

## 6. Captured sources

**Transcripts (2)** — `research/transcripts/`: vc-drone-synthi-catsynth-demo-tut-p1 ·
vc-drone-synthi-synthanatomy-firstlook.
**Links (3)** — `research/links/`: vc-drone-synthi-sos-vc7-review · vc-drone-synthi-arturia-sounddesign ·
vc-drone-synthi-www2004-guide.

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first line =
the original URL). Primary: CatSynth TV, SYNTH ANATOMY, Sound on Sound, Arturia sound-design
page. **Honesty flag:** Arturia's Tips FAQ 403'd; the deep Sonic Academy/Groove3 courses are
paywalled — recipes are synthesized from the component tutorials + reviews.
