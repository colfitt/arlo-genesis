# Chase Bliss MOOD MkII — Usage Guide

The MOOD MkII is two effects in one box, played like an instrument: a **Wet Channel**
(Reverb / Delay / Slip) and an always-listening **Micro-Looper** (Tape / Stretch / Env),
blended by **MIX** and unified by the **CLOCK** knob (sample rate → it sets the loop length
*and* the wet quality at once). There is **no knob labeled "MOOD."** It rewards improvisation,
not recall — "fish for music," freeze a moment, play over it, and capture it with the
upstream/Wet effects baked in. In this rig it turns a banjo/baritone phrase into an evolving
bed; keep wide-stereo intent for later stages since the **mono Blooper downstream collapses
its stereo**. Andy Othling (who authored its factory presets) is the voice to study.

> Architecture clarification (a common mix-up): **LEFT footswitch/side = Wet Channel**,
> **RIGHT = Micro-Looper**; **MIX** = dry↔MOOD blend, **CLOCK** = master sample-rate/character.
> Lower CLOCK = grittier/longer loops; higher = cleaner/shorter. *(video-manual-pt1)*

> Firmware: **1.1 (free)** restores the original MkI **Stretch** character inside **Classic
> Mode** (stock 1.0 Stretch "confused people"); the updater was rebuilt at
> firmware.chasebliss.com. *(firmware-1-1-stretch-restore)*

---

## 1. Essential workflows

### The two channels + modes (official video manual)
**Wet Channel (TIME / MODIFY):**
- **Reverb** — TIME = decay/size; MODIFY = tap smear (CW = wash, CCW = distinct multi-tap clusters).
- **Delay** — TIME = delay time (pitch-artifact-free, safe to sweep live); MODIFY = feedback
  (CCW one repeat → fully CW piles up forever like a looper). *Manual time-stretch:* sweep TIME
  with MIX + MODIFY up.
- **Slip** — continuous auto-sampler; TIME = sample size (low = pitch-shifter, high = trailing
  harmonized phrases); MODIFY = playback speed/direction in **semitone** steps (CCW of noon =
  real-time reverse).
- **Freeze:** hold the **LEFT** footswitch → current wet sound repeats infinitely; move knobs
  while frozen. *(video-manual-pt1, doug-hanson)*

**Micro-Looper (LENGTH / MODIFY; always listening, length set by CLOCK, LED blinks per cycle):**
- **Tape** — LENGTH = playback slice; MODIFY = speed/direction **quantized to octaves
  (half / normal / 2× / 4×)**. *Gritty loop:* slow CLOCK + fast playback.
- **Stretch** — chops the loop into slices; LENGTH = slice size (high = clear, low = grainy);
  MODIFY = direction + stretch, and **at noon FREEZES a single grain** (LENGTH sizes it),
  reverse CCW of noon. *(video-manual-pt1)*
- **Env** — repeats the current slice whenever input audio is detected; LENGTH = slice size,
  MODIFY = detector sensitivity. *(video-manual-pt1)*

### Micro-loop gesture workflow ("fishing for music")
The looper records *while bypassed*, so you capture whatever played a moment ago — with any
Wet/upstream effect baked in. Tap to grab; **hold the RIGHT footswitch to overdub** (latching
if the LATCH dip is on). The channels are aware of each other — process micro-loops through the
Wet Channel, or record the Wet Channel into the looper. *(video-manual-pt1, video-manual-pt2)*

### Dip switches & the hidden menu
- **Dips:** MISO (mono→stereo), SPREAD (per-mode stereo image), DRY KILL, TRAILS, LATCH,
  **NO DUB**, **SMOOTH CLOCK** (de-steps the CLOCK sweep), **CLASSIC** (restores V1 lo-fi flaws). *(video-manual-pt2)*
