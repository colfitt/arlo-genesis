# Decapitator — Usage Guide

Decapitator is the **in-the-box analog saturation / harmonic-color** box — 5
hardware-modeled styles whose real value, by near-unanimous community verdict, is
**warmth and tone-shaping, not full distortion** ("it shines when you DON'T use it
for distortion"). The headline feature is the **Mix knob** (parallel saturation,
no aux routing). For this rig it's the *intentional analog-harmonic* stage — it
overlaps very little with the degradation tools (RC-20 / SketchCassette = wobble/
noise/dropout *motion*) and complements the hardware (Colour Box V2 / Generation
Loss = committed front-end character you print). `research/links/decapitator-tapeop-review.md`, `research/links/decapitator-vs-other-saturators.md`

## 1. Essential workflows

- **Pick the style first, then dial Drive** — even at zero Drive each style already
  reshapes the spectrum/harmonics; you're choosing a *behavior*. `research/transcripts/decapitator-xnb-deep-dive.md`
- **Subtle warmth/glue** — A style, low Drive, low Mix; the everyday console-color
  use (the "shines when not distorting" consensus).
- **Parallel saturation via Mix** — drive hard, pull Mix toward dry to keep
  transients/clarity with texture underneath (like parallel compression, in-box). `research/links/decapitator-tapeop-review.md`
- **Saturate-then-wash** — Decapitator *early* → modulation → reverb (Valhalla):
  generate harmonics upstream and let the reverb smear them, rather than dirtying a
  clean tail. `research/links/decapitator-chaining-reverb-shoegaze.md`

## 2. Signature settings & presets (copyable)

**The 5 styles** (manual mapping — note: a popular tutorial mislabels E as
"triode"; the manual is authoritative): `research/links/decapitator-manual-v5-controls-and-styles.md`, `research/links/decapitator-musicguymixing-style-button.md`
- **A — Ampex 350** tube tape-drive preamp → "**ultra-ultra-smooth**," flattest,
  tape-flavored. The **always-on tape-color** opener.
- **E — Chandler/EMI TG** console → **beefy lows + airy top**. The **drum-bus** pick
  (adds low end — on already-bassy sources prefer A).
- **N — Neve 1057** (germanium) → weighty-but-solid lows, focused mids; manual flags
  "**especially on guitars**." Trick: drive till it just crackles, then **Steep +
  High Cut** to kill the fizz.
- **T — Culture Vulture, triode → EVEN harmonics.** Warm, punchy; drums/percussion,
  snare-fatten, vocal grit.
- **P — Culture Vulture, pentode → ODD harmonics.** Rawer; bass/808 (sub reads on
  small speakers), crunchy drums. **Careful on tonal pads** — odd harmonics clash.

