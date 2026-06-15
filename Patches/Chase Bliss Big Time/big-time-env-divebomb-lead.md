---
type: patch
title: Env Dive-Bomb Lead
device: Chase Bliss Big Time
date: 2026-06-15
description: "DOUG-designed lead delay where MOTION = Env (the envelope follower, MOTION mode 3) modulates the TIME clock so picking dynamics bend the repeat pitch/time — dig in and the repeats dive-bomb and warp like a delay with a failing power supply; ease off and they settle back to pitch. STATE Digital (no limiter) keeps the pitch movement legible and SCALE Off keeps the bends smooth glides. MOTION=Env is a published feature; the numeric COLOR/FEEDBACK/TILT/DEPTH/RATE positions are an unpublished dialable recipe (flying faders override them on recall)."
tags: [delay, envelope-follower, dynamics-reactive, pitch-bend, dive-bomb, lead, stereo, designed]
hidden:
  RATE: "alt under TIME — moderate (modulation speed; 'gets insane quickly')"
  DEPTH: "alt under CLUSTER — high (dive depth; 'gets insane quickly') -- dialable recipe"
  MISO: "auto-engages off mono IN-L (mono-in / stereo-out) so the dives fan out across the stereo field"
controls:
  - { name: "MODE", type: switch, value: "Short (46-736 ms — tight enough that the dives stay a lead effect, not a wash)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Digital (no limiter — pitch movement stays legible; a limiter would pump on top of the bend)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi (articulate warp — keeps the dive defined)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off (smooth glides — NOT quantized Thermae steps)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Env (envelope follower, MOTION mode 3 — drives the modulation; because TIME is a master clock, the follower modulates the clock itself = pitch dives)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~30-40% (low-modest — keep repeats legible, don't clamp; dialable recipe)" }
  - { name: "FEEDBACK", type: knob, value: "~40-55% (reactive lead delay, not a runaway wall; first ~10% is most of the throw — dialable recipe)" }
  - { name: "TIME", type: knob, value: "to taste in the Short range (this is the clock the Env follower modulates)" }
  - { name: "CLUSTER", type: knob, value: "low (let the core repeat read so the dive is obvious)" }
  - { name: "TILT EQ", type: knob, value: "at/just above noon (dialable)" }
  - { name: "WET", type: knob, value: "~45% (dry retained in series — a lead delay under the note, not wet-only)" }
  - { name: "RATE", type: knob, value: "moderate (alt under TIME — modulation speed)" }
  - { name: "DEPTH", type: knob, value: "high (alt under CLUSTER — dive depth; this is the dive-bomb amount)" }
  - { name: "SPREAD", type: switch, value: "off or widen (mono IN-L auto-engages MISO so dives fan out in stereo either way)", options: ["off", "widen", "ping-pong"] }
  - { name: "DRY KILL", type: switch, value: "OFF (series, dry retained) — flip ON in Options for a wet-only aux warp", options: ["off", "on"] }
  - { name: "MODE button (hold)", type: button, value: "panic-reset — snap back to a clean simple delay if a dive runs away" }
---

# Env Dive-Bomb Lead

## Concept
Echoes whose time bends with your picking dynamics — dig in and the repeats dive-bomb and warp like a delay with a failing power supply; ease off and they settle back to pitch. **MOTION mode 3 (the envelope follower)** drives the modulation, and because **TIME is a master clock**, the follower modulates the clock itself — so harder playing sags/snaps the delay pitch in real time. **SCALE Off** keeps the bends smooth glides (not quantized Thermae steps); **STATE Digital** (no limiter) keeps the pitch movement legible instead of a limiter pumping on top of the bend. A compressed-but-still-dynamic source out front (Clean, slow-attack ~2:1) gives the follower a clean musical dynamic curve to track. A Big Time trick no existing chain uses — and the first patch in the corpus to point Env MOTION at the **TIME clock for pitch dive-bombs** (the one other Env patch, `dynamics-crumble-long-echo`, points Env at misbias **degradation** depth, not pitch).

