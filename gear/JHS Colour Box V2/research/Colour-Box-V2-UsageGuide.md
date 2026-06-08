# JHS Colour Box V2 — Usage Guide

How people *actually* use the Colour Box V2, to complement the spec/reference dossier in `Colour-Box-V2-DeepResearch.md`. This isn't a drive — it's a **Neve-1073-style preamp/EQ/DI** that lives 4th on Board 1 "always-on when able," pre-shaping everything the fuzz wall chews on. The two highest-leverage moves: roll the **HI-PASS up to ~100–200 Hz *before* the fuzzes** to tighten the wall, and master the **STEP → PRE-VOL → MASTER** gain-staging so you can go clean-console → broken-console without volume jumps. It also doubles as a real DI / console-print stage into the Apollo.

> Captured this wave (Tier B, 2 agents): 6 video transcripts + 12 distilled links = 18 sources (see §8). Dossier patched this wave: corrected EQ/HPF spec to **JHS-official figures** (±15/±10 dB, HPF 12 dB/oct 160–650 Hz — not the older ±17 dB / 6 dB/oct), added **verified artists** (Mac DeMarco named the V1; Black Pumas run the V2 on camera), and fixed two video mis-credits (`GK-nmmcGOrQ`=Jorb, `fnkU8aMF2Tg`=The Bass Channel) — all verified via yt-dlp.

---

## 1. Essential workflows

**Gain-staging: STEP → PRE-VOL → MASTER.** **STEP** = coarse gain (5 stepped values, +18…+39 dB); **PRE-VOL** = the drive between the two gain stages ("warmth → saturation → fuzz"); **MASTER** = output trim. Push grit on PRE-VOL/STEP, then pull MASTER back to unity — *every gain change jumps loud otherwise*. For clean: MASTER high, PRE-VOL low, LO mode. For dirty-at-unity: STEP high, PRE-VOL up, MASTER down, HI mode ([waveinformer-v2-walkthrough](links/waveinformer-v2-walkthrough.md); [produce-like-a-pro-neve-in-a-pedal](transcripts/produce-like-a-pro-neve-in-a-pedal.md)).

