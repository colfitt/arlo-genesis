# Hacker Sample Crate — sources, triage, and The Terminal family

The 40-source crate (movie/TV/game hacker sounds + real computer/telecom sounds),
collected for two jobs: **sampler fodder for the music rig** (Octatrack/Digitakt/
looping) and **reference material for a Terminal sound family** — which may be the
most on-brand family this harness could ship: an AI agent that sounds like the
machines it descends from.

## License triage — three lanes, decided per file at download time

| Lane | What goes in it | Where it may live |
|---|---|---|
| **Shippable** | Sonniss GDC bundles (royalty-free, commercial OK), YouTube Audio Library, DTMF/Morse/POST beeps and anything else we synthesize or record ourselves (Model M keyboard, our own CRT, our own floppy drive) | Anywhere — repo, product, release builds |
| **In-house reference** | BBC Sound Effects (free tier = personal/education/research only), movie/TV clips from YouTube, The Sounds Resource / 101Soundboards game rips (GoldenEye, MGS, Deus Ex, Half-Life, System Shock, Watch Dogs), Win95 startup, Mac chime, ICQ/AOL/AIM sounds | Local folders and the music rig only. **Never committed** — this repo is on GitHub, so a commit is distribution |
| **Recreate-first** | Anything from lane 2 we want in the product: rebuild the *gesture* from scratch (the §114(b) rule — method doesn't matter, recognizability does; famous voices like AOL's are also a publicity-rights issue) | Graduates to lane 1 once rebuilt |

Keep `sources.md` next to every downloaded file: filename, URL, license, lane.

## The crate (as collected)

**Movie / TV / game:** WarGames WOPR · Matrix phone-trace · Hackers (1995) UI ·
Sneakers terminals · Jurassic Park UNIX scene · Mission: Impossible security UI ·
GoldenEye 007 (186-file archive) · MGS Codec (1,714-file archive) · Deus Ex
Interface pack · Half-Life HEV assistant · Portal turrets/GLaDOS · System Shock
SHODAN · Watch Dogs CTOS · Mr. Robot (keyboard/room texture, not bleeps) · TRON
Legacy UI · Star Trek LCARS · Alien Mother/Nostromo · Blade Runner Esper machine ·
Terminator HUD · RoboCop targeting · KITT scanner.

**Real computer / telecom (the concentrate-here pile):** 56k handshake · DTMF ·
busy/off-hook tones · dot-matrix printer · floppy seek · old HDD seeking · IBM
Model M · CRT degauss · BIOS POST beeps · Win95 startup · classic Mac chimes ·
ICQ "Uh-oh!" · AOL "You've Got Mail" · AIM/MSN/Yahoo sounds · numbers stations ·
Morse · shortwave tuning · scanner squelch · digital radio bursts.

**Libraries:** Sonniss GDC archive (≈7.5 GB/year, shippable) · BBC Sound Effects
(33k recordings, in-house lane) · YouTube Audio Library (shippable).

**First 12 for the sampler:** MGS Codec → dial-up handshake → DTMF → GoldenEye UI →
Deus Ex UI → Half-Life HEV → KITT scanner → dot-matrix printer → CRT degauss →
AOL voice → numbers station → radio squelch.

## The Terminal — family concept

Why it wins: the crate's best material (DTMF, modem handshake, Morse, POST beeps,
squelch) is **trivially synthesizable from first principles** — DTMF is literally two
sine waves — so the whole family can be lane-1 original and still drip with the
aesthetic. The rips stay in-house as references; the family ships.

| Cue | Concept | Source lane |
|---|---|---|
| ping | single DTMF chirp | synthesize (two sines) |
| mention | codec-style double beep-beep | synthesize (gesture only, not the MGS recording) |
| message-in | teletype/RTTY micro-burst | synthesize |
| message-out | Morse dit-dah tail | synthesize |
| question | off-hook "intercept" rising double tone | synthesize |
| done | clean POST beep resolving down to D | synthesize |
| done-big | full modem handshake miniature ending in the connect chord | synthesize |
| error | squelch burst + low buzz | synthesize |
| warning | busy-signal single cycle | synthesize |
| start | dial tone + first DTMF digit | synthesize |
| progress | one Morse dit / HDD seek tick | synthesize or record own drive |
| connect | handshake chirps → carrier lock | synthesize |
| disconnect | carrier drop + click | synthesize |
| approve | two ascending DTMF digits | synthesize |
| deny | number-unobtainable falling tone | synthesize |
| published | dot-matrix line feed *zip-ding* | record a real printer (lane 1 if it's ours) |
| signed-off | fax confirmation chirp | synthesize |
| phase-advance | three ascending POST beeps | synthesize |
| space-complete | CRT power-off *bwoop* + degauss ghost | record our own CRT |
| fireworks | numbers-station voice fragment + shortwave burst + carrier bloom | record own voice + synthesis |

Six teaser cues are prototyped in `prototypes/terminal-*.wav` — pure synthesis,
lane 1, audible on the audition page.

## Music-rig notes

For the looping rig, the crate wants different processing than the harness: run the
rhythmic machinery (dot-matrix, HDD seeks, Model M) into the Digitakt as one-shots;
KITT scanner and numbers stations into Blooper/Microcosm as pads; DTMF and Morse
through Generation Loss for instant hauntology. Same folders, two destinies.
