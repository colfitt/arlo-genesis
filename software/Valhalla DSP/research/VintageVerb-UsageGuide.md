# VintageVerb — Usage Guide

VintageVerb is the in-the-box **vintage-colored ambient/character reverb** — 20+
algorithmic modes × 3 era "color" modes, decay to **70 s**, near-zero CPU. The
whole point for this rig: it's a *colored, modulated, era-degradeable* reverb, not
a clean realistic space (its sibling **Room**, also installed, is the transparent
one — next wave). Choose the mode by the **sound character** you want (not the
instrument), keep it **100% wet on a send**, carve with PreDelay/EQ/Damping rather
than just cranking Mix, and **stack instances** for walls. Its two real limits —
**no Freeze, 70 s ceiling** — are exactly where Big Sky and the free Supermassive
come in (see §5/§7). `research/links/vintageverb-kvr-how-do-you-use.md`, `research/links/vintageverb-faderpro-how-to.md`

## 1. Essential workflows

- **Pick by character, not instrument** — VintageVerb = colored/lush/modulated/
  "unreal"; reach for it when you want vintage texture, not a believable room. `research/links/vintageverb-kvr-how-do-you-use.md`
- **100% wet on an aux send** (Mix = full wet); EQ and saturate the *wet only* on
  the return. `research/links/vintageverb-faderpro-how-to.md`
- **Build a wall:** long Decay + big Size + **raised Attack** (slow swell) + Mod up
  + High Cut down (~2–3 kHz) + Low Cut ~300 Hz. `research/transcripts/vintageverb-flo-controls-walkthrough.md`
- **The color modes are the lo-fi engine** — flip 1970s on a sustained drone for the
  degraded/"recorded-wrong" character (see §2). `research/links/vintageverb-chaotic-and-color-modes.md`

## 2. Signature settings & presets (copyable)

**Modes — which for ambient/drone:** `research/links/vintageverb-official-modes-taxonomy.md`, `research/links/vintageverb-modes-sean-costello.md`
- **Chaotic Hall / Chaotic Chamber / Chaotic Neutral** — *the drone family.*
  Tape-derived: wow/flutter + tape saturation (higher internal drive) that actually
  *reduces* ringing → long tails that stay **clear**. Chaotic Chamber "glues source
  and reverb together." Pair with 1970s color for the degraded tape wall.
- **Random Space / Chorus Space** — deep, wide, slow-attack; **Chorus Space** adds
  lush chorused mod (the shimmer-ish wide wash).
- **Concert Hall / Bright Hall** — the classic lush late-70s/80s ambient halls.
- **Sanctuary** — dense detuned late reverb + bit-reduction → near-infinite **bloom**
  pad (also mono-in/stereo-out).
- **Cathedral / Palace / Hall1984** — huge **clean** spaces ("BIG yet clear") when
  you want a cathedral wall without mud.
- **Dirty Hall / Dirty Plate / Chamber1979** — gritty late-70s hardware character
  (depth/grit, not size).

**The 3 color modes:** `research/links/vintageverb-chaotic-and-color-modes.md`
- **1970s** — dark, noisy mod, **downsampled, 10 kHz ceiling**; sustained notes throw
  "strange random sidebands." **The gold setting for the degraded drone aesthetic** —
  most audible on long tails.
- **1980s** — full-rate but still gritty/dark mod, brighter.
- **Now** — clean, transparent, bright. Color is subtle on short sounds, obvious on
  held drones.

**Key controls:** Decay (0.2–70 s) · Size · **Predelay** (push 20–60 ms to keep the
dry pitch legible under a long tail) · **Attack** (high = slow swell into the wall) ·
**Bass Mult × Bass Freq** (set Freq ~250 Hz, Mult <1.0 to make lows decay *shorter*
so long tails don't turn to mud) · **Damping** (darkens the tail *over time* — ≠ the
static HiCut/LowCut EQ) · **Mod Rate/Depth** (unusually musical — push for chorused
shimmer-adjacent tails without obvious wobble) · Mix. `research/transcripts/vintageverb-flo-controls-walkthrough.md`, `research/links/vintageverb-reviews-cycling74-plugindrop.md`

