# Preproduction and Demo Handoff

**Scope:** workflow
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Mixerman, *Zen and the Art of Producing*; Howard Massey, *Behind the Glass*; SOS Inside Track features (TMS LDN / Capaldi in corpus); Pro Audio Files and Production Expert workflow guides
**Tags:** `workflow`, `preproduction`, `methodology`, `demo`, `tracking`, `principle`

---

## Why preproduction is the highest-leverage stage

Every problem solved at the songwriting and arrangement desk costs an order of magnitude less than the same problem solved at the mix desk. Sound on Sound's preproduction overview is explicit on this: spending more time at the planning stage saves far more time downstream, and most "mix problems" are actually unmade preproduction decisions wearing a different hat [(SOS, Pre-production)](https://www.soundonsound.com/techniques/pre-production). Howard Massey's *Behind the Glass* interviews with top producers — originally Musician magazine's First Take series — converge on the same observation across 37 different producers: the producers who routinely deliver finished records on schedule are the ones who arrive at tracking with the song already decided, not the ones who plan to "find it in the studio" [(Behind the Glass, Internet Archive)](https://archive.org/details/behindglasstopre00mass). This document collects the concrete decisions, conventions, and handoff formats that turn that observation into a process.

## What to lock before tracking

Five elements must be locked before a single mic is hung. Each one is a decision that compounds; each one costs an order of magnitude more to revisit after tracking starts.

