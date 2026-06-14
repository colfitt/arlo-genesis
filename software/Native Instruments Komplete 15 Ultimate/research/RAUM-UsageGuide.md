# RAUM — Usage Guide

RAUM is NI's abstract/ambient reverb — and the navigator's nominated **"#1 rig reverb"** for
infinite drones, granular clouds, and resonator tones. For this rig it's the end-of-chain
"make-it-infinite" box: freeze a chord into an endless bed, or push Cosmic feedback to 100% for a
self-blurring wash, then play banjo/baritone over it.

> **⚠️ NOT CURRENTLY INSTALLED.** RAUM is **not on disk** (not in CONTENTS.md / the Components
> folder). It's **included in Komplete 15 Ultimate AND free via Komplete Start** — so it's a
> one-click **Native Access** install at no cost. The navigator previously listed it as an active
> rig tool; treat this guide as "install it, then do this." [links/raum-free-komplete-start.md]

> **⚠️ NAVIGATOR CORRECTION (propagated):** the old nav said "Cosmic mode + Freeze = infinite
> drones." **Wrong mechanism — Freeze is on GROUNDED and AIRY only; Cosmic has no Freeze button.**
> Infinite *Cosmic* drones come from **Predelay Feedback = 100%** (Cosmic's all-pass cascade lives
> in the predelay feedback path). Both give infinite sustain, different routes.
> [links/raum-manual-freeze-global-controls.md; links/raum-manual-algorithms.md; transcripts/raum-ni-walkthrough.md]

---

## 1. The three algorithms & Freeze

- **Grounded / Airy** — classic→ethereal reverbs; controls = **Diffusion / Size / Density / Decay
  / Damp / Modulation**. **Freeze** available here.
- **Cosmic** — abstract all-pass-cascade space; controls = **Density / Size / Rate / Modulation**;
  **no Freeze** — its infinite comes from **Predelay Feedback**.
- **Global:** **Predelay** (sub-1 ms → 2 s, syncable to 4 bars), **Feedback** (100% = infinite),
  **Low/High Cut**, **Mix** vs **Reverb** amount.
[links/raum-manual-algorithms.md; links/raum-manual-predelay-filters.md]

---

## 2. Essential workflows

- **Infinite Freeze drone (Grounded/Airy):** Mix → 100%, play chord, hit **Freeze** — transport
  can stop, tone holds forever. The **only live control under Freeze is Size** — ride it. *Riser
  variant:* Size 100% → Freeze → turn Size **left** (Dense = noise wash, Sparse = granular riser).
- **Infinite Cosmic drone:** Cosmic + **Predelay Feedback → 100%**, hold a note → the cascade
  blurs each pass into an endless wash. Modulate Size/Rate live.
- **Hans-Zimmer pitch-bend swell:** automate **Size** on Airy (clean, no clicks). "Just modulate
  the size, it'll sound awesome."
[transcripts/raum-ni-walkthrough.md; links/raum-manual-freeze-global-controls.md]

---

## 3. Signature settings (this rig)

- **Granular cloud:** Density **Sparse** + Size **high** → "almost a granular effect."
- **Detuned/seasick shimmer wall:** **Modulation > 70%** = "weird, uncanny, detuned and
  dissonant" (designer Julian Parker); big Size + Airy.
- **Tuned resonator on banjo/baritone:** very low **Predelay** (sub-ms→few ms) + high **Feedback**
  = a pitched comb; predelay length sets the pitch; a percussive pluck rings like a physical model.
- **Dub decay:** high Feedback + sweep **High Cut** down → repeats darken into the wall.
- **4-bar drone looper:** **Predelay Sync ON** (up to 4 bars) + Feedback 100% → an adaptive-limiter
  "auto-overdub"; play to layer, stays HF-crisp (sample-quantized).
[links/raum-parker-design-resonator-looper.md; links/raum-manual-predelay-filters.md]

---

## 4. Rig-specific recipes

- **Navigator chain:** source → Mod Pack → Bite/Freak → Replika XT (Diffusion) → **RAUM (Cosmic +
  Feedback 100%, *or* Grounded/Airy + Freeze)** → infinite.
- **Send vs insert (Felix Raphael's real setup):** run RAUM on **Logic aux/return buses, Mix 100%
  on the bus** — two returns: a **"Room"** (Mix 10–35%, short Decay, Predelay 20–60 ms, Low cut
  150–200 Hz / High cut 8–12 kHz) and an **"Atmos/Drones"** (long Decay + Freeze). Returns = CPU
  headroom + independent depth. [links/raum-felix-raphael-live-returns.md]
- **Logic AU:** automation-friendly throughout; no host-specific gotchas surfaced.

---

## 5. Notable users & techniques
**Felix Raphael** (ambient/emotional electronic, album *DO YOU*) — documented in detail: Freeze on
an Atmos bus over performed pads, algorithm-as-emotion mapping, clamped automation ranges,
"negative space" restraint. [links/raum-felix-raphael-live-returns.md]

## 6. Pitfalls / gotchas
- **Freeze ≠ Cosmic** (see correction). Under Freeze only **Size** is live.
- Feedback 100%+ with loud input is tamed by an internal **adaptive limiter** (input ducks the
  loop) — no classic runaway, but watch overall bus gain.
- **Not installed** — install via Native Access (free). **Logic AU** when installed; **Lite** track
  limits as secondary host.

## 7. Captured sources & QC
- Transcript: `raum-ni-walkthrough` (knob-by-knob on a pad).
- Links: `raum-manual-algorithms`, `raum-manual-freeze-global-controls`, `raum-manual-predelay-filters`,
  `raum-parker-design-resonator-looper` (designer interview), `raum-felix-raphael-live-returns` (artist),
  `raum-free-komplete-start`. Builds on the existing nav link `km-nav-raum-reverb-design`.

**QC:** algorithms/controls/Freeze from NI's manual + official walkthrough + the designer
interview (high confidence — the Freeze/Cosmic correction is triple-sourced). NI product page
403'd → free-availability triangulated (Komplete Start + MusicTech + KVR). Walkthrough video is
2020-era (knobs identical to current). **Install status: NOT on disk; free via Native Access.**

## Sources
See §7. Originals: youtube.com (NI), native-instruments.com manual + blog (Parker interview, Felix
Raphael). URLs on line 1 of each file.
