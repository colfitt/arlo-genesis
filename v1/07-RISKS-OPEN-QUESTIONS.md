# 07 — Risks & Open Questions

Honest unknowns. The point of a restart kit is to not relearn these the hard way.

## Risks

### R1 — "Can odysseus even do what I want?" (your own doubt, and mine)
odysseus is a **general, horizontal** self-hosted AI workspace (chat/agent/email/calendar/RAG), **Python web stack**, **brand-new** (created 2026‑05‑31), large surface (its own `THREAT_MODEL.md`). Its **UI** is close to what you want; its fit as the **engine** for a focused, gear-grounded music partner is **unproven**. → Mitigation: treat it as **UI reference**, prove the engine independently ([04](04-USING-IT-WITH-CLAUDE.md)), and **timebox a spike** (Option 3 in [05](05-UI-DIRECTION.md)) before committing.

### R2 — Context-window vs corpus size
`chunks.jsonl` is 5.6 MB; profiles + research are hundreds of files. Dumping into a prompt won't work. → Mitigation: retrieval-first ([04](04-USING-IT-WITH-CLAUDE.md) B/C); never inline the corpus.

### R3 — Absolute-path coupling
The seed folders are at machine-specific absolute paths (`/Users/cfitt/Dev/...`). Hardcoding spreads brittleness. → Mitigation: one config file (Phase 0); symlinks under `data/`.

### R4 — Persona drift / "shaping project"
ARLO's `CLAUDE.md` persona is iterative by your own framing. Risk: it bloats or contradicts itself over time. → Mitigation: keep `CLAUDE.md` tight; the persona toggle lets you A/B against raw claude; version it in git.

### R5 — Grounding vs hallucination
The whole value is "uses *my* data, not generic advice." If retrieval misfires, ARLO sounds confident but ungrounded. → Mitigation: enforce the **citation rule** (claims link to a file); make "falling back to generic" explicit in answers.

### R6 — Stack fragmentation
Two reference stacks exist (odysseus = Python/web; old patchbay-ai = Rust/Tauri). Picking by UI-look alone could saddle you with the wrong engine stack. → Mitigation: engine is stack-agnostic markdown + claude; choose UI stack last, after the spike.

### R7 — Seed-data integrity is the moat
If the markdown/frontmatter gets messy (3 gear folders already lack `GearProfile.md`), grounding degrades. → Mitigation: a lightweight validator; treat profiles as a schema; backfill missing profiles.

## Open questions (answer early)

1. **UI scope** — does the UI need music-specific surfaces (skeleton grid, patch editor, gear drawer — the Tauri prototype), or is **chat + gear sidebar + documents** (odysseus) enough? *(The pivotal UI question — [05](05-UI-DIRECTION.md).)*
2. **Project home** — same dir as this kit, or a sibling? (Phase 0.)
3. **Songs** — there's currently no songs/studio data source. Where do songs live, and are they in-scope for v1 or deferred?
4. **Local model vs API** — ARLO via the `claude` CLI/API, or also local models (odysseus's Cookbook)? Affects privacy and the engine.
5. **Persona definition** — does `arlo/` need an explicit `CLAUDE.md`/persona doc authored from the taste-profile + workflows, or is the persona defined in the new home's `CLAUDE.md` only?
6. **Seeding budget** — firing the AESTHETIC + ALBUMS corpus dispatchers is real token/time spend. How much to seed before building UI?

## What is NOT at risk (the durable core)

- The **seed data** exists and is portable markdown — engine/UI choices can change without losing it.
- The **engine approach** ([04](04-USING-IT-WITH-CLAUDE.md)) works with the `claude` CLI today; it doesn't depend on odysseus or any UI.
- The **vision and use-cases** ([01](01-VISION.md)/[02](02-USE-CASES.md)) are stable targets regardless of how it's built.
