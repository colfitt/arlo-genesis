# iZotope Ozone 11 — Usage Guide

> **Scope note:** Despite the folder name "iZotope (suite)," only **Ozone 11** is
> actually installed (VST3 + the `iZOzone11AUHook.component` AU bridge; verified in
> `Software/_inventory.json`). The "Vocal De-Esser/Reverb/Prep" plugins that were once
> grouped under iZotope are **Antares** (different vendor), and **RX / Nectar are NOT
> installed**. So this is the **Ozone wave**. (You also own **Ozone 11 Standard** inside
> Komplete — same module family, fewer modules; the Advanced-only Vintage modules + Match
> EQ + Stabilizer live in the full Ozone 11 build covered here.)

Ozone is a **mastering suite** — a hostable rack of master-bus modules (EQ, Dynamics,
Maximizer/limiter, Imager, Exciter, Low End Focus, the Vintage Tape/EQ/Comp/Limiter, plus
the Master Assistant / Tonal Balance AI). You are **not** a mastering engineer making
loud, clean records — you make degraded, sustained, lo-fi walls. So Ozone's job here is
**not loudness**: it's (1) gentle **glue + analog color** on a bounce, (2) **tonal/level
consistency** across a release, (3) **widening** the wall, and (4) **cleaning a muddy
drone low end** — all without crushing the intentional dynamics or scrubbing the grit. The
single biggest insight for this rig: **every module can run as a standalone insert on a
bus**, so Ozone is really a box of creative tone-shapers, not just a master strip.

---

## 1. Essential workflows

**A. The "fast sketch then undo half of it" master (recommended default).**
Drop Ozone on the master/stereo bus → click the **Master Assistant** (circular/globe
button) → **Custom** → choose **Vintage** intent + **Low** intensity (seeds the chain with
the *colored* modules, not clinical ones) → set Analysis Time to your loudest swell → set
loudness target to **-14 LUFS** (not -9) → Play to analyze. Then **"Enter the Ozone,"** turn
on **Gain Match**, and aggressively prune: bypass anything that flattens the dynamics, pull
the **Maximizer** back to ≤2-3 dB gain reduction, and keep only what helps (usually
Vintage Tape + a gentle EQ trim + maybe Low End Focus). MA is trained on commercial hits,
so it *will* over-master a drone — treat its output as a starting sketch, not a finish.
[ozone-master-assistant-workflow.md, ozone-10-steps-quick-master.md]

**B. Ozone-as-insert (the creative path).** Instead of the whole suite on the master, drop a
**single module** on a bus — Vintage Tape on the guitar wall, Imager on the reverb return,
Low End Focus on the drone bass. This is where Ozone earns its place in textural music.
[ozone-vintage-modules-4-uses.md, ozone-imager-6-tips.md]

**C. Release consistency (the real "mastering" job for this music).** For an album/EP,
the goal is **not** loudness — it's making the tracks belong together. Line them up, use
**Tonal Balance Control** + gentle EQ / **Match EQ** to pull them into the same tonal space
without flattening each track's character, and limit only to catch wayward peaks.
[ozone-mastering-ambient-kvr.md, ozone-low-end-focus.md]

---

## 2. Signature presets & settings (copyable)

**Vintage Tape — "glue + warmth" (master or wall bus)** — iZotope's own example:
- Speed **30 IPS** (preserves top, cleans lows, firms the kick/sub) · Input Drive **+4 dB**
  · Bias **-0.5** (tilts distortion to the highs, pushes the mids) · Harmonics **2.0**
  (density) · Low Emphasis **0.5** · High Emphasis **2.5**.
- For a **warmer/lo-fi** tilt instead: switch to **15 IPS** (warmer, more saturation, more
  low-freq distortion — "15 can be lo-fi"), push **Input Drive** up, and use a **positive
  Bias** to thicken the low end and tame shriek/harshness. [ozone-vintage-modules-4-uses.md,
  transcripts: music-tech-help-guy, ozone8-tut04, coming-to-it]