## How to play it
1. Set **MOTION = Env** (mode 3 — the envelope follower) and **SCALE = Off** so the bends are smooth glides, not quantized steps.
2. **MODE Short**; **STATE Digital** so no limiter fights the pitch movement; **VOICING HiFi** for an articulate warp.
3. In the Alt menu (hold the far-left SHIFT): push **DEPTH** (under CLUSTER) up for dramatic dives; set **RATE** (under TIME) moderate.
4. Keep **COLOR low-modest** and **FEEDBACK ~40-55%** so the line dives, warps, and settles instead of running away.
5. Feed it a leveled-but-dynamic source (e.g. CB Clean transparent enhancer) so the follower reads a clean dynamic curve, not a mangled one.
6. Play single-note lead lines and use right-hand pick force as the pitch wheel: soft = near pitch, hard accent = dive-bomb.
7. If a dive is too violent, drop **DEPTH** first; if it's inert, push **DEPTH** and let more dynamics survive the front comp.
8. Panic-reset: hold the center **MODE** button to snap back to a clean simple delay.

## Notes
- **MOTION mode 3 = Envelope follower** (Mark Johnston deep-dive: MOTION button steps 1 = Sine, 2 = Square, 3 = Env). TIME is a master clock, so the follower modulates delay time = pitch dive-bombs / warp. This is a published feature.
- **RATE / DEPTH live in the Alt menu** (RATE under TIME, DEPTH under CLUSTER) and per the deep-dive "get insane quickly" — high DEPTH = deep dives. They are hidden alt-knob positions here, dialed by ear/LED.
- **SCALE Off = smooth glides** (the failing-power-supply warp); SCALE On would quantize the bends into Thermae-style pitch steps — not the intent of this patch.
- **STATE Digital = no limiter**, cleanest/most stable feedback — keeps the warp articulate and the pitch legible. A limiter (Compressed / Saturated) would pump on top of the bend; misbias would add degradation noise that buries the pitch move.
- Runs **backwards from a wall chain**: you are conditioning the *modulator* (a clean dynamic curve into the follower), not slamming the delay — so keep COLOR low and front-comp musical, not crushed.
- **Honesty / distinctness flag:** the SEED billed this as "the first Big Time patch in the corpus to use Env MOTION." That is NOT accurate — `Patches/Chase Bliss Big Time/dynamics-crumble-long-echo.md` already uses MOTION Env (to ride **misbias degradation** depth). What IS new here: Env MOTION on **STATE Digital** pointed at the **TIME clock for pitch dive-bombs/warp** — a pitch-bend lead, not a degradation patch. Verified by scanning every `Patches/Chase Bliss Big Time/*.md` (all others use Off / Sine / Square except that one Env-misbias patch).
- **Numeric values are a dialable recipe, NOT published settings** — Chase Bliss publishes character, not numbers. The control surface (MOTION=Env, STATE Digital, SCALE Off, RATE/DEPTH alt locations) is verified against the deep-dive and GearProfile; the specific COLOR / FEEDBACK / TILT / DEPTH / RATE positions are designed starting points and the motorized flying faders override them on recall.

## Sources
- 🟢 character (numerics interpreted) — `gear/Chase Bliss Big Time/research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (MOTION button 1/2/3 = Sine/Square/Env; TIME = master clock; RATE/DEPTH in Alt menu under TIME/CLUSTER and "get insane quickly"; SCALE off = smooth glides).
- 🟢 character — `gear/Chase Bliss Big Time/research/links/cb-big-time-factory-presets-recipes.md` (STATE Digital = no limiter, cleaner textures + stable feedback; COLOR-vs-FEEDBACK gain rule).
- 🟢 character — `gear/Chase Bliss Big Time/research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md` (first-party per-STATE character: Digital = clean/stable).
- `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` (low COLOR keeps repeats legible; MISO auto-engages on mono IN-L; hold-MODE = panic reset).
- Distinctness checked against `Patches/Chase Bliss Big Time/dynamics-crumble-long-echo.md` (the other Env-MOTION patch — misbias degradation, not pitch dive-bomb).
- 🟣 Provenance: designed (DOUG) — MOTION=Env is a published feature; the numeric COLOR/FEEDBACK/TILT/DEPTH/RATE positions are an unpublished dialable recipe, flagged as such (Chase Bliss publishes character, not numbers; flying faders override on recall).