1. **Key** — verified against the artist's actual vocal range at performance volume. Range checks done at speaking volume routinely produce keys that the vocalist can't sustain over a full take.
2. **Tempo** — entered as a metronome BPM, with intentional tempo changes mapped explicitly. Tracking studios' preproduction guidance is direct on this point: even a couple BPM can change the song's feel, and tempo is the cheapest thing to decide and the most expensive thing to revisit [(Island Recording Studios)](https://www.islandrecordingstudios.com/post/recording-prep-checklist).
3. **Arrangement and song length** — bar counts named for every section, intro/outro length decided, total runtime within ~20 seconds of target. "Knowing how many bars the intro is, the order of the verses, choruses and bridges, how the song finishes" is on essentially every preproduction checklist published by working studios [(2201 Recording)](https://www.2201.co.uk/blog-1/music-producers-pre-recording-checklist).
4. **References** — 2–4 commercial records that define tone, density, and arrangement. References are a vocabulary, not a target.
5. **Instrumentation** — every part on the track named, with performers booked and parts charted where appropriate.

The simplest test for preproduction completeness: can the producer write down the song's structure on a single index card without consulting the DAW? If not, preproduction isn't finished.

## The demo's structural role

A demo is not a rough version of the final record; it is a structural blueprint that the final record will reference. Producer Mikko Gordon's Tape Op interview frames the distinction: the demo's job is to establish aesthetic direction before tracking starts, so that "there should be a sense of the direction the production is going in, from the very first moment people start making sounds" [(Tape Op #157)](https://tapeop.com/interviews/157/mikko-gordon). A well-built demo settles arrangement, tempo, key, instrumentation, and tonal references. A poorly-built demo establishes none of these and forces tracking to do the work — which is what produces the 30-tracks-of-drums sessions Gordon describes [(Tape Op #157)](https://tapeop.com/interviews/157/mikko-gordon).

## What survives the demo-to-final transition

The empirical pattern across published producer interviews and writeups: the elements that survive from demo to final are the ones that establish identity, not the ones that establish quality. The conventions:

- **Songwriting and arrangement** almost always survive. If the chord progression, melody, lyric, and section order are working in the demo, they shouldn't change at tracking.
- **Tempo and key** survive almost always, occasionally adjusted by a half-step or a few BPM.
- **Scratch/demo vocals** are usually re-tracked, but exceptions are common enough to be worth taking seriously. The Killers kept Brandon Flowers' scratch vocals on roughly half of *Day & Age* because re-tracking lost the energy, and "Superstar" by the Carpenters used the original scratch vocal in the final master [(Wikipedia, Scratch vocal)](https://en.wikipedia.org/wiki/Scratch_vocal). Always record scratch vocals well enough that they could survive — through a real mic, into a clean preamp, with usable headphone monitoring.
- **Demo drums and demo synths** usually get re-tracked or replaced, but the parts they played survive — the drummer plays what the programmed kit established, the keyboard player voices what the demo synth voiced.
- **Vibe and energy** survive in the form of a reference rough mix that the tracking team listens back to before takes. The first rough is the record at its most honest; subsequent versions tend to chase polish at the expense of energy [(Sweetwater on rough mixes)](https://www.sweetwater.com/insync/rough-mix/).

The decision discipline: before retracking any element, the producer should be able to say what the retracked version will gain that the demo version doesn't already have. "Better quality" is not an answer; "tighter time" or "different harmonic density" or "real-room ambience" is.

## The "rough mix first" rule

The discipline of building a rough mix during tracking — not after — is recommended consistently by tracking-studio engineers. The Production Expert workflow habits article phrases the principle bluntly: comp, fade, and balance during tracking so playback sounds good the next time the session opens [(Production Expert)](https://www.production-expert.com/production-expert-1/the-workflow-habits-every-audio-engineer-should-master). The corollary from Sweetwater's rough-mix entry: the rough mix is shared, listened to, and heard by people who will form opinions about the song based on it — leaving a tracking day with a rough mix the producer isn't proud of is a mistake [(Sweetwater)](https://www.sweetwater.com/insync/rough-mix/). The rough should pass through the full mix bus, include all stems at workable balance, and be exported at the end of each tracking day with a date in the filename.

## Stem hand-off conventions: format

When a track is heading to a mix engineer, the stems must conform to format conventions the engineer can rely on. The consensus across producer-prep guides:

- **Format:** 24-bit WAV at the session's sample rate (44.1 or 48 kHz typical, 96 kHz if the session was tracked there). Lossy formats are unacceptable [(Tyler Gunz)](https://www.tylergunz.com/new-blog/2017/11/18/submitting-stems-to-your-mixing-engineer).
- **Start point:** every stem starts at bar 1, regardless of when the source track has audio. This guarantees alignment when the mix engineer imports.
- **Length:** every stem is the same length as every other stem. Pad with silence as needed.
- **Headroom:** no clipping anywhere in the chain. Pull individual track faders down if necessary; do not rely on master-fader attenuation to fix pre-fader clipping [(Pro Audio Files)](https://theproaudiofiles.com/preparing-files-for-a-mix-engineer/).
- **Master-bus processing:** removed before bounce. The mix engineer needs the raw stems, not the producer's master-bus chain [(Tyler Gunz)](https://www.tylergunz.com/new-blog/2017/11/18/submitting-stems-to-your-mixing-engineer).
- **Naming:** descriptive (Kick, Snare-Top, Vox-Lead, Synth-Bass), not creative (MEGA-OOTS, GoodOne-3). The Pro Audio Files header format `artist_track_120BPM_STEM` is one widely-used convention [(Pro Audio Files)](https://theproaudiofiles.com/preparing-files-for-a-mix-engineer/).

The Gearspace consensus naming pattern for film/TV work — `ShowID_Identifier_Channels_Date_versionNN` — is the formal version of the same idea, with version numbers incrementing on every redelivery [(Gearspace, Printmaster/Stems naming)](https://gearspace.com/board/post-production-forum/1014111-printmaster-stems-naming-convention.html).

## Stem hand-off conventions: what to include

A complete hand-off package, by working-engineer convention, includes more than the stems themselves:

- **The stems**, in a single zipped folder named for the project and version.
- **A reference rough mix** as a stereo bounce — the version the producer wants the mix engineer to use as the emotional and tonal compass [(Tyler Gunz)](https://www.tylergunz.com/new-blog/2017/11/18/submitting-stems-to-your-mixing-engineer).
- **Notes** in a plain-text or PDF file: tempo, key, sample rate, intended deliverable format, any sections that need attention, anything unusual (e.g., a delay throw the producer wants preserved, an intentional clip, a vocal moment that must read).
- **Reference tracks** (commercial records) named in the notes — not bounced into the package, just identified by artist and track title.
- **DAW session file** as backup, if the mix engineer uses the same DAW. The stems remain the primary deliverable.

The "compress to .zip before sending" rule is small but matters: it cuts transfer size and prevents Finder/Explorer file-reordering on the recipient's machine [(Tyler Gunz)](https://www.tylergunz.com/new-blog/2017/11/18/submitting-stems-to-your-mixing-engineer).

## Session-prep checklist for the producer

The producer's pre-handoff checklist, drawn from working-engineer guidance:

1. Delete unused or muted tracks.
2. Rename every track from generic labels (Audio-12, Inst-3) to source-specific names (Kick-In, Vox-Lead, Pad-Wide).
3. Verify start and end points across all stems.
4. Clean audio artifacts — clicks, breaths if not wanted, unintended silence.
5. Confirm no clipping anywhere, especially on the master bus.
6. Group multi-mic sources (drums, guitar amps, layered vocals) into clearly-named folders.
7. Bounce dry stems and wet stems if both are wanted; keep them in separate folders.
8. Render a reference rough mix as a stereo file.
9. Compile session notes with tempo, key, references, and special instructions.
10. Zip the whole package and version-number it [(Pro Audio Files)](https://theproaudiofiles.com/preparing-files-for-a-mix-engineer/).

Items 1, 2, and 5 are the most commonly skipped — and they are the most expensive when skipped, because the mix engineer's first hour gets spent on them instead of on mixing.

## Artist-vs-producer role separation

Modern preproduction blurs the historical separation between artist, songwriter, and producer — particularly in pop and hip-hop, where the producer is often in the room from the first idea. The Audiospring breakdown of roles makes the practical distinction: the songwriter crafts the song into existence (structure, melody, chords, lyric), and the producer enhances, arranges, edits, and directs the recording toward a polished outcome [(Audiospring)](https://audiospringmusic.com/the-roles-of-songwriter-vs-producer-in-making-songs/). When the same person plays both roles, the discipline that protects the work is mode-switching: songwriting mode is open and exploratory, producer mode is decisive and structural. Mixerman's framing — producing is decision management — applies most acutely to the producer-side decisions an artist-producer is making on their own behalf, where the lack of a second voice in the room amplifies both perfectionism and avoidance [(Tape Op review)](https://tapeop.com/reviews/gear/93/zen-and-the-art-of-producing-book).

## The TMS LDN model: starters as preproduction artifacts

The Sound on Sound Inside Track feature on Lewis Capaldi's "Someone You Loved" is one of the most concrete preproduction case studies in print. TMS LDN — the production trio behind the track — works on a five-day cycle split into three writing days and two production days, with different two-person configurations each week. They create 15-second musical "starters" — keyboard parts, drum sketches, vocal ideas — and present a portfolio of these to the visiting artist [(SOS, Capaldi Inside Track)](https://www.soundonsound.com/techniques/inside-track-lewis-capaldis-someone-you-loved). The methodological insight: the starter is a preproduction artifact that gives the artist options without committing them to a fully-built backing track. It balances preparation (the team has done work) with spontaneity (the artist doesn't walk into a finished song). The writing room itself is designed to support the mode — a living-room layout, no vocal booth, lyrics on a projector screen so everyone is working from the same surface [(SOS)](https://www.soundonsound.com/techniques/inside-track-lewis-capaldis-someone-you-loved).

## The "tracking sheet" as preproduction artifact

A tracking sheet is the in-session document that captures every take, comp, and decision during recording. Standard fields: song name, take number, performer, mic, signal path, time-of-day, producer notes ("V2 — keeper, comp in for chorus"). The discipline is administrative — tracking sheets exist so the producer in three months can identify which take is on which track, and so the mix engineer can be told "use take 4 of the bridge vocal" without ambiguity. Pro audio guidance treats this as part of the session-prep package: the tracking sheet stays with the session files, and a summary travels with the stems to the mix engineer.

## When the demo becomes the master

Producers occasionally discover that the demo version is the version. The pattern across published cases — Brandon Flowers' Day & Age scratch vocals, "Superstar" by the Carpenters, Mick Jagger demos that became finals — is that the demo had energy and intention that the retracked version couldn't recapture [(Wikipedia, Scratch vocal)](https://en.wikipedia.org/wiki/Scratch_vocal). The practical implication for preproduction: track every demo through good enough signal chain that the demo could survive. A demo vocal cut through a USB interface and a $50 mic into a noisy preamp can't be promoted to master no matter how good the performance. A demo vocal cut through a real preamp into a quiet 24-bit converter can be. The cost of treating demos like real takes is small; the cost of having to retrack a magic performance is large.

## What to send the mix engineer, restated

The single message to send to a mix engineer alongside stems should answer five questions: what is the song's tempo and key, what are the references, what is the intended delivery format, what is the deadline, and what does the producer want the mix engineer to know that isn't audible in the stems. Everything else can be inferred from a well-named stem package and a reference rough. The mix engineer's job is to mix; the producer's job is to make that job tractable. The Production Expert workflow rule applies: another engineer should be able to open the package and understand the project without a phone call [(Production Expert)](https://www.production-expert.com/production-expert-1/the-workflow-habits-every-audio-engineer-should-master).

## How preproduction discipline pays back

The producers profiled across Massey's *Behind the Glass* converge on a consistent observation: the records that finish well are the records whose preproduction was complete. The mechanism is structural, not motivational — preproduction decisions are the cheapest decisions in the project, and deferring them just makes them more expensive without making them better. A producer who locks key, tempo, arrangement, references, and instrumentation before tracking, who builds a structurally-honest demo, who runs a rough mix in parallel with recording, and who hands off stems in conventional format with conventional notes, has spent perhaps two days on preproduction and saved a week of mixing. The leverage is empirical and reproducible — which is why the same conventions appear, in slightly different language, in essentially every working-producer source.

## Cited Retrieval Topics

- "what should i lock before tracking"
- "how do i prepare stems for a mix engineer"
- "what survives from a demo to the final record"
- "should i retrack a scratch vocal"
- "what goes in a rough mix during tracking"
- "what's the difference between an artist and a producer"
- "how do i name and version stems for handoff"
- "what's the tms starters approach"
- "do i need to remove master bus processing before sending stems"
- "what format do mix engineers want stems in"

## Sources

- [Sound on Sound — Pre-production](https://www.soundonsound.com/techniques/pre-production)
- [Sound on Sound Inside Track — Lewis Capaldi "Someone You Loved"](https://www.soundonsound.com/techniques/inside-track-lewis-capaldis-someone-you-loved)
- [Tape Op #157 — Mikko Gordon interview](https://tapeop.com/interviews/157/mikko-gordon)
- [Tape Op — Zen and the Art of Producing review](https://tapeop.com/reviews/gear/93/zen-and-the-art-of-producing-book)
- [Howard Massey, Behind the Glass — Internet Archive](https://archive.org/details/behindglasstopre00mass)
- [Sweetwater InSync — Rough Mix](https://www.sweetwater.com/insync/rough-mix/)
- [Production Expert — Workflow Habits Every Audio Engineer Should Master](https://www.production-expert.com/production-expert-1/the-workflow-habits-every-audio-engineer-should-master)
- [Pro Audio Files — Preparing Files for a Mix Engineer](https://theproaudiofiles.com/preparing-files-for-a-mix-engineer/)
- [Tyler Gunz — Submitting Stems to Your Mixing Engineer](https://www.tylergunz.com/new-blog/2017/11/18/submitting-stems-to-your-mixing-engineer)
- [Gearspace — Printmaster/Stems Naming Convention](https://gearspace.com/board/post-production-forum/1014111-printmaster-stems-naming-convention.html)
- [Island Recording Studios — Recording Prep Checklist](https://www.islandrecordingstudios.com/post/recording-prep-checklist)
- [2201 Recording — Music Producers Pre-Recording Checklist](https://www.2201.co.uk/blog-1/music-producers-pre-recording-checklist)
- [Audiospring — The Roles of Songwriter vs Producer](https://audiospringmusic.com/the-roles-of-songwriter-vs-producer-in-making-songs/)
- [Wikipedia — Scratch vocal](https://en.wikipedia.org/wiki/Scratch_vocal)
