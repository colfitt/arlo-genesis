# Old Blood Noise Endeavors × Emily Hopkins Parting — Usage Guide

How people *actually* use Parting, to complement the spec/reference dossier in `Parting-DeepResearch.md`. In this rig it OPENS Board 2: the way to get the most out of it is to treat it as a **chance-driven texture *generator*** at the head of the chain — park **Chance at noon** for a reliable bed, or push it up for sound-on-sound chaos, and use **Dissolve** (bit-crush left / reverse right) as the signature "destroy it beautifully" control. The single most playable mode is **Envelope Shape**, where your picking dynamics gate the glitches — ideal for banjo rolls and baritone chords driving the buffer.

> Captured this wave: 7 video transcripts + 11 distilled link files (see §8). It's a **Jan-2026 pedal**, so coverage is demo-heavy and the two richest teaching resources are both first-party (Emily Hopkins + OBNE's own channel); genuine forum discussion is thin (Reddit returned nothing indexed; The Gear Page is paywalled; EffectsDatabase 403'd). All video attributions were re-verified via yt-dlp. Minor dossier touch-ups folded in (see §4 and the §6 resources note).

---

## 1. Essential workflows

**Understand the clock = the dice.** The modulation LFO is Parting's clock; every time the LED above Aux blinks, the pedal "rolls the dice" on whether a glitch-delay burst happens. **Rate sets how often it rolls.** **Chance** sets the odds and what enters the buffer: fully down = never; **noon = constant / surprise-free**; above noon = climbing chance of feeding *old* output back into itself, toward a chaotic sound-on-sound looper at max ([harp-lady official](transcripts/harp-lady-emily-hopkins-official-parting.md); [obne-dan-explains-it-all](transcripts/obne-dan-explains-it-all-parting.md)).

**Smear is the delay→reverb morph.** Turn it up and the delay taps diffuse into a genuinely lush reverb — a continuum, not a mode switch. "Turns the delay into essentially a reverb" at max.

**Dissolve — the heart ("destroy your signal in a beautiful way").** Center = clean. **Left = sample-rate reduction / bit-crush.** **Right = reverse delay that keeps dividing its clock into longer, more degraded reverse trails.** This duality was the central design idea ([harp-lady-pedals-that-inspired-parting](transcripts/harp-lady-pedals-that-inspired-parting.md)).

**Glitch = clock chaos.** Below noon: clean clock divide (half/normal/double → audible octave-up/-down jumps). Above noon: rising chance the clock is *randomly* reassigned + random sample-rate halving. And because Parting is digital, you can **Smear the pitch-shifting glitch delay into the reverb** so the octave jumps become part of the wash — Emily notes no other pedal does this.

**Envelope Shape = the playable mode.** Set Shape to Envelope and signal only enters the delay when you play loud; **Chance becomes the sensitivity/threshold.** The most dynamics-reactive, least random mode — best for plucked transients (harp, banjo).

**The two Mix modes (unique to Parting).** Standard = normal dry/wet. **Modified (LED lit) routes the *dry* signal through mod/bit-crush/reverse too** — so you can make a *pure* tremolo, *pure* bit-crush, or *pure* reverse of your tone. Emily calls this the feature that gives Parting "a strong personality but also extreme versatility" ([harp-lady-pedals-that-inspired-parting](transcripts/harp-lady-pedals-that-inspired-parting.md)).

**Reset the buffer fast.** Turning the **Time** knob is silent by design — Emily kept it that way specifically as a quick way to **reset/clear the delay buffer when feedback runs away**.

---

## 2. Signature settings

No preset-sharing platform exists and Parting is chance-driven, so published "settings" are **control-direction recipes**, not exact clock values. Clocks below are directional/inferred from documented behavior; named sounds attributed to source ([parting-named-sound-recipes](links/parting-named-sound-recipes.md); [russo-music](links/russo-music-parting-review.md)).

| Sound | Recipe (directional) |
|---|---|
| **Constant bed** (the "tame it" baseline) | Chance **noon**, Glitch below noon (normal clock), Smear up for reverb. Predictable, no surprise feedback |
| **Pseudo-synth chop** (darkwave) | Mod = **Tremolo**, Dissolve ~1–3:00 (into reverse), Rate moderate-fast, Shape Sine/Random Sine → "furious, shimmery chopping waves" |
| **Tape wow/flutter delay** | Dissolve just below noon (gentle grit), Mod = Vibrato slow/shallow, Chance ~noon, Smear ~9–11 → "reel slip-and-slide" |
| **Time-stretch / warp** | Glitch above noon (random reassignment), Dissolve above noon (reverse), Chance noon–1 → "warped blinks in the time-space continuum" |
| **Digital rubble** (bit-crush) | Dissolve ~8–9:00 (heavy crush), Filter **LP** ~1:00 to tame aliasing, Mix to taste |
| **Long reverse trail** | Dissolve ~3:00 (longest/most degraded reverse), Smear ~11–1 to bloom into reverb, Time moderate-long |
| **Chaos sound-on-sound wall** | Chance above noon toward max (old-signal feedback), Smear high — ride Mix/Chance to avoid runaway |

**Factory presets:** 3 onboard slots confirmed, but **no named factory-preset content is documented** anywhere as of mid-2026. (Marketing's "8 presets" is wrong; the manual's 3-onboard / 127-via-MIDI is authoritative.) See dossier §13 for four fuller rig-tuned starting points.

---

## 3. Power-user tips, tricks & hidden features

- **Expression maps any combination of knobs at once** (per-preset) — build a single heel→toe gesture (e.g. heel = clean-ish delay, toe = reverse + bit-crush + Smear-to-reverb + filter closing). This is the defining performance move; the EXP jack also accepts a momentary footswitch (OBNE Scooch) as external tap.
- **Feed it sustained / line-level sources.** Multiple reviewers note it "functions better as a synth effect than a guitar pedal" — sustained drones, bass, and VG-800 pad patches give the chance engine and Smear continuous material to build from ([matrixsynth-molten-music](links/matrixsynth-molten-music-parting.md)).
- **Run it in a loop.** Community tip: put Parting in a **send/return or inside another delay's feedback loop** with MIDI-synced randomness — it shines as a texture generator, not just an inline effect ([elektronauts](links/elektronauts-parting-thread.md)).
- **Dial heuristics:** slow Rate = drifting ambient; fast Rate = rhythmic/unpredictable; low Depth = subtle, high Depth = expressive ([deathcloud](links/deathcloud-parting-usage-notes.md)).
- **Hidden secondary controls** (hold Aux + turn): Rate→subdivisions, Depth→**stereo Width** of the modulation, Time→time-subdivisions. The tremolo stereo-width control exists specifically to avoid disorienting headphone ping-pong.
- **Aux** is assignable to Tap Tempo / Half-Speed / Preset switching.

---

## 4. Notable users & techniques

**VERIFIED — Emily Hopkins (co-designer; the whole point).** Classically-trained electroacoustic **harpist**/composer from Long Island; runs the "Harp Lady" YouTube channel (400K+ subs, started July 2019 — first upload was a Chase Bliss MOOD harp demo); scores for Ubisoft, The Line, and film. She **pioneered running classical harp through guitar pedals**, works mood-first/improvisation-first, and picks gear by "how compelling it is in creative applications" — surprise over surgical control. Parting is essentially her taste rendered as one box ([emily-hopkins-technique-background](links/emily-hopkins-technique-background.md); [emily-hopkins-design-intent](links/emily-hopkins-design-intent.md)).

Her own words on the design: *"Parting goes a lot further than putting my favorite effects together in one box… this really is a physical and a sonic representation of this entire journey I've been on."* Her stated essential pedals — **Chase Bliss MOOD MkII, EQD Avalanche Run, Blackskycraft Unusual EAS (bitcrusher), Empress Heavy Menace** — directly prefigure Parting's MOOD-style Chance buffer + Dissolve crush/reverse. Technique: long sustained plucked chords + fast rolls, reverse + bit-crush for "broken tape machine that's sad" textures, and she MIDI-syncs a second Parting to a drum machine.

**The design-lineage map** (from her own teardown, [harp-lady-pedals-that-inspired-parting](transcripts/harp-lady-pedals-that-inspired-parting.md)): bit-crushed reverb ← Unusual EAS / AC Noises Arma / OBNE Dark Star; reverse Dissolve ← Avalanche Run + OBNE BL44 (but cleaner); the octave-jump Glitch ← Flower/Flancher "double" + CB Thermae's clock-multiply; vibrato ← EQD Aqueduct; the non-resonant Filter ← Vongon.

**Attribution notes (verified via yt-dlp):** the canonical reference demo `rayDmE0T78o` is on **Emily's own "Harp Lady" channel** (dated 2026-01-21), titled "Old Blood Noise x Emily Hopkins - Parting" — i.e. it's the co-designer's own harp demo. And "A Pedal Made For Harp!? …Emily Hopkins" (`Tfu-pLCxXG4`) is a **JHS Pedals / Josh Scott** stream, *not* Emily playing, despite her name in the title.

It's a Jan-2026 pedal — beyond Emily Hopkins, the artist field is genuinely empty; no other users invented.

---

## 5. Rig-specific recipes (this banjo/baritone drone rig)

Slot: `[Board 1 / Deco V2 stereo out] → Parting → CB Lost & Found → Microcosm → Walrus QI → Dark Star V3`. **First setup step: set Routing = full Stereo** (hold On/Off + tap Preset to the third LED) so Parting preserves the Deco's L/R image at the head of the texture board; **trails on** for ambient use.

- **Banjo-as-lead in reverse.** Shape = **Envelope** so each banjo pluck gates the glitch; **Dissolve above noon** turns banjo rolls into stretched backwards arpeggios; **Filter LP ~1:00** rolls off banjo's 2–4 kHz spike before Microcosm granularizes it downstream. A signature texture this rig can produce.
- **Baritone Smear bloom.** Long sustained baritone chords + Smear high = lush delay→reverb; low fundamentals survive Dissolve's bit-crush as satisfying grit. Envelope Shape lets dynamics gate it.
- **Pre-granular fodder for the Microcosm.** Park Chance at noon for a *steady* degraded/reverse stream the Microcosm can reliably capture and loop — or push Chance high for chaos the Microcosm then freezes. Parting *generates*, Microcosm *granularizes* — keep their roles distinct.
- **Feedback discipline (three random pedals in a row).** With Lost & Found's random gating and the Microcosm right after, keep Parting's Chance near noon unless you specifically want stacked chaos — Parting Chance + Lost & Found + Microcosm modes all maxed turns unmusical fast.
- **OBNE-ecosystem bookends.** Parting (delay/glitch/reverse) opens Board 2 and the **Dark Star V3** (pad/reverb) closes it — same platform DNA (stereo, dry-through, expression-over-every-knob, MIDI). Map a single EXP morph on Parting and let the Dark Star smear/pitch-shift whatever it hands over.
- **Darken the whole wall (with a caveat).** To tone-tilt the entire stereo signal, use Mix = **Modified** + Filter LP — but accept that your dry also gets dissolved/modulated (the Filter only touches the wet path in Standard mode).

---

## 6. Best learning resources

The two richest teaching resources are first-party:
- **Emily Hopkins / "Harp Lady"** — [the official co-designer demo](transcripts/harp-lady-emily-hopkins-official-parting.md) (full control tour + harp), and [the design-lineage teardown](transcripts/harp-lady-pedals-that-inspired-parting.md) (what inspired every feature — the best single explainer of *why* each control behaves as it does).
- **Old Blood Noise Endeavors** — ["LIVE: Dan Explains It All ft. Emily Hopkins"](transcripts/obne-dan-explains-it-all-parting.md) (2026-01-28) — the authoritative knob-by-knob walkthrough. *(This OBNE official walkthrough wasn't in the dossier's demo list — added here.)*
- **collector//emitter (Ian Pritchard)** — [wordless ambient sound study](transcripts/collector-emitter-sound-study-parting.md) *(no captions — notes)* for hearing the range on guitar.
- **JHS / Josh Scott** — [strong endorsement + stereo/UI/format insight](transcripts/jhs-josh-scott-pedal-made-for-harp-parting.md). **PedalScapes** — [honest first-play learning-curve notes](transcripts/pedalscapes-parting-unboxing-first-play.md).

**Text — reviews (community is thin; these are the best accessible):**
- [Russo Music — Eric Lapp](links/russo-music-parting-review.md) — the best hands-on prose + the named-sound tone recipes.
- [Guitar Pedal X — Stefan Karlsson](links/guitarpedalx-parting-writeup.md) — lineage (5th square-format pedal) + the 3-preset resolution.
- [Elektronauts thread](links/elektronauts-parting-thread.md) — the one accessible community forum (small-sweet-spot + send-loop tips).
- [Gearnews](links/gearnews-parting-debut.md) / [Synth Anatomy via design-intent](links/emily-hopkins-design-intent.md) — Emily's design quotes.

---

## 7. Common pitfalls / gotchas

- **The sweet spot is small.** Owners note many knob combos are noise — "the sweet spot is small compared to the range of unusable sounds." Dial deliberately; learn the control directions ([elektronauts](links/elektronauts-parting-thread.md)).
- **Hard-to-read panel on a dark stage.** The James Roo art is gorgeous but the labels are low-contrast — memorize knob positions.
- **Runaway feedback.** Chance above noon climbs toward 100% old-signal feedback (sound-on-sound looper); ride Mix/Chance, or **turn Time to reset the buffer**.
- **Randomness = non-repeatable.** Two identical knob settings won't produce identical output — hard for parts that must be repeatable take-to-take. Park Chance at noon + Glitch below noon for consistency.
- **The Filter is non-resonant** — a clean 12 dB/oct LP/HP tilt, *not* a screaming resonant sweep or drone filter (this corrects the rig-art "Filter" framing).
- **Stereo Width can collapse to mono** if the Depth alt-control (Width) is set low — easy to leave narrow by accident on a stereo board. Set Routing to full Stereo and check Width.
- **350 mA hungry digital pedal** — needs an isolated 350 mA+ slot; don't daisy-chain it with other digital boxes on a marginal output.
- **USB-C is present but has no function yet** (reserved for future firmware). Single-version, first-run pedal — no firmware history.

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `harp-lady-emily-hopkins-official-parting.md` — Harp Lady (Emily Hopkins), 2026-01-21 — the official co-designer demo; full control tour + harp.
- `harp-lady-pedals-that-inspired-parting.md` — Harp Lady, 2026-03-10 — design-lineage teardown (best single explainer of every control).
- `obne-dan-explains-it-all-parting.md` — OBNE, 2026-01-28 — authoritative knob-by-knob walkthrough (Dan + Emily).
- `jhs-josh-scott-pedal-made-for-harp-parting.md` — JHS Pedals, 2026-03-25 — endorsement + stereo/UI/format insight.
- `pedalscapes-parting-unboxing-first-play.md` — PedalScapes, 2026-03-07 — unboxing + honest learning-curve notes.
- `collector-emitter-sound-study-parting.md` — collector//emitter (Ian Pritchard), 2026-01-21 — wordless ambient sound study *(notes only — no captions)*.
- `the-pedal-zone-parting-control-demo.md` — The Pedal Zone, 2026-01-21 — ~20-min control demo *(notes only — caption endpoint 429)*.

**Links** (`research/links/`):
- `emily-hopkins-design-intent.md` — Synth Anatomy — verbatim Hopkins design quotes + curation ethos.
- `emily-hopkins-technique-background.md` — SineSquares interview — richest bio/technique/gear list.
- `emily-hopkins-parting-demos.md` — YouTube (Harp Lady) — her demos + the Harp-Lady-vs-JHS attribution corrections.
- `parting-named-sound-recipes.md` — Russo + manual cross-check — 7 named-sound control recipes + Envelope mode + preset status.
- `obne-parting-official-copy.md` — oldbloodnoise.com — official voicing language; confirms no published settings.
- `russo-music-parting-review.md` — Eric Lapp — tape/synth/time-stretch tone recipes + descriptors.
- `elektronauts-parting-thread.md` — Elektronauts — the only accessible community forum; small-sweet-spot + send-loop tips.
- `matrixsynth-molten-music-parting.md` — MatrixSynth/Molten Music — bass/synth demo; "feed it sustained sources."
- `deathcloud-parting-usage-notes.md` — DeathCloud — beginner dial-in heuristics + 350 mA / Aux / expression confirmations.
- `guitarpedalx-parting-writeup.md` — Stefan Karlsson — lineage + 3-preset resolution.
- `gearnews-parting-debut.md` — Jef — design-intent framing + analog dry-through.

## Sources

All claims above cite a captured `transcripts/` or `links/` file. Original URLs are on the first line of each captured file; all video attributions were re-verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Parting-DeepResearch.md`](Parting-DeepResearch.md); the manual is at [`manuals/OBNE Parting.pdf`](../manuals/OBNE%20Parting.pdf).
