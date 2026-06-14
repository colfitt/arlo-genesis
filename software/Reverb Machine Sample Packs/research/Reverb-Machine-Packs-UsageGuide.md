# Reverb Machine Sample Packs — Usage Guide

Reverb Machine (Dan Tindall's blog + shop) is a *small* unit with one honest twist:
**the free blog is worth far more than the paid packs.** The packs you actually own
live on the offline `PlaySomeGodDamnMusic` drive; in *this* rig the workhorse path is
(1) load the Kontakt-format packs (VP-30 / PS-48) into Kontakt 8 inside Logic, (2) run
the Ableton-rack pack (Motions) in Live 12 Lite and bounce textures back to Logic, and
(3) mine the blog deconstructions for drone/ambient recipes you build with gear you
already have. Tier-C doc — short, practical, honest where thin.

> **Drive caveat:** the installed packs sit at
> `/Volumes/PlaySomeGodDamnMusic/Sample Libraries/Reverb Machine` and were **offline
> during research** — exact on-disk file lists couldn't be enumerated. Product detail
> below is from the vendor site; verify formats against the drive when mounted.

---

## What Reverb Machine actually offers (packs + racks + blog)

Three distinct product types — only some are samples:

1. **Synth-preset packs** (the majority). Banks of presets *for a specific third-party
   synth* — mostly Arturia (V Collection / Analog Lab / Pigments), TAL U-NO-LX, Cherry
   Audio. **These are NOT samples** — they only work if you own that exact synth. Good
   news: the user owns **Arturia V Collection 11 + Analog Lab**, so the Analog-Lab packs
   are loadable here — notably **Chroma Campfire** (Boards-of-Canada ambient; works even
   in free Analog Lab Play), **Europa** (ethereal Jup-8 pads), **Seminal** (generative
   SEM pads). `revmachine-sounds-catalog.md`, `revmachine-chroma-campfire-playthrough.md`
2. **Ableton-native sample/rack packs** (`.adg` racks built from WAV). The texture-
   relevant ones:
   - **Motions** ($30) — 50 lo-fi ambient patches from 128 cassette-loop / granular /
     guitar-pedal samples, 2–5 macro variations each, + 3 reusable FX racks (tape
     emulator, pitch-shifting quad delay, shimmer reverb) + "Random Generator" patches
     (Ableton random-LFO + arpeggiator). **Ableton Live 11+, works in ALL editions
     incl. Lite.** The single most drone/ambient-aligned product.
     `revmachine-motions-pack.md`
   - **DrumVerse R8** / **Drumtraks** / **Vice** — vintage drum-machine sample sets
     (Roland R-8, SCI Drumtraks, LinnDrum) as Ableton racks (Drumtraks also Logic/FL).
3. **Multi-format sampler packs** — **VP-30** (Roland VP-330 strings/choir/vocoder, 1,050
   samples) and **PS-48** (Yamaha PSS-480 FM) ship **Kontakt + Decent Sampler + Ableton**
   versions. **Kontakt version needs full Kontakt 6+ → the user's Kontakt 8 loads them.**
   `revmachine-vp30-ps48-kontakt.md`
4. **Remake Projects** — paid Ableton project files ($15–40) that rebuild famous tracks,
   shipped with **frozen tracks + WAV stems + MIDI** (so usable in any DAW). The ambient
   ones: Vangelis Tears in Rain ($25), Aphex Twin SAW 85–92 ($35).
   `revmachine-remake-projects.md`
5. **The blog** — 70+ free sound-design deconstructions. The real value (next section).

---

## Using them in THIS rig

### Logic (primary) — the Kontakt path
- **VP-30 / PS-48 → Kontakt 8 inside Logic.** Load the `.nki`; needs full Kontakt (have
  it). VP-30's male/female/mixed choir + strings are ready-made sustained pads to sit
  under a banjo wall. Decent Sampler version = a free, low-CPU fallback.
- Any pack that's **just WAV** (drum sets, or extracted Motions samples) imports straight
  into Logic's Sampler/Quick Sampler — or map them in Kontakt 8 to build a custom
  **playable drone instrument** (hold-loop a single sustained sample across the keyboard,
  set loop points, add a long-attack/release envelope). This is the user's "sample my own
  gear into Kontakt" habit applied to a bought pack.

### Ableton Live 12 Lite (secondary) — the racks, with the Lite caveat
- **Motions explicitly works in Lite** (vendor + KVR both confirm "all editions," no Max
  for Live). The racks are built from stock devices Lite has (Sampler/Simpler + EQ /
  Delay / Reverb / the Random LFO). `revmachine-motions-pack.md`, KVR.
- **But Lite's ceiling still bites elsewhere:** the paid **Remake Projects** are full Live
  11/12 sets — Lite's track/scene caps and missing Suite-only devices can stop a whole
  project loading intact. Use the **stems + MIDI** those projects ship instead, in Logic.
- Workflow: open Motions in Live 12 Lite → play/automate a patch → **resample/bounce to
  WAV** → drag the WAV into Logic (or re-map in Kontakt). Lite is the "rack player +
  texture factory," Logic is the studio.

### Turning packs into drones (copyable)
- Take a Motions cassette/granular patch (or a VP-30 choir note), hold one note, and let
  its built-in tape/shimmer rack evolve — that's a drone. Layer two at a 4th/5th apart.
- Or extract the raw WAV, drop it in Kontakt 8, set a **long loop region** + long
  attack/release, and you have a played-from-the-keyboard sustained wall.

---

## The blog is the real resource (annotated)

Dan Tindall's deconstructions are genuinely rig-relevant because they reverse-engineer
ambient/drone records — and several use the exact plugins the user owns. Read these:

- **Brian Eno — Music for Airports** — the **incommensurable-loops** method: stack 3–5
  sustained loops of slightly-different lengths so they never re-sync = endless evolving
  wall. Free WAV loops at the end. THE drone blueprint. `revmachine-blog-eno-airports.md`
- **Brian Eno — Discreet Music** — the **long-delay self-generating system** (Frippertronics
  / two-tape feedback) sourced from an **EMS Synthi** — the user owns **Arturia Synthi V**.
  Recipe: 2 MIDI loops of different bar-lengths → long delay (5600 ms+) on a send, high
  feedback. `revmachine-blog-eno-discreet.md`
- **Vangelis — Tears in Rain** — CS-80 brass + Rhodes + one big reverb send. The remake
  literally uses **Arturia CS-80 V4 + Prophet-5 V + Stage-73 V2 + Valhalla VintageVerb** —
  all owned. Map aftertouch→brightness, pitch-bend→ribbon slides.
  `revmachine-blog-vangelis-bladerunner.md`
- **Boards of Canada — Chord Theory (Pts 1–2)** — **perfect-fifth dyads** (no third =
  ambiguous drone harmony), auto-fifth osc detune (+7 st), odd-length phrases, and the
  **±20–50 cent global detune** for tape-warped nostalgia (maps to SketchCassette /
  RC-20 / the CB tape pedals). `revmachine-blog-boards-of-canada-chords.md`
- **Aphex Twin — Selected Ambient Works 85–92** — the lo-fi-ambient blueprint: one reverb
  (Quadraverb) on everything, mix to cassette, R-8 drums (= the DrumVerse R8 pack), and a
  73 ms-decay / zero-sustain pluck patch. `revmachine-blog-aphex-saw.md`
- Also on the blog: **Tycho's "Awake" synths**, **Exploring the DX7 / CS-80**, Boards of
  Canada parts, lo-fi retrowave with Forhill. Index: reverbmachine.com/articles/

---

## Copyable recipes

1. **VP-330 choir pad under a banjo wall (Logic).** Kontakt 8 → VP-30 Mixed Choir `.nki`,
   long attack/release, hold a fifth (root + +7 st), Valhalla VintageVerb on a send (the
   Vangelis "one big reverb" move). Play the banjo as the moving lead on top.
2. **Eno incommensurable drone (Logic or Live).** Sample a sustained banjo/guitar note (or
   a CB Big Time / Blooper loop) into Kontakt/Quick Sampler. Make 3–5 loops of *different*
   lengths (think in seconds, grid off). Let them drift; bounce the emergent wall.
   `revmachine-blog-eno-airports.md`
3. **Discreet-Music generative drone (Synthi V).** Arturia Synthi V → two MIDI loops at
   8 vs 5 bars → a long delay (max time, high feedback) on a send. LP filter + long
   envelopes. Self-runs. `revmachine-blog-eno-discreet.md`
4. **BoC tape-nostalgia drone.** Any owned synth: osc 2 +7 st auto-fifth, then global
   detune −30 cents (or run it through SketchCassette II / RC-20 / a CB tape pedal). The
   **Chroma Campfire** pack productises this in Analog Lab — start from its "Reach for the
   Drone" / "Sundown Fifths" presets. `revmachine-blog-boards-of-canada-chords.md`
5. **Motions texture → Logic.** Live 12 Lite → a Motions ambient patch → resample/bounce
   to WAV → drag into Logic or re-map in Kontakt for a keyboard-playable wall.
6. **Aphex cassette master.** Build the bed, then bus → SketchCassette II / RC-20 / PORTA424
   / a CB tape pedal for the mixed-to-cassette lo-fi glue. `revmachine-blog-aphex-saw.md`

---

## Common pitfalls / gotchas

- **Most "packs" are synth presets, not samples** — buying one is useless without the
  target synth. Check the synth requirement before purchase; the Analog-Lab ones are the
  safe bet here (V Collection owned).
- **Kontakt packs need FULL Kontakt** (6+), not the free Player. Fine here (Kontakt 8),
  but the Decent Sampler version is the free fallback.
- **Ableton-rack packs in Logic:** there's no native `.adg` import in Logic. Run them in
  Live 12 Lite and bounce, or extract the underlying WAVs.
- **Lite ceiling on Remake Projects:** the full Ableton projects may not open intact in
  Live 12 Lite (track/scene caps, Suite-only devices) — use their stems+MIDI in Logic.
  Motions itself is Lite-safe; the *projects* are the risky ones.
- **Drive dependency:** the owned packs live on an external drive that must be mounted —
  the SoftwareProfile flags `requires_drive_mounted: true`.
- **Community usage is genuinely thin** — Motions has 0 KVR reviews; the YouTube videos are
  music playthroughs with no captions/narration. Don't expect a tutorial ecosystem; the
  blog articles ARE the documentation.

---

## Captured sources

**research/links/**
- `revmachine-sounds-catalog.md` — full pack catalog (presets vs samples vs racks)
- `revmachine-motions-pack.md` — Motions ambient pack (Lite-compatible) deep detail
- `revmachine-vp30-ps48-kontakt.md` — the Kontakt-ready packs (Logic path)
- `revmachine-remake-projects.md` — paid Ableton learning templates (stems+MIDI)
- `revmachine-blog-eno-airports.md` — incommensurable-loops drone method
- `revmachine-blog-eno-discreet.md` — long-delay self-generating system
- `revmachine-blog-vangelis-bladerunner.md` — CS-80 cinematic pads (owned tools)
- `revmachine-blog-boards-of-canada-chords.md` — fifths + detune nostalgia
- `revmachine-blog-aphex-saw.md` — lo-fi-ambient blueprint

**research/transcripts/** (no-caption videos — distilled from descriptions)
- `revmachine-vangelis-tears-in-rain-remake.md` — CS-80 V4 + Stage-73 + VintageVerb remake
- `revmachine-chroma-campfire-playthrough.md` — BoC Analog Lab preset pack (incl. drone presets)

## Sources
- Reverb Machine — Sound Packs: https://reverbmachine.com/sounds/
- Motions: https://reverbmachine.com/sounds/motions-lofi-ambient-ableton/ · KVR: https://www.kvraudio.com/product/motions-by-reverb-machine
- VP-30: https://reverbmachine.com/sounds/vp-30/
- Remake Projects: https://reverbmachine.com/projects/
- Articles index: https://reverbmachine.com/articles/
- Eno Airports: https://reverbmachine.com/blog/deconstructing-brian-eno-music-for-airports/
- Eno Discreet: https://reverbmachine.com/blog/deconstructing-brian-enos-discreet-music/
- Vangelis: https://reverbmachine.com/blog/vangelis-tears-in-rain-blade-runner/ · video: https://www.youtube.com/watch?v=pcPWDdiQi8c
- Boards of Canada chord theory: https://reverbmachine.com/blog/boards-of-canada-chord-theory-part-one/
- Aphex Twin SAW: https://reverbmachine.com/blog/aphex-twin-selected-ambient-works-85-92/
- Chroma Campfire video: https://www.youtube.com/watch?v=TFJfcKmFxiU
