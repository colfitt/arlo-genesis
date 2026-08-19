# Sound Spec — the 15 cues

The whole pack is **one instrument speaking one language**. Every cue is built from the
same struck-bell/kalimba voice, lives in D major pentatonic (with one deliberate
exception), and says what it means through interval direction, not through volume.

## The grammar

| Direction | Meaning | Cues that use it |
|---|---|---|
| Rising interval | Incoming / needs your attention | ping, mention, message-in, question, connect, approve, start |
| Falling, resolving to D | Completion / outgoing / closing | done, done-big*, message-out, disconnect, deny |
| Low + damped + dark | Something is off (never harsh, never loud) | error, warning, deny |
| Single tiny tick | Ambient state, felt not heard | progress |

*done-big rises to the octave but lands on D — it resolves home emphatically rather
than falling.

Three hard rules, straight from the research (see `01-Research-Notification-Sound-Design.md`):

1. **Attention is earned by pitch shape, not loudness.** The error sound is *quieter*
   than the ping. Nobody should ever be startled by a failure.
2. **Under one second, always.** Longest cue (done-big) is 0.9 s; most are 0.4–0.6 s.
3. **The 100-times test.** Every cue must survive being heard 100 times in a row and
   layered over speech/music. Anything that develops an edge gets softened.

## The 15 cues

| # | Cue | Meaning in the harness | Notes / shape | Length | Rel. peak |
|---|---|---|---|---|---|
| 1 | `ping` | Generic notification | Single **A5**, bright bell | 0.42 s | −3 dB |
| 2 | `mention` | You were named / DM'd | **D5 → A5** rising fifth, quick | 0.55 s | −3 dB |
| 3 | `message-in` | Message arrived (ambient) | **E5 → F#5** gentle step up, soft timbre | 0.45 s | −6 dB |
| 4 | `message-out` | Message sent | **F#5 → D5** quick falling step | 0.40 s | −9 dB |
| 5 | `question` | Agent needs your input | **D5 → F#5 → B5**, ends *unresolved* — the musical question mark | 0.70 s | −3 dB |
| 6 | `done` | Task complete | **A5 → D5**, settles home with a warm tail | 0.70 s | −4 dB |
| 7 | `done-big` | Long job / build finished | **D5 → A5 → D6** flourish + F#6 sparkle + D4 floor | 0.90 s | −3 dB |
| 8 | `error` | Failure | **D4 + E♭4** minor-second rub, dark damped timbre — the palette's only dissonance | 0.50 s | −6 dB |
| 9 | `warning` | Caution, non-fatal | Single muted **F4** with slow vibrato | 0.46 s | −7 dB |
| 10 | `start` | Task / agent kicked off | Glide **A4 ↗ D5** with an octave lift — "lift-off" | 0.46 s | −6 dB |
| 11 | `progress` | Milestone tick | Tiny wooden **D6** blip | 0.13 s | −12 dB |
| 12 | `connect` | Session / agent online | **D5 → D6** octave up | 0.55 s | −6 dB |
| 13 | `disconnect` | Session ended | **D6 → D5** the same octave, coming down | 0.52 s | −8 dB |
| 14 | `approve` | Permission granted / confirm | **F#5 → A5** quick bright "mm-hm" | 0.42 s | −4 dB |
| 15 | `deny` | Permission declined / cancel | **A4 → F4** soft low falling third — a no, not a slap | 0.48 s | −7 dB |

Paired cues are deliberate mirrors, so the ear learns them for free:

- `connect` / `disconnect` — the same octave, up vs. down
- `approve` / `deny` — bright-rising vs. dark-falling
- `message-in` / `message-out` — step up vs. step down
- `question` / `done` — unresolved vs. resolved

## Loudness tiers

Peak normalization targets in the prototypes (production masters get a proper LUFS
pass — see the production plan):

- **Tier 1, interrupt (−3 to −4 dBFS peak):** ping, mention, question, done-big, done, approve
- **Tier 2, inform (−6 to −8 dBFS):** message-in, error, warning, start, connect, deny, disconnect
- **Tier 3, ambient (−9 to −12 dBFS):** message-out, progress

## Technical targets

| Property | Prototype | Production master |
|---|---|---|
| Format | WAV, 48 kHz / 16-bit, mono | WAV, 48 kHz / 24-bit (record at 96 k), mono-summed stereo |
| True peak | per-tier, ≤ −3 dBTP | ≤ −3 dBTP after limiting |
| Loudness | peak-tiered | tier-matched by ear + LUFS-S check, error/warning always below ping |
| Onset | 4 ms soft attack (no clicks) | keep attack ≥ 3 ms; de-click tails |
| Low end | fundamental ≥ D4 (294 Hz) | high-pass 150 Hz — cues must survive laptop + phone speakers |

## Accessibility

- Sound is **never the only channel** — every cue mirrors a visual state in the harness.
- Fundamentals sit between 294 Hz and 1175 Hz, the band that survives small speakers
  and mild high-frequency hearing loss (research doc, accessibility section).
- Tiers let users scale "interrupt" cues independently of ambient ones; a
  reduced-motion-style "minimal sounds" mode should keep only mention, question, error.

## Prototypes

`prototypes/render_prototypes.py` renders all 15 deterministically (pure Python
stdlib, no dependencies) and writes `manifest.json` for the harness to consume.
Audition them side by side before re-voicing anything in production.