**Controls & signal order:** Low Cut + **Thump** (LF boost *at* the low-cut freq =
tape head-bump) + **Tone** (tilt, pre-sat) → **Style + Drive + Punish** → **High
Cut + Steep** (post-sat) → Output/**Auto** → **Mix**. Drive also *shifts the EQ
curve* (low = flatter, high = textured), so it's a tone control too. **Punish** =
+20 dB instant gain. **Auto** (default on) drops output as Drive rises for honest
color-vs-loudness A/B — turn off for deliberate level. **Steep + High Cut 4–5 kHz =
guitar-cab/DI emulation.** `research/links/decapitator-audiopluginnews-tips.md`, `research/transcripts/decapitator-soundtoys-quickstart.md`

**Copyable recipes:** `research/links/decapitator-gearspace-styles-and-tips.md`, `research/links/decapitator-808-bass-settings-wethesound.md`, `research/links/decapitator-splice-creative-distortion.md`
- *Subtle glue:* A, **Drive ≤2, Mix 10–20%**. · *Subtle texture:* Drive 4 / Mix 10%.
  · *Obvious color:* Drive 6 / Mix 90%.
- *Parallel drum smash:* full Drive, set **Low Cut** so it doesn't touch the lows,
  blend **Mix** back (E on the bus); *crunchy drums:* **P, Drive 6+**.
- *Bass/808:* A/N Drive 1–3, Mix 100% (warmth); E for attack; **Punish ON + Low Cut
  ~midway** for tight musical dirt; T/P + Punish for aggressive sub-harmonics.
- *De-fizzed driven guitar:* **N, Drive ~9, Tone bright, + Steep/High Cut**.
- *Vocal grit / saturation-as-EQ:* A or T subtle, Tone critical; the Mix knob
  preserves transients ("sand down the harsh top"). `research/links/decapitator-tapeop-review.md`
- *Lo-fi "recorded-wrong":* extreme **Low Cut + High Cut = telephone / AM-radio**
  bandpass (built into the manual's design). `research/links/decapitator-manual-v5-controls-and-styles.md`
- *Sustained wall/drone:* A/E/N, low Drive, low Mix, placed **early** as harmonic
  texture that blurs note definition → mod → Valhalla. `research/links/decapitator-chaining-reverb-shoegaze.md`

## 3. Power-user tips, tricks & hidden features

- **Mix = in-plugin parallel saturation** — the universally-praised feature; restores
  transients the saturation chops. `research/links/decapitator-tapeop-review.md`
- **Drive changes the EQ, not just the dirt** — low Drive flatter, high Drive a
  unique evolving textured EQ. Treat Drive as tone. `research/links/decapitator-audiopluginnews-tips.md`
- **Auto stops you fooling yourself** (auto-gain for honest A/B); **Punish = +20 dB**
  for quiet sources or instant brutality. `research/links/decapitator-audiopluginnews-tips.md`
- **Thump** = punch/tightness at the low-cut freq before saturation; **Steep** =
  6→30 dB/oct fizz-killer; **Low Cut pre** (stops flabby low-end dirt) / **High Cut
  post** (kills fizz). `research/links/decapitator-splice-creative-distortion.md`
- **Gain-staging matters** — saturators are level-sensitive; aim ~−18 dBFS (0 VU) in;
  a gain trim before/after sits it in the window. `research/links/decapitator-audiopluginnews-tips.md`
- **Aliasing as a feature:** no internal oversampling → it aliases at 44.1/48k. For a
  lo-fi rig that "crusty" aliasing is usable *on purpose*; for clean color run 88.2/
  96k. `research/links/decapitator-aliasing-oversampling.md`

## 4. Notable users & techniques (sourced, flagged)

- **Tchad Blake** (Radiohead, Black Keys, Tom Waits) — "**I like it on everything**"
  (vendor-quoted). The most aesthetically-aligned name (dark/saturated/"recorded-
  wrong"), also an EchoBoy user. `research/links/decapitator-artists-sourced-uses.md`
- **Andrew Scheps** — uses it constantly, "subtle saturation to full-on mangling"
  (paraphrased, high confidence). **Pete Weiss** (Tape Op) — de-harsher on nearly
  every mix via the Mix knob. **Fab Dupont** ("instavibe-in-a-box"), **Ryan Hewitt**
  (vendor quotes). `research/links/decapitator-artists-sourced-uses.md`, `research/links/decapitator-tapeop-review.md`
- **Honest flag:** no named drone/doom/shoegaze artist surfaced — relevance is by
  **technique** (Tchad-Blake degradation, saturation-as-color, parallel grit under a
  wall, distortion→mod→reverb), none invented. `research/links/decapitator-artists-sourced-uses.md`

## 5. Rig-specific recipes (your gear by name)

- **Software vs hardware drive:** Decapitator = recallable, automatable, free to
  instance, *versatile* → the **studio/back-end** color (stems, returns, reamps in
  the box). **Colour Box V2** (transformer/EQ preamp grind) and **Generation Loss**
  (real tape-degradation) = committed signature character you **print on the way
  in**. Pedals = front-end commitment; Decapitator = recallable back-end. `research/links/decapitator-vs-other-saturators.md`
- **Complementary, not competing:** pair Decapitator (harmonic *color*) with **RC-20
  / SketchCassette** (degradation *motion*) — don't stack two hard saturators
  fighting. `research/links/decapitator-vs-other-saturators.md`
- **Saturate then wash into Valhalla:** saturate the *source* feeding a slow-attack
  Supermassive/VintageVerb wall to keep it dense without making the reverb harsh; or
  **grit a reverb return** (low Drive/Mix, A/E/N) — watch aliasing on full-spectrum
  tails (High Cut + Steep). `research/links/decapitator-chaining-reverb-shoegaze.md`
- **After a delay** (incl. EchoBoy): post-delay Decapitator adds overtones and tames
  the "too crisp" digital repeat. `research/links/decapitator-chaining-reverb-shoegaze.md`
- **Shoegaze/drone chain order: distortion FIRST → modulation → time/reverb** — for
  banjo/baritone walls, A/E/N early as the harmonic bed under the time effects. `research/links/decapitator-chaining-reverb-shoegaze.md`

## 6. Best learning resources

1. **XNB "A deep look to the DECAPITATOR" (14 min)** — best signal-flow; spectrum +
   harmonic analyzer proves each style at zero drive.
2. **ARTFX (31 min)** — longest; style-by-style across drums/bass/EP/piano/full-mix
   with settings dialed.
3. **Nathan Nyquist (18 min)** — the drive-then-mix workflow + honest limits (same
   channel as the EchoBoy flagship resource).
4. **Distinct Mastering (12 min)** — clearest parallel-saturation demo.
5. **Groove3 "Effects Explained"** — the "use it as an EQ" idea + Decapitator-on-a-
   delay-return. Reference: the v5 manual + Tape Op review.

## 7. Common pitfalls / gotchas

- **No internal oversampling → aliasing** (audible at 44.1/48k, gone by 96k). Run
  88.2/96k for clean color, or embrace the crust for lo-fi. `research/links/decapitator-aliasing-oversampling.md`
- **Harshness** usually = too much Drive into bright material; saturating to "fix"
  harsh highs can *add* harshness. Stay clean with **low Mix + High Cut/Steep +
  styles A/E/N**. **Stacking many instances compounds aliasing** — freeze in Logic. `research/links/decapitator-aliasing-oversampling.md`
- **Level jumps** if Auto is OFF — engage Auto for honest A/B. `research/links/decapitator-audiopluginnews-tips.md`
- **It's less of a single signature sound** than a SansAmp/the hardware boxes — the
  trade-off for versatility/recall. `research/links/decapitator-honest-review-limits-musco.md`

## 8. Captured sources

**Transcripts (6)** — `research/transcripts/`: decapitator-xnb-deep-dive (spectrum/
signal-flow) · decapitator-artfx-soundtoys5 (31-min style-by-style) · decapitator-
nathan-nyquist (drive-then-mix) · decapitator-distinct-mastering-sources (parallel
saturation) · decapitator-groove3-effects-explained (as-EQ + delay-return) ·
decapitator-soundtoys-quickstart (canonical numbers + cab tip).

**Links (13)** — `research/links/`: decapitator-manual-v5-controls-and-styles
(authoritative) · decapitator-musicguymixing-style-button (A/E/N/T/P map) ·
decapitator-audiopluginnews-tips (controls + Drive→EQ + gain-staging) · decapitator-
splice-creative-distortion · decapitator-808-bass-settings-wethesound · decapitator-
gearspace-styles-and-tips · decapitator-tapeop-review · decapitator-soundtoys-
product-page · decapitator-honest-review-limits-musco · decapitator-aliasing-
oversampling · decapitator-vs-other-saturators · decapitator-chaining-reverb-
shoegaze · decapitator-artists-sourced-uses.

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: official Decapitator v5 manual,
Tape Op (Pete Weiss), XNB, ARTFX, Nathan Nyquist, Distinct Mastering, Splice,
AudioPluginNews, Music Guy Mixing, Soundtoys artist/product pages. **Honesty
flags:** Gearspace/KVR 403 direct fetch (distilled from snippets, flagged in-file);
no named drone/shoegaze artist verified (relevance by technique); the Nathan Nyquist
transcript mislabels E as "triode" — corrected here per the manual.
