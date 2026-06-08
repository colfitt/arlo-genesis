# Chase Bliss Generation Loss MkII — Usage Guide

The Generation Loss MkII is the rig's **tape-ruin core** — the VHS/cassette degradation engine
that *is* the "recorded-wrong" aesthetic. It sits on the End board feeding the Big Time delay,
and it's the pedal that turns a clean banjo/baritone into worn tape. The two rules that matter
most: **a little goes a long way** (the home base is Wow ~10:00, Flutter just-below-audible, a
touch of Saturate — cranking everything = mush), and because it has **no MIDI clock**, your
modulation engine is the onboard **Bounce/ramp** (saved into a preset), not the sequencer.
Artists use it the same way you should: a **degraded-texture layer engaged for moments**,
paired with granular (Microcosm) and another color box (MOOD/Chroma) — not always-on.

> Coverage note: there's **no community "recipe-share" culture** (it's demo-video-driven), so the
> concrete settings below come from the manual's starting points, CB's technique tips, and the
> deep kevwyxin "Read the Manual" videos. **MIDI = PC/CC only, NO clock; 2 onboard presets** (see
> the reusable `cb-stack` files). *(genloss-mkii-recipes-where-they-live)*

---

## 1. Essential workflows

### Knob baselines & the subtle↔destroyed axis
- **Volume** noon = unity, full CW = 2× boost. **Saturate** = warm tape *drive* (also boosts
  level). **Model** fully CCW = OFF/clean. **Failure** fully CCW = off; CW adds snags → drops →
  crinkles/pops. *(kevwyxin-pt1, chasebliss-video-manual)*
- **Subtle warmth ("secret ingredient"):** Saturate alone = tape overdrive; **a hair of Flutter
  under a clean tone = vintage-not-broken.** **Total destruction:** crank Failure + Models 1–3
  (VHS). *(kevwyxin, official-walkthrough)*
- **The Model knob is the main tone-shaper** — not set-and-forget; hunt per source. Differences
  are **subtle by ear** and read mostly as **EQ band-limiting + stereo spread**, clearest on
  transients with Wow/Flutter/Failure low. *(martinyammoller, community-tips)*

### Failure surgery & the hidden noise controls
- **DROP BYP** removes volume cut-outs · **SNAG BYP** removes pitch-warps (keep only crinkles/
  pops) · **HUM BYP** removes mechanical noise — mix to taste. *(kevwyxin-pt2)*
- **Hidden Hiss = the Flutter knob in the hidden menu** — dial it down; this is the real fix for
  the "hiss is aggressive" complaint. **Hidden Mechanical Noise = the Saturate knob** (noon = 0,
  CW = hum/buzz, CCW = VCR noise) — a second noise voice. *(kevwyxin-pt2)*
- **DRY TYPE dip:** **Small** = the community default for melodic material (tape dominant but
  keeps body/intelligibility); **Unity** = more dramatic tape-chorus; **None** = full wet. *(community-tips, kevwyxin-pt2)*

