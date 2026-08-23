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
| **The Terminal** | 6-cue teaser prototyped | shippable candidate | Telecom/hacker aesthetic built from first-principles synthesis (DTMF, POST beeps, Morse, squelch, modem handshake) — the crate rips stay in-house as references; the family ships original. Full roster in `06-Hacker-Sample-Crate.md` |

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

## Family concept rosters

Full cue-by-cue concepts for the planned families. Every family speaks the same
grammar (rising = attention, falling-resolving = done, low/damped = trouble, magnitude
= syllable count) in its own vocabulary — that's what keeps a swapped theme instantly
legible. All concepts are original sounds to synthesize or record ourselves.

### The Declan — full roster (in-house only; everyday absurd foley)

| Cue | Concept |
|---|---|
| ping | single knuckle knock on wood |
| mention | *duunn… dun* — two ominous low notes ✅ prototyped |
| message-in | creaky screen door opening |
| message-out | letter dropped into a mail slot — *shunk* |
| question | confused dog whine — *hrrn?* |
| done | microwave *DING* (dinner's ready) |
| done-big | bowling strike, full pin explosion |
| error | doppler fire truck driving past your build ✅ prototyped |
| warning | kettle just starting to whistle |
| start | lawnmower pull-cord — catches on the first pull, obviously |
| progress | one popcorn pop |
| connect | dial-up modem handshake (0.5 s micro-cut) |
| disconnect | CRT television powering off — *bwoop* |
| approve | celebratory gunfire (party-popper salvo) ✅ prototyped |
| deny | sad trombone — *womp womp* |
| merge/`done` variant | toilet flush ✅ prototyped |
| published | newspaper hitting the porch — *thwap* |
| signed-off | rubber stamp — *THUNK* |
| phase-advance | elevator ding + doors sliding open |
| space-complete | balloon slowly deflating |
| hero (fireworks) | champagne cork + fizz + a small crowd going *heyyy* |

### The Movie — cinematic trailer language (skin; possible alt theme)

Palette: sub-booms, risers, braams, short orchestral gestures, projector foley.
Big Sky bloom on the tails per the mangling recipes.

| Cue | Concept |
|---|---|
| ping | miniature whoosh-hit — a trailer boom at 1% scale |
| mention | two-note French horn call — you are summoned |
| message-in | projector flicker + soft whoosh arriving |
| message-out | whoosh departing, doppler tail |
| question | string tremolo swell ending on an unresolved high harmonic |
| done | timpani roll into one warm resolving orchestral hit |
| done-big | title-card moment: short braam + choir swell |
| error | low detuned piano cluster with a dark reverb tail (quiet) |
| warning | single tense cello stab |
| start | white-noise riser into a soft downbeat |
| progress | one film-reel sprocket click |
| connect | projector motor spin-up, first frame of light |
| disconnect | projector spin-down, film end flapping |
| approve | quick major-chord swell — the plan works |
| deny | soft minor micro-braam |
| published | clapperboard — *action!* |
| signed-off | the double clap — that's a wrap |
| phase-advance | act-break sting: three ascending orchestral hits |
| space-complete | single end-credits piano note, long tail |
| hero (fireworks) | an original studio-logo fanfare, 1.5 s |

### The Video Game — chiptune/arcade (skin; possible alt theme)

Palette: square/triangle waves, fast arpeggios, bitcrush — the Tiobi pentatonic
grammar spoken in 8-bit. Also producible by mangling Tiobi masters through
Lossy/Generation Loss.

| Cue | Concept |
|---|---|
| ping | one square-wave blip |
| mention | two-note rising square call |
| message-in | item-get sparkle: fast three-note arp up |
| message-out | laser *pew* downward |
| question | NPC text-scroll blips ending on a high one — *blip-blip-blip?* |
| done | quest-complete arpeggio, rising then resolving |
| done-big | level-clear fanfare: fast run + chord |
| error | short damage buzz with a pitch drop (soft, never harsh) |
| warning | ONE low-health beep — it does not loop (the Zelda lesson) |
| start | ready-go countdown blip pair |
| progress | XP tick |
| connect | power-up rising sweep |
| disconnect | power-down falling sweep |
| approve | coin ding |
| deny | soft buzzer *bzzt* |
| published | checkpoint chime |
| signed-off | save-game jingle: two notes + sparkle |
| phase-advance | level-up run — the da-ding-a-ling in chiptune |
| space-complete | slow descending arp, wistful |
| hero (fireworks) | boss-defeated fanfare with bitcrushed firework pops |

### The Fun Cut — tastefully cut fun version (in-house)

Palette: human and toy sounds — whistles, snaps, mouth pops, toy piano, bicycle
bell — recorded on the SM57/OP-1 Field mic. Playful but still short, quiet, and
tiered: fun in the timbre, manners intact.

| Cue | Concept |
|---|---|
| ping | finger snap |
| mention | two-tone "hey, over here" whistle |
| message-in | cheek pop |
| message-out | short *pff* blow |
| question | rising *hm?* whistle |
| done | toy piano, two notes resolving |
| done-big | tiny kazoo fanfare (one second, tasteful, somehow) |
| error | tongue *tsk* + low toy-piano thunk |
| warning | mechanic's inhale through teeth — *ssss* |
| start | short slide whistle up |
| progress | single tongue click |
| connect | two glasses clinking |
| disconnect | reverse cork pop |
| approve | bicycle bell *ding!* |
| deny | playful two-note *uh-uh* hum |
| published | typewriter carriage return + ding |
| signed-off | pen scribble + decisive tap — the signature flourish |
| phase-advance | three ascending whistle notes |
| space-complete | contented sigh, pitched down a touch |
| hero (fireworks) | party horn + confetti shaker |

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
