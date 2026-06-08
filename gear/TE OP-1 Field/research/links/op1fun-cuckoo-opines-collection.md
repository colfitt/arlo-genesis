https://op1.fun/users/cuckoomusic/packs/opines-collection
op1.fun · cuckoomusic (Cuckoo) · "Opines Collection" pack (accessed 2026-06-03)

# Cuckoo "Opines Collection" — 15 shared patches with real engine/octave/FX/LFO settings

A free op1.fun pack by Cuckoo. Chiptune / "Nintendoish" character, almost entirely the **DR Wave** synth engine. These are the concrete per-patch settings exposed on op1.fun's patch pages (engine = `type`, plus octave, FX type, LFO type). Per-knob numeric values (the `knobs`/`adsr`/`fx_params` arrays) are NOT shown by op1.fun's UI — to get those you download the .aif and run `op1-dump` (see `op1-patch-file-format.md`).

## Synth patches (13) — all DR Wave engine
| Patch | Engine | Octave | FX | LFO |
|---|---|---|---|---|
| brinsting | DR Wave | -2 | — | — |
| tristair | DR Wave | -1 | — | — |
| slot_piano | DR Wave | +1 | delay | random |
| plinka | DR Wave | 0 | delay | tremolo |
| paper_keys | DR Wave | 0 | spring (reverb) | value |
| konapulse | DR Wave | 0 | — | — |
| feena | DR Wave | +1 | delay | tremolo |
| kraids_echo | DR Wave | 0 | delay | — |
| bass_buzzer | DR Wave | -2 | — | — |
| ikaros | DR Wave | +1 | delay | — |
| pianoid | DR Wave | +1 | delay | — |
| popofone | DR Wave | +1 | — | — |
| zeldas_nerves | DR Wave | 0 | — | tremolo |

## Drum patches (2) — DBox physical-model drum synth
| Patch | Engine | Notes |
|---|---|---|
| opines_a | DBox | drum kit |
| opines_b | DBox | variation — "different hihat crunchiness" |

## Takeaways
- Bass patches sit at **octave -2** (bass_buzzer, brinsting); leads/keys at **+1**.
- The go-to FX in this pack is **delay**; LFOs are **tremolo / value / random**.
- Two drum kits are built on the **DBox** engine (synthesized, not sampled) rather than the Drum Sampler — useful when you want a kit without sampling anything.
