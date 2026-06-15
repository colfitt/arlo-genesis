---
type: chain
title: "Lost & Found ↔ MOOD Recorded-Wrong Cloud"
date: 2026-06-15
artists: [Grouper, Tim Hecker]
instrument: guitar
gear:
  - Chase Bliss Lost & Found
  - Chase Bliss MOOD MkII
  - Hologram Chroma Console
---

# Lost & Found ↔ MOOD Recorded-Wrong Cloud

A shoegaze Slow-verb wash that MOOD freezes and granulates, then prints through Gen-Lite-style tape imperfections — a self-evolving, degraded cloud that holds and decays on its own. Two stereo evolving boxes feed each other: Lost & Found's swirling reverb gets *baked into* MOOD's frozen grain, and the Chroma Console prints the character on the way out. No artist played this exact chain — it's a 🟣 DOUG-designed integration that chases the documented sounds of each box.

## Signal path

guitar → **CB Lost & Found — "Shoegaze Special"** (1A Slow-verb → 6A Ensemble Expander, `L>R` series, SPREAD on → stereo wash) → **CB MOOD MkII — "Stretching 101 + Frozen Grain Wall"** (Stretch looper, MODIFY→NOON = frozen grain, CLASSIC on for grit) → **Hologram Chroma Console — "CASSETTE Deterioration Touch"** (TEXTURE CASSETTE, light AMOUNT → tape wow/flutter print) → amp / interface, stereo throughout.

All three are stereo in / stereo out, so the wash is stereo the moment it leaves Lost & Found and stays in the field through MOOD's grain and the Chroma's print — no MISO mono-to-stereo trick needed here.

## Per-unit

- **CB Lost & Found — "Shoegaze Special":** the CB factory Combo, `L>R` series. **L slot = 1A Slow-verb**, **R slot = 6A Ensemble Expander** (native channels, no SWAP). MODIFY(L) ~1:00 (pre-diffusion feedback), TIME(L) ~1:00 (medium size), ALT(L diffusion) ~2:00–3:00 for the smeared bloom; Ensemble at ≈4 voices (MODIFY(R) ~11:00, TIME(R LFO) ~10:00) with BLEND ~1:00 toward the chorus, MIX(RAMP) ~1:00–2:00. **SPREAD on, TRAILS on.** Push MODIFY(L) higher and the hidden EQ CCW for more weight/darkness. This is the *source-aging-into-wash* stage — it does the reverb swirl so MOOD can just freeze and grain it. (Modes + routing are CB Field Guide verbatim; the exact MODIFY/TIME/ALT/BLEND clock positions are dialable starting points, not published numbers.)
- **CB MOOD MkII — "Stretching 101 + Frozen Grain Wall":** Looper MODE **Stretch**. Start MODIFY and LENGTH at MAX, then **slowly rotate MODIFY toward NOON** for "good ol' stretching," dropping LENGTH down for the grainy stretch. **NOON = FROZEN** — the current slice of the L&F wash repeats infinitely; LENGTH then sizes the held grain (high = clearer phrase, low = blurry/grainy). **CLOCK lower = grainier**; bake **CLASSIC on** for MkI-flavor grit. ROUTING **IN+micro-loop** so you can keep feeding fresh wash over the held cloud, MIX high enough that the frozen grain owns the bed. ⚠️ MODIFY at full MAX outputs no effect — keep it just below. This is the *freeze + granulate* stage; the frozen reverb is precisely the kind of pre-blurred fodder MOOD's Stretch wants.
- **Hologram Chroma Console — "CASSETTE Deterioration Touch":** TEXTURE **CASSETTE** — wow, flutter, slowing/speeding, and magnetic-tape degrade ("like running your sound through a Portastudio"). Start with a **little AMOUNT** for a subtle, believable deterioration that worsens as you climb. Leave the other three modules (CHARACTER / MOVEMENT / DIFFUSION) low or off so the Chroma reads as a *print*, not a second wall. Watch the lows — CASSETTE flubs bass-heavy material, so keep the L&F EQ from going too dark if the cloud gets boomy. This is the *final coloring / character print* stage.

## Routing

