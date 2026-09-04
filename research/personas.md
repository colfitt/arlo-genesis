# ARLO — Target Personas

*Synthetic personas for product/marketing targeting. All people, names, and
backgrounds below are fictional. They are grounded in what ARLO actually is
(see [`v1/01-VISION.md`](../v1/01-VISION.md) and [`v2/README.md`](../v2/README.md))
and in the real gear/software library this repo is shaped around.*

---

## Who ARLO is for, in one line

A **taste-driven musician with a boutique hardware+software rig and a recall
problem** — someone who has enough gear that "what did I *do* to get that
sound?" is a real, recurring pain, who works local-first on a Mac, and who
wants a partner that knows *their* rig and *their* taste rather than generic
advice.

## Segment map

| # | Persona | Segment | Priority | Core job-to-be-done |
|---|---------|---------|----------|---------------------|
| 1 | Maya Okafor | Ambient gear-hoarder / bedroom producer | **Primary** | "Never lose a sound I stumble into again." |
| 2 | Deacon Reyes | Gigging / worship guitarist (live) | **Primary** | "Flip my whole rig, song to song, without tap-dancing or fear." |
| 3 | June Park | Hybrid singer-songwriter (mk.gee-core) | **Primary** | "Set the song up fast so I can get to writing." |
| 4 | Ori Halvorsen | Synth sound-designer / composer | Secondary | "Recall a patch *exactly*, and organize hundreds of them." |
| 5 | Marcus "Fitz" Fitzgerald | Privacy-conscious tinkerer-dev musician | Secondary | "A tool I own, can trust in the signal path, and can extend." |
|   | *Anti-persona* | Beginner / pure-ITB / "write my song for me" | **Not for** | — |

---

## 1. Maya Okafor — *"The board is a museum of forgotten settings."*
**PRIMARY**

- **34, Portland OR.** Senior product designer at a mid-size SaaS company; music is
  the serious hobby that keeps her sane.
- **Rig:** ~30 pedals on a too-big board — Chase Bliss Blooper, MOOD MkII, Generation
  Loss, Brothers; Strymon Big Sky + TimeLine; Hologram Microcosm; OP-1 Field;
  Digitakt 2; RME Babyface Pro FS into a Mac Studio. Ableton Live + Valhalla.
- **Aesthetic:** ambient / electro-acoustic drift — Grouper, Bon Iver, Hainbach,
  early Tim Hecker. Long evolving textures, tape wobble, granular clouds.

**A day in the life.** She gets 90 minutes after dinner. She patches the Blooper
into the Microcosm, tweaks for 40 minutes, and around 1am something *gorgeous*
happens — a specific stack of overdubs and a filter sweep she'll never
reconstruct. She hums "I'll remember it," powers down, and by Thursday it's gone.
Her Voice Memos are full of beautiful fragments attached to no settings.

**Goals.** Finish things. Build a library of *her* sounds she can recall and reuse.
Stop re-buying the same discovery.

**Frustrations / pains.**
- **Patch amnesia** — the #1 pain. No memory of what created a sound.
- Boutique pedals with deep menus and no screens; state lives in her head.
- Analysis paralysis — 30 pedals, and she uses the same 4 out of habit.
- Guilt: more gear than finished tracks. *(DOUG would ask if she finished a track
  before buying that next pedal.)*

**Why ARLO.** A **scene** captures the synth patch + every pedal's preset + the
controller state as one recallable markdown artifact. She can fire "that 1am
thing" back byte-identical. And she can *ask* — "what did I have the Blooper doing
on the drone from last week?" — and get an answer grounded in her actual rig.

**What makes her bounce.** If setup is fiddly, if it feels like homework, or if it
can't see her specific pedals. She has zero patience for another tool that adds
friction to a fragile creative window.

**Closing feature:** instant, byte-identical scene recall + "ask about my own rig."

---

## 2. Deacon Reyes — *"I can't be scared of my own pedalboard mid-song."*
**PRIMARY**

- **29, Nashville TN.** Plays guitar for a large church (3 services/weekend) plus
  session and fill-in touring work. Semi-pro; the rig has to *work*.
- **Rig:** Eventide H90, Strymon TimeLine + Big Sky, Strymon Iridium (amp-less),
  Novation 61SL MkIII, MacBook Pro running Ableton for tracks/pads. UAFX Del-Verb.
