# Vocal Stacking — Bon Iver-Style Layered Choirs

**Scope:** technique — Bon Iver-style layered vocal stacking as a generic recipe
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Aesthetic-stack relevance:** Bon Iver, vocal stacking
**Tags:** `vocal-stacking`, `bon-iver`, `formant`, `sm57`, `recipe`, `mixing`

---

## The Constraint That Became the Style

The Bon Iver vocal sound did not start as an aesthetic choice — it started as a workaround. Justin Vernon tracked all of *For Emma, Forever Ago* (2008) on a single [Shure SM57](https://www.musicradar.com/news/bon-iver-platinum-record-microphone) — the dynamic mic most engineers put on a snare. The SM57 is not a flattering vocal mic: it rolls off air, scoops upper-mids, and proximity-effects hard. To compensate, Vernon "employed layer upon layer of his falsetto vocals" — stacking identical passes rather than relying on a single take. That stacking became the signature. The takeaway is direct: if your mic, room, or voice sounds thin as a single take, *don't try to fix it with EQ first*. Sing it three to twelve times, layer the takes, and let mass do the work fidelity would otherwise do. The "Bon Iver constraint" is portable — it works as well on an SM58 in a closet as on Vernon's SM57 in a Wisconsin cabin. (For Vernon-specific mic and signal-chain history, see the sibling artist file linked below.)

## Step One — Track Multiple Takes, Don't Comp

The non-negotiable first move: record the same vocal line as separate, fresh performances. Do not record one perfect take and duplicate it in the DAW. Do not comp the best syllables across passes. Engineer Zach Hanson describes Vernon's process directly: "He will sit down with an SM7 in front of him and sing one line in one section of the song, and then he will duplicate that track, and sing another line" [(Sound on Sound)](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million). The micro-variations between performances — slightly different breath placement, slightly different vibrato onset, slightly different consonant length — are the entire reason the stack reads as a choir instead of a chorus pedal. Six to eight passes per section is a reasonable starting count for a home producer; *22, A Million* sessions reportedly had blocks of "six vocals in one section of the song and eight vocal tracks in another part," with some songs running to 40+ tracks total [(Sound on Sound)](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million). Start with six. Add more only if the song needs more density.

## Step Two — Vary the Capture Without Changing the Performance

Once you have your six identical passes, you want tonal variation between them — but you want it to come from capture, not from the singer's performance. Vernon's technique is to capture the same line on "different SM7s, or sit at different distances from the mic" [(Sound on Sound)](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million). At home, you can fake this in three ways: (1) move three inches closer or farther between takes, (2) angle the mic off-axis by 15–30 degrees on alternating passes, or (3) record half the passes through a different preamp or different mic if you have one. The goal is to make each layer occupy a slightly different mid-range carving, so when they sum they fill the spectrum like real bodies in a room would. Singers using a single SM57 or SM58 should especially exploit the proximity-effect dance — close-mic passes will have a bottom-heavy intimacy, off-axis passes will have a brighter, drier sit.

## Layering by Unison vs. Layering by Interval

There are two distinct stacking modes that produce two distinct effects:

**Unison stacks** — every layer sings the same notes as the lead. This is the dominant Bon Iver mode. The result is mass, not harmony. Vernon "layers identical voicings to create richness, and one big vocal sound rather than using varied pitches" [(Sound on Sound)](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million). Unison stacks read as "the singer is bigger" rather than "the singer has friends."

**Interval stacks** — additional layers sing a third, fifth, octave, or seventh away from the lead. This is the move you hear in the choral *outchoruses* of *Holocene* or the cathedral-style climbs in *re: Stacks*. A workable starting recipe for interval stacks ([LANDR](https://blog.landr.com/vocal-layering/)): a third above the melody (3–4 semitones) for sweetness, a fifth above (7 semitones) for power, an octave above ("felt more than heard," kept –8 to –12 dB below the lead) for shimmer.

Most Bon Iver-style productions use **unison stacks for verses** and **interval stacks for choruses or outros** — start the song with mass, end it with mass *and* harmony. Mixing the two within a single section is fine; mixing them poorly produces mud, so keep the interval layers panned wider and the unison stacks tighter to the lead.

## Formant Manipulation — Making One Voice Sound Like Many Bodies

Real choirs sound choral because they contain *bodies of different sizes*. A child singing the same note as a baritone produces a different formant — different resonant frequencies in the throat and chest — and the ear hears that difference as "multiple humans." A single singer stacked twelve times produces twelve formant-identical layers, which sums to "one big version of the same person." Formant manipulation tools fix this without changing pitch.

**Soundtoys Little AlterBoy** is the go-to. It shifts pitch and formant independently — leave pitch at zero and pull formant down (more chest, more masculinity) or push it up (more head, more childlike). Vernon ran "six of the saxophone tracks" through Little AlterBoy on *22, A Million* to "change the masculinity of how something sounds." Applied to a stack: instantiate Little AlterBoy on three of your six layers, leave three at zero, and offset the shifted layers in –2/–4/–6 or +2/+4/+6 increments. Jamie Lidell, profiled by [Soundtoys](https://www.soundtoys.com/jamie-lidell-little-alterboy/), combines Pro Tools varispeed with Little AlterBoy's formant control to "sneak extra layers of detail and texture" into a harmony stack — the principle generalizes: any tool that decouples formant from pitch is a body-faker.

**Antares Harmony Engine** is the heavier weapon. Its Choir feature can "turn each harmony voice into 2, 4, 8, or 16 individual unison voices," generating up to a 32-person ensemble from one vocal [(Antares)](https://www.antarestech.com/community/harmony-engine-blog). The realism controls (Humanize, vibrato variation, timing variation) separate "choir" from "chorus pedal" — turn them up. Harmony Engine is also the core of Francis Starlite's Prismizer and a published ingredient of the live Messina rig.

**Antares Choir Evo** is the focused, cheaper sibling — five-channel vocal multiplication with no harmony generation. Use it when your harmonies are already in place and each one needs to bloom into multiple bodies.

## Pitch Correction As Saturation, Not Correction

A Bon Iver-style stack almost always has Auto-Tune printed across it — not because the notes are wrong but because Auto-Tune is a *timbre* tool on already-in-tune voices. Engineer Brian Joseph: "Almost all these vocal tracks have Auto-Tune, which is part of his sound. It doesn't only tune his vocal, it also adds a kind of saturation that can be really musical" [(Sound on Sound)](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million). Recipe: after your stack is recorded but before you bus it, instantiate Auto-Tune (or Waves Tune Real-Time, or Melodyne in pitch-grid mode) on every layer, set the key correctly, and pull retune speed to fastest. The harmonic distortion the algorithm introduces at fast retune times is the glue that locks the layers together. If the result sounds "too perfect," back retune speed off a little — saturation without the obvious snap. Bypass it on solo to hear how dry the unprocessed stack is.

## Panning the Stack — Stage, Not Headphone Toy

The reflex move is to hard-pan every layer; this produces a hole in the middle and disconnects the vocals from the rest of the mix [(Vocal Market)](https://thevocalmarket.com/blogs/how-to/how-to-layer-vocals-like-a-pro-any-genre). A better mental model: treat the stereo field as a stage and place each singer where a real human body would stand. A common Bon Iver-style distribution for a six-pass unison stack:

- **Lead vocal** — dead center, the loudest element by 3–6 dB.
- **Pass 2** — 15 percent left.
- **Pass 3** — 15 percent right.
- **Pass 4** — 40 percent left.
- **Pass 5** — 40 percent right.
- **Pass 6** — 70 percent left or right (the "outlier" body that pushes the field).

For interval-harmony stacks (thirds, fifths, octaves), pan them *wider* than your unison stack so the chord opens up — thirds at 60/–60, fifths at 80/–80, octave layers split 50/–50. Automate the field: narrow the stack in verses (everything inside 30 percent) and widen it in choruses (push to the edges). This is a generic vocal-mix move, but the dynamic-width automation is what makes a stacked production *feel like it grows*.

## EQ Carve — Make Room for the Lead

A stack of six identical voices will eat the center of the spectrum and bury the lead. The fix is to EQ the stack as a single thing (bus it to a group) and carve a midrange notch where the lead lives. Practical starting points:

- **High-pass the stack bus** at 120–180 Hz. The lead vocal owns the low-mids; the stack does not need them.
- **Notch –2 to –4 dB at 1–3 kHz** on the stack bus, where the lead's intelligibility lives. The stack supports the lead by getting out of its way in the consonant band.
- **Gentle shelf boost at 8–12 kHz** on the stack bus if the SM57/SM58-style capture sounds dull; air, not presence.
- **Low-shelf cut at 200–300 Hz** if the stack feels boxy when summed.

The lead vocal itself should be EQ'd to bloom in the slot the stack carved out — boost where the stack is notched, cut where the stack is full.

## Reverb As Glue — Send Everything To The Same Room

The single most common mistake when stacking vocals is putting different reverbs on different layers. The stack will not glue. The right move: bus the entire stack to one reverb send and let the shared early reflections weld the layers into a single space. The Bon Iver-era favorite reverbs are the [AMS RMX16](https://www.antarestech.com/community/bon-iver-vocal-sounds-live) (dense early-'80s digital character), the Bricasti M7 set to "Dark Chamber," and the EMT 140 plate emulation. For a home recipe:

- **Stack bus** → short-decay plate (1.2–1.8s) at 15–20 percent wet. Soundtoys Little Plate, Valhalla Plate, or UAD EMT 140 all work. This is the *glue* reverb.
- **Lead vocal** → its own slightly longer plate or chamber (2.0–2.5s) at 10–15 percent wet. This sits the lead one step *in front* of the stack rather than buried inside it.
- **Optional outro/climax send** → a longer hall (3.5–5.0s) with predelay 40–80 ms, opened up only on the final chorus or outro. This is the "cathedral" gesture you hear on *Holocene*'s final stack.

The principle behind the recipe: all layers should share a *room*, the lead should sit *forward in that room*, and any "epic" reverb should be a third, separate space that opens up dramatically.

## When the Stack Beats a Single Take — And When It Doesn't

A six-layer stack is not always the right call. It is right when:

- The lyric is general/atmospheric and the song wants mass, not narration.
- The voice on its own sounds thin, harsh, or under-supported.
- The arrangement is sparse and the vocal needs to fill space.
- The section is an outro, bridge, or climax where you want to feel the song *grow*.

It is wrong when:

- The lyric is intimate, confessional, or specifically narrative — a single voice carries truth that a choir of one cannot.
- The arrangement is already dense — adding a stack on top of a busy band creates mud.
- The vocal performance has a particularly characterful single take (a crack, a breath, a vulnerability) that gets averaged out by stacking.
- The song needs *contrast* — keep the verses single-tracked so the choruses can bloom into a stack and the dynamic shift does work.

The Bon Iver discography itself uses both modes. *Re: Stacks* (the closing track of *For Emma*) is a remarkably restrained vocal arrangement compared to the earlier album cuts. *Holocene* opens with a relatively dry lead voice and only blooms into full stacking in its final third. The stack is a tool, not a default; the dynamic decision of *when to deploy it* is half the production.

## A Worked Example — The Outchorus of "Holocene"

*Holocene* (from 2011's *Bon Iver, Bon Iver*) is the canonical study in stacking dynamics. The vocal is sung "almost entirely in falsetto," peaking around F#5 with harmonies reaching higher [(SingingCoach)](https://singingcoach.ai/holocene-bon-iver). The song opens with a single-track-feeling lead — there is doubling, but the field is narrow and the layers are nearly unison. As the arrangement expands (acoustic guitars and bass underneath, claps and snare entering, keyboard pads filling the back of the room), the vocal expands in parallel. By the final outchorus, the voice has become "another instrument in the atmospheric mix" — a wide stack of unison falsetto and interval harmonies summed into a single choral mass. The production lesson is the *gradient*: a song can begin with a single voice and end as a choir without ever cutting between the two. Practically: track your unison stack and your interval stack as separate buses, automate each bus's level and width across the song, and let the choir emerge rather than appear.

## Recipe Summary — A Repeatable Workflow

1. **Sing the line 6–8 times.** Don't comp; fresh performance each pass.
2. **Vary capture, not performance.** Move mic distance, off-axis angle, or mic choice between passes.
3. **Tune every layer.** Auto-Tune at fast retune speed in the correct key, for the saturation as much as the tuning.
4. **Apply formant variation** to 50 percent of the layers. Little AlterBoy at ±2/±4/±6 formant offsets.
5. **Pan as a stage** — 15/30/40/70 percent spread, lead center, no hard-panned holes.
6. **Bus the stack** to a group, high-pass at 150 Hz, notch the midrange where the lead lives.
7. **Send the whole stack to one short plate** for glue; keep the lead's reverb separate and slightly longer.
8. **Decide where the stack belongs** in the song — verses small, choruses bloom, outros open up.
9. **Optional — add interval harmonies** (3rd, 5th, octave) as a *second* stack, panned wider, only in climax sections.
10. **Optional — add a Harmony Engine layer** for the Prismizer/Messina-adjacent diatonic-chord-from-one-voice effect, keeping Humanize and timing variation high.

## See Also

- [Bon Iver Vocal Layering and the Messina Device](../artists/bon-iver-vocal-layering-messina.md) — Vernon/Messina/Burton-specific session detail, the Messina rig, *22, A Million* signal chain, mic/preamp/compressor specifics, and the BJ Burton Fostex tape parallel.

## Cited Retrieval Topics

- Falsetto stacking as constraint-driven aesthetic
- Same-line duplication vs. comping
- Unison vs. interval stacking
- Formant manipulation for choir-from-one-voice
- Auto-Tune as saturation
- Stack panning and EQ carving
- Reverb glue strategies
- When to stack vs. when to leave single-tracked

## Sources

- [MusicRadar — Bon Iver Platinum-record SM57 story](https://www.musicradar.com/news/bon-iver-platinum-record-microphone)
- [Sound on Sound — Inside Track: Bon Iver *22, A Million*](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million)
- [WAVHeaven — How to Produce Like Bon Iver](https://medium.com/@wavheaven/how-to-produce-like-bon-iver-d37b543a74f6)
- [Soundtoys — Jamie Lidell's Little AlterBoy Vocal Harmony Trick](https://www.soundtoys.com/jamie-lidell-little-alterboy/)
- [Antares — Harmony Engine: Create a Virtual Ensemble from a Single Voice](https://www.antarestech.com/community/harmony-engine-blog)
- [LANDR — Vocal Layering: 7 Ways To Stack Vocals For Powerful Sound](https://blog.landr.com/vocal-layering/)
- [The Vocal Market — How to Layer Vocals Like a Pro](https://thevocalmarket.com/blogs/how-to/how-to-layer-vocals-like-a-pro-any-genre)
- [SingingCoach — How to Sing Holocene by Bon Iver](https://singingcoach.ai/holocene-bon-iver)
- [Antares — Bon Iver Vocal Sounds Live](https://www.antarestech.com/community/bon-iver-vocal-sounds-live)
