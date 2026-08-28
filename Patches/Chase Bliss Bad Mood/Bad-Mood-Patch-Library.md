---
type: patch-library
title: Bad Mood Patch Library
device: Chase Bliss Bad Mood
date: 2026-08-28
description: "Control reference + 40-patch library for the Chase Bliss BAD MOOD (2026 Small Batch Bliss two-channel ambient multi-effect — always-listening Micro-Looper with Burst/Radio/Mask modes, Wet Channel with Soup/Relay/Flip modes, harmonized-step CLOCK, global GLUE saturator, CROSS inter-channel modulation). Matches the depth and organization of the Big Time patch corpus: per-patch knob positions, toggle/mode states, hidden options, dip switches, MIDI CC snapshots, use cases, playing tips, and variations, grouped by intent. Every control behavior is sourced to the manual/MIDI manual; numeric knob positions are dialable starting points unless flagged otherwise."
tags: [patch-library, ambient, looper, micro-looper, spectral-reverb, glitch, harmony, chase-bliss, control-reference]
---

# Chase Bliss Bad Mood — Control Reference & Patch Library

> **New-product honesty (2026-08-28):** BAD MOOD is a **Small Batch Bliss** made-to-order run —
> $399, order window closes **Aug 31 2026**, current estimate for new orders **~November 2026**,
> and Chase Bliss says Small Batch won't return for at least two years. The **first units landed
> with owners Aug 26–28** — the owner-report pool is literally days old (a handful of posts on
> the Elektronauts Chase Bliss megathread, pp. 151–155). So: **no seasoned tip culture, no
> firmware lore, no community recipe library yet.** The canon is the **manual (27 pp.)**, the
> **MIDI manual (9 pp.)**, the product page/blog, the two official videos (media by Knobs, who
> also wrote the launch blog), and the first press demos. Chase Bliss ships only **two factory
> presets** (toggle slots 1–2) and documents their contents nowhere. Everything here is flagged:
> 🟢 **verified** (manual / MIDI manual / product page — behavior stated first-party),
> 🟡 **video/demo-sourced** (official videos or press coverage), 🟣 **designed** (an unpublished but
> dialable starting point built on verified behavior — Chase Bliss publishes character, not numbers).

---

# Part I — Control Reference

## 1. What it is (architecture)

BAD MOOD is a **two-channel multi-effect**: one channel **samples and loops brief moments**
(the Micro-Looper), the other is a collection of **real-time spatial effects** (the Wet Channel).
Both exit through a global **GLUE** saturator/destroyer. The channels are **aware of each other**:
you can process the micro-loops with the spatial effects, record those effects into the loops, or
use either side to modulate and interfere with the other (CROSS / INPUT MOD). 🟢 (manual p.3)

It is **not a MOOD MkII sequel** — Chase Bliss calls it a sibling/inversion: *"MOOD MKII captures
the soft, dreamy side of ambience, and BAD MOOD explores the raw, reckless side."* It shares the
MkII's control scheme but was **built from scratch**. 🟢 (bad-mood-blog)

**Signal flow:** input → (Micro-Looper ∥ Wet Channel, with ROUTING deciding what feeds the Wet
Channel) → **GLUE** → output. Dry path is **analog, buffered bypass** (true bypass available via
gesture; the always-listening looper stops working in true bypass). 🟢 (manual pp.16, 42)

**Face layout:** 6 knobs — top row **MIX · CLOCK** (shared); Wet Channel **TIME · MODIFY**;
Micro-Looper **LENGTH · MODIFY**. 3 toggles — **Wet MODE** (Soup/Relay/Flip), **ROUTING**,
**Looper MODE** (Burst/Radio/Mask), plus the **PRESET** toggle between the footswitches.
2 footswitches — left = Wet Channel (tap bypass / hold FREEZE), right = Micro-Looper
(tap record⇄playback / hold OVERDUB). 🟢 (manual pp.8–13)

**Power / I/O:** 9V DC center-negative, **~200 mA**. Mono, stereo (TRS), or mono-in/stereo-out
(MISO dip). Stereo I/O with analog dry-thru; many stereo rigs need TRS→dual-TS cables.
🟢 (manual pp.2, 4)

## 2. Shared controls

### MIX
Balance between input signal and BAD MOOD — **controls both channels simultaneously**. When
ramping is engaged (any control-bank dip ON), MIX is repurposed as **ramp speed**; hold the left
footswitch while turning to adjust actual mix during ramping. 🟢 (manual pp.8, 46)
Channel-vs-channel loudness is NOT set here — that's the hidden **BALANCE** option (§5).

### CLOCK — the sample-rate master
Sets BAD MOOD's **sample rate**, which controls the **length and resolution of the Micro-Looper**
and the **quality and time of the Wet Channel** — "tone, length, and quality, all in one."
It moves in **musical, harmonized steps**: dropping 64k → 32k halves the speed of the micro-loop
*and* the Wet Channel effect. 🟢 (manual p.20)

