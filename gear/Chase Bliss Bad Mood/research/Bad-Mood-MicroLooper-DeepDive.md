# Chase Bliss Bad Mood — Micro-Looper & Arranger Deep Dive

The right-hand channel of the BAD MOOD, exhaustively: the **always-listening Micro-Looper** and
its three modes — **Burst** (loop → 8-step sequencer), **Radio** (one loop → five genre
"stations"), **Mask** (threshold-triggered loop disguiser) — plus everything that *arranges*
what the loop becomes: the CLOCK sample-rate master, the overdub/replace/capture rules, the
FADE / SYNC / BLEND / BALANCE hidden options, and the MIDI surface. This is the companion
deep-dive to `Patches/Chase Bliss Bad Mood/Bad-Mood-Patch-Library.md` (control reference +
40 patches; behaviors cross-referenced as A1…E6) and to `Bad-Mood-WetChannel-DeepDive.md`
(the left channel: Soup / Relay / Flip).

Flags as in the library: 🟢 manual / MIDI manual / product page (first-party, verbatim behavior) ·
🟡 official videos, press, or the days-old owner pool · 🟣 designed/inferred on top of verified
behavior. First units reached owners **Aug 26–28 2026**; treat every 🟡 owner claim as a
first-impression, not lore.

---

## 1. Identity: an "always listening looper," not a looper pedal

The manual's own framing 🟢 (p.30):

> "The Micro-Looper on BAD MOOD is a bit unique. It's an 'always listening looper,' which is
> like **fishing for music**: It is continuously recording when bypassed, and then you turn it
> on and see what you get. Instead of manually setting the length like a typical looper, it's
> set by the CLOCK position."

Three consequences that define everything below:

1. **There is no record button.** Capture is retroactive — you play first, then tap the
   footswitch and "it will keep whatever was played most recently and loop it." The walkthrough
   demonstrates it in one line: "if I just make a sound right now and I turn this on — **it's in
   there**." 🟢🟡 The performance skill is *timing the grab*, not arming a recorder.