**Copyable recipes** (synthesized from the control walkthroughs + ranges — not one
verbatim forum patch): `research/links/vintageverb-ambient-settings-recipes.md`
- *Infinite ambient wash* — Chaotic Hall/Sanctuary · 1970s · Decay 20–40 s · Size
  ~90–100% · Predelay 0–20 ms · Mod low rate/med-high depth · HiCut ~3–4 kHz · LowCut
  ~250 Hz · Mix 100% (return).
- *Drone bed* — Chaotic Chamber · 1970s · Decay 10–20 s · Attack high · Bass Mult
  ~0.5 @ 250 Hz · HiCut ~2.5 kHz · LowCut ~300 Hz.
- *Lo-fi 1970s grainy verb* — Dirty Hall/Sanctuary · 1970s · Decay 3–6 s · HiCut
  ~2 kHz (the 10 kHz ceiling does the rest) · embrace the noisy sidebands.
- *Lush long plate* — Plate/Smooth Plate · Decay 4–8 s · Predelay 20–40 ms · Mod up.
- *Cathedral/huge clean* — Cathedral/Palace/Hall1984 · Now or 1980s · Decay 6–12 s ·
  Size max · Predelay 40–80 ms.
- *Chorused shimmer-ish tail* — Chorus Space · Decay 8–15 s · Mod Depth high · large
  Size.
- *Banjo/guitar ambient* — two returns: ① Chamber mode "Fat Plate," ~2.5 s, HiCut
  ~2 kHz; ② short Ambience/tiled room; LowCut ~300 Hz on each.

## 3. Power-user tips, tricks & hidden features

- **Huge Size + Decay near 70 s = "almost frozen"** — the fake-infinite move (there's
  no real Freeze). `research/links/vintageverb-mono-cpu-gotchas.md`
- **Mod is unusually musical** — VintageVerb's nearest thing to Shimmer; crank Rate +
  Depth for chorused tails without obvious pitch wobble. `research/links/vintageverb-reviews-cycling74-plugindrop.md`
- **Damping vs EQ are two tools** — Damping shapes how the tail darkens over time; the
  HiCut/LowCut sets the wet's static balance. Use both. `research/links/vintageverb-faderpro-how-to.md`
- **The Chaotic modes' saturation reduces ring/mud** in long tails (counterintuitive)
  → clear tape-warble drones. `research/links/vintageverb-chaotic-and-color-modes.md`
- Hover a Mode name for its sonic personality; right-click for preset/init.

## 4. Notable users & techniques (sourced, flagged)

- **Tycho — "Awake"** (Reverb Machine breakdown, HIGH): the two-insert wall — #1 *Fat
  Plate @ Mix 15%* to de-dry, then #2 *Large Hall, 1970s, Mix 30%, Mod cranked*, with
  a **delay AFTER the reverb** so the modulated tail gets repeated = bigger wall.
  Maps straight onto **VintageVerb → EchoBoy → comp/EQ**. ★ the directly transferable
  recipe. `research/links/vintageverb-tycho-awake-reverbmachine.md`
- **Kendrick/SZA "All the Stars"** (Sound on Sound Inside Track, HIGH) — VintageVerb in
  the vocal chain; proves pro ubiquity (vocal, not ambient). Charlie Puth/Calvin Harris
  = MEDIUM (marketing-sourced). `research/links/vintageverb-artists-sourced.md`
- **Honest flag:** no sourced evidence for Stars of the Lid / Tame Impala / Bon Iver —
  the ambient reputation is real but word-of-mouth; only Tycho + Kendrick are safe to
  cite. None invented. `research/links/vintageverb-artists-sourced.md`

## 5. Rig-specific recipes (your gear by name)