- **Hidden menu — hold BOTH footswitches (LEDs green), then move a control:** Wet MODIFY = wet
  **hi-cut (TONE)**; Wet TIME = **stereo width** (w/ SPREAD); Wet MODE toggle = **channel sync**;
  MIX = **ramp LFO waveform**; **LEVEL BALANCE = the CLOCK knob** (noon = even); ROUTING =
  **SPREAD SOLO**; looper LENGTH CCW = loops **fade while overdubbing**; looper MODIFY CW =
  blend clean micro-loop into the 100%-wet path; looper MODE toggle = half loop length. **Reset:**
  flip the PRESET toggle L-and-back 3× → press both footswitches. **True bypass:** tap both
  footswitches 3× (LEDs blink red). *(video-manual-pt2, hidden-options-dip-walkthrough)*

---

## 2. Signature recipes & settings

**Presets are minimal & there's no official cookbook:** **122 MIDI preset slots via Program Change;
slots 1-2 = the two face preset-toggle positions** (recall via MIDI PC — see CB-stack §5); CB
pitched it as an improvisation tool ("tiny knob differences are
crucial"), so the community shares *techniques + approximate positions*, not exact patches.
**Andy Othling authored the factory presets** (the Tim-&-Eric names "Nude Tayne," "Tittleman's
Crest"…) — audio on the CB SoundCloud; copy by ear. *(recipe-sources, artists-and-techniques)*

**Verified copyable recipes:**
- **Pixy Dust** — Wet Reverb, **CLOCK ramped 0→max** = rising sparkle. *(recipe-sources / loopydemos)*
- **Gooey Modulation** — Wet Delay, very short TIME, auto-ramp TIME 0→set via dip.
- **Manual time-stretch** — Wet Delay, MIX + MODIFY up, hand-sweep TIME. *(video-manual-pt1)*
- **Gritty Tape loop** — Micro Tape, slow CLOCK + fast (2×/4×) playback.
- **Frozen grain wall** — Micro Stretch, MODIFY at noon = freeze, LENGTH sizes the grain.
- **Trail Catcher / Freeze pad** — hold LEFT FS to freeze the wet; capture bakes the ambience in.

**Perry Frank's drone mode-pairing cookbook** (the best "which two modes for a drone" map):
**Reverb + Tape** and **Reverb + Stretch** = sustained-wall / endless-decay workhorses;
**Delay + Tape** = rhythmic/pulsing drone; **Reverb + Env** = dynamic/interactive (your attack
carves into the bed). *(perry-frank-ambient-drone)*

---

## 3. Power-user tips, tricks & hidden features

- **NO DUB = pseudo-live effect** (drops looper feedback to 0) — **leave overdub engaged** for it
  to work; the higher the **CLOCK**, the closer it tracks your live playing. *(hidden-options-dip-walkthrough)*
- **Fix channel balance with LEVEL BALANCE (the CLOCK knob in the hidden menu), not MIX** — MIX
  is dry↔wet only; the two channels aren't auto-balanced. *(community-vs-original, hidden-options-dip-walkthrough)*
- **Tame MkII brightness with wet TONE** (hidden: Wet MODIFY) — push it back toward the darker V1
  voicing or to sit the wash under a mix. *(community-guitar-com)*
- **SMOOTH dip** turns the stepped CLOCK into continuous pitch-bends — a strong drone/SFX move. *(hidden-options-dip-walkthrough)*
- **EXP/CV (0–5V) can drive several knobs at once** (Time/Length/Modify/Clock) as Bounce or
  ramp-and-hold — one pedal morphs the whole texture. *(community-guitar-com)*
- **Keep TRAILS on** so toggling the effect mid-performance doesn't kill the wash. *(community-guitar-com)*

---

## 4. Notable users & techniques

- **Andy Othling (Lowercase Noises)** — THE defining, on-aesthetic voice; consults for CB and
  **authored MOOD's factory presets**. Philosophy = this rig's: pedalboard-as-DAW, parallel
  chains, freeze→play-over, capture→stretch into walls ("DAW/plugin moves before it even hits the
  computer"). *(artists-and-techniques)*
- **Mike Stringer (Spiritbox)** — documented MkII user whose texture board runs **MOOD +
  Microcosm + Generation Loss — the same trio as this rig** — proving the stack scales to heavy/
  doom walls. *(artists-and-techniques)*
- **James Blake, Mike Gordon (Phish), Knobs** — documented users, no published settings.
- **Shane Becker** — repo cross-reference (runs vocals/instruments "thru the clean and MOOD");
  no public MOOD settings (thin). *(artists-and-techniques)*
- **The pattern:** nearly every on-aesthetic public demo is **MOOD + Microcosm** (often + OP-1):
  "Microcosm generates, MOOD warps, Blooper commits." *(Common writeup error: Microcosm's Micro/
  Judder/Sustain modes are NOT MOOD's — don't conflate.)* *(artists-and-techniques)*

---

## 5. Rig-specific recipes & CB-stack MIDI

- **Banjo/baritone drone bed:** capture a phrase → **Tape, MODIFY half-speed/octave-down** = instant
  low drone; or **Stretch, MODIFY noon** to freeze a single grain into a sustained wall. *(video-manual-pt1)*
- **Synth/VG-800/OP-1 as looper food:** a bare synth waveform or VG-800 pad is ideal Micro-Looper
  source; set **ROUTING (SPREAD SOLO / hidden)** so the Wet Channel hits only the loop → play dry
  over a drenched bed. *(unperson)*
- **In-time capture, then commit:** use the hidden **channel-sync (LEFT)** so the looper length is
  set to the wet time → capture rhythmic ideas in time with the **Digitakt clock**, then commit the
  loop to the **Blooper** downstream. *(video-manual-pt2)*
- **Stereo intent:** MkII is fully stereo, but the **mono Blooper immediately downstream collapses
  it** — save wide SPREAD/width for later stages (Chroma Console / H90). *(community-pitfalls)*
- **CB-stack MIDI/clock** *(reuse the shared `cb-stack-*` files in the Blooper folder):* MOOD
  **follows MIDI clock via CC51** (0 = ignore), divisions **CC53 (wet) / CC54 (looper)** — **EXCEPT
  in Synth Mode**, and a stray **MIDI Note auto-engages Synth Mode** and silently knocks it out of
  clock (watch this when the Digitakt sequences it). Default channel 2; one-PC whole-stack scene
  recall as per the shared file. *(cb-stack-clock-sync-per-pedal, cb-stack-preset-scene-recall)*

---

## 6. Best learning resources

- **Chase Bliss (official)** — the **two-part video manual** (pt.1 controls/modes, pt.2 dips/hidden
  options) is the authoritative reference; build recipes from it. Plus the Team Demo + Firmware 1.1 clips.
- **Perry Frank** — ambient drone songs organized by explicit Wet+Looper **mode pairings** — the
  best recipe map for this rig's aesthetic.
- **The Unperson (Ali)** — synth/Eurorack-into-MOOD routing + the dry-over-wet-loop trick.
- **Doug Hanson** — concise control intro; quick MkII-vs-V1 + Synth Mode orientation.
- **Knobs** — the launch film (aesthetic reference, not settings).
- **Community:** chasebliss.com/setting-the-mood (official onboarding — "start with all dips off");
  the "Read the Manual" community deep-dive; TGP "MOOD MKII Settings Share" + the FB "Chase Bliss
  Audio Settings" group (both gated to automated fetch — browse manually for owner shares). *(video-manual-pt1/pt2, perry-frank, unperson, doug-hanson, recipe-sources)*

---

## 7. Common pitfalls / gotchas

- **Channels aren't auto-balanced and MIX won't fix it** — use LEVEL BALANCE (hidden). *(community-vs-original)*
- **Delay MODIFY at max self-oscillates** into a wall — back off ~1:00 for controlled piling. *(community-pitfalls)*
- **Capturing through the wet effect bakes the ambience into the loop permanently** ("Trail Catcher" — intentional, plan the moment). *(community-pitfalls)*
- **SPREAD widens *existing* stereo; it does NOT create it** — that's MISO. *(community-pitfalls)*
- **The looper does NOT run in true-bypass** — don't pick true-bypass if you rely on always-listening capture. *(community-pitfalls)*
- **FADE and NO DUB are mutually exclusive.** **DRY KILL** turns MIX into wet-only (MIX down = silence). *(community-pitfalls)*
- **MIDI clock is ignored in Synth Mode**, and a stray MIDI Note auto-engages Synth Mode. *(cb-stack-clock-sync-per-pedal)*
- **~270 mA, 9V center-negative** — needs a beefy isolated supply slot. *(community-pitfalls)*
- **Stock 1.0 Stretch differs from MkI** — flash firmware 1.1 + use Classic Mode to get the old character. *(firmware-1-1-stretch-restore)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `chasebliss-mood-mkii-video-manual-pt1.md` — official control/mode walkthrough (Wet + Micro-Looper, MIX/CLOCK)
- `chasebliss-mood-mkii-video-manual-pt2.md` — official dip-switch + hidden-options walkthrough
- `youtube-mood-mkii-hidden-options-dip-walkthrough.md` — community by-ear demo of every dip/hidden option
- `youtube-mood-firmware-1-1-stretch-restore.md` — official firmware 1.1 (MkI Stretch in Classic Mode)
- `perry-frank-ambient-drone-howto.md` — six drone songs mapped to exact Wet+Looper mode pairings
- `unperson-mood-mkii-reverb-delay-looper.md` — synth/Rings/OP-1-into-MOOD routing + dry-over-wet-loop
- `doug-hanson-mood-mkii-demo.md` — concise control intro + MkII-vs-V1 + Synth Mode
- `knobs-mood-mkii-launch-film.md` — the launch film (aesthetic reference, notes-only)
- `cb-mood-mkii-team-demo.md` — official multi-instrument tone montage (notes-only)

**Links** (`research/links/`)
- `mood-mkii-recipe-sources-and-shared-settings.md` — where recipes live + verified copyable settings + recipe-building cheat-sheet
- `mood-mkii-artists-and-techniques.md` — Othling (presets + philosophy), Stringer/Spiritbox trio, Blake, Gordon, the MOOD+Microcosm pattern
- `chasebliss-setting-the-mood-tips-page.md` — official onboarding ("all dips off")
- `community-mood-mkii-vs-original-clock-noise-levels.md` — MkII-vs-V1 differences, clock-noise history, level-balance gotcha
- `community-mood-mkii-guitar-com-hands-on-tips.md` — looper/granular/clock behaviors + EXP/CV multi-knob detail
- `community-mood-mkii-pitfalls-and-gotchas.md` — consolidated gotcha list (verified vs community-flagged)
- *(MIDI/clock: reuse `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`)*

## Sources

Video (YouTube): CB official manual `O87_xgGxJgI`, `9UzYim0o_Wo` · CB firmware 1.1 `PZPuwN85TOI`
· CB team demo `PjsrTkm-srE` · community dip walkthrough `7BHsCIvyzLk` · Perry Frank `Cqp5Hod3E0M`
· The Unperson `RQcTZRnyauo` · Doug Hanson `II2m-ua_ZcA` · Knobs `9EThN8EGmtU`.
Official: chasebliss.com/setting-the-mood · firmware.chasebliss.com · SoundCloud (Othling presets).
Community: loopydemos.com · guitar.com review · sinesquares.net · TGP / ModWiggler / FB group
(fetch-blocked, via cross-reference). Artists: Equipboard · Tasselmyer Substack · Premier Guitar.
CB-stack MIDI: `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`.
