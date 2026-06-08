# Caroline Somersault — Usage Guide

How people *actually* use the Somersault, to complement the spec/reference dossier in `Somersault-DeepResearch.md`. In this rig it's the **last mono, unstable pitch-wobble** before the field goes stereo (after the BF-3, before the CE-2W + Deco). The whole pedal is governed by two ideas: **MIX sets what it is** (any dry+wet = chorus; full-wet = vibrato), and **OFFSET is the danger/seasick knob**. The honest calibration up front: it's a *pretty, largely pristine* chorus by default — the lo-fi is **opt-in** (hi-cut Tone + square wave), so lean on the downstream tape gear for real degradation and use this for *early, gestural pitch-warp*.

> Captured this wave (Tier B, 2 agents): 6 video transcripts + 8 distilled links = 14 sources (see §8). Dossier patched this wave: four §10 demo credits were missing/wrong channels — the NAMM interview is **The Pedal Zone** (not Caroline), plus Jackson Brooksby / The Pedal Zone / Zachari Smith — all verified via yt-dlp.

---

## 1. Essential workflows

**Start at noon.** Three independent sources (builder Herndon, The Pedal Zone, Zachari Smith) agree: **everything at 12 o'clock + triangle wave = a "divine/perfect" chorus** — tweak from there ([pedalzone-namm19-herndon](transcripts/pedalzone-namm19-herndon.md); [zachari-smith-spotlight](transcripts/zachari-smith-spotlight.md)).

**MIX is the chorus↔vibrato switch.** Any dry+wet blend = **chorus** (keeps a pitch reference); **full-wet = true pitch vibrato** (no anchor, so tonal material seesaws). The #1 gotcha: maxing MIX expecting "more chorus" gives you vibrato. Reviewer rule of thumb: "fully wet masks articulation, fully dry defeats the purpose."

**OFFSET is the danger/seasick knob (not Depth).** It sets the time difference between the modulated and dry lines; past ~2 o'clock it detunes fast into "pitch-bended slapback" / seasick. Yvette Young's on-camera scale: Offset low = "subtle warble," cranked = "like you're on a boat about to throw up" ([yvette-young-cme](transcripts/yvette-young-cme.md)). **Useful inverse tip:** Offset fully **CCW = fastest delay / least warp / least latency** — that's the tight 80s-chorus end (AndyDemos keeps it there even for vibrato, raising Mix/Depth instead).

**WAVE + TONE choose the lo-fi.** Triangle = musical default; **square = glitchy bleep-bloop** (near-self-oscillating synth tones at noon+bright; can even land an in-tune octave-down). **TONE is a toggle, not a sweep** — full-range or **hi-cut on the wet only** (darkens the modulated voice without dulling the dry = the worn-tape illusion). Square + hi-cut is where the "recorded-wrong" character lives.

**HAVOC is a gesture, not a setting.** Hold it → rate instantly slams to max (no ramp), snaps back on release → rotary speed-up / "vinyl skips and tape jumps." Unlike Caroline's dirt/delay HAVOCs it does **not** self-oscillate, so it's safe to use musically — rotary swells, or square+hi-cut glitch stutters at phrase-ends.

---

## 2. Signature settings

Boutique pedal — players share **by feel** ("noon," "fully CCW"), not clock charts. Attributed below; the only fully-numeric public settings (Guitar Chalk) are QC-flagged as likely SEO/AI content (it even mislabels Tone as a knob and cites the wrong current draw) — audition-only.

| Sound | Settings | Source |
|---|---|---|
| **Universal start** | everything **noon**, triangle | builder + 2 demos (quoted) |
| **80s / classic chorus** | Depth ~noon · **Offset fully CCW** (least warp) · dry+wet Mix · triangle · Tone bright | [andydemos-somersault](transcripts/andydemos-somersault.md) |
| **Vibrato / Leslie** | **Mix 100% wet**, then raise Offset *or* Depth (keep Offset CCW to reduce latency) | quoted, AndyDemos |
| **Seasick warble** | Offset low→cranked = subtle→"boat about to throw up"; triangle | quoted, Yvette Young |
| **Lo-fi tape-wow** | **hi-cut (dark) Tone** is the key; 100% wet = darkest "Bioshock" voice; Offset >~9:00 = audible | quoted, [jackson-brooksby-lofi-to-80s](transcripts/jackson-brooksby-lofi-to-80s.md) |
| **Square-wave glitch** | everything noon, **square + bright** = bleep-bloop / near-self-osc; square + higher Offset/Depth = rhythmic pitch blips | [zachari-smith-spotlight](transcripts/zachari-smith-spotlight.md) |
| **HAVOC** | momentary rate-to-max — a gesture over any base setting | all demos |

