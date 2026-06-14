# ValhallaRoom — Usage Guide

ValhallaRoom is the in-the-box **transparent / realistic depth-and-space reverb** —
a **dual-engine** algorithm (separate **Early** + **Late** reverbs crossfaded by a
**Depth** knob), 12 modes, decay to **100 s**, near-zero CPU. It's the *anonymous,
psychoacoustic* sibling to VintageVerb's *colored, era-degradeable* character (both
installed). The whole point for this rig: Room supplies **believable depth and
placement** plus **lush evolving walls** without a vintage stamp — the natural space
*under* VintageVerb's color. Choose the mode by **how realistic vs how lush/dark** you
want it, run **100% wet on a send** (carve with the 3-band decay multipliers + High/Lo
Cut, not just Mix), and use **Depth** to move between close placement (Early) and big
tail (Late). `research/links/room-controls-deep-dive.md`, `research/links/room-vs-vintageverb.md`

> **★ Brief correction (verified):** ValhallaRoom has **no "Bloom" mode** —
> "Bloom" is a *ValhallaShimmer* concept (the Alesis Midiverb II preset Shimmer
> emulates), not in Room. Room also has **no Halls / RandomSpace** named modes
> (those are VintageVerb territory). In Room the **bloom/evolving-pad job** is done
> by **Bright Room** (long decay → pad) and the **slow-attack Alien modes
> (LV-426 etc.)**; the drone-wall job by the **Dark** modes. There is **no Freeze**.
> `research/links/room-official-modes-taxonomy.md`

## 1. Essential workflows

- **Dial in this order:** Mode → **Early Size** → **Late Size** → Decay → High Cut →
  **Depth** → fine-tune Mod + the 3-band decay mult. The workhorse method: most of the
  sound is set by Mix/Decay/High Cut + the two Size knobs. `research/transcripts/room-workhorse-parameter-walkthrough.md`
- **100% wet on an aux send**; EQ/saturate the *wet only* on the return (or use the
  built-in **Lo Cut**, added v2.0.0). `research/links/room-controls-deep-dive.md`
- **Use Depth as the depth/placement knob** — 0% = Early reflections only (close,
  placed, no tail) … 100% = Late tail only (the body/wall). It crossfades the two
  engines. `research/transcripts/room-late-section-crossover-decay.md`
- **Build a wall:** a dark/slow mode (LV-426 / Dark Space) · Depth 100 · long Decay ·
  big Late Size · large Early Size + **Early Send ~1.0** for a slow swell-in · Late Mod
  up · High Cut down · **Bass Mult < 1** so the lows don't turn to mud. `research/links/room-ambient-settings-recipes.md`

## 2. The modes — which for ambient/drone vs depth `research/links/room-official-modes-taxonomy.md`

**Natural / realistic depth:**
- **Large Room** — most "natural"; modulation widens the image **without** random pitch
  shifts → the stable, believable default bed.
- **Medium Room** — wider/"square," sparse early density; mod *can* pitch-shift on long
  decays. Classic-Lexicon flavor.
- **Large Chamber / Dense Room** — "larger than life," **colorless**, high echo density
  → the clean big neutral space.

**Evolving pad (the in-Room "bloom"):**
- **Bright Room** — slower attack, extra HF "air/sheen," deep random chorusing.
  **"Long decays turn static input into evolving pads"**; "close to string ensembles"
  at some settings. Costello's reference: *Vangelis "Blade Runner."* ★

