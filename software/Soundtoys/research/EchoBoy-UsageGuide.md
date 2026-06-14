# EchoBoy — Usage Guide

EchoBoy is the **in-the-box tape echo** for this rig — but its real value is
**character**, not clean repeats: 30 modeled styles + a Saturation section +
per-repeat EQ-Decay make it a tape-coloring engine, and it's *secretly a chorus,
a reverb, and a saturator* too. The Soundtoys creed — "echoes sound better when
the repeat does NOT sound like the input" — is exactly this rig's degraded /
"recorded-wrong" aesthetic. It sits as the **echo + chorus + color** stage
feeding a real reverb (Valhalla) and **complements** the hardware delays
(TimeLine / Big Time / Generation Loss / Deco) rather than replacing them. `research/links/echoboy-soundonsound-review.md`

## 1. Essential workflows (the core moves)

- **Character delay** — pick a Style for the vibe (tape/BBD/lo-fi/ambient), set
  time + a few repeats, blend. The Style + Saturation + Decay-EQ do the work.
- **Saturation-only color** (no delay) — Time 0, Feedback 0, Mix 100% wet → the
  Styles become pure tape/analog saturation. (See §3 for the latency caveat.) `research/transcripts/greenlightsound-bass-saturation.md`
- **Self-oscillation drone** — push Feedback toward runaway (Space Echo style),
  automate to infinite on a held note = endless wash usable as a pad. `research/transcripts/echoboy-6-tips-thomas-brett.md`
