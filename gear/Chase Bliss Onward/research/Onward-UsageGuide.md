# Chase Bliss Onward — Usage Guide

The Onward is **two parallel channels** you play like an instrument: a **FREEZE** channel
(captures and sustains a chunk into an infinite pad) and a **GLITCH** channel (samples a
~1-second chunk and stutters/repeats it), blended by **MIX**. It's a **dynamic, always-
tracking sound-design / layer-maker** — not a commit-style looper — so in this rig it lives
*before* the granular/space pedals (**Onward → Microcosm → Dark Star**), generating evolving
capture that the Blooper commits and the Microcosm re-granulates. The core move everyone
lands on: **latch FREEZE to lock a drone, then play glitchy or lead material over the top.**
It samples any source, so the banjo, baritone, and VG-800/COSM output are all fair game.

> Coverage note: young (June 2024), niche, and **no public firmware changelog** exists — so no
> old-vs-new worries. Reddit + the TheGearPage megathread (the densest tip pools) were
> unreachable to the agents (blocked/paywalled) — a manual skim is the way to go deeper. MIDI
> (clock, retrigger, factory reset) is in the reusable `cb-stack` files. *(onward-forum-landscape, community)*

---

## 1. Essential workflows

### The two channels
- **FREEZE** (sustain/pad): **SIZE = the fade-in envelope** of the held sound; **SUSTAIN =
  feedback** (low = repeats fade, **max = infinite hold until you resample**). Hold/latch the
  footswitch to lock it and play over. *(aaron-rusch-freeze)*
- **GLITCH** (sample/stutter): **SIZE = how much of the front of the grabbed ~1s chunk plays**
  — so a **hard pick/banjo transient survives a small SIZE**, while a slow swell gets lost
  (its front is quiet). Audition it with MIX full + SUSTAIN max. **FADE** = feel: FAST replaces
  the sample immediately; SLOW won't even commit short staccato hits (feels like it ignores
  you); USER = a custom fade in the hidden menu. *(aaron-rusch-glitch)*
- **ERROR** (per channel, timing-linked to SIZE so it stays rhythmic): **Timing** = random
  size = rhythmic variation; **Condition** = mutes + sample-rate-reduction bite (chaotic);
  **Playback** = destabilizes speed/direction (reversing, octave jumps). **Effects:** OCTAVE
  (noon off, L = down/half, R = up/double), TEXTURE (L = bit/SRR, R = OD), ANIMATE (L = vibrato
  whose rate follows SIZE, R = slow chorus). *(aaron-rusch-glitch, doug-hanson)*

### Capture, momentary & dips
- **Capture is dynamic and *replacing*, not stacking** — each new note forgets the old one
  ("looper-light, not a looper"). **Tap to engage; hold to lock** the current sample to play
  over; the **LATCH dip** makes hold latch (owners single this out as the enabling dip). *(aaron-rusch-overview, guitar-com)*
- **Auto-handles chord changes** — feed it one chord after another and it re-chops the new
  signal, no footswitch dance. *(gearnews via community)*
- **Dips:** **HALF SPEED** (2s, lo-fi, Glitch only), **REVERSE** (Glitch backward), **MISO**
  (mono→stereo), **DUCK** (dips when you play), **SIDECHAIN** (Freeze dips on each Glitch reset =
  pumping), **MANUAL** (footswitch-triggered sampling vs dynamic), **LATCH**. *(doug-hanson)*

### Hidden menu, routing & clock
- **Hold both footswitches + move a control** for hidden options: **SENSITIVITY (on SIZE)** =
  trigger threshold (noon default; dial toward LESS for the hot GK-5 so it doesn't grab clicks);
  **BALANCE (on MIX)** = relative loudness of the two channels; **per-channel ROUTING** (isolate
  ERROR / FADE / ANIMATE-EFFECT to one channel only); plus User-fade, Error-Blend, EQ, Duck-
  Depth. **Tap tempo = double-tap both footswitches.** Factory reset = CC56 / power-up gesture. *(aaron-rusch-hidden-options)*
- **MIDI clock:** with clock present, **SIZE = the subdivision** so Glitch locks to tempo;
  reuse the cb-stack map (**CC51** ignore, **CC53** subdivision, **CC108/CC109** Glitch/Freeze
  retrigger, SIZE = CC14, ch.2, via the CB MIDIbox/TRS). *(doug-hanson, cb-stack-clock-sync-per-pedal)*

---

## 2. Signature recipes & settings

**No big recipe library yet** (young pedal). Where settings live, ranked: the **"Presets for
Chase Bliss" iOS app** (unofficial, Laurens Lamberts — browse/share/Bluetooth-push, the de-facto
community hub), the **manual's starting points** (Instant Eno / Sub Synth / Auto-Repeater /
Living Pad — in the dossier §13), and presets named in CB's Courtney Swain demo. *(onward-preset-recipe-sources)*

