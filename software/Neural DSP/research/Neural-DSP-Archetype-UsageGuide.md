# Neural DSP Archetype (John Mayer X / Nolly X) — Usage Guide

Two boutique amp-sim plugins that are really *full rigs in a window* — amp + pre/post
FX + cab/IR + onboard reverb & delay. For this drone/doom/shoegaze rig they earn their
keep two ways: **John Mayer X** for lush ambient/shoegaze **cleans + swells** (Gravity
Tank spring/harmonic-trem → Dream Delay → Studio Verb), and **Nolly X** for **doom/sludge
low-gain walls** and big ambient washes on the **baritone**, with the rare *pre-amp delay*
and a built-in **transpose-down-a-fifth = instant baritone** trick. Host them in Logic as
AU; the onboard delay/reverb are good enough to be the whole ambient FX path. Tier-C
single-agent pass — honest where the community skews metal.

> **"X" = the new Neural DSP platform** (free update). Adds: resizable UI, **Transpose**,
> **Doubler** (one-pass double-track), **Live Tuner**, Metronome (standalone), and Quad
> Cortex compatibility (future CorOS). Per-title bumps below. `research/links/neural-x-platform-whatschanged.md`

---

## 1. What's in each plugin (the parts that matter here)

### Archetype: John Mayer X — the ambient-clean machine
`research/transcripts/neural-jmx-guitarworld-walkthrough.md`, `research/links/neural-jmx-official-intro.md`
- **3 amps** (all from Mayer's own units): **Smooth Operator** (1964 Fender Vibroverb —
  bright jangle, early gnarly breakup) · **Headroom Hero** (Dumble Steel String Singer #002
  — mid-forward, huge headroom → smooth OD via FET switch) · **Signature 83** (Two-Rock
  Signature Prototype — full-range, big clean headroom). **Three-in-One blend** runs all
  three at once with a **Room Send** (the locked "studio" sound — cab editing is disabled
  in blend mode; single-amp mode unlocks the cab block).
- **Gravity Tank** (the ambient secret weapon) — **harmonic tremolo + '60s spring reverb**
  in one box, *before* the amp. The trem adds breathing movement; the spring gets drippy.
  Reviewer's favourite combo = harmonic trem + a touch of Tube Screamer drive.
- **Pre FX**: Justa Boost (Keeley Katana, always-on fattener) · Antelope Filter (EHX
  Q-Tron+ envelope) · Halfman OD (Klon clone) · Tealbreaker (Bluesbreaker **or** Tube
  Screamer toggle) · Millipede slapback delay (Way Huge Aqua Puss).
- **Post FX**: 4-band semi-parametric **EQ** + Distressor-ish **Compressor** (Input/Output
  only) → **Dream Delay** (clean digital, tempo-sync, long tails, **Ping Pong**) →
  **Studio Verb** (Hall **or** Plate; decay/predelay/mix).
