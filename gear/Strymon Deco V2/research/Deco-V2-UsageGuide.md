# Strymon Deco V2 — Usage Guide

The Deco V2 is two tape-deck engines in one box — a **Tape Saturation** stage and a
**Doubletracker** (flange→chorus→slapback→delay) — and in this rig it's the **front-of-chain
warmer**: the dossier's split is "**Deco warms the clean source up front; Generation Loss
breaks it at the End — run both.**" The maker's own headline move is to run the Saturation
**always-on and ride your guitar volume** so it fattens everything without being heard, then
use the Doubletracker for width into the stereo stages. **Hammock** (who run a Deco) are the
on-aesthetic model: place it early, after the dirt, before time/reverb, and *perform* its knobs.

> V2 vs original: the engines are unchanged; **V2 added the front-panel TONE knob, the CASSETTE
> voice, true stereo I/O, and MIDI + 300 presets**. It's a **gain device** (expect a volume jump
> on engage). Keep firmware current (**v1.33**) — earlier revs had a MIDI-PC lockup (fixed v1.20)
> and a saturation-sweep volume burst (fixed v1.22). *(deco-v2-firmware-release-notes, pete-celi-in-depth)*

---

## 1. Essential workflows

### Tape Saturation (the always-on warmer)
- **Maker's technique (Pete Celi):** set Saturation fairly high, then **let guitar volume set the
  drive** — rolled back = clean/transparent, dug in = harmonics + compression + dynamic band-
  limiting (tames sharp transients). As glue, keep it low enough you "don't really hear it." Single
  coils warm audibly ~**10:00**. *(pete-celi-in-depth)*
- **Voice (V2): Cassette = fatter, more compressed, more low end, more grit; Classic = cleaner**
  (more like a normal OD). Lean Cassette to fatten low-output sources, Classic if it over-compresses
  against the dirt stack. *(guitar-center-rob-gueringer, kaleidoscope)*
- **TONE knob (V2 front panel):** absorbs the old high-trim duty — roll it dark to avoid re-
  brightening the banjo. *(strymon-deco-v2-manual-revd)*

### Doubletracker (the Lag-Time arc)
**Lag Time** sweeps a continuous arc: **flange (−.3–3 ms) → chorus (past noon) → slapback →
full ~500 ms delay**. **Blend 50/50 = strongest flange**; favor the reference deck to mellow;
Blend full CW = hear the wet deck alone. **Wobble** = random tape-speed detune (subtle movement →
vibrato — keep low for doubling, push for warped tape). **Type:** **Bounce** = brightest/most
wobble (ping-pong feel), **Sum** = cleanest, **Invert** = middle. *(superdanger, pete-celi-in-depth)*

### Wide Stereo & the hidden layer (V2, Rev D manual)
- **Wide Stereo mode** (held on WOBBLE, saved per preset): splits **reference → L, lag → R** for a
  wide doubled image; auto-disables if only OUT L is connected (then Blend becomes a pan). *(pete-celi-wide-stereo, strymon-deco-v2-manual-revd)*
