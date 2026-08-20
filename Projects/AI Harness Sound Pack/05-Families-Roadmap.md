# Families Roadmap — what ships, what stays in-house, and how they swap

The pack is growing from one sound set into a system of **swappable families**: every
family implements the same cue IDs (`ping`, `mention`, `done`, `error`, …), so the
harness swaps a whole personality by pointing at a different family — the way Pixel
ships themed sound packs and Halo ships the Grunt Birthday Party skull.

## The families

| Family | Status | Audience | Description |
|---|---|---|---|
| **Tiobi** | prototyped (the current D-pentatonic bell kit) | ships with the open source product | The default voice: warm struck-bell, semantic grammar, tiered loudness. Everything in `02-Sound-Spec.md` |
| **Fun cut** | planned | in-house | A tastefully cut fun version of Tiobi — same cues, more play, still restrained enough for daily use |
| **Video game** | planned | in-house → possibly shipped as an alt theme | The arcade/lo-fi skin: Tiobi masters mangled through Lossy / Generation Loss (recipes in `04-Game-Sound-Inspiration.md`) |
| **Movie** | planned | in-house → possibly shipped as an alt theme | The cinematic skin: risers, sub-weight, Big Sky bloom tails — trailer-grade `done-big` and `fireworks` |
| **The Declan** | prototyped | **in-house only, never ships** | See below |

*(Assumption: "Tiobi" is the product/family name — rename here and in the manifest if
that's off.)*

## The Declan

The office family. Caricatures, synthesized from scratch, prototyped in
`prototypes/declan-*.wav`:

| Cue | Sound |
|---|---|
| `approve` | celebratory gunfire (rendered as a party-popper salvo with a confetti glint — festive, not literal) |
| `mention` | two ominous low semitone notes… something approaches (*duunn… dun*) |
| `error` | doppler-effect fire truck — the siren pitches down as it drives past your build |
| `merge` | toilet flush — whoosh, three descending glugs, drain tail. The PR is gone now |

**Why it never ships:** the mention cue is a two-note caricature in the direction of a
famous film motif. Synthesized in-house for laughs at our own desks: negligible risk.
Distributed in an open source product: a recognizability problem we've already decided
not to have (see the legal lines in `04-Game-Sound-Inspiration.md` — method doesn't
matter, recognizability does). Same logic keeps every joke family internal.

## How families swap

The mechanism is already half-built: `prototypes/manifest.json` now tags every cue
with a `family` field. Target layout for the production repo:

```
sounds/
  manifest.json          # lists families + cue IDs + per-cue metadata
  tiobi/    ping.wav mention.wav ... (ships)
  arcade/   ping.wav mention.wav ... (optional theme)
  declan/   ...            (internal directory, excluded from release builds)
```

Harness contract:
- Every family implements the **same cue IDs**; missing cues fall back to Tiobi.
- The active family is a user setting (`sound_theme: "tiobi"`); loudness tiers and
  the rate-limit/cooldown rules apply identically to every family, so a theme can
  change the costume but never the manners.
- Release packaging excludes internal families by an `internal: true` flag in the
  manifest — the joke families physically can't leak into a build.

## Full cue inventory so far (24 prototypes)

- **Tiobi core (15):** ping, mention, message-in, message-out, question, done,
  done-big, error, warning, start, progress, connect, disconnect, approve, deny
- **Tiobi milestones (4):** published, signed-off, phase-advance, space-complete
- **Tiobi hero (1):** fireworks
- **Declan (4, internal):** declan-approve, declan-mention, declan-error, declan-merge