**Copyable values found:**
- **Sprawling ambient:** **SIZE ~3:00, MIX all the way up** → "turns any sounds you play into a
  sprawling ambient composition." *(courtney-swain)*
- **Sub-synth drone:** OCTAVE hard-left (down/half) + SUSTAIN max + FADE slow + hold-Freeze-to-
  lock = infinite sub; TEXTURE-right (OD) for a warmer, darker pad. *(aaron-rusch-freeze)*
- **Classic repeater:** simple infinite Glitch loop (SUSTAIN max). **"Frantic company":** wild
  glitch burst on attack + soft infinite freeze in the gaps. *(courtney-swain)*
- **Getting-started dips:** all OFF except **LATCH**; then add SPREAD/MISO (width), HALF SPEED
  (longer lo-fi glitch), DUCK/SIDECHAIN (pumping). *(onward-preset-recipe-sources)*

---

## 3. Power-user tips, tricks & hidden features

- **Freeze-lock + play-over** (the core trick, 3 independent sources): latch FREEZE, play over the
  held drone with dry passing through. *(aaron-rusch, guitar-com, delaydude)*
- **MIX at noon = the Freeze pad sweet spot; MIX full up = total float-away** (all-wet drone wall). *(delaydude)*
- **Error × Type-toggle × Glitch = the most creatively adventurous zone.** *(guitar-com)*
- **Route an Effect to one channel only** (hidden) — e.g. TEXTURE drive on Glitch while the Freeze
  pad stays clean. *(delaydude, aaron-rusch-hidden-options)*
- **Samples any source well** — field recordings, vocals (Swain), drums, the VG-800's COSM output. *(gearnews via community)*

---

## 4. Notable users & techniques

- **Courtney Swain (Bent Knee)** — the most instructive use (CB vocal demo): **Freeze = sustained
  base voice, Glitch = rhythmic textural top voice**, played together; MANUAL mode for hands-on
  capture/stop; "bounce the SIZE" for evolving subdivisions. Maps onto banjo-lead-over-walls. *(courtney-swain)*
- **A Last Picture From Voyager (ALPFV)** — closest aesthetic match: the track **"Beautiful
  Errors"** (2025 "Chase Bliss Journey" EP) is built around embracing the **ERROR section** — the
  rig's "recorded-wrong" target. Runs Onward in a CB ambient stack with Blooper + MOOD. *(alpfv-onward)*
- **CB design team (Majeski/Korte/Bramble)** — official walkthrough = canonical design intent
  (the secret all-Errors blend, lock-to-follow, per-channel stereo errors). *(chasebliss-onward-walkthrough-official)*
- **Tier-2 sightings (board photos/promo, technique undocumented):** James Blake, Chris Vanderkooy
  (Peach Pit), Balsac (GWAR), Austin Hull. *(onward-artists-roundup)*

---

## 5. Rig-specific recipes & MIDI

- **Banjo rhythmic stutter:** SIZE-down **Glitch** (the percussive attack survives) → banjo rolls
  become tight rhythmic stutter beds; dial **SENSITIVITY toward LESS** for the hot GK-5 so it
  doesn't over-trigger. *(aaron-rusch-glitch, aaron-rusch-hidden-options)*
- **Banjo/baritone → infinite pad:** **Freeze + SUSTAIN max** sustains a banjo chord into a pad it
  physically can't hold; OCTAVE-down for a baritone sub-drone. *(aaron-rusch-freeze)*
