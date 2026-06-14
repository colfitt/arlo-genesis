# EchoBoy Jr. — Usage Guide

EchoBoy Jr. is the **one-panel, fast version of EchoBoy**: the same core analog-echo
engine and the same warm "the repeat shouldn't sound like the input" character, with
**7 curated styles** and **everything visible at once** — no nested Tweak menus. It is
not a different-sounding plugin; it's a **speed/low-friction** tool. In this rig it's
the **quick tape/analog echo you stamp on a banjo/baritone/synth and move on**, while
the **full EchoBoy stays the deep mangler for drone/ambient walls** (its own guide:
`research/EchoBoy-UsageGuide.md` — defer there for all shared-engine detail: Style
Editor/Decay, Diffusion, Wobble, Prime Numbers, Rhythm/16-tap, the saturation-only
trick, EchoBoy→Valhalla, artist names). `research/links/echoboyjr-manual-v5.md`, `research/links/echoboyjr-tapeop-review.md`

## 1. What Jr INCLUDES vs what's CUT (the definitive delta)

**Included (the core EchoBoy engine on one page):** `research/links/echoboyjr-manual-v5.md`
- **Mix** (12 o'clock = 50/50), **Echo Time** (knob / type into LCD / browse arrows),
  **Feedback** (incl. runaway self-oscillation).
- **Timing modes** — **Time (ms, up to ~2.4 s)** and tempo-synced **Note / Dot / Trip**
  (1/2 down to 1/64), auto-syncing to host tempo. Same logic as full EchoBoy.
- **7 curated styles** (see §2) selected by Style knob or by clicking the name.
- **Stereo Mode** (3): **Normal / Wide / Ping Pong** — *yes, Jr has stereo + ping-pong*.
- **Glide** ON/OFF (tape-style pitch sweep when retiming, or clean retime).
- **Low Cut / High Cut** (2-band tone on the repeats).
- **Input / Output** (analog input-drive → dirt; affect the echo only, not dry; LED
  meters) + **Saturation** (tube/tape compression + subtle distortion on the delay).

**Cut vs full EchoBoy** (this is the "complex tweak" the manual says it stripped): `research/links/echoboyjr-manual-v5.md`, `research/links/echoboy-vs-echoboy-jr.md`
- The **Style Editor** — per-band EQ **Gain + Decay** = the **tape generation-loss
  engine** (each repeat darkens/evolves). Jr's repeats darken only as far as the
  fixed style models do.
- **Diffusion / Size / Loop-vs-Post** (the wash-into-reverb control).
- **Wobble** (wow/flutter), **Prime Numbers** (de-comb for clean clouds).
- **Feel / Accent / Groove / Warp** and the **Dual + Rhythm (16-tap)** modes.
- The **full 30-style bank** (Jr = 7). No standalone "saturation-only color" Style
  Editor moves — Jr's Saturation knob is the single coarse version.

## 2. The 7 styles (what to reach for) `research/transcripts/echoboyjr-deep-dive-guide.md`, `research/links/echoboyjr-manual-v5.md`

- **Studio Tape** — ATR-102 @ **15 IPS**. The neutral reference: mild tape comp, "not
  too dark, not too bright." (NB: full EchoBoy splits Master Tape @30ips / Studio Tape
  @15ips — Jr's single Studio Tape = the 15 ips one.)
- **Plex** — Echoplex EP-3. Brighter, thinner, more saturated, tail pitch-modulation;
  **repeats sit "in your face"** (use High Cut + Saturation to push back).
- **Space** — Roland RE-201 (real one is 4-head; **Jr gives one tap**). Dark, smooth,
  warm; modulated decay; **self-oscillates on high Feedback** — the dub/drone pick.
- **Cheap Tape** — worn consumer tape. Bright + very compressed; with Studio Tape the
  two "controlled," longer/thinner-decay styles.
- **Memory** — EHX Memory Man, bucket-brigade: repeats **darken as they decay** + are
  **chorused**, and **stay in the background** even when pushed → the style for leads
  that must keep the dry forward.
- **Ambient** — Distortion + Diffusion combined; "**reverb on the feedback loop**,"
  long and lush — Tape Op calls it a "**Daniel Lanois zone**." The atmosphere style.
- **Transmitter** — CB-radio: distorted, resonant, **mid-heavy** grit. Great on
  guitar/synth, weak on dull sources; the "recorded-wrong" character pick.

## 3. Essential workflow + signature settings (Jr-specific)

- **Stamp-a-color workflow:** pick the style for the vibe → set Echo Time (ms or
  Note/Dot/Trip) → a couple repeats of Feedback → blend with Mix. That's the whole
  point — minimal tweaking. `research/transcripts/echoboyjr-deep-dive-guide.md`
- **Tape slap (banjo/baritone)** — Studio Tape or Plex, Time mode ~100–200 ms, low
  Feedback (1–2 repeats), Wide mode for spread off a mono pickup. `research/links/echoboyjr-manual-v5.md`
- **Dub/drone throw** — Space, Note/Dot (dotted-8th), moderate-high Feedback, ride
  toward runaway for self-oscillation; Glide ON for the pitch-sweep "throw." `research/transcripts/echoboyjr-deep-dive-guide.md`
- **Lush atmosphere bed** — Ambient, long time, high Feedback, High Cut to darken =
  the closest Jr gets to a reverb-ish wash on a held drone/lead. `research/links/echoboyjr-tapeop-review.md`
- **Tame an aggressive repeat** — Plex too forward? High Cut up + **Saturation up**
  (smooths/compresses, cuts dynamics) + drive **Input**, drop **Output** → controlled
  darker tone. `research/transcripts/echoboyjr-deep-dive-guide.md`
- **Dirty vs clean** — push **Input** into yellow/red for dirty delays, keep low for
  clean (drives only the echo, dry untouched); LED yellow = 6 dB below clip, red =
  clipping. `research/links/echoboyjr-manual-v5.md`
- **Glide OFF** when dialing time with Feedback up (no pitch artifacts feeding back);
  **Glide ON** for deliberate tape-stop/pitch-jump moves. `research/transcripts/echoboyjr-deep-dive-guide.md`

## 4. Reach-for: Jr vs full EchoBoy

**Reach for Jr when:** `research/links/echoboyjr-tapeop-review.md`, `research/transcripts/echoboyjr-deep-dive-guide.md`
- You want **a flavor, fast** — "which analog echo," not "design a tape circuit."
  Tape Op's exact case: he prefers EchoBoy's sound but it was *slower to dial than a
  stock delay*; Jr = "best of both worlds," his "go-to for all jobs."
- A **quick coloring delay on a banjo/baritone/synth insert** where you don't need
  evolving tails.
- You want **less CPU / less screen clutter** at scale (many quick delays). Lighter is
  **inferred** from the stripped engine, not benchmarked. `research/links/echoboyjr-community-and-availability.md`

**Reach for full EchoBoy when (the drone/shoegaze default):** `research/links/echoboy-vs-echoboy-jr.md`, `research/EchoBoy-UsageGuide.md`
- You need **generation-loss** (Style-Editor Decay = each repeat darker), **Diffusion-
  in-Loop** wash, **Wobble** warble, **Prime Numbers** clean self-feeding clouds,
  **Rhythm/16-tap** evolving patterns, or **Dual/Ping-Pong with deep stereo control**.
- The **saturation-only color trick** (Time 0 / 100% wet / Style Editor decay+out
  sat) — that lives in full EchoBoy.
- For **sustained walls / evolving tape tails**, full EchoBoy → Valhalla. Jr can't
  mangle the tail; it stamps a fixed style.

## 5. Rig recipes

- **Into the degrade chain (Logic):** Jr early as the **fast tape/analog echo + tone**
  stage → push **Input** for crust → then SketchCassette/RC-20 motion or
  Decapitator → into Valhalla/EchoBoy for the wall. Jr is the "color the repeat" link,
  not the wall-maker. `research/transcripts/echoboyjr-deep-dive-guide.md`
- **Banjo-as-lead / baritone:** Memory style = repeats stay **behind** the lead (dry
  shines); Wide mode to spread a mono pickup; short Time slap for surf/post-rock.
  Plex when you *want* the repeat forward. `research/transcripts/echoboyjr-deep-dive-guide.md`
- **Synths/drones:** Transmitter for mid-gritty character; Space + high Feedback for
  self-oscillating drone beds; Ambient for the lush pad-ish wash. `research/transcripts/echoboyjr-deep-dive-guide.md`
- **Logic AU:** the installed `EchoBoyJr.component` (AU) is correct — Logic is AU-only,
  no VST needed. Insert at Mix to taste, or 100% wet on a send (manual's own
  guidance). Freeze if you stack many. `research/links/echoboyjr-manual-v5.md`
- **vs the hardware tape echoes:** like full EchoBoy, Jr is the **recallable in-the-box**
  echo. The **Big Time** (playable centerpiece) and **Generation Loss / Deco**
  (literal tape degradation) stay the hands-on/committed front-end. Use Jr when you
  want the tape vibe **fast and recallable** without patching hardware. (See
  `research/EchoBoy-UsageGuide.md` §5 for the full hardware-vs-software logic.)

## 6. Notable users & techniques

- **Honest:** no named artists are tied to **Jr specifically** — it's a utility-lite
  plugin and was a free giveaway, so credits don't track it. The full EchoBoy's
  documented users (Greg Wells, Manny Marroquin, Tchad Blake, etc.) and all genre
  technique live in `research/EchoBoy-UsageGuide.md` §4 — they apply to Jr's shared
  styles (e.g. the **Memory** = "Memory Man" sound Greg Wells loves). Tape Op's
  reviewer flag of the **Ambient = "Daniel Lanois zone"** is the closest on-aesthetic
  name-check. None invented. `research/links/echoboyjr-tapeop-review.md`

## 7. Pitfalls / gotchas (+ honest flags)

- **High Feedback boosts output level a lot** (manual warns) — protect monitors; Jr
  has **no "Limited" style** to catch runaway (that's a full-EchoBoy style), so use
  High Cut / lower Output. `research/links/echoboyjr-manual-v5.md`
- **Can't force full mono** — Normal still adds slight width; a stereo source in = a
  stereo (offset) delay out. `research/transcripts/echoboyjr-deep-dive-guide.md`
- **Saturation is a single coarse knob** and its effect is style-dependent — on some
  styles it's "fairly subtle"; this is not the full EchoBoy gain-staging chain.
- **No evolving/generation-loss tail** — for drone/ambient mangling, this is the
  reason to switch to full EchoBoy, not a Jr setting you're missing. `research/links/echoboy-vs-echoboy-jr.md`
- **CPU "lighter than full EchoBoy" = inferred, not benchmarked.** `research/links/echoboyjr-community-and-availability.md`
- **Thin ecosystem (honest):** dedicated Jr tutorials are sparse — most "EchoBoy"
  content covers the full version; the official intro/vocal videos are music-only
  (no narration). Best dedicated source is the deep-dive video + the manual + Tape Op.
  Gearspace direct fetch 403'd (triangulated). `research/links/echoboyjr-community-and-availability.md`, `research/transcripts/echoboyjr-deep-dive-guide.md`

## 8. Captured sources

**Transcript (1)** — `research/transcripts/`: echoboyjr-deep-dive-guide (chaptered
single-creator deep-dive; every style A/B'd, modes, Glide, input-drive, saturation).

**Links (3)** — `research/links/`: echoboyjr-manual-v5 (authoritative v5 manual —
control set + 7-style spec + design intent) · echoboyjr-tapeop-review (the "why reach
for Jr" workflow case; "Daniel Lanois zone" Ambient) · echoboyjr-community-and-
availability (Gearspace sentiment [403-triangulated] + Soundtoys-5-bundle packaging +
Dec-2025 free giveaway + CPU-inferred note).

**Also see** (in EchoBoy's set): `research/links/echoboy-vs-echoboy-jr.md` (feature
split) and `research/EchoBoy-UsageGuide.md` (all shared-engine detail, artists, the
EchoBoy→Valhalla and hardware-vs-software logic).

## Sources

All claims cite a captured file (first line = original URL). Primary: official
EchoBoy Jr. v5 manual, Tape Op (John Baccigaluppi), the "Deep Dive to ECHOBOY JR"
video, Soundtoys product/meet pages, Gearspace, rekkerd/offtheknob (2025 giveaway).
**Honesty flags:** Gearspace 403'd (triangulated from snippets, labeled in-file); no
Jr-specific artist credits (utility-lite/giveaway — full-EchoBoy users apply via
shared styles); "lighter CPU" inferred from the stripped engine, not benchmarked;
official intro/vocal videos are music-only and were not usable as transcripts.
