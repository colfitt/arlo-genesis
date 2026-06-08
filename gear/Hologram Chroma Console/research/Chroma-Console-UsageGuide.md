# Hologram Chroma Console — Usage Guide

The Chroma Console is the Texture board's **character/tape/lo-fi morpher** — four
reorderable color modules (each with 5 effects), a knob-motion recorder (**GESTURE**), a
30-second looper/sustainer (**CAPTURE**), and a global vintage-instability control
(**DRIFT**), all on a screen-free "control deck." You get the most out of it the way
**Rival Consoles** does — *light-touch layering*, "10% of this, 5% of that," to color and
"finish" a sound — and by leaning into **DRIFT + CASSETTE/REELS** for the degraded,
"beautiful sound that's really falling apart" target. In this rig it's the **mono→stereo
re-expander after the Blooper** and the partner to the Microcosm (the exact two-Hologram
pairing **Ed O'Brien (Radiohead)** runs live).

> Firmware note: the only published firmware is **v1.04 (May 5, 2025)** — faster preset
> loading + new per-module bypass MIDI CCs. No historical changelog exists, so treat
> "old-vs-new" claims with care. *(hologram-firmware-page)*

---

## 1. Essential workflows

### The control deck — learn the button combos (no screen)
- **A+B** = Secondary controls (incl. **DRIFT**, SENSITIVITY) · **A+D** = **FX Setup**
  (reorder modules + Dual Bypass + Capture routing + Filter style) · **B+C** = Copy/Save
  preset · **C+D** = **GESTURE** · **all four** = Global Settings. *(elektronauts-megathread, nervouscooks)*
- **Auto-calibrate to your instrument:** hold both footswitches → purple → play a note; it
  sets headroom. **Re-calibrate when swapping banjo/baritone/VG-800** — many effects (SWELL,
  SWEETEN, SQUASH) are level-triggered. *(wolfewithane, nervouscooks)*

### Routing (series-only, but reorderable)
- The 4 modules run **in series**; in **FX Setup (A+D)** tap the module buttons in the order
  you want them chained — there is **no per-slot parallel**. *(elektronauts-megathread)*
- **Dual Bypass:** in FX Setup, hold bypass → blinking-yellow modules bypass, solid-yellow
  stay on. Keep one module (e.g. **SWEETEN**) as an always-on core while the rest footswitch
  off. *(wolfewithane)*
- **FILTER style is a hidden 3-way** (in FX Setup, blue knob): **TILT / High-pass /
  Low-pass.** **Capture routing** PRE/POST set by the gray MIX knob (left=pre, right=post). *(elektronauts-megathread)*

### GESTURE — the motion recorder (the headline feature)
**C+D** → move an encoder (records, step lights **red** + timer) → **C+D** to stop (loops,
**green**, like DAW automation). Layer more knobs by repeating; delete one by nudging it a
hair to white; hold C+D to wipe all. **Gestures are clock-locked** — record a slow sweep,
then **re-tap/MIDI a faster tempo to play the motion back faster than your hand could move**
(or record at 120 and drop to 70 for a different feel). **Gestures save with the preset.** *(hologram-gesture-howto, hologram-sound-from-scratch-3)*

### CAPTURE — looper/sustainer
Hold the **left footswitch** to record up to **30 s**; release to loop. Short note → seamless
overlapping **ambient pad/drone (blue LED)**; longer phrase → traditional **looper (green
LED)**. Records parameter moves too; **a new recording overwrites** (no take-layering).
Routable PRE/POST-FX. **CAPTURE recordings are NOT saved in presets.** *(molten-modular, hologram-looper)*

### DRIFT — vintage instability (secondary, A+B)
The pedal's central "aged/unstable" control, strongest on MOVEMENT and DIFFUSION modules:
on **VIBRATO** it morphs sine→random + adds stereo (back MIX off for a chorus); on **SPACE**
it pitch-modulates the reverb tail; on **REELS** it ages the delay line. Bottom LEDs show the
amount and **flash on exit** to warn a secondary value is active. *(hologram-sound-from-scratch-3, molten-modular)*

---

## 2. Signature presets & settings

**First, the constraint (same as the Microcosm): presets are RECIPE-ONLY.** No file format,
no import/export, no first-party app; **80 user slots (4 banks A–D × 20) ship BLANK** — there
are **no factory presets**. Save with **B+C**; recall live via **MIDI Program Change** (no
preset footswitches). A preset stores effects + routing + all controls + **GESTURE
recordings** + Filter style + Dual Bypass + Capture routing + expression + tapped tempo (but
**not** the CAPTURE recording). The community **Chroma Controller** web editor can snapshot/
share settings over MIDI, but it's **one-way (editor→pedal)** — touch a hardware knob and it
desyncs. *(chroma-presets-how-banks-work, chroma-community-editors)*

**Sam Wittek "SW Chroma Console" pack** (MultiTracks, 10 presets, delivered as a **PDF of knob
positions** — dial by hand). The copyable recipes: *(sam-wittek-pack, sam-wittek-showcase)*
- **Wide Vibes** — VIBRATO's stereo side: collapses to the sides for a huge wide image + light
  chorus (re-widens a mono Blooper loop).
- **Huge Fuzz** — **HOWL** (resonant filter fuzz) + **DOUBLER** (width) + a little **SPACE**.
- **Analog** — warm **CASCADE** delay, modulation blooming on later repeats; **MIDI-clock-synced
  to an eighth, stacked against a dotted-eighth on a Strymon TimeLine** (one clock).
- **Supernova** — **COLLAGE** delay + a recorded **GESTURE** sweeping octaves + heavy reverb →
  ambient soundscape generator.
- **Reverse Ice** — **REVERSE** delay, **100% wet**, repeats pitched **up an octave** → pulsing
  rhythmic texture.
- **Lo-Fi** — **PITCH**-based vibrato + **FILTER** rolling off highs → chewy lo-fi wobble.
- **Tape-glue** (Hologram official): SWEETEN (50/50) → PHASER (RATE down, AMOUNT up a hair) →
  REELS (DRIFT ~50% = aged tape + stereo flutter) → CASSETTE (50%), reordered so PHASER
  modulates the delay trails. *(hologram-sound-from-scratch-1)*
- **Harmonic tremolo:** record a GESTURE on the FILTER knob sweeping ~7→10 o'clock, tempo-
  synced. *(wolfewithane)*

**Module cheat-notes:** SWEETEN = gentle clean glue (the always-on); HOWL/FUZZ = the heaviest
drives; **PITCH is the secret-weapon vibrato/chorus base** (not VIBRATO); CASSETTE = Portastudio
wow/flutter; COLLAGE = Microcosm-ish scattered delay; REVERSE works on leads/pads not staccato;
BROKEN/INTERFERENCE = databender glitch. *(sam-wittek-showcase, molten-modular)*

---

## 3. Power-user tips, tricks & hidden features

- **Gesture tempo-warp** — record slow, play back fast via clock (the manual's stated trick). *(hologram-gesture-howto)*
- **Dual Bypass core** — keep SWEETEN (or any module) always-on, footswitch the rest for in-song "adds." *(wolfewithane)*
- **Slow PHASER as a clean LFO** — RATE fully down + AMOUNT fully up = smooth movement on a sustained source. *(kvndra)*
- **Tap-tempo extension** — turning TIME up pushes delays *beyond* the tapped tempo for long evolving echoes. *(wolfewithane)*
- **Overdrive one module with another** — it's a 4-channel mixer; push a module's EFFECT VOL hot into the next for deliberate soft-clip. *(wolfewithane)*
- **MIDI CCs (confirmed):** SENSITIVITY 72, DRIFT-Movement 74, DRIFT-Diffusion 76, OUTPUT 78,
  EFFECT VOL 73/75/77/79; v1.04 added per-module bypass CCs. (PC preset-recall map not confirmed
  in captured docs — verify before scripting scenes.) *(chroma-midi-cc-manual)*

---

## 4. Notable users & techniques

- **Ed O'Brien (Radiohead)** — VERIFIED: 2025 touring **"Pitch and Glitch" board, side-by-side
  with the Microcosm** (this rig's pairing). His "make sounds that don't sound like the guitar"
  philosophy is the right lens; no published settings. *(artist-ed-obrien)*
- **Rival Consoles (Ryan Lee West)** — **the gold-standard reference for this rig's job:** Prophet
  → Chroma, *"adding 10% of this, 5% of that… a much more coloured, enhanced and finished sound."*
  On *Nocturne*, a *"beautiful melodic synth sound that's really falling apart… through this
  malfunctioning effect"* — the tape-ruined/recorded-wrong target. *(artist-rival-consoles)*
- **Darkside — Dave Harrington** — runs **Chroma + Microcosm + Eventide H90** on one improvised-
  ambient board (Premier Guitar, Apr 2025) — real proof this rig's Chroma/Microcosm/H90 trio is a
  coherent architecture. *(artist-darkside)*
- *Coverage honesty:* 2024 product — per-song/per-knob artist settings are essentially
  unpublished; the instructive material is *architecture + philosophy* + the Wittek recipes.

---

## 5. Rig-specific recipes (using gear actually owned)

- **Mono→stereo re-expander after the Blooper (the key adjacency):** capture/layer in the mono
  Blooper, then let Chroma's **DOUBLER / VIBRATO+DRIFT / SPACE** fan it back to stereo before the
  H90 (which preserves it). The single most important reason it sits where it does. *(dossier §, molten-modular)*
- **Banjo-as-lead, recorded-wrong:** **CASSETTE + FILTER (LPF)** to roll off the banjo's ice-pick
  top; **SWELL** or a recorded **GESTURE** volume swell turns staccato banjo loops into bowed
  drones; **COLLAGE/REVERSE** on a banjo Blooper loop = the signature texture. *(dossier §6, sam-wittek-showcase)*
- **Microcosm pairing labor-split:** **don't double SPACE/reverb** across the two Hologram pedals
  — let one own it, and keep Chroma's INTERFERENCE distinct from the Microcosm's glitch. *(kvndra)*
- **Clock-synced dual delays:** Chroma REELS/CASCADE clock-syncs — run an **eighth on Chroma +
  dotted-eighth on the TimeLine** off the Digitakt's clock. *(sam-wittek-showcase)*
- **Feed it the fuzz:** with Board 1 fuzz upstream feeding it hot, gain-stage with OUTPUT LEVEL +
  per-module EFFECT VOL (it can soft-clip near the headroom limit — use that deliberately or back
  off). Re-calibrate to the hotter signal. *(elektronauts-megathread, wolfewithane)*
- **Live:** set Bypass to **Buffered/Buffered+Trails** (True Bypass defeats the mono→stereo
  re-expansion), turn **Preset Audition OFF**, and use **Dual Bypass + MIDI PC** since preset
  switching has a load gap and there are no preset footswitches. *(elektronauts-megathread, molten-modular)*

---

## 6. Best learning resources

- **Hologram Electronics (official)** — the "Sound from Scratch" series + the Gesture Recording
  how-to; authoritative, concise.
- **NervousCook$** — best operational deep-dive (every button combo, calibration, reorder, dual
  bypass, filter type, globals, factory reset; confirms "no factory presets").
- **Molten Music Technology (Robin Vincent)** — the deepest single review (~66 min); superb on
  DRIFT and honest live limitations; driven from Eurorack (line-level relevant).
- **Sam Wittek** — practical, live-usable preset recipes; MIDI-clocks Chroma to a TimeLine.
- **KVNDRA** — Microcosm + Chroma pairing logic on synth.
- **Communities:** Elektronauts "Chroma Console" mega-thread (firmware/bug/MIDI tracking),
  ModWiggler + TGP (modular/guitar; both fetch-blocked — manual browse), and the community
  editors **chromacontroller.co.uk** + the Max-for-Live device. *(nervouscooks, molten-modular, sam-wittek, kvndra, elektronauts-megathread, chroma-community-editors)*

---

## 7. Common pitfalls / gotchas

- **No factory presets — 80 blank slots.** A fresh pedal auditions silent; build your own. *(chroma-presets-how-banks-work, nervouscooks)*
- **Recipe-only sharing** — no file format; share knob positions, or use the one-way community web editor. *(chroma-presets-how-banks-work)*
- **REVERSE's DRIFT appears inert** — animate a REVERSE patch with a GESTURE on TIME instead. *(elektronauts-megathread)*
- **Secondary-knob values may not be remembered per-effect** on early firmware (DRIFT carries across a module's effects) — re-set on switch. *(elektronauts-megathread)*
- **One effect per module, hard cap** — can't run two effects from the same module (e.g. COLLAGE + SPACE); use the H90/Big Sky downstream for a second time-voice. *(molten-modular)*
- **Power ≥ 500 mA, isolated** — daisy-chaining caused a high-pitched whine. *(wolfewithane)*
- **Preset switching has a load gap and there are no preset footswitches** — use Dual Bypass for adds + MIDI PC for scenes. *(molten-modular)*
- **True Bypass kills the mono→stereo re-expansion** — run buffered. *(elektronauts-megathread)*
- **Gain-staging** — it's a 4-channel mixer; a hot fuzz upstream can soft-clip the chain. *(wolfewithane)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `hologram-sound-from-scratch-1-build-preset.md` — official: build SWEETEN→PHASER→REELS→CASSETTE + reorder + dual bypass
- `hologram-sound-from-scratch-3-electric-piano.md` — official: VIBRATO/SPACE/FILTER+GESTURE patch; clearest DRIFT explanation
- `hologram-gesture-recording-howto.md` — official: the GESTURE knob-motion recorder, step by step
- `nervouscooks-deep-dive-tutorials-part2.md` — full operational walkthrough; every button combo; "no factory presets"
- `molten-modular-chroma-console-review.md` — deepest review; DRIFT/GESTURE/CAPTURE + honest live limitations
- `kvndra-microcosm-chroma-synth-soundlab.md` — Microcosm + Chroma pairing; reverb labor-split
- `sam-wittek-chroma-preset-showcase.md` — walkthrough of all 10 Wittek presets w/ module recipes

**Links** (`research/links/`)
- `chroma-presets-how-banks-and-saving-work.md` — banks/saving/browse/MIDI recall; recipe-only finding
- `sam-wittek-chroma-preset-pack-multitracks.md` — the one commercial pack (10 presets, PDF recipes)
- `chroma-console-community-editors-web-and-m4l.md` — community web + Max-for-Live editors (one-way sync)
- `chroma-console-midi-cc-implementation-manual.md` — confirmed CC numbers, clock modes, full button-combo map
- `elektronauts-chroma-console-megathread-tips-gotchas.md` — Reverse-DRIFT bug, one-per-module, tempo behavior, editors
- `hologram-firmware-page-chroma-console.md` — only v1.04 published; no historical changelog
- `wolfewithane-blog-chroma-console-usage-tips.md` — harmonic-trem gesture, reorder, tap extension, dual-bypass, power/whine
- `artist-ed-obrien-radiohead-chroma-console.md` — Ed O'Brien 2025 board placement (beside the Microcosm)
- `artist-rival-consoles-chroma-texture-finishing.md` — layered "10%/5%" finishing + "malfunctioning effect"
- `artist-darkside-dave-harrington-chroma-microcosm.md` — Chroma+Microcosm+H90 rig parallel + famous-users list

## Sources

Video (YouTube): Hologram official `dqui4XqPoEQ`, `wXX49jLXVsA`, `netMZsuuUA0` · NervousCook$
`EmCcd1NS2mY` · Molten Music `MAAuyuXL_Jk` · KVNDRA `akr7S1tlkJU` · Sam Wittek `M6rZzfBAXp4`.
Community: elektronauts.com (Chroma mega-thread t/202802) · modwiggler.com (403) ·
thegearpage.net (paywalled) · chromacontroller.co.uk + maxforlive.com (editors).
Docs/firmware: hologramelectronics.com (firmware, looper) · manualslib.com (MIDI CC manual).
Presets/artists: multitracks.com (Sam Wittek pack) · thekingofgear.com (Ed O'Brien) ·
musicradar.com (Rival Consoles) · premierguitar.com (Darkside).
