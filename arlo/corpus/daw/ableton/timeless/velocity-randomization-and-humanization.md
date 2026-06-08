# Velocity Randomization and Humanization on MIDI Tracks

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** [Live 12 Reference Manual — MIDI Effect Reference](https://www.ableton.com/en/live-manual/12/midi-effect-reference/); [Live 12 Reference Manual — Random MIDI Effect](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#random); [Live 12 Reference Manual — Velocity MIDI Effect](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#velocity); [Live 12 Reference Manual — MIDI Tools (Velocity Shaper)](https://www.ableton.com/en/live-manual/12/midi-tools/); [Ableton Learn Live — Programming Drums](https://www.ableton.com/en/blog/programming-drums-in-live/)
**Tags:** `daw-ableton`, `live-12`, `daw-ableton-timeless`, `velocity`, `humanization`, `midi`, `recipe`

---

## Why humanize at all

A MIDI clip programmed straight onto the grid with identical velocities sounds mechanical because real performers never play that way — drummers vary velocity by 10–20 across consecutive hits, pianists' fingers naturally land microseconds early or late, and the velocity of a single drum hit changes its timbre as well as its volume (a snare hit at 70 doesn't just sound quieter than one at 110, it sounds different — fewer overtones, less crack). Humanization addresses both: small random offsets to velocity and timing make programmed parts breathe like played ones. The Random and Velocity MIDI effects shipped in Live 8 and remain the workhorse humanization tools in Live 12, even after the [Live 12 MIDI Tools Velocity Shaper transformation](https://www.ableton.com/en/live-manual/12/midi-tools/) added a more surgical clip-modification approach. Both workflows have their place: real-time MIDI effects modulate every clip on the track identically and the source notes stay editable; the MIDI Tools Velocity Shaper bakes the changes into the clip's note data. This file covers the classic Random + Velocity MIDI effect chain in depth, then sketches when the Live 12 alternative wins.

## The Random MIDI effect — what it actually does

The **Random** MIDI effect is a real-time device that intercepts incoming MIDI notes and randomizes their **pitch** by a controllable amount. It has four parameters per the [Live 12 Reference Manual Random entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#random): **Chance** (the probability, 0–100%, that any given note gets randomized), **Choices** (the number of possible pitch offsets the random selection picks from), **Scale** (the size of the largest random offset, in semitones from -24 to +24), and **Sign** (positive, negative, or bipolar — controls whether offsets go up, down, or both). Importantly, **Random does not randomize velocity** — its outputs are pitch offsets. For velocity randomization you stack a Random with a Velocity device, or use the Velocity device's own randomization knob (covered below). Random's most common humanization use is paired with **Scale = 1 semitone, Chance = low** to occasionally bump a note up or down a half-step, mimicking the way human performers sometimes hit a wrong note — but for pitched humanization in tonal contexts, downstream Scale or scale-aware tools are usually needed to keep output in-key.

## The Velocity MIDI effect — the workhorse

The **Velocity** MIDI effect is the device that does the actual velocity humanization. Per the [Live 12 Reference Manual Velocity entry](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#velocity), its core parameters are **Out Hi / Out Low** (output velocity range — incoming velocities get scaled to fit between these values), **Range** (random variance applied per note), **Drive** (compression or expansion of the velocity curve), and **Mode** (Fixed, Clip, Gate, Compress) that controls how incoming velocities map to outputs. The humanization-relevant knob is **Random** (also labeled Range in some Live versions) — it adds a random ± offset to each note's velocity. A typical humanization setting: leave Mode at Clip, set Random to 5–15 (out of 127), leave the input range alone. Every note that passes through gets ±5 to ±15 of velocity variance, which is enough to break up mechanical repetition without making the part sound chaotic. The Velocity device sits **before the instrument** in the MIDI track's signal chain — drop it on the MIDI track and it will affect every incoming note in real time.

## Classic chain — Random then Velocity, or just Velocity

The "classic Random + Velocity chain" referenced in older tutorials usually means two distinct moves stacked: Random for occasional pitch wobble, Velocity for the steady velocity humanization. In practice, for drum and synth tracks where you want only velocity variation (not pitch variation), **the Velocity device alone is enough** — its Random parameter does the velocity-only humanization. The chain becomes Random + Velocity specifically when you want both pitched and velocity variation, which is most common on pad and texture parts where occasional pitch surprises add musical interest. On drum racks, where pitch randomization would map different drums to different chains (causing snares to play as kicks etc.), use Velocity only or scope Random to off. The [Ableton drum-programming blog post](https://www.ableton.com/en/blog/programming-drums-in-live/) walks through the drum-rack case.

## Settings for drums — kick, snare, hihat

Different parts of a drum kit tolerate different amounts of velocity randomization. **Hi-hats** tolerate the most — real drummers vary hat velocity by 20–30 across consecutive notes naturally, and a hat with Random = 10–15 sounds dramatically more alive. **Snares** tolerate moderate randomization — Random = 5–10 keeps the snare's character intact while breaking up flam-like rolls. **Kicks** tolerate the least — a kick with high random velocity can suddenly drop a beat too quiet to land properly, breaking the groove. Use Random = 2–5 on kick if you want any randomization, or skip it entirely and just program kick velocities by hand. The asymmetry follows from how human drummers play: a drummer's foot on the kick pedal is the most consistent limb, the snare hand is medium, the hi-hat hand is the most varied. Live's drum-rack architecture means a single Velocity device on the rack affects all chains equally — for per-chain randomization, drop a Velocity device on each chain inside the rack instead of on the rack itself.

## Per-clip velocity randomization via clip envelope

A second classic approach: skip the MIDI effects entirely and use Live's **clip envelopes** to draw a velocity curve on a specific clip. In the MIDI clip editor, switch the envelope dropdown to **Note Properties → Velocity**, and draw a curve that humanizes individual notes — emphasize beats 1 and 3, ghost on the offbeats, drop the second chorus' verse hat to make room for something else. This per-clip approach is more surgical than the Velocity device but only affects the one clip; if you want the same humanization across many clips, the Velocity device wins. Clip envelopes are documented in the [Live 12 Reference Manual clip envelopes section](https://www.ableton.com/en/live-manual/12/clip-view/). For programmed acoustic drum parts where you want musical phrasing (crescendo into the chorus, decrescendo into the bridge), clip envelopes are the right reach.

## The Live 12 Velocity Shaper transformation — when to switch

[Live 12's MIDI Tools sidebar](https://www.ableton.com/en/live-manual/12/midi-tools/) added a **Velocity Shaper** transformation that bakes velocity changes into the clip's note data using an adjustable envelope curve. The user flow: select notes (or whole clip), open MIDI Tools sidebar, pick Velocity Shaper, draw the curve, click Apply (or leave Auto Apply on for live preview). Velocity Shaper differs from the real-time Velocity device in two important ways. First, it's **destructive** — once applied, the original velocities are overwritten in the clip (Auto Apply off and the Undo system are your safeguards). Second, it's **shape-based, not random** — Velocity Shaper applies a curve (crescendo, decrescendo, accent pattern), it doesn't add random jitter. So the Live 12 Velocity Shaper is the better tool for **intentional dynamic shaping** of a clip; the classic Velocity device's Random parameter is still the better tool for **random humanization jitter**. Use Velocity Shaper for "make this drum fill build up", use the Velocity MIDI effect's Random for "make this hat pattern not sound robotic."

## When to bake (destructive) vs. modulate (real-time)

The deeper architectural choice between the two workflows is **bake vs. modulate**. The classic Velocity MIDI effect modulates every note that passes through, every time the clip plays back — the source notes are untouched and the randomization is regenerated on each playback (subtly different every time, which is more "live"). The Live 12 Velocity Shaper bakes a single shaping pass into the clip's stored note data — the same shape plays back identically every time, deterministic and repeatable. For session work where you want the part to evolve as you re-trigger it (especially in live performance and generative arrangements), the real-time Velocity device wins. For finished arrangements where you want the part nailed down exactly as you heard it, MIDI Tools Velocity Shaper wins. Many producers use both on the same track: Velocity Shaper to draw the intentional shape, then a Velocity device after it for live jitter on top. The order matters — MIDI Tools transformations apply to clip data, then the real-time MIDI effects act on the playback stream.

## Humanizing timing — the Groove Pool, not MIDI effects

Velocity randomization handles dynamics but not timing. For timing humanization in Live, the canonical tool is the **Groove Pool**, not a MIDI effect. Groove templates apply timing offsets to notes based on their position in the bar, pulling some notes ahead and some behind by groove-defined amounts. Drop a built-in groove (Logic Swing 16, MPC60 Swing, etc.) on a clip via the clip's Groove dropdown, set the Amount, and the clip's notes nudge off-grid by the groove's pattern. This is fundamentally different from random timing offsets because grooves are **musical and consistent** — a hat that's pulled 5 ticks behind the beat every two beats sounds like swing; the same hat with random ±10-tick offsets sounds like a sloppy performer. Use grooves for swing and feel, save random timing offsets for cases where you specifically want sloppy. Cross-reference the I3 groove-pool file in this corpus and the general-corpus [groove-construction-and-pocket.md](../../../rhythm/groove-construction-and-pocket.md) for the principle layer.

## How much randomization is too much — by source

The "right" Random value on the Velocity device differs by source. **Drums:** 5–15 is typical, with hats tolerating the upper end and kicks the lower. **Lead synths:** 3–8 — too much randomization makes a melody line sound uncertain rather than human. **Bass:** 3–5 if any — bass is rhythmically rigid in most genres. **Pads and arpeggios:** 10–20 — these tolerate heavy randomization because no single note is structurally critical. **Piano and acoustic instruments:** 8–15, and consider adding a clip-envelope shape (crescendo into the bar line, etc.) on top of the random jitter. The rule of thumb: the more structurally important each note is, the less randomization it tolerates. A chord at the top of a verse is structural; a hi-hat 16th in the middle of a fill is not.

## What humanization can't fix

There's a working-engineer truth that random velocity and timing offsets do not produce a "human" performance. They produce a less-robotic MIDI part, which is different. A skilled drummer's velocity choices follow musical logic — accent on beat 1, ghost on the offbeats, crescendo into a fill, drop into a chorus — patterns that random jitter cannot replicate. For a part that needs real musical feel, the workflow is: program the notes, draw a Velocity Shaper or clip-envelope curve for the intentional dynamics, then layer a small amount of Random Velocity (3–8) on top for the inhuman-grid jitter, and finally apply a groove for the timing feel. The randomization is the last 5%, not the foundation. Producers who lean on Random as a substitute for thinking about the part end up with MIDI that sounds randomly varied but musically dead. The [Ableton drum-programming blog](https://www.ableton.com/en/blog/programming-drums-in-live/) makes this point too — humanization is a polish, not a fix.

## The "humanize" knob in the Velocity device vs. randomization

Some older tutorials reference a "Humanize" button or randomize-velocity action in Live's edit menu. That refers to the Edit menu's [**Note Velocity → Randomize**](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#velocity) command, which applies a one-time random offset to selected notes' velocities and bakes the change into the clip. This is functionally similar to the Live 12 Velocity Shaper but simpler — pick a percentage, apply, done. It's a destructive bake (like Velocity Shaper) but with no shape curve — just random offsets. For a quick "make this clip less mechanical" pass, it's the fastest move. For ongoing real-time randomization that survives across clip-edit sessions, the Velocity MIDI effect is the right reach. Live 12's MIDI Tools sidebar makes this menu command somewhat redundant; older tutorials referring to "humanize the selected notes" usually mean the Edit menu version.

## A complete humanization recipe — drums

A worked example for a programmed drum part. (1) Program the notes with deliberate velocity choices — beat 1 kick at 110, beat 2 at 95, ghosted snares at 60, accented snares at 105, hi-hats varying from 70 to 90 by position. (2) Drop a Velocity MIDI effect on the drum rack, set Random to 8 (gives ±8 of jitter on every note). (3) Apply a groove from the Groove Pool — pick "Logic Swing 16" or similar at 30–40% Amount for slight swing. (4) Optionally use the MIDI Tools Velocity Shaper to draw a slight crescendo across long fills. (5) Listen — adjust the Velocity device's Random down if the part sounds chaotic, up if it still sounds robotic. The order matters: intentional choices first, groove for feel, Random as the last polish. The same recipe scales to any rhythmic part — bass plucks, arpeggios, percussion loops — adjusted for the source's tolerance per the per-source guidelines above.

## Cited Retrieval Topics

- "how do i humanize midi in ableton"
- "ableton velocity randomization for drums"
- "what is the random midi effect in ableton"
- "ableton velocity midi effect settings for hats"
- "velocity shaper vs velocity midi effect ableton"
- "how to make a programmed drum part sound less robotic in live"
- "how much velocity randomization is too much"
- "ableton humanize notes menu command"
- "live 12 velocity shaper midi tools"
- "real time vs destructive velocity randomization in ableton"

## Sources

- [Live 12 Reference Manual — MIDI Effect Reference](https://www.ableton.com/en/live-manual/12/midi-effect-reference/)
- [Live 12 Reference Manual — Random MIDI Effect](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#random)
- [Live 12 Reference Manual — Velocity MIDI Effect](https://www.ableton.com/en/live-manual/12/midi-effect-reference/#velocity)
- [Live 12 Reference Manual — MIDI Tools](https://www.ableton.com/en/live-manual/12/midi-tools/)
- [Live 12 Reference Manual — Clip View](https://www.ableton.com/en/live-manual/12/clip-view/)
- [Ableton blog — Programming Drums in Live](https://www.ableton.com/en/blog/programming-drums-in-live/)

## See also

- [corpus/daw/ableton/timeless/classic-midi-effect-chains-scale-random-notelength.md](./classic-midi-effect-chains-scale-random-notelength.md) — the broader MIDI-effect chain context
- [corpus/daw/ableton/live-12/midi-generators-and-transformations.md](../live-12/midi-generators-and-transformations.md) — Velocity Shaper transformation and the MIDI Tools sidebar
- [corpus/rhythm/groove-construction-and-pocket.md](../../../rhythm/groove-construction-and-pocket.md) — DAW-agnostic groove and humanization principles
- [corpus/rhythm/drum-programming-by-genre.md](../../../rhythm/drum-programming-by-genre.md) — DAW-agnostic drum programming
