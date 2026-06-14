---
type: chain
title: Big Sky Freeze-Ahead → Banjo Lead Over the Wall
date: 2026-06-14
artists: [Swans, Sufjan Stevens]
instrument: banjo (via GK-5 → VG-800)
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - MXR M173 Classic 108 Fuzz
  - EarthQuaker Devices Hizumitas
  - Strymon TimeLine
  - Strymon Big Sky
---

# Big Sky Freeze-Ahead → Banjo Lead Over the Wall  ⭐

Freeze a fuzz wall into an infinite hold, then play a banjo LEAD over it that *still gets reverb* — solving the freeze-kills-the-lead problem with the documented "reverb ahead of the freeze" placement. (Big Sky is the End-board reverb here; substitute for the H90 when you want the dedicated freeze workstation.) Designed integration.

## Signal path

Banjo (GK-5 → **VG-800 #3 GR-300 Thick-Synth Lead** for the lead voice, or #5 VIO for an attackless bed) → **CB Clean #5 Banjo Transient Tamer** → 108 #9 → **Hizumitas #9 Banjo Sustain Manufacturer** → (End board) → **Strymon TimeLine** (a short ambient delay AHEAD of the freeze, so the lead gets space) → **Strymon Big Sky #2 Drone Wall (Cloud, freeze)** → tape.

## Per-unit

- **VG-800 #3:** with `COMP SW ON` extends the banjo's fast decay so it behaves like a held note.
- **Clean #5:** slow Attack (~1:00) lets the pluck spike through then clamps; **Envelope Balance high** (comp tracks the bright register, ignores phantom lows).
- **Hizumitas #9:** Tone 1–2:00 (bass side) to roll off the banjo's 2–4 kHz pierce + manufacture sustain.
- **Big Sky #2:** Machine **CLOUD**, DECAY 20 s+, Diffusion high, **HOLD = FREEZE**; for banjo-as-lead pull **MIX back to ~12:00** so the wall sits behind the line.

## Routing

Stereo from the End board. **The placement is load-bearing:** with HOLD = FREEZE the notes you play *over* the frozen chord come through DRY — so the TimeLine sits **before** the Big Sky to give those lead notes their own ambience (Big Sky #4 documented fix). INFINITE instead of FREEZE would add every new note to the wash (chaotic) — use FREEZE.

## Sound

A frozen oceanic Cloud wall with a present, reverberant banjo lead floating on top. Taste-ref: drone/doom + banjo-as-lead (Swans bed under a Sufjan-style melodic line).

## Play

Strum a chord, freeze it on the Big Sky, then play the banjo lead over the static wall; the TimeLine gives the lead its space. Optionally capture the frozen pad to the Blooper (Big Sky #5) and change patches underneath.

## Sources

- Basis: designed integration; chains VG-800 #3 + Clean #5 + 108 #9 + Hizumitas #9 + TimeLine + Big Sky #2. The **reverb-ahead-of-freeze** placement is the documented Antoine Michaud fix (Big Sky #4, `antoine-michaud-bigsky-infinite-vs-freeze.md`).
- Source file: `Research/Chains/drone-walls.md` (C4)
