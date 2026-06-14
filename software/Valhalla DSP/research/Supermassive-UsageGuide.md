# Valhalla Supermassive — Usage Guide

Supermassive is Valhalla's **FREE delay/reverb hybrid** — a stack of **feedback delay
networks (FDNs)** wrapped in 22 modes named after celestial objects. It is **not** a
"reverb with a delay button"; every mode is a different FDN topology, and the whole
plugin lives or dies on the interplay of **Feedback (decay), Warp (echo↔reverb smear),
Density (echo count/mix) and Delay (the longest delay line).** For this rig it does the
**two things the installed VintageVerb + Room can't**: a **genuine infinite/freeze drone**
(Feedback 100% = forever, with the EQ *outside* the feedback path so the held tail stays
full and bright) and **cascading delay-into-reverb washes** that drift on their own. It's
the free held-underbed + fake-shimmer wash maker under banjo/baritone/synths/drones.
★ **It's free — install it** (`valhalladsp.com`, no account, no feature limits; not on
disk yet per CONTENTS.md). `research/links/supermassive-blog-the-controls.md`,
`research/links/supermassive-blog-infinite-reverb.md`

## 1. Essential workflows

- **Pick the MODE first — it's the most powerful control.** Modes differ wildly in
  attack/sustain/decay/echo-density (a slow-swell thousand-second smear vs a tight
  spring). Choose by the *character of motion* you want, then refine with the 4 knobs. `research/links/supermassive-blog-the-controls.md`, `research/links/supermassive-blog-the-modes.md`
- **The four load-bearing knobs:** **Feedback** = decay length (→100% = infinite);
  **Warp** = how much discrete echoes smear into reverb (0% = clean repeats, 50%+ =
  reverberant); **Density** = perceived echo count / how isolated-vs-mixed the delays are
  (0% = discrete, 100% = smooth reverb); **Delay** = longest delay line (ms or tempo-sync). `research/links/supermassive-blog-the-controls.md`
- **100% wet on an aux send** (use **Mix Lock** so browsing presets keeps it full-wet),
  then EQ/saturate the *wet only* on the return — same send discipline as VintageVerb/Room. `research/links/supermassive-blog-the-controls.md`, `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`
- **High-pass the return** (or use the built-in **EQ Low Cut**) so a big wet wash doesn't
  turn the low end to fog. Both EQ filters sit **outside the feedback loop** → they shape
  output without darkening the tail over time. `research/links/supermassive-blog-the-controls.md`, `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`

## 2. The modes — character map (22, grew over updates) `research/links/supermassive-blog-the-modes.md`, `research/links/supermassive-version-history-modes.md`, `research/links/supermassive-studiobrootle-modes-breakdown.md`