- **Two-personality patch (the rig's signature Onward move):** use hidden **ROUTING + BALANCE** to
  run a **Freeze sub-drone underneath + a Playback-error Glitch tracking on top** — a hands-free
  pad + tracking glitch nothing else in the rig does. *(aaron-rusch-hidden-options, delaydude)*
- **Clock from the Digitakt:** SIZE = the Glitch subdivision so banjo/baritone stutters lock to
  the kit; fire **CC108/CC109** from the DT2 for clock-quantized re-triggers. Without MIDI, double-
  tap both = tap tempo. *(doug-hanson, cb-stack-clock-sync-per-pedal)*
- **Role-split (don't duplicate):** Onward = the **dynamic, hands-free, warp-a-loop layer maker**;
  the **Blooper** commits/builds loops, the **Microcosm** re-granulates. Home: **Onward → Microcosm
  → Dark Star** on Board 2. *(aaron-rusch-why-buy-this, onward-vs-microcosm-mood-blooper)*
- **MIDI:** syncs GLITCH timing to clock; **2 onboard presets**, PC recall in the one-PC whole-stack
  scene; default ch.2; **dips save into presets** (see the gotcha). *(cb-stack-preset-scene-recall)*

---

## 6. Best learning resources

- **Aaron Rusch Guitar — 5-part series** (unsponsored, owner): the deepest tutorial set; **Part 4
  "Hidden Options" is the densest**. The channel to study for exact knob behavior.
- **Doug Hanson** — the most *efficient* full spec (every control + all 8 dips + routing + MIDI
  subdivision in ~2 min). Best quick reference.
- **Chase Bliss (official) "Onward – Walkthrough"** — design intent + the secret Error-blend.
- **Courtney Swain (CB vocal demo)** — the best on-aesthetic technique (Freeze base + Glitch top).
- **guitar.com review** + **delaydude review** — best written usage sources.
- **Communities (untapped):** TheGearPage Onward megathread (20+ pp, paywalled) and Reddit
  r/chasebliss + r/guitarpedals (uncrawlable here) are the densest tip pools — skim manually;
  Morningstar forum for MIDI-loop-switcher integration. *(aaron-rusch-*, doug-hanson, chasebliss-onward-walkthrough-official, courtney-swain, guitar-com, delaydude, onward-forum-landscape)*

---

## 7. Common pitfalls / gotchas

- **"When you get loud, it gets loud"** — the dynamics→volume jump is the #1 thing to tame (esp.
  with the hot GK-5); back off input or use DUCK. *(guitar-com)*
- **Dips save *into* presets** — a weird preset can silently carry MANUAL (feels "dead"/no
  triggering), DUCK/SIDECHAIN, MISO, or HALF-SPEED into the next song. Recovery: **turn all dips
  off** → middle preset → SENSITIVITY ~noon → factory reset (CC56). *(onward-troubleshooting-dips-off)*
- **Stuck Dry-Kill / config corruption in a MIDI loop switcher** (real ML10X report) — **fixed by
  factory reset.** *(morningstar-onward-ml10x)*
- **Not for fast/tight rhythm** — it's an ambient/textural box; "fast rock riffs are not ideal." *(delaydude)*
- **It doesn't replace** a delay or a dedicated freeze pedal (Superego) — different job. *(onward-vs-microcosm-mood-blooper)*
- **SLOW FADE ignores short staccato hits** by design — use FAST/USER if it feels unresponsive. *(aaron-rusch-glitch)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `aaron-rusch-onward-overview-quickstart.md` — Part 1: I/O, channels, preset save, control quick-start
- `aaron-rusch-onward-freeze-channel.md` — Part 2: Freeze deep-dive (SIZE = fade envelope, sub pad)
- `aaron-rusch-onward-glitch-channel.md` — Part 3: Glitch (SIZE = front-of-sample, Error, Fade-as-feel)
- `aaron-rusch-onward-hidden-options.md` — Part 4 (densest): hidden menu, Sensitivity/Balance/routing, tap, reset
- `aaron-rusch-onward-why-buy-this-workflows.md` — Part 5: the two real workflows + buying advice
- `chasebliss-onward-walkthrough-official.md` — CB launch walkthrough (design intent, Error-blend)
- `doug-hanson-onward-demo-feature-rundown.md` — efficient full spec of every control + dips + routing
- `courtney-swain-onward-vocals-demo.md` — Swain's Freeze-base/Glitch-top technique + named presets

**Links** (`research/links/`)
- `onward-preset-recipe-sources.md` — where recipes/presets live (CB app, manual, demo presets) + copyable values
- `courtney-swain-onward-vocals-demo.md` — Swain technique + named factory presets distilled
- `alpfv-onward-beautiful-errors.md` — ALPFV's ERROR-forward ambient track
- `onward-artists-roundup.md` — ranked artist roundup with honesty flags
- `wayward-zoia-onward-glitch-clone.md` — ZOIA recreation of the Glitch section (CCs ≠ real Onward)
- `guitar-com-onward-review-usage.md` — placement, LATCH, dynamics gotcha, Error×Type×Glitch
- `delaydude-onward-review-usage.md` — playing-style-as-macro, MIX float-away, per-channel routing
- `morningstar-onward-ml10x-gotcha.md` — stuck-Dry-Kill in a loop switcher, fixed by factory reset
- `onward-troubleshooting-dips-off.md` — "turn all dips off" recovery rule
- `onward-vs-microcosm-mood-blooper-community.md` — role framing vs the rig's other glitch boxes
- `onward-forum-landscape-and-firmware.md` — where the community lives + access flags + firmware status
- `tgp-onward-megathread.md` — documents the main (paywalled) forum thread
- *(MIDI/clock: reuse `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`)*

## Sources

Video (YouTube): Aaron Rusch `TcQqftZbsXM`, `3MB4F4ldH8I`, `pDZ_jZqzOs4`, `RZDGGQZ01AE`,
`VMxExzUHq7w` · CB official `ez2TyzuWOLs` · Doug Hanson `UtGwQ6OfZNk` · Courtney Swain `gzP8yXCznRk`
· Knobs `ozK-TgxIq8c` (cinematic, not transcribed).
Official: chasebliss.com/onward + manual; the "Presets for Chase Bliss" iOS app (unofficial).
Community: guitar.com · delaydude.de · forum.morningstar.io · gearnews · TheGearPage (paywalled) ·
Reddit r/chasebliss + r/guitarpedals (uncrawlable). Artists: equipboard.com · alpfv.bandcamp.com.
CB-stack MIDI: `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`.
