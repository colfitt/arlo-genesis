# Chase Bliss Bad Mood — Wet Channel Deep Dive

The left-hand channel of the BAD MOOD, exhaustively: the three real-time spatial effects —
**Soup** (spectral resynthesis reverb), **Relay** (a no-decay, fixed-count repeater), **Flip**
(a chordcaster that spreads harmonies across time) — plus everything that shapes what they do:
the CLOCK sample-rate master, FREEZE per mode, ROUTING/BLEND/SYNC as they feed the channel, the
SPREAD stereo engine, the EQ/GLUE/CROSS character layer, and the MIDI surface. Companion to
`Bad-Mood-MicroLooper-DeepDive.md` (the right channel) and to
`Patches/Chase Bliss Bad Mood/Bad-Mood-Patch-Library.md` (control reference + 40 patches,
cross-referenced as A1…E6).

Flags: 🟢 manual / MIDI manual / product page (first-party, verbatim behavior) · 🟡 official
videos, press, or the days-old owner pool · 🟣 designed/inferred on top of verified behavior.
First units reached owners **Aug 26–28 2026**; every 🟡 owner claim is a first impression.

---

## 1. Identity: "unorthodox spatial treats"

The manual's framing 🟢 (p.22): "The Wet Channel is where you will find BAD MOOD's live effects.
It's a collection of unorthodox spatial treats that can process your micro-loops, input signal,
or both." Where the Micro-Looper *captures and reinterprets*, the Wet Channel works in **real
time** — but the two are deliberately entangled: the looper records the wet output in its
always-listening state, the wet can process the loop instead of (or alongside) you, and either
side can modulate the other via CROSS.

The slot-by-slot inversion of the MOOD MkII 🟡 (Mark Johnston's opening read): instead of "the
beautiful ambient multi-tap reverb… this one has Soup — a very synthy, gritty, digital-sounding
reverb that kind of **pulls at itself** as you turn up the modify control." Instead of "that
clean digital delay that you just kind of grit up with some clock noise… you now have Relay — a
take on delay that doesn't have any decay." And instead of Slip, "you now have something called
Flip… probably **more broadly useful and approachable on the Bad Mood versus the original Mood
Mark II**" — one of his two standout features of the whole pedal. Harp Lady agrees from the
other direction: "I thought that you couldn't really top the slip mode… but this is actually
better. It's like Slip, but better… almost like a Rainbow Machine."

**The control surface** 🟢 (pp.10, 22): two knobs whose meaning changes per mode —

| Mode | TIME | MODIFY | Freeze (hold left footswitch) |
|---|---|---|---|
| **Soup** | Decay / Size | Character | Ambient pad |
| **Relay** | Delay time | Number of repeats | Looping echo |
| **Flip** | Lag / Spacing | Harmony | Repeating chord |

Left footswitch: **tap = bypass** (with TRAILS dip, the tail exhales instead of cutting),
**hold = FREEZE** (momentary; latching with the LATCH dip). The **MIDI/EXT jack doubles as an
external footswitch input** (normally-open TS switch) that automatically takes over engaging
the Wet Channel — the tabletop rig hookup (p.49). Over MIDI: CC102 bypass, CC105 freeze, CC21
mode (Soup 0–1 · Relay 2 · Flip ≥3), CC14 TIME, CC17 MODIFY.

## 2. CLOCK and the Wet Channel — one knob, three different levers

CLOCK sets the sample rate, which controls "the quality and time of the Wet Channel" 🟢 (p.8) —
but *what that means* is different per mode, and the demos map it 🟡:

- **Soup:** CLOCK changes "the stretch characteristic of that reverb as well as the snappiness
  and the resolution" (Johnston). His poles: **max CLOCK = fastest/highest sample rate, "no
  stretching being applied," snappy, hi-fi, "a lot of presence and treble information"; min
  CLOCK = "the grittiest, the grainiest, the most broken sounding"** — all treble gone, "a ton
  of grit." The manual's own aesthetic: "in our opinion it sounds best when CLOCK is rolled
  back," and high CLOCK adds "sparkling artifacts that might be your kind of thing" (p.24
  "CLOCK OUT").
