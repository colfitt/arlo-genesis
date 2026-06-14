# Nudistort — Usage Guide

Nudist Audio **Nudistort** (dev Caleb Reske) is the rig's **generative-chaos**
box — a single-band **nonlinear/time-varying distortion + an "abnormal" delay +
modulation** that the maker himself calls "distortion" a misnomer for ("a
Rube-Goldberg machine of cascading audio"). The community verdict is unanimous:
**no direct equivalent.** For this rig it's the recallable, in-the-box *mangler*
— ring-mod, self-oscillating delay drones, telecom grit, note-keyed resampling —
that complements Decapitator (predictable analog color) and the hardware fuzzes
(the performed wall). Same knobs ≠ same result: treat it as a collaborator, start
from presets, audition by sweeping.

> Filed under Nudist Audio after a repo mis-grouping (`com.NudistAudio.Nudistort`,
> not Devious Machines); see `research/links/nudistort-brand-misattribution.md`.

## 1. What it is & architecture

Three stacked engines feeding a reactive visualizer: `research/links/nudistort-feature-reference.md`, `research/links/nudistort-waveinformer-review.md`
- **DISTORT** — `Drive` (**non-monotonic** — higher ≠ more distorted), `Type`
  (4 algorithms A–D, each very different), `Mode` (**T/P** per Type → 8 flavors;
  T = traditional, P = unpredictable/expressive), `Grain` (alters micro-timing/
  feel, unique per Type — *not* granular), `Damping` (tames transient harshness
  **and** acts as a tone/voicing control), `Mix`.
- **DELAY** (a real second engine) — `Time` (<90 ms = comb/"oil-can" tone-shaping;
  higher = chordal/harmonic spread), **`Abnormality`** (clean delay → "harmonically
  recombined chaos"), `Feedback` (high FB + high Abnormality = **self-oscillating**
  "beautiful disorder"), 4 types, `Sync`, L/R offset.
- **GLOBAL / mod knobs** — `Tone` (**pre**-distortion tilt EQ), **`Mu-law`**
  (telecom companding — lo-fi/bitcrush-adjacent grit), `Buzz` (amp noise), `Wobble`
  (tape pitch mod), `Mod Amount/Freq` (trem/ring-mod-ish), **`Noodle`** (pitch-
  following sine added pre-distortion — best in **envelope mode**), **`Species`**
  (note-keyed harmonic resampling — set to the **tonic** of the track).

There is **no multiband split, no crossovers, no per-band dynamics** — the brief's
"multiband + envelope dynamics" premise was the mis-attribution; the real plugin is
single-band and chaotic. `research/links/nudistort-feature-reference.md`

## 2. Essential workflows

- **Drone wall / self-oscillation** — Delay **high Feedback + high Abnormality** →
  spiralling "beautiful disorder"; layer **Species = tonic** for hypnotic harmonic
  locking. Banjo/baritone sustain → endless evolving drone. `research/transcripts/nudistort-boring-gear-reviews.md`
- **"Recorded-wrong" grit** — `Mu-law` + `Buzz` + dark `Tone` = telecom/degraded
  lo-fi (the most rig-aligned use). `research/links/nudistort-waveinformer-review.md`
- **On reverb/delay sends** — the vendor/WaveInformer headline rec: mangle the
  *wash*, not the dry source. Distortion-before-reverb = crunch then smear; reverb-
  before-Nudistort = mangle the tail itself. `research/links/nudistort-chaining-and-rig-placement.md`
- **Subtle saturation** — keep all the **Mix** knobs low; nudge `Grain` + `Mu-law`,
  `Drive` low ("great on bass, on the lowest/minimum-weird settings").

## 3. Signature settings & presets

The plugin is **deliberately non-deterministic**, so think "starting zones," not
exact patches: `research/transcripts/nudistort-boring-gear-reviews.md`, `research/transcripts/nudistort-noise-kitchen-review.md`
- **The "organic" formula** (most-cited): **Grain + Mu-law + Noodle(envelope) + the
  three Mix knobs** are the controls that matter.
- *Metallic / oil-can space* — Delay `Time` <90 ms, moderate Abnormality (comb-
  filtered robotic verb).
- *Massive sludge* — high `Drive` swept against `Damping` to find a throaty HM-2-ish
  spot; pair with a big pre-delay reverb (→ your Valhalla wall).
- *Ring/C8 textures* — the Mode-P algorithms + Mod for inharmonic tones.
- Factory presets are named **"minimum / medium / maximum weird"**; use **Mix Lock**
  to audition them at a fixed parallel blend.
- **★ Do NOT trust AI "Drive/Bias/Tilt %" recipes** — there is **no Bias knob**;
  those circulating numbers are confabulated. `research/links/nudistort-feature-reference.md`

## 4. Power-user tips, tricks & hidden features

- **Drive is non-monotonic** — sweep to find the spot; subtle settings are often the
  weirdest. `research/links/nudistort-waveinformer-review.md`
- **Damping is a tone/EQ move** — "just by controlling Damping the EQ changed
  totally"; it's how you voice the distortion. `research/transcripts/nudistort-boring-gear-reviews.md`
- **Mix Lock** — locks wet/dry so you can swap Types/Modes/presets at a fixed
  parallel grit (the practical parallel-distortion workflow). `research/transcripts/nudistort-noise-kitchen-review.md`
- **Pre-EQ into the drive matters** — the distortion reacts to what you feed it;
  the built-in `Tone` is *pre*-distortion, and a low-pass ahead of it tames the fizz. `research/transcripts/nudistort-noise-kitchen-review.md`
- **Species = tonic** for harmonic lock; **Noodle in envelope mode** = a pitch-
  tracking "spectral shadow" that follows dynamics. `research/links/nudistort-feature-reference.md`
- **Very low CPU** for this much nonlinear processing (repeatedly cited). `research/links/nudistort-kvr-thread.md`

## 5. Notable users & techniques (sourced, flagged)

- **Andrew Huang** — Nudistort was **#7 in his Top 10 Plugins of 2024** and he built
  an official preset bank. (HIGH) `research/links/nudistort-artists-and-developer.md`
- **Factory preset authors** (names on presets ≠ proof of records): **Kenny Beats,
  Romil Hemnani (BROCKHAMPTON), Psymun, Shane Becker, Doug Schadt (Maggie Rogers/
  Wet), Reske.** Skew = experimental hip-hop / alt-pop / electronic. `research/links/nudistort-artists-and-developer.md`
- **Honest flag:** no named doom/drone/shoegaze artist surfaced (2024 plugin,
  electronic-leaning adoption). Relevance is by **technique** (droning sustains,
  distorted-delay washes, send-mangling) — the Boring Gear demo's sustained-guitar
  drone use is the closest aesthetic bridge. None invented. `research/links/nudistort-artists-and-developer.md`

## 6. Rig-specific recipes & "which distortion when"

- **vs Decapitator** — Decapitator = predictable **analog harmonic color/warmth**
  (shines when *not* fully distorting); Nudistort = **unpredictable nonlinear
  destruction/texture + a weird delay.** Zero overlap → stack them (color → chaos,
  or mangle → re-glue). `research/links/nudistort-chaining-and-rig-placement.md`
- **vs RC-20** — RC-20 = lo-fi *degradation motion* (wobble/noise/dropout); Nudistort
  is far more aggressive/alien and brings a delay RC-20 lacks. "Old broken tape" vs
  "broken in a way you've never heard."
- **vs Hizumitas / MXR 108 / Colour Box V2** — those are committed, pick-dynamic,
  feedback-interactive front-end character you **print by performing**; Nudistort is
  recallable/automatable studio mangling that does things no fuzz can (ring-mod,
  abnormal delay, Species). Fuzz for the performed wall, Nudistort for studio chaos. `research/links/nudistort-community-sentiment-comparisons.md`
- **Per-string** — run each string of the **GK-5 → VG-800 hexaphonic** banjo/baritone
  through its own Nudistort (WaveInformer demoed exactly this with a hexaphonic
  pickup). `research/links/nudistort-chaining-and-rig-placement.md`
- **Mud control** — full-range, no multiband: high-pass into it / low-pass the wet on
  bass, one lead-dirt per source.

## 7. Best learning resources

1. **WaveInformer review** (text, Apr 2025) — deepest control-by-control + per-source
   recipes + the EchoBoy-vs-Nudistort delay verdict.
2. **Boring Gear Reviews — "You've NEVER Heard Anything Like This!"** — 4 preset
   walkthroughs (Feedback Reverb / ring / oil-can delay / HM-2 sludge).
3. **Noise Kitchen — "The Nudistort Review"** — live Logic sound-design jam; reveals
   Mix Lock, the "weird" preset naming, pre-EQ-into-drive, commit-to-tape.
4. **Nudist Audio's own tutorial** (`youtube.com/watch?v=0nu7996-o_U`) — canonical,
   but auto-subs were 429-rate-limited (retry to capture).

## 8. Common pitfalls / gotchas

- **Unpredictable by design** — not for clean/linear work; start from presets. `research/links/nudistort-kvr-thread.md`
- **Delay runaway** — high Feedback + Abnormality spirals fast; automate/gate `Feedback`. `research/transcripts/nudistort-boring-gear-reviews.md`
- **No multiband / no oversampling toggle** — manage lows manually; can alias (that's
  the character). `research/links/nudistort-feature-reference.md`
- **★ AI-confabulated "Bias knob" recipes** — ignore any "Drive/Bias/Tilt %" values;
  no Bias control exists. `research/links/nudistort-feature-reference.md`
- **Thin Reddit footprint** — discussion lives on KVR/VI-Control/Gearspace/YouTube
  (some 403 direct fetch; distilled from snippets). `research/links/nudistort-kvr-thread.md`

## 9. Captured sources

**Transcripts (2)** — `research/transcripts/`: nudistort-boring-gear-reviews
(4-preset hands-on; Damping-as-EQ; drone) · nudistort-noise-kitchen-review (live
Logic jam; Mix Lock, pre-EQ-into-drive, commit-to-tape).

**Links (7)** — `research/links/`: nudistort-brand-misattribution (Nudist-Audio-not-
Devious proof) · nudistort-feature-reference (full control set + Bias-confabulation
flag + low-CPU) · nudistort-waveinformer-review (deepest review + per-source) ·
nudistort-chaining-and-rig-placement (placement, send-mangling, per-string, "which
dirt when") · nudistort-community-sentiment-comparisons (the "no equivalent" signal)
· nudistort-kvr-thread (reception + install gotcha) · nudistort-artists-and-developer
(Caleb Reske, Andrew Huang #7/presets, preset roster, doom/shoegaze honesty flag).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: WaveInformer, Boring Gear Reviews,
Noise Kitchen, KVR / VI-Control / Gearspace, Nudist Audio's site. **Honesty flags:**
the official vendor tutorial transcript is missing (YouTube 429); no public PDF
manual; no named drone/shoegaze artist (technique-relevant only); numeric "recipes"
online are largely AI-confabulated (the fake "Bias knob") and are NOT used here.
