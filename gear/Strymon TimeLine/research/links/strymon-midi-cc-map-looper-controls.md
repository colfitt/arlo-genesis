https://midi.guide/d/strymon/timeline/  +  https://www.strymon.net/faq/what-are-the-midi-controls-for-the-timeline-looper/
midi.guide (community CC dump) + strymon.net (official looper FAQ) · verified cross-source

The complete, verified TimeLine MIDI CC map. Useful because the Digitakt-2-clocked rig may MIDI-control the TimeLine in failover. CC numbers cross-checked between the community midi.guide dump and Strymon's official looper FAQ — they agree.

## Main knobs (CC)
| Param | CC |
|---|---|
| TIME | 3 |
| REPEATS | 9 |
| MIX | 14 |
| FILTER | 15 |
| GRIT | 16 |
| SPEED | 17 |
| DEPTH | 18 |

(VALUE/fine-time and the per-machine params have their own CCs/NRPNs — see the manual MIDI spec, p.24–25.)

## Control functions (CC)
| Function | CC |
|---|---|
| TAP TEMPO (tap footswitch) | 81 |
| EXPRESSION pedal | 100 |
| BYPASS (engage/bypass) | 102 |
| Preset recall | Program Change (PC), 200 presets over 2 MIDI banks: Bank0 = 00A–63B, Bank1 = 64A–99B |

## Looper functions (CC) — official Strymon FAQ
| Function | CC |
|---|---|
| Record | 87 |
| Play | 86 |
| Stop | 85 |
| Undo (to initial loop) | 89 |
| Redo | 90 |
| Reverse (toggle) | 94 |
| Full/Half Speed (toggle) | 95 |
| Pre/Post (toggle) | 96 |
| Looper Level | 98 (range 0–17) |

(Note CCs also exist as alternatives to all looper functions.)

## VERIFICATION / honesty flags
- **No dedicated CC for "infinite repeats" / "hold."** A circulating claim that "CC#97 = infinite repeats" is **NOT confirmed** by either the official looper FAQ or the midi.guide dump. Infinite repeats is a **footswitch-HOLD** behavior, not (confirmed) a CC. Treat CC#97 as unverified until tested on the unit or found in the manual MIDI spec.
- Older firmware-era docs listed Reverse=103 / Half-Speed=104 as "absolute" looper commands (added v1.42); the current FAQ uses 94/95 toggles. If MIDI looper control misbehaves, check firmware-era CC mismatch.