**Maximizer — "loud-ish without squash"** — Ceiling **-1.0 dB** (down to -2.0 if you'll
encode to MP3/AAC); **Learn Threshold** set to **-14 LUFS**; keep gain reduction **≤3-4 dB**
at peaks; raise the **Sustain** slider so the limiter rides the swell of pads/drones instead
of grabbing it; raise **Transient** if there are banjo plucks / hits to protect.
[ozone-maximizer-settings-splice.md]

**Imager — "widen the wall, keep the sub mono"** — Band 1 (sub) Width **0%** (mono); widen
the upper bands of the guitar/synth wall modestly; on the **master**, keep Width ≤ **~25%**
and check the correlation meter. To turn a mono source stereo, use **Stereoize Mode II at
~50-60%**. [ozone-imager-6-tips.md]

**Low End Focus — "de-mud a drone"** — **Smooth** mode, **Contrast** modest, frequency
markers narrowed onto the boomy band inside **20-300 Hz**, **Mid-Side** so you clean the
sides without touching the mono rumble. [ozone-low-end-focus.md]

**Vintage Limiter (Fairchild 670 style)** — use *instead of* the Maximizer when you want
weight + vibe rather than transparency: soft knee, program-dependent attack/release, tube
harmonics. Glues + adds density while reducing the level demand. [ozone-vintage-modules-4-uses.md]

---

## 3. Power-user tips, tricks & hidden features

- **Upward expansion = put life BACK.** In the Dynamics module drop the **Limiter ratio
  below 1.0:1** (and bypass the Compressor: ratio 1.0:1, threshold -130 dB) to *expand*
  transients upward across 3-4 bands (fast attack 0.5-10 ms, release 50-100 ms). Great for
  re-animating an over-limited bounce. [ozone-advanced-mastering-tips.md]
- **Mixed-phase EQ for diffusion.** The digital EQ's phase slider blends linear (0%) ↔
  minimum (100%) phase. Leaning **minimum-phase** smears/diffuses the image — useful on a
  wall; **linear** preserves spatial precision. [ozone-advanced-mastering-tips.md]
- **Transient/Sustain imaging.** The Imager can width the **sustain** (the wall/tails)
  independently from transients per band — widen the body of the drone without smearing
  the few transients. [ozone-advanced-mastering-tips.md]
- **Every module is a standalone insert.** You don't need the whole suite — load just
  Vintage Tape, just the Imager, just Low End Focus on any track/bus. [ozone-vintage-modules-4-uses.md]
- **Custom reference target.** In Master Assistant, hit **"+"** in Targets and upload a
  reference drone/ambient record you like — MA matches its tone/width/dynamics/loudness
  instead of forcing a pop "genre target." (No vocal-balance target gets made from a custom
  ref.) [ozone-master-assistant-workflow.md]
- **Vintage Tape Bias is a tone control, not just distortion.** Negative bias = more
  high-frequency emphasis *and* more HF distortion (air + edge); positive bias = stronger
  low end, less highs, but over-biasing kills dynamics. Roll bias **up** for bass-shy
  material, **down/zero** for material lacking air. [transcript: music-tech-help-guy]
- **Gain Match always.** A louder output always sounds "better" — turn on Gain Match before
  judging any module. [ozone-10-steps-quick-master.md]

---

## 4. Rig-specific recipes

> Host = **Logic Pro (AU)**; the `iZOzone11AUHook.component` is the AU bridge. Secondary
> Ableton Live 12 Lite. Tie these to the actual drone/doom/shoegaze workflow.

- **Master-bus glue for a drone track (the everyday move).** On the Logic stereo-out:
  **Vintage Tape** (Speed 30 IPS, Drive ~+4 dB, Bias -0.5, Harmonics 2.0) → a 1-2 dB
  broad **EQ** trim → **Vintage Limiter** OR a barely-moving **Maximizer** (Ceiling -1.0,
  ≤3 dB GR, Sustain up). Aim ~**-14 LUFS** and stop. The grit survives; the bounce just
  feels glued. [ozone-tape-emulation-creative.md, ozone-vintage-modules-4-uses.md,
  ozone-maximizer-settings-splice.md]