Straight stereo series, three boxes, no clock required — this is an evolving texture, not a rhythmic grid (MOOD can still take MIDI clock from a rig master if you ever want the grain length locked). **The whole game is one tape/degrade job per box so the cloud compounds without turning to porridge:**

1. **Lost & Found does the wash + light tape feel.** Slow-verb + Ensemble builds the swirling stereo reverb bed. It also already carries a touch of CB character, which is why the *only* heavy tape-degrade stage downstream is the Chroma's CASSETTE — not a stacked Generation Loss in front. (This honors the rig's "don't double the tape" rule: Gen Lite / Gen Loss stays out so CASSETTE is the single tape print.)
2. **MOOD freezes, doesn't re-saturate.** Stretch captures and grains the wash; the "degrade" it adds is grain + low-CLOCK aliasing + CLASSIC grit, not a second reverb. Because the source is already a blurred verb cloud, MOOD's frozen grain reads as a coherent held pad rather than mush.
3. **Chroma prints the character, lightly.** CASSETTE at a small AMOUNT is the last word — it ages the whole frozen cloud as one tape pass. If it gets muddy: pull Chroma AMOUNT down first, then back off the L&F EQ darkness, *then* check MOOD CLOCK isn't too low. The mud lives at the two texture stages (MOOD grain + Chroma tape), so trim there, not at the wash.

## Sound

A vast, seasick stereo reverb wash that gets caught mid-bloom and held as a grainy, infinitely-repeating cloud, then printed through wow-and-flutter tape so the whole thing breathes and warps as it sustains — a self-evolving, "recorded-wrong" pad that decays on its own without ever fully resolving. Glassy and infinite underneath, granular and tape-soft on top.

**Taste-ref:** Grouper's drowned-reverb intimacy / Tim Hecker's degraded ambient walls — a sustained wash that ages and falls apart in slow motion as it repeats.

## Play

1. Play sustained chords into the **Shoegaze Special** and let the Slow-verb + Ensemble swirl build a stereo wash.
2. With MOOD in **Stretch** (MODIFY + LENGTH starting near MAX), **slowly rotate MODIFY toward NOON** while the wash is blooming — catch a slice you like and **land MODIFY exactly at NOON to FREEZE** that grain into an infinite cloud.
3. Size the held grain with **LENGTH** (low = blurrier/grainier) and drop **CLOCK** for more grit; **CLASSIC** is baked on.
4. Keep playing over the frozen cloud (ROUTING **IN+micro-loop**) — fresh chords smear into the held bed.
5. Bring up the **Chroma CASSETTE AMOUNT** to taste — start subtle, climb for heavier wow/flutter as the cloud evolves.
6. To collapse: ease MOOD MODIFY back off NOON to let the grain progress/decay, then pull the L&F MIX down to dry out the wash.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Lost & Found — "Shoegaze Special"** (factory, reused) + **CB MOOD MkII — "Stretching 101 + Frozen Grain Wall"** (factory, reused) + **Hologram Chroma Console — "CASSETTE Deterioration Touch"** (community, reused). One-tape-job-per-box gain-staging (only CASSETTE prints tape; no Gen Loss in front) follows the rig's "don't double the tape" rule documented in the CASSETTE patch and the Lost & Found / Gen Lite sheets.
- Shoegaze Special modes + `L>R` routing are CB Field Guide "Combos" verbatim (`research/links/cb-manual-combos-official-recipes.md`); MODIFY/TIME/ALT/BLEND clock positions are DOUG's dialable starting points, not published.
- MOOD Stretch / MODIFY-at-NOON freeze / lower-CLOCK-grainier / CLASSIC grit from MOOD MkII manual pp.34–35 ("Stretch Mode / Stretching 101") and `research/links/mood-mkii-official-manual-try-this-recipes.md` (Recipe 6).
- Chroma CASSETTE = Portastudio wow/flutter/degrade and the "watch the lows / don't double the tape" caveats from `research/transcripts/molten-modular-chroma-console-review.md` (Robin Vincent / Molten Music).
- Note: knob clock-positions in the reused patches that aren't factory-published are dialable recipes (DOUG's interpretation), not sourced preset values.