**It distorts fast — clean-or-grind, not graceful edge-of-breakup.** The HI/LO toggle picks the lane: **LO** = clean headroom/DI, **HI** = distorts readily (OD→distortion→fuzz). The in-between can be harsh; plan to clean up with the *controls*, not the guitar volume (cleanup is real but limited — it's a preamp, not a Fuzz Face).

**HI-PASS before the fuzzes (the rig's key move).** Fuzz multiplies low-end mush; roll the HI-PASS (12 dB/oct, sweepable 160–650 Hz) up to ~100–200 Hz before the MXR 108 + Hizumitas and the wall tightens dramatically — the chord reads instead of turning to mud. The Hizumitas Tone can darken but can't high-pass; this can.

**The MID band steers what the fuzz emphasizes.** Boost ~1 kHz before the 108 → more aggressive/present/cutting fuzz; scoop it → darker "behind-the-wall" doom. You're choosing the fuzz's voice from in front of it.

**The EQ "honk/telephone" trick:** set all three SHIFTs to a midrange frequency and boost all three bands for a snarly, honking, radio-through-a-phone voice ([waveinformer-v2-walkthrough](links/waveinformer-v2-walkthrough.md)).

---

## 2. Signature settings

No official numbered presets exist — JHS gives the spec and leaves dialing to the user. Below are attributed; the only fully-numbered guitar presets in the wild are a low-confidence Guitar Chalk list (flagged).

| Sound | Settings | Source |
|---|---|---|
| **Clean Neve color** | LO mode · low STEP · low PRE-VOL · MASTER high; gentle Bass lift + Treble air | [waveinformer](links/waveinformer-v2-walkthrough.md) |
| **Console crunch** (into the fuzz wall) | HI mode · STEP 2–3 · PRE-VOL ~noon · mids pushed · **HI-PASS on ~120–200 Hz** · MASTER trimmed | [produce-like-a-pro](transcripts/produce-like-a-pro-neve-in-a-pedal.md) |
| **Broken-console fuzz** | **HI · STEP 5 · PRE-VOL maxed · EQ flat** — "pure preamp distortion, no amp" | quoted, [produce-like-a-pro](transcripts/produce-like-a-pro-neve-in-a-pedal.md) |
| **Bass DI (clean color)** | STEP 2–3 clicks · PRE-VOL ~9:00 · **MASTER ~3:00** — low-noise rule: **keep MASTER lower than PRE-VOL**; boost ~1 k / cut ~200–300 Hz for clarity | [bass-negus-bass-tutorial](transcripts/bass-negus-bass-tutorial.md) |
| **DI / recording** | XLR-input for line level + **engage the 20 dB PAD**; dual-out print (1/4"→amp, XLR→interface) | [colour-box-di-and-recording-settings](links/colour-box-di-and-recording-settings.md) |

See dossier §13 for four fuller clock-position starting points (clean Neve / console-crunch-into-fuzz / DI print / acoustic-violin).

---

## 3. Power-user tips, tricks & hidden features

- **The 193 mA / 9 V draw is the #1 real-world gotcha.** 9 V center-negative **only** (never exceed 9 V), but 193 mA is enormous — needs a **dedicated high-current isolated output ≥193 mA** (Strymon Zuma/Ojai 500 mA port, CIOKS DC7/8, MXR Iso-Brick, etc.). **Never daisy-chain; dedicate the slot.** Migration trap: V1 ran **18 V** — don't reuse a V1 supply. JHS's web page omits the mA figure, which is why people get caught ([colour-box-193ma-power-tips](links/colour-box-193ma-power-tips.md)).
- **It's a real channel strip:** XLR in (48 V phantom pass-through) + transformer DI + XLR out → straight to interface/FOH. Use the **−20 dB PAD (XLR-only)** on hot/line-level sources (an HX Stomp — or this rig's line-level VG-800).
- **Per-band EQ bypass:** each EQ knob is flat at its center detent — leave a band at noon and it's effectively out of circuit.
- **Dual parallel outs = DI + amp blend:** 1/4" → amp, XLR → interface simultaneously (same mono signal) for a re-amp-able DI track alongside the amp track.

---

## 4. Technique & placement (the console-to-tape arc)

- **Front-end for the whole fuzz wall.** Because it's always-on, the rest of Board 1 is voiced *through* it: set its EQ as the baseline tone, then let the 108/Hizumitas/Longsword stack on top. Bypassing it makes the front end brighter, looser, less mid-forward — so its engaged tone is "home base."
- **Console-front-end → tape-print arc** (Tape Op-backed): Colour Box = the Neve front end (color/DI in) → **PORTA424 / JHS 424** = the tape at the back → **Apollo x8** print. For a deliberate "recorded-wrong" print, push the Colour Box into console-crunch and let the 424s degrade the result.
- **Better on non-guitar sources** is the strong consensus — Tape Op tracked bass, vocals (ribbon mic), Moog, percussion, tabla through it ("worth the price alone just as a DI"). In this rig that means it's the natural DI for the **bass, acoustic (Taylor/Yamaha), and violin**, likely bypassing the fuzz section entirely for those.
- **Back off the downstream drives:** the Colour Box already adds gain + color, so the Brothers AM / Longsword / Oxford are stacking on a hot, saturated, EQ'd source — especially the Oxford (another JHS) compounds fast; use it as an intensifier, not added gain.

---

## 5. Notable users & recording history (honest)

- **Verified pedal-namers** (these resolve the dossier's old open question — use these over the marketing roster):
  - **Mac DeMarco** named the **Colour Box (V1)** in a 2019 Reverb interview: *"If you wanna get nasty, you get the Colour Box"* — he uses it to emulate a driven Neve preamp live.
  - **Black Pumas run the V2 on camera** in Premier Guitar's Rig Rundown — both **Eric Burton** (guitar board) and bassist **Brendan Bond** (who uses it "as a simple overdrive") ([colour-box-artist-vs-technique](links/colour-box-artist-vs-technique.md)).
- **The genuine recording technique it emulates** (verified): direct-into-Neve/EMI — Beatles "Revolution," Led Zeppelin "Black Dog," the Byrds "Mr. Tambourine Man," Chic "Le Freak," Motown, plus the Steely Dan/Petty/Nirvana direct-in lineage ([neve-direct-in-recording-history](links/neve-direct-in-recording-history.md)).
- **Artist-vs-technique caveat:** JHS's "U2, Wilco, The National, Spoon, Muse, The War on Drugs, Phantogram…" list describes records made with the **Neve direct-in *technique***, not verified Colour Box owners — JHS itself says those bands "used this *technique*." Cite it as technique, not endorsement.

---

## 6. Rig-specific recipes (banjo/baritone + DI duties)

Chain: `VG-800 → Polytune → CB Clean → Colour Box V2 → MXR 108 → Hizumitas → … → Deco`.

- **Banjo-into-fuzz fixer (its best trick in this rig).** Banjo is all 2–4 kHz attack, almost no body. Before the fuzz: pull **TREBLE down** (SHIFT toward ~6–10 kHz), **boost BASS/low-MID** to fake body, engage HI-PASS lightly. This is the pedal that makes the banjo-into-fuzz idea actually work.
- **Baritone:** home territory — HI-PASS to keep the low B from flubbing the fuzz, modest mid lift for cut; less corrective EQ than the banjo.
- **Console-crunch always-on (the key setting):** HI · STEP 2–3 · PRE-VOL ~noon · MID + at 1 kHz · TREBLE − (tame for the fuzz) · **HI-PASS on ~120–200 Hz**. Tightens and voices everything the 108 + Hizumitas chew on.
- **Bass/acoustic/violin DI → Apollo:** LO mode, low STEP, gentle Bass lift + Treble air, XLR out → interface (PAD if it clips). For violin the transformer warmth tames bowed top-end harshness. Pairs with PORTA424/JHS 424 → tape print.
- **VG-800 line-level source:** for clean modeled tones run LO as EQ only; push PRE-VOL to saturate an already-modeled amp into "recorded-wrong" territory. Mind line level — use the PAD logic if feeding the XLR in.

---

## 7. Best learning resources

- **Produce Like A Pro** — [the engineer's-eye view](transcripts/produce-like-a-pro-neve-in-a-pedal.md): DI + mic'd-amp print, the broken-console fuzz, on-screen manual specs.
- **WaveInformer** — the most detailed V2 control walkthrough ([clean→fuzz, Hi/Lo, Shift ranges, the honk trick](links/waveinformer-v2-walkthrough.md)).
- **The Bass Negus** — [deep bass settings + the low-noise gain-staging rule](transcripts/bass-negus-bass-tutorial.md). **The Bass Channel** — [10th-anniversary control walkthrough](transcripts/bass-channel-10th-anniversary.md) (confirms HPF 12 dB/oct).
- **Off Shift** — [using it like a plugin / re-amp + line-level interfacing](transcripts/off-shift-colour-box-like-a-plugin.md). **Jorb** — [multi-instrument demo](transcripts/jorb-multi-instrument.md) (synth/Wurli/lap-steel). **Reverb** — [classic direct-in guitar tones](transcripts/reverb-classic-direct-guitar-tones.md) (Revolution/Nirvana/ZZ Top/Floyd).
- **Text:** [JHS official spec](links/jhs-official-spec-and-named-sounds.md), [Tape Op engineer's DI take](links/colour-box-tapeop-engineer-di.md), [193 mA power tips](links/colour-box-193ma-power-tips.md).

---

## 8. Common pitfalls / gotchas

- **193 mA on a 9 V supply** — dedicate a high-current isolated slot; never daisy-chain; never exceed 9 V; don't reuse an 18 V V1 supply.
- **Stereo myth:** it's **mono** — the dual 1/4" + XLR outs are **parallel mono** (same signal to two destinations), not stereo. (The GearProfile was corrected to mono; the rig art's "V2 added stereo" is wrong.)
- **Wrong-input silence:** if the INST/XLR switch is set wrong, *no signal passes at all* — check the side switch first when debugging.
- **XLR out is OFF when bypassed** (in INST mode) — if you feed FOH/print off the XLR, killing the pedal kills that feed. Plan around it for always-on use.
- **Volume jumps on every gain change** — PRE-VOL/STEP set both gain and level; trim MASTER (muscle memory). The PAD is XLR-only and does nothing on INST.
- **It distorts fast** — the zone between clean and grind is harsh; pick a lane with HI/LO.

---

## 9. Captured sources

**Transcripts** (`research/transcripts/`):
- `produce-like-a-pro-neve-in-a-pedal.md` — Produce Like A Pro — engineer DI + mic'd-amp print; broken-console fuzz; manual specs.
- `waveinformer-v2-walkthrough.md` *(link)* / on-site — most detailed V2 control walkthrough.
- `bass-negus-bass-tutorial.md` — The Bass Negus — deep bass settings + low-noise gain-staging.
- `bass-channel-10th-anniversary.md` — The Bass Channel — control walkthrough; confirms HPF 12 dB/oct 160–650 Hz.
- `off-shift-colour-box-like-a-plugin.md` — Off Shift — hardware-plugin/re-amp + line-level interfacing.
- `jorb-multi-instrument.md` — Jorb — multi-instrument (synth/Wurli mic-pre/lap-steel print).
- `reverb-classic-direct-guitar-tones.md` — Reverb — Revolution/Nirvana/ZZ Top/Floyd/Byrds direct-in technique.

**Links** (`research/links/`):
- `jhs-official-spec-and-named-sounds.md` — JHS — authoritative corrected spec (±15/±10 dB, HPF 12 dB/oct).
- `waveinformer-v2-walkthrough.md` — WaveInformer — ranges, named sounds, the honk trick.
- `colour-box-gain-staging-di-technique.md` — STEP/PRE-VOL/MASTER discipline, HI/LO, HI-PASS, DI workflow.
- `colour-box-193ma-power-tips.md` — the 193 mA/9 V gotcha + which supplies run it.
- `colour-box-stereo-myth-io-gotchas.md` — stereo myth, wrong-input silence, XLR-off-when-bypassed, PAD-is-XLR-only.
- `colour-box-bass-settings.md` / `colour-box-bass-di-talkbass.md` — consolidated bass DI use (PAD for line level; "better on bass than guitar").
- `colour-box-di-and-recording-settings.md` — DI/print/re-amp + classic direct-in settings.
- `neve-direct-in-recording-history.md` — the genuine direct-into-Neve records.
- `colour-box-artist-vs-technique.md` — separates the marketing list from VERIFIED Mac DeMarco (V1) + Black Pumas (V2).
- `colour-box-tapeop-engineer-di.md` — engineer's DI/mic-pre/console-print take.
- `guitarchalk-numbered-presets.md` — 5 numbered presets (flagged low-confidence/AI-ish).

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Colour-Box-V2-DeepResearch.md`](Colour-Box-V2-DeepResearch.md); the manual is at [`manuals/ColourBoxV2.pdf`](../manuals/ColourBoxV2.pdf).

> **Honest coverage notes:** TalkBass (403), Reverb, and Reddit blocked the fetcher, so owner/bass tips lean on accessible reviews (WaveInformer, Bass Musician, Tape Op, Produce Like A Pro) + JHS official. No demo gives numbered acoustic/violin settings (those are inferred from the "sweetener" use); the only fully-numbered guitar presets are a low-confidence Guitar Chalk list, flagged. The EQ/HPF spec was corrected this wave to JHS's current official figures.