See dossier §13 for four fuller rig-tuned starting points (seasick chorus / deep vibrato / tape-wow / HAVOC glitch).

---

## 3. Power-user tips, tricks & hidden features

- **Offset CCW = least latency** — counterintuitive but the tightest, most usable end; reach for it whenever the chorus feels too smeared.
- **Square wave can be tuned** — at certain settings it produces an in-tune octave-down or rhythmic pitch pulses synced to the rate.
- **Hi-cut Tone is the "tape track" maker** — it darkens *only* the wet line, so a clean dry sits over a degraded modulated voice (the worn-cassette illusion). Binary, no halfway.
- **It's more pristine than its name** — two reviewers independently caution the Somersault is actually quite hi-fi; the lo-fi is mild and opt-in. Don't expect chewed-up tape from it alone — that's the downstream gear's job.
- **HAVOC won't run away** (unlike the Wave Cannon/Kilobyte versions) — it's purely a Speed override, safe to stomp mid-phrase.

---

## 4. Stacking recipes (this rig)

- **Unstable → stable (the textbook move):** put the pitch-unstable Somersault *upstream* of the stable CE-2W (modulation rule: character pedal first). A **mono** Somersault feeding the stereo split makes the widest, most "underwater" image the CE-2W alone can't. Pick one to be the character and the other the width — don't run both as deep chorus (mud) ([somersault-stacking-recipes](links/somersault-stacking-recipes.md)).
- **Into tape saturation (Deco V2):** saturate the wobble through the Deco's tape sim to compound into a "tape-ruined chorus wall" — the calibration line is "short of Generation Loss, you won't find a better lo-fi chorus."
- **Two-LFO beating:** set the Somersault's Speed slightly different from a downstream LFO (the Deco's wow/flutter) for an organic, non-mechanical waver.
- **Three-modulation honesty:** BF-3 → Somersault → CE-2W all full-up = a muddy mess; treat them as a palette (jet-flange / seasick pitch / width), rarely all three at once.
- **Redundancy with the End Board:** the rig already has heavier lo-fi/tape downstream (Generation Loss, Chroma, PORTA424/JHS 424). The Somersault's unique value is warping pitch *early* on Board 1, *before* the front-end chorus/saturation — something the End Board structurally can't do. If Generation Loss is running heavy, keep the Somersault subtle or it's inaudible.

---

## 5. Notable users & builder (honest)

- **Caroline Guitar Company / Philippe Herndon** — founded **2010, Columbia SC**; Herndon is a former touring guitarist + USC MBA who "failed to sell his soul to corporate devils." The "small batch distortery™" ethos, zine-style humorous manuals, signs every pedal, reportedly the **first pedal company to crowdfund** (Kickstarter, funded +234%/+268%). Design quote: "we didn't write any rules; we only wrote a manual." **HAVOC is a line-wide signature** footswitch (self-oscillation on the Wave Cannon/Kilobyte/Megabyte/Météore; a Speed override here) ([caroline-herndon-builder](links/caroline-herndon-builder.md); [havoc-signature-switch](links/havoc-signature-switch.md)).
- **Artist honesty:** **Yvette Young (Covet)** recorded the **Chicago Music Exchange demo (July 2019)** — a store/promo **demo placement, NOT a signature endorsement** or a Caroline artist deal. No other named artist could be verified using it as a core voice — coverage is genuinely thin ([yvette-young-association](links/yvette-young-association.md)).

---

## 6. Rig-specific recipes (banjo/baritone drone)

Slot: `… → BF-3 → Somersault → CE-2W (stereo split) → Deco V2 → …`

- **Baritone doom-vibrato (home turf):** Mix full-wet, Speed slow, Depth moderate, triangle — woozy Leslie wobble under sustained baritone drones. Watch Offset on low notes (too much = disorienting pitch seesaw against the fundamental).
- **Banjo:** favor **triangle** for musical waver and engage **hi-cut Tone** to tame the bright transients; square-wave on banjo gets choppy/percussive (good for rhythmic glitch, can be harsh). Full-wet vibrato on a banjo drone is a genuinely novel seasick texture.
- **"Worn cassette under the wall":** Mix ~1:00, Offset high, Depth high, Speed slow, triangle, **hi-cut** → into the Deco's saturation; pull Speed slower than the Deco's wobble so the two LFOs drift apart.
- **HAVOC into the Deco:** held HAVOC bursts read as glitchy tape-flutter once saturated; stutter at phrase-ends into the CE-2W/Deco split.
- **Bass (Jazz Bass):** keep **Mix toward dry** (chorus blend) so the dry low-end stays solid — full-wet vibrato loses the fundamental and sounds untuned.
- **VG-800 modeled/pad patches:** turn into lush drifting choruses; the lo-fi waver pairs well with the cleaner modeled tones, dirtying them up.