2. **There is no stop command and "it's never really off."** 🟢 (p.30) Even bypassed it is
   recording (see the state machine, §2) — with one exception: **true bypass mode kills the
   always-listening looper entirely** ("the always-listening looper will not work until you exit
   true bypass," p.16). 🟢 If you rely on retroactive capture, stay on buffered bypass.
3. **Loop length is a property of CLOCK, not of your take.** You don't decide how long the loop
   is by playing; you decide by where the sample-rate knob sits (§3). This is the deepest
   difference from Blooper-style looping and the reason CLOCK is the channel's real master
   control.

Lineage: this is the MOOD/MOOD MkII looper concept ("fish for music") rebuilt from scratch —
same workflow, entirely new modes. Chase Bliss: not a sequel, "a sibling, or an inversion." 🟢
(blog). The MkII's Tape/Stretch/Env trio is gone; its *behaviors* partially survive inside Radio
(§5.2: the Tape station is first-party described as "an interpretation of tape that you find in
Mood Mark II" 🟡 walkthrough).

## 2. The state machine

Three states, one footswitch 🟢 (pp.12, 30–32):

| State | How you get there | What's happening |
|---|---|---|
| **Recording** (= bypassed, always-listening) | tap while playing/looping | Channel output is off; the buffer continuously records the pedal's input **including the Wet Channel's output regardless of ROUTING** (p.41). The LED **blinks at the loop-cycle rate** — a free visual metronome for the current CLOCK length (p.30). Crucially this state **erases as it goes**: "as soon as the channel is bypassed it starts to erase the existing loop and record the input audio in its place" — the manual names this the **REPLACE** function (p.32). 🟡 Mark Johnston describes the mechanism precisely: "even when it's bypassed, it is always taking in new information into the buffer and discarding it as it gets to the end of the buffer size **as defined by your clock control**… if you turn on that looper, it starts playing back whatever is currently in the buffer of your recent playing" — a circular buffer whose window is the CLOCK length. |
| **Playing** | tap from recording | The most recent buffer contents loop. All three modes mangle *playback* only — the underlying recording is intact, which is why **FREE PLAY** works: "Once a micro-loop is recorded you can switch freely between the looping modes without it being erased" (p.31). |
| **Overdubbing** | hold from playing (latching with the LATCH dip, p.45; MIDI CC106) | New audio is added to the loop under the overdub rules of §4. |

**Performance readings of the state machine** (each verified behavior, 🟣 the application):

- **The blink is your conductor.** Since the LED blinks per cycle while recording, you can watch
  it to time a retroactive grab on a bar line — tap on the blink and the loop seam lands close
  to your downbeat.
- **Bypass = destructive punch-in.** Because recording erases-in-place, rhythmic off/on blinks
  splice new audio (or silence) into an existing loop — the manual explicitly endorses this "to
  clear out some space or add glitches to your loops." Patch C4 (Eraser Head) is built on it.
- **Bypass = resampler.** Because recording hears the Wet Channel no matter the routing, a brief
  off/on while Soup rings **re-captures the loop with its trails baked in** — the manual's named
  **TRAIL CATCHER** move (p.31), patch A7. Every blink is a generation.
- **The gotcha twin of both:** any accidental bypass *is* an erase-in-progress. If a loop is
  precious, don't tap the right footswitch to "mute" it — there is no mute; that's REPLACE. Use
  MIX/BALANCE, or protect the moment by saving a preset (presets store everything but not the
  audio buffer — see §12 open questions on buffer-vs-preset behavior ⚠️). 🟡 David Hilowitz says
  it as an aesthetic: "once I hit this button, this texture will be gone for good… I have no
  control over what the pedal hears. My sounds will be chopped and recombined according to a
  logic I can't predict." Ephemerality is the design, not a limitation.

## 3. Loop length, resolution & CLOCK — the arranger's time ruler

🟢 (pp.8, 20, 45; MIDI manual p.4):

- CLOCK sets the **sample rate**, which sets "the length and resolution of the Micro-Looper
  Channel" — low CLOCK = **longer, grainier** loops; high CLOCK = **shorter, cleaner** loops.
  🟡 Mark Johnston's summary of its reach: CLOCK sets "the fidelity, size, length, lag, and
  texture of **everything** happening in the Bad Mood"; moving it under a playing loop changes
  "the fidelity and pitch and kind of playback speed of what I have just recently captured" —
  pitch and speed shift together, a sample-rate looper by construction. 🟡 Hilowitz on why the
  stepping matters: "it's **stepped so that the pitch shifts are harmonically useful**"; super
  low = "degraded bit-shifty."
- It steps through an 11-position **harmonized ladder** — 2k · 3k · 4k · 6k · 8k · 12k · 16k ·
  24k · 32k · 48k · 64k (CC18 value ranges in the library, Part I §2). Each step is a musical
  fourth/fifth; every second step an octave. "Lowering the sample rate from 64k to 32k will
  halve the speed of your micro-loop as well as your Wet Channel effect."
- **HALF dip** = loop length cut in half, "matching the response of the original MOOD (loop
  length is relative to the CLOCK setting)" (p.45). So BAD MOOD's stock loop window is the
  longer MkII-style one; HALF restores the original MOOD's tighter window.
- **SMOOTH dip** de-steps CLOCK for continuous glides — with a loop playing this is a tape-speed
  varispeed lever (pitch and length slide together).
- ⚠️ **Absolute loop lengths in seconds are unpublished** — for any CLOCK position, with or
  without HALF; no owner has posted a measurement either (confirmed across every reachable
  source, 2026-08-28). What *can* be derived 🟣 from 🟢 facts: the loop is a **fixed sample
  count replayed at the CLOCK sample rate** (Johnston's circular-buffer description + the
  manual's 64k→32k halving rule), so across the 11-step 2k→64k ladder the loop window spans a
  **32:1 length range** — the 2k floor holds a loop 32× longer (and 5 octaves lower on
  playback) than the 64k ceiling. When the pedal arrives: measure per CLOCK step with the LED
  blink and log it here.

**CLOCK as a musical control over an existing loop** (all first-party behaviors):

- Move CLOCK during **playback**: the loop transposes and re-speeds in harmonized steps —
  fourths/fifths/octaves, so "wrong" pitches are rare by construction. (Getting-started page:
  "roll back the CLOCK knob to turn it all into a big, moving texture," p.7.)
- Move CLOCK during **overdub**: the one sanctioned free move — "You can freely move the CLOCK
  knob while overdubbing and your notes will remain right where you played them. A great way to
  build harmonies that play at different speeds." (p.33, "USE THE CLOCK!") This is the pedal's
  multi-speed multitracking feature: each overdub pass at a different CLOCK = a voice at a
  different octave/speed, all coexisting in one loop.
- 🟡 **Owner headroom trick** (Elektronauts, first week): record loops **1–2 CLOCK steps high**
  so you have room to slow down later "and get more granular at a reasonable pitch" — recording
  at the top of the ladder makes the whole ladder available downward.
- 🟡 Owner observations on CLOCK's limits (dizzy, Elektronauts #3149, day two of ownership):
  "Lowering Clock also lowers the pitch, so not sure you could slice a loop into grains and just
  shorten the loop to a few grains with pitch preserved" — **there is no independent
  grain/length control in the looper itself** (pitch-preserved manipulation lives in the Ambient
  station instead). And the wet channel doesn't simply inherit the loop's pitch: "the modes on
  the other channel will play the loop pitched up depending on where it's dialed in to, so even
  if you lower Clock the other channel might play it back at the original pitch or higher" —
  Radio stations "interact with the wet channel side a bit differently depending on which one +
  Clock + Length." Needs systematic hardware mapping (§12 #8).

**Synced length (the SYNC hidden option, both directions)** 🟢 (p.17):

- **SYNC left — Micro-Looper synced to Wet Channel:** "The length of the micro-loop is now set
  by the TIME knob." The loop length detaches from CLOCK and follows the wet TIME — the
  2-Track/bar-length workflow (patch B1): dial TIME to your bar and both channels share it.
- **SYNC right — Wet Channel synced to Micro-Looper:** TIME snaps to "steps that are
  rhythmically related to the micro-loop length" — the loop becomes the tempo authority and the
  wet effect grids to it (patch B8). ⚠️ Which subdivisions the steps are is unpublished.
- Middle = unsynced (default). Over MIDI: CC31 (0–1 = looper→wet · 2 = none · ≥3 = wet→looper).

**External clock and the looper** 🟢 (MIDI manual pp.3–4): CC51 ≥1 = follow MIDI clock;
**CC54** sets the looper's own clock division (1/32 … double-whole, saved globally,
independent of the wet channel's CC53). Below an effective 60 BPM the pedal must shift its
internal sample rate and **existing audio changes speed and pitch** — the loop lurches when you
cross that line. There is **no MIDI clock out** documented. In **Synth Mode** (any stray MIDI
note!) clock is ignored entirely — the classic MOOD-family landmine.

## 4. What gets recorded when — the capture rulebook

The four rules, all first-party 🟢 (pp.31–33, 41), because every Bad Mood looping technique is
some combination of them:

1. **Always-listening state records EVERYTHING the pedal is making** — "it will record the
   sounds from the Wet Channel **regardless of the routing setting**. If you're playing through
   Relay mode before engaging the Micro-Looper, the loop will have those repeats captured within
   it." (p.41) → Trail Catcher (A7), Synthetic Starter (A2 — a frozen Soup pad is capturable),
   printing a Flip chord-freeze (D1 variation), bouncing a Relay pile-up (B1 variation).
2. **Overdub records ONLY the clean input** — "While you will hear the Wet Channel's effects as
   you overdub, they will not be recorded into your micro-loops. This would create a loud, scary
   feedback loop. No thanks." (p.32) → to layer *wet* material you must exit to the
   always-listening state and re-grab (rule 1); to layer *dry* material you overdub. The two
   capture paths are complementary, not redundant.
3. **Overdub placement is subject to the current playback mangling** — "If any of these effects
   are happening while overdubbing, the recorded audio may end up in a different place than you
   expect. ALWAYS UNPREDICTABLE!" (p.32) The manual's fix for traditional layering is to
   overdub at each mode's neutral spot (shown graphically p.32; consistent reading: Burst
   MODIFY-min, Radio on Tape at normal speed, Mask MODIFY-min 🟣) — or embrace the displacement
   as a compositional partner (patch C5).
4. **Burst's special case:** overdubs are "recorded into the micro-loop that it's built from,"
   not into the sequence — "what you hear and where you're being recorded are disconnected"
   (p.34). New material re-slices on the next detection pass.

**FADE — the decay valve** 🟢 (p.14): hidden option under LENGTH. Below unity, "your loops
gradually fade while overdubbing, for slowly evolving loops or the ability to treat the
Micro-Looper Channel like a delay." Two readings:
- *Evolving loop:* FADE slightly down + periodic overdubs = a bed whose oldest layers sink as
  new ones arrive — composition by forgetting.
- *Pseudo-delay:* FADE low + **latched overdub** = everything you play recirculates on the loop
  cycle and dies over a few generations — a loop-locked echo whose "delay time" is the CLOCK
  length and whose repeats transpose if you move CLOCK (patch E4). This is the feature Knobs
  points to with "you can turn the micro looper into a delay" 🟡, and it replaces the MkII's
  NO DUB dip territory.
- 🟡 **FADE is pausable mid-fade** (Mark Johnston, demonstrated): start a fade, then "set it
  back… and wherever the fade currently is, it will just hold there" — you can duck a loop to a
  chosen residual level and park it, a manual volume-envelope on the loop rather than an
  all-or-nothing decay.

**BLEND — the parallel-loop valve** 🟢 (p.15): when the loop is routed through the Wet Channel
it is normally **replaced 100%** by the processed version (p.41 "WET LOOPS"); BLEND mixes the
clean micro-loop back underneath. This is the arranger's dry/wet fader *for the loop only* —
your live signal isn't touched by it. Use it whenever a Souped/Flipped loop needs its original
articulation ghosting through (A8, D5). 🟡 Johnston confirms the parallel reading: turning it up
gives "access to a kind of retained version of that micro looper" — dry loop + Souped loop
simultaneously, "so the loop isn't just a soup."

**BALANCE** 🟢 (p.16): hidden, on MIX — relative loudness of the two channels ("EVEN" at
center). The channels are not auto-balanced; when the loop buries the wet (or vice versa) this,
not MIX, is the fix — a direct MkII carry-over. MIDI CC25; MIDI-only MASTER VOLUME (CC30) sits
after everything for makeup gain.

## 5. The three modes, exhaustively

### 5.1 Burst — the loop sequencer

🟢 (pp.13, 34–35): "takes your loops and turns them into rhythmic patterns of **up to 8
steps**… Wherever a 'unique' sound is detected in the loop, Burst creates a step. It then
cycles through those slices of audio to create a pattern."

- **LENGTH** = "the speed of the pattern / size of each step."
- **MODIFY** = "the sensitivity of the envelope detector. When a sound is louder than the
  threshold while in playback, the pattern will be **scrambled**" — the *fills* engine: "these
  patterns dynamically react to your instrument when in playback, to create randomizing 'fills'
  when you play along."
- The sequence is a *view* of the loop; the loop persists underneath (walkthrough demos "the
  loop hiding underneath" vs the pattern 🟡) — flip to Mask-min anytime to hear ground truth.

**Step detection in practice** 🟡 (walkthrough, demonstrated note by note): one sound recorded =
a 1-step pattern; add a second sound = 2-step; "with each note I added, a new step was created
in the sequence," up to 8. So the pattern length is *earned by events*, not fixed — silence
doesn't create steps, and a legato wash gives Burst little to slice (the manual's **STABLE
SEQUENCING** advice inverts this: "play short, muted notes, so that the different sounds in the
loop are neatly separated," or record in another mode first and switch over, p.35).

**Step size and the scramble-recovery gotcha** 🟡 (Mark Johnston): LENGTH sets "the size and the
pattern playback of each of the steps" — larger steps move slower, smaller steps more briskly.
With **big steps, a threshold trip scrambles the entire step and the pattern "has to wrap that
big long step before it returns back to normal"** — long recovery; small steps recover almost
instantly. So LENGTH doubles as a *fill-length* control: small = flams and stutters, large =
whole-bar derailments. His summary of why it works anyway: "it's staying rhythmically resonant."
Party mode: run it full-wet and strike muted strings — pure scramble-trigger playground.

**The three Burst postures** (🟢 behaviors, 🟣 framing):
1. *Backbone* — MODIFY min (detector off): a fixed 8-or-fewer-step pattern, the pedal's
   drum-machine-adjacent mode (patch B4).
2. *Duet partner* — MODIFY at the dig-in threshold: normal playing coexists, accents scramble —
   fills you conduct with pick attack (patch B5; walkthrough: "you could have the fills only
   happen when you like really dig in").
3. *Chaos loom* — MODIFY high and/or overdubbing against rule 4's displacement: aleatoric
   sequencing where you respond to where notes landed (patch C5).

**Arranger lens:** Burst is the channel's **step sequencer** — it converts *time-domain*
material into *event-domain* material. LENGTH is the tempo fader; the loop is the sample pool;
overdubs are pool edits, not pattern edits. Feed it a drum machine and it's a live remixer;
feed it muted guitar and it's an MPC with opinions.

### 5.2 Radio — five loopers, one dial (the genre arranger)

🟢 (pp.13, 36–37): "five distinct loopers that take the same recording and interpret it into
different genres spread across various stations. You can scan freely between the stations,
introducing interference and combining the different loops." **MODIFY scans; LENGTH means
something different per station; the stations share the loop.** Between stations: "noise and
filtering and disruption" 🟡; each station has "a clean, pure version… Simply scan the MODIFY
knob until you reach an area where the static parts, and you will know you've arrived" (the
manual's **DON'T TOUCH THAT DIAL** aside, p.36). 🟡 Walkthrough addition: "in these in-between
zones, you're also able to blend different stations together. So you can have two at once
playing" — note the phrasing "**each station has a clean version of itself** that you can find":
the clean spots are zones inside each station's territory, not single points. 🟡 Johnston on the
crossovers: both adjacent loopers run **in parallel** plus interference — "dialing in those
stations does not come without noise" — and his two favorite blend recipes: Orchestral/Ambient
midpoint = voices + time-stretch + radio noise simultaneously, "**and you can overdub into
that**"; Shoegaze/Dance midpoint = "that frozen-in-place quality of shoegaze and that stuttery
dance move."

Station order across MODIFY, counterclockwise → clockwise, with exact MIDI values for the clean
spots 🟢 (MIDI manual p.4 "RADIO STATIONS (CC19)"):

| # | Station | CC19 | LENGTH = | First-party character + what's known beyond the manual |
|---|---|---|---|---|
| 1 | **TAPE** | 0 | Speed / Direction | "Plays your loop back in full with no funny business, but lets you change its playback speed and/or direction." 🟡 Walkthrough: "an interpretation of tape that you find in Mood Mark II." 🟡 Johnston: "a speed and direction control." **The only *direct* reverse control in the pedal** (owner + reviewer consensus — but see Orchestral's SPREAD trick, next rows). Half-speed+reverse = the classic MOOD memory move (patch B7). |
| 2 | **AMBIENT** | 32 | Playback speed | "Maintains the pitch of your loop but lets you slow it down dramatically, turning it into a cinematic blur." 🟡 Walkthrough: "without changing the pitch, slow down the loop dramatically… a soundscape," and the pure version "is aided by a bit of Soup." 🟡 Johnston on its texture: slowing "stretches the notes… but you get all this **transient glitchy information** because it's not changing the pitch at all." 🟡 Owners: **forward-only** (no reverse, unlike MkII Stretch); speed spans the *whole* knob (finer control than MkII's half-knob); **no grain-size control**; character likened to "really early Ableton timestretch… old Akai vibe." 🟡 **Owner freeze trick:** snap LENGTH fully CCW at the chosen moment → that slice repeats indefinitely at pitch; there's a rough artifact zone at the very bottom — pass it, then ease back (patch A5). |
| 3 | **ORCHESTRAL** | 63 | # of voices | "A symphony of different voices that come in and out, creating a unique arrangement of your loop." 🟡 Walkthrough: "different voices playing different parts of your loop… popping in and out and creating a complete loop together, **playing at different speeds for different moments**." 🟡 **Johnston, with the SPREAD dip on: Orchestral plays the loop in reverse on one side and forward on the other** — huge width, deep obfuscation of the original part (so hidden reverse *does* exist here, stereo-only). His single-chord recipe: erase, capture one chord — Orchestral plays it "at a variety of speeds and pitches." The literal *arranger* station (patches A8, D5). |
| 4 | **SHOEGAZE** | 97 | Moment selector | "Converts your micro-loop into a collection of **frozen moments that last forever**. You can then navigate through different stacked layers of those moments." 🟡 Walkthrough: slices repeat "kind of like soft feeding clouds," stack e.g. the very beginning + very end simultaneously; at the extreme "all of the loop — beginning, middle, end — playing in like a little repeating tower"; always "soft"; **longer loops give phrase-sized slices, short loops give short repeating grains** (patch A6). 🟡 Johnston: "automatically chops up your micro loop into frozen sections that play back forever. And you can move between them using the length knob." |
| 5 | **DANCE** | 127 | Rotation speed | "Rotates steadily between three different versions of your loop: Half speed, double speed, and normal speed. Club night at the circus." 🟡 Walkthrough poles: "slow and ambient with it, or more percussive" (patch B6). 🟡 Johnston hears it as resampling "in a very kind of **side-chainy** way… chopping up the loop into progressively more stuttery effects" as LENGTH rises. |

**Arranger lens:** Radio is the **genre re-arranger** — one recording, five orchestrations, plus
tuned static and two-station blends as transitional material. The performance surface is MODIFY
(hard cuts via CC19 jumps: 0/32/63/97/127; smears by hand — patch C1), and LENGTH is a different
*arrangement parameter* at every stop: transport (Tape), tempo-of-time-itself (Ambient),
ensemble size (Orchestral), which-moment (Shoegaze), rotation rate (Dance).

### 5.3 Mask — the loop disguiser (the dynamics arranger)

🟢 (pp.13, 38): "a noise-sensitive mode that takes the **loud parts** of your loop and turns
them into something new. Any sound over the volume threshold is changed in a way of your
choosing, giving you a musical push and pull as the mask turns on and off."

- **MODIFY** = threshold — "the higher this is turned up, the more of your loop will be
  disguised." Two named extremes 🟢: **THRESHOLD SURFING** — sit where "only the transients of
  your notes are masked, creating mysterious, ear-catching bursts" (patch C2) — and full-CW,
  where "the mask [applies] at all times… Each loop you record will bring out a different
  response."
- **LENGTH** = "the character of the mask" — *what* the disguise is. The manual never enumerates
  the characters ⚠️; the demos together map the sweep 🟡: **minimum = "crumbly gates… a
  mechanical sputtering failure"** (walkthrough) → "very smooth, flowy stuff" → a **distortion**
  zone → a **time-stretching / pitch-shifting** zone (Johnston, called out mid-sweep) →
  "obliterated, noisy stuff" at the top (patch C3). Johnston's overall verdict: Mask is "the
  most straightforward and predictable of the three," and MODIFY-min is his default "cleanest
  possible version of a micro looper" throughout his demo — the escape hatch verbatim: "you can
  get back to your clean, original loop… by minimizing your modify control."
- **MODIFY min = the pure loop** — the manual's **A GOOD LISTEN** (p.38): "you will be hearing
  the pure micro-loop recording… also a good position for building up a micro-loop if you want
  more precision, before bringing it into the other modes." The channel's monitor/edit bay
  (patch E1). 🟡 Walkthrough agrees: "the stable-est of the micro looping modes… great if you
  want something controlled. Just turn modify down."
- 🟡 Feedback loop with your material: "if I was to add more noise to this loop, it would just
  change the way that the mask is reacting" — the disguise re-triggers off whatever the loop
  currently contains, so overdubs re-choreograph it.

**Arranger lens:** Mask is a **dynamics-keyed arranger** — it splits the loop into
above-threshold and below-threshold populations and re-orchestrates only one of them. Surf the
threshold and the *arrangement decision* ("which notes get the effect") is made per-event by the
loop's own dynamics — an auto-mixer for texture.

## 6. Freeze vs loop — two different infinities

They're on opposite footswitches and are frequently confused 🟢 (pp.10, 22):

| | Wet FREEZE (hold left) | Micro-Looper (right) |
|---|---|---|
| What repeats | the Wet Channel's *current sound* — per mode: Soup = ambient pad, Relay = looping echo, Flip = repeating chord | the recorded buffer |
| Length | not length-based — an infinite sustain | the CLOCK-defined loop window |
| Survives knob moves | yes — and CLOCK *transposes* it | yes; modes re-interpret it |
| Records your playing | no ("play overtop without being recorded" — the 2-Track punch-out) | only in overdub/always-listening states |
| Persistence | while held/latched (LATCH dip) | until replaced |

The powerful moves live in the crossings: freeze → capture (Synthetic Starter, A2; the frozen
pad is Wet output, so the always-listening state records it — rule 1); loop → freeze (dunk a
loop in Soup via ROUTING-down, then freeze the *processed* result and replace the loop
underneath it); freeze-as-punch-out while the looper holds the bed (2-Track, B1).

🟡 **The resample ladder** (Mark Johnston, demonstrated): capture a loop → run it into the wet
channel → **freeze the result** → turn the looper off (always-listening resumes) → the frozen
sound is re-captured as the new loop — "just hand it back and forth for forever." Or route the
frozen material through Relay/Soup, freeze the *reverb*, reshape it in real time with the knobs,
"and now that's captured into the loop instead." Every rung is rule 1 (§4) applied recursively;
combined with CLOCK steps between rungs it's an infinite-generation instrument (the manual's
Trail Catcher is rung one of this ladder).

## 7. Routing: where the loop sits in the signal

🟢 (pp.40–41): ROUTING (face toggle) decides what the Wet Channel processes **when both
channels are on**: input only / input + loop / loop only. For the looper specifically:

- **Loop-only** (down) is the *arranger monitor*: your instrument stays clean while the loop is
  re-orchestrated — "dunk your micro-loops into the Soup, but leave your instrument clean as you
  play over top." The dry-lead-over-processed-bed posture (A5, B8, D5).
- **Input-only** (up) protects a precious loop from further processing — but remember rule 1:
  the moment you bypass the looper it hears the wet anyway.
- **Both** (middle) is the everything-in-the-pool posture (A1, C8).
- **Wet loops are 100% wet** unless BLEND restores the clean loop (§4).
- Per-channel SPREAD (hidden, on ROUTING while in hidden mode) can keep **the loop mono inside a
  stereo wet field** — the manual's own example — or the reverse (patch E5). Per-channel EQ
  exists via MIDI only (CC85: wet-only / both / looper-only).

**Stereo capture facts** 🟡 (Mark Johnston, demonstrated):
- **The loop records in stereo and keeps what it hears:** capture a loop while the wet side is
  doing stereo widening and "the loop retains that stereo image **even after SPREAD is turned
  off** — because it received it in stereo from the delay side." Baked-in width is a one-way
  door; if you need a mono loop, capture with SPREAD off (or per-channel SPREAD = wet-only won't
  help once the wet is *in* the recording — rule 1 again).
- **True-stereo placement without SPREAD:** running dual-mono, the looper's playback "lands
  exactly where [the] audio pieces are hitting on the left and right channels" — a stereo rig's
  imaging passes through the loop faithfully.
- **Orchestral + SPREAD = reverse left / forward right** (§5.2) — the widest, most disorienting
  station configuration and the pedal's only stereo-reverse trick.

## 8. Cross & Glue as they touch the looper

- **CROSS/INPUT MOD** 🟢 (p.43): the looper can be **modulation source** (INPUT MOD right — the
  loop's dynamics bend/duck the wet channel: patch C7) or **modulation target** (INPUT MOD left —
  the wet channel's swells interfere with the loop). With CROSS as the intensity ("slight
  squiggles" → "total dropout/failure" 🟡). A Burst pattern is the sharpest source (periodic,
  spiky); a Soup swell is the smoothest. The manual's headline: "use one channel to modulate the
  other, creating a living sense of interconnectedness within the pedal."
- 🟡 **CROSS is amplitude-gated in real time** (Mark Johnston, demonstrated): the disruption
  tracks the source's level moment to moment — "by holding up my note, I can keep it broken";
  release and the pitches "come in and out of fidelity" as the source decays. So the looper as
  source doesn't just *color* the wet, it **gates its brokenness in the loop's rhythm** — a
  side-chained destruction, sustained wherever the loop sustains.
- **GLUE** 🟢 (p.42): end-of-chain, both channels always — the loop cannot escape it. Low =
  "warm up and gel the two channels" (the loop and wet fuse into one body); high = "completely
  thrash" (🟡 torn-speaker → bit-crush). 🟡 What it *is*, per the demos: Johnston hears "a
  compressor limiter thing that quickly becomes something that really mangles your sound as you
  press into it hard"; Hilowitz places it precisely — "at the end of the signal chain, there's a
  saturation effect… like recording on a tape recorder [with] the input level too high" — and
  found the default "plenty." 🟡 First-owner note agrees: the *default* is already hot enough to
  color clean pads — check GLUE before blaming a mode for grit. DRY GLUE extends it to the dry
  signal (and MIX-down turns the whole pedal into a stereo saturator, E2 — no looper involved at
  all).

## 9. MIDI control surface of the looper

🟢 (MIDI manual pp.3–4; full pedal map in the library Part I §7.3):

| CC | Function | Notes |
|---|---|---|
| 103 | Micro-Looper bypass | 0 = bypass (⚠️ = REPLACE begins), ≥1 = engage. Rhythmic CC103 toggling = automated Eraser Head / Trail Catcher |
| 106 | OVERDUB | 0/≥1 — hands-free latched dubbing from a controller |
| 16 | LENGTH | 0–127 — station parameter / pattern speed / mask character by mode |
| 19 | MODIFY (looper) | Burst sensitivity · **Radio stations: 0/32/63/97/127 clean spots** · Mask threshold |
| 23 | Looper MODE | Burst 0–1 · Radio 2 · Mask ≥3 — FREE PLAY means PC-less mode jumps mid-song are safe |
| 18 | CLOCK | stepped table in the library; automate for harmonized loop transposes |
| 26 | FADE | decay-while-overdubbing valve |
| 31 | SYNC | 0–1 looper→wet · 2 none · ≥3 wet→looper |
| 29 / 25 / 30 | BLEND / BALANCE / MASTER VOLUME | the loop's mix bus |
| 54 | Looper clock division | 0–8 (1/32 → double-whole), saved globally |
| 51 | MIDI clock follow/ignore | sub-60 BPM warps existing audio; Synth Mode ignores clock |
| 85 | EQ per channel | ≥3 = looper-only EQ (MIDI-only feature) |

Plus **Synth Mode** (any MIDI note): the looper becomes an oscillator bank — the MIDI manual's
own recipe is Radio + a few overdubs + **LENGTH and MODIFY both at 11 o'clock**, keys
transposing the result in semitones (patches D6–D8). Presets: PC 1–122 recall everything
including dips; **whether the audio buffer itself survives a preset change is unpublished** ⚠️.

## 10. Techniques cookbook (looper-centric quick index)

Verified-behavior techniques, each expanded as a full patch in the library:

| Technique | Core rule(s) | Patch |
|---|---|---|
| Retroactive grab ("it's in there") | §1 | A1 |
| Synthetic Starter (freeze → seed the loop) | §4 r.1, §6 | A2 |
| Trail Catcher (blink = bake the trails in) | §4 r.1, §2 | A7 |
| Eraser Head (bypass = punch-in/erase) | §2 REPLACE | C4 |
| 2-Track (Relay + freeze + SYNC-left) | §3 sync, §6 | B1 |
| Loop-locked grid (SYNC-right) | §3 sync | B8 |
| Stable Sequencing (build in Mask, switch to Burst) | §5.1, FREE PLAY | B4 |
| Dig-in fills (Burst threshold duet) | §5.1 | B5 |
| Misplaced-overdub composition | §4 r.3–4 | C5 |
| Station surfing & two-station blends | §5.2 | C1 |
| Ambient LENGTH-snap freeze 🟡 | §5.2 | A5 |
| High-CLOCK headroom capture 🟡 | §3 | A5 var. |
| Multi-speed harmony overdubs (CLOCK during dub) | §3 | A8 var., C5 var. |
| Threshold Surfing / A Good Listen | §5.3 | C2, E1 |
| Looper-as-delay (FADE + latched dub) | §4 FADE | E4 |
| Loop as Cross modulator / target | §8 | C7 |
| Genre-hard-cuts via CC19 | §9 | C1 var. |

## 11. Labor division: this looper vs the MkII's vs Blooper

For the rig question "which looper do I reach for": 🟣 framing on 🟢/repo-documented facts.

- **BAD MOOD Micro-Looper** = the *reinterpreter*. Fragments, retroactively grabbed, endlessly
  re-orchestrated (sequence / genre / disguise). No stop, no undo, no song structure — the loop
  is raw material, not a composition. Its "arranger" nature is the point: the same four notes
  become a step pattern, a symphony, a tower, or a club night without re-recording.
- **MOOD MkII Micro-Looper** = the *soft sibling* — same fishing workflow, but pointed at dreamy
  granular (Stretch grains, Env-triggered slices, reversible Tape). Reach for it when you want
  reverse-anything, grain-size control, or the pristine end (owner consensus: BAD MOOD is less
  conventionally granular, forward-only outside Tape 🟡).
- **Blooper** (repo corpus) = the *composition looper*: song-length, layered, undo/redo,
  modifiers, stable. Structure lives there. The natural chain remains: BAD MOOD reinterprets a
  moment → Blooper commits the keeper to the song.

## 11.5 Demo-sourced margin notes (wet side as it feeds the looper, + reception)

Facts from the demo mining that don't fit the looper sections but matter to loop-building 🟡:

- **Soup under CLOCK** (Johnston): max CLOCK = "hi-fi, snappy, no stretching"; min = "grittiest,
  grainiest, most broken" — pick the register *before* a Trail Catcher pass, since the capture
  bakes it in. Hilowitz adds: Soup has "a sort of brittle resonance… the more notes you play,
  the more noticeable it is" — dense loops feed that resonance.
- **Relay's ending** (Hilowitz): at max MODIFY repeats pile up, then "after a while it just kind
  of stops dead" — a hard cutoff, no fade. Johnston: "no real sense of which repeats are newer
  and which are older"; full-wet Relay = "its own form of Frippertronics sound-on-sound looper";
  low CLOCK stretches and grimes the pile.
- **Flip under low CLOCK** (Johnston): harmonies arrive "further delayed, time-stretched… very
  angry, very dark, very gritty, very sluggish pitch shifts" — the doom register of D4.
- **Flip knob-direction discrepancy, resolved:** Knobs demos MODIFY ascending through 1 → 2 → 3
  → 4-note zones; Johnston says "the further clockwise you go, both the fewer notes and the more
  the notes cascade down." The **MIDI manual's CC17 chord table settles it**: chords 1–6 (single
  interval) sit at low values, 41–48 (four-note) at the top — **more notes as MODIFY rises**.
  Knobs and the table agree; treat Johnston's line as a misspeak (his cascade-direction
  observation may still describe the *voicing* of the upper chords, several of which stack
  downward intervals).
- **Flip freeze** (Johnston): Flip has "no regeneration… you're getting one jump each" — freeze
  is what sustains a Flip pattern (why Chord Looper, D1, is a freeze technique).
- **Reception, for the record:** Jason Mays — "the implementation of the micro looper is by far
  the best that I've seen on a Chase Bliss pedal… it surpasses MOOD, and I find it to be a bit
  more musical." Harp Lady — Flip is "like Slip, but better… almost like a Rainbow Machine,"
  and "a lot of it was designed from the ground up and then placed into Mood's existing
  interface." Knobs — Radio is "probably the best mode in Bad Mood… To me, this is kind of peak
  Bad Mood. It's everything." Elektronauts pre-arrival read (Azzarole): "Burst in particular
  seems to be great… I'd happily take the right side and put it in my standard Mood; these algos
  seem a lot more useful than the microlooper on standard Mood" — though he judges the pedal
  overall guitar-leaning rather than synth/drum-machine-first. Owner dizzy's honest framing of
  the whole box: "you could get pretty close to a Bad Mood sound with bitcrushing/sample-rate
  reduction, overdrive, reverbs etc, it just wouldn't be as immediate."
- **Secondaries confirmations** (Johnston): all hidden options are *labeled on this pedal*
  (unlike MOOD MkII); MIX-alt is the loop-vs-wet **BALANCE** ("crank reverb mix without drowning
  the loop, or vice versa"); hidden-options reset = preset-toggle ×3 with a marquee-LED confirm;
  SYNC engages via hold-footswitches + wet MODE toggle, giving "**properly quantized micro loops
  in a Mood, which for a long time felt like happy accidents only**."

## 12. Open questions (measure when the unit arrives)

1. **Loop length in seconds** at each CLOCK step, with and without HALF (§3) — measure via LED
   blink; log the table here.
2. **Does the audio buffer survive preset changes / power cycles?** Unpublished (§9).
3. **SYNC-right subdivision set** — which rhythmic steps TIME takes (§3).
4. **Overdubbing's "predictable settings"** — confirm the p.32 graphic against hardware (§4 r.3).
5. **Mask LENGTH character zones** — partially mapped by the demos (min = crumbly gates →
   smooth/flowy → distortion → time-stretch/pitch-shift → obliterated, §5.3); confirm zone
   boundaries on hardware.
6. **Radio in-between zones** — how wide each clean zone is; whether blends are equal-power.
7. **Burst step detection** — what counts as "unique" (level? spectral change?); max step
   granularity vs CLOCK; whether the loop's own playback can trip the fill threshold.
8. **Wet-channel pitch behavior when CLOCK moves under a loop** — scope of the owner report (§3).
9. **Whether the LED blink continues in playing/overdub states** (manual specifies recording
   only).
10. **CC22/31/32/33 endpoint orientation** — inherit the library's flag; confirm which value is
    which side.
11. **Orchestral's SPREAD reverse-one-side behavior** (Johnston-demonstrated) — confirm whether
    it needs the SPREAD dip, per-channel SPREAD on the looper, or both; and whether other
    stations have SPREAD-specific behaviors.
12. **SYNC-left loop quantization** — Johnston's "properly quantized micro loops" suggests
    grabbed loops snap to the TIME length; confirm whether the grab quantizes the seam or just
    the window size.

## Sources

- **Manual (Field Guide)** — `../manuals/Bad-Mood_Manual_Chase-Bliss.pdf`, looper chapter pp.30–38, routing pp.40–41, customize/ramping pp.44–47. The 🟢 backbone of §§1–7.
- **MIDI Manual** — `../manuals/BAD-MOOD_MIDI-Manual_Chase-Bliss.pdf`, CC map + stations + clock/divisions + Synth Mode. §9.
- **Mark Johnston, "Chase Bliss BAD MOOD | Secret Weapons"** — youtube.com/watch?v=KBY0gqpfpHw
  (1h20m, full transcript captured 2026-08-28): the deepest parameter-by-parameter source —
  circular-buffer mechanics, Burst step-size/scramble-recovery, Mask sweep zones + escape hatch,
  Orchestral SPREAD reverse/forward, station-blend recipes, stereo-image retention, FADE hold,
  amplitude-gated CROSS, Glue-as-compressor/limiter, the resample ladder, SYNC "properly
  quantized micro loops," labeled secondaries.
- **"BAD MOOD – Walkthrough" (Knobs)** — youtube.com/watch?v=5UgwxdzB9CQ, full transcript captured 2026-08-28 (station-by-station demo, Burst note-by-note construction, Mask sweep poles, blending, "it's in there," loops-persist-across-modes, sync/fade/synth acknowledged-not-demoed).
- **David Hilowitz, "BAD MOOD: chasing the distorted side of ambient"** —
  youtube.com/watch?v=Z1B3pCYEKVo (12m49s, transcript captured): harmonically-useful CLOCK
  steps, Relay's dead-stop pile, Glue placement/level, the ephemerality framing; Bastl Kalimba
  source, side-by-side with MOOD.
- **Harp Lady (Emily Hopkins)** — youtube.com/watch?v=uIXLHh-HYzU (12m18s, transcript captured):
  played demo; Flip "like Slip, but better… almost like a Rainbow Machine"; ground-up design
  quote. **Jason Mays** — youtube.com/watch?v=9JAAUfurXmw (8m42s): reception only ("best micro
  looper on a Chase Bliss pedal"). **ambienttrash** (qrHkNQnEAF8) and **Daniel Saint**
  (eoXawwPy4E4): music-only, no extractable narration. The rumored Zack/Courtney
  "every-instrument" video could not be located on the official channel as of 2026-08-28.
- **"Introducing – BAD MOOD"** — youtube.com/watch?v=DRNCfhESRA4 (positioning only).
- **Elektronauts CB megathread pp.150–155** — elektronauts.com/t/chase-bliss-effects-pedals/31096:
  **the entire public owner pool as of 2026-08-28** (thread confirmed to end at post #3154 via
  the Discourse API — first deliveries Aug 26–28 in AU/US, EU still in transit). Contents:
  Ambient freeze trick with audio clip, headroom trick, forward-only stretch / whole-knob speed /
  no grain size, direct-reverse-only-in-Tape, hot Glue default, Soup phaser tell, the
  wet-repitch and no-grain-slicing limits (#3149), the dub-techno/ambient same-loop demo clips
  (#3149/#3151).
- **Press** — gearnews, Synth Anatomy, Delicious Audio, No Treble, GuitarPedalX (launch coverage;
  all reprint the manual's mode copy, no hands-on measurements; GuitarBomb's Cross-access
  description is garbled — disregard it). Chase Bliss's generic **Dip Switches 101** PDF adds
  nothing Bad Mood-specific (its loop-synced-ramp feature is Blooper-only).
- **Known-but-unreachable (future mines):** TheGearPage thread "**2026 Small batch bliss — Bad
  Mood, L&F**" (started ~Jul 26 — bot-walled); all of Reddit; the CB Discord; YouTube
  comments/chapters. Additional demo roster with no extractable narration: Mike Hermans
  (9iKqfEVR6vo), the Jorb demo, a Duskmos video announced as incoming. lines (llllllll.co) has
  essentially no Bad Mood discussion yet. No support site or FAQ exists (help@chasebliss.com
  only); the printed Field Guide isn't online.
- **Repo cross-refs** — `Patches/Chase Bliss Bad Mood/Bad-Mood-Patch-Library.md` (control reference + the 40 patches indexed in §10); `gear/Chase Bliss MOOD MkII/research/` (MkII looper comparison); Blooper corpus (labor division §11).

<!-- DEMO-FINDINGS -->
