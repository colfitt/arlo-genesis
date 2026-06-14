---
name: iZotope Ozone 11
brand: iZotope
category: software
subcategory: mastering-suite
formats: [vst3, au]
host_in: [logic, ableton]
installed: true
version: "11"
status: owned
tags: [mastering, master-bus, tape-saturation, stereo-imaging, limiter, glue]
related: [Komplete (Ozone 11 Standard), Antares (the mis-grouped "Vocal*" plugins)]
---

# iZotope Ozone 11

**Summary** — A **mastering suite**: a hostable rack of master-bus modules (EQ, Dynamics,
Maximizer, Imager, Exciter, Low End Focus, Vintage Tape/EQ/Comp/Limiter, Master Assistant /
Tonal Balance). Installed as the **Ozone 11** VST3 + the `iZOzone11AUHook.component` AU
bridge (verified in `Software/_inventory.json`).

> **Folder-name correction:** despite "iZotope (suite)," **only Ozone is installed.** The
> "Vocal De-Esser/Reverb/Prep" plugins once grouped here are **Antares**, and **RX /
> Nectar are NOT installed.** A second copy — **Ozone 11 Standard** — ships inside
> Komplete (same family, fewer modules; the Advanced-only Vintage modules + Match EQ +
> Stabilizer are in *this* full build).

## Why I have it
The "studio end" polish stage for a degraded/drone/doom/shoegaze rig — but **not** for
loudness mastering. Its real jobs here: gentle **glue + analog color** on a bounce
(Vintage Tape / Vintage Limiter), **release consistency** (Tonal Balance Control / Match
EQ across an EP), **widening the wall** (Imager), and **de-mudding a drone low end** (Low
End Focus). Every module also runs as a **standalone insert**, so it doubles as a box of
creative tone-shapers on individual buses, not just a master strip.

## Signature uses
- **Vintage Tape glue** on the master/wall bus — 30 IPS, Drive +4 dB, Bias -0.5, Harmonics
  2.0 (or 15 IPS + positive bias for a warmer lo-fi tilt).
- **Master Assistant as a sketch** — Vintage intent, Low intensity, -14 LUFS target, then
  prune everything that flattens the dynamics.
- **Imager** to widen the reverb/delay return of a wall (sub band kept mono).
- **Low End Focus** (Smooth, Mid-Side) to clean a boomy drone bass.
- **Vintage Limiter** instead of the Maximizer when weight/vibe > transparency.

## Notes
- **Don't over-master.** Maximizer is the least-useful module here — keep gain reduction
  ≤3-4 dB or skip it. Loudness is largely pointless under streaming normalization
  (Spotify/Tidal -14, YouTube -13, Apple -16 LUFS); master ~-14 and keep the grit.
- **Vintage modules + Match EQ + Stabilizer are Advanced-only** (the Komplete Standard
  copy lacks some). This is the full build.
- **Logic = AU-only**, loads via `iZOzone11AUHook.component`.
- Bass drones distort first under limiting — watch the sub, set ceiling -1.0/-2.0 dB.
- Full usage guide: `research/iZotope-Ozone-UsageGuide.md` (11 captured sources).
