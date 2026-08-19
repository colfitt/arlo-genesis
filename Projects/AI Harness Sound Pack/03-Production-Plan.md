# Production Plan — recording the pack on this rig

The good news from the research pass: the studio documented in this repo is already a
professional UI-sound production facility. Google records Pixel sounds in the sound
lead's home studio; Microsoft synthesized all of Windows 11's cues. Nothing needs to be
bought. This plan turns the 15 prototypes into release-quality masters in roughly three
sessions.

## Why this rig is overqualified for the job

| Need | Already owned |
|---|---|
| Clean conversion & preamps | **UA Apollo x8** (desk), **RME Babyface Pro FS** (portable) |
| DAW | **Logic Pro** (primary for this — stock LUFS metering) or **Ableton Live 12** |
| The family voice, sampled | **Kontakt 8 / Komplete 15 Ultimate** — kalimba, marimba, celesta, music box are all in the factory + Spitfire libraries |
| The family voice, synthesized | **Arturia V Collection 11** (DX7 V for FM bells), Ableton Operator-style FM via Arturia; **OP-1 Field** for character passes |
| Color & character | Chase Bliss pedals, **Strymon Deco V2** (tape saturation), **Hologram Chroma Console**, **JHS Colour Box** (console color) via **Radial X-Amp** reamping |
| Space | **Valhalla Room** (tiny ambience tails), Strymon Big Sky if a hero sound wants shimmer |
| Repair & polish | **iZotope RX** (de-click/de-noise), **Ozone** (true-peak limiting, LUFS check), **Soundtoys** for transient/color |
| A real transient | **SM57** (the one pointed at the MPC speaker) or the OP-1 Field's built-in mic for felt/wood strike layers |

## The three-layer recipe (per cue)

Industry-standard hybrid stack — every cue is built from the same kit so the family
holds together:

1. **Voice layer** — the pitched notes from the spec, played on the chosen family
   instrument (see Session 1). This carries the melody/interval.
2. **Sub layer** — a sine one octave below, −12 to −18 dB under the voice, high-passed
   at 150 Hz. Adds weight on good speakers, disappears politely on phone speakers.
3. **Strike layer** — a tiny recorded transient (fingernail on kalimba body, felt
   mallet on wood, OP-1 Field mic on a muted pluck) at very low level. This is what
   makes it feel physical instead of synthetic.

## Session 1 — voice the family (half a day)

Goal: pick ONE instrument to be the pack's voice. Candidates, in audition order:

1. **Kontakt kalimba/mbira patches** (Komplete factory library) — warmest match to the
   prototypes.
2. **Arturia DX7 V** FM bell, rounded operators — the Windows 11 route, most "digital calm".
3. **OP-1 Field** FM/bell engine tracked through the **Deco** at low drive — the most
   "us" option: digital source, tape-rounded edges.

Process: load the MIDI from the prototypes (the spec table gives every note and
timing), play each candidate through the full 15-cue sequence, listen on monitors AND
a phone speaker. Pick one. Record/bounce all 15 voice layers at **96 kHz / 24-bit**
(interpolation headroom for any later pitch work; delivery is 48 k).

Keep takes human: play the two-note cues by hand, keep the best of ~5 takes each.
Micro-timing variance between cues is a feature — Google "flams" the Pixel boot notes
on purpose.

## Session 2 — strike layers + assembly (half a day)

1. Record strike transients: SM57 or OP-1 Field mic, close, quietest room available
   (closet + duvet is genuinely fine — noise floor matters, acoustics don't, at
   these lengths). Record 20–30 hits of 2–3 sources, 96 k/24-bit, peaks around −12 dBFS.
2. In Logic: assemble each cue = voice + sub + strike. Trim to onset, 2–5 ms fade-in,
   full fade-out on tails.
3. Character pass where wanted: reamp `done-big`, `connect`, `error` through Deco/
   Chroma Console via the Radial X-Amp for tape rounding. Subtle — the cue must stay
   clean at phone-speaker size.
4. **Variations:** for the three highest-frequency cues (`ping`, `message-in`,
   `progress`) render 5 variants each with ±10 cents pitch and ±10% level scatter;
   the harness picks randomly. This is the anti-fatigue trick used across the industry.

## Session 3 — mix, master, test, deliver (half a day)

**Per-cue chain (Logic):**
- High-pass 150 Hz (nothing below survives a laptop anyway; it just eats loudness)
- Gentle EQ: tame 2.5–4 kHz harshness; small presence lift only for Tier 1 cues
  (brighter reads as more important — Material's trick — without being louder)
- Transient designer: keep attacks defined, no pumping compression
- Ozone limiter in true-peak mode: ceiling **−1.5 dBTP** (codec headroom for OGG/AAC)

**Loudness (the numbers that matter):**
- Master mono. Target **−19 LUFS integrated mono** (≡ −16 stereo, Google's earcon
  spec) for Tier 2 "inform" cues.
- Tier 1 interrupt cues up to ~**−14 LUFS**; Tier 3 ambient down to ~**−24 LUFS**.
- Then match the family **by ear** in one Logic session, cues back to back — meters
  get the ballpark, ears set the final trims. `error` must always land below `ping`.

**The gauntlet (do not skip):**
1. 100-times loop test per cue — anything that develops an edge goes back to Session 2.
2. Play the full set over a podcast + over music, at low volume.
3. MacBook speaker, iPhone speaker, AirPods, monitors. A cue fails if its meaning
   doesn't survive all four.
4. Pairs check: connect/disconnect, approve/deny, question/done back to back — the
   mirror relationships must be audible.

**Delivery set (per cue):**

```
masters/  <cue>_48k24.wav          mono, 48 kHz / 24-bit, -1.5 dBTP
app/      <cue>.ogg                Vorbis q6, lowercase names (Android-safe)
app/      <cue>.m4a                AAC 192k (macOS/iOS/web fallback)
manifest.json                      id, file, tier, duration, LUFS, variant list
```

Filenames lowercase snake/kebab, no spaces, versions machine-sortable
(`ping_v03.wav`). The prototypes' `manifest.json` schema carries over so the harness
integration doesn't change when prototypes are swapped for masters.

## Harness integration notes

- Sounds mirror visual states — never the only signal (accessibility baseline).
- Respect OS do-not-disturb; expose per-tier volume, and a "minimal" preset that keeps
  only `mention`, `question`, `error`.
- Debounce: `progress` no more than once per 2 s; collapse cue bursts (N pings in
  500 ms → one `mention`-weight cue). Fatigue is a product-logic problem as much as a
  sound-design one.

## Budget & timeline reality check

DIY on this rig: **$0 and ~3 half-day sessions.** Market alternatives, for context:
marketplace licensing $1–5/sound (zero brand identity), freelance custom 15-sound
family ≈ $1.5k–8k over 2–6 weeks, agency sonic branding €15k+. If the pack ever
needs to become a company-wide sonic identity (marketing, video, hero brand sound),
that's the moment to hire a sonic-branding studio — and this pack becomes the brief
that saves half their discovery fee.

Full sourcing for every number above: `01-Research-Notification-Sound-Design.md`.