- **Cab** (single-amp only): matched cabs (15" CTS / EVM12L / G12M Greenback), 2 movable
  mics (ribbon 121 + dynamic 421, also a 57), Position/Distance, plus a **Room Send** for
  ambience. **Custom IRs loadable.**

### Archetype: Nolly X — the heavy + ambient workhorse
`research/transcripts/neural-nolly-x-secret-weapons.md`, `research/transcripts/neural-nolly-indepth-review.md`, `research/links/neural-nolly-x-official.md`
- **4 amps** (community-confirmed): **Clean** = Bogner Shiva (gorgeous, hard-to-break-up
  clean — best clean platform here) · **Crunch** = modded Marshall Super Lead (plexi
  edge-of-breakup → JCM crunch) · **Rhythm** = Peavey 6505/5150 (the metal/doom engine) ·
  **Lead** = Victory Kraken (Hiwatt/Marshall/Orange mash — **ambient crunch when gain is
  low**, squishy saturated high).
- **Pre FX**: solid-state **Compressor** (doubles as clean boost) · **Overdrive 1** (TS9/808
  Tube Screamer — **X adds a Bright toggle**) · **★ Pre-Delay** (a delay BEFORE the amp —
  rare; HP/LP tone, tempo-sync; feed *washed-out repeats into the dirt* for shoegaze
  chaos) · **Overdrive 2** (amp-in-a-box MOSFET drive; Vol/Gain/Treble/Bass — great as the
  doom dirt or a roll-off boost).
- **9-band graphic EQ** in the loop. **X adds "Nolly's Mod" EQ** = a 2nd notched-band set
  (toggle vs the original bands; dB moves persist) — useful for ambient/mid-gain, not just
  metal.
- **Cab**: 600+ IRs, 4 matched cabs (Greenback 4x12 / Marshall T75 / Mesa B30 / Zilla V30),
  4 mics (dynamics + 414 condenser + 121 ribbon). **X doubles to 4 speakers per cab**
  (closed/open Greenback; V30 straight + V30 angled; etc.) and **adds a Room Send on every
  cab**. Link/unlink amp↔cab freely. **Custom/3rd-party IRs loadable.**
- **Post FX**: stereo **Delay 2** (modulation that *pans* the repeats, ping-pong, tempo,
  hi/lo cut → tape-warm or digital) → **Reverb** (lush washed-out Hall; crank the decay —
  reviewers call it "incredible"). One specific (very good) flavour; pair an external verb
  if you want a different colour.

---

## 2. Using them for the aesthetic (drone / doom / shoegaze / lo-fi)

- **★ Ambient-clean walls (John Mayer X):** single-amp **Smooth Operator** or **Signature
  83** clean → compressor on → **Gravity Tank** (harmonic trem slow/gentle + a little
  spring) → **Dream Delay** (Ping Pong, long feedback, tempo-sync) → **Studio Verb Hall**
  (high decay, ~40%+ mix). Volume-swell into it (DAW-automate **Output** or a volume-pedal
  plugin pre-amp) → the bloom is the shoegaze "breathing." `research/links/neural-ambient-swells-technique.md`
- **★ Doom/sludge baritone wall (Nolly X):** **Rhythm (5150)** or low-gain **Lead (Kraken)**
  → keep gain loose/moderate for thick breakup → **Mesa B30** or **Zilla V30** cab, dynamic
  + ribbon → 9-band EQ scoop/tighten. Hit the front with a fuzz (see §5) for the wall. The
  "Doom Crush" factory direction = thick/gritty deep-low loose breakup for doom/sludge/stoner.
- **★ Shoegaze chaos via the PRE-delay (Nolly X):** put washed-out repeats into **Overdrive
  1 + a dirty amp** — the delay tails stack *into* the gain (a thing you can't do with a
  post delay). The Secret Weapons demo calls this the standout shoegaze move.
- **Processing baritone/banjo:** Transpose **down a 5th** ≈ a convincing baritone in a mix
  (no retune); the **Doubler** gives instant one-pass double-tracked width. Banjo through the
  Nolly Clean (Shiva) + Room Send + long reverb = an unexpected ambient bed.
- **Run on a send / as a reamp:** both work as bus/send FX (mind the dry/wet). Reamp a DI
  banjo/synth/baritone through them at mix to audition amps non-destructively. To dodge
  plugin latency, the standalone-app + print-the-wet workflow works (see §4).
- **Lo-fi:** Nolly Delay 2 hi/lo-cut → tape-warm repeats; stack SketchCassette II / RC-20 /
  Decapitator *after* the plugin for the degraded layer (Neural makes the amp bed, the
  tape/lofi boxes do the damage).

---

## 3. Copyable recipes

1. **Mayer X ambient-clean wall** — Smooth Operator (single amp), Bright on, gain low;
   Compressor smooth, light; **Gravity Tank**: harmonic trem speed slow / intensity low +
   spring ~20–30%; **Dream Delay**: Ping Pong, tempo 1/8 or 1/4, feedback high-ish, mix
   ~30–40%; **Studio Verb Hall**: decay high, mix ~40%+. Volume-swell chords in. Sparse
   voicings. (Mayer reviewers' "Gravity Clean"/"Plate ~45% mix, short decay, little
   predelay" for tighter ballad cleans.)
2. **Nolly X doom/sludge baritone wall** — Rhythm (5150), gain ~10–12 o'clock (loose, not
   tight-metal); Overdrive 2 as dirt OR external fuzz in front; Mesa B30 cab, 57 + 121;
   9-band EQ: scoop low-mids slightly, roll highs ~just above 6–8k; Delay 2 light, Reverb
   Hall decay cranked. Drop/baritone tuning. Add Transpose −5th for sub-bass weight.
3. **Nolly X shoegaze lead (pre-delay-into-dirt)** — Clean or Crunch amp; **Pre-Delay**
   tempo-sync, feedback ~40–50%, into **Overdrive 1 (Bright)**; post Delay 2 ping-pong +
   Reverb long. Let the repeats build into the gain; play sparse.
4. **Banjo/synth reamp ambient bed** — DI → reamp into **Nolly Clean (Shiva)** + Room Send
   → big Reverb (decay max) → optional SketchCassette II after for wow/flutter.

---

## 4. Rig-specific notes (Logic / hardware)

- **Logic Pro (AU):** loads as AU; tempo-sync delays lock to the project BPM automatically.
  Use Logic automation on the plugin **Output** for volume swells. **Freeze** the track —
  Neural plugins are CPU-heavy; use the input gate (set threshold to kill hiss, not
  sustain) and dial global input so it peaks **−14 to −9 dB** (Neural's own spec). Cmd-drag
  = fine knob adjust; double-click = default; right-click a knob = MIDI Learn (map to the
  61SL MkIII or an expression pedal for live swells). `research/links/neural-x-platform-whatschanged.md`
- **Latency / standalone trick:** run the **standalone app**, route guitar in via the
  interface, and **print the processed audio** to the DAW (or reamp DI tracks at mix) — the
  Secret Weapons reviewer does this to avoid plugin monitoring latency. `research/transcripts/neural-nolly-x-secret-weapons.md`
- **Ableton Live 12 Lite:** loads fine as a VST3/AU; watch the device/CPU ceiling — bounce
  heavy ambient takes to Logic.
- **Custom IRs:** both load 3rd-party IRs in the cab block (left/right mic dropdown → Load
  Custom IR). Drop in your favourite cab/space IRs; or unlink amp↔cab for mismatched pairings.

---

## 5. Neural vs Iridium vs Guitar Rig 7 (reach-for map)
`research/links/neural-vs-iridium-vs-plugins.md`

| Need | Reach for |
|---|---|
| Commit the amp tone while **tracking** (with band/loops), latency-free DI | **Strymon Iridium** (hardware) — print it; "more like a real amp than a real amp." |
| The *specific* modelled amp (Dumble/Two-Rock cleans; Shiva/5150/Kraken) + onboard ambient FX, revisable at mix | **Neural Archetype** — deeper amp + full FX + custom IR, non-destructive. |
| Build an **elaborate degraded/lo-fi chain** in one window, or process **non-guitar** (synth/drums) | **Guitar Rig 7** — modular FX rack, freely reorderable, lo-fi suite + routing. |

- **vs Iridium:** Iridium = the committed front-end you *print* (esp. tracking live); Neural
  = the flexible reamp/mix amp with its own reverb/delay and the exact voice you want. "Besides
  high-gain, the tonal quality is not that different." Plugin caveat = slight insert latency
  (use standalone+print, §4).
- **vs Guitar Rig 7:** GR wins versatility/reorderable-routing/lo-fi and **non-guitar**
  duty; Neural wins realism/feel and turnkey artist-rig tones. For a doom *wall* on baritone,
  Neural Nolly is the more convincing amp; for a *degraded experimental* texture, GR's
  reorderable rack (distortion-last trick) is the tool. `Software/Native Instruments Komplete 15 Ultimate/research/Guitar-Rig-7-UsageGuide.md`

---

## 6. Best demos & resources

1. **Secret Weapons — "Archetype: Nolly X | Secret Weapons Demo"** ★ — the single best Nolly
   X source for *this* rig: ambient/shoegaze use of the pre-delay-into-dirt, the new room
   sends, Nolly's Mod EQ, the transpose-down-a-fifth baritone trick, and the (excellent)
   reverb. Non-metal angle. `research/transcripts/neural-nolly-x-secret-weapons.md`
2. **Guitar World (Pete) — "Archetype John Mayer X demo & walkthrough"** ★ — full JM X device
   tour incl. Gravity Tank, Dream Delay, Studio Verb hall/plate, transpose, doubler.
   `research/transcripts/neural-jmx-guitarworld-walkthrough.md`
3. **In-depth Nolly review** (original Nolly; same architecture) — the definitive amp/cab/IR
   breakdown (confirms every modelled amp + cab). `research/transcripts/neural-nolly-indepth-review.md`
4. **Official product/intro pages** — authoritative feature lists.
   `research/links/neural-jmx-official-intro.md`, `research/links/neural-nolly-x-official.md`
5. **Preset packs** (paid, for shortcuts): Chernobyl Audio "Doom Metal Vol 1" (Nolly X,
   10 presets, Standard E→Drop A, Paradise Lost/Candlemass vibe); Adam Dodson / Mix-Ready
   ambient & mix-ready packs; Karl Golden "Shoegaze Wash / Shimmer Clean / Lush Swells"
   presets. (No settings exposed on the pages — results-only.)

---

## 7. Pitfalls / gotchas

- **CPU-heavy** — freeze tracks in Logic; standalone+print to dodge insert latency.
- **No effect reordering** (all Neural plugins) — the signal chain is fixed; you can't put
  distortion *after* reverb in-plugin (do that in Logic/Guitar Rig if you want the
  distortion-last wall).
- **JM X 3-amp blend locks the cab** — drop to a single amp to edit the cab/mics/Room Send.
- **Transpose tracks single notes; chords get "dark & wobbly" past ~4 semitones** (JM X) —
  fine for the −5th baritone trick on lines/power-chords, less so for dense voicings.
- **Reverbs are one (good) flavour** — both onboard verbs are a specific washed-out Hall;
  for a different space, pair Valhalla/Logic ChromaVerb after.
- **Community skews metal/djent** — almost no named drone/shoegaze artist using these
  surfaced; relevance here is by technique (ambient cleans, low-gain doom, baritone), not
  by artist precedent. **Honest flag:** the ambient/doom angle is reviewer- and
  technique-derived, not a documented signature use.

---

## 8. Captured sources

**Transcripts (4)** — `research/transcripts/`: neural-nolly-x-secret-weapons ·
neural-nolly-x-pmg-review · neural-nolly-indepth-review · neural-jmx-guitarworld-walkthrough.
**Links (5)** — `research/links/`: neural-jmx-official-intro · neural-nolly-x-official ·
neural-x-platform-whatschanged · neural-vs-iridium-vs-plugins · neural-ambient-swells-technique.

## Sources

Every claim cites a captured file (first line = original URL). Primary: official Neural DSP
product/intro pages; YouTube walkthroughs (Guitar World, Secret Weapons, in-depth review,
PMG); Guitar World / MusicRadar / Sound on Sound reviews; Strymon + Gearspace/TapeOp for the
Iridium comparison; Guitar World / ambientguitar.net for swell technique. **Honesty flags:**
the in-depth Nolly review covers the *original* (pre-X) plugin — amp/cab architecture is
identical, X-only additions (Nolly's Mod EQ, 4 speakers/cab, room sends, transpose/doubler)
are confirmed from the Secret Weapons (X) demo + official pages. Doom/ambient framing is
technique-derived; no preset-pack page exposed concrete settings. Gearspace threads were
403/paywalled in places — corroborated across the aggregated review sources.