- **vs the hardware reverbs:** VintageVerb wins on recall, automation, cheap
  multi-instancing, and vintage color → the studio/back-end air & texture. **Big Sky**
  for Cloud lushness + **real Freeze** (held infinite drones VVV can't do) and to reamp
  a played bed. **Microcosm** for granular/glitch/loop textures. **H90** for pitched/
  modulated reverb-as-instrument (Blackhole). Workflow: capture moody beds *through the
  pedals*, then add recallable color/depth with VintageVerb. `research/links/vintageverb-vs-bigsky-hardware.md`
- **VintageVerb → EchoBoy → comp/EQ** (the Tycho wall): big modulated tail repeated by
  the delay, then bus-glue so it stays cohesive, not muddy. `research/links/vintageverb-tycho-awake-reverbmachine.md`
- **Saturate the return:** Decapitator or RC-20 *after* VintageVerb on the wet (LowCut
  first) = the saturated doom/shoegaze wall. `research/links/vintageverb-creative-chaining-izotope.md`
- **Reverb-into-reverb:** VintageVerb for texture/color + a few % **Room** for stereo
  image and depth (both owned). `research/links/vintageverb-forum-ambient-tips-and-vs-room.md`
- **★ Budget note — install the FREE Supermassive.** It fills VintageVerb's two gaps:
  a genuine **infinite/Freeze** (max Feedback) and delay-meets-reverb feedback washes
  that drift forever. Division of labor: VintageVerb = characterful believable space;
  Supermassive = held infinite underbed + cascading feedback drone. Stack them. (Paid
  **Shimmer** is unnecessary — VVV's musical Mod + Supermassive cover most shimmer needs
  at $0.) `research/links/vintageverb-vs-supermassive-free.md`, `research/links/vintageverb-best-reverb-for-costello.md`

## 6. Best learning resources

1. **Valhalla DSP blog (Sean Costello)** — authoritative mode taxonomy: "The MODES,"
   the 1.7.1 "Chaos Reigns" (Chaotic modes), 4.0.0 (Chamber1979/Hall1984) posts.
2. **Flo of Music — "How to use VintageVerb"** — clearest control-by-control (Bass Mult
   math, damping, attack).
3. **The Indie Music Lab — step-by-step** — return-track + preset-first workflow, the
   EQ "blanket" warm-verb moves.
4. **Reverb Machine (Tycho "Awake")** — the sourced ambient-wall recipe.
5. KVR "best Valhalla for ambient" threads; iZotope creative-reverb techniques.

## 7. Common pitfalls / gotchas

- **No Freeze, 70 s ceiling** — for truly held drones use Big Sky's Freeze or
  Supermassive's max-feedback infinite. `research/links/vintageverb-mono-cpu-gotchas.md`
- **No post-reverb EQ on the tail** — chain a separate EQ after it (on the return).
- **Mono behavior varies by mode** (Sanctuary = mono-in/stereo-out; others sum
  differently) — check mono compatibility if collapsing or feeding a mono pedal chain. `research/links/vintageverb-mono-cpu-gotchas.md`
- **Mud:** long decay + no LowCut = boom — always LowCut the wet; predelay keeps pitch
  legible.
- **1970s/Dirty modes add real artifacts** (downsampling/quantization) — that's the
  character, not a clean reverb; don't use them when you need transparency.
- **CPU is a non-issue** on Apple Silicon (~32 instances <30%). The "big verb glosses
  over poor playing" cliché — carve, don't drown. `research/links/vintageverb-mono-cpu-gotchas.md`

## 8. Captured sources

**Transcripts (2)** — `research/transcripts/`: vintageverb-flo-controls-walkthrough
(control-by-control engine) · vintageverb-indie-music-lab-step-by-step (return-track
preset-first workflow).

**Links (16)** — `research/links/`: modes/color (vintageverb-official-modes-taxonomy,
vintageverb-modes-sean-costello, vintageverb-chaotic-and-color-modes) · controls/
recipes (vintageverb-faderpro-how-to, vintageverb-reviews-cycling74-plugindrop,
vintageverb-ambient-settings-recipes) · workflow/community (vintageverb-kvr-how-do-you-use,
vintageverb-kvr-best-for-ambient, vintageverb-forum-ambient-tips-and-vs-room,
vintageverb-creative-chaining-izotope) · artists (vintageverb-tycho-awake-reverbmachine,
vintageverb-artists-sourced) · comparisons (vintageverb-vs-bigsky-hardware,
vintageverb-vs-supermassive-free, vintageverb-best-reverb-for-costello) · gotchas
(vintageverb-mono-cpu-gotchas).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/`
(first line of each = the original URL). Primary: the Valhalla DSP blog (Sean
Costello), Flo of Music, The Indie Music Lab, Reverb Machine, Sound on Sound, KVR,
iZotope, Cycling '74/PluginDrop. **Honesty flags:** YouTube yt-dlp was 429
rate-limited (only 2 video transcripts; the blog is the authoritative mode
reference); Gearspace/Equipboard/MOD WIGGLER 403'd (snippet-distilled, flagged
in-file); copyable values are synthesized from control ranges, not one verbatim
patch; artist claims beyond Tycho/Kendrick are flagged MEDIUM or excluded.
