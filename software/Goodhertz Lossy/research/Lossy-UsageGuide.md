# Goodhertz Lossy — Usage Guide

Lossy is the rig's **codec/data-compression-artifact axis** — the one degrade tool
that does *digital* damage (MP3 spectral crush, "joint-stereo" swirl, packet
dropouts, dial-up/bad-stream glitch) that tape (SketchCassette II), the lo-fi suite
(RC-20), saturation (Decapitator), and bitcrush (NI Bite) genuinely can't. For this
degraded/"recorded-wrong" aesthetic its headline move is **automating Loss Amount
(or Loss Mode) from clean to destroyed across a section** — Goodhertz parameters are
zipper-free, so you can ride it on a stem *or the master bus* for a "signal falling
apart / sent over a bad connection / ripped from YouTube" arc. Honest scope: it's a
$79 special-interest **character** plugin ("love/hate — but when I love it, I love
it"), not an everyday insert. Tier-C single-pass; community depth is thin but the
manual + two strong tutorials cover it well.

## 1. What Lossy is + its controls

A **creative** codec-artifact effect — explicitly **NOT a real codec** ("not an MP3
codec checker"); it *generates the sound* of heavily compressed audio in a realtime,
automatable plugin. Origin: producer Tyler Duncan wanted a drum fill "like the year
2001 — a low-bitrate MP3 ripped from KaZaA." Signal flow ≈ Preprocess gain →
(Verb if Pre) → Filter → Loss → (Verb if Post) → out. `research/links/lossy-manual-reference.md`, `research/links/lossy-artists-and-origin.md`

**Loss section (the core):**
- **Loss Mode** — Standard · Inverse · **Phase Jitter** (the swirly/warbly artifact)
  · **Packet Repeat** (stutter) · **Packet Loss** (dropouts) · Standard + Packet
  Loss · Standard + Packet Repeat. Standard = the steady MP3-style spectral crush;
  the packet modes = intermittent "bad-connection" glitches; the hybrids combine
  both.
- **Loss Amount** — degradation intensity (the "bitrate/quality" knob in spirit;
  default 0%). **The prime automation target.**
- **Loss Speed** — the character knob: **slower = more spectral smear** (swirly,
  underwater), **faster = more garbled** (and at low/small settings you "start to
  hear the FX, pops and clicks in between"). Default 100%.
- **Loss Gain** — output (peak meter). `research/links/lossy-manual-reference.md`, `research/transcripts/lossy-adlibs-automation-missy.md`

**Filter section:** Normal (bandpass) or Inverted (bandreject); **Low Cut** (def 20
Hz) + **High Cut** (def 20 kHz) + a shared **Slope** (def 24 dB/Oct — steeper = more
abrupt/telephone-band, "jagged edgy" sound). This is your built-in
telephone/AM-radio bandlimiter. `research/links/lossy-manual-reference.md`

**Verb section:** built-in reverb with a **Pre/Post** switch — **Pre feeds the verb
INTO the loss** (the tail itself gets crushed → "fuller, more expansive," the
signature Lossy move), Post = conventional space after. **Verb Amount** + (advanced)
**Verb Decay** 0–200%. `research/links/lossy-manual-reference.md`

**Master:** **Master Mix** — a TRUE global dry/wet (def 100%; unlike SketchCassette,
which has none) + Master On/Off.

**Advanced page:** **Auto Gain** (keeps perceived volume up as info is removed — turn
up for heavy loss), **Gate Threshold** (def −96 dB; mutes the artifact/noise tail in
gaps → tighter, "jack-in-the-box" results), **Stereo Mode** (Stereo / **Joint Stereo**
/ Mono — Joint Stereo is the classic MP3 stereo-collapse / swirly-side artifact;
independent-Stereo loss gives the "VHS stutter" spread), **Weighting** (Perceptual =
psychoacoustic/codec-like, removes "least audible" first; Flat = even), Preprocess
Input + Postprocess Output gain. `research/links/lossy-manual-reference.md`, `research/transcripts/lossy-adlibs-automation-missy.md`

## 2. Creative use for the aesthetic

- **The Loss-Amount automation arc (THE move).** Ride Loss Amount (or jump Loss
  Mode) from clean → destroyed across a section for a "signal degrading / falling
  apart" build — on a stem or the master bus. Zipper-free automation makes this
  Lossy's headline edge over a real encoder. `research/links/lossy-artists-and-origin.md`, `research/transcripts/lossy-adlibs-automation-missy.md`
- **Clean → dirty contrast.** Keep one pass clean, automate Lossy *in* on the
  answer/repeat pass for momentum — or bring it in *mid-word* for a surprising
  in-line degrade. Works on banjo lead, vocal, any repeated phrase. `research/transcripts/lossy-adlibs-automation-missy.md`
- **Under-the-drone ambience crush** (the Lorde "Shapeshifter" technique): put Lossy
  on a *texture/ambience layer* (not the lead) to crunch it up so it sits dirty and
  far-off beneath a clean sustained wall. `research/links/lossy-artists-and-origin.md`
- **Master-bus codec-crush** (the Jane Remover *Frailty* technique): Lossy across the
  2-bus, low Mix, for whole-mix grit & "depth" — or automated up for the degraded
  sections. Sanctioned here because it has a real global Mix + Auto Gain. `research/links/lossy-artists-and-origin.md`
- **The "Internet Noise" bed:** Lossy on an *empty* track set to heavy loss/noise =
  a dial-up/static ambience floor under the mix. `research/links/lossy-tapetown-experimental-guide.md`
- **Degraded reverb throw:** Lossy on a dedicated throw track with high Verb Amount
  (Pre) → drag words/notes to it for a gritty, codec-smeared throw instead of a
  clean reverb. `research/transcripts/lossy-adlibs-automation-missy.md`

## 3. Copyable settings/recipes

Relative starting points — ride **Loss Amount** + **Master Mix** to taste after.
Factory presets in brackets are good launch pads. `research/links/lossy-manual-reference.md`, `research/links/lossy-tapetown-experimental-guide.md`

- **Subtle codec warmth** — Loss Mode Standard, Loss Amount low, Loss Speed ~100%,
  Master Mix ~30–50%, Auto Gain up, filters open. (≈ the *128 kbps* preset pulled
  back.) The always-usable "this was an MP3 once" stamp.
- **Heavy MP3-artifact bed** — Standard (or Standard + Packet Loss), Loss Amount
  high, **slow Loss Speed** for spectral smear, Joint Stereo for the swirly side
  collapse, Mix 100%. (≈ *32 kbps* / *Digital Garbage*.) The full degraded wall.
- **Telephone / streaming glitch** — Filter Normal with a tight Low Cut + High Cut
  (steep slope) for the band, **Packet Loss or Packet Repeat** for dropouts/stutter,
  moderate Loss Amount, Mono or Joint Stereo. (≈ *Bad Cell Connection* / *Bad Video
  Streaming* / *Can't Acquire Signal*.)
- **Lo-fi vocal/banjo** — Standard + a touch of **Phase Jitter**, moderate Loss
  Amount, **Gate Threshold up** so the artifact tail mutes in the gaps (tighter,
  jaggier), filters lightly narrowed. (≈ "Low-Fi" + jitter.) Banjo-as-lead "found in
  the dirt": same, plus automate Loss Amount up only where it should sound recorded
  wrong. `research/transcripts/lossy-adlibs-automation-missy.md`, `research/links/lossy-tapetown-experimental-guide.md`
- **Drone degrade (Pre-verb smear)** — Verb **Pre**, high Verb Amount + long Decay,
  Loss Mode Standard, **slow Loss Speed** (max smear), low–moderate Loss Amount, Mix
  ~50% blended under the drone. (≈ *Deep Space Network* / *Atlantic Cathedral* /
  *Infinite Hold*.) The verb tail itself gets Lossified → underwater-cathedral wash.

## 4. Lossy vs the other degrade tools (the niche)

These barely overlap — don't stack them fighting. `research/links/lossy-audiosex-alternatives-diy.md`, `research/links/lossy-kvr-questions-alternatives.md`

- **Lossy = CODEC/DATA-COMPRESSION artifacts** — MP3 spectral crush, joint-stereo
  swirl, phase jitter, packet dropouts/stutter, dial-up/bad-stream glitch, the
  pre-verb smear. *Nothing else in the rig does this.* Reach for it for the
  "recorded-wrong / sent over a bad connection / ripped from YouTube" sound and the
  zipper-free degrade-automation arc.
- **vs SketchCassette II (tape):** SC = *analog* wow/flutter/dropout/hiss realism,
  per-track only. Lossy = *digital* artifacts. Pair them — SC for the tape layer,
  Lossy for the codec layer — but don't expect SC to do MP3 swirl or Lossy to do
  capstan wobble.
- **vs RC-20 (lo-fi suite):** RC-20 is the broad lo-fi *suite* (noise, wobble,
  distort, basic bitcrush, space, tape) with a Magnitude macro. It overlaps Lossy
  *least* on the actual codec/MP3-artifact axis — RC-20's "Digital" module is plain
  bit/rate crush, not codec smear. Use RC-20 for general overt lo-fi; Lossy when you
  specifically want *MP3/streaming* character.
- **vs Decapitator (saturation):** different axis entirely — Decapitator = analog
  harmonic color/warmth. No motion, no digital artifacts.
- **vs NI Bite (bitcrush):** **bitcrush ≠ codec.** Bite reduces bit-depth/sample-rate
  (quantization/aliasing grit); Lossy throws away *perceptually-weighted spectral
  content* and adds codec-specific swirl/dropouts. Different damage — Bite for 8-bit
  crunch, Lossy for "bad MP3."
- **vs the hardware (Generation Loss / Big Time):** those are the *played-in,
  real-time, committed* degrade (and GenLoss is its own VHS/tape-codec flavor). The
  Chase Bliss **Lossy pedal** is the same engine hands-on + freeze/limiter for live;
  the **plugin** is the studio back-end — full recall, the advanced page, and
  automation. Use pedals/GenLoss on the way in; the Lossy plugin after the fact on
  stems/bus. `research/transcripts/lossy-plugin-vs-pedal-happymag.md`
- **vs the free DIY baseline:** you *can* just bounce to a low-bitrate MP3 (V0 /
  192 / 320) and re-import — more "authentic" to one real bitrate, but **destructive,
  offline, and un-automatable**. Lossy is the realtime/recallable/tweakable version
  that also goes far past any real encoder (packet loss, jitter, slow-speed smear,
  verb). Free rivals worth knowing: **Lese Codec** (free; one user rates it *above*
  Lossy musically), Unfiltered LO-FI-AF, MAIM; budget paid: **Aberrant Digitalis**
  ($24, the recurring "cheaper Lossy"). `research/links/lossy-audiosex-alternatives-diy.md`, `research/links/lossy-kvr-questions-alternatives.md`

## 5. Rig-specific recipes (your gear by name)

- **In Logic (AU):** Lossy is the AU; automate **Loss Amount** (and/or Loss Mode) for
  the clean→destroyed arc — zipper-free, so ride it hard. On the **stereo out** for
  the Jane-Remover whole-mix crush (low Mix + Auto Gain), or on a **texture aux** for
  the Lorde under-the-drone ambience crush. Light on CPU, but freeze/commit heavy or
  multiple instances for recall hygiene. `research/links/lossy-artists-and-origin.md`
- **Banjo-as-lead "found in the dirt":** Lossy on the stem — Standard + a little
  Phase Jitter, Gate Threshold up, automate Loss Amount up only where the lead should
  sound recorded-wrong; keep it clean on the important notes. `research/transcripts/lossy-adlibs-automation-missy.md`
- **Reamping / hardware-front chains:** record the pedalboard or OP-1/Digitakt/MPC/
  Octatrack clean(ish), then add Lossy on the return for the *codec* layer the analog
  front-end can't make (the digital-degrade complement to the played-in tape/GenLoss
  sound). Don't double the same artifact — pick the hardware codec-ish flavor
  (Generation Loss) OR Lossy per layer.
- **Sampling hardware into Kontakt/Logic:** run a recorded sample through Lossy
  (Standard, slow Speed, Joint Stereo) for an "old downloaded MP3" stamp before
  chopping. `research/links/lossy-tapetown-experimental-guide.md`
- **In Ableton Live 12 Lite (secondary):** works as VST3/AU; the Loss-Amount arc
  automates cleanly on a clip/scene; bounce/resample heavy chains to stay inside
  Lite's track ceiling.

## 6. Power-user tips & gotchas

- **Verb = Pre** is the underused trick — crushing the reverb tail (not just the dry)
  is what makes the smeared, underwater, "expansive" Lossy sound. `research/links/lossy-manual-reference.md`
- **Gate Threshold** turns a wash into something rhythmic/jagged by muting the
  artifact tail in the gaps — great for percussive or staccato sources. `research/transcripts/lossy-adlibs-automation-missy.md`
- **Auto Gain on** before pushing heavy loss, so the degrade doesn't drop your level.
- **Joint Stereo** is where the classic MP3 stereo-swirl lives; **independent Stereo**
  gives a wider "VHS stutter"; **Mono** collapses for a phone/AM feel.
- **Loss Speed is the character dial:** slow for smear/underwater, fast for garbled,
  small for audible pops/clicks — automate it for evolving texture.
- **Honesty / gotchas:** $79 special-interest plugin — a "love/hate" character tool,
  not an everyday insert; **limited factory preset bank**; some find the UI
  off-putting; first-load wants a Goodhertz account login (offline challenge/response
  auth exists). For one fixed real bitrate the free MP3-bounce-and-reimport is more
  authentic but un-automatable. **No verified drone/doom/shoegaze artist credit** —
  relevance is by *technique* (the Lorde ambience-crush + Jane Remover master-bus use)
  and the aesthetic, not a genre-peer endorsement. The Omar Apollo "Evergreen" claim
  is **unverified** — do not assert it. `research/links/lossy-kvr-questions-alternatives.md`, `research/links/lossy-artists-and-origin.md`

## 7. Best demos & resources

1. **Missy — "How To Mix PRO ADLIBS With Only ONE PLUGIN — GoodHertz LOSSY"** — by
   far the most practical: a full Pro Tools session showing the clean→dirty
   automation, mid-word transitions, the gritty reverb throw, master-fader automation,
   and a plain-English tour of every control (gate, stereo modes, speed). Rap genre,
   but the techniques transfer wholesale. `research/transcripts/lossy-adlibs-automation-missy.md`
2. **Happy Mag — "LOSSY: Goodhertz Plugin vs. Chase Bliss Pedal"** — cleanest recital
   of the control set + the plugin-vs-pedal (studio back-end vs played-in live)
   division of labor. `research/transcripts/lossy-plugin-vs-pedal-happymag.md`
3. **Official manual (manuals.goodhertz.com/3.13/lossy)** — the authoritative
   parameter + preset reference. `research/links/lossy-manual-reference.md`
4. **Tapetown Studio writeup** — the experimental/lo-fi recipe + preset pointers
   (and the artist examples — verify before trusting). `research/links/lossy-tapetown-experimental-guide.md`
5. **AudioSEX + KVR threads** — the alternatives map (Lese Codec, Digitalis, MAIM)
   and the DIY-MP3 baseline. `research/links/lossy-audiosex-alternatives-diy.md`, `research/links/lossy-kvr-questions-alternatives.md`

## 8. Captured sources

**Transcripts (2)** — `research/transcripts/`: lossy-adlibs-automation-missy (deepest
practical: automation, every control, the clean→dirty/throw/master tricks) ·
lossy-plugin-vs-pedal-happymag (control recital + plugin-vs-pedal split).

**Links (5)** — `research/links/`: lossy-manual-reference (authoritative params +
full preset list) · lossy-tapetown-experimental-guide (experimental recipes +
presets + artist examples) · lossy-audiosex-alternatives-diy (alternatives map +
the free DIY-MP3 method = the honest niche) · lossy-kvr-questions-alternatives
(budget alts Digitalis/MAIM + licensing + love/hate sentiment) · lossy-artists-and-
origin (KaZaA origin story, zipper-free automation, Lorde/Jane Remover VERIFIED +
Omar Apollo UNVERIFIED).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: Goodhertz official manual/site/FAQ,
Missy ad-libs tutorial, Happy Mag plugin-vs-pedal demo, Tapetown Studio, AudioSEX,
KVR Audio, Tape Notes Ep. 158 (Lorde/Jim-E Stack), Equipboard (Jane Remover).
**Honesty flags:** (1) thin community depth — a $79 special-interest character
plugin, fewer deep tutorials than a Soundtoys-tier product; (2) no verified
drone/doom/shoegaze artist credit (relevance is by technique + the aesthetic); (3)
the Omar Apollo "Evergreen" usage is single-source/unverified and is flagged, not
asserted; (4) two of the five demo videos found were music-only (no usable spoken
content) and were discarded.
