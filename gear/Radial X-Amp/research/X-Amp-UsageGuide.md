# Radial X-Amp — Usage Guide

How the X-Amp is *actually used* day to day, to complement the spec/reference dossier in `X-Amp-DeepResearch.md`. The X-Amp is a **utility, not a tone source** — there is no artist mythology and almost no "sound" to dial in; it is the transparent analog box that makes the rig's **"commit later, mangle infinitely"** workflow possible. So this guide is workflow-first: **the reamp loop step by step, level/ground/phase hygiene, latency alignment, the two-channel use cases, and the rig-specific reamp moves** (banjo/baritone/VG-800 through the boards, X-Amp vs. the EHX Effects Interface).

> Captured this wave (Tier C, 1 agent): 1 video transcript + 3 distilled links = 4 sources (see §8). The official Radial video attribution was verified via `yt-dlp --print channel` = **Radial Engineering**. **Honest coverage note up front:** there is *no* X-Amp-specific deep-demo culture to mine — it's behind-the-glass studio plumbing. Coverage leans on **Radial's own first-party docs (manual + blog + FAQ)** plus **general reamp engineering** (latency/phase), which all transfer cleanly. The Apollo-side routing was already documented in `Gear/UA Apollo x8/research/Apollo-x8-UsageGuide.md` §1; this guide stays consistent with it and goes deeper on the X-Amp itself.

---

## 1. The reamp loop, step by step

The one move this box exists for. Print clean once, ruin it afterward as many times as you like.

1. **Print a clean DI** of the source to the Apollo (banjo, baritone, bass, guitar) — and/or print the **VG-800's modeled output** as its own track. Use a quality DI on the way in so the source is as clean/natural as possible. Focus on the *performance*; tone comes later.
2. **Send the printed track out a SPARE Apollo line output** — Line Out 3 or higher, **kept OFF the monitor bus**. Assign that DAW track's output to the spare line out.
3. **Balanced XLR (or TRS→XLR) into the X-Amp's input.** **No DI box is needed** between the Apollo and the X-Amp — both are balanced line level (a DI is for the *opposite* direction). The X-Amp's XLR input is line-level only; never feed a guitar into it.
4. **X-Amp converts line → instrument level/impedance** on **OUT-1** (¼" TS instrument cable) → into the **front of Board 1 / the VG-800**. Run *into the pedalboard first*, then onward through the chain (texture → time → tape) and/or into the VG-800 for amp/cab/synth modeling.
5. **Re-capture the mangled wet result on a FRESH Apollo input** (a new DAW track). **Set that record track's output to the main stereo bus — NEVER back to the spare line out feeding the X-Amp** (that's the feedback loop). The end-of-chain stereo pair prints to two new inputs.
6. **Repeat at will** — re-roll chain settings, swap pedals, change the VG-800 model. The player never re-performs; the DI is frozen.

**Level setting (do this by the CLIP LED, not by ear first):**
- Start the recessed **LEVEL pot at 12 o'clock** (adjust with a pick or flat-head; it's recessed so it can't get knocked).
- Raise the **DAW/Apollo output** until the X-Amp's **CLIP LED just occasionally blinks on peaks**, then **back off until it never blinks** — that keeps the X-Amp's *output* clean.
- Then set **LEVEL** so the amp/pedal sees the same level/tone it saw when the instrument was plugged in directly (guitar amps have no input meter, so match by ear/feel). Push the DAW send as hot as possible without clipping for the best reamp signal-to-noise.

**Ground / hum elimination (two layers, work in order):**
- Hum or buzz? **First** depress the **input-side GROUND LIFT** (disconnects pin-1 at the XLR) — this kills most ground-loop hum.
- Still buzzing **and** you're using a second amp on OUT-2? Then flip the recessed **internal OUT-2 GROUND LIFT** (accessed with a small screwdriver through the side-panel hole; factory-set to *lifted*).
- **Keep a grounded amp on OUT-1 at all times when using OUT-2** — OUT-1 is the direct-coupled output and the box's **safety ground reference**, even if that amp is off/unused.

---

## 2. Phase / latency alignment

The X-Amp is analog and adds no meaningful latency — the delay is the **Apollo round trip** (D/A → X-Amp → rig → return → A/D → DAW), so the reamped take always lands slightly **late** vs. the original DI. Left uncorrected, blending the two combs/cancels. Fix it once, reuse the number ([reamp-latency-phase-alignment](links/reamp-latency-phase-alignment.md)):

