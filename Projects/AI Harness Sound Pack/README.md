# AI Harness Sound Pack

Twenty short UI cues — pings, mentions, done, question, error, the milestone
"da-ding" family, and a fireworks hero cue — designed as coherent sound families for
the AI harness, plus the research and the production plan to record them properly on
the rig this repo already documents.

## What's here

| File | What it is |
|---|---|
| `01-Research-Notification-Sound-Design.md` | How Slack, Apple, Google, and Microsoft design notification sounds — the findings this pack is built on |
| `02-Sound-Spec.md` | The 20 cues: semantic grammar, pitch, timing, loudness tiers, delivery targets |
| `03-Production-Plan.md` | The personalized plan to produce release-quality versions on the existing rig (Logic + Apollo x8 + Komplete/Arturia + iZotope) |
| `04-Game-Sound-Inspiration.md` | What Risk of Rain, Halo, Zelda, and Mario teach the palette; the milestone da-ding family; pedalboard "mangling skins" |
| `05-Families-Roadmap.md` | The swappable-family system: Tiobi (ships), fun cut, video game and movie skins, and The Declan (in-house only) |
| `prototypes/` | 24 audible WAV prototypes + `render_prototypes.py` (pure Python, no deps) + `manifest.json` (family-tagged) |

## The one-paragraph version

Every big-company notification family works the same way: **one timbre, one key, under
one second, meaning carried by pitch direction instead of loudness.** This pack speaks
D major pentatonic in a warm struck-bell voice. Rising = incoming/attention. Falling
and resolving = done/outgoing. Low and damped = something's wrong — and the error sound
is deliberately *quieter* than the ping. The prototypes are audition-ready today; the
production plan re-voices them with sampled and hardware instruments already in the
studio, masters them to tiered loudness, and ships WAV + OGG/M4A with the manifest.

## Regenerate the prototypes

```
cd prototypes && python3 render_prototypes.py
```
