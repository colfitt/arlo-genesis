https://www.nudistaudio.com/nudistort  (+ KVR product page, retailer listings)
nudistaudio.com / kvraudio.com · vendor + aggregated listings · 2024–2025

Canonical feature/spec reference for Nudist Audio Nudistort. (The official page is
JS-rendered and resists scraping; this distills the vendor's own copy + the KVR
product page + retailer descriptions.)

## What it is (vendor's own framing)
"A completely new kind of distortion" — the dev notes "distortion" is a misnomer.
"Nudistort's algorithm is inherently hard to describe, because it works differently
from other distortions under the hood. It is highly conditional, nonlinear, and
time-varying — a Rube-Goldberg machine of cascading audio signals." Marketed as
spanning subtle transformation → total destruction. Poetic copy: "an auditory
calcifier… an oxidized ear-sword."

## Spec
- **$40** (often **$32** on sale).
- Formats: **VST3, AU, AAX**. macOS 10.13+ (Universal 2 / Apple Silicon native),
  Windows 10+.
- **Very low CPU** (repeatedly cited as a standout — unusual for this much
  nonlinear processing).
- Sibling product: **Fermenter** (2025), same dev.

## Control set (consolidated)
DISTORT: Drive · Type (A/B/C/D — four genuinely different algorithms) ·
Mode (T/P) · Grain (changes behaviour per Type; not granular) · Damping ·
Mu-law (companding) · Buzz (noise) · Mix.
GLOBAL/TONE: Input/Output gain · Tone (tilt EQ, pre-distortion).
DELAY: Mix · Time · Abnormality · Feedback · Type · Sync · L/R Offset.
MODULATION: Wobble (tape pitch) · Mod amount/freq · Noodle (pitch-tracking sine) ·
Species (note-keyed harmonic resampling).
"The delay algorithm you cannot find anywhere else… sounds amazing and massive."

## Presets — curated by named producers
Kenny Beats · Andrew Huang · **Romil Hemnani (BROCKHAMPTON)** · Psymun · Reske ·
Shane Becker · Doug Schadt. Presets are the recommended starting point given how
non-obvious the params are.

## CORRECTION / honesty flag (important)
Several SEARCH-ENGINE SUMMARIES (not the actual reviews) claim a simplified
"Drive / Bias / Tilt EQ" three-knob layout with values like "drum overheads Drive
~10% Bias Even" and "vocals Drive ~15% Mix 30%." These do NOT appear in any
directly-fetched primary source (WaveInformer's hands-on review, KVR, the vendor
page). The real layout has NO "Bias" knob — it has Type/Grain/Damping/Mode. Treat
those Bias/percentage values as likely AI-confabulated and DO NOT cite them as
real Nudistort settings.