**Original 8 (verbatim character from Valhalla's blog):**
- **Gemini** — most "conventional"; **very quick attack, natural exponential decay.** Low
  Density = pointillistic, high = smooth reverb. Clean infinite-hold mode.
- **Hydra** — fast attack, **very lush + long decay**, *extremely* Density-sensitive
  (0% = simple echoes → high = complex reverb). Clean infinite-hold mode.
- **Centaurus** — slow fade in/out; **attack tied to Feedback** (more feedback = faster
  attack), medium density → slow-swell pad.
- **Sagittarius** — **VERY long attack**, *"slow to get going, slow to go away,"* builds
  mass/inertia → swelling drone.
- **Great Annihilator** — slow attack + predelay, **super-long decay**, "more massive"
  than Centaurus. Clean infinite-hold mode.
- **Andromeda** — **very slow attack + predelay, decay into the THOUSANDS of seconds**,
  very high density. ★ the longest, most smeared drone-smear mode.
- **Lyra** — quick attack, long decay, **very low echo density** (lives in "echo" not
  "reverb"). Clean infinite-hold; tight spacey echoes.
- **Capricorn** — quick attack, long decay, **medium density** (bigger Lyra); spring-like
  at tight delays; "pointillistic reverbs + lush chorus."

**Added by later updates (grab the update for these):** Cassiopeia (feeding-back echoes,
dub), Cirrus Major/Minor (cloud washes), Large Magellanic Cloud (huge), Orion, Triangulum;
**v2.0** Aquarius/Pisces ("EchoVerb" — reverberant echoes, tempo-sync); **v2.5** Scorpio,
Libra (echoes that filter out over time, dub); **v3.0** **Leo** (*"long swelling and
dense — really good for background textures"* ★), Virgo (digital reverb + moving filters);
**v4.0** Pleiades (echoes filtering out as they feed back — MusicRadar's drone pick). `research/links/supermassive-version-history-modes.md`

**For this rig, the shortlist:**
- **Long-smear drones:** Andromeda · Great Annihilator · Sagittarius · Large Magellanic Cloud.
- **Background-texture swell:** Leo · Centaurus · Pleiades.
- **Clean infinite-hold (freeze):** Gemini · Hydra · Lyra · Capricorn · Great Annihilator.
- **Echo-forward / dub-rhythmic:** Cassiopeia · Libra · Aquarius · Pisces · Lyra.

## 3. Signature settings & recipes (copyable)

(Knob ranges + mode picks synthesized from the control/modes/infinite blog posts + the
tutorials — not one verbatim factory patch unless named.)

- **★ Infinite drone / freeze** — Gemini, Hydra, Great Annihilator, Lyra, *or* Capricorn ·
  **Feedback 100%** · **Warp non-zero** (so it's reverb, not a loop) · **Density non-zero**
  (smooth) · **Mod Depth 0%** (holds pitch) · Mix 100% (send). Play the note in, it holds
  forever. To *freeze a moment*: ride Feedback to 100% once the tail you want is in. ★ this
  is the move VintageVerb/Room can't do. `research/links/supermassive-blog-infinite-reverb.md`
- **Long-smear ambient wall** — Andromeda · Feedback ~80–95% · Warp ~40–60% (reverberant) ·
  Density high · Delay 300–800 ms (or 1/2-note sync) · slow Mod (Rate low, Depth low-med) ·
  EQ High Cut ~3–4 kHz · EQ Low Cut ~150 Hz · Mix 100%.
- **Slow-swell pad / background texture** — Centaurus or **Leo** · Feedback 60–85% (in
  Centaurus this also speeds the attack) · Warp ~50% · Density med-high · Delay med · Mix to taste.
- **Pleiades drone-from-a-pad** (MusicRadar) — load a pad/string, **insert** Supermassive ·
  Pleiades · **Warp ~50%** · Feedback up to extend decay · Density to set smear · Mix to taste. `research/links/supermassive-musicradar-textures-beds-drones.md`
- **Fake-shimmer wash (the free "shimmer")** — start from the factory **"Swelling Synth
  Verb"** preset and **dial it back** until musical (it's intense at default); it's a
  *late-reverb* shimmer, not a pitch-shift. Add a phaser/chorus or a pitch-shifter AFTER
  Supermassive if you want literal rising harmonics. `research/transcripts/supermassive-omynel-free-shimmer-on-guitar.md`, `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`
- **Dream-pop / shoegaze guitar** — **shorter Delay + moderate Feedback + a smidge of Mod
  Depth + wide Width** = sparkle without cartoon-shimmer artifacts. `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`
- **Dub / rhythmic feedback echo** — Cassiopeia or Libra · **Delay Sync to notes** ·
  Feedback 60–85% · Warp low (keep repeats discrete) · Density low-med · ride Feedback live. `research/links/supermassive-studiobrootle-modes-breakdown.md`
- **Harmonic descending tails** — any mode · **Warp 5–15%** → resonances shift *downward*
  as the sound decays (subtle pitched drift without a pitch shifter). `research/links/supermassive-blog-the-controls.md`

## 4. Power-user tips, tricks & hidden features

- **Why infinite stays full:** modes use modulation with **no filtering in the feedback
  path**, and the **EQ Low/High Cut sit OUTSIDE the loop** → a held infinite tail doesn't
  lose highs over time (unlike most reverbs). This is the design reason it's a better
  freeze than faking it in VintageVerb. `research/links/supermassive-blog-infinite-reverb.md`
- **Mod Depth = 0 on a freeze** to preserve pitch; **add motion downstream** (a phaser
  after Supermassive) instead of using internal mod that would detune the held tail. `research/links/supermassive-blog-infinite-reverb.md`
- **Ride Warp + Delay LIVE** for evolving texture — *"adjusting Warp and Delay in real
  time introduces temporary pitch changes"* → drone risers, tape-warble bends, performed
  swells. Automate small per-section moves so the wash "feels alive." `research/links/supermassive-musicradar-textures-beds-drones.md`, `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`
- **Warp is the echo↔reverb dial:** 0% = clean discrete echoes; 5–15% = downward-shifting
  harmonic delays; 20–50% = smeared clusters going reverberant; >50% = full reverb. `research/links/supermassive-blog-the-controls.md`
- **Density isolates vs mixes the delays** AND raises L/R crossfeed — turn it down for
  discrete pings, up for a smooth wall; 0% Mod Depth makes Warp artifacts more audible. `research/links/supermassive-blog-the-controls.md`
- **Negative Width swaps L/R** (and 0% = mono) — useful for collapse-safety before a mono
  pedal/Octatrack input, or for a hard stereo flip on a doubled send. `research/links/supermassive-blog-the-controls.md`
- **Keep two presets** — a lush/intense solo version and a dialed-back mix version; the
  big shimmer wall is "a little intense in a full mix." `research/transcripts/supermassive-omynel-free-shimmer-on-guitar.md`
- **Delay Sync** (notes/dotted/triplets) turns it into a tempo-locked dub/ambient delay,
  not just a wash. `research/links/supermassive-blog-the-controls.md`

## 5. Rig-specific recipes (your gear by name)

- **The free held-underbed under VintageVerb/Room:** division of labor — **VintageVerb =
  characterful vintage space, Room = believable depth/lush dark wall, Supermassive = the
  genuine infinite/freeze underbed + cascading feedback drift** they can't do. Stack: a
  short Room/VVV send for body + a Supermassive send (infinite mode, Feedback 100%) for the
  held drone. `research/links/vintageverb-vs-supermassive-free.md`, `research/links/supermassive-blog-infinite-reverb.md`
- **On banjo / baritone (the fade-in fix):** a slow-swell Supermassive patch fades in
  unpleasantly on sharp attacks fed a *dry* signal → **put a short delay + reverb BEFORE
  Supermassive** so the source is already sustained going in (the swell has something to
  grab). Maps onto banjo → short slap/verb → Supermassive wall. `research/transcripts/supermassive-omynel-free-shimmer-on-guitar.md`
- **Into / after the degrade chain:** for a *clean* infinite bed, run **Supermassive
  early/clean, then saturate the return** (Decapitator / SketchCassette / RC-20, Low Cut
  first) → the saturated doom/shoegaze wall. For "baked-in" grime, degrade *before* the
  send so the held tail inherits the artifacts. Pairs with the Tycho-style **delay AFTER
  the reverb** move using EchoBoy. `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`, `research/links/vintageverb-vs-supermassive-free.md`
- **On synths/drones:** synth send, Mix 100%, bump Feedback + Density, slow the Delay,
  gentle Mod, **hold one note = instant evolving ambient bed.** Andromeda/Leo for the
  smear; ride Warp for evolution. `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`, `research/links/supermassive-musicradar-textures-beds-drones.md`
- **Send vs insert:** **send** (100% wet, Mix Lock) for a shared ambient wall under
  several instruments; **insert** for a dedicated spot effect on one sustained sound
  (MusicRadar's pad/drone-from-a-string). `research/links/supermassive-musicradar-textures-beds-drones.md`
- **Logic Pro (AU-only host):** Supermassive ships AU — drops straight on a Logic aux/bus.
  As with Room, if a **mono** source feeds a stereo aux watch pan-vs-wet scaling — keep the
  source track + send **stereo** (hard-center a mono banjo on a stereo track). Ableton Live
  12 Lite: fine as an insert/return; Lite's lower track/return count is the only limit. `research/links/supermassive-blog-the-controls.md`

## 6. Notable users & techniques (sourced, flagged honestly)

- **No specific named ambient/post-rock artist credit surfaced** for Supermassive — the
  "every serious free-reverb thread tops out here" reputation is real but word-of-mouth
  (same situation as VintageVerb/Room's ambient rep). None invented. The strongest sourced
  *use*-cases are the tutorial workflows above (Omynel clean-guitar shimmer; MusicRadar
  pad/drone). `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`
- **Documented technique, not artist:** "hold one note to become an ambient artist" (synth
  send, Feedback/Density up, slow Delay) — the canonical instant-ambient move. `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`

## 7. Common pitfalls / gotchas

- **Feedback runaway / self-oscillation:** Feedback >100% (or 100% + some modes) can build
  past unity and clip/runaway — **keep a limiter on the return**, ride Feedback, and don't
  stack two infinite Supermassives into each other unguarded. `research/links/supermassive-blog-infinite-reverb.md`
- **Unpleasant fade-in** on sharp attacks with slow-swell modes fed a dry signal — front
  it with a touch of delay/reverb (see §5). `research/transcripts/supermassive-omynel-free-shimmer-on-guitar.md`
- **Low-end fog:** big wet washes mud out fast — High Cut/Low Cut the wet (or HPF the
  return); the EQ being outside the loop means you can carve hard without killing the tail. `research/links/supermassive-blog-the-controls.md`
- **Mod on a freeze detunes it** — set Mod Depth 0 for held drones; add motion after. `research/links/supermassive-blog-infinite-reverb.md`
- **It's not a real shimmer** (no pitch shifter) — the "shimmer" is a dense late-reverb
  wash; for literal rising-octave shimmer use paid Shimmer / the H90 / a pitch plugin after. `research/transcripts/supermassive-omynel-free-shimmer-on-guitar.md`, `research/links/supermassive-pluginreport-ambient-shoegaze-recipes.md`
- **Old version = missing modes** — modes were added free over updates (Leo, Pleiades,
  Scorpio, Libra, etc.); update to get all 22. `research/links/supermassive-version-history-modes.md`
- **CPU:** heavier than VintageVerb/Room (it's a big FDN with modulation) but still light
  on Apple Silicon; the cost is per-instance — prefer one shared send over many inserts for
  walls.

## 8. Captured sources

**Transcript (1)** — `research/transcripts/`: supermassive-omynel-free-shimmer-on-guitar
(real clean-guitar shimmer workflow: "Swelling Synth Verb" dialed back, the front-end
delay/reverb fade-in fix, keep-two-presets).

**Links (7 new + 1 reused)** — `research/links/`: *authoritative Valhalla blog* —
supermassive-blog-the-controls (every knob, Warp ranges, EQ-outside-loop) ·
supermassive-blog-the-modes (original 8 with attack/decay/density) ·
supermassive-blog-infinite-reverb (the Feedback-100 freeze recipe + why it stays full);
*modes/version* — supermassive-version-history-modes (22 modes, which update added which) ·
supermassive-studiobrootle-modes-breakdown (per-mode character + dub modes); *recipes* —
supermassive-musicradar-textures-beds-drones (Pleiades pad/drone, ride-Warp-live) ·
supermassive-pluginreport-ambient-shoegaze-recipes (ambient pad + shoegaze guitar +
HPF-return, 403'd→triangulated); *context* — vintageverb-vs-supermassive-free (division of
labor, reused from the VintageVerb wave).

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first
line of each = the original URL). Primary: the **Valhalla DSP blog (Sean Costello)** — the
authoritative control/mode/infinite reference — plus MusicRadar (Jon Musgrave), Studio
Brootle, The Plugin Report, MusicTech/Audio Plugin Guy (version history), and the Omynel
guitar-workflow video. **Honesty flags:** Plugin Report 403'd on direct fetch (distilled
from search snippets, labeled in-file); the Omynel video gives technique not numeric
values (auto-subs, deduped); the per-version mode-add list is triangulated (original 8 are
blog-confirmed; update modes from the individual update posts + the v2.0 roster of 16);
copyable knob values in §3 are synthesized from official control ranges, not one verbatim
factory patch (except the named "Swelling Synth Verb" preset and the Pleiades/MusicRadar
steps); **no specific ambient artist credit is sourced** — reputation flagged as
word-of-mouth, none invented. **Confirm free-vs-paid + on-disk status** against CONTENTS.md
(Supermassive is NOT installed yet per the scan — grab it from valhalladsp.com, free).
