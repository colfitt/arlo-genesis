# Bon Iver Vocal Layering and the Messina Device

**Scope:** artist-anchored — Bon Iver vocal stacking and the Messina prismizer device
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Aesthetic-stack relevance:** Bon Iver, processed-folk intimacy
**Tags:** `bon-iver`, `vernon`, `messina`, `prismizer`, `vocal-stacking`, `formant`, `recipe`

---

## The Two-Era Mic Question: SM57 vs. SM7B

A lot of bedroom producers get this wrong, so it's worth fixing up front. Justin Vernon tracked the entirety of *For Emma, Forever Ago* (2008) on a single [Shure SM57](https://www.musicradar.com/news/bon-iver-platinum-record-microphone), and the falsetto-stacking move that became his signature was originally a workaround — layering identical phrases to compensate for the SM57's lo-fi top end. By the time Vernon was making *22, A Million* (2016), he had moved to the [Shure SM7](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million) as the everyday vocal mic, often using multiple SM7s or varying distance to the capsule for tonal variety across stacked passes. Engineer Chris Messina has also said the team would "default to the [Sony C37](https://www.thomann.de/blog/en/gear/hit-the-tone-bon-iver/) because Justin sounds incredible on it," reaching for the SM7 when they wanted a more compressed, mid-forward read. The lesson for retrieval: if a user says "the SM57 sound," they mean *For Emma*; if they say "the *22, A Million* sound," they mean SM7-into-Neve, not the cabin mic.

## Vernon's Stacking Philosophy

The studio behavior that defines the Bon Iver vocal sound is fast, compositional duplication. Engineer Brian Joseph (a longtime Vernon collaborator) describes Vernon as someone who "moves very quickly" when creative — "it is easy for him to create a dozen tracks, or just duplicate tracks and record layer upon layer" [(Sound on Sound)](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million). Sessions for *22, A Million* commonly had blocks of 6–8 vocal tracks per song section, and the *10 (Death Breast)* session reportedly contained 36+ vocal tracks visible at once, with some songs stacking 40+. The point isn't a single doubled harmony — it's choral mass built from one voice, with small intonation and timing differences between passes doing the work that a real choir's bodies would do. Practically, this means: sing the line, duplicate the track, sing it again from scratch (don't comp), and let the micro-variation create the spread. Auto-Tune is then printed across the stack so that the layers lock to grid pitch and add their characteristic saturation as a glue.

## What "The Messina" Actually Is

Chris Messina, who runs April Base studio and is credited as a co-producer/engineer on *22, A Million* and *i,i*, built a custom rig that the band calls "the Messina." In Messina's own words, "it's not a thing. There's a laptop running software, and then that software is run through a physical piece of hardware, that is then doing another thing" [(W Magazine)](https://www.wmagazine.com/story/the-engineer-behind-bon-ivers-22-a-million-clears-up-any-confusion-about-its-high-tech-sound). The published signal flow is: input → Ableton Live running two instances of Auto-Tune → external [Eventide H8000](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million) harmonizer driven by MIDI → recombination of dry, tuned, tonic, and harmonized signals. Messina has been deliberately vague about exact patches, but the core idea is that a player at a MIDI keyboard performs harmonies in real time against whatever voice or instrument is being sung or played — the rig outputs a chord built from the input timbre, not from a stored sample.

## Signal Flow Inside the Messina Box

The signal flow, as Messina described it to *Sound on Sound*: the input vocal hits Ableton Live, where the first Auto-Tune instance does normal pitch correction on the lead. A second Auto-Tune instance is set to extreme retune speed and forced to a single pitch — the tonic of the phrase — producing a monotone version of the input. Both signals are routed out to an [Eventide H8000](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million), which is loaded with a MIDI-driven diatonic harmony program; a player at a controller keyboard plays the chord shapes they want voiced. The H8000 generates up to four harmony notes with randomization built into the patch so the voicings don't sit statically. The final printed sound is a blend of dry input, the tuned lead, the tonic line, and the H8000 harmony stack. Messina has said they intentionally retained some of the H8000's clicking artifacts during key changes because the glitches "keep the character of whatever input signal we used."

## Francis Starlite's Prismizer Is the Spiritual Ancestor