### FREEZE, Classic mode & stereo
- **FREEZE** (MkII, CLASSIC mode): Aux toggle → **FAIL** + engage **CLASSIC + DROP BYP + SNAG
  BYP** → left footswitch infinitely holds the last sound. **MkII uniquely lets you play your WET
  signal OVER the frozen note** (the original couldn't) — drone-and-solo. *(kevwyxin-pt2, genloss-aux-freeze)*
- **Classic-mode filter box:** Saturate (GEN) full CW, Failure (HP) full CCW, Model (LP) full CW
  = filters wide open → a usable HP/LP band-pass over anything. *(kevwyxin-pt1)*
- **Stereo:** TRS auto-detects; **MISO** = mono→stereo; **SPREAD** is failure-driven (scatters
  drops/snags L↔R — use headphones); in Classic, SPREAD instead = smooth Wow-linked panning.
  **Auto-panner trick:** SNAG BYP + SPREAD + MISO, knobs down → clean signal skitters L↔R. *(chasebliss-video-manual, community-tips)*

### Ramping = the modulation engine (no MIDI clock)
**Bounce** dip = continuous LFO; pick targets with the top-row dips; **SWEEP B/T** sets the
travel endpoints; the **Volume knob becomes ramp SPEED** while ramping (hold left footswitch to
still set actual volume). **Ramp Wow+Flutter+Model together** and **save the whole ramp/dip setup
to a preset** so a song scene recalls the *moving* patch. *(nickrees, kevwyxin-pt2)*

---

## 2. Signature recipes & settings

The 12 Models (1–3 CPR-3300 VHS · 4–5 Portamax cassette · 7–9 Dictatron/toy band-limited).
**Copyable starting patches** (clock-face; manual + CB tips): *(genloss-mkii-recipes-where-they-live)*
- **Subtle warmth / tape age:** Wow 10:00 · Flutter just-below-audible · Saturate 9:00 · Failure
  8:00 · **Model 4** · Dry **Small**.
- **Dying cassette / seasick:** Wow 1–2:00 · Flutter 12:00 · Saturate 11:00 · Failure 9:00 ·
  **Model 5 (half-speed)** · Dry **None**.
- **Worn VHS / dropout chaos:** Wow 11:00 · Flutter 1:00 · Saturate 1:00 · Failure 2–3:00 ·
  **Model 1–3** · SPREAD on · Dry **None** · Aux = **STOP**.
- **"AM radio" / filtered lo-fi:** Wow 9:00 · Flutter 8:00 · Saturate 10:00 · Failure low ·
  **Model 7–9** · Dry **Small** (no named "AM radio" preset — it's built from the band-limiting models).
- **Official dip recipes:** Freeze (above); **tape chorus** = Dry **Unity** + Wow up; **clean
  auto-panner** = SNAG BYP + SPREAD + MISO, knobs down; **"tape hopper"** = Bounce **Model** + RANDOM dip. *(genloss-mkii-recipes-where-they-live)*

---

## 3. Power-user tips, tricks & hidden features

- **Aux footswitch is latching (tap) AND momentary (hold)** — onset speed set in the hidden menu
  (Wow knob); the MIDI/aux jack also takes any normally-open external momentary (no MIDI needed). *(genloss-aux-freeze)*
- **Gen Loss → reverb → EQ** chain — EQ *after* cleans the muddy lows while keeping the reverbed
  high harmonics (relevant: the H90 is downstream). *(community-tips)*
- **A bonus LFO/wobble for already-wonky digital sources** — de-perfects VG-800 modeled patches /
  synths. *(community-tips)*
- **Self-modulation needs no external gear** — Bounce Model + RANDOM = "tape hopper"; Bounce
  Failure = evolving malfunction; both saveable to a preset. *(nickrees, kevwyxin-pt2)*

---

## 4. Notable users & techniques

- **Mike Stringer (Spiritbox)** — the marquee user; **Gen Loss + MOOD + Microcosm** on the "textures
  & ambience top row." On **"Crystal Roses"** it's "really over-the-top… crazy ambience" over a drum
  solo — **used sparingly but heavily when on.** No published settings. *(spiritbox-mike-stringer-rig-rundown)*
- **St. Vincent (Annie Clark)** — Gen Loss MkII in the studio on *All Born Screaming* (2024),
  named alongside **Chroma Console + Microcosm** — the exact lo-fi/granular cluster this rig pairs. *(genloss-mkii-artists)*
- **Andy Othling (Lowercase Noises)** — Gen Loss + MOOD + Blooper; treats the board "like a DAW"
  with texture sends; Gen Loss = **texture generator, not tone-shaper.** *(genloss-mkii-artists)*
- **Convergent signal:** two independent on-aesthetic deployments use it identically — a
  **degraded-texture layer paired with granular delay, engaged for moments, not always-on.** Numeric
  settings essentially don't exist for any artist — the role + pairing is the takeaway. *(genloss-mkii-artists)*

---

## 5. Rig-specific recipes & MIDI

- **Banjo/baritone tape-ruin:** the band-limiting models (4–8) + filter rolloff bite hardest on the
  banjo's percussive attack — blur staccato into sustain. Keep Wow/Flutter low to hear the model EQ,
  then push for the smear. *(martinyammoller, dossier §6)*
- **Degrade-then-delay:** the **Aux = STOP** tape-halt and momentary **FAIL** punch-ins are
  performance moves the downstream **Big Time** delay will catch and repeat. *(kevwyxin-pt2)*
- **Seed the texture trio:** **Freeze** (Classic-mode) holds a Gen Loss drone you can feed into the
  **MOOD** micro-loop / **Microcosm** granular — broken source without playing (the Stringer trio). *(genloss-aux-freeze, spiritbox-mike-stringer-rig-rundown)*
- **Hiss before the cassette print:** set **hidden Hiss (Flutter knob) low** + **HUM BYP** so you
  don't stack two noise floors into the PORTA424 tape stage. *(kevwyxin-pt2, community-tips)*
- **MODS — keep yours STOCK for this rig:** the **bass hardware mod** removes the gentle analog HPF,
  but that HPF is what **tames Saturate's flub on the baritone drone** — skip it. The **low-latency
  firmware (1.1.0)** halves latency/kills drum-doubling but trades the stereo from chorus-y →
  flange-y; only flash it if transient timing matters more than the wide chorus. *(cb-mods-page, community-tips)*
- **Latency (measured):** ≈**25 ms wet / 9 ms dry** (~16 ms skew) — the internal Dry blend is **not
  phase-coherent on percussive/transient material**; fine for synths/ambient/sustained guitar, but for
  tight parallel work use a DAW insert + latency comp (or flash 1.1.0). *(yt-genloss-latency-measured)*
- **MIDI:** **PC/CC only — NO clock** (Wow/Flutter free-run); **2 onboard presets**; default ch.2;
  recall via PC in the one-PC whole-stack scene. *(cb-stack-clock-sync-per-pedal, cb-stack-preset-scene-recall)*

---

## 6. Best learning resources

- **kevwyxin "Read the Manual" Pt 1 + Pt 2** — the deepest free resource; **Pt 2 is the goldmine**
  (every hidden option, all dips, the Freeze recipe, ramping, the 3 bypass modes).
- **Chase Bliss (official) Video Manual** — authoritative control/dip/hidden behavior + MkII-vs-Classic.
- **Nick Rees** — the clearest Bounce/Sweep ramping explanation.
- **Martin Yam Møller** — the only clean A/B of all 12 models on familiar sources (ear-training the Model knob).
- **CB Mods page + Modification Guide PDF** — authoritative on the latency-firmware + bass-hardware mods.
- **Communities:** the **Elektronauts Gen Loss MkII megathread** (t/174731, 40+ pp — synth/Elektron-
  leaning, best for mod/firmware chatter) and the CB Discord (gated to fetch — skim manually for recipes). *(kevwyxin, chasebliss-video-manual, nickrees, martinyammoller, cb-mods-page, community-tips)*

---

## 7. Common pitfalls / gotchas

- **Hiss is louder than expected** — leave Noise OFF by default (or hidden Hiss low). *(community-tips)*
- **Dry-blend latency isn't phase-coherent on transients** (kick flaming) — see §5. *(yt-genloss-latency-measured)*
- **Failure is random/non-repeatable** — tame with DROP BYP / SNAG BYP. *(community-tips)*
- **Saturate flubs on bass-heavy sources** — the stock HPF tames it → for the baritone-drone rig,
  KEEP stock, skip the bass mod. *(community-tips)*
- **Pitch-warp fatigue** ("can get nauseating"); **250 mA** draw needs a dedicated isolated slot. *(community-tips)*
- **MkII Classic mode ≠ bit-perfect MkI** (Wow/Flutter/Gen/Noise differ; layers extra noise); no MkII
  gives V1's separate wow speed+depth — a genuine loss vs the original. *(yt-genloss-4version, community-tips)*
- **A little goes a long way** — cranking every knob = undifferentiated mush. *(community-tips)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `kevwyxin-read-the-manual-part1-basics.md` — full knob/toggle/model walkthrough + Classic "no sound" fix + filter-box
- `kevwyxin-read-the-manual-part2-advanced-dips-hidden.md` — every hidden option, all dips, Freeze recipe, ramping, 3 bypass modes (deepest)
- `chasebliss-official-video-manual.md` — authoritative control/dip/hidden reference + MkII-vs-Classic
- `chasebliss-official-walkthrough.md` — launch demo (audio reference)
- `nickrees-chasebliss-ramping-genloss-mood-reverse.md` — Bounce/Sweep ramping mechanics + save-to-preset
- `martinyammoller-12-tape-models-familiar-sounds.md` — A/B of all 12 models; model-character notes
- `genloss-latency-prose.md` — measured-latency video, cleaned
- `genloss-4version-comparison-prose.md` — V1/V2/MkI/MkII per-control A/B, cleaned

**Links** (`research/links/`)
- `genloss-mkii-recipes-where-they-live.md` — where recipes exist + 5 copyable starting patches + official dip recipes + model picks
- `genloss-aux-freeze-classic-trick.md` — hidden Freeze access + all 4 aux behaviors + momentary
- `genloss-community-tips-pitfalls.md` — distilled forum/review tips, pitfalls, MkII-vs-original sentiment
- `cb-mods-page-genloss-latency-bass.md` — official latency-firmware + bass-hardware mods, procedures, rig guidance
- `yt-genloss-latency-measured.md` — measured latency (~25/9/16 ms) + the DAW fix
- `yt-genloss-4version-comparison-tripedal.md` — V1/V2/MkI/MkII per-control A/B by an owner of all four
- `spiritbox-mike-stringer-rig-rundown.md` — Stringer's Gen Loss + MOOD + Microcosm usage ("Crystal Roses")
- `genloss-mkii-artists-othling-stvincent.md` — St. Vincent, Othling, Carter, Bro, model collaborators
- *(MIDI/clock: reuse `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`)*

## Sources

Video (YouTube): kevwyxin `EqRI_oJmkCA`, `SiEP0SHxZM4` · CB official `Rv7O005y43M`, `HzXb6WIMvwU` ·
Nick Rees `dwyFzow481A` · Martin Yam Møller `zhXPpBJ8Qoc` · latency `7HuHyHSX8d8` · Tri Pedal
4-version `2i2Hjwk1qls` · Spiritbox rig rundown `067jy4EhQeE`.
Official: chasebliss.com/generation-loss-mkii + /gen-loss-mkii-mods + Modification Guide PDF.
Community: elektronauts.com (Gen Loss MkII megathread t/174731) · guitar.com · TGP · reddit (snippet-level).
Artists: premierguitar.com (Spiritbox) · equipboard.com (St. Vincent) · strymon.net (Othling).
CB-stack MIDI: `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`.
