# ARLO — Genesis Kit

A fresh-start kit for building **ARLO**: a music-production AI partner that runs on *your own* gear, software, and knowledge.

## The one-line goal

> Use the seed data I already have — my gear, my software, my songwriting/production knowledge — **with `claude`, correctly**, so ARLO answers as a partner who knows my actual rig and taste.

This kit exists so the project can be **started again from zero** without re-deriving any context. Everything an engineer (or a future Claude session) needs to rebuild is here.

## How to use this kit

Read in order. Each file stands alone but they build on each other:

| File | What it answers |
|------|-----------------|
| [01-VISION.md](01-VISION.md) | What ARLO is, and the real need behind it |
| [02-USE-CASES.md](02-USE-CASES.md) | The concrete workflows ARLO must support |
| [03-SEED-DATA.md](03-SEED-DATA.md) | The asset you already have (gear / software / arlo corpus) and its formats |
| [04-USING-IT-WITH-CLAUDE.md](04-USING-IT-WITH-CLAUDE.md) | **The crux** — how to make `claude` use the data well (recommended approach) |
| [05-UI-DIRECTION.md](05-UI-DIRECTION.md) | The UI you want (odysseus as reference), kept separate from the engine |
| [06-BUILD-PLAN.md](06-BUILD-PLAN.md) | Phased local stand-up |
| [07-RISKS-OPEN-QUESTIONS.md](07-RISKS-OPEN-QUESTIONS.md) | Honest unknowns, including whether odysseus fits |

## Mental model in one diagram

```
        YOUR SEED DATA (already exists)            ARLO ENGINE                 UI (later)
  ┌─────────────────────────────────────┐    ┌──────────────────┐      ┌──────────────────┐
  │ Pedalxly/Gear     (44 devices)       │    │  claude +        │      │ odysseus-like    │
  │ Pedalxly/Software (18 vendors)       │──▶ │  ARLO persona +  │ ──▶  │ workspace        │
  │ patchbay-ai/arlo  (corpus, taste,    │    │  skills + retrieval     │ (chat + sidebar  │
  │                    workflows)        │    │  over the folders)│     │  + documents)    │
  └─────────────────────────────────────┘    └──────────────────┘      └──────────────────┘
       the moat (portable markdown)            the thing to get right         the nice-to-have
```

**Key separation this kit insists on:** the *engine* (claude using your data correctly) is the hard, valuable part. The *UI* (odysseus-style) is a layer on top and can wait. Don't let the UI choice block the engine.

## Provenance

This kit was synthesized from the prior `patchbay-ai` planning (`.planning/PROJECT.md`, roadmap), a direct read of the three seed-data folders, and an evaluation of `pewdiepie-archdaemon/odysseus`. The prior Tauri `patchbay-ai` app is **reference only** — see [05-UI-DIRECTION.md](05-UI-DIRECTION.md).

*Created 2026-06-03.*