**Dark / lo-fi / deep-space (the drone-doom family):**
- **Dark Room** — deliberately **lo-fi**: noisy interpolation, **no highs above ~11 kHz**,
  grainy flutter, lush randomized chorusing. ★ the degraded/tape-aesthetic mode (Room's
  answer to VVV's 1970s color). Crank Early+Late Mod Depth.
- **Dark Chamber** — washier dark chamber. **Dark Space** — HUGE dark space, deep
  detuning mod → the biggest dark wall.
- **Nostromo / Narcissus / Sulaco / LV-426** (Alien-named) — dark, **slow-attack**, lush
  random modulation, beautiful long decays. **LV-426** = slow-attack + dense + deep =
  ★ the lush slow-bloom drone mode (community: also great for lo-fi/retro). Narcissus =
  "great on pianos," lowest CPU. Sulaco = lots of detune, Late Cross moves its image.

## 3. Early ↔ Late dual-engine & depth `research/links/room-controls-deep-dive.md`

- **Two stereo reverbs in one:** **Early** = first reflections / placement / distance
  (subtle bursts up to ~1 s gated); **Late** = diffuse decaying body (0.1–100 s). The
  **Depth** knob crossfades them (equal-power) and *is* the depth/placement control. `research/transcripts/room-late-section-crossover-decay.md`
- **Costello's own framing for Depth** (clears up the #1 misunderstanding): it's a
  **level-normalized** crossfade, so it changes *character/distance, not loudness* —
  think **"moving a mic further from the source: the blend of close mics (low Depth =
  placement/attack) vs room mics (high Depth = body)."** 50% is the canonical start. `research/links/room-costello-early-and-depth-technique.md`
- **Early Size** does attack+decay for the early reflections in one knob — the biggest
  determinant of perceived size; **dial it first.** 10–50 ms = small-room reflections /
  widening; >100 ms = gated territory. `research/transcripts/room-workhorse-parameter-walkthrough.md`
- **Early Send** feeds the early energy into the Late reverb (0 = parallel, 1.0 = max):
  big Early Size + Send 1.0 = a **slow cathedral-like onset**; the way to get a swelling
  bloom into the tail. `research/links/room-early-tricks-gated-space.md`
- **Space** (v2.0.0, Early tab) = feedback around predelay+early; **>60% the early
  reflections become their own self-feeding reverb** → a modulated wash from the Early
  engine *alone*, distinct from the Late tail. ★ Room's nearest thing to a runaway drone
  source. `research/links/room-early-tricks-gated-space.md`

## 4. Key controls & building blooms `research/links/room-controls-deep-dive.md`

Mix · **Predelay** (0–20 ms safe; >50 ms = slapback; "moves the walls") · **Decay**
(RT60 on the Late, mid-based) · **High Cut** (3–7.5 kHz for big rooms) · **Lo Cut**
(v2.0.0 low shelf — keeps long tails out of mud without an external EQ) · **Depth** ·
**Late/Early Size** · **Cross** (stereo spread, subtle) · **Diffusion** (low = distinct
slaps, high = smooth wash — **1.0 for clean spaces, but DROP to 0–0.5 for grit** — dark-ambient
presets sit grainy at 0–0.5, halls at 0.9–1.0) · **Mod
Rate/Depth** (0.25–0.5 Hz warms; 1–2 Hz string-ensemble; smooths *or* lushes the tail).