- **Measure (loopback):** reamp the dry DI straight back into an Apollo input once, zoom way in, line up a clear transient against the original DI, and **read off the sample difference.** That's your nudge value for that sample rate + buffer. (Apollo+X-Amp users report a **64-sample buffer** lands "pretty much spot on"; 528 samples ≈ 12 ms @ 44.1 kHz is an illustrative figure — measure your own.)
- **Apply it** three ways: (a) **manually nudge** the reamped clip back N samples (drop a transient/click at the head of the take to make alignment easy); (b) set a **negative recording offset / nudge** in the DAW for many passes; (c) best of all, patch the X-Amp+rig as a **DAW external-FX / hardware insert** (Logic Pro's **I/O plugin**, or Cubase/Reaper/Pro Tools) — the DAW pings the loop, measures latency, and **compensates automatically**, and you can reamp in real time as a printable insert.
- **Keep the buffer fixed** across stacked passes so the offset stays identical — important when layering many passes of the same DI into a wall.

---

## 3. Using the two channels (OUT-1 + OUT-2)

The dual output is the X-Amp's headline feature vs. a single-output reamper. Three ways to use it:

- **Two parallel chains, blended in the box.** OUT-1 → a body chain (e.g. VG-800 clean model, or Board 1 with dirt off); OUT-2 → the full mangled chain (Hizumitas → Longsword → End Board). Capture both returns to separate Apollo inputs and blend in the DAW. Classic **parallel/blend reamping** (clean weight + dirty texture), done in real analog. The active buffer holds level across both outputs without re-trimming.
- **Stereo reamp** — split one DI to two boards for a wide stereo wall, OUT-1 left / OUT-2 right.
- **A/B two destinations** — feed two different rigs and pick the keeper.
- **Phase-check every time you change a destination.** Re-patching can flip phase; A/B the **180° POLARITY** switch on OUT-2 with both amps at equal volume and keep whichever "sounds the fullest." OUT-2's transformer also provides galvanic isolation, so the second chain won't ground-loop.

---

## 4. Rig-specific reamp workflows

- **Banjo (Gold Tone EBM-5) — tame the bright transient after the fact.** Print the EBM-5 dry (and/or its VG-800 output). Reamp through Board 1 with the VG-800 on a darker amp model and the Hizumitas Tone past noon; iterate on the *frozen* DI until the 2–4 kHz ice-pick becomes a wall. No fatiguing re-performance through fuzz.
- **Baritone Jazzmaster (GK-5).** Print the magnetic DI **and** the VG-800 output as separate tracks; reamp either. The baritone's low fundamental survives the X-Amp's 20 Hz–15 kHz response fine.
- **The VG-800 double-reamp (the most rig-specific trick).** The VG-800 is already a modeled COSM source — print it dry, then **reamp the model back through real pedals** (a modeled tweed re-fuzzed through MXR 108 + Hizumitas; a VG-800 pad reamped into the End Board's reverbs to become a distorted drone). Or **double-reamp:** DI → VG-800 → capture; then *that* capture → the three boards → capture. Each pass is a new generation of "wrong."
- **Build the wall by stacking passes.** Because the X-Amp is transparent, reamp the **same DI a dozen times** with different settings and layer the passes — clean banjo line becomes a Hizumitas drone on one pass and a Microcosm wash on the next, both committed at leisure. (Keep the buffer fixed so they stay phase-aligned — §2.)
- **Bass.** Reamp through a drive/amp for grit while keeping the clean DI underneath for low-end weight — parallel bass distortion, after the fact.
- **Keyboards / S08 (a Radial-documented trick).** The manual notes synths and organ tracks reamped through a distorted amp/pedal — Jan Hammer's "guitar" synth-solo growl and Keith Emerson's distorted-Hammond approach. Same move applies to the S08 or accordion: reamp a clean keys track into the boards for grit.

---

## 5. X-Amp vs. the EHX Effects Interface (when to grab which)

Both bridge a line-level track back into the pedals — they are **complementary, not redundant**:

- **Grab the X-Amp when** you want **fast, clean, latency-free, pure-analog** reamping with **no computer in the audio path**, or a **two-destination split** (parallel/stereo). It's instant: power it, patch it, set LEVEL by the CLIP LED, go.
- **Grab the EHX Effects Interface when** you want the reamp to be a **recallable, automatable DAW plugin** living inside the session (USB-C "hardware plugin," wet return on its own track), or you want to **drop software plugins onto the physical board**. It's the digital/plugin-bridge counterpart.
- Rule of thumb: **X-Amp = commit clean and mangle infinitely in analog; EHX = make that same reamp a recallable session object.** Owning both is justified — different workflows.

---

## 6. Power & hookup gotchas

- **15 VDC / 400 mA, NOT 9 V.** The single biggest gotcha for a pedalboard owner — it will **not** run from a 9 V isolated supply slot. Use the included brick (or a 15 V multi-voltage outlet). It's **active and passes no signal unpowered** (no true bypass). Don't lose the adapter.
- **OUT-1 must stay connected to a grounded amp** whenever OUT-2 is in use (safety ground / box reference).
- **Long cable runs are fine** — the active buffer drives unbalanced ¼" cable up to ~50 ft, so the X-Amp can live in the rack with the boards across the room (Radial SGI for longer).
- **LEVEL is recessed** ("set & forget") — keep a pick/flat-head nearby if you tweak it often.

---

## 7. Common pitfalls / gotchas

- **Feedback loop:** never route the reamp *record* track back out the spare line out feeding the X-Amp. Record track → main bus; dry-send track → spare line out (kept off the monitor bus).
- **Monitor bleed / feedback in the room:** when the amp/loop is live, **turn the monitors down and use headphones** while recording the reamp pass.
- **Phase flips on re-patch:** re-check the 180° switch any time you change a destination.
- **Misaligned reamp prints comb-filter:** always nudge the reamped take by the measured round-trip offset before blending against the dry DI (§2).
- **Wrong end of the box:** the XLR input is **line-level only** — don't feed a guitar into it; the ¼" outputs are the instrument-level side.
- **Converter-stage color you didn't ask for:** when capturing the reamped return, bypass the Apollo preamp to the A/D for the cleanest print (the damage should come from the chain, not the converter) — consistent with the Apollo guide.

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `radial-reamp-academy-ideal-workflow.md` — **Radial Engineering** (channel verified) — official "How to Reamp" part-2 video: the 3-step workflow, DI/THRU monitoring, "level as hot as possible without clipping," DAW-EQ-on-the-way-out, combined-box tip.

**Links** (`research/links/`):
- `radial-the-reamping-workflow.md` — Radial Engineering blog (2023-05-09) — written 3-step primer; the feedback-avoidance rule (mic track → stereo bus, not the reamp send); level-match the reamp box AND DAW to the direct-guitar level.
- `radial-xamp-faq.md` — Radial Engineering X-Amp FAQ — LEVEL at 12 o'clock, ground lift for hum, 180° for multi-amp phase, "outputs can feed instrument-level effects," ~50 ft cable drive, XLR-in is line-level-only.
- `reamp-latency-phase-alignment.md` — Fractal/Kemper/Reaper forum consensus — round-trip-latency measurement (loopback → sample count → nudge), manual transient alignment, DAW recording-offset, and external-FX auto-compensation (Logic I/O plugin); keep the buffer fixed across stacked passes.

## Sources

All claims above cite a captured `transcripts/` or `links/` file (original URLs on the first line of each), the manual, or the dossier. Video attribution verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`X-Amp-DeepResearch.md`](X-Amp-DeepResearch.md); the manual is at [`manuals/XAMP-Manual-WEB-04-2025.pdf`](../manuals/XAMP-Manual-WEB-04-2025.pdf). The Apollo-side reamp routing is in [`Gear/UA Apollo x8/research/Apollo-x8-UsageGuide.md`](../../UA%20Apollo%20x8/research/Apollo-x8-UsageGuide.md) §1 — this guide stays consistent with it.

> **Honest coverage note:** the X-Amp is studio plumbing, so there's no demo/artist culture to mine and no tone to "dial in." Coverage is therefore **first-party Radial docs (manual + blog + FAQ) + transferable general reamp engineering** rather than X-Amp-specific demos — which is the right and honest fit for a utility box. The reamp loop, level/ground/phase hygiene, two-channel use, and latency alignment are all well-sourced and consistent across Radial's own material and the Apollo guide. The rig-specific banjo/VG-800/stacking workflows are the original synthesis here.