- **Vintage-tape character on the guitar/banjo wall (not the master).** Insert Vintage
  Tape on the *wall bus* and drive it from "glue" toward "saturation" — low-end bump +
  softened highs add the analog warmth the digital signal lacks. This complements the
  hardware tape in the chain (**Chase Bliss Big Time**, **Chase Bliss Generation Loss**
  tones, the Strymon **Deco**) — use the pedals for character while tracking/reamping, and
  Ozone Tape for the final sweetening. [ozone-tape-emulation-creative.md, transcripts]
- **Widen a wall.** Put the **Imager** on the *reverb/delay return* (Width up, Stereoize
  OFF) for "larger-than-life space," rather than widening the dry source. Keep the sub band
  mono. Pairs with the hardware ambience (**Big Sky**, **Microcosm**, **QI Etherealizer**)
  feeding that return. [ozone-imager-6-tips.md]
- **Tame a muddy banjo/synth drone low end.** **Low End Focus**, Smooth mode, Mid-Side,
  markers on the boom — cleans the mud between notes without gutting the sustained rumble,
  which plain EQ struggles to do. [ozone-low-end-focus.md]
- **"Recorded-wrong" extreme.** Slam **Vintage Tape** into all-out distortion on a stem
  (or a resampled hardware loop from the **Digitakt / Octatrack / MPC**) for crushed lo-fi
  color, then blend under the dry. Pair with **SketchCassette II** / **RC-20** already in
  the rig. [ozone-tape-emulation-creative.md]
- **Album/EP consistency pass.** Use **Tonal Balance Control** + **Match EQ** across the
  release to seat each track in the same tonal space; limit only to catch peaks. This is
  the genuinely useful "mastering" job for a drone record. [ozone-mastering-ambient-kvr.md]

---

## 5. Common pitfalls / gotchas

- **Don't over-master degraded music.** The whole community consensus for ambient/drone:
  *far less limiting*, "stop chasing the numbers," let it breathe. If a processor has to
  work hard, the **mix** needs more headroom — go back, don't crush at the master.
  [ozone-mastering-ambient-kvr.md]
- **The Maximizer is the least useful module for this rig.** It squashes the intentional
  swells. Keep GR ≤3-4 dB or skip it for the Vintage Limiter. [ozone-maximizer-settings-splice.md]
- **Loudness is mostly pointless under streaming normalization.** Spotify/Tidal -14,
  YouTube -13, Apple -16 LUFS — a crushed -8 master gets turned *down* to match, so you
  lose dynamics for nothing. Master to ~-14 (or quieter) and keep the grit.
  [ozone-maximizer-settings-splice.md]
- **Bass drones distort first.** Limiting/clipping artifacts show up earliest in extended
  low end — watch the sub, set a safe ceiling, consider Low End Focus before the limiter.
  [ozone-mastering-ambient-kvr.md]
- **Widening loses level in mono / can phase-cancel.** Never widen mix fundamentals or the
  sub; watch the correlation meter; keep master Width subtle (~25%). [ozone-imager-6-tips.md]
- **Vintage modules are Advanced-only.** The Vintage Tape/EQ/Comp/Limiter, Match EQ, and
  Stabilizer require the full **Ozone Advanced** build — the **Ozone 11 Standard** that
  ships in Komplete won't have them all. (You have the full Ozone 11 here.) [transcripts]
- **Logic = AU-only.** Ozone loads via the `iZOzone11AUHook.component` AU bridge; the VST3
  is for other hosts. Fine in Logic, but if a project ever loses the plugin, check the AU
  component is present/validated. [_inventory.json]

---

## 6. Best learning resources

- **iZotope Learn — "4 Uses for Ozone's Vintage Modules"** — the single best page for this
  rig: concrete Vintage Tape/Comp/EQ/Limiter settings + the glue/character framing.
  [ozone-vintage-modules-4-uses.md]
