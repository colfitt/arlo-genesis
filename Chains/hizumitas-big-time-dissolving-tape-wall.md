---
type: chain
title: "Hizumitas → Big Time Dissolving Tape Wall"
date: 2026-06-15
artists: [William Basinski, Swans]
instrument: baritone guitar (single sustained chord)
gear:
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
  - Eventide H90
---

# Hizumitas → Big Time Dissolving Tape Wall ⭐

The headline Snyder degradation move. Hold ONE sustained chord on the baritone through the Hizumitas wall, then let Big Time's misbias limiter re-degrade each repeat until the fuzz literally eats itself — Disintegration-Loops-style crumbling stereo echoes — before the whole thing opens into a huge Blackhole hall. The making-of fantasy: *recording on dissolving tape in a failing deck.*

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases (William Basinski's *Disintegration Loops*, with Swans-weight underneath).

## Signal path

baritone (single sustained chord) → **EQD Hizumitas — "Doom Wall (max heavy)"** (mono) → **CB Big Time — "Dissolving Tape Wall"** (IN-L, auto-MISO mono→stereo) → **Eventide H90 — "Cavernous Blackhole Drone"** (Blackhole hall, body only) → tape.

The only "real-artist signal order" invoked is the general **fuzz-before-delay** standard (a documented pedal-order best-practice), not an artist-specific path. The degradation happens *inside* Big Time, after the wall is already built — that's the whole point.

## Per-unit

- **EQD Hizumitas — "Doom Wall (max heavy)"** — Volume max, Sustain max, **Tone fully CW** (max bass; mids scooped, highs tamed). The full-CW Tone is deliberate: the dark/scooped voicing keeps the wall *controllable* and gives Big Time a thick, low-mid-heavy source to chew on. Needs amp/monitor volume for the sustain bloom to arrive so the held chord never decays before Big Time grabs it.
- **CB Big Time — "Dissolving Tape Wall"** *(new patch)* — MODE **Long** (~12 s, ~24 s with 0.5X) so the delay time is longer than the bias-sag attack/recovery envelope — that's what lets the buffer "continue to eat itself alive." STATE **#!&% (misbias)**, dropping to **Saturated** if you want the destruction tamer. VOICING **Warm** (brick-wall ~10k roll-off, the "ripping itself in half" pairing Snyder calls out with misbias). **0.5X ON** (half sample rate + 12-bit reduction = the failing-tape crush; doubles the time too). **COLOR modest (~30–40%)** — lower COLOR explores the dynamic threshold where soft passages stay clean and digs-in crumble; too much COLOR + a hot fuzz clamps the limiter to porridge. FEEDBACK high (~70%) so repeats stack and re-degrade pass after pass. TEXTURE sets the misbias amount (the sag depth). WET ~45%, SPREAD widen.
- **Eventide H90 — "Cavernous Blackhole Drone"** — Blackhole on Preset A, **Mix pulled back (~30–40%)** so it's the doom *space*, not a second wall; Size 90+, Gravity right, Feedback long-but-not-frozen so the crumbling echoes keep moving through the hall instead of locking. Lo Level slightly down to keep the baritone bottom clear under the rumble.

## Routing

Mono fuzz wall → **Big Time IN-L auto-engages MISO** (mono-in / stereo-out) — the clean way to fan one mono fuzz into a stereo degradation field; stereo from Big Time onward into the H90. No clock needed (free-running drone, not rhythmic).

**Gain-staging is the whole game.** The Hizumitas already supplies all the saturation, so Big Time's job is *erosion*, not more dirt: keep COLOR modest and let the misbias limiter take its excursion out of the reproducible region and crawl back — that "sag-and-return" is the crumble. With a Long time and 0.5X engaged, you can even punch in a clean held section and come back later to find Big Time has destroyed it. The H90 only ever catches the wet field; pull its Mix back so the hall is doom space, not competition. Favor **DRY KILL ON** on the Big Time if you want a pure dissolving wet bed to print to tape with no clean note alongside it.

## Sound

A sustaining fuzz wall that slowly re-degrades through Big Time's misbias limiter into crumbling, asymmetrical stereo echoes — each repeat thinner, more broken, more "tape" than the last — then opens into a cavernous hall. The contents of the delay continuing to eat themselves alive.

**Taste-ref:** William Basinski *Disintegration Loops* (tape literally crumbling as it plays), with Swans crushing-sustained weight underneath. The rig's degradation thesis at its most literal.

## Play

1. Set the Hizumitas wall and let one baritone chord bloom to full sustain.
2. Let it feed Big Time and **dig in vs. play gently to ride the misbias threshold** — soft = grit without much loss, hard hits = fast dropout and crackle. The performance *is* the destruction.
3. Walk COLOR up slowly until the repeats just begin to crumble — no further (past that it clamps to porridge).
4. Let the crumbling field open into the Blackhole hall and print to tape.
5. Panic-reset Big Time (hold MODE) if the misbias runs away into a clean delay.

## Sources

- **Basis:** designed integration; chains **EQD Hizumitas "Doom Wall (max heavy)"** + new **CB Big Time "Dissolving Tape Wall"** + **H90 "Cavernous Blackhole Drone"**. The misbias self-eating behavior — sidechain shifts the limiter bias, "sag-and-return" reminiscent of disintegration-loop / failing-tape textures, "the contents of the delay continuing to eat themselves alive" at long times, misbias + Warm + TEXTURE "rips itself in half," lower COLOR to explore the dynamic threshold — is sourced verbatim from `Gear/Chase Bliss Big Time/research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md` (§ STATE/VOICING, lines 52–53, 69) and `mark-johnston-secret-weapons-big-time-deep-dive.md` (STATE/0.5X mechanics). 0.5X = half sample rate + 12-bit reduction (Snyder; Mark says 16-bit — treat exact bit depth as unverified). Fuzz-before-delay order + MISO auto-engage + COLOR-modest gain-staging from `research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A.
- `Research/Taste-Profile/taste-profile.md` (degradation / making-aesthetic thesis)