- **Live-Edit secondaries — hold TAPE SATURATION ON** (V2 has **4 params + 2 MIDI toggles**: Low
  Trim, Auto-Flange Time, Wide Stereo, Doubletracker Boost/Cut). *(Note: this differs from V1, which
  used both footswitches and a separate High/Low-Trim set — don't follow V1 secondary guides.)* *(strymon-deco-v2-manual-revd, daftparagon-deco-v1-secondary-functions)*
- **Auto-Flange:** press-and-hold **DOUBLETRACKER ON** for a momentary through-zero flange; on
  **firmware v1.20+ it works even with the doubletracker bypassed** (grab the flange only for
  transitions) — also MIDI **CC#97**. *(strymon-deco-v2-manual-revd, thegearpage)*

### MIDI / presets
**300 presets / 3 banks**, recalled via **MIDI PC** (TRS EXP/MIDI or USB-C) or the **Favorite**
footswitch; PC0=Favorite, PC1–3=MultiSwitch A/B/C, **PC127=Manual (live knobs)**. **MIDI clock
syncs the lag/echo** (Lag Time becomes a tempo mult/div, the DT LED turns **pink**) — **but the
Wobble is free-running and NOT clockable.** Manage/back-up/share in **Nixie 2** (Deco V2 supported,
USB-C; presets are `.syx`). Channel + MIDI-OUT mode are **power-up settings, not per-preset** (set
MIDI OUT = Off when using a Strymon MIDI EXP cable). *(strymon-deco-v2-manual-revd, strymon-deco-presets-nixie2-loading)*

---

## 2. Signature settings

- **Always-on glue (maker):** Saturation fairly high, Volume to unity, ride guitar volume; TONE/Low
  Trim to taste. *(pete-celi-in-depth)*
- **Max flange:** Blend 50/50, short Lag Time, a little Saturation so the comb reads on a dirty
  source. **Through-zero without dropout:** Invert + Blend 50/50 + Lag *just past* zero. *(pete-celi-in-depth)*
- **Static parkable comb (the "notch on a fuzz wall"):** Strymon's "Flange Filtered" — distorted
  input, **Wobble = 0**, sweep Lag Time by hand (or expression). *(strymon-tape-flanging-chorus-examples)*
- **Slapback level trick:** **Volume low + Saturation up slightly** so the slap doesn't sound weak. *(thegearpage)*
- **Wide mono→stereo:** **Bounce** type (the widener) or Wide Stereo mode. *(pete-celi-wide-stereo)*
- **Rob Gueringer 50s/60s OD+slap:** Saturation MAX, Cassette, Vol just under noon, Tone just above
  noon; Doubletracker Blend noon, Wobble near off, Bounce. *(guitar-center-rob-gueringer)*
- **Factory Quick Start patches:** Wide Wobbles · Wet Slapback Cassette · On The Edge · Worn Out
  Deck · Pretty Tape Flange. **Strymon named recipes:** Thick Shake, Flange Filtered, Off-Center,
  Vintage Doubles, Rocking Chair, Lagging in Stereo, etc. *(strymon-tape-flanging-chorus-examples)*
- *(GuitarChalk numeric 0–10 recipes exist — e.g. "Crushed lo-fi" 9/Vol4/Tone2-dark/Lag3/Blend4/
  Wobble9 — but read SEO/AI-generated; use as ballpark only.)* *(guitarchalk-deco-v2-settings)*

**Presets:** there's **no dedicated Deco "This Week's Preset" library** — roll your own scenes and
back up/share via Nixie 2 `.syx`. *(strymon-deco-presets-nixie2-loading)*

---

## 3. Power-user tips, tricks & hidden features

- **Expression over Lag Time** = walk the whole flange→chorus→slapback→echo arc under one foot
  (the most-recommended live trick). *(thegearpage)*
- **Auto-Flange-while-bypassed** (v1.20+) for transitions without committing the doubletracker. *(strymon-deco-v2-manual-revd)*
- **Bounce for character, Sum for clean glue** (Type-mode rule of thumb). *(guitar-center-rob-gueringer)*
- **MIDI wiring quick-test:** saturation footswitch off → send **CC#10 = 127** → the LED should turn on. *(strymon-deco-v2-manual-revd)*
- **Reverb/Flint INTO the Deco:** tape-saturate a long reverb tail (Superdanger runs a Flint hall →
  Deco, then Wide Stereo) — a concrete ambient recipe. *(superdanger)*

---

## 4. Notable users & techniques

- **Hammock (Marc Byrd / Andrew Thompson)** — the one confirmed on-aesthetic Deco user (Strymon
  pedalboard feature): Deco sits **early, after the dirt, before time/reverb** (tape-on-source), in a
  Big Sky + TimeLine + Deco + Flint rig. Transferable gold: **perform the Deco — ride Lag/Wobble (or
  EXP) during a sustained chord** rather than parking it. *(hammock-deco-ambient-technique)*
- **Myles Kennedy, Ben Howard** — confirmed on board, no published settings, off-aesthetic. **Yvette
  Young** — Equipboard sighting but **NOT on her published 2023 board** (flag); notable overlap is
  she runs the same **EAE Longsword + Caroline Somersault** as this rig's Board 1. *(deco-artists-roundup)*
- **Honest:** no artist claims the Deco as a signature voice — model Hammock's *method*, not settings. *(deco-artists-roundup)*

---

## 5. Rig-specific recipes

- **Warm the banjo/baritone at the front:** modest Saturation, ride the VG-800/guitar level; **TONE
  dark + Low Trim up** so it doesn't re-brighten the banjo or flab the baritone; **Cassette** voice
  to fatten the low-output GK-5 sources, Classic if it over-compresses into the dirt. *(pete-celi-in-depth, dossier §6)*
- **Fat doubled stereo into Board 2:** **Wide Stereo mode** (or Bounce) splits the decks L/R → hand
  the Microcosm / Dark Star / CE-2W a wide pair instead of a mono source. *(pete-celi-wide-stereo, superdanger)*
- **Pair with Gen Loss at the End (no overlap):** the Deco is well-behaved and builds **glue + width
  on the source**; the Gen Loss **ruins the finished bus**. *(dossier §; pete-celi-in-depth)*
- **Tape-saturated reverb tail:** run the **Flint/Big Sky → Deco** (Superdanger) for a saturated,
  widened wash. *(superdanger)*
- **MIDI recall** the 300 presets per song-section from the Digitakt/controller; lag/echo can clock-
  sync, Wobble can't. *(strymon-deco-v2-manual-revd)*

---

## 6. Best learning resources

- **Strymon (official) — Pete Celi "In-Depth Demo"** — the engine bible (saturation-by-volume,
  Sum/Invert/Bounce, the Lag arc); plus the **Wide Stereo Mode** demo and the **Tape Flanging/Chorus
  named-recipe** video. (Original-Deco era but applies to V2.)
- **Superdanger Studios** — the best V2 "how I use it": always-on/end-of-chain, reverb-into-Deco,
  Wide Stereo, MIDI/plugin-controller.
- **Guitar Center / Rob Gueringer** — V2 pro walkthrough with explicit knob positions + Type ranking.
- **Authoritative docs:** the **Deco V2 Rev D manual** (Live-Edit procedure, full MIDI CC table,
  presets) and **firmware release notes** outrank any forum post. **TheGearPage** "indispensable
  settings" thread for community tricks (paywalled; snippets only). *(pete-celi-*, superdanger, guitar-center-rob-gueringer, strymon-deco-v2-manual-revd, thegearpage)*

---

## 7. Common pitfalls / gotchas

- **It's a gain device — volume jumps on engage**; level-match with per-side Boost/Cut + Volume
  (Strymon even firmware-patched a saturation-sweep volume burst in v1.22). *(deco-v2-firmware-release-notes, thegearpage)*
- **MIDI PC lockup on pre-v1.20 firmware** — update to v1.33 for the MIDI-recallable rig. *(deco-v2-firmware-release-notes)*
- **Stereo needs a TRS adapter on the INPUT** (a mono cable = mono in); **Wide Stereo auto-disables
  with mono out** (Blend becomes a pan). *(strymon-deco-v2-manual-revd)*
- **MIDI Channel + MIDI-OUT mode are power-up settings, not per-preset**; set MIDI OUT = Off with a
  Strymon MIDI EXP cable. *(strymon-deco-v2-manual-revd)*
- **Wobble gets seasick past mid** on sustained notes — keep it low for "doubling." *(superdanger)*
- **Don't follow V1 secondary-function guides** — V2's hidden layer differs (4 params via TAPE
  SATURATION-hold; TONE is now a front-panel knob). *(strymon-deco-v2-manual-revd, daftparagon-deco-v1-secondary-functions)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `strymon-pete-celi-in-depth-demo.md` — official engine bible: saturation-by-volume, Sum/Invert/Bounce, full Lag/Blend/Wobble
- `strymon-pete-celi-wide-stereo-mode.md` — official Wide Stereo / split-mode demo
- `strymon-tape-flanging-chorus-examples.md` — official named patch recipes (Thick Shake, Flange Filtered, etc.)
- `superdanger-one-pedal-endless-tone-deco-v2.md` — V2 deep "how I use it" (always-on, reverb-into-Deco, Wide Stereo, MIDI)
- `guitar-center-rob-gueringer-deco-v2.md` — V2 pro walkthrough w/ explicit knob positions + Type ranking
- `kaleidoscope-deco-v2-unboxing-quickstart-patches.md` — V2 factory Quick Start patch names + cassette note (notes-only)

**Links** (`research/links/`)
- `strymon-deco-v2-manual-revd-secondary-midi.md` — authoritative V2 Live-Edit + full MIDI CC table + presets
- `strymon-deco-v2-firmware-release-notes.md` — V2 firmware changelog (v1.20/1.22/1.33) + the gotcha fixes
- `strymon-deco-presets-nixie2-loading.md` — 300 presets + Favorite + Nixie 2 `.syx`; no-dedicated-TWP flag
- `strymon-secondary-functions-deco.md` — Strymon secondary-functions page *(note: V1-leaning; see Rev D manual for V2)*
- `daftparagon-deco-v1-secondary-functions-mnemonic.md` — V1 secondaries + explicit V1→V2 reconciliation
- `thegearpage-deco-indispensable-settings.md` — community tips (slapback-level trick, expression-over-Lag)
- `hammock-deco-ambient-technique.md` — Hammock confirmed Deco user + knob-riding technique
- `deco-artists-roundup-equipboard-rigrundowns.md` — documented users w/ source-strength flags
- `guitarchalk-deco-v2-settings-recipes.md` — five numeric recipes (QC-flagged SEO/AI-generated)

## Sources

Video (YouTube): Pete Celi/Strymon `ST8pp4HN554`, `QHLA5JByIYc`, `PUNklBG8gAc` · Superdanger
`gxS7ueTq6_I` · Guitar Center/Gueringer `1KNWCXIqscY` · Kaleidoscope `lwGE721e0tI`.
Official: strymon.net (Deco V2 Rev D manual, firmware release notes, secondary functions, Nixie 2) ·
strymon.net pedalboard feature (Hammock). Community: thegearpage.net (paywalled) · daftparagon.com ·
guitarchalk.com (SEO-flagged) · equipboard / Premier Guitar rig rundowns. Presets: `.syx` via Nixie 2.
