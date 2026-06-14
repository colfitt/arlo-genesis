https://op1.fun/users/pattisoni/packs/drones-2166 · https://op1.fun/users/vagelismoschos/packs/ambient-drone-pack · https://op1.fun/users/nate437/patches/statiq · https://op1.fun/users/nate437/patches/celestial · https://op1.fun/users/nate437/patches/windswept · https://op1.fun/users/alanholding/patches/planks · https://op1.fun/users/theredbear/patches/cluster_pad · https://op1.fun/users/cuadroped/patches/nangs · https://op1.fun/users/vanillasun/patches/drone
op1.fun · various uploaders (iFaber, nate437, alanholding, TheRedBear, cuadroped, VanillaSun, Onemanbandthing) · 2017–2018, accessed 2026-06-14

# op1.fun — NEW drone / ambient / pad patches with concrete engine/octave/FX/LFO settings

Expansion pass beyond the Cuckoo "Opines" capture. These are real, high-download community patches whose op1.fun pages expose **engine type, octave, FX type, LFO type** (and an author description). As with Opines, the numeric `knobs`/`adsr`/`fx_params` arrays are NOT shown by the web UI — download the `.aif` and run `op1-dump` (see `op1-patch-file-format.md`) for those. Engine/octave/FX/LFO is the same granularity already accepted in this folder.

## pattisoni "drones" pack — 11 patches (the most rig-on-target set found)
ALL sub-octave, drone-purpose, drwave/cluster/phase. iFaber's six (drone1–6) are the core:
| Patch | Author | Engine | Octave | FX | LFO |
|---|---|---|---|---|---|
| drone1 | iFaber | drwave | **-2** | — | value |
| drone2 | iFaber | drwave | **-2** | — | value |
| drone3 | iFaber | drwave | **-2** | — | value |
| drone4 | iFaber | drwave | **-2** | delay | value |
| drone5 | iFaber | phase | **-2** | grid | value |
| drone6 | iFaber | cluster | 0 | grid | tremolo |
| SFX-Wobbledrone | Onemanbandthing | drwave | -1 | delay | value |
| WAV-Droney | Onemanbandthing | drwave | -1 | — | value |
| Digital_Drone | spaceflightsnice | (not shown) | — | — | — |
| didg_drone | bronko | (not shown) | — | — | — |
| organ drone | B3N3/)Tt0 | (not shown) | — | — | — |

**Pattern to copy for a banjo/baritone doom drone:** drwave engine at **octave -2**, a **value LFO** on, no FX (or `grid`/`delay` for motion). Phase at -2 + grid for a metallic sub-drone.

## Individual flagship patches (high downloads = community-vetted)
| Patch | Author | Engine | Oct | FX | LFO | Downloads | Author description |
|---|---|---|---|---|---|---|---|
| **statiq** | nate437 | digital | 0 | nitro (on) | value (on) | 15,804 | "Somber, Distant, Lo-Fi. Great as a lead or as harmonic filler." |
| **celestial** | nate437 | voltage | +1 | punch (on) | random (off) | 18,061 | (celestial/ambient lead) |
| **windswept** | nate437 | cluster | 0 | cwo (off) | value (off) | 1,647 | "Synth that replicates the sounds of a windy day." |
| **planks** | alanholding | cluster | 0 | nitro (on) | value (off) | 11,101 | "Compressed pad" |
| **cluster_pad** | TheRedBear | cluster | 0 | filter (off) | element (off) | 11,057 | (lush cluster pad) |
| **Nangs** | cuadroped | digital | 0 | nitro (on) | value (on) | 22,538 | "Tame impala 'Nangs' esque patch needs some vibrato but other than that pretty close" |
| **Cassette Ambient** | VanillaSun | sampler | +1 | punch (on) | tremolo (on) | 24,077 | "resampled from an old Sony Walkman w/ analog synth — vintage tape character" |

## Why these fit the rig (drone/doom/shoegaze/degraded)
- **statiq** (digital · nitro · value) — "somber, distant, lo-fi, great as a LEAD or harmonic filler" is almost a spec for the banjo-as-lead/degraded-wall brief. nitro = the OP-1's gnarly distortion/filter FX.
- **Nangs** (digital · nitro · value) — a named **Tame Impala** reference patch (psych/shoegaze adjacent); the most-downloaded synth patch found.
- **planks / cluster_pad / windswept** (cluster) — the supersaw-ish "thick lush pad" engine; nitro on `planks` = compressed/saturated pad, the wall-bed move.
- **celestial** (voltage · punch · +1) — voltage is "biting/AM-rich, surprisingly good for evolving sounds"; punch FX = its SP-303/lo-fi-grit color.
- **Cassette Ambient** (sampler · punch · tremolo) — already-degraded resampled tape texture; 24k downloads.

> Honesty flag: octave/FX/LFO/engine are read directly off the op1.fun pages; the per-knob numeric arrays are not exposed and were not dumped. "Field-compatible" assumed (standard `.aif`); a handful of OG-era patches using removed engines can fail on Field (see RMR capture).