- **EchoBoy → Valhalla for walls** — EchoBoy as the character/echo stage *into* a
  true reverb (it can't make a smooth tail alone — repeats show through). `research/links/echoboy-as-reverb-ambient-gearspace.md`

## 2. Signature settings & presets (copyable)

**Style models** (30 total; full catalog in the manual): `research/links/echoboy-manual-tweak-panel-deep.md`
- *Tape:* **Master Tape** (ATR-102 @30ips, cleanest, saturates nicely) · **Studio
  Tape** (@15ips, dirtier "tracked-to-tape") · **EchoPlex** (EP-3 warm slap) ·
  **Space Echo** (RE-201, warm/gritty dub staple; self-oscillates on Feedback) ·
  **Tube Tape** (aggressive, high-mid distortion) · **Cheap Tape** (bright
  consumer cassette — the lo-fi pick).
- *Stompbox/BBD:* **Memory Man** (warm chorus-echo, the Edge sound — use Width as
  its chorus) · **DM-2** · **TelRay** (oil-can warble) · **Binsonette** (Echorec).
- *Lo-fi/"recorded-wrong":* Telephone · AM/FM Radio · Shortwave · **Transmitter**
  (CB-radio, distorted mids — good on synths).
- *Ambient/reverb:* **Ambient** ("distortion + diffusion, great for long feedback
  loops") · Diffused · Splattered · Verbed · **Limited** (built-in limiter —
  "great with high feedback," the runaway-tamer).
- *Chorus:* **CE-1 Chorus** (the Boss CE-1).

**Copyable recipes:** `research/transcripts/echoboy-6-tips-thomas-brett.md`, `research/links/echoboy-as-reverb-ambient-gearspace.md`
- *Tape slapback* — Single, EchoPlex/Studio Tape, 100–200 ms, 1–2 repeats, Width up.
- *Dub delay* — Space Echo, dotted-8th, moderate-high Feedback, drive Saturation;
  ride Feedback toward runaway for the "throw."
- *Dotted-8th ping-pong* — Ping-Pong, dotted-16th L / straight-16th R, Memory Man,
  lots of feedback.
- *Ambient wash / long-feedback drone* — **Ambient** (or Diffused), long time,
  high Feedback, **Diffusion in Loop**, High Cut to tame, **Prime Numbers ON** so
  the cloud thins instead of ringing one pitch. The factory **"EchoBoy's Galaxy"**
  preset is a ready prime-number high-feedback cloud.
- *Self-oscillating noise* — Space Echo, Feedback near max; **Limited** style to
  keep it from blowing up; automate Feedback on a held note.
- *Lo-fi degraded echo* — Cheap Tape / Transmitter, drive Input, narrow the EQ,
  add Random-Walk Wobble for cassette warble.
- *Saturation-only (Green Light bass patch)* — Single, Time 0, no feedback, Mix
  100% wet, **Input +6 dB**, Saturation ~12 o'clock, style **Cheap Tape**; in the
  Style Editor set **Decay Sat ≈ −8.4 dB, Out Sat ≈ +20–24 dB**, shape brightness
  with the 3-band EQ. `research/transcripts/greenlightsound-bass-saturation.md`

## 3. Power-user tips, tricks & hidden features

- **Saturation-only trick + the latency caveat:** Time 0 / Feedback 0 / 100% wet
  turns the Styles into tape colors — but **Width, Diffusion, and Wobble still
  inject delay at Time 0** and phase against a dry signal, so **zero them** (or run
  100% wet on a send). High Cut is **inverted** (max = most highs cut), and
  **Input drives the saturation stage** while Output trims after — keep Input at
  the 3rd green LED for clean, push into yellow/red for dirt. `research/links/echoboy-magneticmag-spotlight.md`, `research/transcripts/nathan-nyquist.md`
- **Tape generation-loss = Style-Editor Decay:** each EQ band has Gain (first
  repeat) + **Decay** (how that band evolves per repeat, needs Feedback up).
  **Negative High-Decay → each repeat darker** (authentic tape roll-off). The core
  evolving-tail control. `research/links/echoboy-soundonsound-review.md`
- **Diffusion Loop vs Post:** Post = every repeat equally smeared; **Loop =
  diffusion inside the feedback loop, so each repeat smears more than the last**
  (washing into reverb). Long time + Feedback + Diffusion = plate/hall. `research/links/echoboy-manual-tweak-panel-deep.md`
- **Wobble** (tape wow/flutter): slow Rate + low Depth + **Random Walk** shape =
  sauntering vintage drift; **FB/Out** toggles route it to the feedback path/
  wet-only; **Sync** CW = L/R out of phase (R pitches up as L pitches down) = rich
  chorus/flange. `research/links/echoboy-soundonsound-review.md`
- **Prime Numbers switch** de-aligns repeat times to kill resonant/comb build-up —
  essential for clean self-feeding ambient clouds and short-delay chorus. `research/links/echoboy-manual-tweak-panel-deep.md`
- **Rhythm Echo** = 16 taps ("16 tape heads") with **Shape** envelopes (Decay/
  Reverse/Swell/NonLin) + **Warp** to cluster taps (bouncing-ball / Aphex motion);
  sync to MIDI clock for generative tempo-locked delays. `research/links/echoboy-manual-tweak-panel-deep.md`
- **Feel / Accent / Groove** for off-grid tails: **Feel** = Rushin'/Draggin'
  (±pre-delay), **Accent** alternates repeat loudness on/off-beat. **Echo Time
  knob moved live = analog pitch-slide** (automate for tape-stop transitions). `research/links/echoboy-soundonsound-review.md`
- **Psychoacoustic depth:** high-cutting the repeats makes them recede ("move away
  from you") = depth without more reverb. `research/transcripts/echoboy-walkthrough-modes-overview.md`
- **Ducking** (no internal sidechain): on a send, follow with a **sidechain
  compressor keyed off the dry lead** (2–4 dB GR) so the delay tucks while the
  part plays and blooms in the gaps. `research/links/echoboy-proaudiofiles-tips-and-ducking.md`

## 4. Notable users & techniques (sourced, flagged)

- **Greg Wells** (Katy Perry, Adele) — "I'd be dead in the water without the
  **Memory Man preset** in EchoBoy"; uses the automated-feedback bloom into
  choruses. `research/links/echoboy-artists-sourced-uses.md`
- **Manny Marroquin** — "I also love the Valhalla reverb, the EchoBoy" — the exact
  EchoBoy→Valhalla chain this rig favors. `research/links/echoboy-artists-sourced-uses.md`
- **Tchad Blake** (Radiohead, Black Keys, Tom Waits) — EchoBoy for creative echo;
  **the most aesthetically aligned name** (dark, saturated, "recorded-wrong"
  mixes). Also **Jack Antonoff** (retro/lo-fi/saturated) and **Andrew Scheps**
  (longer delays). `research/links/echoboy-artists-sourced-uses.md`
- **Honest flag:** no *named* shoegaze/drone artist saying "I use EchoBoy"
  surfaced — genre relevance is by **technique** (Memory Man style,
  automated-feedback walls, saturation-as-color, Tchad-Blake degradation), not a
  name-drop. None invented. `research/links/echoboy-artists-sourced-uses.md`

## 5. Rig-specific recipes (your gear by name)

- **Software vs hardware echo — when to use which:** **EchoBoy** = recallable,
  automatable (feedback-to-infinity, pitch-slides), per-repeat EQ/Decay, the
  saturation-only color trick, infinite cheap voices → the **studio/back-end echo**
  on stems/reamps/in-the-box. **TimeLine / Big Time** = playable, performance-first
  centerpiece for hands-on dub/oscillation. **Generation Loss / Deco** = the
  literal tape-degradation hardware. Complementary, not redundant. `research/links/echoboy-vs-valhalla-delay-community.md`
- **EchoBoy → Valhalla for walls** (the Marroquin chain): EchoBoy can *imply*
  reverb (Diffused/Splattered/Galaxy) but the discrete repeats show through, so for
  a featureless wash **feed it into Valhalla** rather than asking it to be the
  reverb. `research/links/echoboy-as-reverb-ambient-gearspace.md`
- **Use the full EchoBoy, not EchoBoy Jr, for drone/shoegaze** — Jr is 7 curated
  styles, single-echo, **no Style Editor / Diffusion / Wobble / Prime Numbers /
  Rhythm modes**; it's a fast "stamp a color" tool, not a mangler. `research/links/echoboy-vs-echoboy-jr.md`
- **In Logic:** insert at Mix ~50%, or on a send at 100% wet with sidechain
  ducking; **freeze** tracks (Diffusion/Rhythm/many instances get CPU-heavy). The
  installed `.component` (AU) is correct — no VST needed.

## 6. Best learning resources

1. **Nathan Nyquist — "Use EchoBoy Like a Pro" (55 min)** — deepest; gain-staging,
   EQ-drives-saturation, Wobble Sync, Diffusion, EchoBoy-as-reverb. Best single
   resource.
2. **RealHomeRecording (29 min)** — send-vs-insert, the 55–95 ms "in-your-face"
   blend range, comb-filtering, prime-numbers/mono.
3. **The Pro Audio Files / Thomas Brett "6 Tips"** — the most copyable recipe set.
4. **Next Level Sound walkthrough** — signal flow + the "also a chorus/reverb"
   framing + Rhythm-mode drum programming.
5. **Green Light Sound** — focused saturation-without-delay demo with values.
6. Reference: the official EchoBoy v5 manual + the Sound on Sound review.

## 7. Common pitfalls / gotchas

- **Runaway feedback boosts output level a lot** — protect ears/monitors; tame
  with the **Limited** style or High Cut. `research/transcripts/echoboy-6-tips-thomas-brett.md`
- **Saturation-only at Time 0 still phases** if Width/Diffusion/Wobble are
  non-zero (they inject delay) — zero them or run 100% wet on a send.
- **High Cut is inverted** (max = most cut) and the Input→Saturation→Output
  gain-staging surprises people. `research/transcripts/nathan-nyquist.md`
- **It won't make a smooth reverb tail** — discrete repeats show through; pair with
  Valhalla. `research/links/echoboy-vs-valhalla-delay-community.md`
- **CPU** moderately heavy at scale (Diffusion/Rhythm/many instances) → freeze in
  Logic. **Ping-Pong sums input to mono** (stereo out); Single/Dual are
  true-stereo.

## 8. Captured sources

**Transcripts (5)** — `research/transcripts/`: nathan-nyquist (55-min deep dive) ·
realhomerecording (modes + blend range + send/insert) · echoboy-6-tips-thomas-brett
(copyable recipes) · echoboy-walkthrough-modes-overview (signal flow + chorus/
reverb framing) · greenlightsound-bass-saturation (saturation-only patch values).

**Links (8)** — `research/links/`: echoboy-manual-tweak-panel-deep (authoritative
style catalog + Edit-panel) · echoboy-soundonsound-review (generation-loss decay +
philosophy) · echoboy-magneticmag-spotlight (saturation-only trick, CE-1, Warp) ·
echoboy-proaudiofiles-tips-and-ducking (external ducking) · echoboy-as-reverb-
ambient-gearspace (ambient wash + Galaxy + limits) · echoboy-vs-valhalla-delay-
community (why-EchoBoy + where Valhalla wins) · echoboy-vs-echoboy-jr (feature
split) · echoboy-artists-sourced-uses (Wells/Marroquin/Blake/Antonoff/Scheps,
flagged).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: official EchoBoy v5 manual,
Sound on Sound, Nathan Nyquist, RealHomeRecording, The Pro Audio Files (Thomas
Brett), Green Light Sound, magneticmag, Soundtoys artist pages, KVR/Gearspace.
**Honesty flags:** Gearspace/Equipboard 403 direct fetch (distilled from snippets,
flagged in-file); no named drone/shoegaze artist verified — genre relevance is by
technique; EchoBoy is acknowledged as harder to learn than peer delays.
