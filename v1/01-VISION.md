# 01 — Vision

## What ARLO is

**ARLO is a music-production partner you talk to.** It knows your actual rig (every pedal, synth, interface, and plugin you own), it knows production/songwriting craft (a curated knowledge corpus + your taste profile), and it helps you **set up songs** — structure, signal chains, gear/patch choices, workflow — so you can get to making music faster.

ARLO is **the `claude` profile for how *you* make music.** Same Claude underneath; the difference is the persona, the data it can reach, and the discipline of how it uses both.

## The real need (why this kit exists)

You **already have the hard part**: a large, hand-curated body of seed data — gear research, software inventory, a production/aesthetic corpus, songwriting workflows, and a taste profile. What's missing is the *engine*: a reliable way to **use that data inside `claude` correctly**, so ARLO's answers are grounded in *your* gear and *your* taste rather than generic advice.

So the project is not "build an app." It is: **wire the seed data into `claude` so ARLO is real**, then (optionally) put a nice UI on it.

## Core value

> You ask ARLO a music question and it answers as someone who has read your gear's manuals, knows which pedals you own, understands the production techniques in your corpus, and shares your taste — with citations back to the source.

If everything else falls away, *this grounded-conversation loop* is the product.

## Principles (carried forward, still locked)

These come from the prior project and remain true regardless of engine/UI:

- **Honest tool.** ARLO sets up structure and gear/control; the human makes the music. No fake authorship, no pretending to play. Composition/melody generation stays off by default.
- **Markdown is canonical.** The seed data is portable markdown + frontmatter. Any engine reads it; no engine "owns" it. This keeps the moat engine-agnostic.
- **Provenance matters.** Instructional claims should be traceable to a source (a manual, a corpus chunk, a gear profile). The corpus (`chunks.jsonl`) exists for exactly this.
- **Gear is instructional, never simulated.** Third-party hardware/plugin internals are described, not faked. ARLO tells you how to dial it in; it never renders fake knob state.
- **Your data, local-first.** Runs on your hardware against your folders. No dependency on a hosted service to deliver core value.

## What changed from the prior plan

The prior `patchbay-ai` was a bespoke **Tauri (Rust + React) desktop app** with an embedded `claude` terminal and reactive panels. That app was built to the design prototype and works visually — but the new direction is a **fresh start centered on the engine** (claude + seed data) rather than the bespoke shell. The Tauri app and its design are now **visual reference**, not the foundation. See [05-UI-DIRECTION.md](05-UI-DIRECTION.md).

## Non-goals (for the fresh start)

- Not building a general AI workspace (email, calendar, etc.). ARLO is a *music* partner.
- Not generating music/lyrics by default.
- Not committing to a specific UI before the engine proves out.
- Not re-deriving the seed data — it exists and is the asset.
