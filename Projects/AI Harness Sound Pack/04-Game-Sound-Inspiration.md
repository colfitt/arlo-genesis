# Game Sound Inspiration — reward audio, and how to steal it legally

Video games are the deepest tradition of reward sound design there is: players hear
the same cues thousands of times and still love them, which is exactly the fatigue
problem a harness faces. This doc maps the famous game cues worth learning from onto
our palette, and then covers the fun part — mangling the clean family through the
pedalboard to make themed "skins."

## The rule first: steal the gesture, never the sound

The recordings themselves are copyrighted, and the most famous ones function as
sonic trademarks. Sampling a Halo or Risk of Rain sound into a commercial product is
off the table — but the *gesture* (contour, rhythm, structure, physics, emotional
shape) is not protectable and is exactly what's worth taking. Our `fireworks` cue
copies the physics of a firework — launch, burst, crackle, falling embers — not
anybody's recording of one. That's the pattern for everything below.

## The map

| Game cue | What makes it great | What it teaches our palette |
|---|---|---|
| **Risk of Rain 2 — Fireworks item** | Objectives celebrated with a salvo of actual fireworks: chaotic, physical, earned | The `fireworks` hero cue: launch riser → burst → crackle → pentatonic embers. Celebration through physics, not fanfare |
| **Halo — Grunt Birthday Party** | Headshots become confetti + a children's cheer. Absurd joy as an *opt-in skin* on a standard event | Skins (below): the same cue can wear a celebration costume without changing its meaning |
| **Halo — shield recharge** | A rising hum that means "you're safe again" — status change you feel without looking | The `connect` / recovery archetype: restoration reads as a rise |
| **Halo — shield-low alarm** | Iconic, but infamous for grating under repetition | The cautionary tale for `warning`: a caution cue that loops will be hated. Ours fires once, quietly |
| **Zelda — puzzle-solved chime** | The canonical "you got it" arpeggio: rising, then *resolving*. Instantly parseable for 35+ years | The `done` / `done-big` archetype — rise then land. Ours lands on home D for the same reason |
| **Mario — 1-Up** | A fast syllabic run upward. It is, literally, a da-ding-a-ling | Direct validation of the milestone family: syllable count scales with reward size |
| **Metal Gear Solid — the "!" alert** | One sharp stab. Total attention, zero melody | The `mention` archetype: directness is a feature when the event is about *you* |
| **Final Fantasy — victory fanfare** | A full musical phrase — but only after battles, never for menu actions | Hero-tier discipline: the big sound stays rare or it dies. `fireworks` should fire, at most, a few times a week |
| **Peggle — Ode to Joy** | Rainbow + Beethoven on the final peg: the absolute ceiling of celebration, once per level | Where the ceiling is. We stay well under it, but it's useful to know joy maximalism *works* when rationed |
| **Animal Crossing** | A soundscape where nothing punishes; even errors are gentle | Confirms the palette's rule that `error` is quiet and dark, never a buzzer |

## The milestone "da-ding" family, formalized

The document that kicked this off said it perfectly in onomatopoeia — and onomatopoeia
is a legitimate spec language for earcons (designers pitch sounds to each other this
way). The mapping:

| Event | Onomatopoeia | Realized as |
|---|---|---|
| published | *ding* | Single bright D6 |
| signed off | *happy da-DING* | A5 pickup → D6, the ding earns a syllable |
| phase advancing | *joyful da-DING-a-LING* | A5 → D6 → E6 → F#6 rising run over a warm floor |
| space complete | *sad ding* | One D5 bell that droops a minor third to B4 as it decays — closure with wistfulness |

The design law it demonstrates: **within a family, magnitude = syllable count.** Same
voice, same key, same "ding" DNA — a listener who has only heard `published` will
correctly rank `phase-advance` as a bigger deal on first listen. This is the Mario
1-Up / earcon-hierarchy principle (Blattner 1989: families built from a shared motif,
research doc §craft).

## Mangling skins — the pedalboard as sound-design tool

The clean D-pentatonic masters are canon. But the rig this repo documents is a
world-class mangling chain, and running the finished cues through it yields themed
variant packs — the way Pixel ships sound families and Halo ships the Birthday Party
skull. Reamp via the Radial X-Amp from the Apollo, print at 96k, master to the same
loudness tiers:

| Skin | Chain | Character |
|---|---|---|
| **Tape** | Strymon Deco V2, low drive → wow/flutter | Rounded, warm, slightly unstable — the "calm" skin |
| **Lo-fi / Arcade** | Goodhertz Lossy or Generation Loss MkII | Codec artifacts and bitcrush — the retro-game skin |
| **Granular** | Hologram Microcosm / Chase Bliss Blooper | Stuttered, shimmering micro-variants — also an anti-fatigue variant farm: one pass yields 10 usable takes of `ping` |
| **Bloom** | Strymon Big Sky shimmer, ~15% wet | Hero cues only (`fireworks`, `done-big`) — adds occasion |
| **Speakerphone** | Play cues out the OP-1 Field speaker, re-record with its mic | Instant nostalgia-hardware character, genuinely useful for testing small-speaker survival too |

Ship the clean family as the default theme, one skin as an alternate, and let users
pick — sound themes are cheap delight, and no AI product currently offers them.

## Harness hooks worth copying from games

- **Rarity budget:** games meter their biggest sounds by making them expensive to
  trigger. Give `fireworks` an actual cooldown in the harness (e.g., once per day max).
- **Streak escalation:** Duolingo/arcade combo logic — the Nth consecutive `done` in a
  session could climb one scale degree, resetting daily. Cheap to implement (pitch
  offset on playback), huge charm.
- **Reactive mixing:** games duck UI sounds under dialogue; the harness should skip
  Tier 2/3 cues entirely while the user is in a voice session.
