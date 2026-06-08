# Boss BF-3 Flanger — Usage Guide

How people *actually* use the BF-3, to complement the spec/reference dossier in `BF-3-DeepResearch.md`. In this rig it's the **first modulation after the entire dirt stack** — so its real job is **mono Standard/Ultra flange on a sustained fuzz wall**, a louder, more violent task than the clean-guitar demos. Two things govern everything: **RES is the whole pedal** (subtle ↔ screaming jet), and a flanger is a comb filter, so a *continuous, harmonically dense wall* is the ideal source — the sweep becomes a dramatic "talking" movement across the whole spectrum.

> Captured this wave (Tier B, 2 agents): 4 video transcripts + 8 distilled links = 12 sources (see §8). No dossier mis-credits this wave (agents verified all channels via yt-dlp); the dossier's existing flags were confirmed correct — **"Momentum" is NOT an official Boss term** (it's "tap tempo via pedal" + a separate "Momentary mode"), and the **60 mA** draw is right (the circulating "40 mA" is wrong). Added one verified lineage note (the famous Boss-flanger record is the BF-2's "A Forest," not a BF-3).

---

## 1. Essential workflows

**RES is the entire pedal.** Every source agrees: low RES (~4–5/10) = subtle, chorus-ish movement; high RES (8–10) = metallic, vocal, screaming comb that approaches self-oscillation. **Slow RATE + high RES = a sustained screaming resonant peak** (the jet/laser swell); **fast RATE + high RES = chaos.** Maxed RES *plus* maxed MANUAL is the documented "other-worldly" extreme ([bf3-settings-cookbook-res-tips](links/bf3-settings-cookbook-res-tips.md); [guitarchalk-bf3-review-baseline](links/guitarchalk-bf3-review-baseline.md)).

**The four modes:** **Standard** (normal flange), **Ultra** (longer/more-present/scooped/aggressive — "a bit intrusive but totally usable"; the signature voice), **Gate/Pan** (in **mono** = a volume-slicer tremolo; in **stereo** = real L/R rotary), **Momentary** (flange only while the footswitch is held — EVH-style bursts; no tap in this mode).

**Flanging the fuzz wall (the rig's actual task).** After-distortion (the BF-3's slot) = "stronger, more metallic swooshing," cleaner; before-distortion = "wobblier, organic, thicker, chewier" but muddier (and in front of the MXR 108 Fuzz Face it gates/splatters). Keep it **after the dirt for predictability** — and watch level: high RES on a hot sustained input is **additive gain**, and users confirm an output spike in Gate/Pan + tap ([flanger-before-after-distortion](links/flanger-before-after-distortion.md); [bf3-modes-bass-input-digital-sheen](links/bf3-modes-bass-input-digital-sheen.md)).

**Tap-tempo:** hold the footswitch ≥2 s → the indicator blinks → tap the beat to sync the sweep (touching RATE returns control to the knob). Note: there is **no external footswitch/expression jack** — tap is on the pedal's own switch only.

---

## 2. Signature settings

Clock positions vary by source (Guitar Chalk uses a 1–10 scale where 5–6 ≈ noon; Messano speaks in clock positions). Attributed below.

| Sound | Settings | Source |
|---|---|---|
| **Classic jet-plane flange** (the rig's "swell on the wall") | Standard · MANUAL/DEPTH/RATE all **noon** · **RES 3–4 o'clock** | quoted, [messano-5-cool-ways-settings](links/messano-5-cool-ways-settings.md) |
| **Subtle / chorus-ish drift** | Standard · DEPTH ~10 · RATE ~1:00 · RES + MANUAL down to ~7 | quoted, Messano |
| **Laser / resonant comb** | Standard · MANUAL 7 · **RES 10** · RATE 3 · DEPTH 5 (maxed RES + slow RATE = screaming) | Guitar Chalk |
| **Ultra extreme** | Ultra · MANUAL 6 · RES 5 · RATE 9 · **DEPTH ~60–70%** ("too low loses shimmer, too high = chaos") | Guitar Chalk (inferred) |
| **Gate/slicer (mono) → rotary (stereo)** | Gate/Pan · MODE/RATE/DEPTH ~9 · MANUAL + RES ~6–7; same mode, mono vs stereo depends only on whether OUTPUT B is patched | quoted, Messano |
| **Baseline / out-of-box** | all knobs at **noon**, Standard | Guitar Chalk |

> **QC flag:** Guitar Chalk's *song-match* recipes ("Freak on a Leash" Gate/Pan, "Black Hole Sun" Ultra) are the author's approximations — **neither band used a BF-3 on those records**; keep the numbers as starting points, distrust the attributions. Messano's settings (spoken on camera while playing) are the trustworthy ones. See dossier §13 for four rig-tuned starting points.

---

## 3. Power-user tips, tricks & hidden features

- **MANUAL is dead when DEPTH is maxed** — people think the knob is broken; it isn't (max depth overrides the center-frequency setting). *(A manual/dossier fact — not surfaced in any demo.)*
- **Ultra is the doom setting** — hollow, metallic, scooped, borderline ring-mod at high RES; it sounds *broken*, not "classic rock." Both Boss and Guitar Chalk note Ultra pairs especially well with distortion/soloing — direct support for the rig's flange-after-dirt placement.
- **Gate/Pan mono ≠ stereo** — selecting Gate/Pan in this mono slot gives a volume-slicer, not the L/R Leslie spin. Not a fault; the rotary needs OUTPUT B patched into a stereo path (which doesn't happen until the CE-2W downstream).
- **Watch the level spike** — high RES / Gate/Pan + tap can saturate the output; trim what you feed into the Somersault/CE-2W.
- **Buffered bypass** (not true bypass) — irrelevant tone-suck under a fuzz wall, and the buffer arguably helps drive the mono run downstream.
- **Battery is "ultra greedy"** (60 mA digital draw) — run it off the isolated supply, never a battery.

---

## 4. Bass input (an under-used asset)

The BF-3 has a **dedicated BASS IN** jack (disabled when GUITAR IN is plugged — it's an either/or repatch). It's voiced to **retain low end** (a shorter delay-time range, 0.3–6.3 ms vs guitar's 0.3–14.4 ms) where a guitar-input flanger famously eats the bottom — "nice for slap." Honest caveat: it's **not universally preferred** — some bassists still run GUITAR IN. If the Jazz Bass ever runs through Board 1, try BASS IN specifically to keep the fundamental ([bf3-modes-bass-input-digital-sheen](links/bf3-modes-bass-input-digital-sheen.md)).

---

## 5. Lineage & notable users (honest)

- **BF-1 (1977) → BF-2 (1980–2001, analog BBD) → BF-3 (Feb 2002, digital DSP).** The BF-3 went **digital**, which is the central BF-2-loyalist debate: it gained Ultra, Gate/Pan, Momentary, tap-tempo, dual inputs, and stereo out, but loyalists call it "more metallic / cold-and-clear digital" vs the BF-2's "warmer, organic, liquid" analog sweep. **Moot in this rig** — you're flanging a fuzz wall, so the digital cleanliness is buried under saturation. (The **BF-2B** bass variant, 1987, is the conceptual ancestor of the BF-3's BASS IN.) ([bf2-vs-bf3-analog-digital](links/bf2-vs-bf3-analog-digital.md)).
- **"Momentum" is NOT an official Boss term** — Boss says "tap tempo adjustable via pedal" and lists "Momentary mode" as a separate thing; "Momentum" appears only in retailer/community shorthand. Use the two correct, distinct terms ([momentum-term-check](links/momentum-term-check.md)).
- **No iconic BF-3 record exists** — and that's the honest framing. The famous flanges belong to other pedals: MXR M117 (Van Halen "Unchained," McGeoch "Permafrost"), Phoenix kit (Heart "Barracuda"), EHX Electric Mistress (Andy Summers, Gilmour, Lifeson), Tycobrahe (Geezer Butler "E5150"). **The only Boss flanger with a famous record is the analog BF-2 — The Cure's "A Forest."** Sell the BF-3 on mode flexibility + front-of-chain placement, never a borrowed tone ([no-iconic-bf3-record-famous-flanges](links/no-iconic-bf3-record-famous-flanges.md)).

---

## 6. Rig-specific recipes (banjo/baritone drone)

Slot: `… Oxford → BF-3 → Somersault → CE-2W (stereo split) → Deco`.

- **Subtle drift on the wall:** Standard · RATE ~8 (slow) · DEPTH ~11 · RES ~9 · MANUAL ~11 — engage *once the dirt stack is already a sustained wall* so the flange breathes rather than announces itself.
- **Jet-flange swell:** Standard (or Ultra for more edge) · RATE 9–10 · DEPTH 2:00 · RES 1:00 · or tap-sync the sweep — watch output into the Somersault.
- **Ultra chaos ("recorded-wrong"):** Ultra · RATE 1–2:00 · DEPTH max · RES maxed (MANUAL irrelevant) — self-oscillating against the fuzz feedback; pair with the granular pedals downstream.
- **Baritone home turf:** the low fundamental + sustained fuzz gives the notches enormous content to sweep; Standard/Ultra, slow RATE, moderate DEPTH — but watch a deep notch briefly gutting the fundamental.
- **Banjo:** flanges well *once it's a Hizumitas-sustained wall*; a clean-ish banjo lead into the BF-3 sounds thin/metallic (the notches hit its 2–4 kHz spike) — use low RES + shallow DEPTH on exposed banjo, or only engage it inside the wall.
- **VG-800 pad patches:** a continuous synth pad is unlimited comb-filter material — slow Standard/Ultra = an evolving, rotor-like wash (one of the better drone tricks here).
- **Don't double-stack fast:** BF-3 slow/shallow → Somersault chorus = lush/seasick; BF-3 fast → Somersault = soup. Pick one as the lead motion. **Honest redundancy:** the H90 + Chroma can flange in stereo better — the BF-3's irreplaceable trick is flanging the *dirt at the source*, footswitchable, which the End Board can't do.

---

## 7. Best learning resources

- **Alex Messano** — [the best settings content](transcripts/messano-5-cool-ways.md): 5 distinct uses with spoken knob positions (the most copyable numbers), mono + stereo.
- **Sweetwater (Don Carr)** — [the cleanest mode-by-mode walkthrough](transcripts/sweetwater-don-carr-review.md) (all 4 modes, tap-tempo, both inputs).
- **Marcos Lelo Craveiro** — [isolated Ultra + Gate/Pan ear-reference](transcripts/craveiro-ultra-gatepan-samples.md) *(no captions — notes)*. **The Bass Channel** — [bass demo](transcripts/bass-channel-bf3-bass-demo.md).
- **Text:** [Guitar Chalk settings cookbook](links/bf3-settings-cookbook-res-tips.md) (RES-is-the-whole-pedal), [the flanger placement debate](links/flanger-before-after-distortion.md), [BF-2-vs-BF-3 lineage](links/bf2-vs-bf3-analog-digital.md), [Boss official spec/page](links/momentum-term-check.md).

---

## 8. Common pitfalls / gotchas

- **MANUAL is dead at max DEPTH** — not broken.
- **Gate/Pan rotary needs stereo** — in this mono slot it's only a volume slicer.
- **High RES = additive level spike** (esp. Gate/Pan + tap) — trim the downstream feed.
- **Buffered bypass** (not true bypass) — fine here, but it's not removable cleanly on a digital Boss.
- **60 mA, "ultra greedy" on battery** — isolated supply only (the "40 mA" figure circulating online is wrong).
- **No external footswitch / expression jack** — tap is the pedal's own switch only (the GearProfile already reads `expression: false`).
- **Digital sheen on *clean* tones** — the BF-2-loyalist complaint; inaudible under saturation, so irrelevant in this rig.

---

## 9. Captured sources

**Transcripts** (`research/transcripts/`):
- `messano-5-cool-ways.md` — Alex Messano — 5 settings with spoken knob positions (best for numbers).
- `sweetwater-don-carr-review.md` — Sweetwater — clean 4-mode + tap-tempo walkthrough.
- `craveiro-ultra-gatepan-samples.md` — Marcos Lelo Craveiro — isolated Ultra + Gate/Pan ear reference *(no captions)*.
- `bass-channel-bf3-bass-demo.md` — The Bass Channel — bass demo.

**Links** (`research/links/`):
- `messano-5-cool-ways-settings.md` — the 5 Messano recipes extracted as copyable settings.
- `bf3-settings-cookbook-res-tips.md` — Guitar Chalk cookbook — 6 recipes + RES-is-the-whole-pedal.
- `guitarchalk-bf3-review-baseline.md` — Guitar Chalk — "all knobs at noon" baseline + RES = comb sharpness.
- `flanger-before-after-distortion.md` — PedalPlayers — the placement debate (after = metallic; before = chewy/muddy).
- `bf2-vs-bf3-analog-digital.md` — MaxxMusic — BF-1/BF-2/BF-3 lineage + BBD→DSP transition.
- `momentum-term-check.md` — Boss official — "Momentum" is NOT official; correct terms = tap tempo + Momentary mode.
- `no-iconic-bf3-record-famous-flanges.md` — Stompbox Book — the flanger canon; only Boss = BF-2 (The Cure), no BF-3 record.
- `bf3-modes-bass-input-digital-sheen.md` — Audiofanzine — user takes on the 4 modes, bass input, digital-sheen complaint, the 40-vs-60 mA flag.

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`BF-3-DeepResearch.md`](BF-3-DeepResearch.md); the manual is at [`manuals/BF-3_M_eng03_W.pdf`](manuals/BF-3_M_eng03_W.pdf).

> **Honest coverage notes:** strong on clean-guitar demos + copyable settings, but the rig-critical **flange-on-a-fuzz-wall** task has only indirect support (Boss + Guitar Chalk endorse Ultra+distortion, but no demo flanges a sustained doom wall — an inherent gap). TalkBass, Reddit, and Rex-and-the-Bass were blocked/unreachable, so the bass-input low-end-retention detail leans on the dossier + aggregated reviews. Guitar Chalk's song-match attributions are unreliable (flagged); Messano's spoken settings are the trustworthy numeric source.
