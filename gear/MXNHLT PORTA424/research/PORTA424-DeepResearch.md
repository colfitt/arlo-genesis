# MXNHLT Effects PORTA424 — Deep Research

A working dossier for the **7th pedal on Board 3 (End / Time → Tape)**, the first half of the two-box cassette **print stage** that closes the entire rig. The PORTA424 sits right after the Eventide H90 and immediately before the JHS 424 — together they are the "summing to a 4-track cassette" terminus the Generation Loss dossier already named: the whole stereo bus, including every upstream tape voice (Deco, Generation Loss, Chroma Console), gets glued into one cohesive lo-fi bounce before it hits the Apollo/FOH. Where the JHS Colour Box V2 at the front of Board 1 is the **Neve console front-end**, the PORTA424 + JHS 424 pair at the back is the **cassette deck the console prints to**. Note up front: the rig-design.html tags this box "Stereo," but it is **mono in / mono out** — §5 addresses what that means for a stereo chain.

## 1. Lineage: the Tascam "Porta," the Mk.gee wave, and a one-man EE shop

The PORTA424 is the work of **Max Anhalt**, who runs **MXNHLT Effects** ("MXNHLT" = MaX aNHaLT) out of **Goleta, California**. Per [MXNHLT's About page](https://mxnhlteffects.com/pages/about), Anhalt built his first pedal in 2016, took a degree in Electrical Engineering, and began building seriously in 2022 — the company's stated mission is "bringing attention and updates to underrated pedals, creating new original circuits, and collaborating with players." This is a genuinely boutique, **made-to-order** operation (Reverb listings cite a ~2-week lead time), which is why §10 has to be honest about thin web coverage.

The pedal is part of a very specific 2024 phenomenon: the artist **Mk.gee** runs guitar straight into a **Tascam Portastudio** instead of a guitar amp, pushing the cassette deck's preamp into its "elastic, lo-fi" saturation, and his 2024 record sent guitarists scrambling to recreate it ([MusicRadar](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)). That triggered a small wave of Portastudio-channel-strip pedals — **JHS 424, Benson Portable Distortion 424, MXNHLT Porta 424, Neutrino Labs MX 424** — covered side-by-side in [Guitar Pedal X's "4 of a Kind"](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps).