The 11 steps (from the MIDI manual's stepped-clock chart, CC18): 🟢

| Step | CC18 value | Step | CC18 value |
|---|---|---|---|
| 2k  | 0–4    | 16k | 70–83   |
| 3k  | 5–16   | 24k | 84–95   |
| 4k  | 16–28  | 32k | 96–109  |
| 6k  | 29–40  | 48k | 110–121 |
| 8k  | 41–53  | 64k | 122–127 |
| 12k | 54–69  |     |         |

Full ladder: **2k · 3k · 4k · 6k · 8k · 12k · 16k · 24k · 32k · 48k · 64k**.
The ratios alternate ×1.5 / ×1.33 — i.e. each step transposes by a **perfect fifth or fourth**,
with every second step landing an octave. That's what "harmonized steps" means in practice:
CLOCK is a musical transposer, not a free-running rate knob. 🟣 (derived from the 🟢 step table;
the manual says "musical, harmonized steps" without listing intervals)
⚠️ The printed chart gives 3k as 5–16 **and** 4k as 16–28 — value 16 is listed twice; treat 16 as
a boundary value and avoid it when programming. 🟢 (MIDI manual p.4, as printed)

- **SMOOTH dip** removes the stepping for fluid sweeps (pitch-bend glides). 🟢 (manual p.45)
- **Overdub exception:** CLOCK may be moved freely **while overdubbing** and existing notes stay
  where you played them — the sanctioned way to build harmonies at different speeds. 🟢 (p.33)
- Signature move: play a note, roll CLOCK down while the ambience decays, play again — the whole
  character has dropped in harmonized steps. 🟢 (manual p.21 "try this")

### ROUTING toggle
Decides **what the Wet Channel processes** — only has an effect when **both channels are on**: 🟢 (p.40)
- **Up — INPUT ONLY:** your instrument through the Wet Channel; micro-loops stay clean.
- **Middle — INPUT + MICRO-LOOPER:** everything through the Wet Channel.
- **Down — MICRO-LOOPER ONLY:** loops get dunked; your live playing stays clean over top.

Two riders: 🟢 (pp.40–41)
- **Always-listening override:** when the Micro-Looper is bypassed (recording), it captures the
  Wet Channel's output **regardless of routing** — play through Relay before engaging the looper
  and the repeats are in the loop.
- **Wet loops are 100% wet:** a loop routed through the Wet Channel is *replaced* by the processed
  version; the hidden **BLEND** option mixes the clean loop back in.

### PRESET toggle
Left and right positions are stored presets; middle = **live** (current controls). Save right slot:
hold right footswitch 3 s → hold left footswitch 3 s (middle LED blinks); opposite order for left.
**Dip-switch states are saved with presets.** Via MIDI: 122 slots, PC recall (slot 1 = right,
slot 2 = left, PC 0 = live); no factory presets beyond the two loaded in slots 1–2. 🟢 (pp.18–19; MIDI p.2)

## 3. Wet Channel — Soup / Relay / Flip

The Wet Channel is BAD MOOD's live effects: "unorthodox spatial treats" that process your
micro-loops, input, or both (per ROUTING). Left footswitch: **tap = bypass**, **hold = FREEZE**
(infinite repeat of the current sound). Freeze character per mode: **Soup = ambient pad ·
Relay = looping echo · Flip = repeating chord**. 🟢 (pp.10, 22)

### Soup — synthetic reverb
A **spectral reverb that resynthesizes your playing** — it analyzes and recreates whatever passes
through it, "unnatural ambience that is a distant memory of your instrument"; per the walkthrough,
built from "thousands of little frequency bands that act and behave like a reverb." 🟢 (p.24) 🟡
- **TIME** = decay / size.
- **MODIFY** = character; clockwise emphasizes the synthetic nature. 🟡 Walkthrough detail: it is
  also the **modulation amount** — at zero there's no modulation and Soup is "a more familiar
  reverb"; Knobs "likes to leave it around noon."
- **CLOCK dependency:** Soup is highly CLOCK-dependent — Chase Bliss's own opinion: it "sounds
  best when CLOCK is rolled back"; turning CLOCK up introduces **sparkling artifacts**. 🟢 (p.24 "CLOCK OUT")
- 🟡 Early-owner tell (Elektronauts, days-old): Soup has "a very noticeable phaser-like quality" —
  one owner hears it as another Chase Bliss take on shimmer. Treat as one ear's report.

### Relay — abstract repeater
"A delay that doesn't fade out." Instead of feedback you select a **precise number of repeats
that each share the same volume** — a sampler that's always recording, each sample repeated a
chosen number of times. 🟢 (p.24)
- **TIME** = delay time.
- **MODIFY** = number of repeats; **at max, repeats are stable and pile up like a looper**.
- Because old and new echoes share one volume, old/new can't be told apart — an "audio illusion"
  and "a very fun spin on Frippertronics-style looping." 🟢 (p.25 "WHEN DID YOU GET HERE?")

### Flip — chordcaster
A **pitch shifter that creates layered harmonies but spreads the notes across time** — pitch
shifting → chord stacks → harmonic sequences. 🟢 (p.26)
- **TIME** = lag time between notes (up slightly = "the laggy character of older pitch shifters" —
  the manual's "VINTAGE" HARMONIES tip). 🟢 (p.27)
- **MODIFY** = harmony select: "a variety of different arrangements of 4ths, 5ths, and octaves,
  going both up and down. The higher the knob is set, the more notes will be present." 🟢 (p.26)
  The MIDI manual publishes the full 48-chord map (§7.4): chords 1–6 are single intervals,
  7–21 two-note, 22–40 three-note, 41–48 four-note stacks. 🟢 (MIDI p.7)

## 4. Micro-Looper Channel — Burst / Radio / Mask

An **"always listening looper"** — like fishing for music. It continuously records while bypassed;
turn it on and it keeps **whatever was played most recently** and loops it. Loop length is **not
set manually** — it's set by the **CLOCK** position (HALF dip halves it, matching the original
MOOD's response). 🟢 (pp.30, 45)

**Three states — Recording (bypassed, always listening) → Playing (tap) → Overdubbing (hold):**
- The LED **blinks while recording** to show the current loop length. 🟢 (p.30)
- **No stop command; it's never really off.** 🟢 (p.30)
- **Wet capture:** if the Wet Channel is on while the looper is in its recording state, its
  effects **are recorded into the loop** (any routing). 🟢 (pp.30, 41)
- **FREE PLAY:** once recorded, you can switch looper modes freely without erasing the loop. 🟢 (p.31)
- **REPLACE:** the moment you bypass the channel it starts **erasing the existing loop and
  recording input in its place** — use it to clear space or add glitches. 🟢 (p.32)

**Overdub rules:** 🟢 (pp.32–33)
- Hold the right footswitch to overdub (**LATCH dip** makes holds latching).
- **Wet overdubs are NOT recorded** — you hear the Wet Channel while overdubbing but only the
  clean input is written (prevents a "loud, scary feedback loop"). Wet effects only get captured
  in the always-listening state.
- **Misplaced overdubs:** if a mode's playback mangling is active while overdubbing, audio lands
  somewhere other than where you played it. "ALWAYS UNPREDICTABLE!"
- For **traditional, predictable overdubbing** the manual shows recommended positions graphically
  (p.32). ⚠️ The exact printed positions don't survive text extraction; the consistent reading —
  each mode's "neutral" spot — is **Burst: MODIFY min (envelope off) · Radio: MODIFY on the Tape
  station, LENGTH at normal speed · Mask: MODIFY min (pure loop)**. 🟣 (inferred; see §8 ambiguities)
- **CLOCK is the exception** — move it freely while overdubbing; notes stay put. Different CLOCK
  per overdub pass = harmonies at different speeds. 🟢 (p.33)

### Burst — loop sequencer
Turns micro-loops into **rhythmic patterns of up to 8 steps**. Wherever a "unique" sound is
detected in the loop, Burst creates a step, then cycles the slices into a pattern. 🟢 (p.34)
- **LENGTH** = speed of the pattern / size of each step.
- **MODIFY** = sensitivity of the envelope detector — during playback, any sound louder than the
  threshold **scrambles the pattern** ("fills" that react to your playing).
- Overdubs are recorded into the **underlying micro-loop**, not the sequence — what you hear and
  where you're recorded are disconnected; the steady sequencer keeps it feeling rhythmic. 🟢 (p.34)
- **STABLE SEQUENCING** (manual technique): record the loop in another mode first, then switch to
  Burst; or play short muted notes so slices separate cleanly. 🟢 (p.35)

### Radio — shortwave looper
"Its own little world": **five distinct loopers** that interpret the same recording into different
genres spread across stations. Scanning between them introduces **interference** and combines
loops. 🟢 (p.36)
- **MODIFY** = scan through the stations (static parts between them; each station has a clean,
  pure spot — the manual's **DON'T TOUCH THAT DIAL** tip says to learn each station in isolation).
- **LENGTH** = a different parameter per station: 🟢 (p.37)

| Station | LENGTH does | Character (manual verbatim) |
|---|---|---|
| **TAPE** (CC19 ≈ 0) | Speed / direction | Full playback, "no funny business" — but speed and/or direction change. 🟡 The only *direct* reverse control in the pedal (early-owner + reviewer consensus; the one exception: Orchestral with SPREAD plays reversed on one side — Mark Johnston, demoed) |
| **AMBIENT** (≈ 32) | Playback speed | Keeps pitch, slows dramatically — "a cinematic blur." 🟡 Forward-only (unlike MkII Stretch); speed spans the whole knob = finer control; no grain-size control |
| **ORCHESTRAL** (≈ 63) | # of voices | "A symphony of different voices that come in and out" — a unique arrangement of your loop |
| **SHOEGAZE** (≈ 97) | Moment selector | Loop becomes "a collection of frozen moments that last forever"; navigate stacked layers |
| **DANCE** (≈ 127) | Rotation speed | Rotates half-speed / double-speed / normal — "Club night at the circus" |

**🟡 Early-owner field notes on Radio (Elektronauts, first days of ownership):**
- **Ambient freeze trick:** while the loop plays on the Ambient station, snap **LENGTH fully CCW
  at the moment you want** — that slice repeats indefinitely at preserved pitch. There's a
  "rough, artifact-y" zone at the very bottom of LENGTH; raise past it, then ease back down.
- **Headroom trick:** record loops at a **high CLOCK (1–2 steps/octaves up)** so you have room to
  slow down later "and get more granular at a reasonable pitch." Lowering CLOCK lowers loop
  pitch; some Wet Channel processing may render at its own pitch regardless.
- One owner's context test: same loop → Tape station hard-CCW + Flip with moving TIME = "kinda
  dub techno"; switch to Soup and fiddle MODIFY/CLOCK = ambient pad. The loop is raw material,
  the modes are genres.

### Mask — loop disguiser
**Noise-sensitive**: any sound in the loop over the volume threshold is **changed in a way of your
choosing** — a musical push/pull as the mask flips on and off. 🟢 (p.38)
- **LENGTH** = character of the mask.
- **MODIFY** = threshold; higher = more of the loop disguised.
- **THRESHOLD SURFING** (manual technique): find the spot where **only the transients** are
  masked ("mysterious, ear-catching bursts"), or max MODIFY to mask at all times. 🟢 (p.38)
- **A GOOD LISTEN:** MODIFY fully down = **the pure micro-loop recording** — the monitoring spot,
  and a good position for building loops precisely before mangling them elsewhere. 🟢 (p.38)

## 5. Hidden Options (hold both footswitches — LEDs green)

Hold both footswitches; both LEDs light **green**; each face control becomes a hidden option.
Release to return. Defaults are the manual's pictured positions. 🟢 (pp.14–17)

| Hidden option | Face control | What it does | Default |
|---|---|---|---|
| **EQ** | Wet MODIFY | Two-way **global** EQ: CW removes lows (brighter), CCW removes highs (darker); noon = flat. Per-channel assignment only via MIDI CC85. | noon |
| **CROSS** | TIME | Intensity of the dynamic pitch+amplitude interference modulation (§6.2). | 0 (off) |
| **FADE** | LENGTH | Turn down → loops **gradually fade while overdubbing** — evolving loops, or treat the looper like a delay. | max (unity = no fade) |
| **BLEND** | Looper MODIFY | Blends clean micro-loop back in when it's routed through the Wet Channel (which is otherwise 100% wet). | 0 (fully wet) |
| **GLUE** | CLOCK | End-of-chain saturator/destroyer intensity (§6.1). | "pretty low" |
| **BALANCE** | MIX | Relative loudness of the two channels; center = even. | center |
| **SYNC** | Wet MODE toggle | Left: **Micro-Looper synced to Wet Channel** — loop length now set by TIME. Middle: unsynced. Right: **Wet Channel synced to Micro-Looper** — TIME moves in steps rhythmically related to loop length. | middle (unsynced) |
| **SPREAD (per-channel)** | ROUTING toggle | Applies the SPREAD dip to one channel only — e.g. keep the micro-loop mono but let it pass through a stereo Soup. Middle = both. | both |
| **INPUT MOD** | Looper MODE toggle | Source for CROSS: left = **Wet Channel**, middle = **your input**, right = **Micro-Looper**. | input |

⚠️ Which MODIFY hosts EQ vs BLEND is shown only graphically (p.14); the assignment above follows
the manual's per-option knob icons **and** the MOOD MkII precedent (wet MODIFY = tone,
looper MODIFY = clean-loop blend). 🟢/🟣 (functions verbatim; knob assignment near-certain)

**Reset hidden options to defaults:** preset toggle **left → center three times** → lights blink →
press both footswitches to confirm. 🟢 (p.17)

**True bypass mode:** tap both footswitches **three times** — all three LEDs blink red; tap either
to exit. Bypassed signal is otherwise buffered/analog. **The always-listening looper does not work
in true bypass.** 🟢 (p.16)

## 6. Glue & Cross — the character layer

### 6.1 GLUE (hidden, behind CLOCK)
A **global end-of-chain saturator/destroyer** — "a blend of different ingredients that let you
choose BAD MOOD's base character," applied to **both channels**. Low = "warm up and gel the two
channels"; high = "completely thrash everything passing through the pedal"; flavors in between.
Default is "pretty low, but you should turn it up if you really want to be bad." 🟢 (p.42)
- **DRY GLUE dip** extends GLUE to the dry signal — to mesh wet/dry, or: **MIX fully down +
  DRY GLUE ON = standalone stereo saturator/destroyer.** 🟢 (pp.42, 45)
- 🟡 Lineage & sound: the Glue concept debuted on **Lost and Found**; the intro video insists this
  one is "way different," and GuitarPedalX calls it a refined, more destructive take. The
  walkthrough's characterization of the sweep: "very torn speaker overdrive" rising into
  "interesting bit crushing." Knobs: "I'll be using glue on and off throughout the video. It's
  generally better when it's on, but you can also make it very, very clean."
- 🟡 First owner-report: the **default Glue level was "too hot" for clean pads** for one early
  owner, who turned it down — if a pristine texture is the goal, check GLUE first.

### 6.2 CROSS (hidden, behind TIME) + INPUT MOD
"A unique form of modulation that **dynamically interferes with both pitch and loudness**. It can
modulate itself or be modulated by your playing." **CROSS** = intensity; **INPUT MOD** = source
(Wet Channel / input / Micro-Looper). 🟢 (p.43)
- Simplest demo (manual's own): source = input, CROSS way up, play through **Soup** — "notice how
  it bends and sputters as you play."
- The interesting part: **one channel modulating the other** — "a living sense of
  interconnectedness within the pedal."
- Off by default "to avoid confusion, but don't overlook it!"
- 🟡 Walkthrough characterization: "it interrupts and sabotages the frequency and the volume of
  the pedal in a variety of ways" — the intensity sweep runs from "slight squiggles" to "total
  dropout/failure." Best heard on reverb trails; channel-to-channel routing "makes Bad Mood come
  alive." The intro video bills Cross modulation as "never been done before."

## 7. Dip switches, ramping, external control, MIDI

### 7.1 Right bank — CUSTOMIZE (8 yellow dips; saved with presets) 🟢 (pp.44–45)

| Dip | CC | Function |
|---|---|---|
| **MISO** | 71 | Mono in → stereo out split |
| **SPREAD** | 72 | Stereo processing on — each mode has its own stereo-image approach |
| **DRY KILL** | 73 | Removes clean signal from the output (even bypassed) |
| **TRAILS** | 74 | Effects fade naturally after bypass |
| **LATCH** | 75 | Hold functions (freeze/overdub) become latching |
| **HALF** | 76 | Halves loop length — matches the original MOOD's response |
| **SMOOTH** | 77 | Removes CLOCK's harmonized stepping (fluid sweeps) |
| **DRY GLUE** | 78 | GLUE applies to the dry signal too |

### 7.2 Left bank — CONTROL (ramping / bounce / CV / EXP) 🟢 (pp.46–49)

| Dip | CC | Function |
|---|---|---|
| TIME | 61 | assign wet TIME to ramp/bounce/EXP/CV |
| MODIFY (wet) | 62 | assign wet MODIFY |
| CLOCK | 63 | assign CLOCK |
| MODIFY (looper) | 64 | assign looper MODIFY |
| LENGTH | 65 | assign LENGTH |
| **BOUNCE** | 66 | ON = continuous bounce (LFO-like); OFF = one-shot ramp on engage |
| **SWEEP** | 67 | (B)ottom / (T)op — knob position sets the range's min or max |
| **POLARITY** | 68 | (F) / (R) — travel direction for EXP/CV response |

- Engaging any knob dip engages ramping and **repurposes MIX as ramp speed** (hold left footswitch
  + turn to reach actual MIX). **Ramp** = knobs rise/fall once to the set position at engage —
  "a wave of motion and activity when you first turn BAD MOOD on." **Bounce** = steady continuous
  movement between CLOCK settings/knob range. 🟢 (pp.46–47)
- **CV (0–5 V, floating-ring TRS→TS) / expression (TRS)** auto-detected on the EXP/CV jack; with
  no knob dips engaged, an EXP/CV signal controls **MIX**. 🟢 (pp.48–49)
- **MIDI** arrives on the **MIDI/EXT jack via ¼" TRS** (Chase Bliss MIDIBox converts 5-pin);
  the same jack accepts a **normally-open momentary TS footswitch**, which automatically takes
  over **engaging the Wet Channel** (tabletop use). 🟢 (pp.48–49)

### 7.3 MIDI — full CC map (channel 2 default) 🟢 (MIDI manual pp.2–8)

Change channel: hold both stomps at power-up; the pedal adopts the channel of the first PC it sees.

**Knobs & footswitches**

| CC | Control | Values |
|---|---|---|
| 14 | TIME (wet) | 0–127 |
| 15 | MIX | 0–127 |
| 16 | LENGTH (looper) | 0–127 |
| 17 | MODIFY (wet) — Flip chord table §7.4 | 0–127 |
| 18 | CLOCK (stepped — table in §2) | 0–127 |
| 19 | MODIFY (looper) — Radio stations: TAPE 0 · AMBIENT 32 · ORCHESTRAL 63 · SHOEGAZE 97 · DANCE 127 | 0–127 |
| 20 | RAMP SPEED | 0–127 |
| 102 | Wet Channel bypass | 0 off / ≥1 on |
| 103 | Micro-Looper bypass | 0 off / ≥1 on |
| 104 | Hidden Options | 0 off / ≥1 on |
| 105 | FREEZE | 0 off / ≥1 on |
| 106 | OVERDUB | 0 off / ≥1 on |

**Toggles**

| CC | Control | Values |
|---|---|---|
| 21 | Wet MODE | Soup 0–1 · Relay 2 · Flip ≥3 |
| 22 | ROUTING | input only 0–1 · both 2 · looper only ≥3 |
| 23 | Looper MODE | Burst 0–1 · Radio 2 · Mask ≥3 |

**Hidden options**

| CC | Option | Values |
|---|---|---|
| 24 | CROSS | 0–127 |
| 25 | BALANCE | 0–127 |
| 26 | FADE | 0–127 |
| 27 | EQ | 0–127 |
| 28 | GLUE | 0–127 |
| 29 | BLEND | 0–127 |
| 30 | MASTER VOLUME (MIDI-only — no face control) | 0–127 |
| 31 | SYNC | looper→wet 0–1 · no sync 2 · wet→looper ≥3 |
| 32 | SPREAD per-channel | one-only 0–1 · both 2 · other-only ≥3 |
| 33 | CROSS INPUT (INPUT MOD) | wet 0–1 · input 2 · looper ≥3 |

⚠️ For CC22/31/32/33 the endpoint icons don't survive text extraction; middle values (2) are
printed in words (BOTH / NO SYNC / INPUT) and the endpoints above follow the face-toggle order.
🟢 middle / 🟣 endpoints (near-certain; verify once units ship).

**Misc / global**

| CC | Function | Values |
|---|---|---|
| 51 | MIDI clock | 0 ignore · ≥1 follow |
| 52 | Ramping | 0 stop · ≥1 resume |
| 53 | Wet clock division (saved globally) | 0=1/32 · 1=1/16 · 2=1/8T · 3=1/8 · 4=1/4 · 5=1/2 · 6=dotted 1/2 · 7=whole · 8=double whole |
| 54 | Looper clock division (saved globally) | same 0–8 map |
| 55 | True bypass mode | 0 off / ≥1 on |
| 56 | Factory reset | 0–127 |
| 85 | EQ per channel | wet-only 0–1 · both (default) 2 · looper-only ≥3 |
| 93 | Tap tempo | 0–127 (exit: hold footswitch + turn TIME) |
| 100 | Expression over MIDI | 0–127 |
| 110 | MIDI reset (restores synth-mode globals: clock-ignore off, +3-octave transpose, quarter division, portamento off, gate off) | 0–127 |
| 111 | Preset save | 0–122 |

**Clock sync fine print:** BAD MOOD runs at any BPM/division, but **below 60 BPM it must shift its
internal sample rate — existing audio changes speed and pitch**. Effective BPM depends on the
division (120 BPM at quarter = 120; switch to whole note = 30). 🟢 (MIDI p.4 footnote)

**Presets via MIDI:** PC 1–122 recalls (empty slot = nothing); PC 0 = live. Save = send PC while
holding both footswitches, or CC111. Slot 1 = right toggle, slot 2 = left toggle. 🟢 (MIDI p.2)

### 7.4 Flip chord table (CC17 / wet MODIFY in Flip) 🟢 (MIDI manual p.7)

48 chords across the sweep; intervals are ±4th, ±5th, ±octave. Density rises with the knob:
**1–6 single interval · 7–21 two notes · 22–40 three notes · 41–48 four notes.**

| # | CC17 | Notes | # | CC17 | Notes |
|---|---|---|---|---|---|
| 1 | 0–2 | −Oct | 25 | 64–66 | +5th +4th +4th |
| 2 | 3–5 | −5th | 26 | 67–68 | −Oct −5th +4th |
| 3 | 6–7 | −4th | 27 | 69–71 | −5th +4th +5th |
| 4 | 8–10 | +4th | 28 | 72–74 | +Oct +5th −5th |
| 5 | 11–13 | +5th | 29 | 75–76 | +5th −5th −Oct |
| 6 | 14–15 | +Oct | 30 | 77–79 | −Oct −5th +Oct |
| 7 | 16–18 | −Oct −5th | 31 | 80–82 | −Oct −4th +4th |
| 8 | 19–21 | −5th +Oct | 32 | 83–84 | −4th +4th +Oct |
| 9 | 22–23 | −Oct −4th | 33 | 85–87 | +Oct +5th −4th |
| 10 | 24–26 | −4th +Oct | 34 | 88–89 | +5th −4th −Oct |
| 11 | 27–29 | −Oct +4th | 35 | 90–92 | −Oct −4th +Oct |
| 12 | 30–31 | +4th +Oct | 36 | 93–95 | −5th −4th +5th |
| 13 | 32–34 | −Oct +5th | 37 | 96–97 | −Oct +4th +5th |
| 14 | 35–37 | +5th +Oct | 38 | 98–100 | +Oct −4th −5th |
| 15 | 38–39 | −Oct +Oct | 39 | 101–103 | −Oct +4th +Oct |
| 16 | 40–42 | −5th −4th | 40 | 104–105 | +Oct +5th −Oct |
| 17 | 43–44 | −4th +4th | 41 | 106–108 | −Oct −5th −4th +4th |
| 18 | 45–47 | −5th +4th | 42 | 109–111 | −5th −4th +5th −Oct |
| 19 | 48–50 | −5th +5th | 43 | 112–113 | −4th +Oct −Oct −5th |
| 20 | 51–52 | −4th +5th | 44 | 114–116 | +5th −Oct −5th +4th |
| 21 | 53–55 | +4th +5th | 45 | 117–119 | −5th +4th +Oct −Oct |
| 22 | 56–58 | −Oct −5th −4th | 46 | 120–121 | +5th +Oct −Oct −5th |
| 23 | 59–60 | −5th −4th +4th | 47 | 122–124 | +4th +5th −Oct −4th |
| 24 | 61–63 | +Oct +5th +4th | 48 | 125–127 | +4th +Oct −Oct −4th |

*(Rows 22–48 transcribed from the MIDI manual's four note-columns; the table's column alignment in
the PDF is tight — spot-check the densest chords against the pedal when it arrives. 🟢 with a ⚠️.)*

### 7.5 Synth Mode (MIDI-only) 🟢 (MIDI manual pp.6–8)

Send a **MIDI note** → Synth Mode engages automatically: BAD MOOD becomes a monophonic
instrument, **transposing via the CLOCK knob in semitones** from MIDI notes. Exit: move CLOCK or
send any value to **CC59**. MIDI clock is **ignored** in Synth Mode. Settings save globally.

| CC | Function | Values |
|---|---|---|
| 58 | Output type | 0 = OPEN (constant drone, transposable effect — default) · 1 = ON/OFF (gates with notes, instant attack/release) · ≥2 = ADSR (full envelope; most synth-like) |
| 80–83 | Attack / Decay / Sustain / Release | 0–127 |
| 57 | Octave transpose | 1–9 → +12…+108 semitones |
| 84 | Portamento | 0–127 |
| 59 | Exit Synth Mode | any |
| — | Pitch bend (±4 semitones) / mod wheel | auto-connected |

Velocity is followed in ON/OFF and ADSR modes. Manual walkthrough recipe: freeze Soup with the
LATCH dip on for a base sound, then play keys; or build layered voices with the Radio looper
(overdub a few sounds, **LENGTH and MODIFY at ~11 o'clock**). "Use the exit" — in ON/OFF and ADSR
the pedal is silent without notes; don't forget you're in Synth Mode.

## 8. Bad Mood vs MOOD MkII — what carries over

🟢 unless noted (BAD MOOD manual + `gear/Chase Bliss MOOD MkII/research/`):

**Same skeleton (MkII muscle memory transfers):** two channels (Wet left / Looper right), MIX +
CLOCK masters, always-listening looper with length set by CLOCK, freeze = hold left, overdub =
hold right, hidden options behind both-footswitch hold, true bypass = 3× both-tap (looper dies in
true bypass), reset gesture via preset toggle, MIDIBox TRS MIDI on channel 2, 122 PC presets +
2 face slots, Synth Mode with the same auto-engage-on-note gotcha, CV/EXP via control-bank dips,
MISO/SPREAD/DRY KILL/TRAILS/LATCH/SMOOTH dips, CC51/53/54 clock behavior.

**Swapped guts:** Wet Reverb/Delay/Slip → **Soup/Relay/Flip** (spectral resynthesis instead of
reverb; fixed-count no-decay repeats instead of feedback delay; time-lagged chord stacks instead
of the Slip sampler). Looper Tape/Stretch/Env → **Burst/Radio/Mask** (step-sequencer; five-genre
radio; threshold disguiser). Tape/Stretch/Env behaviors live on *inside* Radio (Tape station =
Tape mode's speed/direction; Ambient station ≈ tape-stretch blur).

**New in BAD MOOD:** face-level **ROUTING** toggle (was hidden SPREAD SOLO-ish on MkII),
**GLUE** (+ DRY GLUE dip), **CROSS + INPUT MOD** inter-channel modulation, two-way **SYNC**
(MkII synced one way), **two-way EQ** replacing the wet-only TONE hi-cut (per-channel via CC85),
**HALF** dip (BAD MOOD's default loop length is the MkII-style longer one; HALF restores original
MOOD response), MIDI-only **MASTER VOLUME** (CC30), published **stepped-clock and 48-chord CC
maps**. Lighter draw (~200 mA vs ~270 mA).

**Gone (vs MkII):** NO DUB dip (FADE covers the evolving-loop territory), CLASSIC mode dip,
ramp-LFO-waveform hidden option (MIX-hidden is now BALANCE).

**🟡 Early-owner deltas vs MkII (days-old reports, Elektronauts):** the time-stretch (Ambient
station) is **forward-only** — MkII's Stretch reverses, BAD MOOD's doesn't; only the Tape station
plays backwards. Stretch speed spans the whole LENGTH knob (vs half on MkII) = finer control, but
there's **no real grain-size control** — BAD MOOD is *less* conventionally granular than MkII
overall. One MkII owner preferred BAD MOOD's stretch anyway. The stretch character has been
compared to "really early Ableton timestretch… old Akai vibe."

**MkII techniques that still apply:** fishing for music (capture through the wet effect — Trail
Catcher is now a named manual technique), freeze-then-capture pads, LEVEL BALANCE (not MIX) to
fix channel loudness, TRAILS for seamless toggling, EXP/CV multi-knob morphs, dry-over-soaked-loop
via ROUTING (now a face toggle), SMOOTH-clock pitch-bend sweeps, in-time capture via SYNC,
"tiny knob differences are crucial" improvisation-first philosophy.

## 9. Ambiguities & open questions (verify when units ship)

1. **Loop length in seconds per CLOCK step** — never published (MkII's wasn't either). The 64k→32k
   halving rule and the HALF dip are the only published anchors.
2. **"Predictable overdubbing" knob positions** (manual p.32) are graphical only — inferred as
   each mode's neutral spot (§4).
3. **EQ vs BLEND knob assignment** in the hidden options — near-certain (icons + MkII precedent)
   but not textual.
4. **Endpoint CC values for CC22/31/32/33** — middle positions are printed; endpoints follow face
   order (🟣).
5. **CC18 value 16** is printed in both the 3k and 4k ranges.
6. **Mask's LENGTH "character" options** — the manual never enumerates what the disguises *are*;
   expect a sweep of textures ("changed in a way of your choosing").
7. **Factory presets in slots 1–2** — contents undocumented anywhere first-party.
8. **Glue's "ingredients"** — described only as "a blend of different ingredients."
9. **SWEEP (B/T) and POLARITY (F/R) letter meanings** — Bottom/Top per the ramp diagram; F/R
   plausibly Forward/Reverse for EXP/CV travel (not spelled out).
10. **Whether CROSS's *depth* differs per source** — the manual describes character ("bends and
    sputters") not ranges.

---

# Part II — Patch Library

**How to read a patch.** Every patch lists: channel states, all six knobs (clock-face + what the
position means), the three toggles + preset slot advice, hidden options (only non-defaults),
dip switches (assume **all off** unless listed), a **MIDI snapshot** (the CC string that
reproduces the patch on channel 2), use case, numbered playing tips, and variations. Sources per
patch: 🟢 = the control routing/behavior is manual-verbatim; 🟡 = official-video/press-sourced;
🟣 = numeric positions are designed starting points (the honest default for a pedal nobody owns
yet — dial by ear, then save to a slot or via CC111).

**Groups** (matching the Big Time corpus organization):
**A. Ambient pads & drones** · **B. Rhythmic & sequenced** · **C. Glitch, noise & broken** ·
**D. Harmony & synth** · **E. Utility, subtle & studio**

## Group A — Ambient pads & drones

### A1 · First Swim
*The manual's own getting-started texture — "turn something polite and small into something wild and large." The reference patch: learn the CLOCK here.*
**Tags:** ambient, texture, radio, soup, starter, verified-workflow

- **Channels:** Micro-Looper ON (Radio) → then Wet ON (Soup).
- **Knobs:** MIX 1:00 (effect-forward but dry audible) · CLOCK 10:00 (≈CC18 55 → 12k — "rolled back" into the murk) · TIME 1:00 (medium-long Soup decay) · MODIFY-wet noon (Knobs's spot: synthetic strangeness blended with familiar reverb) · LENGTH noon (neutral station behavior) · MODIFY-looper explore (scan stations until "you find a spot that you like").
- **Toggles:** Wet MODE **Soup** · ROUTING **middle (input + looper)** · Looper MODE **Radio** · save to a preset slot once it sings.
- **Hidden options:** defaults (GLUE at its low default is part of the sound).
- **Dip switches:** all off (the manual's recommended starting state).
- **MIDI snapshot:** `CC21=0 · CC22=2 · CC23=2 · CC18=55 · CC15=72 · CC14=72 · CC17=64 · CC16=64 · CC19=sweep · CC103=1 · CC102=1`
- **Use case:** the first sound the manual teaches: play a few notes, engage the looper, roll CLOCK back until the fragment becomes "a big, moving texture," scan Radio, then "turn on the Wet Channel and go swimming."
- **How to play it:**
  1. Both channels bypassed; play a few notes (the looper is already listening).
  2. Tap the right footswitch — whatever you just played is looping.
  3. Roll CLOCK back a step at a time; each step drops the loop a harmonized interval and lengthens it.
  4. Sweep looper-MODIFY through the static to audition stations; park on one.
  5. Tap the left footswitch and let Soup resynthesize the whole thing.
  6. Play sparse notes over top; MIX balances you against the texture.
- **Variations:** HALF dip on for a tighter original-MOOD-length fragment · CLOCK to 8k or 6k for tape-rot register · ROUTING down (looper only) to stay dry over the wash.
- **Verification:** 🟢 workflow is manual pp.6–7 verbatim; 🟡 MODIFY-wet noon is Knobs's stated preference; 🟣 remaining numerics.

### A2 · Synthetic Starter
*The manual's named freeze-seeding technique — freeze Soup, record the frozen reverb into the micro-loop, and you have "a nice starting sound to build on."*
**Tags:** freeze, pad, seed, soup, radio, named-technique

- **Channels:** Wet ON (Soup, frozen) → Micro-Looper ON to capture.
- **Knobs:** MIX 2:00 (pad-forward) · CLOCK 9:30 (low — Soup's best register, manual's own opinion) · TIME 2:00 (long decay so the freeze has body) · MODIFY-wet 1:00 (leaning synthetic — the freeze holds the strangeness) · LENGTH noon · MODIFY-looper at a clean station (Ambient ≈ 10:00 area) or Mask-min later.
- **Toggles:** Wet **Soup** · ROUTING middle · Looper **Radio** (or Mask for a pure capture).
- **Hidden options:** defaults; LATCH dip optional so the freeze holds hands-free.
- **Dip switches:** LATCH ON (recommended).
- **MIDI snapshot:** `CC21=0 · CC22=2 · CC23=2 · CC18=48 · CC14=80 · CC17=72 · CC105=1 (freeze) · then CC103=1 · CC105=0`
- **Use case:** building a pad from nothing: the frozen reverb becomes the loop's raw material, so the micro-loop starts life as a sustained, synthetic bed instead of a plucked fragment.
- **How to play it:**
  1. Play a chord or swell into Soup; hold (or latch) the left footswitch to freeze — Soup's freeze is an ambient pad.
  2. Wait a few seconds — let the frozen pad stabilize (manual: "freezing Soup, waiting for a few seconds").
  3. Turn the Micro-Looper on: the reverb is recorded into the micro-loop.
  4. Unfreeze and play through the (still-running) Soup over your new bed.
  5. Reshape the bed with CLOCK (transposes the pad in harmonized steps) and the looper mode of your choice — FREE PLAY means switching modes won't erase it.
- **Variations:** capture into Mask with MODIFY at min for the purest pad, then flip to Shoegaze to tower it · overdub gentle notes with FADE slightly down so the bed slowly evolves.
- **Verification:** 🟢 technique named and described in the manual (p.22 "SYNTHETIC STARTER"); 🟢 freeze-per-mode behavior; 🟣 numerics.

### A3 · Distant Memory Hall
*Pure Soup: the spectral reverb as an instrument-remaker — "unnatural ambience that is a distant memory of your instrument."*
**Tags:** soup, spectral, reverb, pad, low-clock

- **Channels:** Wet ON only (looper bypassed — but remember it's still listening).
- **Knobs:** MIX noon · CLOCK 9:00 (≈CC18 41 → 8k; rolled back, per the manual "in our opinion it sounds best when CLOCK is rolled back") · TIME 3:00 (long) · MODIFY-wet noon→2:00 (raise to "emphasize Soup's synthetic nature"; at zero the modulation disappears and it's "a more familiar reverb") · LENGTH/MODIFY-looper irrelevant (channel off).
- **Toggles:** Wet **Soup** · ROUTING moot (one channel) · Looper any (off).
- **Hidden options:** EQ slightly CCW (darker) to sink the wash behind the instrument.
- **MIDI snapshot:** `CC21=0 · CC102=1 · CC103=0 · CC18=41 · CC14=96 · CC17=64 · CC27=52`
- **Use case:** the everyday ambient patch — a reverb that isn't a reverb, for exploring "impossible spaces and synthetic dreamscapes" under fingerpicking, bowed swells, or synth pads.
- **How to play it:**
  1. Start MODIFY at zero and play — familiar, unmodulated reverb.
  2. Sweep MODIFY up and hear the resynthesis take over; noon is the blend point.
  3. Ride CLOCK: every step down darkens and slows the space a harmonized interval; a step up adds shimmer.
  4. Hold the footswitch anytime for the freeze pad and solo over it.
- **Variations:** **Sparkle Bath** — CLOCK at max (64k) for the manual's "sparkling artifacts that might be your kind of thing," EQ brighter → Knobs's "distant arcade sound" · TIME low + MODIFY high = short synthetic smear, almost a vocoder-y doubler.
- **Verification:** 🟢 all control behavior manual-verbatim (p.24); 🟡 MODIFY-zero = no modulation and the "arcade"/mellow EQ characterizations are from the walkthrough; 🟣 numerics.

### A4 · Sunken Cathedral (Freeze Bed + Live Swimming)
*Soup freeze as a performance drone floor — the LATCH dip makes it a hands-free pedal-point you re-pitch with CLOCK.*
**Tags:** freeze, drone, latch, pedal-point, transposable

- **Channels:** Wet ON (Soup); looper optional garnish.
- **Knobs:** MIX 2:30 (drone dominates) · CLOCK 9:00 start · TIME max (largest space) · MODIFY-wet 1:30 · LENGTH — · MODIFY-looper —.
- **Toggles:** Wet **Soup** · ROUTING up (input only — if the looper joins later, its loop stays out of the Soup so the frozen pad stays clean) · Looper **Mask** for later.
- **Hidden options:** EQ a touch dark; BALANCE center.
- **Dip switches:** **LATCH ON** · TRAILS ON (bypass won't guillotine the pad).
- **MIDI snapshot:** `CC21=0 · CC22=0 · CC102=1 · CC105=1 · CC75=1 · CC74=1 · CC18=41→sweep`
- **Use case:** the one-footswitch drone floor: latch a frozen chord, then use **CLOCK as a chord-change lever** — because the freeze lives in the sample-rate domain, each CLOCK step transposes the drone by the harmonized ladder (fifths/fourths/octaves), which stays consonant with most tonal music.
- **How to play it:**
  1. Swell a chord in; tap-hold left (latched) — infinite pad.
  2. Play the song over it, dry-ish (ROUTING up keeps your live line un-Souped if the looper is on).
  3. At the section change, step CLOCK down one notch: the pad drops a fourth/fifth — an instant "new chord."
  4. Unlatch to release; TRAILS lets it exhale rather than cut.
- **Variations:** SMOOTH dip ON turns the section change into a tape-speed *glide* (portamento drone) · run the pad into Cross (source = input) so your playing makes the drone duck and bend around you (see C6).
- **Verification:** 🟢 freeze/latch/trails/smooth behavior manual-verbatim; 🟣 the CLOCK-as-chord-change application is designed (the harmonized-step transposition it relies on is 🟢).

### A5 · Cinematic Blur
*Radio's Ambient station — the loop keeps its pitch but slows "dramatically... into a cinematic blur," with a little Soup on top (the walkthrough's own pairing).*
**Tags:** radio, ambient-station, timestretch, blur, soundscape

- **Channels:** Both ON.
- **Knobs:** MIX 1:30 · CLOCK 11:00 (roomy loop) · TIME 1:00 · MODIFY-wet 10:00 (gentle Soup — supporting, not drowning) · **LENGTH 9:00–7:00 (playback speed — lower = slower blur)** · **MODIFY-looper ≈10:00 on the clean Ambient spot (CC19 ≈ 32)**.
- **Toggles:** Wet **Soup** · ROUTING **down (looper only — the blur gets Souped, your playing stays clean)** · Looper **Radio**.
- **Hidden options:** BLEND slightly up if you want a ghost of the unprocessed loop; GLUE low default.
- **MIDI snapshot:** `CC21=0 · CC22=127 · CC23=2 · CC19=32 · CC16=32 · CC18=62 · CC103=1 · CC102=1`
- **Use case:** film-scoring in a box: capture any phrase — even a scrappy one — and Ambient turns it into a slow-motion score cue; Soup adds the room the blur lives in.
- **How to play it:**
  1. Capture a phrase (always-listening: play, then tap the looper on).
  2. Park looper-MODIFY on Ambient's clean spot — scan until the static parts.
  3. Pull LENGTH down and hear the loop slow without dropping pitch.
  4. Play melodies over the blur; ROUTING down keeps you dry and separate.
  5. For scene changes, step CLOCK — the whole cue transposes/slows in harmony.
- **Variations:** the walkthrough's exact tip — Ambient "is aided by a bit of Soup" — reverse it: MODIFY-wet high + TIME max for a blur *inside* a dream · nudge MODIFY-looper off-station for tuned static under the cue · **Ambient freeze trick (early-owner, verified in the field):** while the loop plays, snap LENGTH fully CCW at the exact moment you want held — that slice repeats indefinitely at pitch (mind the artifact-y zone at the very bottom; raise past it, then ease down) · **headroom trick:** record 1–2 CLOCK steps high so slowing down later stays at a reasonable pitch.
- **Verification:** 🟢 station behavior + CC19=32 (manual p.37, MIDI manual p.4); 🟡 Soup pairing from the walkthrough, freeze + headroom tricks from first-week owner reports; 🟣 numerics.

### A6 · Tower of Forever Moments
*Radio's Shoegaze station — the loop becomes "a collection of frozen moments that last forever," stacked into "a little repeating tower."*
**Tags:** radio, shoegaze-station, freeze-stack, wall, layered

- **Channels:** Micro-Looper ON (Radio); Wet optional.
- **Knobs:** MIX 2:00 · **CLOCK 12:00–1:30 — deliberately roomier: longer loops give Shoegaze bigger phrase-slices (walkthrough tip); short loops give short repeating grains** · TIME — · MODIFY-wet — · **LENGTH = moment selector: sweep to navigate which frozen moments play, max stacks beginning/middle/end simultaneously** · **MODIFY-looper ≈2:30 on the clean Shoegaze spot (CC19 ≈ 97)**.
- **Toggles:** Looper **Radio** · ROUTING middle if Wet joins · Wet **Soup** for the full wall.
- **Hidden options:** GLUE nudged up — a shoegaze wall wants the gel; SPREAD dip ON for the stereo image.
- **Dip switches:** SPREAD ON.
- **MIDI snapshot:** `CC23=2 · CC19=97 · CC16=sweep · CC18=70 · CC72=1 · CC28=~50 · CC103=1`
- **Use case:** the MBV-adjacent wall: any strummed fragment becomes stacked, softly-fed frozen layers ("soft feeding clouds") you *navigate* with LENGTH rather than replay.
- **How to play it:**
  1. Record a full strummed phrase at a high-ish CLOCK (long loop = big slices).
  2. Flip to Shoegaze's clean spot; sweep LENGTH slowly — you're walking through the phrase's moments.
  3. Push LENGTH toward max: moments stack into the repeating tower.
  4. Add Soup (routing middle) and a bump of GLUE to fuse it into one mass.
- **Variations:** capture *tremolo-picked* material — the freeze-stack turns it into pure texture · record at low CLOCK instead for granular micro-towers · overdub into the underlying loop while the tower plays (misplaced-overdub roulette, see C5).
- **Verification:** 🟢 station behavior + CC value; 🟡 slice-size-vs-loop-length and "tower"/"clouds" language from the walkthrough; 🟣 numerics.

### A7 · Trail Catcher
*The manual's named resample move: run a micro-loop through Soup, blink the looper off/on, and the trails are IN the loop now.*
**Tags:** resample, generation-stacking, soup, named-technique, evolving

- **Channels:** Both ON.
- **Knobs:** MIX 1:00 · CLOCK 10:30 · TIME 2:00 (trails worth catching) · MODIFY-wet noon · LENGTH noon · MODIFY-looper on any clean station (or Mask min for fidelity).
- **Toggles:** Wet **Soup** · ROUTING **down (looper only)** · Looper **Radio** or **Mask**.
- **Hidden options:** defaults; FADE at unity (you're stacking, not fading).
- **MIDI snapshot:** `CC21=0 · CC22=127 · CC23=2 · CC18=58 · CC14=80 · then blink CC103 0→1`
- **Use case:** infinite-generation ambience: each off/on blink re-captures the loop *with its Soup trails baked in* — the always-listening state records the Wet Channel regardless of routing, so every generation gets deeper, blurrier, more synthetic.
- **How to play it:**
  1. Capture a phrase; route it through Soup (ROUTING down).
  2. Let the Soup bloom around it.
  3. Tap the looper **off** — it instantly starts re-recording (and it hears the Soup output).
  4. Tap it back **on** a moment later: the new loop = old loop + trails.
  5. Repeat. Each pass is a generation; CLOCK steps between passes transpose generations against each other.
- **Variations:** do a pass through **Flip** instead — each generation gains a harmony layer (a chorale accretes) · a pass through **Relay** prints rhythmic repeats into the bed · with CROSS up (source: looper) the recapture also catches the interference.
- **Verification:** 🟢 named in the manual (p.31 "TRAIL CATCHER") + the always-listening-records-wet rule (p.41); 🟣 the Flip/Relay generation-stacking extensions are designed on those verified rules.

### A8 · Orchestra in the Next Room
*Radio's Orchestral station under a dark EQ — "a symphony of different voices that come in and out," arranged from one played phrase, with the clean loop blended back for anchor.*
**Tags:** radio, orchestral-station, arrangement, voices, blend

- **Channels:** Both ON.
- **Knobs:** MIX 1:30 · CLOCK 11:00 · TIME 11:00 (modest Soup) · MODIFY-wet 10:00 · **LENGTH = number of voices — start 10:00 (a few voices), raise for the full section** · **MODIFY-looper ≈ noon on the clean Orchestral spot (CC19 ≈ 63)**.
- **Toggles:** Wet **Soup** · ROUTING **middle (both — your playing joins the room)** · Looper **Radio**.
- **Hidden options:** **BLEND up ~noon** (clean micro-loop ghosts under the wet arrangement — the anchor) · EQ slightly dark (next-room feel).
- **MIDI snapshot:** `CC23=2 · CC19=63 · CC16=48 · CC21=0 · CC22=2 · CC29=64 · CC27=48 · CC103=1 · CC102=1`
- **Use case:** self-arranging chamber beds: voices enter and leave "playing at different speeds for different moments," so a single melodic phrase becomes an ensemble that never repeats identically — ideal underneath sparse lead playing.
- **How to play it:**
  1. Record a *melodic* loop (single-line phrases give the clearest voices).
  2. Park on Orchestral's clean spot; set LENGTH low and hear two or three voices trade your phrase.
  3. Raise LENGTH for the fuller symphony; raise BLEND so the original phrase grounds it.
  4. Play against the arrangement — it dovetails rather than echoes.
- **Variations:** drop CLOCK two steps after recording — a bass-register orchestra (notes stay where you played them if you move CLOCK during an overdub pass) · Orchestral into **Flip** (routing down) = harmonized orchestra.
- **Verification:** 🟢 station behavior/CC + BLEND function; 🟡 "different speeds for different moments" phrasing from the walkthrough; 🟣 numerics and the arrangement-under-lead use case.

### A9 · Tidal Clock
*Bounce automation on CLOCK: the whole pedal breathes up and down the harmonized ladder — a self-playing tide.*
**Tags:** bounce, ramping, automation, drift, generative

- **Channels:** Both ON (Soup + any looper mode holding a bed).
- **Knobs:** **MIX = RAMP SPEED while ramping is engaged — set slow (9:00); hold the left footswitch and turn to reach the real mix** · **CLOCK = one end of the bounce range (with SWEEP=T, knob = top; the bounce moves below it)** — set 12:00 · TIME 1:00 · MODIFY-wet noon · LENGTH noon · MODIFY-looper on Ambient or Shoegaze.
- **Toggles:** Wet **Soup** · ROUTING middle · Looper **Radio**.
- **Hidden options:** defaults.
- **Dip switches (control bank):** **CLOCK ON · BOUNCE ON · SWEEP = T** (others off).
- **MIDI snapshot:** `CC63=1 · CC66=1 · CC67=1 · CC20=25 (slow) · CC18=70 · CC21=0 · CC23=2 · CC19=32`
- **Use case:** a generative drone that re-pitches itself: bounce walks CLOCK between steps, so loop + reverb slowly rise and fall through fourths/fifths/octaves — tidal, harmonized, hands-free.
- **How to play it:**
  1. Engage the CLOCK + BOUNCE dips; MIX now sets bounce speed — go slow.
  2. Capture a loop and let Soup swallow it.
  3. The texture now breathes through the harmonized steps on its own; play long tones that sit across the moving root.
  4. To freeze the tide mid-breath: CC52=0 stops ramping (resume with CC52≥1).
- **Variations:** add the **SMOOTH dip** and the steps become continuous tape-bend tides (seasick, beautiful) · bounce **TIME** instead (dip 61) for a Soup that swells and shrinks around a stationary loop · BOUNCE OFF converts this into the one-shot ramp patch (see E6).
- **Verification:** 🟢 ramping mechanics, MIX-repurposing, SWEEP/CC52 all manual-verbatim (pp.46–47); 🟣 range/speed choices and the generative framing.

## Group B — Rhythmic & sequenced

### B1 · 2-Track
*The manual's named layered-composition technique: Relay as a second looper, freeze as the record-arm, SYNC as the tape sync — "you can go surprisingly far."*
**Tags:** relay, looper, layering, composition, sync, named-technique, freeze

- **Channels:** Both ON.
- **Knobs:** MIX 1:30 · CLOCK 11:00 · **TIME = the Relay phrase length — and with SYNC left engaged, also the micro-loop length** (set it to your bar) · **MODIFY-wet at MAX (repeats stable, "pile up like a looper")** · LENGTH noon · MODIFY-looper Mask-min (clean track 1) or Tape.
- **Toggles:** Wet **Relay** · ROUTING up (input only — the mic-loop shouldn't re-enter Relay unless you want smear) · Looper **Mask** (or Radio/Tape).
- **Hidden options:** **SYNC left — Micro-Looper synced to Wet Channel; TIME now sets the loop length** so both "tracks" share one bar length.
- **Dip switches:** LATCH ON (freeze becomes a latching record-arm).
- **MIDI snapshot:** `CC21=2 · CC17=127 · CC22=0 · CC23=127 (Mask) · CC31=0 (sync L) · CC75=1 · CC102=1 · CC103=1`
- **Use case:** two independent loopers in one pedal: the Micro-Looper is track 1 (a riff, a chord bed), Relay is track 2 (a lead, counter-line, percussion layer) — and freeze on Relay means "preserve the current sound and not have your playing recorded," i.e. punch **out**.
- **How to play it:**
  1. Record track 1 into the Micro-Looper (Mask, MODIFY min = faithful).
  2. Engage SYNC left so TIME defines the shared bar; adjust TIME to taste — the loop follows.
  3. Play track 2 into Relay with MODIFY max: every phrase piles up at equal volume.
  4. **Freeze** (latched) when track 2 is complete — Relay now loops it and ignores your playing.
  5. Solo over both. Unfreeze to punch back in and add more; overdub the Micro-Looper (hold right) for track-1 changes.
- **Variations:** SYNC right instead — build track 1 first and let Relay's TIME snap to rhythmic subdivisions of it (see B8) · MODIFY-wet just below max = track 2 slowly renews itself (oldest phrases fall away — an evolving arrangement) · try Relay into the always-listening capture for a bounce-down (loop absorbs the pile, then Relay is free again).
- **Verification:** 🟢 technique named in the manual (p.22 "2-TRACK") incl. the sync recommendation and freeze-as-preserve; 🟢 Relay max = looper pile-up; 🟣 numerics/workflow details.

### B2 · Honest Echo
*Relay as the everyday rhythmic delay — except every repeat is full volume, so it reads as a hocketing double, not a fading echo.*
**Tags:** relay, delay, rhythmic, slapback, doubling

- **Channels:** Wet ON only.
- **Knobs:** MIX 11:00 (repeats sit with the dry, not behind it — they don't decay, so mix lower than a normal delay) · CLOCK 1:00 (clean, bright) · **TIME to the rhythm (9:00 slap → 2:00 phrase echo)** · **MODIFY-wet ~9:00–10:00 (a precise 1–3 repeats)** · LENGTH/MODIFY-looper —.
- **Toggles:** Wet **Relay** · Looper off (still listening, though).
- **Hidden options:** EQ a touch dark so repeats tuck behind the attack.
- **MIDI snapshot:** `CC21=2 · CC102=1 · CC14=48 · CC17=~20 · CC18=84 · CC27=48`
- **Use case:** the walkthrough's list: "doubling effect… rhythmic stuff… cloning yourself… taking double tracking and stretching that out over time." One or two equal-volume repeats = instant tape-double/hocket; three or four = a rhythm section of yourself.
- **How to play it:**
  1. Set MODIFY for exactly the repeat count you want — this is a *choice*, not a feedback dice-roll.
  2. Play staccato phrases and rests: Relay fills the rests at full confidence.
  3. Because repeats don't decay, silence is your mix knob — leave space or it stacks into mud.
  4. Tap the footswitch off between sections; TRAILS optional.
- **Variations:** CLOCK down two steps = the repeats come back darker and slower (lo-fi echo without a tone knob) · sync to rig tempo over MIDI: CC51≥1 + wet division CC53 (e.g. 3 = eighths); remember sub-60 BPM re-pitches existing audio · MODIFY to max mid-phrase = catch the current bar and let it pile (gateway to B1).
- **Verification:** 🟢 Relay control roles + stability-at-max (p.24); 🟡 use-case list from the walkthrough; 🟣 numerics.

### B3 · When Did You Get Here?
*Relay's "audio illusion" — old and new echoes at identical volume until the room is full of yous and nobody can say who played what, when. The manual's own Frippertronics spin.*
**Tags:** relay, frippertronics, illusion, ambient-rhythm, pile-up

- **Channels:** Wet ON; looper joins late as the archivist.
- **Knobs:** MIX 2:00 (the illusion needs the copies as loud as you) · CLOCK 11:00 · **TIME long (3:00–4:00) — phrases return after you've forgotten them** · **MODIFY-wet high but shy of max (~3:30): the pile very slowly renews instead of accreting forever** · LENGTH noon · MODIFY-looper clean station.
- **Toggles:** Wet **Relay** · ROUTING up · Looper **Radio** (for later).
- **Hidden options:** GLUE nudged to taste — the gel helps the copies fuse into one performer.
- **MIDI snapshot:** `CC21=2 · CC14=110 · CC17=112 · CC18=62 · CC28=~45 · CC102=1`
- **Use case:** the manual's "WHEN DID YOU GET HERE?" — "unique, abstract sensations where old and new can't be told apart… a very fun spin on Frippertronics-style looping." Solo-performer counterpoint: play a line, answer the echo of your line, answer the answer.
- **How to play it:**
  1. Long TIME, high MODIFY; play one short phrase and wait — it returns at your volume.
  2. Converse with it. Every phrase you add becomes a colleague, not an echo.
  3. When the ensemble is right, tap the Micro-Looper on: the whole illusion is captured (always-listening records the wet), and you can freeze the conversation as a bed.
  4. Escape hatch: MODIFY down to 1–2 repeats and the crowd politely leaves.
- **Verification:** 🟢 concept + Frippertronics framing manual-verbatim (p.25); 🟢 capture rule; 🟣 numerics and the conversation workflow.

### B4 · Stable Sequencer
*The manual's named recipe for order inside Burst: record clean in another mode first (or play short muted notes), then let the 8-step slicer run.*
**Tags:** burst, sequencer, rhythmic, 8-step, named-technique

- **Channels:** Micro-Looper ON (Burst); Wet off at first.
- **Knobs:** MIX 1:00 · CLOCK 11:00 (HALF dip optional for a tight bar) · TIME — · MODIFY-wet — · **LENGTH = pattern speed / step size — start noon, then rhythm-shop** · **MODIFY-looper at MIN (envelope detector off = no scrambling — the stable half of the technique)**.
- **Toggles:** Looper **Burst** · ROUTING moot until Wet joins · Wet **Relay** later.
- **Hidden options:** defaults; BALANCE toward looper if the pattern should lead.
- **Dip switches:** HALF ON (optional, tighter step material).
- **MIDI snapshot:** `CC23=0 · CC19=0 · CC16=64 · CC18=62 · CC76=1 · CC103=1`
- **Use case:** a micro-loop turned drum-machine-adjacent pattern: Burst finds each "unique" sound in the loop, makes it a step (up to 8), and cycles the slices at the sequencer's steady pace — "everything always feels rhythmically connected."
- **How to play it:**
  1. Record the source loop in **Mask, MODIFY min** — deliberate, separated, short muted notes (both of the manual's stability tricks at once).
  2. Flip the mode toggle to **Burst** (FREE PLAY: the loop survives the switch).
  3. LENGTH sets the pattern's tempo/step size; find the pocket.
  4. Keep MODIFY at min while it's the backbone of a piece.
  5. Overdub with care: overdubs write into the **underlying loop**, not the sequence — treat each pass as reshuffling the deck (see C5 to weaponize this).
- **Variations:** one-note-at-a-time construction (walkthrough demo): record a single staccato note = 1-step pattern; bypass-replace a moment to add note 2 = 2-step; grow the sequence stepwise · run the pattern through **Relay** (ROUTING down) at a related TIME = polyrhythmic delays on a sequence · CLOCK down one step mid-pattern = the whole sequence drops a fourth/fifth in tempo and pitch together.
- **Verification:** 🟢 technique named in the manual (p.35 "STABLE SEQUENCING") + slice/step mechanics; 🟡 note-by-note growth from the walkthrough demo; 🟣 numerics.

### B5 · Dig-In Fills
*Burst's chaotic half used on purpose: set the envelope threshold so hard accents scramble the pattern — drum fills you trigger with your pick hand.*
**Tags:** burst, fills, dynamic, interactive, scramble

- **Channels:** Micro-Looper ON (Burst); play along live.
- **Knobs:** MIX noon (pattern and player equal) · CLOCK 11:00 · **LENGTH grooving (as B4)** · **MODIFY-looper at the threshold sweet spot (~1:00–2:00): normal playing leaves the pattern alone, digging in scrambles it** — the walkthrough demos exactly this "fills only when you really dig in" setting.
- **Toggles:** Looper **Burst** · ROUTING up if Wet is on (keep the pattern out of the wet so the fill contrast stays sharp).
- **Hidden options:** defaults.
- **MIDI snapshot:** `CC23=0 · CC19=~80 · CC16=64 · CC18=62 · CC103=1`
- **Use case:** a rhythm partner that listens: comp quietly and the 8-step pattern holds; accent a downbeat and Burst throws a randomized fill, then falls back into the groove. "Randomizing fills when you play along" — manual-verbatim purpose.
- **How to play it:**
  1. Build a stable pattern (B4 recipe).
  2. Raise looper-MODIFY until *only* your accents cross the threshold — calibrate by playing at performance volume.
  3. Groove against it; punch an accent where a drummer would fill.
  4. Too twitchy = MODIFY down a hair; asleep = up. (COLOR-style rule of thumb: the threshold hears the *loop* too — a hot loop self-scrambles.)
- **Variations:** MODIFY max = perpetual self-scramble (the pattern never repeats — IDM mode) · feed it a drum machine or MPC instead of guitar: the fill threshold becomes a velocity-reactive remixer · CROSS source = looper on top (C7) so the fills also warp the wet channel.
- **Verification:** 🟢 threshold/scramble behavior manual-verbatim (p.34); 🟡 the dig-in calibration demoed in the walkthrough; 🟣 numerics + the self-scramble reading of a hot loop (the manual says the detector reacts "when a sound is louder than the threshold while in playback" — whether the loop itself can trigger it is inferred).

### B6 · Club Night at the Circus
*Radio's Dance station — the loop rotates half-speed / normal / double-speed in strict time. LENGTH is the DJ.*
**Tags:** radio, dance-station, rotation, octaves, rhythmic

- **Channels:** Micro-Looper ON (Radio).
- **Knobs:** MIX 1:30 · CLOCK 11:00–noon · **LENGTH = rotation speed: slow (9:00) = ambient octave-drift; fast (3:00) = percussive churn (walkthrough: "slow and ambient with it, or more percussive")** · **MODIFY-looper fully CW on the clean Dance spot (CC19 = 127)**.
- **Toggles:** Looper **Radio** · ROUTING down if Wet joins (dance the loop, stay dry).
- **Hidden options:** GLUE up a notch — the rotation loves grit.
- **MIDI snapshot:** `CC23=2 · CC19=127 · CC16=32↔96 · CC18=62 · CC28=~55 · CC103=1`
- **Use case:** "Club night at the circus" (manual-verbatim): instant octave-jumping rhythmic material from any riff — half/double-speed rotation means the loop keeps re-voicing itself across three octave registers in a steady cycle.
- **How to play it:**
  1. Record a rhythmically confident riff (this station rewards groove).
  2. Park MODIFY at the Dance clean spot; set LENGTH slow first — hear the three versions trade politely.
  3. Speed LENGTH up until the rotation itself becomes the rhythm.
  4. Play sparse stabs in the gaps; the rotation does the arranging.
- **Variations:** LENGTH at max + short loop = a ratcheting, near-arpeggiated churn · rotate *into* Relay (ROUTING down, TIME matched by SYNC right) = the three speeds each get echoed in grid · drop CLOCK for the same night in a much worse part of town.
- **Verification:** 🟢 station behavior + CC value + "club night" line (p.37); 🟡 slow-ambient-vs-percussive poles from the walkthrough; 🟣 numerics/pairings.

### B7 · Backwards Tape Memory
*Radio's Tape station — the pedal's only reverse. Half-speed and backwards, the original MOOD move, one knob away from "no funny business."*
**Tags:** radio, tape-station, reverse, half-speed, mkii-carryover

- **Channels:** Micro-Looper ON (Radio); Soup optional gauze.
- **Knobs:** MIX 1:00 · CLOCK 10:30 · TIME 11:00 (if Soup joins) · MODIFY-wet 10:00 · **LENGTH = speed/direction — hunt the reverse zone, then the half-speed-reverse corner** · **MODIFY-looper fully CCW on the clean Tape spot (CC19 = 0)**.
- **Toggles:** Looper **Radio** · Wet **Soup** · ROUTING down.
- **Hidden options:** defaults; BLEND up a bit to ghost the forward loop under the reversed one.
- **MIDI snapshot:** `CC23=2 · CC19=0 · CC16=explore · CC21=0 · CC22=127 · CC103=1 · CC102=1`
- **Use case:** the memory-play move MkII owners reach for: a phrase played once, returned backwards at half speed under gauze — and this is **the only direct reverse control in BAD MOOD** (the sole exception: Orchestral station + SPREAD reverses one stereo side), so this patch is the reverse patch.
- **How to play it:**
  1. Capture a lyrical phrase (legato > staccato for reverse beauty).
  2. On the Tape clean spot, sweep LENGTH until playback flips direction; fine-tune speed.
  3. Add Soup at low MODIFY for the classic reversed-memory wash.
  4. Overdub forward notes while it runs backwards — call-and-response with your own past (overdubs land per the current playback mangling: expect happy misplacement).
- **Variations:** the early-owner "dub techno" accident — Tape hard-CCW + **Flip** with a moving TIME instead of Soup · CLOCK moves after capture re-pitch the whole memory in harmonized steps · HALF dip for shorter, more phrase-like memories.
- **Verification:** 🟢 station function (speed/direction) + CC value; 🟡 "only reverse in the pedal" from first-week owner/reviewer consensus, dub-techno pairing from an owner report; 🟣 numerics and the reverse-zone location on LENGTH (the manual doesn't map the knob's zones).

### B8 · Locked Steps
*SYNC right: the Wet Channel snaps to the micro-loop — Relay's TIME "moves in steps that are rhythmically related to the micro-loop length." The groove version of the pedal.*
**Tags:** sync, relay, rhythmic-grid, subdivisions, loop-locked

- **Channels:** Both ON.
- **Knobs:** MIX 1:00 · CLOCK 11:00 · **TIME = quantized subdivision selector (post-SYNC) — click through the steps and every position is in time** · MODIFY-wet 10:00 (a few repeats) · LENGTH noon · MODIFY-looper Dance or Tape clean spot.
- **Toggles:** Wet **Relay** · ROUTING **down (looper only — the loop gets gridded echoes; you stay dry)** · Looper **Radio**.
- **Hidden options:** **SYNC right — Wet Channel synced to Micro-Looper** (the whole point).
- **MIDI snapshot:** `CC31=127 (sync R) · CC21=2 · CC22=127 · CC23=2 · CC14=step-select · CC17=~40 · CC103=1 · CC102=1`
- **Use case:** loop-locked rhythmic delay with zero tap-dancing: record any loop and Relay's echoes land on its subdivisions by construction. The un-synced alternative (nudging TIME by ear) is exactly the fiddliness this hidden option deletes.
- **How to play it:**
  1. Record the loop first — it defines the bar.
  2. Engage SYNC right (hidden options: wet MODE toggle to the right).
  3. Turn TIME slowly: it now *steps*; each step is a related subdivision. Pick the pocket.
  4. Play over the grid; retune the groove anytime by stepping TIME — never out of time.
  5. CLOCK still transposes/stretches everything together — the grid survives.
- **Variations:** swap Relay for **Flip**: the lag between harmony notes now lands in grid = arpeggiator territory (see D3) · Burst under SYNC right = sequence + gridded echo, one pedal techno · this + B1's freeze = synced 2-track.
- **Verification:** 🟢 SYNC-right behavior manual-verbatim (p.17); 🟣 numerics, and note the manual never specifies *which* subdivisions the steps are — listed in §9 open questions.

### B9 · Clocked to the Rig
*BAD MOOD under external MIDI clock — divisions per channel, tap tempo, and the sub-60 BPM pitch-warp quirk used musically.*
**Tags:** midi-clock, sync, rig-integration, divisions, utility

- **Channels:** Both ON, any modes (Relay + Burst is the natural clocked pair).
- **Knobs:** per the host patch — CLOCK becomes the follower's rate base; TIME/LENGTH behavior under clock follows the divisions below.
- **Toggles:** any.
- **Hidden options:** any.
- **MIDI setup (channel 2):** `CC51≥1 (follow clock) · CC53 = wet division (0=1/32 … 4=1/4 … 8=double whole) · CC54 = looper division · CC93 = tap tempo (exit: hold footswitch + turn TIME) · CC110 = MIDI reset if the synth-mode globals get weird`
- **Use case:** the pedalboard-as-band move: Digitakt/DAW clocks the rig, BAD MOOD's loop length and Relay time lock to the grid, and CLOCK stays free as a *musical* register control.
- **How to play it:**
  1. Send clock; CC51≥1. Set the two divisions — e.g. wet at eighths (CC53=3), looper at a whole note (CC54=7) so the loop is a bar and the echoes subdivide it.
  2. Record loops on the beat; Burst patterns now sit in the host groove.
  3. **Know the warp:** below 60 BPM effective (BPM depends on division — 120 BPM at whole note = 30 effective) the pedal shifts its internal sample rate and **existing audio changes speed and pitch**. Avoid by keeping divisions short — or exploit it: drop the division from quarter to whole mid-song and the whole texture lurches down like a power-cut.
  4. **Synth-mode landmine (MkII heirloom):** any stray MIDI note auto-engages Synth Mode, which *ignores clock*. Filter notes away from channel 2, or send CC59 to bail out.
- **Variations:** BAD MOOD unclocked but tap-tempo'd via CC93 from a controller · clock only the looper (wet division long) for free-time Soup over a locked loop.
- **Verification:** 🟢 all CCs and the sub-60 BPM behavior from the MIDI manual (pp.3–4); 🟢 synth-mode auto-engage (MIDI p.6); 🟣 the musical exploitation of the warp.

## Group C — Glitch, noise & broken

### C1 · Don't Touch That Dial
*The manual's named Radio move, inverted: DO touch it. Scanning MODIFY through the static blends stations, smears genres, and plays the interference as an instrument.*
**Tags:** radio, scan, static, interference, performance, named-technique

- **Channels:** Micro-Looper ON (Radio).
- **Knobs:** MIX 2:00 (the static deserves the stage) · CLOCK 10:30 · **LENGTH noon (it stays live for every station you pass through — one LENGTH, five meanings)** · **MODIFY-looper = the performance control: sweep it, hover between stations to blend two at once (walkthrough-verified), rest inside pure static**.
- **Toggles:** Looper **Radio** · ROUTING as needed · Wet off or Soup low.
- **Hidden options:** GLUE mid — static + saturation = broadcast from a dying transmitter.
- **MIDI snapshot:** `CC23=2 · CC19=ride 0↔127 · CC16=64 · CC18=58 · CC28=~64 · CC103=1`
- **Use case:** the "shortwave" in shortwave looper: one loop becomes a night of channel-surfing — tape memory, slow-motion blur, orchestra, frozen wall, club — with "noise and filtering and disruption" as the segues. The manual's tip is to learn stations in isolation *because* the scramble is so seductive; this patch is the scramble.
- **How to play it:**
  1. Record a loop with variety (chords + a run + a bit of noise — every station interprets it differently).
  2. Sweep MODIFY slowly end to end once — map where the five clean spots and the static zones sit on your knob.
  3. Perform the dial: hold two-station blends (Ambient+Orchestral is a lush accident; Shoegaze+Dance is a beautiful fight).
  4. Ride MIX down when the static should whisper, up when it should swallow.
- **Variations:** automate the scan — MODIFY-looper dip ON + BOUNCE = the pedal channel-surfs itself (CC64=1, CC66=1; slow ramp speed) · CC19 jumps from a MIDI controller = instant hard cuts between genres (0/32/63/97/127 for clean, in-betweens for chaos) · park just off a clean spot for "almost tuned" unease under a song.
- **Verification:** 🟢 scan/static/clean-spot behavior + the named tip (p.36); 🟡 two-station blending confirmed in the walkthrough; 🟣 numerics and the blend aesthetics.

### C2 · Threshold Surfing
*The manual's named Mask calibration: only the transients get disguised — "mysterious, ear-catching bursts" riding on top of an otherwise honest loop.*
**Tags:** mask, transients, threshold, dynamic, named-technique

- **Channels:** Micro-Looper ON (Mask).
- **Knobs:** MIX 1:00 · CLOCK 11:00 · **LENGTH = what the disguise IS — start ~2:00 (smooth/flowy end) and audition** · **MODIFY-looper = the surf: raise from min until *only* the loop's attacks cross the threshold**.
- **Toggles:** Looper **Mask** · ROUTING up if Wet on.
- **Hidden options:** defaults.
- **MIDI snapshot:** `CC23=127 · CC16=~85 · CC19=calibrate ~35–55 · CC18=62 · CC103=1`
- **Use case:** a loop that stays itself except at the moments that grab the ear: each attack blooms into something else, then hands back to the honest recording — "a musical push and pull as the mask turns on and off."
- **How to play it:**
  1. Record a loop with clear dynamics (defined attacks, quieter sustains).
  2. MODIFY at min = pure loop (your reference). Raise slowly; the loudest instant flickers first.
  3. Stop exactly where only transients trigger — that's the surf line. Every loop you record re-draws it ("each loop you record will bring out a different response").
  4. Choose the disguise with LENGTH: flowy at one end → "obliterated, noisy stuff" at the other.
  5. Overdub louder/softer notes to *compose* which events get masked.
- **Variations:** surf the other break — MODIFY just *below* full-mask so only the quietest moments survive undisguised · LENGTH at min for the walkthrough's "crumbly gates… mechanical sputtering failure" on each attack (see C3) · CROSS source = looper: the masked bursts also shove the wet channel around.
- **Verification:** 🟢 technique named + threshold behavior (p.38); 🟡 LENGTH's smooth↔obliterated↔crumbly-gate poles from the walkthrough; 🟣 numerics.

### C3 · Crumbly Gates
*Mask at its meanest: LENGTH at minimum, MODIFY at max — the whole loop re-rendered as a sputtering, gated mechanical failure.*
**Tags:** mask, gated, broken, noise, industrial

- **Channels:** Micro-Looper ON (Mask); Wet off (bare) or Relay (rhythmic debris).
- **Knobs:** MIX 2:30 (commit) · CLOCK 9:30 (low rate compounds the rot) · **LENGTH at MIN — the "crumbly gates / mechanical sputtering failure" end of the character sweep** · **MODIFY-looper at MAX — "apply the mask at all times"**.
- **Toggles:** Looper **Mask** · ROUTING down if Relay joins.
- **Hidden options:** **GLUE high** (the bit-crush zone) · EQ CCW (dark = heavier machinery).
- **MIDI snapshot:** `CC23=127 · CC16=0 · CC19=127 · CC18=48 · CC28=~100 · CC27=~40 · CC103=1`
- **Use case:** the loop as a malfunction: everything above silence is gated, chopped, and sputtered — rhythmic in the way a dying relay cabinet is rhythmic. Under a clean dry signal (MIX lower) it's an industrial floor; alone it's a texture piece.
- **How to play it:**
  1. Record something sustained — the gates need material to interrupt.
  2. LENGTH min, MODIFY max: total disguise.
  3. Play with CLOCK steps: the sputter transposes and slows in harmonized intervals — broken machinery in tune with itself.
  4. Sweep LENGTH up mid-performance to melt the gates into smoother disguises and back.
- **Variations:** EQ per channel over MIDI (CC85≥3 = looper-only EQ) to scoop just the debris while the wet stays full-range · Soup after it (ROUTING down) = ruins in a cathedral · FADE down + overdub = the failure slowly consumes each new phrase.
- **Verification:** 🟢 full-mask behavior (p.38); 🟡 the crumbly-gates/sputtering-failure character at LENGTH min is walkthrough-verbatim; 🟣 numerics, EQ/GLUE dressing.

### C4 · Eraser Head
*The bypass switch as an instrument: REPLACE starts erasing and re-recording the instant the looper is bypassed — punch-in destruction with a footswitch.*
**Tags:** replace, punch-in, glitch, erase, performance

- **Channels:** Micro-Looper ON (any mode; Mask-min shows the surgery clearest).
- **Knobs:** MIX 1:30 · CLOCK 11:00 · LENGTH noon · MODIFY-looper min (Mask) — you want to *hear* the edit.
- **Toggles:** Looper **Mask** to monitor, then any mode to mangle.
- **Hidden options:** defaults; FADE at unity (edits should be hard, not soft).
- **MIDI snapshot:** `CC23=127 · CC19=0 · CC103=toggle 1→0→1 in rhythm · CC18=62`
- **Use case:** the manual's REPLACE reading of bypass: "as soon as the channel is bypassed it starts to erase the existing loop and record the input audio in its place… an interesting way to clear out some space or add glitches." Quick blinks = glitch punches; held bypass = wholesale replacement; silence during bypass = carving holes.
- **How to play it:**
  1. Record a full loop.
  2. Blink the footswitch off-on in rhythm while playing something new: each blink splices new audio (or silence) into the old loop.
  3. Blink while *not* playing to punch rests into the loop — negative-space glitching.
  4. Remember the always-listening rule: whatever the Wet Channel is doing during the blink gets spliced in too (Trail Catcher's evil twin).
- **Variations:** blink over a Burst pattern — the sequence re-slices itself around your edits · long-held bypass with a swelled chord = crossfade-free scene change · LATCH off here (you want momentary precision).
- **Verification:** 🟢 REPLACE behavior manual-verbatim (p.32) + always-listening capture rule (p.41); 🟣 rhythmic-blink performance technique.

### C5 · Misplaced Overdubs
*Burst's honest warning label — "ALWAYS UNPREDICTABLE!" — played as the feature. What you hear and where you're recorded are two different places.*
**Tags:** burst, overdub, displacement, aleatoric, glitch

- **Channels:** Micro-Looper ON (Burst).
- **Knobs:** MIX 1:00 · CLOCK 11:00 · **LENGTH off-noon (a pattern speed that chews)** · **MODIFY-looper ~2:00 (scramble active — the displacement engine)**.
- **Toggles:** Looper **Burst**.
- **Hidden options:** FADE slightly down (~10:00) so failed experiments dissolve after a few passes instead of accumulating forever.
- **MIDI snapshot:** `CC23=0 · CC16=~75 · CC19=~80 · CC26=~45 · CC106=hold · CC103=1`
- **Use case:** aleatoric composition: overdubs are written into the underlying micro-loop while you *hear* the Burst sequence — so notes land somewhere else in the pattern than where you played them. "Just toss some notes in there and see what happens" is the manual's actual advice; this patch commits to it.
- **How to play it:**
  1. Start from any loop; let Burst sequence it.
  2. Hold overdub and play a note *against* the pattern — it reappears seconds later, somewhere unexpected, re-sliced as a new step.
  3. Respond to where it landed, not where you aimed. Iterate: the piece composes itself between you and the slicer.
  4. FADE keeps the population under control; MODIFY-min anytime to hear the true underlying loop (sanity check).
- **Variations:** same game in **Radio/Shoegaze** — overdubs land inside frozen moments you can't preview · CLOCK moved during the overdub is the ONE stable move (notes stay put) — use it to add a slow layer to a fast chaos · print keepers by re-capturing through the always-listening state.
- **Verification:** 🟢 the hear-vs-record disconnect and "ALWAYS UNPREDICTABLE!" are manual-verbatim (pp.32, 34); 🟢 CLOCK-during-overdub exception; 🟣 the workflow of playing against the displacement.

### C6 · Sputter & Bend
*The manual's own Cross demo: source = your input, CROSS way up, play through Soup — "notice how it bends and sputters as you play."*
**Tags:** cross, input-mod, dynamic, sputter, pitch-bend, soup

- **Channels:** Wet ON (Soup); looper optional and clean.
- **Knobs:** MIX 1:00 · CLOCK 10:00 · TIME 2:00 · MODIFY-wet noon · LENGTH/MODIFY-looper — (or a quiet Mask-min loop underneath).
- **Toggles:** Wet **Soup** · ROUTING **up (input only — the loop, if any, stays out of the warp zone so the contrast reads)** · Looper **Mask**.
- **Hidden options:** **CROSS high (~3:00 first, then to taste — the sweep runs "slight squiggles" → "total dropout/failure")** · **INPUT MOD = middle (input)**.
- **MIDI snapshot:** `CC21=0 · CC22=0 · CC24=~100 · CC33=2 · CC14=80 · CC17=64 · CC102=1`
- **Use case:** touch-responsive sabotage: your playing dynamics modulate the pedal's **pitch and loudness** — dig in and the reverb tail bends, stutters, drops out; play soft and it barely shivers. A dynamics-reactive broken-ness no LFO can fake.
- **How to play it:**
  1. Set INPUT MOD to input (its default), then raise CROSS with a trail ringing — you'll hear the interference arrive.
  2. Play soft: squiggles. Play hard: dropouts and bends. Your attack is the mod wheel.
  3. Calibrate CROSS to your dynamic range the way you'd set a compressor threshold.
  4. For pure effect-on-tails, freeze Soup and then play — the frozen pad gets shoved around by notes it isn't even recording.
- **Variations:** drop CROSS to ~10:00 for "naturalistic variance" (the manual's musical framing — vibrato-adjacent life on everything) · same setting on **Relay** = repeats that flinch when you play · on **Flip** = harmonies that detune under attack.
- **Verification:** 🟢 the exact recipe is the manual's own demo (p.43); 🟡 squiggle→dropout intensity poles from the walkthrough; 🟣 numerics.

### C7 · Living Interference
*Cross with the channels pointed at each other — "a living sense of interconnectedness within the pedal." The loop shoves the reverb; flip it and the reverb breathes through the loop.*
**Tags:** cross, inter-channel, generative, interference, both-directions

- **Channels:** Both ON.
- **Knobs:** MIX 1:30 · CLOCK 10:30 · TIME 1:30 (Soup with a tail to shove) · MODIFY-wet noon · LENGTH noon · MODIFY-looper on a lively station (Dance or a Burst pattern in Burst mode).
- **Toggles:** Wet **Soup** · ROUTING **up (input only): the loop is NOT in the wet path, it only *modulates* it — cleanest way to hear the interference as interference** · Looper **Radio** or **Burst**.
- **Hidden options:** **CROSS ~1:00–3:00** · **INPUT MOD = right (Micro-Looper modulates the wet)**.
- **MIDI snapshot:** `CC21=0 · CC22=0 · CC23=2 · CC24=~80 · CC33=127 · CC102=1 · CC103=1`
- **Use case:** a self-playing ecosystem: the loop's rhythm and dynamics continuously bend and duck the Wet Channel, so the reverb pumps and warps in time with material *you recorded minutes ago*. Nothing repeats exactly; the two channels are audibly alive to each other — the pedal's headline party trick per the intro video ("CROSS MODULATION!").
- **How to play it:**
  1. Record a dynamic loop (a Burst pattern is an ideal modulator — spiky, periodic).
  2. INPUT MOD right; raise CROSS until the wet visibly flinches with each loop event.
  3. Play long tones into Soup: your sustain gets rhythmically carved by the loop.
  4. Now reverse the wiring — **INPUT MOD left (CC33=0): the Wet Channel modulates the looper** — and the loop instead breathes/bends under the reverb's swells: slower, tidal interference.
  5. The third position (input) returns it to C6's touch-control.
- **Variations:** CROSS max + Dance station = the rotation's octave jumps yank the wet around violently — seasick techno · both directions in one performance via a MIDI controller flipping CC33 · keep the loop *silent-ish* (record room noise) = ghost modulation, movement with no audible source.
- **Verification:** 🟢 source options + interconnectedness framing manual-verbatim (p.43); 🟡 channel-to-channel "makes Bad Mood come alive" from the walkthrough; 🟣 numerics and both-direction aesthetics (which direction sounds tidal vs rhythmic is inferred from what each channel outputs).

### C8 · Total Thrash
*GLUE at the destroyer end, dry included — "completely thrash everything passing through the pedal." The patch you were warned about.*
**Tags:** glue, destruction, bitcrush, wall, noise

- **Channels:** Both ON, everything hot.
- **Knobs:** MIX 3:00 · CLOCK 9:00 (low rate = pre-crushed) · TIME 2:00 · MODIFY-wet 2:00 · LENGTH noon · MODIFY-looper Shoegaze spot (a wall to thrash).
- **Toggles:** Wet **Soup** · ROUTING middle (everything into everything) · Looper **Radio**.
- **Hidden options:** **GLUE at/near MAX — through "torn speaker overdrive" into the bit-crush zone** · EQ to taste (CCW tames the shriek).
- **Dip switches:** **DRY GLUE ON** (no survivors) · SPREAD ON (a wide ruin).
- **MIDI snapshot:** `CC28=127 · CC78=1 · CC72=1 · CC21=0 · CC22=2 · CC23=2 · CC19=97 · CC18=41 · CC27=~45`
- **Use case:** the "raw, reckless side of ambience" at full commitment: loop + reverb + dry fused into one distorting, crushed mass — shoegaze-wall into power-electronics territory depending on MIX and EQ. This is the "you should turn it up if you really want to be bad" ending.
- **How to play it:**
  1. Build any texture (A6's tower is a great victim).
  2. Hidden options: sweep GLUE up slowly *while it plays* — overdrive, then crush, and hear where the texture stops being texture and becomes material.
  3. EQ CCW to put the weight low; CW for glass-shard highs.
  4. De-escalate live: GLUE back to 9:00 and the same patch is merely warm (the entire subtle↔destroyed range lives on one hidden knob — see E3 for the other end).
- **Variations:** MASTER VOLUME (CC30) down before you max GLUE, then ride it — MIDI-only makeup gain · thrash only the channels: DRY GLUE off, MIX max = destroyed wet under an untouched dry (doom-lead-over-ruins) · pair with C3 for the full industrial collapse.
- **Verification:** 🟢 GLUE range + DRY GLUE behavior manual-verbatim (pp.42, 45); 🟡 overdrive→bitcrush sweep from the walkthrough; 🟣 numerics.

## Group D — Harmony & synth

### D1 · Chord Looper
*The manual's named "strange little synth": freeze Flip on one note, then transpose the repeating chord with CLOCK and re-voice it with MODIFY.*
**Tags:** flip, freeze, chord, synth, transpose, named-technique

- **Channels:** Wet ON (Flip).
- **Knobs:** MIX 2:00 · **CLOCK = the transposer (start noon; every step = a harmonized interval)** · **TIME UP (the manual's instruction — "Turn up TIME": the chord notes arrive spread in time, so the freeze holds a repeating *pattern*, not a block chord)** · **MODIFY-wet = the re-harmonizer (sweep the 48-chord map live)** · LENGTH/MODIFY-looper —.
- **Toggles:** Wet **Flip** · ROUTING up · Looper off (until you print).
- **Hidden options:** defaults.
- **Dip switches:** **LATCH ON** (hands-free hold while both hands re-voice).
- **MIDI snapshot:** `CC21=127 · CC14=~100 · CC17=sweep · CC18=step · CC105=1 · CC75=1 · CC102=1`
- **Use case:** manual-verbatim: "play a single note, and freeze Flip: You will now have a repeating pattern that you can transpose with CLOCK and re-harmonize with MODIFY… a launching point for turning BAD MOOD into a strange little synth." One plucked note becomes a self-playing chord arpeggio you conduct with two knobs.
- **How to play it:**
  1. TIME up, pick one clean note, freeze (latched).
  2. MODIFY sweeps the harmony: low = single intervals, high = 4-note stacks (the map in Part I §7.4 — e.g. CC17≈9 = +4th; ≈62 = +Oct+5th+4th; ≈127 = a 4-note splinter).
  3. CLOCK steps the whole pattern through fourths/fifths/octaves — chord changes on a knob.
  4. Play bass notes or melody under your own accompaniment.
  5. Unfreeze, play the next note, refreeze — new root.
- **Variations:** print it — tap the Micro-Looper on while frozen (the pattern is captured; the always-listening state records the wet) and now Flip is free for live harmony *over* the printed chord · SMOOTH dip + CLOCK = the frozen chord tape-glides between keys · MODIFY into the 40s (4-note zone) with TIME max = a broken music box.
- **Verification:** 🟢 technique named + both knob roles manual-verbatim (p.22 "CHORD LOOPER"); 🟢 chord map from the MIDI manual; 🟣 numerics.

### D2 · Vintage Shifter
*The manual's "'VINTAGE' HARMONIES" tip: a small TIME lag recreates "the laggy character of older pitch shifters and harmony effects."*
**Tags:** flip, harmonizer, vintage, lag, lead

- **Channels:** Wet ON (Flip).
- **Knobs:** MIX 11:00 (harmony supports, doesn't lead) · CLOCK 1:00 (clean tracking register) · **TIME just up from min (~8:30–9:00) — the "just a bit" lag** · **MODIFY-wet in the low zone: a single interval (CC17: 0–2 = −Oct · 8–10 = +4th · 11–13 = +5th · 14–15 = +Oct)** · LENGTH/MODIFY-looper —.
- **Toggles:** Wet **Flip** · ROUTING up.
- **Hidden options:** EQ slightly dark to seat the shifted voice.
- **MIDI snapshot:** `CC21=127 · CC14=~10 · CC17=12 (+5th) · CC18=84 · CC27=52 · CC102=1`
- **Use case:** the HM-80s harmonizer illusion: a fifth or octave that arrives a breath behind you, slightly synthetic — solo-lead thickener, organ-ish octave doubler, or (−Oct at CC17≈1) an instant faux-bass under a guitar line.
- **How to play it:**
  1. Pick one interval on MODIFY (the detents-by-ear zones are small — trust little moves; over MIDI the map is exact).
  2. TIME barely up: the lag is felt, not counted.
  3. Play lines, not chords, for the cleanest vintage-shifter read.
  4. CLOCK down a step drags the harmony voice into grainier, older territory.
- **Variations:** +4th under everything (CC17≈9) = instant quartal mystery · the walkthrough notes Flip spreads voices in the **stereo field** — SPREAD dip ON widens the doubled voice away from you · MODIFY to a two-note zone (16–55) for shadowed twin harmonies.
- **Verification:** 🟢 tip + TIME behavior manual-verbatim (p.27); 🟢 interval CC values; 🟡 stereo spread of voices from the walkthrough; 🟣 numerics.

### D3 · Splinter Cascade
*Flip with TIME wide open: the chord stops being a chord and becomes a harmonic sequence — "splintered harmonies" as an arpeggiator.*
**Tags:** flip, arpeggiator, sequence, cascade, splintered

- **Channels:** Wet ON (Flip); looper prints beds.
- **Knobs:** MIX 1:30 · CLOCK 11:00 (also scales the lag — walkthrough: CLOCK affects how much lag there is) · **TIME HIGH (2:30–max) — maximum spacing: notes arrive one… by… one** · **MODIFY-wet in the 3–4-note zones (CC17 ≥ 56): more notes = longer cascades** · LENGTH noon · MODIFY-looper clean station.
- **Toggles:** Wet **Flip** · ROUTING up · Looper **Radio** (to catch cascades).
- **Hidden options:** GLUE low-mid; CROSS a whisper (~9:00, source input) so hard attacks bend the cascade.
- **MIDI snapshot:** `CC21=127 · CC14=~115 · CC17=~62 (+Oct+5th+4th) · CC18=62 · CC24=~25 · CC33=2 · CC102=1`
- **Use case:** single notes bloom into ordered showers of fourths/fifths/octaves spread across time and the stereo field — the pedal's "splintered harmonies" tagline as a playing surface. Between Thermae-style cascades and a music-box arpeggiator, but from *your* attack.
- **How to play it:**
  1. Big TIME, dense MODIFY zone. Pluck once; count the voices as they land.
  2. Time your next note to interlock with the tail of the cascade — you're duetting with the harmony engine.
  3. MODIFY choice matters more than ever up here: hunt the 3-note zones for consonant rain (e.g. CC17≈62), the 4-note extremes for beautiful wrong answers (≈127 = +4th+Oct−Oct−4th).
  4. Capture a cascade in the looper, then solo through Flip over it — self-harmonizing rounds.
- **Variations:** SYNC right (B8) grids the lag to a loop = a true arpeggiator pattern · freeze mid-cascade = D1 from a different door · CLOCK step-down mid-cascade re-pitches the *unarrived* notes (report: expect weirdness; unverified which pitch domain wins — flagged).
- **Verification:** 🟢 TIME = lag/spacing + density-by-MODIFY (pp.26–27); 🟡 CLOCK-scales-lag from the walkthrough; 🟣 numerics + the mid-cascade CLOCK behavior (untested — §9).

### D4 · Power Interval Doom
*Flip's single-interval floor pointed down: −Oct or −5th under everything, into a dark EQ and honest GLUE — the harmony patch for riffs.*
**Tags:** flip, octave-down, power-chord, doom, heavy

- **Channels:** Wet ON (Flip); looper as riff-catcher.
- **Knobs:** MIX 1:00 (the low voice is the point) · CLOCK 10:00 (grit becomes weight) · **TIME at MIN — walkthrough: at minimum spacing you get the interval as one stacked voice ("the same note" zone starts it; barely up = tight stack)** · **MODIFY-wet: chord 1 (−Oct, CC17 0–2) or chord 2 (−5th, 3–5) or chord 7 (−Oct−5th, 16–18) for the full doom triad** · LENGTH noon · MODIFY-looper Tape.
- **Toggles:** Wet **Flip** · ROUTING up · Looper **Radio/Tape**.
- **Hidden options:** **GLUE ~2:00 (torn-speaker zone)** · EQ CCW (dark).
- **Dip switches:** DRY GLUE ON if the whole riff should sag together.
- **MIDI snapshot:** `CC21=127 · CC14=0 · CC17=17 (−Oct−5th) · CC18=55 · CC28=~85 · CC27=~40 · CC78=1 · CC102=1`
- **Use case:** the baritone-in-a-box: every note carries its own low octave/fifth shadow with zero lag, glued and darkened — power chords from single notes, or sub-weight under an already-heavy riff. The "raw, reckless" answer to a polyphonic octaver.
- **How to play it:**
  1. TIME hard down (stack, not cascade). Pick the interval: −Oct alone first.
  2. Riff. Adjust MIX so the shadow reinforces rather than replaces.
  3. Step up to chord 7 (−Oct−5th) for the two-voice doom bed.
  4. Catch a riff in the looper; drop CLOCK one step → the *loop* falls a fourth/fifth below your live line: twin-guitar sludge, one player.
- **Variations:** +Oct (CC17≈15) + bright EQ flips this into 12-string jangle · Freeze on a stack = D1 in doom voicing · CROSS (input) low = the shadow trembles under pick attack.
- **Verification:** 🟢 interval map + TIME-min behavior (manual p.26–27, walkthrough "at minimum you get the same note"); 🟣 numerics and the doom application.

### D5 · Radio Choir
*Orchestral's voice-arrangement through Flip's harmony engine — the loop becomes an ensemble, then the ensemble gets harmonized. Both channels, everything on.*
**Tags:** radio, orchestral-station, flip, choir, ensemble, both-channels

- **Channels:** Both ON.
- **Knobs:** MIX 2:00 · CLOCK 11:30 · **TIME 10:00 (a little Flip lag so the harmony ripples across the voices)** · **MODIFY-wet two-note zone (CC17≈20, −5th+Oct — open, choral)** · **LENGTH = # of voices, generous (2:00)** · **MODIFY-looper on Orchestral's clean spot (CC19 ≈ 63)**.
- **Toggles:** Wet **Flip** · ROUTING **down (looper only — the choir gets harmonized; your live line stays a soloist)** · Looper **Radio**.
- **Hidden options:** **BLEND ~11:00** (the unharmonized ensemble ghosts through) · GLUE low ("gel").
- **MIDI snapshot:** `CC21=127 · CC22=127 · CC23=2 · CC19=63 · CC16=~85 · CC14=~40 · CC17=20 · CC29=~55 · CC102=1 · CC103=1`
- **Use case:** the biggest small-ensemble sound in the box: Orchestral already arranges your loop into voices that "come in and out"; Flip re-pitches that arrangement into moving fourth/fifth/octave harmony — a generative choir that never sings the same voicing twice.
- **How to play it:**
  1. Record a slow, melodic loop (hymn-speed material blooms best).
  2. Orchestral clean spot, LENGTH high — let the arrangement establish.
  3. Wet ON: the ensemble refracts through the chosen Flip chord.
  4. Sing/play the lead over the top; adjust BLEND until the choir has both body (clean) and halo (harmonized).
- **Variations:** swap Flip→**Soup** = the ensemble in a synthetic nave (A8's sibling) · MODIFY-wet sweep during a swell = the choir re-voices mid-phrase · CLOCK step down after capture = male choir; up = boys' choir.
- **Verification:** 🟢 both engines' behaviors + CC values; 🟣 numerics and the pairing itself (no published demo combines Orchestral+Flip — designed on verified routing).

### D6 · Open Drone Transposer (Synth Mode I)
*Synth Mode's default OPEN output: BAD MOOD drones continuously and your MIDI keyboard re-pitches it in semitones — the CLOCK knob with keys.*
**Tags:** synth-mode, midi, drone, transposable, open

- **Channels:** Both ON (the drone is whatever texture you've built — e.g. A6's tower or A2's pad).
- **Knobs:** as the host texture; **CLOCK = played by MIDI notes now (semitone steps — finer than the knob's own harmonized ladder)**.
- **Toggles:** any (the texture's).
- **Hidden options:** any.
- **MIDI setup:** send any **MIDI Note** → Synth Mode auto-engages · `CC58=0 (OPEN — constant sound, default)` · `CC57 = octave transpose (1–9 → +12…+108 semitones)` · pitch bend ±4 semitones + mod wheel auto-connected · exit: move CLOCK or `CC59=any`.
- **Use case:** the MIDI manual's "transposable effect… melodic element": a frozen/looped texture becomes a playable drone instrument — hold a bass note on the keys and the entire pedal (loop + wet) sits on that root; walk the keys and the texture follows in semitones, which the face CLOCK can't do (it steps in fourths/fifths/octaves; SMOOTH glides but doesn't quantize).
- **How to play it:**
  1. Build a texture worth droning (capture + freeze or a Shoegaze tower).
  2. Press a key: the pedal is now in Synth Mode (OPEN = it never gates).
  3. Play slow root movements; the whole soundscape modulates underneath a band or a sequence.
  4. **Clock warning:** MIDI clock is ignored in Synth Mode — a clocked rig will drift the moment a note arrives; that stray-note auto-engage is the classic MOOD-family landmine.
  5. Done? CC59 or nudge CLOCK — don't leave it armed.
- **Variations:** portamento (CC84 up) = the drone slides between roots — SMOOTH-dip glide but keyed · pitch bend as a ±4-semitone lever on a whole soundscape · sequence the root from a Digitakt for basslines made of ambience.
- **Verification:** 🟢 all Synth Mode behavior from the MIDI manual (pp.6–8); 🟣 the texture choices.

### D7 · Frozen Soup Keys (Synth Mode II)
*The MIDI manual's own walkthrough recipe: freeze Soup (LATCH on), switch the output to ADSR, and play the frozen ambience like a poly-pad-turned-mono-synth.*
**Tags:** synth-mode, midi, adsr, keys, frozen-soup, official-recipe

- **Channels:** Wet ON (Soup, frozen); looper off or bed.
- **Knobs:** CLOCK 10:00 at capture (dark starter timbre) · TIME 2:00 · MODIFY-wet explore ("explore how different MODIFY and TIME positions affect the texture" — MIDI-manual verbatim) · MIX 2:00.
- **Toggles:** Wet **Soup** · ROUTING up.
- **Dip switches:** **LATCH ON** (the recipe specifies it — the freeze must hold itself while you play keys).
- **MIDI setup:** freeze, then Note On → Synth Mode · `CC58=2 (ADSR)` · `CC80/81/82/83 = A/D/S/R (slow attack ~70, release ~60 for pads; snappy A=5 R=20 for keys)` · `CC84 = portamento` · velocity followed automatically · exit CC59.
- **Use case:** the "strange instrument" endgame: a frozen spectral reverb becomes the oscillator, ADSR carves it into notes, velocity gives it touch — "the most synth-like response" (MIDI manual). Every captured freeze is a new patch; the sound source is literally your instrument's memory.
- **How to play it:**
  1. Play a rich chord/texture into Soup; latch-freeze it.
  2. Set CC58=2; press a key — silence shapes into a note with your envelope.
  3. Slow A/R = bowed-glass pads; fast = plucky spectral keys.
  4. Re-voice the oscillator live with MODIFY/TIME (the frozen texture keeps responding).
  5. "USE THE EXIT": in ADSR the pedal is silent without notes — CC59 before you forget and think it's broken (the MIDI manual's own warning).
- **Variations:** ON/OFF output (CC58=1) = organ-gate response, no envelope · re-freeze different source material per song section = a preset-per-freeze synth · run the synth output into the always-listening looper and sequence the *result* in Burst.
- **Verification:** 🟢 entire recipe from the MIDI manual walkthrough (pp.7–8), including LATCH and the exit warning; 🟣 ADSR numerics.

### D8 · Layered Radio Organ (Synth Mode III)
*The MIDI manual's second walkthrough recipe, verbatim knobs included: Radio loops + overdubs + "bring both the LENGTH and MODIFY knobs to 11 o'clock" = layered synth voices.*
**Tags:** synth-mode, midi, radio, layered, organ, official-recipe

- **Channels:** Micro-Looper ON (Radio); Wet optional.
- **Knobs:** MIX 2:00 · CLOCK ~11:00 at capture · **LENGTH at 11:00 (the manual's number)** · **MODIFY-looper at 11:00 (the manual's number — between Ambient and Orchestral, i.e. an interference-blend zone)** · TIME/MODIFY-wet if Soup garnish.
- **Toggles:** Looper **Radio** · ROUTING middle.
- **MIDI setup:** record + overdub a few sounds first · Note On → Synth Mode · start CC58=0 (OPEN) then try 2 (ADSR) · CC57 octave to taste · exit CC59.
- **Use case:** MIDI-manual verbatim: "use the Micro-Looper to create interesting, layered synth voices. Radio mode is a good starting point — try overdubbing a few sounds and bring both the LENGTH and MODIFY knobs to 11 o'clock." The overdubbed loop becomes a multi-voice oscillator; the 11-o'clock blend zone gives it detuned, stationy thickness; keys transpose the whole organ.
- **How to play it:**
  1. Record a note; overdub two or three more (CLOCK moves between passes = pre-spread voices).
  2. Both knobs to 11:00 — the specified starting point.
  3. Play keys: chords-of-loops under every root.
  4. Sculpt: LENGTH nudges the station parameter, MODIFY re-tunes the blend; small moves, big timbre.
- **Variations:** capture through Flip first = harmonically pre-stacked oscillator · ADSR + slow attack = a loop-choir swell machine · this patch + D6's portamento = the full "strange instrument."
- **Verification:** 🟢 recipe AND the 11-o'clock positions are MIDI-manual verbatim (p.7) — the only first-party numeric knob setting published for this pedal; 🟣 the surrounding workflow.

## Group E — Utility, subtle & studio

### E1 · A Good Listen
*The manual's own monitoring position: Mask with MODIFY at zero = "the pure micro-loop recording." The loop-builder's workbench.*
**Tags:** mask, utility, monitor, loop-building, precision, named-technique

- **Channels:** Micro-Looper ON (Mask).
- **Knobs:** MIX noon · CLOCK wherever the target patch needs it (build at the destination rate — CLOCK moves later transpose) · LENGTH anywhere (inactive at MODIFY min) · **MODIFY-looper FULLY DOWN — no disguise, no funny business**.
- **Toggles:** Looper **Mask** · Wet off while building.
- **Hidden options:** FADE at unity; BALANCE center.
- **MIDI snapshot:** `CC23=127 · CC19=0 · CC103=1 · CC102=0`
- **Use case:** manual-verbatim: "Because there's often a lot going on in the other loop modes, Mask is a useful place for getting a quick listen to the micro-loop without any funny business… also a good position for building up a micro-loop if you want more precision, before bringing it into the other modes." The pedal's mixing-console tape-monitor button.
- **How to play it:**
  1. Capture and overdub here first — every layer audible exactly as recorded.
  2. Check what the always-listening state actually grabbed (it may include wet trails you forgot were running).
  3. When the loop is right, flip the mode toggle — FREE PLAY carries it into Burst/Radio intact.
  4. Return here anytime mid-chaos to hear ground truth.
- **Variations:** this + HALF dip = tight, precise fragments for Burst · this is also the "predictable overdubbing" home (see Part I §4 note) · A/B trick: preset toggle with slot 1 = this, slot 2 = the mangled destination.
- **Verification:** 🟢 entirely manual-verbatim (p.38 "A GOOD LISTEN", p.31 FREE PLAY); 🟣 workflow dressing.

### E2 · Dry Glue Saturator
*The manual's own standalone trick: DRY GLUE dip on, MIX to zero — BAD MOOD becomes a stereo saturator / destroyer with no time effects at all.*
**Tags:** glue, saturator, utility, standalone, stereo, named-technique

- **Channels:** Both bypassed or on — irrelevant to the dry path; run it as a pure processor.
- **Knobs:** **MIX FULLY DOWN (isolates GLUE — the manual's instruction)** · CLOCK free (GLUE lives behind it; face position no longer matters once set) · others —.
- **Toggles:** any.
- **Hidden options:** **GLUE = the entire instrument now: 9:00 = console-ish gel · noon–2:00 = "very torn speaker overdrive" · high = bit-crush territory**.
- **Dip switches:** **DRY GLUE ON** (required) · MISO ON if feeding mono into a stereo chain.
- **MIDI snapshot:** `CC78=1 · CC15=0 · CC28=to taste · CC71=1 (optional)`
- **Use case:** manual-verbatim: "treat GLUE as a standalone effect by turning MIX all the way down… this will isolate GLUE and turn BAD MOOD into a stereo saturator / destroyer." A true-stereo drive/crush box — rare as a pedal category — for gluing a stereo synth, warming a mix bus at practice, or pre-crushing a signal into another looper.
- **How to play it:**
  1. DRY GLUE dip on, MIX at zero. That's the patch.
  2. Set GLUE by ear from gel to wreck; EQ (hidden) tilts the damage dark or bright.
  3. Save it to a preset slot — an instant "saturator mode" on the toggle (dips save with presets).
  4. Note the early-owner report that even the *default* GLUE runs hot — for "warm" keep it conservative.
- **Variations:** MIX at 9:00 instead of zero = saturator with a whisper of Soup behind it · GLUE via expression (assign nothing, plug in EXP — with no knob dips engaged EXP takes MIX… so for GLUE-under-foot use MIDI CC28 instead — note the asymmetry) · stereo width sanity: MISO+SPREAD for mono sources.
- **Verification:** 🟢 the technique is stated twice in the manual (pp.42, 45); 🟡 tone poles from the walkthrough; 🟣 numerics and the preset-slot workflow.

### E3 · Gentle Gel
*The disproof-of-concept patch: BAD MOOD as a polite, warm, low-key ambient thickener — everything the marketing says it isn't, all verified controls.*
**Tags:** subtle, warm, gel, low-key, tasteful

- **Channels:** Both ON, everything conservative.
- **Knobs:** MIX 10:00 (seasoning) · CLOCK 1:00 (clean rates) · TIME 11:00 · **MODIFY-wet at ~9:00 (mostly familiar reverb — the synthetic character nearly off)** · LENGTH noon · **MODIFY-looper Mask-min (honest loop, if used at all)**.
- **Toggles:** Wet **Soup** · ROUTING up · Looper **Mask**.
- **Hidden options:** **GLUE at ~8:30–9:00 — below its "pretty low" default (first-owner report: default is too hot for clean pads)** · EQ a hair CCW ("something more mellow that hides in the background" — the walkthrough's own words for this EQ zone) · CROSS 0.
- **MIDI snapshot:** `CC21=0 · CC22=0 · CC23=127 · CC19=0 · CC17=~30 · CC28=~20 · CC27=~55 · CC102=1`
- **Use case:** the always-on setting: a faint synthetic halo and a touch of glue on an otherwise untouched signal — proof the "wild side" pedal can sit politely in a chain between takes, and the honest baseline to A/B every other patch in this file against.
- **How to play it:**
  1. Set it, save it to a preset slot, forget it.
  2. When a song needs "a little something," this is the something.
  3. Knobs's caveat is the design brief here: "you can also make it very, very clean."
- **Variations:** TRAILS ON so bypassing exhales · MASTER VOLUME (CC30) trims unity precisely · nudge MODIFY-wet toward noon on the last chorus — the halo turns synthetic exactly when the song lifts.
- **Verification:** 🟢 all controls; 🟡 the "very, very clean" pole and mellow-EQ language from the walkthrough, hot-default report from an owner; 🟣 numerics.

### E4 · Fade to Delay
*The hidden FADE option turned down: overdubs decay generation by generation — the Micro-Looper becomes a long, strange delay with a loop's soul.*
**Tags:** fade, evolving-loop, pseudo-delay, decay, ambient-loop

- **Channels:** Micro-Looper ON (Mask or Radio); Wet to taste.
- **Knobs:** MIX 1:00 · CLOCK sets the "delay time" (loop length = repeat cycle) · LENGTH per mode · MODIFY-looper Mask-min for the honest version.
- **Toggles:** Looper **Mask** · Wet **Soup** low · ROUTING down.
- **Hidden options:** **FADE at ~9:00–10:00 — "loops gradually fade while overdubbing, for slowly evolving loops or the ability to treat the Micro-Looper Channel like a delay"** (manual-verbatim).
- **Dip switches:** **LATCH ON** — overdub latched = the channel behaves as an always-writing echo.
- **MIDI snapshot:** `CC23=127 · CC19=0 · CC26=~30 · CC75=1 · CC106=1 (latched dub) · CC103=1`
- **Use case:** the MOOD-family "looper as delay" move, now with a dedicated control: latch overdub and play — each phrase repeats on the loop cycle and dies away over a few generations. Slower and stranger than a delay pedal: repeats are loop-locked, and everything CLOCK does (transpose! slow!) happens to the echo tail.
- **How to play it:**
  1. FADE down a third; latch overdub; play.
  2. Phrases recirculate and sink — set FADE lower for faster forgetting, higher for near-looper persistence.
  3. Move CLOCK mid-decay: the dying repeats transpose in harmonized steps (a delay pedal cannot do this).
  4. Unlatch to freeze the current population as a normal loop again.
- **Variations:** in **Burst**: fading *sequences* — patterns that thin out and regenerate as you feed them · FADE at min + Radio/Dance = echoes that octave-rotate while dying · classic MkII trick preserved: high CLOCK = the closest to real-delay tracking.
- **Verification:** 🟢 FADE's function manual-verbatim (p.14); 🟢 latch behavior; 🟣 numerics and the performance framing (MkII's equivalent workflow is documented in the MkII corpus).

### E5 · Wide Loop, Narrow Loop
*The stereo-strategy patch: MISO, SPREAD, and the per-channel SPREAD hidden option — the manual's own example of a mono loop passing through a stereo reverb.*
**Tags:** stereo, spread, miso, imaging, utility

- **Channels:** Both ON.
- **Knobs:** musical content free — this patch is about the switches.
- **Toggles:** Wet **Soup** · ROUTING down · Looper any.
- **Hidden options:** **SPREAD per-channel = wet-only (the manual's example: "keep your micro-loop mono, but have it pass through a stereo reverb")**.
- **Dip switches:** **SPREAD ON** (stereo processing engaged — "each mode has its own unique approach to generating a stereo image") · **MISO ON** if the source is mono.
- **MIDI snapshot:** `CC72=1 · CC71=1 · CC32=0 (wet-only spread) · CC21=0 · CC22=127 · CC102=1 · CC103=1`
- **Use case:** deliberate stereo staging: the loop stays a solid mono object in the center; Soup blooms wide around it. The image *tells the listener what's bed and what's air* — and downstream stereo pedals inherit a coherent field instead of soup-on-soup.
- **How to play it:**
  1. MISO if mono in; SPREAD dip on.
  2. Hidden options: ROUTING-toggle position sets which channel gets the spread — wet-only here.
  3. Capture; listen to the mono loop sit while the reverb wraps it.
  4. Flip the per-channel setting live for arrangement moves: loop suddenly wide = the bed swallows the room.
- **Variations:** looper-only spread + dry-center = wide bed under a mono voice · **DRY KILL dip** converts this into a wet-only aux/parallel send for a mixer or switcher (kill applies even bypassed — mind your routing) · MkII heirloom rule still true here: SPREAD *processes* stereo, MISO *creates* it.
- **Verification:** 🟢 all three controls + the mono-loop/stereo-reverb example are manual-verbatim (pp.16, 44); ⚠️ which CC32 endpoint is "wet-only" is the §9 flag — confirm on hardware; 🟣 the staging aesthetics.

### E6 · Grand Entrance
*One-shot RAMP on engage: knobs rise (or fall) to their positions the moment the pedal comes on — "a wave of motion and activity when you first turn BAD MOOD on."*
**Tags:** ramp, swell, entrance, automation, performance

- **Channels:** Wet ON (Soup) as the showcase; looper optional.
- **Knobs:** **MIX = ramp speed (slow-ish, ~10:00 — a real swell)** · **CLOCK 1:00 = the ramp *destination* (with SWEEP=B it climbs from the bottom of the range up to here)** · TIME 2:00 · MODIFY-wet noon.
- **Toggles:** Wet **Soup** · ROUTING up.
- **Hidden options:** defaults.
- **Dip switches (control bank):** **CLOCK ON · BOUNCE OFF (one-shot = ramp) · SWEEP = B** — others off.
- **MIDI snapshot:** `CC63=1 · CC66=0 · CC67=0 · CC20=~35 · CC18=84 · CC21=0 · CC102=1`
- **Use case:** a built-in intro: engage the Wet Channel and the sample rate surges up from the depths to the set point — the texture literally wakes up, pitch and fidelity blooming into place, then stays. The manual's stated purpose, verbatim.
- **How to play it:**
  1. Dip CLOCK on, BOUNCE off, SWEEP=B; set CLOCK to the destination.
  2. Bypass, wait for the moment, engage: the rise happens once.
  3. Re-trigger by bypassing and re-engaging (TRAILS off for a clean re-arm).
  4. CC52=0 halts a ramp mid-flight — a brake pedal for drama.
- **Variations:** SWEEP=T inverts it — engage at pitch, *sink* to the destination (outro patch) · ramp TIME instead: Soup that opens from a closet into a hall on engage · EXP/CV epilogue: the same dip assignments hand the ramped knobs to an expression pedal (POLARITY dip flips direction; no dips engaged = EXP gets MIX) — one treadle morphs the whole texture, the MkII multi-knob trick intact.
- **Verification:** 🟢 ramp/bounce/sweep mechanics + the "wave of motion" purpose are manual-verbatim (pp.46–49); 🟣 numerics and staging.

---

## Coverage matrix

| Requirement | Where |
|---|---|
| Soup / Relay / Flip | A1–A4, C6 / B1–B3, B8 / D1–D5 |
| Burst / Radio / Mask | B4–B5, C5 / A1, A5–A6, B6–B7, C1 / C2–C3, E1 |
| Radio stations: Tape · Ambient · Orchestral · Shoegaze · Dance | B7 · A5 · A8, D5 · A6 · B6 |
| Routing: input only · both · looper only | A4, C6, C7 / A1, A8, C8 / A5, A7, B8, D5, E5 |
| Cross sources: input · looper→wet · wet→looper | C6 · C7 · C7 (step 4) |
| Glue: subtle → destroyed · dry-glue · standalone | E3 → C8 · D4, C8 · E2 |
| Sync: looper→wet · wet→looper | B1 · B8 |
| Freeze: Soup pad · Relay echo · Flip chord | A2, A4, D7 · B1, B3 · D1 |
| Ramp (one-shot) · Bounce (continuous) | E6 · A9, C1 var. |
| Stereo: SPREAD · per-channel SPREAD · MISO · mono | C8, D2 · E5 · E2, E5 · default-state patches |
| Dips: HALF · SMOOTH · LATCH · TRAILS · DRY KILL · DRY GLUE · FADE (hidden) | B4, E1 / A9, D1 var. / A4, B1, D7, E4 / A4, E3 / E5 var. / C8, D4, E2 / C5, E4 |
| Named techniques: Synthetic Starter · 2-Track · Chord Looper · Trail Catcher · Stable Sequencing · Threshold Surfing · Don't Touch That Dial · Dry Glue saturator | A2 · B1 · D1 · A7 · B4 · C2 · C1 · E2 |
| Manual freeze-ideas + A Good Listen + Replace + Vintage Harmonies | A2/B1/D1 · E1 · C4 · D2 |
| MIDI: clock sync both roles · divisions · Synth Mode (all 3 output types) · PC/preset workflow | B9 (BAD MOOD as follower; note: **no clock OUT exists — see below**) · B9 · D6–D8 · throughout |
| Early-owner tricks (verified in the field) | A5 (Ambient freeze, headroom) · B7 (dub-techno accident) · E2/E3 (hot Glue default) |

**One honest asymmetry vs the Big Time corpus:** Big Time can be a MIDI clock *master*; BAD MOOD's
MIDI manual documents clock **in** only (CC51 follow/ignore) — no clock-out is published. "Sync in
both directions" on BAD MOOD means the internal SYNC option (either channel leading, B1/B8), not
MIDI clock direction.

## Sources

**First-party (🟢 backbone)**
- Bad Mood Field Guide (manual, 27 pp.) — `gear/Chase Bliss Bad Mood/manuals/Bad-Mood_Manual_Chase-Bliss.pdf` (fetched 2026-08-28 from chasebliss.com)
- BAD MOOD MIDI Manual (9 pp.) — `gear/Chase Bliss Bad Mood/manuals/BAD-MOOD_MIDI-Manual_Chase-Bliss.pdf`
- Product page — https://www.chasebliss.com/bad-mood ($399, Small Batch Bliss, Nov 2026 est., 2+122 presets, ~200 mA)
- Launch blog (written by Knobs) — https://www.chasebliss.com/bad-mood-blog (the sibling/inversion framing; no-origin-story story; Tim Wilkins comic)

**Official video (🟡)**
- "Introducing – BAD MOOD" — youtube.com/watch?v=DRNCfhESRA4 (teaser: "every mode is new," new Glue, "CROSS MODULATION! NEVER BEEN DONE BEFORE!", "instant trouble, instant mischief")
- "BAD MOOD – Walkthrough" (Knobs, 25 m) — youtube.com/watch?v=5UgwxdzB9CQ (full transcript captured: Soup MODIFY=modulation/noon preference; Glue torn-speaker→bitcrush + "generally better on"; Cross squiggles→dropout; Flip 1/2/3/4-note zones + stereo spread; Mask crumbly-gates minimum + "stable-est mode"; Burst note-by-note construction + dig-in fills; all five Radio stations incl. station-blending, Shoegaze slice-size-vs-loop-length, Ambient+Soup pairing; sync/fade/synth acknowledged but not demoed)
- CB "every instrument through BAD MOOD" (Zack & Courtney; pedal steel/drums/harmonica; Relay into Radio, "Moog Soup," drum-machine Burst) — noted, not yet transcribed

**Press (🟡)**
- Synth Anatomy — synthanatomy.com/2026/07/chase-bliss-bad-mood-a-grumpy-sounding-experimental-ambient-fx-pedal.html
- gearnews — gearnews.com/chase-bliss-bad-mood-bad-tempered-ambient-creativity/
- Delicious Audio — delicious-audio.com/chase-bliss-bad-mood/ · No Treble — notreble.com/buzz/2026/08/04/chase-bliss-audio-gets-weird-with-the-bad-mood/
- GuitarPedalX (Glue refined from Lost + Found; order-window coverage) — guitarpedalx.com/news/gpx-blog/…bad-mood…
- Not found despite searching: Sonicstate, Premier Guitar, Guitar World, Reverb.com coverage (MkII-era only as of 2026-08-28)

**Community (🟡, days-old — the entire owner pool)**
- Elektronauts Chase Bliss megathread pp.151–155 — elektronauts.com/t/chase-bliss-effects-pedals/31096 (Ambient freeze trick, headroom trick, hot Glue default, Soup phaser tell, forward-only stretch / finer speed / no grain-size vs MkII, dub-techno accident, CV 0–5V-only warning, first arrivals Aug 26–28)
- Unreachable to automated fetch (browse manually): Reddit r/guitarpedals + r/chaseblissaudiophiles, TheGearPage, ModWiggler, CB Discord, the FB settings group — flagged as future recipe mines once owners accumulate

**Third-party demos (transcribed 2026-08-28 — mined in depth in `gear/Chase Bliss Bad Mood/research/Bad-Mood-MicroLooper-DeepDive.md`)**
- Mark Johnston "Secret Weapons" (1h20m, the deepest parameter source) — youtube.com/watch?v=KBY0gqpfpHw · David Hilowitz "chasing the distorted side of ambient" — youtube.com/watch?v=Z1B3pCYEKVo · Harp Lady / Emily Hopkins "craziest shoegaze pedal" — youtube.com/watch?v=uIXLHh-HYzU · Jason Mays — youtube.com/watch?v=9JAAUfurXmw · ambienttrash stereo demo (music-only) — youtube.com/watch?v=qrHkNQnEAF8 · Daniel Saint "a bad jam" (no captions) — youtube.com/watch?v=eoXawwPy4E4

**Repo cross-references**
- `gear/Chase Bliss MOOD MkII/research/` — the MkII corpus this library's §8 comparison and carried-over techniques draw on
- `Patches/Chase Bliss Big Time/` + `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` — the format/depth template this document matches