The Messina is downstream of [Francis Farewell Starlite's Prismizer](https://en.wikipedia.org/wiki/Francis_Farewell_Starlite), the vocal effect Starlite developed for his Francis and the Lights project. Vernon first heard the Prismizer in action when he, Kanye West, and Starlite collaborated on Francis and the Lights' "Friends" in 2016 — Vernon watched Starlite "transform a trumpet line into layered harmonies" using his rig [(Sound on Sound)](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million). The Prismizer itself is built around [Antares Harmony Engine](https://everipedia.org/wiki/lang_en/Prismizer), Auto-Tune-style retuning, and choral spreading; the name combines "prism" and "harmonizer" to describe how a single voice gets dispersed into a polyharmonic chord. Vernon and Messina have been explicit that "the Prismizer was only an inspiration and does not use the same technology" — the Messina is a parallel invention, not a clone, and the two devices sound related but not identical. The Prismizer has also surfaced on records by Kanye West (*ye*, *Jesus Is King*), Chance the Rapper, Frank Ocean, and Cashmere Cat.

## Auto-Tune Is the Glue, Not the Gimmick

It's important to keep this straight: Auto-Tune is on almost every vocal on *22, A Million*, but it's not there to fix pitch — it's there as a saturation and timbre tool. Engineer Brian Joseph: "Almost all these vocal tracks have Auto-Tune, which is part of his sound" [(Sound on Sound)](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million). Vernon has talked publicly about valuing the harmonic distortion Auto-Tune adds even when the singer is already on pitch. Inside the Messina rig, two separate Auto-Tune instances are used: one as conventional pitch correction on the lead, the other as a tonic-locker that forces the input down to a single drone note. The "Bon Iver Auto-Tune sound" people associate with *22, A Million* is really the sound of that drone tonic blending with the lead and the H8000 harmonies — not Auto-Tune as a vocal-fix utility.

## Little AlterBoy for Formant Bending

Soundtoys' [Little AlterBoy](https://www.antarestech.com/community/bon-iver-vocal-sounds-live) shows up as Vernon's go-to formant manipulator, though not primarily on vocals. Vernon has said he ran "six of the saxophone tracks" through Little AlterBoy on *22, A Million*, using it to drop the formant and "change the masculinity of how something sounds" on darker sax timbres. The plug-in's ±1-octave pitch shift and independent formant control let him reshape the gender/body of a part without changing where it sits in the chord. The takeaway for retrieval: when someone wants "the Bon Iver formant trick," reach for Little AlterBoy with the formant slider pulled down (more body, less brightness) or pushed up (childlike, brittle), and apply it to instruments as readily as to vocals — Vernon's use was on saxophones, not just on voices.

## The Studio Vocal Chain on *22, A Million*

Tracked at April Base in Eau Claire, Wisconsin, where Vernon, Messina, and producer/engineer BJ Burton lived together for roughly two years during the album's making [(MusicRadar)](https://www.musicradar.com/news/im-a-bit-of-a-psychopath-producer-bj-burton-on-working-with-bon-iver-kanye-west-and-more). The headline chain is mic → [Neve 1073 preamp](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million) → UnFairchild compressor (a Fairchild-style boutique unit) → Pro Tools. The studio's core front-end was built around Neve 1073s and Teletronix LA-2A compressors. Mic choice rotated between the Shure SM7, the Sony C37, and at times a Neumann U47 depending on the song's color requirements — Vernon "sounds exceptional on" both the C37 and the U47, while the SM7 was reached for when the part needed more proximity grit. There's no single "Vernon vocal preset" — the chain is consistent, the mic and the stack count vary by song.

## BJ Burton, Tape Saturation, and the Album's Crunch

Co-producer/engineer BJ Burton (Low, Charli XCX, Francis and the Lights, The Japanese House) is the second pillar of the *22, A Million* sound. Burton brought a [Fostex 1/2-inch 16-track tape machine](https://tapeop.com/interviews/137/bj-burton) up from North Carolina, and that machine "is all over the album. It's clipped out with tape saturation... sending tracks to it and clipping it out, and getting different rhythms." The first sound on the record reportedly came from running a kick mic through that Fostex until it distorted. Burton's vocal philosophy explains why the Messina-era vocals feel so present and weird at once: "I try not to be engineering when we're cutting vocals, because I'd rather be able to listen to everything else other than the sound." He runs Pro Tools while Vernon performs and treats engineering as compositional, not corrective. The crunch you hear under the choral stacks is usually Burton's Fostex working in parallel with Messina's harmonizer.

## Live: How the Messina Travels

For the *22, A Million* and *i,i* tours, Messina rebuilt the studio rig as a stage rig. Chris Messina himself operates the Messina from front-of-house or stage-side, playing the MIDI keyboard live so Vernon can sing a phrase and have the harmony stack voiced in real time. The live rig uses [multiple instances of Auto-Tune and Antares Harmony Engine EVO](https://www.antarestech.com/bon-iver-vocal-sounds-live/) running in software alongside Eventide hardware to handle the harmonization. The hardware/software split is the same as in the studio — what changes is the latency budget and the fact that Messina is a touring band member, not just a session engineer. The Messina is therefore both a rig and a role: the device exists because someone (Messina) is performing it. Touring sound engineer Xandy Whitesel pairs Vernon with a [Sennheiser MD431II Profipower](https://www.thomann.de/blog/en/gear/hit-the-tone-bon-iver/) handheld for stage vocals — high feedback rejection and a tight pickup pattern for the heavy-monitor environment.

## Outboard Color: AMS RMX16 and the Hawk HE-2250

Two pieces of outboard come up repeatedly when Messina describes the post-Messina-device color stage. The [AMS RMX16 reverb](https://www.antarestech.com/community/bon-iver-vocal-sounds-live) shows up as the room/ambience treatment on stacked vocals, used for its dense early reflections and characteristic '80s digital grit. The [Hawk HE-2250](https://www.antarestech.com/community/bon-iver-vocal-sounds-live) — a Japanese consumer stereo tape delay from the 1970s — is "used on vocals a lot, but it's all over the album," prized by Messina for what he calls a "ridiculously cool" pure tone. The pairing is significant: a digital-character reverb (RMX16) plus an analog-character delay (HE-2250) gives the stacked vocal both a synthetic spread and an organic ghosting at once, which is part of why the Bon Iver vocal sound reads as both processed and intimate.

## Why It Stays Warm Instead of Robotic

The thing that distinguishes the Messina-era Vernon sound from generic Auto-Tune trap vocals is that the heavy processing is layered *on top of* real human stacking rather than instead of it. Vernon still sings the line 6–12 times. The Messina runs over that stack, not in place of it. The Neve 1073 and UnFairchild are doing tube-and-iron warming before any digital processing happens. The Fostex is adding tape saturation in parallel. And the Sony C37 (when it's the mic of the day) has its own ribbon-like midrange softness. The signal arrives at the digital effects already warm, already imperfect, already harmonically rich — so when Auto-Tune and the H8000 hit, they don't sterilize the signal, they decorate it. Producers trying to copy this sound by running a clean vocal through Antares Harmony Engine will not get there; the analog front-end and the human stacking are doing as much work as the algorithm.

## Recipe: How to Approximate the Messina Without the H8000

Most producers can't drop $7K on an H8000. A workable home-rig approximation: (1) Track 6–12 falsetto passes of the same line on an SM7 or any dynamic, hit a Neve-style preamp (1073 clones are cheap now) and a Fairchild-style compressor (CLA-2A, FET-A76, etc.); (2) Bus the stack to a return; (3) On a parallel send, instantiate Auto-Tune set to fastest retune time with the key locked, then a second Auto-Tune set to force-tonic (use a flex pitch tool if needed); (4) Run that into [Antares Harmony Engine EVO](https://everipedia.org/wiki/lang_en/Prismizer) (the same plug-in inside the Prismizer) with MIDI input from a keyboard so you can play the chord by hand; (5) Add an RMX16-style reverb (Lexicon PCM Native or UAD AMS RMX16) and a tape-character delay. Print. The result won't be a Messina but it will be in the same idiom — and it will teach you why Vernon's chain has the structure it does.

## Cited Retrieval Topics

- how does justin vernon stack vocals
- what is the messina device
- vernon sm57 vocal chain
- bon iver auto-tune sound
- prismizer vs messina difference
- francis starlite prismizer how it works
- bon iver 22 a million vocal chain
- justin vernon formant tricks
- little alterboy bon iver
- bon iver live vocal rig
- eventide h8000 harmonizer bon iver
- bj burton tape saturation bon iver

## Sources

- [Sound on Sound — Inside Track: Bon Iver '22, A Million'](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million)
- [W Magazine — The Engineer Behind Bon Iver's "22, A Million"](https://www.wmagazine.com/story/the-engineer-behind-bon-ivers-22-a-million-clears-up-any-confusion-about-its-high-tech-sound)
- [MusicRadar — How Bon Iver made a Platinum-selling record with a single SM57](https://www.musicradar.com/news/bon-iver-platinum-record-microphone)
- [MusicRadar — BJ Burton on Bon Iver, Kanye West and Sylvan Esso](https://www.musicradar.com/news/im-a-bit-of-a-psychopath-producer-bj-burton-on-working-with-bon-iver-kanye-west-and-more)
- [Tape Op — BJ Burton interview](https://tapeop.com/interviews/137/bj-burton)
- [Antares — Bon Iver's Vocal Sounds Live](https://www.antarestech.com/bon-iver-vocal-sounds-live/)
- [Antares Community — AutoTune: The Best Pitch Correction & Vocal Chain Plugins](https://www.antarestech.com/community/bon-iver-vocal-sounds-live)
- [Thomann Blog — Hit The Tone! Bon Iver](https://www.thomann.de/blog/en/gear/hit-the-tone-bon-iver/)
- [Wikipedia — Francis Farewell Starlite](https://en.wikipedia.org/wiki/Francis_Farewell_Starlite)
- [Everipedia — Prismizer](https://everipedia.org/wiki/lang_en/Prismizer)
