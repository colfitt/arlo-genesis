# MXNHLT PORTA424 — Usage Guide

How people *actually* use the PORTA424, to complement the spec/reference dossier in `PORTA424-DeepResearch.md`. It's the **first of the two-box cassette print stage** that closes the rig (PORTA424 → JHS 424 → Apollo): it sets the **character** (Tascam-Porta warmth + grit) while the JHS 424 does the final level/interface. The whole game is the **Trim ↔ Fader gain-staging** + riding **pick attack** for the Mk.gee dynamic clean-to-filth, and the one real decision is **committing the stereo bus to mono** at this stage.

> Captured this wave (Tier B, 2 agents): 2 video transcripts + 9 distilled links = 11 sources (see §8). **Coverage is genuinely thin** — a one-man made-to-order builder (Max Anhalt), no Premier Guitar review, the three real demos are all *instrumental tone-tests* with no spoken settings, and **no numeric knob patches exist anywhere**. Two light dossier touches this wave: added the best comparison demo (a real-Tascam-vs-MXNHLT-vs-JHS 3-way shootout) and corrected the truncated B10k-taper quote. Video attributions verified clean via yt-dlp.

---

## 1. Essential workflows

**Trim → Fader → Master is the whole game.** **Input Trim** = the front-end gain where the clipping lives; **Channel Fader** (the slider) = how hot that channel runs post-EQ; **Master** = final output. You can hit the **same loudness with very different grit** by trading Trim against Fader/Master — high Trim + low Fader = clipping at a controlled level; low Trim + high Fader = clean DI at the same volume. **Set the character with Trim first, then match print level with Master** ([staging-mono-print-tips](links/staging-mono-print-tips.md); [max-anhalt-mxnhlt-builder](links/max-anhalt-mxnhlt-builder.md)).

**The one documented signature recipe** (verbatim seller copy, repeated everywhere): *"input trim **cranked** and the channel fader turned **up**… super responsive to your pick attack, goes from **clean to filth with just your attack**."* The dynamics live in the picking hand — soft picking stays nearly clean, digging in blooms into gooey grit. This is the Mk.gee move ([reverb-listing-and-owner-reviews](links/reverb-listing-and-owner-reviews.md)).

**Two placements, two identities:** low Trim at the **end of chain** = clean DI / console-warmth print (this rig's role); high Trim at the **front of chain** = thick, trashy distortion as an amp-replacement saturator (a real player, K_YEON_J, runs it "right after guitar line in" for the Mk.gee tone) ([kyeon-j-dream-police-workflow](links/kyeon-j-dream-police-workflow.md)).

**The fader's sweet spot is the upper third.** The current B10k (linear) slide pots "increase volume faster, and actually allow finer control at the top" (builder's words) — so dial fine moves near the top of the slot.

---

## 2. Signature settings

**Honest state of the world: no numeric patches exist** in any source — only directional guidance. The dossier's §13 four settings are the orchestrator's own directional builds, not sourced patches. What's actually documented:

| Sound | Approach | Source |
|---|---|---|
| **Clean cassette-warmth print** (this rig's default) | **low Trim** at end of chain · EQ to taste · Master to unity into the JHS 424 · run **18V** for headroom | MXNHLT product page (directional) |
| **Saturated 4-track / Mk.gee** | **Trim cranked + Fader up**, ride pick attack (clean→filth); **9V** for earlier breakup | quoted seller copy |
| **Front-of-chain amp-replacement** | high Trim, right after the guitar in — trashy lo-fi distortion | K_YEON_J workflow |

**9V vs 18V:** the builder only states "9–18V for different levels of headroom"; one owner called it "a huge plus." The **18V = cleaner-print / 9V = earlier-breakup-trashier** read is standard op-amp behavior (inferred, flagged). Run 18V to keep baritone/bass low end firm when the preamp clips. See dossier §13 for four fuller directional starting points.

---

## 3. Power-user tips, tricks & hidden features

- **It's the *electronic* half of a Portastudio** — preamp + shelving EQ + saturation, with **no wow/flutter/dropouts** (that's the Generation Loss's mechanical job upstream). Use it for warmth and gain-staged grit, not tape-transport artifacts.
- **The EQ is two broad shelving bands** (the Porta One's were fixed Baxandall shelves at ~100 Hz / 10 kHz, ±10 dB) — tilt the whole strip warmer/brighter, don't expect surgical notching.
- **It de-perfects digital modeling beautifully** — a sterile VG-800 modeled cab printed through the cassette channel gains the "recorded-wrong" patina the whole rig is built around.
- **Genuinely useful as a bass/DI channel** — it's literally a 4-track channel; Trim low for clean console warmth, push it for gritty lo-fi bass (mono collapse is a non-issue for bass).

---

## 4. Placement & the mono question (terminus craft)

- **PORTA424 → JHS 424 = character then output** (the key pairing). They recreate **different Tascam machines** — the PORTA424 is the *earlier, rawer Porta channel* (the Porta One: fixed shelves, single speed, lo-fi), the JHS 424 is the *later, hi-fi-er 424 channel* (sweepable mid, double speed, the deck's actual op-amps) with a **balanced XLR + ground-lift** for the Apollo. So they stack rather than duplicate: **let the PORTA424 set warmth + grit, let the JHS 424 do final level + the interface handoff.** Don't crank both into heavy distortion unless you want full collapse ([porta-one-vs-424-lineage](links/porta-one-vs-424-lineage.md); [porta424-vs-jhs424-owner-compare](links/porta424-vs-jhs424-owner-compare.md)).
- **The mono question (the one real wrinkle).** The rig is stereo to the H90, but the PORTA424 is **mono in/out** — so the bus must collapse to mono here. The recommended call: **sum L+R and print mono** — period-correct (a real cassette channel *is* mono), and the stereo width has already done its work upstream (H90, Dark Star, Microcosm). No stereo workaround exists short of a second unit; if wide stereo to FOH is a hard requirement, keep the Porta as a parallel color out of the main path.
- **Print *after* the time/space effects:** saturating after the H90's reverbs/delays glues the wet tails into "a cassette of an ethereal sound" rather than "a clean reverb with a fuzz in front." The wettest H90 algorithms (CrushedHall, BlackHole) print gorgeously through it.
- **vs Generation Loss / Chroma / Deco:** complementary — Gen Loss = mechanical tape voice at the *head*; Chroma = mid-chain morpher; Deco = front-end source warmth; the PORTA424 is the only *channel-strip print* terminus. No overlap in job.

---

## 5. Notable users & builder/lineage (honest)

- **No famous PORTA424 user exists** — and that's expected for a one-man made-to-order boutique. The *machine* it recreates has the pedigree (the Tascam Porta line on countless lo-fi/bedroom records), and the whole pedal category exists because of **Mk.gee's** Tascam-as-amp approach — but **Mk.gee uses a real Tascam, not this pedal.** Don't claim a user.
- **Builder — Max Anhalt / MXNHLT Effects** (MaX aNHaLT), **Goleta, California** (a Guitar Pedal X article erroneously calls it a "Mexican brand" — that's wrong; ignore it). First pedal 2016 → EE degree → serious building from 2022; made-to-order; mission of "underrated pedals / original circuits / collaborating with players." His MO is to learn a vintage circuit deeply then improve it while preserving character — the fluency behind the PORTA424's "meticulously reconstructed gain staging" ([max-anhalt-mxnhlt-builder](links/max-anhalt-mxnhlt-builder.md)).
- **Owner verdict worth knowing:** one owner who A/B'd it against a **real Tascam 424 *and* the JHS 424 picked the MXNHLT as his favorite** of the three for "durability, sound, and ease of use" — a useful direct preference over the box it sits in front of ([porta424-vs-jhs424-owner-compare](links/porta424-vs-jhs424-owner-compare.md)).

---

## 6. Rig-specific recipes (print terminus, Board 3)

Order: `… → H90 → PORTA424 → JHS 424 → Apollo/FOH` — effectively always-on.

- **Subtle always-on print (default):** Trim ~9 · Treble noon · Bass noon–1 · Fader ~upper-third · Master to unity into the JHS 424; run **18V**. Warmth + light compression, no obvious grit — the bus stays intact, just lands "on tape."
- **Mono-sum the bus into it** (the load-bearing setup decision) — collapse the H90 stereo to mono here for a coherent cassette print.
- **EQ'd lo-fi print:** Treble shelved down ~9–10, Bass shelved up ~1–2 — tames residual banjo/modeled brightness and prints a warm, rounded, Type-I-tape-ish bounce under reverb-heavy H90 tails.
- **Degraded "ruined cassette" wall:** Trim maxed, Fader high, Master well down — full trashy distortion as the final word; pair with a *light* JHS 424 (just for level/XLR) so only one stage is destroying, or stack both for total collapse on a drone climax.
- **Banjo/baritone at the terminus:** the bass shelf + preamp compression rounds the attack and thickens the body (the "banjo recorded to a worn cassette" texture); 18V keeps baritone low end from flubbing when the preamp clips.

---

## 7. Best learning resources

- **saint zanus — "tascam 424 vs mxnhlt 424 vs jhs 424"** — [the most rig-relevant demo](transcripts/tascam-vs-mxnhlt-vs-jhs-424.md): a real Tascam vs the MXNHLT vs the JHS, same source back-to-back (instrumental — ear reference for the exact two boxes this rig runs in series).
- **Wesley Nilsen — "Little Bit More" tone test** — [a real-world player tone-test](transcripts/little-bit-more-tone-test.md) (instrumental).
- **Text:** [MXNHLT product page](links/mxnhlt-product-page.md) (authoritative controls/dual-use), [GPX "4 of a Kind" comparison](links/gpx-4-of-a-kind-preamps.md) (PORTA424 vs JHS/Benson/Neutrino), [the Porta-One-vs-424 lineage](links/porta-one-vs-424-lineage.md), the [builder bio](links/max-anhalt-mxnhlt-builder.md), and the [gain-staging/mono-print tips](links/staging-mono-print-tips.md).

---

## 8. Common pitfalls / gotchas

- **Mono only** in a stereo chain — the central wrinkle; plan the stereo→mono collapse deliberately, don't discover it on stage.
- **No numeric settings exist anywhere** — it's a make-to-order boutique with minimal docs; dial by ear (Trim for character, Master for level).
- **No XLR** (that's the JHS 424's feature) — let the JHS be the literal last box into the Apollo.
- **Made-to-order, ~2-week lead** — not an off-the-shelf grab; relevant if a unit needs replacing.
- **No published current draw** (~20–50 mA estimated, unverified) — meter it if your Board 3 supply is tight; it's 9–18V capable, center-negative.
- **Slider fader** (not a knob) — the sweet spot is the upper third; set it by hand or a careful foot.
- **Don't crank both Portastudio boxes** into heavy distortion at once unless you want full collapse — pick one as the saturator.

---

## 9. Captured sources

**Transcripts** (`research/transcripts/`):
- `tascam-vs-mxnhlt-vs-jhs-424.md` — saint zanus — 3-way audio shootout (real 424 vs MXNHLT vs JHS); the best comparison.
- `little-bit-more-tone-test.md` — Wesley Nilsen — 73-sec instrumental tone-test (ear reference).

**Links** (`research/links/`):
- `mxnhlt-product-page.md` — MXNHLT — authoritative controls, B10k "finer control at top," dual-use, no numbers.
- `max-anhalt-mxnhlt-builder.md` — MXNHLT About — builder bio, mission, the 6-pedal line, Goleta-not-Mexico correction.
- `porta-one-vs-424-lineage.md` — muzines (Dec 1984 Porta One review) — Porta One vs Tascam 424 spec-level lineage (why both).
- `porta424-vs-jhs424-owner-compare.md` — Judge.me — owner A/B verdicts + the why-both division of labor.
- `staging-mono-print-tips.md` — Reverb listing — Trim↔Fader discipline, signature recipe, 9V/18V, B10k taper, mono-print.
- `reverb-listing-and-owner-reviews.md` — Reverb — the "clean to filth with your attack" recipe + owner reviews.
- `gpx-4-of-a-kind-preamps.md` — Guitar Pedal X — 4-way Portastudio-preamp comparison (flags the "Mexico" error).
- `mkgee-portastudio-pedal-wave.md` — MusicRadar — the Mk.gee technique + the 4-pedal category context.
- `kyeon-j-dream-police-workflow.md` — K_YEON_J — front-of-chain Mk.gee amp-replacement workflow.

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`PORTA424-DeepResearch.md`](PORTA424-DeepResearch.md); the manual is at [`manuals/MXNHLT PORTA424.pdf`](../manuals/MXNHLT%20PORTA424.pdf).

> **Honest coverage notes:** genuinely thin — a one-man made-to-order builder with no Premier Guitar review, only instrumental demos (no spoken settings), and **no numeric knob patches in any source**. Reverb/Judge.me/Reverb-history blocked the fetcher (403/JS-rendered); owner quotes are from canonical seller copy + search snippets, and the ~4.9/5 rating is builder-reported. The 9V/18V tonal split and current draw are inferred/unpublished (flagged). "Porta MK1" is loose marketing — "early Porta-series ministudio (Porta One lineage)" is the best-supported read. No famous PORTA424 user exists; the fame is the Tascam's.