- **Relay:** delay times scale with the sample rate (64k→32k halves the speed of "your Wet
  Channel effect," p.20); at low CLOCK the repeats become "interesting stretched-out low clock
  noise delays" drifting "through the grime" (Johnston).
- **Flip:** CLOCK scales the **lag** — Knobs: "Clock, of course, will have some impact on how
  much lag there is"; Johnston: "as you turn that clock down and extend that lag, not only do
  they get grittier and grimier and darker as they come out, but it also **delays further and
  further and time stretches them** as they go."
- The steps are the same harmonized 2k→64k ladder as everywhere (library Part I §2); the
  **SMOOTH dip** unsteps it for "legato, nice pitch-bendy" glides (Johnston) — live varispeed
  on a ringing wet tail.
- 🟡 Owner caveat (dizzy, Elektronauts #3149): the wet channel does **not** simply inherit the
  loop's CLOCK pitch — "the modes on the other channel will play the loop pitched up depending
  on where it's dialed in to, so even if you lower Clock the other channel might play it back
  at the original pitch or higher." Per-mode/per-station mapping still needed (§12).
- MIDI clock: the wet channel has its **own division** (CC53, 1/32 → double-whole, saved
  globally, independent of the looper's CC54); tap tempo via CC93 (exit: hold footswitch + turn
  TIME); sub-60 BPM effective tempo forces a sample-rate shift that re-pitches existing audio
  🟢 (MIDI manual pp.3–4).

## 3. Soup — the spectral resynthesis reverb

🟢 (p.24): "Soup is a spectral reverb that **resynthesizes your playing**. It analyzes and
recreates whatever passes through it, creating unnatural ambience that is a **distant memory of
your instrument**. Use it to explore impossible spaces and synthetic dreamscapes, or to remake
your instrument completely." 🟡 Knobs's mechanism description: it recreates the input "using
**thousands of little frequency bands** that act and behave like a reverb."

**Controls:**
- **TIME = decay** — Johnston's sweep: "from a short splash out through giant wafting ambience."
- **MODIFY = character**, CW = more synthetic 🟢 — and 🟡 the walkthrough adds the crucial
  hidden detail: MODIFY is also the **modulation amount**. "With modify at zero, you have no
  modulation. It's a pretty heavily modulated reverb [otherwise]… as you turn up modify, it
  comes back." At zero: "a more familiar reverb sound." Knobs's recommendation: "**I actually
  like to leave it around noon** — you're getting some of that synthetic strangeness blended
  with a more familiar reverb."
- So MODIFY is really a one-knob morph: *plain-ish reverb → modulated reverb → resynthesized
  texture*. The mode's whole range from "conventional ambient tool" to "instrument remaker"
  lives on it.

**Texture notes** 🟡:
- Hilowitz: Soup has "a sort of **brittle resonance** to it. The more notes you play, the more
  noticeable it is" — density feeds the resonance; sparse playing keeps it glassy, chords make
  it bloom/clang.
- Owner tell (dizzy, day two): "Soup has a phaser effect which would be a strong tell, it's
  very noticeable" — he hears it as Chase Bliss's take on a shimmer-adjacent reverb. One ear's
  report; listen for it.
- The hidden **EQ** (wet MODIFY in the hidden options) is "pretty critical for a reverb… it can
  do profound things here — from a distant arcade sound to something more mellow that hides in
  the background" (Knobs). CW cuts lows, CCW cuts highs, noon flat 🟢; per-channel assignment
  via MIDI CC85 only.
- **Freeze = an ambient pad** 🟢 — non-decaying, knob-responsive, transposable by CLOCK, and
  capturable by the looper (the Synthetic Starter seed, patch A2; the drone floor, A4; the
  Synth Mode oscillator, D7).

**Use cases → patches:** everyday synthetic space (A3 Distant Memory Hall), high-CLOCK sparkle
(A3 variation), frozen drone floor (A4), the blur-plus-Soup pairing on Radio's Ambient station
(A5 — Knobs's own tip), Cross sputter demo (C6), gentle always-on halo (E3).

## 4. Relay — the abstract repeater

🟢 (p.24): "Relay is a **delay that doesn't fade out**. Unlike a traditional delay where you
control the amount of feedback, Relay lets you select a **precise number of repeats that each
share the same volume**. You can think of it like a sampler that's always recording, and each
sample can be repeated a chosen number of times."

**Controls:** TIME = delay time; MODIFY = repeat count — "at max, repeats are stable and will
pile up like a looper" 🟢.

**The behavior that defines it — how repeats *end*** 🟡: they don't fade, they stop. Johnston:
the repeats play "at the exact same volume every time until it's run its course, and then it's
just gone… they're all just kind of drifting through the grime of Bad Mood's clock together
until it's time for them **one by one to just stop**." Hilowitz, deadpan: "It's funny — after a
while it just kind of stops dead." No tail, no warning; program around it (or hide the endings
under Soup downstream of a capture).

**The illusion** 🟢 (p.25 "WHEN DID YOU GET HERE?"): "Because 'old echoes' and 'new echoes'
both have the same volume — without decaying feedback to distinguish the two — you can create
unique, abstract sensations where old and new can't be told apart. It's a bit like an audio
illusion, and can be a very fun spin on **Frippertronics-style looping**." Johnston's live
version: full-wet Relay is "its own form of Frippertronics sound-on-sound looper" — you
"introduce new little moments and clusters of notes that just seem to **exist in parallel**
with everything else."

**Use-case sweep** 🟡 (Knobs): "the effect of doubling… a lot of sound effects… a really cool
way to loop full wet… great for rhythmic stuff, great for **cloning yourself**, for building up
loops, for taking double tracking and stretching that out over time."

**Freeze = a looping echo** 🟢 — the current repeat pile loops infinitely and **your playing is
not recorded into it**: the punch-out that makes Relay a second looper (2-Track, p.22; patch
B1). With **SYNC left**, TIME also sets the micro-loop length (shared bar); with **SYNC right**,
TIME snaps to subdivisions of the loop ("properly quantized" echoes — Johnston; patch B8).

**Use cases → patches:** exact-count slap/double (B2 Honest Echo), the illusion pile (B3 When
Did You Get Here?), 2-Track layering (B1), loop-locked grid (B8), repeats-that-flinch under
Cross (C6 variation).

## 5. Flip — the chordcaster

🟢 (p.26): "Flip is a **pitch shifter that creates layered harmonies** to support your playing,
but allows you to **spread the different notes across time**. It can be used for everything
from pitch shifting to chord stacks to harmonic sequences."

**Controls:**
- **MODIFY = the harmony.** "A variety of different arrangements of 4ths, 5ths, and octaves,
  going both up and down. The higher the knob is set, the more notes will be present" 🟢. The
  MIDI manual publishes the complete **48-chord map on CC17** (library Part I §7.4): chords 1–6
  single intervals (−Oct, −5th, −4th, +4th, +5th, +Oct) · 7–21 two-note · 22–40 three-note ·
  41–48 four-note. 🟡 Knobs confirms the zones on the face knob: "one note down here. Two note.
  Three note. And four note" (the panel's tick lines mark them). ⚠️ Johnston says the opposite
  ("further clockwise… fewer notes, and the notes cascade down") — **the CC17 table settles it:
  more notes as MODIFY rises.** Treat Johnston's line as a misspeak; his "cascade down" may
  describe the upper chords' voicings, many of which stack downward intervals.
- **TIME = lag/spacing.** "Sets the lag time between notes" 🟢; Knobs: "the space between the
  different intervals in the chord — down here, you're getting the same note" (min = simultaneous
  stack); Hilowitz per the manual: "time actually controls when the extra notes start." The
  manual's own preset: "**'VINTAGE' HARMONIES** — turn up the TIME knob just a bit to replicate
  the laggy character of older pitch shifters and harmony effects" (p.27; patch D2).
- Intervals are **only** 4ths/5ths/octaves — "all very easy to use, while still giving you a
  lot of rich sounds" 🟡 (Knobs). No 3rds = no major/minor commitment: everything lands modal,
  quartal, or organ-like, which is *why* it's safe to leave running.

**The TIME continuum** (🟢 endpoints, 🟡 middle): min = a chord stack (polyphonic
pitch-shifter) → "just a bit" = vintage-shifter lag → high = the notes arrive one by one — a
**harmonic sequence / arpeggiator** ("splintered harmonies," the product page's phrase; patch
D3). Add low CLOCK and the arrivals stretch: "very angry, very dark, very gritty, very sluggish
pitch shifts" (Johnston) — the doom register (patch D4).

**Freeze = a repeating chord** 🟢 — and it matters because 🟡 "there is no regeneration control
over here… **you're getting one jump each**" (Johnston): un-frozen, each note's harmony speaks
once and is gone. Freeze is what sustains a Flip pattern — the basis of the manual's **CHORD
LOOPER** ("play a single note, and freeze Flip: a repeating pattern that you can transpose with
CLOCK and re-harmonize with MODIFY… a launching point for turning BAD MOOD into a strange
little synth," p.22; patch D1).

**Flip as a delay/looper citizen** 🟡: Knobs — "unique pitch-shifted delays that are specific
harmonies of whatever you played," and "rich harmonies that **spread around the stereo field**"
(with SPREAD). Feeding the *looper* into Flip (ROUTING down): "it's going to take a while for
it to get here… but you can get really broken sounding" (Johnston) — the lag applies to the
whole loop. Owner accident worth keeping (dizzy): Tape station hard-CCW into **Flip with a
moving TIME** reads as "kinda dub techno."

**Reception:** Johnston — the standout engine, "more broadly useful and approachable" than
Slip. Hilowitz — "a chord pitch shifter… yeah, this is made for me." Harp Lady — "like Slip,
but better… almost like a Rainbow Machine."

**Use cases → patches:** D1 Chord Looper, D2 Vintage Shifter, D3 Splinter Cascade, D4 Power
Interval Doom, D5 Radio Choir, B7 variation (dub-techno), A7 variation (chorale generations).

## 6. FREEZE — the wet channel's fourth mode

🟢 (pp.10, 22): hold the left footswitch and "the current sound repeats infinitely." Per mode:
**Soup → ambient pad · Relay → looping echo · Flip → repeating chord.** Playing over a freeze
is **not** recorded into it. LATCH dip = hands-free; TRAILS = graceful exits; CC105 = MIDI
freeze.

What makes BAD MOOD's freeze deeper than a hold pedal:
- **It stays live.** Knob moves keep working on the frozen sound — re-harmonize a frozen Flip
  with MODIFY, reshape a frozen Soup's character, and **CLOCK transposes the freeze in
  harmonized steps** (the A4 chord-change lever; the D7 Synth Mode oscillator).
- **It's capturable.** The freeze is Wet Channel output, so the always-listening looper records
  it regardless of routing — the freeze→capture→freeze **resample ladder** ("just hand it back
  and forth for forever" — Johnston; Trail Catcher A7, Synthetic Starter A2).
- **It's a punch-out.** While frozen, the channel ignores your playing — the 2-Track record-arm
  trick (B1).
- **It's a synth voice.** Frozen Soup + LATCH is the MIDI manual's own Synth Mode starter
  (D7): the freeze becomes the oscillator, keys transpose it in semitones, ADSR carves it.

## 7. What feeds the channel — ROUTING, BLEND, SYNC

- **ROUTING** 🟢 (p.40): input only / input + loop / loop only — active only when both channels
  are on. Loop-only is the *dry-lead-over-processed-bed* posture ("dunk your micro-loops into
  the Soup, but leave your instrument clean"); input-only keeps a precious loop out of the wet;
  middle throws everything in. CC22.
- **BLEND** 🟢 (p.15): wet-routed loops are 100% wet by default — BLEND restores the clean loop
  in parallel. Johnston's demo names the problem it solves: loop into reverb and "suddenly,
  it's just a soup. I mean, it's literally called soup, but it's also just sonically a soup" —
  BLEND gives "a kind of retained version of that micro looper" underneath. CC29.
- **SYNC** 🟢 (p.17): left = loop length follows TIME (the wet channel is the clock source);
  right = TIME steps in loop-related subdivisions (the loop is the clock source); middle =
  free. CC31. Johnston: this is "one of my favorite things about the Bad Mood."
- Remember the capture rule from the looper side: whatever this channel outputs **is recorded**
  whenever the looper sits bypassed — the wet channel is always potentially printing to tape.

## 8. Stereo — how the wet effects make width

🟢 (pp.4, 44): true-stereo device (mono / TRS stereo / MISO); **SPREAD dip** "turns on stereo
processing — each mode has its own unique approach to generating a stereo image."

🟡 Johnston adds the mechanism the manual omits: **SPREAD sums the signal to mono first, then
creates a unique stereo field image from the wet effects** — i.e. it's a stereo *generator*
(great for mono-in rigs, or for re-imaging), not a widener of existing stereo; run without
SPREAD, the pedal is genuinely dual-mono/true-stereo and wet placement follows the input image
exactly ("repeats are landing exactly where they do in relation to where these audio pieces are
hitting on the left and right channels"). The MkII rule survives: **SPREAD creates an image;
MISO creates stereo from mono; true-stereo passes yours through.**

- **Per-channel SPREAD** (hidden, on ROUTING): widening on just the effect, just the loop, or
  both — e.g. wide Soup around a mono loop (the manual's own example; patch E5), or a
  center-channel Relay whose repeats sit where you played them.
- **Flip + SPREAD** spreads the harmony voices around the field 🟡 (Knobs) — the four-note
  chords become a small ensemble seated across the stage (D2/D3).
- Captured loops **keep** whatever stereo image the wet had when they were recorded, even after
  SPREAD is switched off 🟡 (Johnston) — width is baked in at capture.

## 9. The character layer — EQ, GLUE, CROSS on the wet effects

- **EQ** (hidden, wet MODIFY; CC27): two-way — CW cuts lows, CCW cuts highs, noon flat 🟢.
  "Pretty critical for a reverb… profound things — from a distant arcade sound to something
  more mellow that hides in the background" 🟡 (Knobs). Global by default; **CC85** makes it
  wet-only (0–1), both (2), or looper-only (≥3) — a MIDI-only per-channel tilt.
- **GLUE** (hidden, CLOCK; CC28) 🟢 (p.42): end-of-chain saturator/destroyer on both channels —
  the wet effects always exit through it. 🟡 Johnston: "a compressor limiter thing that quickly
  becomes something that really mangles your sound as you press into it hard… it does [it] to
  both sides and it really crunches down quickly." Hilowitz: tape-recorder-input-too-hot; the
  default was "plenty for me." First-owner report: default too hot for pristine pads — turn it
  down for clean Soup work (E3). Low = gel the channels into one body; high = torn-speaker →
  bit-crush (C8); DRY GLUE dip + MIX down = standalone stereo saturator (E2).
- **CROSS** (hidden, TIME; CC24) + **INPUT MOD** (hidden, looper MODE toggle; CC33) 🟢 (p.43):
  dynamic interference with **pitch and loudness**; the manual's own demo is wet-side — source
  = input, CROSS way up, play through **Soup**: "notice how it bends and sputters as you play."
  🟡 It is **amplitude-gated in real time** (Johnston: "by holding up my note, I can keep it
  broken"), the sweep runs "slight squiggles" → "total dropout/failure" (Knobs), reverb trails
  are where you hear it best, and it's "cool for breaking those Flip pitch jumps" (Johnston).
  Sources: input → both channels; looper → the wet channel breaks in the loop's rhythm even
  while you rest; wet → the looper breathes under the reverb's swells (C6, C7).
- **BALANCE** (hidden, MIX; CC25): loop-vs-wet loudness — Johnston's demo is the use case:
  "now I can really crank the mix on my reverb and not have a ton of that loop going, or vice
  versa." Fix balance here, not with MIX. MIDI-only **MASTER VOLUME** (CC30) after everything.

## 10. MIDI surface of the Wet Channel

🟢 (MIDI manual pp.3–8; full map in the library Part I §7.3):

| CC | Function | Notes |
|---|---|---|
| 102 | Wet Channel bypass | 0 off / ≥1 on |
| 105 | FREEZE | 0 off / ≥1 on — hands-free/sequenced freezes |
| 21 | Wet MODE | Soup 0–1 · Relay 2 · Flip ≥3 |
| 14 | TIME | 0–127 — decay / delay time / lag by mode |
| 17 | MODIFY | 0–127 — Soup character/modulation · Relay repeat count · **Flip: the 48-chord table** (exact chords addressable — e.g. 12 = +5th, 17 = −Oct−5th, 62 = +Oct+5th+4th) |
| 27 / 24 / 28 | EQ / CROSS / GLUE | the character layer |
| 31 / 29 / 25 | SYNC / BLEND / BALANCE | the feeding layer |
| 53 | Wet clock division | 0–8 (1/32 → double-whole), saved globally |
| 93 | Tap tempo | exit: hold footswitch + turn TIME |

**Synth Mode** (any MIDI note) turns the wet channel into the voice of an instrument: the
MIDI-manual walkthrough's own recipe is **frozen Soup (LATCH on) as the base sound**, output
type ADSR (CC58=2) with CC80–83 envelopes, portamento CC84, pitch bend ±4 semitones — "explore
how different MODIFY and TIME positions affect the texture" (D6–D8). MIDI clock is ignored in
Synth Mode; exit via CLOCK or CC59.

## 11. Wet Channel vs MOOD MkII wet channel

Slot-for-slot (MkII details from `gear/Chase Bliss MOOD MkII/research/`):

| Slot | MOOD MkII | BAD MOOD | What transfers |
|---|---|---|---|
| 1 | **Reverb** — multi-tap ambient; MODIFY = tap smear (wash ↔ clusters) | **Soup** — spectral resynthesis; MODIFY = character/modulation | The reverb-as-bed workflow, freeze-pad moves, CLOCK-darkens-the-space instinct. Gone: the pretty multi-tap wash (Hilowitz keeps MkII for it). New: resynthesis, the modulation morph, "remake your instrument." |
| 2 | **Delay** — clean digital; MODIFY = feedback (max ≈ pile-up) | **Relay** — no decay, exact repeat count; max = stable pile | Manual time-stretch (sweep TIME), pile-to-looper moves, sync tricks. Changed: no decaying trail — repeats end one by one; count is *chosen*, not emergent. |
| 3 | **Slip** — continuous auto-sampler; TIME = sample size; MODIFY = speed/direction in semitones (reverse CCW) | **Flip** — chordcaster; TIME = lag; MODIFY = 48 chords of 4ths/5ths/octaves | The pitch-play role. Gone: real-time reverse and semitone-step speed (Slip's sitar/reverse tricks have no Flip equivalent — reverse now lives only in Radio's Tape station + Orchestral's SPREAD split). New: true chord stacks, time-spread harmonies, the freeze Chord Looper. |
| — | Wet TONE (hi-cut only) | Two-way EQ (+ CC85 per-channel) | Darkening the wash still works; brightening now exists. |
| — | one-way channel sync | **SYNC both directions** | In-time capture upgraded to "properly quantized micro loops." |
| — | — | **GLUE + CROSS** | No MkII equivalent — the character layer is the inversion. |

MkII techniques that still apply verbatim: freeze-then-capture, dry-over-soaked-loop routing,
LEVEL BALANCE (not MIX) for channel balance, TRAILS for seamless toggling, SMOOTH-clock
pitch-bends, EXP/CV multi-knob morphs, "tiny knob differences are crucial."

## 12. Open questions (verify on hardware)

1. **Soup's modulation** — rate/shape unpublished; is the owner-reported "phaser quality" the
   modulation at MODIFY ≥ 0, or intrinsic to the resynthesis?
2. **Relay's maximum repeat count** below the infinite top — how many, and are the steps
   audible on the knob?
3. **Relay TIME range** in ms per CLOCK step — unpublished (no tap-division chart for the face
   knob; only MIDI CC53 subdivisions are documented).
4. **Flip voice allocation** — monophonic tracker or polyphonic? (Demos are single-note-led;
   Hilowitz's kalimba chords seemed to track, but nobody tests chords explicitly.)
5. **Flip lag range** in ms/beats per TIME+CLOCK combination — unpublished.
6. **Whether freeze output keeps responding to CROSS/GLUE changes identically in all three
   modes** (demonstrated for Soup and Flip; Relay untested).
7. **The wet-repitch matrix** (dizzy's report): which wet modes re-pitch loop playback, and how
   it interacts with each Radio station + CLOCK + LENGTH.
8. **SPREAD's per-mode stereo algorithms** — the manual says each mode has "its own unique
   approach"; only Soup-widening and Flip voice-spreading are described anywhere.
9. **EQ crossover frequency** and slope — unpublished.
10. **Whether SYNC-left changes Relay's audible repeat spacing** or only the loop-length
    coupling.

## Sources

- **Manual (Field Guide)** — `../manuals/Bad-Mood_Manual_Chase-Bliss.pdf`: Wet Channel chapter
  pp.22–27 (modes, freeze ideas, Vintage Harmonies, When Did You Get Here), routing pp.40–41,
  Glue/Cross pp.42–43, customize pp.44–45. The 🟢 backbone.
- **MIDI Manual** — `../manuals/BAD-MOOD_MIDI-Manual_Chase-Bliss.pdf`: CC map, the 48-chord
  CC17 table, CC53/93, Synth Mode.
- **Mark Johnston "Secret Weapons"** — youtube.com/watch?v=KBY0gqpfpHw (1h20m, transcript at
  `transcripts/mark-johnston-secret-weapons-bad-mood-deep-dive.md`): Soup CLOCK poles,
  SPREAD-sums-to-mono mechanism, Relay one-by-one endings + full-wet Frippertronics, Flip lag
  scaling + "one jump each" freeze + looper-into-Flip, the Cross demos (gating, Flip-jump
  breaking), MIX-alt balance demo, Glue-as-compressor/limiter, sync both directions.
- **"BAD MOOD – Walkthrough" (Knobs)** — youtube.com/watch?v=5UgwxdzB9CQ (transcript at
  `transcripts/chasebliss-official-bad-mood-walkthrough.md`): Soup MODIFY = modulation + noon
  preference, EQ characterizations, Relay use-case sweep, Flip 1–4-note zones + TIME-min stack
  + stereo spread, Glue/Cross characterizations.
- **David Hilowitz** — youtube.com/watch?v=Z1B3pCYEKVo (transcript at
  `transcripts/david-hilowitz-bad-mood-distorted-ambient.md`): brittle resonance, Relay
  stops-dead, TIME-controls-when-notes-start, Glue placement/level, MkII side-by-sides
  (kalimba), the ephemerality framing.
- **Harp Lady** — youtube.com/watch?v=uIXLHh-HYzU (transcript at
  `transcripts/harp-lady-bad-mood-shoegaze-demo.md`): "like Slip, but better… almost like a
  Rainbow Machine"; ground-up design quote. **Jason Mays** — youtube.com/watch?v=9JAAUfurXmw:
  wet section "completely different but similar… an inverse."
- **Elektronauts CB megathread pp.150–155** — elektronauts.com/t/chase-bliss-effects-pedals/31096
  (the complete owner pool as of 2026-08-28): Soup phaser tell, hot Glue default, wet-repitch
  report, the Tape+Flip dub-techno clip.
- **Repo cross-refs** — `Bad-Mood-MicroLooper-DeepDive.md` (the right channel; capture rules,
  resample ladder, stations); `Patches/Chase Bliss Bad Mood/Bad-Mood-Patch-Library.md` (control
  reference + the patches indexed throughout); `gear/Chase Bliss MOOD MkII/research/` (§11
  comparison).