- **iZotope Learn — "5 Advanced Mastering Tips"** — upward expansion / mixed-phase EQ /
  transient-sustain imaging: the "add life back" tricks. [ozone-advanced-mastering-tips.md]
- **iZotope Learn — Master Assistant / Low End Focus / Imager pages** — the official
  module workflows. [ozone-master-assistant-workflow.md, ozone-low-end-focus.md,
  ozone-imager-6-tips.md]
- **Splice — Ozone Maximizer basics** — the Sustain slider + safe-loudness practice.
  [ozone-maximizer-settings-splice.md]
- **KVR thread "Mastering techniques for ambient music?"** — the honest community take on
  *not* over-mastering drone. [ozone-mastering-ambient-kvr.md]
- **YouTube Vintage Tape walkthroughs** — "Music Tech Help Guy" (Ozone 7, best control-by-
  control), plus two Ozone 8 walkthroughs. [transcripts/]

---

## 7. Captured sources

**Transcripts** (`research/transcripts/`):
- `ozone-vintage-tape-music-tech-help-guy.md` — Music Tech Help Guy, Ozone 7 #05 Vintage
  Tape (most detailed: Drive/Bias/Speed/Harmonics/Low+High Emphasis, on drums/vocals/bus).
- `ozone-vintage-tape-coming-to-it.md` — "Coming To It," Ozone 8 Vintage Tape module.
- `ozone-vintage-tape-ozone8-tut04.md` — Ozone 8 Tutorial 04, Vintage Tape.

**Links** (`research/links/`):
- `ozone-vintage-modules-4-uses.md` — iZotope, 4 Vintage modules + concrete Tape settings.
- `ozone-advanced-mastering-tips.md` — iZotope, 5 advanced Dynamics/EQ/Imager tricks.
- `ozone-imager-6-tips.md` — iZotope, Imager widening / Stereoize.
- `ozone-master-assistant-workflow.md` — iZotope, Master Assistant + custom reference.
- `ozone-maximizer-settings-splice.md` — Splice, Maximizer / Sustain / LUFS.
- `ozone-low-end-focus.md` — iZotope (+ Black Ghost Audio), Low End Focus + extra tricks.
- `ozone-tape-emulation-creative.md` — iZotope, tape-emulation intensity map.
- `ozone-mastering-ambient-kvr.md` — KVR, ambient-mastering restraint (honest niche).
- `ozone-10-steps-quick-master.md` — iZotope, end-to-end quick-master skeleton.

## Sources

- iZotope Learn: 4 Uses for Vintage Modules — https://www.izotope.com/en/learn/4-uses-for-ozones-vintage-modules.html
- iZotope Learn: 5 Advanced Mastering Tips — https://www.izotope.com/en/learn/advanced-mastering-tips.html
- iZotope Learn: 6 Tips for Imager — https://www.izotope.com/en/learn/6-tips-for-using-imager-in-ozone-9
- iZotope Learn: How to use Master Assistant — https://www.izotope.com/en/learn/how-to-use-master-assistant-in-ozone.html
- iZotope Learn: Mastering Bass with Low End Focus — https://www.izotope.com/en/learn/mastering-bass-with-low-end-focus.html
- iZotope Learn: 10 Steps to a Quick Master — https://www.izotope.com/en/learn/10-steps-to-a-quick-master-in-ozone.html
- iZotope Blog: Tape Emulation (subtle→saturated) — https://www.izotope.com/community/blog/tape-emulation
- Splice: Ozone Maximizer basics — https://splice.com/blog/mastering-ozone-elements-maximizer/
- Black Ghost Audio: 5 Mastering Tricks Using Ozone 9 — https://www.blackghostaudio.com/blog/5-mastering-tricks-using-ozone-9
- KVR: Mastering techniques for ambient music — https://www.kvraudio.com/forum/viewtopic.php?t=531959
- YouTube (Vintage Tape): https://www.youtube.com/watch?v=73IxWW9t340 · https://www.youtube.com/watch?v=PGrRjog1wjs · https://www.youtube.com/watch?v=fGRg_yxrcEk
