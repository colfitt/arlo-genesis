# Drum Programming by Genre

**Scope:** rhythm
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Attack Magazine *Secrets of Dance Music Production* and *Secrets of Techno Production*; Sound on Sound drum-programming articles; Ableton Live manual
**Tags:** `rhythm`, `drum-programming`, `genre`, `electronic`, `pop`, `recipe`

---

## Drum patterns as genre fingerprints

Every modern genre announces itself in the first bar of drums, and the cues are remarkably stable. The kick distribution (every beat? on 1 and 3 only? syncopated and sparse?), the snare or clap placement (backbeat on 2 and 4? on 3 only? displaced?), and the hi-hat subdivision (8ths? 16ths? mixed?) are the three variables that determine where a beat sits in the genre map. As [Native Instruments' "7 drum patterns every producer should know" guide](https://blog.native-instruments.com/drum-patterns/) catalogs, you can recreate the rhythmic identity of almost any popular style by picking the right combination of these three. The rest — the swing percentage, the velocity profile, the percussion overlays — is what separates a generic pattern from a song. This document walks through the canonical patterns by genre with specific programming values.

## House (4-on-the-floor, off-beat hats)

The house template is the most reproducible drum pattern in modern music. **Kick on every quarter note** (1, 2, 3, 4); **clap or snare on 2 and 4**; **closed hi-hat on every off-beat 8th** (the "&" of 1, 2, 3, 4); **open hat on the off-8th of 4** (right before the bar loops). Tempo: **120–128 BPM**, with deep house at 118–122 and tech-house at 124–128. Per [Ben Rainey's house programming guide](https://www.benrainey.co.uk/blog/drum-programming-house-music) and [MusicRadar's four-to-the-floor tutorial](https://www.musicradar.com/how-to/how-to-program-6-different-four-to-the-floor-grooves), the open hat's job is to lift energy into the next bar — putting it on the off-eighth of 4 is the classic disco-inheritance move. Critical detail: in most DAWs, place open and closed hat samples on the same MIDI choke group so the closed hat cuts off the open hat's tail, mimicking a real drummer pressing the hi-hat pedal. Swing typically minimal (50–53%); house lives in straight, propulsive time rather than shuffle.

## Techno (machine-precise, layered subs)

Techno shares the four-on-the-floor kick with house but trades warmth for industrial precision. Tempo: **125–135 BPM**, with rolling techno around 130 and "Berlin" hypnotic techno often 128–132. Per [Attack Magazine's "Rolling Techno" beat-dissected](https://www.attackmagazine.com/technique/beat-dissected/rolling-techno/) and the [Jeff Mills "The Bells" deconstruction](https://www.attackmagazine.com/technique/deconstructed/jeff-mills-the-bells/), the kick is typically a distorted TR-909-style sample with a long tail, often layered with a separate sub-bass hit. Hi-hats run 16th notes, frequently with velocity-randomized accents and pitch automation to add motion. Claps land on 2 and 4 but are often more recessed than in house, sometimes a half-bar phrase rather than every other beat. The genre's distinctive feature is **percussion-layer minimalism with energy controlled by mute/unmute rather than fills** — as Attack's Mills deconstruction notes, "there are no programmed drum fills or sequence changes; all energy is directed by muting and unmuting looping patterns."

## Boom-bap hip-hop (kick-snare displacement, sampled feel)

The canonical 90s East Coast hip-hop pattern: **kick on 1 and the "and-of-3" or "and-of-2"; snare on 2 and 4; closed hat on every 16th**. Tempo: **85–95 BPM**, with the deepest pocket usually at 88–92. Per [BVKER's boom-bap drum patterns guide](https://bvker.com/boom-bap-drum-patterns/) and [MIDI Mighty's three boom-bap patterns](https://midimighty.com/blogs/resources/three-boom-bap-drum-patterns-audio-download), the genre is defined by **kick displacement** — kicks land in unexpected places, never on a strict 1-and-3 pattern. The "ghost kick" — a quieter kick just before the main kick or snare, creating a "ba-boom" or "ba-bap" effect — is the trademark sound. Swing values in the [Attack Magazine boom-bap beat-dissected](https://www.attackmagazine.com/technique/beat-dissected/90s-boom-bap-hip-hop/) reach **57% on the drum pads and 74% on the hi-hats**, with claps "nudged a few milliseconds" off-grid for that wonky feel. The MPC-forum consensus for boom-bap swing clusters around **54–58%** for general drums, occasionally pushing the hats higher.

## Trap (sparse 808 kicks, hi-hat trills)

Trap inverts the busy-kick hip-hop tradition: **the 808 kick is the bass, and it plays sparse, syncopated patterns — not every beat**. The snare or clap lands on **beat 3** (sometimes 2 and 4, but the half-time feel of trap typically puts the backbeat on 3 only). Tempo: **130–150 BPM** notated, but listeners feel it as half-time at 65–75 BPM. Per [Emastered's trap drum patterns guide](https://emastered.com/blog/trap-drum-patterns) and [MusicRadar's trap hi-hat tutorial](https://www.musicradar.com/how-to/how-to-program-mixed-resolution-trap-style-hi-hat-patterns), the defining feature is **mixed-resolution hi-hats** — a base pattern of straight 8ths or 16ths with frequent **32nd-note "trills" and triplet bursts**, often with pitch automation and velocity modulation. Per [Reason Studios' trap drum cheat sheet](https://www.reasonstudios.com/news/post/trap-drum-basics-super-neat-beat-cheat-sheet), a typical 1-bar pattern might have 8th-note hats on beats 1–2, drop into 16ths on 3, then a 32nd-note trill on 4. The 808 kick and the snare/clap should not collide — leave silence around each, because the 808 *is* the bassline.

## UK garage / 2-step (shuffled kicks, snare displacement)

UK garage trades the 4-on-the-floor kick for **syncopated kicks that skip beats**, with the snare on **2 and 4** but the kicks landing on **1 and the "and-of-2" or "and-of-3"**. Tempo: **130–140 BPM**, classic UKG around 135. Per [Studio Brootle's UK garage guide](https://www.studiobrootle.com/uk-garage-drum-pattern-with-presets-and-bassline/) and the [Attack Magazine rolling-2-step beat-dissected](https://www.attackmagazine.com/technique/beat-dissected/rolling-2-step-garage/), the genre's signature is heavy swing — typically **60–65% in the groove pool**, with a common preset being "SP1200 16 Swing-71 at 60% strength." The hi-hats often pair up in tight clusters (two 16ths close together) to accentuate the shuffle. The kick-and-snare pattern looks straight on paper but feels skippy because every 16th is referenced to a swung grid, making the whole thing dance against itself. Bass typically locks to the kicks with extended sustained notes between them.

## Drum and bass / jungle (chopped breakbeats at 174 BPM)

DnB and jungle live at **170–180 BPM**, with the canonical reference being **174 BPM**. The rhythmic basis is the **chopped breakbeat** — historically the Amen, Funky Drummer, or Apache breaks — sliced into individual kick/snare/hat hits and reprogrammed. Per [EDMProd's jungle production guide](https://www.edmprod.com/how-to-make-jungle-music/) and [KAN Samples' Amen break tribute pack](https://kansamples.com/blogs/free-drum-and-bass-sample-packs/amen-break-tribute-pack-free-drum-bass-sample-pack-free-download), the snare classically lands on 2 and 4 but with extra ghost snares scattered through the 16th grid. Kick pattern is variable but typically syncopated, often with **two kicks at the start of the bar and a ghosted kick on the "and-of-4"**. The hi-hats from the original break, when preserved, carry the genre's specific feel — many programmed DnB drums sound stiff specifically because the original breakbeat's micro-timing has been quantized out. The modern workflow: chop a break to a Drum Rack or sampler, reprogram the slices with the original timing preserved, then layer punchier modern kick/snare samples on top.

## Rock and indie (driven 8ths, live feel)

Rock and indie rock are the most "drummer-shaped" of the programmed genres. **Kick on 1 and 3 (or 1, the "and-of-2," and 3); snare on 2 and 4; straight 8th-note closed hi-hat**. Tempo: **100–140 BPM**, with indie typically 110–125, rock 120–140. Per [Indie Band Guru's essential indie grooves guide](https://indiebandguru.com/essential-drum-grooves-every-indie-producer-should-know/) and [Zildjian's 8th-note rock beats lesson](https://ae.zildjian.com/education/beginner-drum-set-lessons/zildjian-drum-set-method-lesson-10/), the genre relies on a "driving kick-snare pattern with straight 8ths on the hi-hat" that supports rather than dominates. Programming considerations: leave hats at varying velocities (an accent pattern with the downbeat hat 10–15 velocity units louder than the off-beats); add the occasional pushed or pulled snare (3–7 ms early for urgency, 5–10 ms late for laid-back); program a snare crack with two layered samples (a top-snare close-mic plus a room sample) for live drum realism. Rock drums almost always sound better with the hat velocities programmed in a 100/75/85/75 accent pattern across the four 8ths in a beat than with everything at a flat 100.

## Pop (genre-blending modern beats)

Modern pop has no single drum pattern — it borrows. A 2026 pop production might combine a **trap-style sparse 808 kick** (on 1 and the "and-of-3"), an **R&B finger-snap on 2 and 4**, **trap-style hi-hat trills** at the bar transitions, and **clap layers** that add weight without conflicting with the snap. Tempo: **90–115 BPM**, with much of mainstream pop sitting around 95–105. The pop-programming convention is **layer rather than choose**: instead of one snare sound, three layered snare-adjacent samples (snap, clap, rim) all triggering simultaneously create a wider, more polished snare than any one sample. As [Native Instruments' drum patterns guide](https://blog.native-instruments.com/drum-patterns/) notes, modern pop drum programming is "more about layered textures and processing than pattern complexity." The Billie Eilish "Bad Guy" production captured in the [Sound on Sound Inside Track](https://www.soundonsound.com/techniques/inside-track-billie-eilish-bad-guy) is a textbook example: minimal pattern complexity, but the drum bus has aux groups for Kick, Main Snare, and Sub Bass, each layered and processed independently.

## Velocity layering for natural feel

A flat 127-velocity drum pattern sounds like a machine. Per [Mystic Alankar's drum programming guide](https://mysticalankar.com/blogs/blog/programming-rhythms-drums-that-fit-any-genre) and [Unison's hip-hop pattern tutorial](https://unison.audio/hip-hop-drum-pattern/), the natural-feel recipe is: **base velocity 75–90 for the main hits, ±5–10 random variation on every hit, accent pattern overlay on top**. A typical 8th-note hi-hat in rock: downbeat hats at velocity 95, the in-between hats at velocity 75, every fourth hat ghost-accented at 105 to mark the bar. A typical 16th-note hi-hat in trap: vary 60–115 across the bar with the loud accents on the trill peaks. For snares: backbeat at 100–115, ghost notes at 15–35. The principle is **dynamic range** — the difference between the loudest and softest hit in the pattern is what creates breath. If everything is between 90 and 100, the beat is stiff regardless of swing settings.

## Kick layering: depth without mud

Most professional drum programming layers two or three kick samples to get a sound that no single sample provides. The standard combination: **a "click" or "beater" kick** (transient-focused, 100–500 Hz emphasis) **plus a "body" kick** (sub-focused, 40–80 Hz fundamental) **plus optionally a "tail" kick** (long-decay 808 or sub-bass hit). The click provides definition that survives on small speakers; the body provides the impact on full-range systems. Per [Unison's drum layering guide](https://unison.audio/drum-layering/), the rule when layering is to **EQ-carve so the samples don't compete in the same frequency range** — high-pass the body kick at 100 Hz and low-pass the click kick at 200 Hz, or use a multiband approach. Phase alignment matters: if two kick samples land at slightly different times (even 1–2 ms), the low end will partially cancel and the kick will feel thinner than either sample alone.

## Programming order: kick first, then snare, then hat

The professional drum-programming workflow is almost universal: **kick first**, because it defines the genre and the tempo's foundation; **snare/clap second**, because the kick-snare relationship is the song's primary backbeat; **hi-hat third**, to fill the subdivision; **percussion overlays last**, as decoration. Per [Mystic Alankar's drum programming workflow](https://mysticalankar.com/blogs/blog/programming-rhythms-drums-that-fit-any-genre), this order isn't arbitrary — building from the bottom of the kit up means each layer references the established pulse rather than fighting it. Common mistake: programming a complex 16th-note hat pattern first, then trying to fit a kick around it. The result is usually a beat that loses its center. Lock the kick-and-snare backbone, audition it solo until it grooves on its own, *then* add hats and decoration. If the kick-and-snare alone doesn't make you nod, no amount of hi-hat complexity will save the pattern.

## Cited Retrieval Topics

- "how do i program house drums"
- "trap hi hat trill programming"
- "boom bap drum pattern kick snare"
- "uk garage 2 step swing percentage"
- "drum and bass 174 bpm pattern"
- "rock drum hi hat 8th note velocity"
- "modern pop drum layering"
- "techno drum pattern jeff mills"
- "what swing for hip hop drums"
- "kick layering for body and click"

## Sources

- [Native Instruments — 7 drum patterns every producer should know](https://blog.native-instruments.com/drum-patterns/)
- [Ben Rainey — Drum Programming for House Music](https://www.benrainey.co.uk/blog/drum-programming-house-music)
- [MusicRadar — How to program 6 different four-to-the-floor grooves](https://www.musicradar.com/how-to/how-to-program-6-different-four-to-the-floor-grooves)
- [Attack Magazine — Stripped Deep House (Beat Dissected)](https://www.attackmagazine.com/technique/beat-dissected/deep-house-stripped-workout-beat-dissected/)
- [Attack Magazine — Rolling Techno (Beat Dissected)](https://www.attackmagazine.com/technique/beat-dissected/rolling-techno/)
- [Attack Magazine — Jeff Mills "The Bells" Deconstructed](https://www.attackmagazine.com/technique/deconstructed/jeff-mills-the-bells/)
- [Attack Magazine — 90s Boom Bap Hip-Hop (Beat Dissected)](https://www.attackmagazine.com/technique/beat-dissected/90s-boom-bap-hip-hop/)
- [Attack Magazine — Rolling 2-Step Garage (Beat Dissected)](https://www.attackmagazine.com/technique/beat-dissected/rolling-2-step-garage/)
- [BVKER — Essential Boom Bap Drum Patterns](https://bvker.com/boom-bap-drum-patterns/)
- [MIDI Mighty — Three Boom Bap Drum Patterns](https://midimighty.com/blogs/resources/three-boom-bap-drum-patterns-audio-download)
- [Emastered — Trap Drum Patterns: The Ultimate Guide](https://emastered.com/blog/trap-drum-patterns)
- [MusicRadar — How to program mixed-resolution, trap-style hi-hat patterns](https://www.musicradar.com/how-to/how-to-program-mixed-resolution-trap-style-hi-hat-patterns)
- [Reason Studios — Trap Drum Basics: Super Neat Beat Cheat Sheet](https://www.reasonstudios.com/news/post/trap-drum-basics-super-neat-beat-cheat-sheet)
- [Studio Brootle — UK Garage Drum Pattern](https://www.studiobrootle.com/uk-garage-drum-pattern-with-presets-and-bassline/)
- [EDMProd — How to Make Jungle Music: The Complete Producer's Guide](https://www.edmprod.com/how-to-make-jungle-music/)
- [KAN Samples — Amen Break Sample Pack](https://kansamples.com/blogs/free-drum-and-bass-sample-packs/amen-break-tribute-pack-free-drum-bass-sample-pack-free-download)
- [Indie Band Guru — Essential Drum Grooves Every Indie Producer Should Know](https://indiebandguru.com/essential-drum-grooves-every-indie-producer-should-know/)
- [Zildjian — Lesson 10: 8th Note Rock Beats](https://ae.zildjian.com/education/beginner-drum-set-lessons/zildjian-drum-set-method-lesson-10/)
- [Mystic Alankar — Programming Rhythms: Drums That Fit Any Genre](https://mysticalankar.com/blogs/blog/programming-rhythms-drums-that-fit-any-genre)
- [Unison — How To Create The Perfect Hip Hop Drum Pattern](https://unison.audio/hip-hop-drum-pattern/)
- [Unison — Drum Layering 101](https://unison.audio/drum-layering/)
- [Sound on Sound — Inside Track: Billie Eilish 'Bad Guy'](https://www.soundonsound.com/techniques/inside-track-billie-eilish-bad-guy)
