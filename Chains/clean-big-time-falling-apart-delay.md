---
type: chain
title: "Clean → Big Time Falling-Apart Delay"
date: 2026-06-15
artists: [William Basinski, Grouper]
instrument: guitar
gear:
  - Chase Bliss Clean
  - Chase Bliss Big Time
---

# Clean → Big Time Falling-Apart Delay

Two collapse engines in series. Clean's Sag (held BYPASS = max Sag on demand) makes notes sputter and fall out of the front of the attack; Big Time's `#!&%` misbias STATE makes every repeat crumble and detune harder as it decays. The result is mournful, decayed, lo-fi delay where the repeats fall apart over the tail — and where a Clean hold-bypass swell becomes a ghost repeat that the misbias slowly dissolves.

🟣 DOUG-designed integration. No artist played this exact two-pedal chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases. The "punch-in-clean-then-let-it-destroy" gesture is Basinski's native move (documented on Big Time's misbias STATE).

## Signal path

guitar → **CB Clean — "Tube Sag — Sputtering Overload"** (Sag zone, HOLD bypass for max-Sag swell) → **CB Big Time — "Falling-Apart Misbias Delay"** (MODE Long, STATE `#!&%`, VOICING Warm) → amp/interface

Mono in, mono out is fine here — this is a two-pedal texture box, not a stereo bed. The only "real artist signal-order" invoked is the general dynamics/sustain-shaping → delay standard (compression before delay), plus Basinski's misbias destroy gesture.

## Per-unit

- **CB Clean — "Tube Sag — Sputtering Overload"** — Dynamics in the final quarter of the sweep (the Sag zone, past 3:00) so the signal "falls out, falters, and sputters as you play harder" (manual). Sensitivity fairly high so digging in trips the sag; WET boosted to recover the level Sag eats. The performance move is **HOLD the BYPASS footswitch** to slam max Sag mid-phrase — a hands-on "fall apart" swell that becomes the seed for a ghost repeat downstream. Sag zone is published as "past 3:00 / last quarter"; the Sensitivity/Wet/Attack amounts are a dialable recipe, not published numbers — set them by ear and the LED. For a dirtier front end, swap to **CB Clean — "Dusty Pre-Dirt Sputter"** (DUSTY dip ON, Dynamics cranked into Sag, Sensitivity rolled back as the clip threshold) — the concept's "Dusty source" alternate.
- **CB Big Time — "Falling-Apart Misbias Delay"** — MODE **Long**, STATE **`#!&%` (misbias)**, VOICING **Warm**. The misbias STATE is playing-reactive (soft = mostly clean, dig in = fast dropout), so each repeat crumbles and detunes more as it loses level over the tail. Keep **FEEDBACK moderate (~45–55%, below COLOR)** so the line *dies out and falls apart* rather than climbing into a wall — this is the opposite gain structure to the doom-wall presets. **COLOR modest (~35%)**, **TILT EQ at/below noon** for the warm, mournful darkening, **TEXTURE mid** (misbias sensitivity — lower = repeats stay coherent longer before collapsing, higher = they fall apart fast). MOTION Sine subtle adds the tape-wow quiver. Dry retained (this is a delay on collapsing notes, not a wet-only loop — that's what separates it from "Nostalgic Repeater"). The values are a dialable recipe (Chase Bliss publishes character, not numbers; on recall flying faders override) — flagged in the patch.

## Routing

Straight series, mono → mono. **Gain-staging is the whole point:** Clean's Sag eats level, so its WET boost has to put a healthy signal into Big Time or the misbias won't have enough drive to react — but don't over-hot it, or the misbias dropout triggers on every note and the delay never sounds like a delay. Aim for the misbias to bite on the louder hits and on the BYPASS-hold swell, while quieter playing passes into mostly-coherent repeats that then decay into crumble. Keep Big Time's COLOR below FEEDBACK so repeats lose energy and fall apart down the tail instead of self-oscillating. If you want the wet to stay out of the printed dry, flip **DRY KILL ON** in Big Time's Options and run it as a parallel/aux — but in this two-pedal box the dry-retained series path is the intended sound.

## Sound

Notes that sputter and collapse on the attack, fed into a delay whose bias is dialed toward crumbling — mournful, decayed, lo-fi repeats that fall apart over the tail. Hold-bypass swells from Clean drift in as ghost repeats and slowly dissolve in the misbias. Two decay characters stacked: Clean takes the attack out from under the note, Big Time takes the repeats apart as they die.

**Taste-ref:** Basinski *Disintegration Loops* (tape literally falling apart on each pass) and Grouper-style fogged, decayed guitar — the "recorded-wrong," mournful lo-fi aesthetic at its most stripped.

## Play

Play sparse, deliberate held notes or slow two-note moves — let each one sputter on attack and then hear the repeats crumble down the tail. For the signature gesture, **HOLD Clean's BYPASS** as a note rings to slam max Sag and swell it back up; that swelled, level-shifted tone drops into Big Time and the misbias dissolves it into a ghost repeat. Dig in harder to trigger faster misbias dropout on the repeats; ease off to let them stay coherent a beat longer before they fall apart. Big Time's hold-MODE is the panic-reset back to a clean delay if it gets away from you.

## Sources

- **Basis:** designed integration; chains **CB Clean — "Tube Sag — Sputtering Overload"** (alt: **"Dusty Pre-Dirt Sputter"**) → **CB Big Time — "Falling-Apart Misbias Delay"**. Clean Sag "falls out, falters, sputters" + BYPASS-hold max-Sag gesture from the Clean manual (Dynamics/SAG pp.26–27, BYPASS p.11). Big Time `#!&%` misbias playing-reactivity ("play gently → stays clean; dig in → texture / dropout") and `#!&%` sag-and-return from `research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md`; low-COLOR/high-FEEDBACK = climbing wall (so FEEDBACK-below-COLOR = falling-apart decay) from manual pp.24–25 + `research/links/cb-big-time-factory-presets-recipes.md`.
- Patch refs: `Patches/Chase Bliss Clean/tube-sag-sputter.md`, `Patches/Chase Bliss Clean/dusty-pre-dirt-sputter.md`, `Patches/Chase Bliss Big Time/falling-apart-misbias-delay.md` (new).
- `Research/Taste-Profile/taste-profile.md` (Basinski/Grouper decayed lo-fi aesthetic)