The crucial lineage distinction — and the one that justifies owning *both* this and the JHS 424 — is **which Tascam each recreates**. The MXNHLT manual states the PORTA424 is "an almost exact recreation of a single channel from the **MK1** version" of a "classic 4 track cassette recorder" ([manual](https://mxnhlteffects.com/products/porta424-channel-strip)). MXNHLT's naming ("PORTA") and "MK1" point at the early budget **Porta-series Ministudio** lineage — the **Tascam Porta One** debuted in 1984 as the affordable, battery-capable entry point in the line ([muzines Dec 1984 review](https://www.muzines.co.uk/articles/tascam-porta-one-ministudio/4197); [Reverb Porta One page](https://reverb.com/p/tascam-porta-one-ministudio-4-track-cassette-recorder)). The **JHS 424**, by contrast, explicitly models the later, higher-spec **Tascam 424** Portastudio and even uses its actual op-amp chips. So the two boxes are not redundant: the PORTA424 is the *earlier, rawer, simpler* Porta channel; the JHS is the *later, hi-fi-er, more-controllable* 424 channel. (Tascam's own line history is tangled — Porta-series budget ministudios ran parallel to the pricier 244 → 424 → 424 MkII/III machines per [Reverb's Portastudio history](https://reverb.com/news/the-tascam-portastudio-through-the-ages) — and MXNHLT's marketing copy is loose about exact model numbers, so treat "Porta MK1 = early Porta-series ministudio" as the best-supported read, lightly flagged.)

**A "channel-strip recreation"** means MXNHLT didn't just clone the input gain stage; per the manual it reconstructs "**the entirety of the signal path** with meticulously reconstructed gain staging" — input trim → 2-band shelving EQ → channel fader → master volume — so you "dial in your settings exactly the same way as on the original," minus the cassette deck and the other three channels.

## 2. Controls (every control on the box)

Five controls, laid out to mirror a single Portastudio channel strip ([manual](https://mxnhlteffects.com/products/porta424-channel-strip); control count/labels corroborated by [Guitar Pedal X](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps)):

- **Input Trim (In).** The front-end gain stage — this is where the saturation lives. Low = clean DI; cranked = the preamp clips into "thick, trashy distortion." This is the single most important knob and the one you ride for clean-to-filth.
- **Treble (EQ Hi).** Shelving high-frequency cut/boost, matching the original deck's top-band shelf. Not a sweepable/parametric EQ — a fixed-corner shelf.
- **Bass (EQ Lo).** Shelving low-frequency cut/boost. Same fixed-shelf behavior on the bottom band.
- **Channel Fader.** A **slider control** (not a rotary knob) — MXNHLT's signature aesthetic touch, replicating the deck's channel fader. Sets the channel level *post-EQ, pre-master*, so the Trim/Fader interplay is the gain-staging game: drive the Trim hard, then use the fader to set how hot that distorted channel runs into the master.
- **Master Volume (Out).** Output level for the whole strip. Sets final level into whatever follows — here, the JHS 424 / Apollo.

The Trim ↔ Fader relationship is the heart of the pedal. Per a Reverb seller summary, "with the input trim cranked and the channel fader turned up it has a really great compressed feel and is super responsive to your pick attack, goes from clean to filth with just your attack." That is exactly the Mk.gee move: stage the gain so the preamp lives at the edge of breakup and let the picking hand do the rest.

**Build/pot note (manufacturing):** MXNHLT's product page notes current units ship with **B10k slide pots in place of A10k** due to parts stocking — electrically equivalent. The builder's full framing is positive: the B (linear) taper *"will increase volume faster, and actually allows finer control at the top"* — i.e. the usable sweet spot lives in the **upper third** of the fader's travel (not "feels more abrupt," as an earlier draft of this note implied). Worth knowing when you're chasing a specific fader position.

## 3. Sonic character

The PORTA424's voice is the **Tascam Porta channel strip**, not a generic "tape sim." Three layers, low to high:

- **Clean DI warmth.** With Trim low, it's a console-ish DI: gentle preamp warmth, light harmonic thickening, the subtle compression and "console-ish" glue of a cassette front-end. A Reverb buyer called it an "outstanding, nostalgic console-ish preamp" with "pleasing warmth whether clean or distorted." This is the always-on "print" mode — coloration, not destruction.
- **Tape saturation / preamp grit.** Push the Trim and the op-amp/preamp stage clips into the Porta's particular "special kind of grit" (manual's words). It's a *gooey, compressed, slightly-fizzy* saturation — the sound of a cassette preamp being overdriven, not a guitar distortion pedal. The cassette source the original optimized for matters: Type-I tape gives the rawer, lo-fi vibe (the Springsteen-*Nebraska* end), Type-II the warmer, cleaner end ([IK Multimedia Porta One notes](https://www.ikmultimedia.com/products/trtascamportaone/)). The PORTA424 leans toward the rawer/grittier side at higher Trim.
- **"Thick, trashy distortion."** At the extreme, Trim cranked + fader up, it's a full fuzzy/trashy lo-fi distortion — the manual's "front of your chain" use case.

**EQ curve:** two broad shelving bands, voiced to the original deck — not surgical. Use them to tilt the whole strip warmer (bass shelf up, treble shelf down) or brighter, not to notch frequencies. **Noise/hiss:** as a faithful Porta channel recreation, it carries some of the source's character noise floor, but being all-solid-state with no actual tape transport, **there is no wow, flutter, or mechanical tape artifact** — that is the key sonic line between this and the Generation Loss (see §5/§9). It is the *electronic* half of the Portastudio (preamp + EQ + saturation), not the *mechanical* half (wow/flutter/dropouts).

## 4. Behavioral notes

- **How hard it saturates:** Trim is the gate. Below ~9–10 o'clock it stays clean-with-warmth; from noon up it progressively clips; cranked it's full trashy distortion. Because it's a recreated *channel strip*, the saturation is gain-staging-dependent — a low Trim with a high fader sounds different from a high Trim with a low fader even at matched output, because you're moving where the clipping happens in the strip.
- **Compression / pick response:** the standout behavioral trait. Cranked Trim yields a "compressed feel… super responsive to pick attack" — soft picking stays nearly clean, hard picking blooms into grit. This dynamic, hand-controlled clean-to-dirty range is the Mk.gee technique and the reason this beats a static distortion for the role.
- **Headroom / 9V vs 18V:** the manual lists **9V DC (standard center-negative), up to 18V capable**. As with most op-amp dirt circuits, running **18V raises headroom** — cleaner, louder, tighter, with the clipping threshold pushed higher up the Trim sweep (more usable clean-warm range before breakup, and a firmer low end when it does break up). Run **9V** for the lower-headroom, earlier-breakup, more-compressed/"trashier" vintage character; run **18V** when you want it primarily as a clean console-warmth print stage with grit only at the top of the Trim. *(MXNHLT does not publish a specific 9V-vs-18V tonal breakdown; the above is standard op-amp-headroom behavior, lightly flagged.)*

## 5. Signal-chain placement — first of the final tape-print pair

This is the rig's terminus philosophy, and it's deliberate. The order on Board 3 is `… → Chroma Console → H90 → **PORTA424** → JHS 424 → Apollo/FOH`. The PORTA424 opens the **print stage**, and four things make that the right slot:

1. **Console-to-tape, bookended.** The JHS **Colour Box V2** at the front (Board 1) is the **Neve console mic-pre/EQ front-end** — where the signal is *recorded into* the console. The PORTA424 (+ JHS 424) at the back is the **cassette deck the console bus prints to**. The whole rig is, conceptually, "track through a console, bounce to a 4-track." Placing the Porta channel-strip *last* completes that metaphor: everything upstream is the performance and the effects; the Porta is the medium it lands on.

2. **Print *after* the time/space effects, not before.** Generation Loss degrades at the *head* of Board 3 (print-then-delay, so the delays/loops/reverbs inherit the wobble). The PORTA424 does the opposite job at the *tail*: it stamps a final, cohesive cassette character over the *already-reverberant, already-delayed* H90 output — gluing the H90's stereo tails, the Chroma morphs, and everything else into one lo-fi bounce. Saturating *after* the reverb is what makes a wall sound "recorded to one cassette track" rather than "a clean reverb with a fuzz in front."

3. **It's the gain-staging anchor into the interface.** As a recreated channel strip with input trim + master, it's the natural place to set final level/character into the Apollo — a literal "channel fader to the recorder."

4. **The mono implication — the one real wrinkle.** The PORTA424 is **mono in / mono out** (GearProfile + manual; the rig-design.html "Stereo" tag is incorrect for this box). Board 3 is **stereo** up to the H90's stereo output, so something has to give:
   - **Option A — run one channel (mono sum or one side).** Sum the H90's stereo to mono into the PORTA424, accept a mono print. For a drone/doom "ruined cassette" terminus this is arguably *authentic* — a Porta cassette track *is* mono, and collapsing to mono is part of the lo-fi bounce aesthetic. This is the simplest and most period-correct option.
   - **Option B — keep stereo, place the Porta only in one path.** Run the PORTA424 on one side (or on a parallel mono feed) and re-merge, but this creates an L/R imbalance unless matched carefully.
   - **Option C — two units / pseudo-stereo.** Truly preserving stereo through this stage would need a second PORTA424 (one per side) — overkill for the role.
   - **Recommendation for this rig:** **Option A — sum to mono here and print mono.** It matches the cassette-deck metaphor, keeps the JHS 424 (also a strong candidate to run mono) and the print stage coherent, and the stereo width has already done its work upstream (the H90, Dark Star, Microcosm). If wide stereo to FOH is a hard requirement, keep the Porta out of the main path and use it as a parallel/blend color instead.

## 6. Source-specific notes

The PORTA424 sees the **fully-processed stereo bus**, not a raw instrument — so its job is bus-printing, but the source still colors what arrives:

- **GK-5 banjo (EBM-5) via VG-800.** Banjo's bright, percussive transients arrive already smeared by the upstream chain; the Porta's bass shelf + preamp compression rounds the attack and the saturation thickens the body — exactly the "banjo recorded to a worn cassette" texture. Use the treble shelf to tame any residual top, Trim moderate so it warms rather than fuzzes the (often dense) signal.
- **Baritone Jazzmaster.** Low-end mass benefits from 18V headroom here so the bottom doesn't get flubby when the preamp clips; ride the bass shelf down slightly if the print muds up. The compression suits sustained baritone drones — they bloom into grit on harder attacks.
- **Modeled VG-800 signal.** The Porta de-perfects digital modeling beautifully: a sterile modeled cab IR printed through a cassette channel strip gains the analog "recorded-wrong" patina the whole rig is built around. Pad/synth COSM patches turn into convincing found-tape drones.
- **Bass (Jazz Bass).** As a DI-style channel strip, this is genuinely useful on bass — it's literally a 4-track channel, and Porta DIs are a known recording move. Keep Trim low for clean console warmth, or push it for a gritty lo-fi bass tone. Mind the mono collapse (a non-issue for bass).
- **As a mix/bus print.** Its native habitat. Trim low–moderate, EQ tilted to taste, fader/master set for unity-ish into the Apollo = a cohesive cassette glue over the entire stereo bus.

## 7. Famous users

**Honestly: none documented, and that's expected.** This is a one-man, made-to-order boutique pedal with no artist roster. The *machine* it recreates has the pedigree — the Tascam Porta/Portastudio line is on countless lo-fi and bedroom records, and the entire pedal category exists because of **Mk.gee's** Tascam-as-amp approach ([MusicRadar](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)) — but Mk.gee uses an actual Tascam, not this pedal. No verified famous PORTA424 user exists; do not claim one. (The honest "famous user" of the *sound* is the Tascam itself, on everything from Springsteen's *Nebraska* aesthetic to a generation of cassette-4-track demos.)

## 8. Live / power / I/O

- **Power:** **9V DC, standard center-negative, 2.1mm barrel; up to 18V capable** (manual). No published current-draw figure — for a simple op-amp channel strip, budget a conservative ~20–50 mA and give it an isolated slot; verify on a metered supply if your board is tight. *(Current draw unverified — not published by MXNHLT.)*
- **I/O:** **mono in / mono out**, 1/4" (manual + GearProfile). No XLR/balanced out (that's a JHS 424 feature, not this one), no stereo, no MIDI, no expression.
- **Bypass:** **true bypass, latching footswitch** (manual). True bypass means it drops cleanly out of the chain when off — but as a *print/terminus* pedal it's effectively always-on in this role, so bypass behavior matters mostly for A/B'ing the print in vs. out.
- **Enclosure:** **125B** — a compact, vertical box; small pedalboard footprint. The slide fader is the one ergonomic quirk (a fader, not a knob, to set with your hand or a careful foot).

## 9. Pairing recommendations (by name)

- **After the Eventide H90 (its immediate upstream):** the H90's stereo reverbs/delays/pitch land here and get printed. Sum to mono (§5) and let the Porta stamp cassette character over the wettest H90 algorithms — CrushedHall, BlackHole, and the like print *gorgeously* through a saturated channel strip. This is where ethereal H90 tails become "a cassette of an ethereal sound."
- **Into the JHS 424 (its immediate downstream — the key pairing):** these two are the print *pair*, and they stack rather than duplicate. The PORTA424 is the **earlier, rawer Porta channel** (saturation + shelving EQ); the JHS 424 is the **later, more-controllable 424 channel** with **two gain stages (Gain 1 + Gain 2)** and a **balanced XLR out + ground lift** for the Apollo/FOH handoff. Run order **PORTA424 → JHS 424** = "track to the Porta, then re-amp/print through the 424 to the desk." Practical division: let the PORTA424 set the *character* (warmth + grit), and use the JHS 424's twin gain stages + XLR as the *final level/interface* stage. Don't crank both into heavy distortion at once unless you want full collapse — pick one as the saturator and let the other glue/output.
- **vs. CB Generation Loss (Board 3 opener):** complementary, never redundant. Gen Loss is the *mechanical* tape voice (wow, flutter, dropouts, 12-model EQ library, stereo failure imaging) at the *head*; the PORTA424 is the *electronic* channel-strip (preamp + EQ + saturation, no wow/flutter) at the *tail*. The Gen Loss dossier's framing holds: **Gen Loss breaks the source; the Porta prints the whole thing to cassette.**
- **vs. Hologram Chroma Console (Board 3, mid):** Chroma is a multi-character morpher used *over the time effects*; the Porta is the *final printer*. No conflict — keep Chroma's tape character light if it's running, so the Porta does the terminal saturation.
- **vs. Strymon Deco V2 (Board 1, front):** Deco warms the *source* with all-analog tape saturation/doubletracking before any texture; the Porta saturates the *finished bus*. Front-warm vs. back-print — different ends of the same idea.
- **As a print stage to the Apollo:** Trim low–moderate, shelves to taste, master set for clean handoff = the cohesive lo-fi bounce into the interface. If you want the XLR/ground-lift convenience, let the JHS 424 be the literal last box before the Apollo and use the Porta purely for character.

## 10. Reviews & demos

**Coverage is thin** — this is a tiny made-to-order builder, so there is no Premier Guitar / Guitar Player review and no deep written deep-dive. What exists:

- **[MXNHLT product page](https://mxnhlteffects.com/products/porta424-channel-strip)** — the authoritative description and the on-site sound demos. Start here.
- **[Guitar Pedal X — "4 of a Kind: Tascam 424 Portastudio-style Preamps"](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps)** — the single most useful third-party piece: puts the PORTA424 head-to-head with the JHS 424, Benson, and Neutrino Labs, with controls and prices.
- **[Judge.me — PORTA424 reviews](https://judge.me/reviews/stores/mxnhlteffects.com/products/porta424-channel-strip)** — aggregated owner reviews (the store cites ~4.9/5 across ~58 reviews); praise centers on faithful gain-staging "touch" and console-ish warmth. *(Individual quotes couldn't be machine-extracted; treat the aggregate rating as builder-reported.)*
- **[Reverb listing](https://reverb.com/item/85978491-mxnhlt-porta-424-portastudio-cassette-saturation-distortion-pedal)** — useful seller description (the "clean to filth with your attack" line) and condition/lead-time notes.
- **[YouTube — Wesley Nilsen, "Little Bit More: tone test w/ MXNHLT Porta 424" (Sep 2024)](https://www.youtube.com/watch?v=Nnm7__6E4Uc)** — a real-world player tone-test (instrumental, no speech); a direct way to hear it. *(Channel = Wesley Nilsen, verified via yt-dlp.)*
- **[YouTube — saint zanus, "tascam 424 vs mxnhlt 424 vs jhs 424" (Aug 2025)](https://www.youtube.com/watch?v=dRE1oZ_Pzr0)** — the most rig-relevant demo: a 3-way audio shootout of a **real Tascam 424 vs the MXNHLT vs the JHS 424**, same source back-to-back (instrumental). The best way to hear the PORTA424-vs-JHS-424 difference this rig runs in series.
- **[MusicRadar — JHS 424 / Mk.gee context](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)** — essential for *why this category exists*, even though it's about the JHS.

For the *sound of the source machine*, the [IK Multimedia T-RackS Tascam Porta One](https://www.ikmultimedia.com/products/trtascamportaone/) plugin demos are a good proxy for the cassette-channel character MXNHLT is recreating.

## 11. Mods, quirks, known issues

- **B10k vs A10k fader taper** (manufacturing change, per the product page): current units use linear B10k slide pots; volume "increases faster" through the fader sweep than a log taper would. Not a defect — just a feel note when dialing the fader.
- **Mono only** in a stereo chain — the central practical quirk (see §5). Plan the stereo→mono collapse deliberately rather than discovering it on stage.
- **No published current draw / detailed specs** — boutique builder, minimal documentation. The "manual" is essentially the product-page copy; the on-site demos are the real reference. **Lean on the manual + demos; flag anything beyond it as inferred.**
- **Made-to-order lead time** (~2 weeks per Reverb) — not an off-the-shelf grab; relevant if a unit ever needs replacing before a tour.
- **No reported reliability problems** — but the sample size is small. Standard boutique hand-built construction.

## 12. Spec sheet

| Spec | Value |
|---|---|
| Builder | MXNHLT Effects (Max Anhalt), Goleta, CA |
| Type | Tascam Porta MK1 single-channel-strip recreation (preamp + EQ + saturation) |
| Source machine | Tascam Porta-series ministudio, "MK1" (early Porta One-lineage; see §1) |
| Controls | Input Trim, Treble shelf, Bass shelf, Channel Fader (slider), Master Volume |
| Power | 9V DC, center-negative, 2.1mm barrel; **up to 18V capable** |
| Current draw | Not published (est. ~20–50 mA, *unverified*) |
| Bypass | True bypass, latching footswitch |
| I/O | **Mono in / mono out**, 1/4" |
| Balanced out / XLR | None (that's the JHS 424, not this) |
| MIDI / expression | None |
| Signal path | All analog |
| Enclosure | 125B |
| Price | ~$170 USD (made to order, ~2-week lead) |
| Warranty | Builder-direct (not formally published) |

Sources: [MXNHLT product page/manual](https://mxnhlteffects.com/products/porta424-channel-strip), [Guitar Pedal X comparison](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps).

## 13. Starting-point settings

Knob positions are clock-face; the **Fader** is described low→high (bottom→top of its slot).

**(a) Subtle cassette warmth** — always-on print glue, clean console color
- Input Trim: 9 · Treble: 12 · Bass: 12–1 · Fader: ~70% · Master: to unity into the JHS 424
- Run **18V** for headroom. This is the default "print" — warmth and light compression, no obvious grit. The bus stays intact, just lands "on tape."

**(b) Saturated 4-track crunch** — the Mk.gee gain-stage, dynamic clean-to-filth
- Input Trim: 1–2 o'clock · Treble: 11 · Bass: 1 · Fader: ~85% · Master: down to compensate for the gain
- Ride your **picking hand** — soft = nearly clean, hard = blooms into gooey grit. The signature trick. 9V for earlier breakup.

**(c) EQ'd lo-fi print** — warm, dark, "old cassette" tilt over the whole bus
- Input Trim: 11 · Treble: 9–10 (shelved down) · Bass: 1–2 (shelved up) · Fader: ~75% · Master: unity
- Tames any upstream brightness (banjo, modeled top end) and prints a warm, rounded, Type-I-tape-ish bounce. Good under reverb-heavy H90 tails.

**(d) Degraded bus terminus** — thick, trashy, "ruined cassette" wall
- Input Trim: maxed · Treble: 1 · Bass: 12 · Fader: ~90% · Master: well down (loud)
- Mono-sum the bus into it (§5). Full trashy distortion as the final word — pair with a *light* JHS 424 just for level/XLR, or stack both for total collapse on a drone climax.

## 14. Versus alternatives — why it earns its slot (esp. vs the JHS 424)

The PORTA424 is one of four Portastudio-channel-strip pedals; the relevant question isn't "which one" but "why this *and* the JHS 424 it sits in front of."

- **JHS 424 ($249)** — the immediate downstream box and the only real "competitor" that's also already in the rig. It models the *later* **Tascam 424** (not the Porta MK1), uses the deck's actual **UPC4570 + NJM4565 op-amps** for "historically accurate" tone, has **two gain stages (Gain 1 / Gain 2)** for a wider range "from lo-fi flavours to zingy fuzzy tones," and crucially carries a **balanced XLR output with ground lift** for studio/FOH integration ([MusicRadar](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)). **Why both, in this order:** the PORTA424 is the *earlier, rawer, simpler Porta channel* that sets cassette **character**; the JHS 424 is the *later, more-flexible 424 channel* with the two-stage gain range and the **XLR/ground-lift interface** to actually print to the Apollo/FOH. Running PORTA424 → JHS 424 is "Porta channel → 424 channel → desk" — two different Tascam generations in series, character then output. They're complementary recreations of *different machines*, which is precisely why the rig keeps both.
- **Benson Portable Distortion 424 MkII ($188)** — 4-control take (Treble, Fader, Bass, Trim) with a Lo-Z impedance option; the most "amp-builder" voiced of the set. A fine standalone, but it doesn't add anything the PORTA424 + JHS 424 pair doesn't already cover, and lacks the JHS's interface features. Not needed here.
- **Neutrino Labs MX 424 ($141)** — the budget option, near-identical control layout (Master, In, Out, EQ Low, EQ High). Cheaper, similar concept; reach for it only if you wanted the Porta channel character on a budget and didn't already own the MXNHLT. Redundant in this rig.
- **CB Generation Loss / Hologram Chroma Console / Strymon Deco V2** — the rig's *other* tape voices, all already accounted for and all doing *different* jobs (mechanical degradation, multi-character morphing, front-end warming respectively — see §9). None of them is a channel-strip *preamp* with shelving EQ and a fader; none of them is a *print/DI* terminus. The PORTA424 is the only "console channel to cassette" box in the chain.

**In this rig specifically**, the PORTA424 earns its slot because it does the one thing nothing else does: it's the **electronic Porta channel strip** — warmth, shelving EQ, and dynamic preamp saturation — that **prints the whole reverberant stereo bus to (mono) cassette** right before the JHS 424 hands it to the Apollo. It's the back-half of the console-to-tape metaphor the Colour Box V2 opens, the first half of the two-box print stage the Generation Loss dossier already named, and the only box in the chain voiced as an actual 4-track channel rather than a tape *effect*.

## Sources

- [MXNHLT Effects — PORTA424 Channel Strip Distortion (product page / manual)](https://mxnhlteffects.com/products/porta424-channel-strip)
- [MXNHLT Effects — About (Max Anhalt / Goleta CA)](https://mxnhlteffects.com/pages/about)
- [Guitar Pedal X — 4 of a Kind: Tascam 424 Portastudio-style Preamps](https://www.guitarpedalx.com/news/gpx-blog/4-of-a-kind-tascam-424-portastudio-style-preamps)
- [MusicRadar — JHS 424 / Mk.gee Portastudio-in-a-pedal](https://www.musicradar.com/guitars/guitar-pedals/hes-not-using-a-guitar-amp-hes-using-a-tascam-424-jhs-pedals-puts-a-portastudio-in-a-pedal-to-help-you-recreate-mk-gees-elastic-lo-fi-tones)
- [Judge.me — MXNHLT PORTA424 reviews](https://judge.me/reviews/stores/mxnhlteffects.com/products/porta424-channel-strip)
- [Reverb — MXNHLT Porta 424 listing](https://reverb.com/item/85978491-mxnhlt-porta-424-portastudio-cassette-saturation-distortion-pedal)
- [RockBoard pedalPedia — MXNHLT Porta424](https://www.rockboard.de/en/pedalPedia/MXNHLT-Effects/Porta424-Channel-Strip/669982766/)
- [YouTube — "Little Bit More: tone test w/ MXNHLT Porta 424"](https://www.youtube.com/watch?v=Nnm7__6E4Uc)
- [Reverb News — The Tascam Portastudio Through the Ages](https://reverb.com/news/the-tascam-portastudio-through-the-ages)
- [muzines — Tascam Porta One Ministudio review (Dec 1984)](https://www.muzines.co.uk/articles/tascam-porta-one-ministudio/4197)
- [Reverb — Tascam Porta One Ministudio reference](https://reverb.com/p/tascam-porta-one-ministudio-4-track-cassette-recorder)
- [IK Multimedia — T-RackS Tascam Porta One (source-machine character reference)](https://www.ikmultimedia.com/products/trtascamportaone/)
- [Wikipedia — Portastudio](https://en.wikipedia.org/wiki/Portastudio)