- **Aesthetic:** modern worship / cinematic post-rock — big ambient swells, U2-ish
  delays, pad-under-everything. Reliability over novelty.

**A day in the life.** Setlist drops Thursday, 6 songs. Each wants different
delay times, a different Iridium cab, a different pad patch, sometimes a controller
remap for volume swells. Right now that's a page of hand-written preset numbers
taped to his board and a lot of tap-dancing between songs — and one wrong stomp
sends a Program Change into the wrong place and eats a cue.

**Goals.** One button per song. Silent, instant switching. Never have a live
surprise. Build the set Thursday, trust it Sunday.

**Frustrations / pains.**
- Song-to-song recall across pedals + synth + controller is manual and fragile.
- Terrified of a stray message nuking a looper/session mid-service.
- Cloud tools are a non-starter on a stage — latency and "is the wifi up?" risk.
- Wants a **dry run** at soundcheck that changes nothing.

**Why ARLO.** `POST /api/scene/fire` flips synth + pedals + controller in **one
call**. **Every fire is dry-runnable** — he can preview every step at soundcheck
with zero bytes on the wire. And the engine **reserves Channel 16** for the
controller session *in code* — a stray PC literally cannot flip his looper. Recall
onto a warm instance is 12–24 ms, so switches feel instant. **No cloud in the
signal path.**

**What makes him bounce.** Any flakiness. One dropped scene on a Sunday and he's
out. He needs the guardrails to be real, not promises in a prompt.

**Closing feature:** one-call scene firing + dry-run + the "refuse, don't clamp"
guardrails.

---

## 3. June Park — *"I don't want it to write my song. I want it to hand me the studio, set up."*
**PRIMARY**

- **26, Brooklyn NY.** Self-producing artist, part-time barista, releasing to
  Bandcamp/streaming. DIY to the bone.
- **Rig:** Strymon Iridium + Deco, Chase Bliss Lost & Found, UA Apollo x8, a
  reamp box, Logic Pro, Auto-Tune, Soundtoys. DI-in / reamp-out guitar weirdness.
- **Aesthetic:** the modern hybrid stack — mk.gee DI-guitar haze, Bon Iver vocal
  layering, Charli XCX maximalist sound design, a little Dijon looseness.

**A day in the life.** She has a chord loop and a mood. She *knows* she wants that
"reamped-through-the-Deco, doubled, pitched-up-third" mk.gee thing — but rebuilding
the signal chain and remembering which reverb/plugin combo got her there last time
burns the first hour, and the idea cools. She wants to name the vibe and have the
setup appear.

**Goals.** Compress the setup gap between *idea* and *tracking*. Get taste-matched
suggestions from her own gear. Keep authorship 100% hers.

**Frustrations / pains.**
- Setup friction kills momentum — the song dies during signal-chain admin.
- Generic AI tips ("try a reverb!") are useless; she needs *her* chain, *her* refs.
- Deeply allergic to tools that generate the music — that's the whole point of
  making it. She wants a **partner, not a ghostwriter**.

**Why ARLO.** ARLO's core loop is exactly this: *"set up songs — structure, signal
chains, gear/patch choices, workflow — so you can get to making music faster,"*
grounded in her library and taste, with citations back to source. And it's an
**honest tool by design** — composition/melody generation is off by default. It
sets the table; she plays.

**What makes her bounce.** If it feels like a generic AI wrapper, or if it ever
tries to write the part for her, she's gone — it violates the one principle she
cares about.

**Closing feature:** grounded "set up this song" that respects her authorship.

---

## 4. Ori Halvorsen — *"'Close enough' recall is not recall."*
**SECONDARY**

- **41, Oslo, Norway.** Freelance film/game composer working from a treated home
  studio. Deadlines, revisions, and *lots* of saved sounds.
- **Rig:** Arturia V Collection 11 (Prophet-5 V, CS-80 V, etc.), NI Komplete/Kontakt,
  Novation 61SL MkIII, Apollo interface. Mostly in-the-box synths, some outboard.
- **Aesthetic:** hybrid orchestral-electronic score work — evolving pads, analog-modeled
  leads, sound design for picture.