**The bloom-shaping engine = the 3-band decay multipliers** (Room's signature control):
`research/transcripts/room-late-section-crossover-decay.md`
- **Bass Xover + Bass Mult** — scales the Decay for lows. **0.5× = lows decay in half the
  time** (10 s → 5 s); **2× = lows ring twice as long.** Mult **< 1** keeps a long wall
  clear; **> 1** = a blooming, swelling low drone.
- **High Xover + High Mult** — scales the Decay for highs. **High Mult > 1 (Xover
  ~4–6 kHz) = the highs ring LONGER than the body → a rising, airy sheen** = the closest
  Room gets to a "shimmer" trick (bright-tail emphasis, **not** pitch shift). **Invert
  it for realism:** Costello's *believable concert-hall* move is **High Mult well below
  1.0 @ Xover ~2–4 kHz** (highs decay shortest, like real halls). So High Mult >1 =
  ethereal/airy, <1 = believable space.

## 5. Signature settings & presets (copyable) `research/links/room-ambient-settings-recipes.md`

(Synthesized from official control ranges + the two transcripts — not one verbatim
factory patch. All 100% wet on a send unless noted.)
- **Natural ambient space** — Large Room · Depth 70–80 · Predelay 15–25 ms · Decay
  2–4 s · Early Size ~30 ms · High Cut 5–7 kHz · Lo Cut ~150 Hz · Mod low.
- **Lush bloom drone** — **LV-426** or Dark Space · Depth 100 · Decay **15–30 s** · Late
  Size near max · large Early Size + **Early Send ~1.0** · Late Mod ~0.5 Hz/high · High
  Cut 2.5–3.5 kHz · **Bass Mult ~0.6 @ 250 Hz.**
- **Big realistic hall** — Large Chamber/Dense Room · Depth 85 · Predelay 30–60 ms ·
  Decay 6–12 s · Late Size max · Early Size 50–80 ms.
- **Tight room "glue"** — Medium/Large Room · Decay 0.3–0.8 s · small Early+Late Size ·
  Diffusion high · **Mix ~10–15% (insert, not send).**
- **Depth bed under VintageVerb** — Large Room · **Depth 0%** (Early only) · Early Size
  **< 40 ms** · Mod off · low Mix → pure placement, then into VVV's colored wall.
- **Degraded lo-fi tape drone** — **Dark Room** · Depth 100 · Decay 10–20 s · Early+Late
  Mod Depth high · High Cut ~3 kHz · Bass Mult ~0.6 → then **saturate the return**.
- **Shimmer-ish rising tail** — Bright Room · Decay 8–15 s · **High Mult 1.5–2.0 @ Xover
  ~4–6 kHz** · Late Mod high.
- **Self-feeding Space drone** — Depth 0% · **Space 65–85%** · large Early Size · Early
  Mod Depth high (a wash built from the Early engine alone).
- **Real shared presets (KVR, normalized 0–1 values)** — *Andromeda* (dark ambient:
  Depth 0.8, lateModDepth 0.7, earlySend 0.7 — the closest ready-made **drone bed**) ·
  *Oort Cloud* (dark/grainy, Diffusion 0) · *Nerevar* (long/grainy, Late Size max). `research/links/room-kvr-shared-presets.md`

## 6. Power-user tips, tricks & hidden features

- **Depth = 0% unlocks the Early engine** — gated reverbs (Predelay 0, Diffusion 100,
  Early Size ~150 ms), tight placement beds, or Space drones. The underused half of the
  plugin. `research/links/room-early-tricks-gated-space.md`
- **3-band decay = surgical tails** — set bass/mid/high decay independently; the move
  that keeps huge tails clear (lows short, body medium, highs long for sheen). `research/transcripts/room-late-section-crossover-decay.md`
- **Diffusion = clean vs grit** — 1.0 stays smooth (won't go metallic on vocals/drums);
  **drop toward 0 for grainy, textured dark-ambient tails.** `research/links/room-kvr-shared-presets.md`
- **Early Size as a tone map** (Costello): **10–50 ms** = small-room reflections / stereo
  widening; **50–100 ms** = a "compressed room" (attack squashed, slight gating); **150
  ms+ with Early Send 1.0** = a slow cathedral onset that *adds clarity*. `research/links/room-costello-early-and-depth-technique.md`
- **Near-frozen, not frozen** — Decay tops at **100 s** (longer than VVV's 70) so a
  "held" wall is easier, but there's no real Freeze. `research/links/room-vs-vintageverb.md`
- Hover a Mode for its character; v2.0.0 GUI is resizable; 150+ factory presets.

## 7. Rig-specific recipes (your gear by name)

- **Room (depth) → VintageVerb (color):** Room places/depth-beds the dry source
  (Depth low, short Early Size), VintageVerb adds the degraded vintage wall on top — the
  two are complementary, both owned. Or invert: transparent Room as the realistic wall,
  VVV on a parallel send for color. `research/links/room-vs-vintageverb.md`
- **vs the hardware:** Room wins on recall/automation/cheap multi-instancing + anonymous
  depth. **Big Sky** = Cloud lushness + **real Freeze** (held infinite drones Room can't
  do) + reamping a played bed. **Microcosm** = granular/glitch loops. **H90/Blackhole** =
  pitched/modulated reverb-as-instrument (and *real* shimmer). Capture moody beds through
  the pedals, then add recallable depth with Room. `research/links/room-community-tips.md`
- **Saturate the return:** Dark Room wall → **Decapitator / SketchCassette / RC-20** on
  the wet (Lo Cut first) = the saturated doom/shoegaze wall. (Or saturate *before* the
  send so the space inherits "baked-in" harmonics — subtler.) `research/links/room-ambient-settings-recipes.md`, `research/links/room-chaining-send-saturation-delay.md`
- **Reverb → Delay = the ambient-wall order:** Room (or Room→VVV) **into EchoBoy** on a
  send — the reverb washes the source, the delay re-throws the wash into a swelling wall
  (delay *after* reverb destroys clarity on purpose; delay *before* stays legible). Pair
  with a **two-send** setup: a short-Room send (placement) + a long-Room/VVV send (size)
  from one banjo/baritone. `research/links/room-chaining-send-saturation-delay.md`
- **Banjo / baritone placement:** Room on the track, **Mix ~10%**, Depth 0%, Early Size
  < 40 ms = a believable room without a wash — then send to a long Room/VVV wall for
  size. `research/links/room-community-tips.md`
- **★ Free add — Supermassive** fills Room's two gaps: genuine **infinite/Freeze** (max
  feedback) and cascading delay-reverb drones. Division of labor: Room = believable depth
  + lush dark walls; Supermassive = held infinite underbed. `research/links/room-vs-vintageverb.md`
- **Plate weakness:** Room is poor at plates — use a convolution reverb + plate IRs, or
  VintageVerb's plate, for that job. `research/links/room-community-tips.md`

## 8. Notable users & techniques (sourced)

Honest: sourced ValhallaRoom attributions are thin and skew electronic/EDM — **no
sourced ambient/post-rock/shoegaze artist on Room specifically** (the ambient rep is
real but word-of-mouth). None invented. `research/links/room-artists-sourced.md`
- **Noisia** — called ValhallaRoom their **favourite reverb plugin** (Noisia Radio
  S02E22, ~38:20). HIGH — the best-sourced endorsement found.
- **Rob Swire / Knife Party** — "Valhalla Room sounds awesome" (Valhalla product page).
  HIGH. MEDIUM (Equipboard-listed): Martin Garrix, 3lau, A.G. Cook (PC Music), Cazzette.
- **Documented technique:** dial a usable space in 10–20 s; producers run **~28
  instances per track** for per-element spatial design (CPU is a non-issue).

## 9. Best learning resources

1. **Valhalla DSP blog (Sean Costello)** — authoritative: "The Reverb Modes," "The High
   Level Sliders," "The Early Controls," the Dark Room / Sulaco / LV-426 mode posts, the
   v2.0.0 Space/Lo-Cut post, and the Tips-and-Tricks (gated, short drum rooms).
2. **"Valhalla Room Tutorial — In Depth How to Use" (YouTube)** — the workhorse
   parameter-by-parameter walkthrough; best on the Depth / Early-Size / Late-Size interplay.
3. **"HOW TO: Valhalla Room Reverb" (YouTube)** — clearest on the 3-band decay
   multipliers + crossovers (with the math) and Diffusion.
4. **Splice "Huge Reverb in a Compact Interface"** — concise mode + control overview.
5. KVR/Gearspace threads (guitar/ambient tips, vs-VintageVerb); Audiotent "Reflections"
   preset pack (size/instrument-sorted starting points).

## 10. Common pitfalls / gotchas

- **No Bloom mode, no Halls, no Freeze, no real Shimmer** in Room — don't go looking for
  them (use Bright Room/LV-426 for blooms; Big Sky/Supermassive for Freeze; Shimmer/H90
  for pitched shimmer). `research/links/room-official-modes-taxonomy.md`
- **Mud:** long Decay + no Lo Cut/Bass Mult = boom. Always **Bass Mult < 1** and/or Lo
  Cut on big tails; Predelay keeps the source legible.
- **Dark Room is genuinely lo-fi** (11 kHz ceiling, noisy interpolation) — that's the
  character, not a clean reverb; don't use it when you need transparency.
- **Plates are a weak point** — cover them elsewhere.
- **Depth is misnamed-feeling** — it's an early/late crossfade, *not* intensity. Many
  people miss the whole Early engine because of this.
- **★ AU pan-vs-Depth bug (Logic is AU-only!):** a **mono** track sent to a Room aux on
  the **AU build** makes **panning scale the reverb** (100% R ≈ dry, 100% L ≈ full wet).
  Fix: make **both the source track and the aux send stereo** (hard-center a mono source
  on a stereo track). `research/links/room-mono-au-cpu-gotchas.md`
- **Mono collapse:** sum **L+R** (never one channel — you lose echo density); if a mode
  goes metallic in mono, switch modes or micro-delay one output ~12 ms before summing —
  relevant before feeding a Room tail to a mono pedal / Octatrack input. `research/links/room-mono-au-cpu-gotchas.md`

## 11. Captured sources

**Transcripts (2)** — `research/transcripts/`: room-workhorse-parameter-walkthrough
(Depth/Early-Size/Late-Size interplay, the 3-4-knob philosophy) · room-late-section-crossover-decay
(the 3-band decay multipliers + crossovers, Diffusion, Late section).

**Links (12)** — `research/links/`: *settings facet* — room-official-modes-taxonomy (the
12 modes + the Bloom/Halls/Freeze correction) · room-controls-deep-dive (every control,
the dual engine, Space, Lo Cut) · room-early-tricks-gated-space (Depth-0% gating,
placement beds, Space drones) · room-vs-vintageverb (the contrast) · room-ambient-settings-recipes
(copyable recipes) · room-community-tips (KVR/Gearspace usage, plate weakness);
*technique/artists facet* — room-costello-early-and-depth-technique (mic-distance Depth,
Early Size table, High Mult <1 realism) · room-kvr-shared-presets (Andromeda/Oort Cloud/
Nerevar with normalized values, Diffusion-as-grit) · room-chaining-send-saturation-delay
(reverb→delay wall order, two-send, saturate before/after) · room-vs-vintageverb-which-i-reach-for
(lived "which do I grab" verdicts) · room-artists-sourced (Noisia/Knife Party HIGH +
flags) · room-mono-au-cpu-gotchas (the AU pan-vs-Depth bug + mono summing).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first
line of each = the original URL). Primary: the **Valhalla DSP blog (Sean Costello)** —
the authoritative mode/control reference — plus Splice, two YouTube control
walkthroughs, ProducerHive/VI-Control/KVR comparison & usage threads, Gearspace guitar
tips, Audiotent. **Honesty flags:** the **brief's "Bloom family / Halls / RandomSpace"
modes do not exist in ValhallaRoom** (Bloom = Shimmer; Halls = VintageVerb) — corrected
throughout and flagged, none invented. The two ambient *guitar* demo videos found
(Vincenzo Avallone; Ambient Djent clean guitar) have **no captions** (musical demos, not
tutorials) so only the two tutorial videos were transcribed. Gearspace 403'd on direct
fetch (distilled from search snippets, flagged). Copyable values in §5 are **synthesized
from official control ranges + the transcripts, not one verbatim factory patch.**