---

## 7. Best learning resources

- **AndyDemos** — [the most settings-explicit demo](transcripts/andydemos-somersault.md): chorus / vibrato / glitch / octave recipes, the Offset-CCW-for-latency tip.
- **Jackson Brooksby** — [best control map](transcripts/jackson-brooksby-lofi-to-80s.md): the hi-cut toggle + the Offset ~9:00 audibility threshold.
- **The Pedal Zone** — [Herndon NAMM '19 builder interview](transcripts/pedalzone-namm19-herndon.md) + [the "Faves" demo](transcripts/pedalzone-faves-demo.md) (HAVOC gesture; the pristine-not-gritty caveat).
- **Zachari Smith** — [honest review](transcripts/zachari-smith-spotlight.md) (noon default, square self-osc). **Chicago Music Exchange** — [the Yvette Young demo](transcripts/yvette-young-cme.md).
- **Text:** [Caroline product page](links/caroline-product-page.md), [Perfect Circuit power-user tips](links/somersault-poweruser-tips.md), [Delicious Audio stacking](links/somersault-stacking-recipes.md), the [builder bio](links/caroline-herndon-builder.md).

---

## 8. Common pitfalls / gotchas

- **Full-wet seesaws pitch** — that's vibrato, not chorus; it surprises people who max MIX expecting more chorus.
- **TONE is a toggle, not a sweep** — full-range or hi-cut, no halfway.
- **It's more hi-fi than "lo-fi" implies** — the degradation is opt-in (dark toggle + square); don't rely on it for heavy tape-ruin.
- **No tap, no expression jack** — Speed is hand-set; HAVOC is the only foot-controlled parameter.
- **Hybrid architecture** — the wet line is a digital chip; it's not a pure-analog BBD chorus despite the analog dry/LFO/mix.
- **9 V only, ~30 mA** — do not exceed 9 V (no 18 V trick); trivial draw otherwise.
- **Three modulations at once mud up** — use BF-3 / Somersault / CE-2W as a palette, not all full-up.

---

## 9. Captured sources

**Transcripts** (`research/transcripts/`):
- `pedalzone-namm19-herndon.md` — The Pedal Zone — Herndon NAMM '19 builder walkthrough (noon = perfect chorus).
- `yvette-young-cme.md` — Chicago Music Exchange (Yvette Young) — OFFSET = seasick/warble continuum.
- `andydemos-somersault.md` — AndyDemos — most settings-explicit (chorus/vibrato/glitch/octave + Offset-CCW latency tip).
- `jackson-brooksby-lofi-to-80s.md` — Jackson Brooksby — best control map; hi-cut toggle + Offset 9:00 threshold.
- `zachari-smith-spotlight.md` — Zachari Smith — honest review; noon default, square self-osc.
- `pedalzone-faves-demo.md` — The Pedal Zone — "Faves"; HAVOC gesture, pristine-not-gritty caveat.

**Links** (`research/links/`):
- `caroline-product-page.md` — Caroline — manufacturer named-sound vocabulary + control→sound mapping.
- `somersault-poweruser-tips.md` — Perfect Circuit — MIX/OFFSET/DEPTH/SPEED logic, WAVE/TONE, gotchas.
- `somersault-stacking-recipes.md` — Delicious Audio — unstable→stable, into-tape, two-LFO beating, redundancy honesty.
- `demo-derived-settings.md` — consolidated copyable recipes spoken in the demos (attributed).
- `guitarchalk-settings-suggestions.md` — 5 numeric recipes (QC-flagged, audition-only).
- `caroline-herndon-builder.md` — SCETV interview — builder bio + "distortery" ethos + crowdfunding.
- `havoc-signature-switch.md` — Caroline — HAVOC as line-wide signature; the Somersault's Speed-override version.
- `yvette-young-association.md` — Truth in Shredding — Yvette Young = CME demo (honest: not signature).

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Somersault-DeepResearch.md`](Somersault-DeepResearch.md); the manual is at [`manuals/SOMERSAULT.pdf`](../manuals/SOMERSAULT.pdf).

> **Honest coverage notes:** boutique pedal — coverage is thin and mostly verbal; no artist patch sheets exist (players share by feel, not clock charts), and the only fully-numeric public settings (Guitar Chalk) are unverified/likely-AI and flagged. Equipboard, Perfect Circuit, and The Gear Page were partly blocked (403/paywall), so artist-user verification is limited — **Yvette Young is a demo placement, not a signature user**, and no other named user could be confirmed. Two reviewers note the pedal is actually fairly pristine — its lo-fi is mild and opt-in.