**A day in the life.** A director asks to bring back "the pad from cue 14, but
darker." He needs the *exact* patch state — not a param readout he has to trust,
not a preset that's 90% there. He's been burned by hosts that send Program Change
into a plugin and land somewhere subtly wrong. He wants to design in the plugin's
real editor while audio stays live, save, wreck, and get it back *identically*.

**Goals.** Perfect recall he can stake a deadline on. Organize hundreds of patches
into scenes he can retrieve by name and vibe.

**Frustrations / pains.**
- Plugin recall integrity — needs the **opaque state chunk**, not PC-into-a-plugin.
- Hundreds of sounds, weak organization; "where's that one?" tax.
- Wants a native editor + live audio + API all up at once, and a host that won't
  take the session down if one plugin hangs.

**Why ARLO.** ARLO's recall doctrine *is* the pro-host doctrine: capture and
restore the plugin's own state chunk, proven **byte-identical** both directions,
VST3 and AU. The JUCE host runs the plugin's native editor while audio and the API
stay live, and a **hardened supervisor** kills one hung worker without dropping the
service. Local-first, deadline-safe.

**What makes him bounce.** He's a secondary target because he's less about pedals
and live scenes; if the synth-host story ever feels less robust than Gig
Performer / Cantabile, he stays where he is. Byte-identical proof is what earns him.

**Closing feature:** demonstrable byte-identical state-chunk recall + crash isolation.

---

## 5. Marcus "Fitz" Fitzgerald — *"If it phones home from inside my signal path, I'm out."*
**SECONDARY**

- **38, Berlin (remote).** Senior software engineer; makes ambient/generative music
  on weekends. Runs his own NAS, self-hosts things, reads licenses.
- **Rig:** modest but nice — a few Chase Bliss + OBNE pedals, an Elektron box, a
  Mac, Ableton, Valhalla. More interested in *systems* than accumulation.
- **Aesthetic:** generative / systems-driven ambient, Eno-ish, patch-as-composition.

**A day in the life.** He distrusts subscription DAW-clouds and anything that owns
his data. He'll happily run four small local processes if it means he understands
and controls the whole chain. He reads a repo's LICENSE before its README. When a
tool is hackable and local, he becomes its biggest evangelist.

**Goals.** Own his data. Trust the signal path. Extend and script the thing. Keep
his library portable forever.

**Frustrations / pains.**
- Cloud lock-in and opaque data ownership.
- Tools that can't be inspected, scripted, or run offline.
- Formats that trap his work in one vendor.

**Why ARLO.** Local-first, **no cloud in the signal path**, markdown-canonical
(his library is portable text he owns), four small killable processes he can curl
directly, and **AGPLv3**. This is a tool built the way he'd build it — he'll adopt
it *because* of the architecture, and tell every gear forum about it.

**What makes him bounce.** Secondary because he's a small (but loud and valuable)
slice, and he's demanding: any hidden telemetry, any binary blob he can't audit,
any drift toward a hosted dependency and he's gone — and vocal about it.

**Closing feature:** local-first architecture + AGPLv3 + curl-able, scriptable engine.

---

## Anti-persona — who ARLO is *not* for (yet)

Being explicit here keeps positioning sharp and saves marketing spend.

- **The beginner** with a Boss Katana and two pedals. No recall problem yet —
  ARLO solves a pain they don't have. (Great *future* user; wrong *first* user.)
- **The pure in-the-box producer** with no hardware and one soft-synth. Nothing to
  recall across; a stock DAW preset browser is enough.
- **The "make the AI write my song" user.** ARLO is an honest tool by design —
  composition/melody generation is off by default. Someone who wants a ghostwriter
  will be disappointed, and that's intentional.
- **Windows/Linux-first users.** ARLO is macOS / Apple Silicon today. Real
  constraint, worth stating up front.

---

## How to use these

- **Prioritize primaries (1–3).** They share the recall + taste + local-first spine
  and are the reachable early adopters (boutique-pedal forums, worship-guitar
  communities, mk.gee-adjacent producer TikTok/YouTube).
- **Secondaries (4–5)** validate the engine's depth (perfect recall, open
  architecture) and produce the loudest evangelists per capita.
- **Feature decisions:** if a change doesn't move the needle for at least one
  primary's *closing feature*, question whether it's on the critical path.
