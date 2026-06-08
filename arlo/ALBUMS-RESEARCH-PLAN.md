# ARLO Albums Research Plan

A separate expansion pass covering **89 canonical albums** as album-anchored chunks. Distinct from `AESTHETIC-RESEARCH-PLAN.md` (which was aesthetic-curated artist anchors). User framing: *"not all of them have my music tastes to what I want to make"* — this is a **musical-vocabulary research pass**, not a "do-this-style" pass. ARLO ends up knowing how *Paul's Boutique* is constructed without claiming the user wants to sound like the Dust Brothers.

User explicit: *"there is no limit to anchors"* and *"this research pass may take a few days."*

---

## Design decision: album-anchored, not artist-anchored

For this list specifically, files are organized **per album**, not per artist. Three reasons:

1. **The production story IS the album.** *Loveless*, *Bitches Brew*, *Kid A*, *Paul's Boutique*, *Remain in Light* are studied as discrete production artifacts. Sound on Sound's *Classic Tracks* series, Tape Op, and most engineer interviews are organized this way. Forcing them into an artist-level "Beatles overview" loses the *White Album* (chaos / faction-split / minimal-engineer) vs. *Abbey Road* (Geoff Emerick / 8-track / focused) distinction.
2. **Multi-album entries demand it.** Bowie ×2, LCD ×2, Charli ×2, Beatles ×2, Stooges ×2, Pink Floyd ×2, Outkast ×2, VU ×2, Misfits ×2, Tom Waits ×3, Dylan ×4, Swans ×2, Radiohead ×2. The Dylan jump from *Freewheelin'* (1963) to *Highway 61 Revisited* (1965) is the canonical *same-artist-different-production-world* case.
3. **Scales without ceremony.** Adding album #150 later doesn't require renaming or restructuring.

### Updated folder structure

```
corpus/
├── artists/         (existing — artist career overviews + philosophy + lineage)
├── albums/          ← new — per-album production deep-dives
└── techniques/      (existing — technique-anchored chunks)
```

Existing artist files in `corpus/artists/` stay as **overview** files. New album files in `corpus/albums/` carry the production-detail work. A reader of `bon-iver-vocal-layering-messina.md` (artist) is learning Vernon's stacking philosophy; a reader of `albums/bon-iver-22-a-million.md` (hypothetical, doesn't exist yet) is learning the specific 2016 session details. They cross-reference via tags.

### File naming convention

`corpus/albums/{artist-slug}-{album-slug}.md`. Example: `corpus/albums/talking-heads-remain-in-light.md`, `corpus/albums/my-bloody-valentine-loveless.md`.

---

## Duplicate resolution — 11 albums overlap with existing anchors

These don't get *new* artist anchors. They get album files that cross-link to the existing artist anchor.

| Album | Existing artist anchor | Resolution |
|---|---|---|
| Bowie — *Ziggy Stardust* (1972) | #24 Bowie (Berlin Trilogy focus) | New album file; cross-link |
| Bowie — *Station to Station* (1976) | #24 Bowie (Berlin Trilogy focus) | New album file; cross-link |
| LCD — *Sound of Silver* (2007) | #2 LCD Soundsystem | New album file; cross-link |
| LCD — *This Is Happening* (2010) | #2 LCD Soundsystem | New album file; cross-link |
| Charli XCX — *Charli* (2019) | #3 Charli XCX | New album file; cross-link |
| Charli XCX — *BRAT* (2024) | #3 Charli XCX + proposed prompt #7 | **Reroute:** the prompt #7 (`charli-xcx-brat-production`) becomes the album file `albums/charli-xcx-brat.md`. Don't write both. |
| Radiohead — *OK Computer* (1997) | #8 Radiohead | New album file; cross-link |
| Radiohead — *Kid A* (2000) | #8 Radiohead + proposed prompt #24 | **Reroute:** the prompt #24 (`radiohead-kid-a-production`) becomes `albums/radiohead-kid-a.md` |
| Postal Service — *Give Up* (2003) | #14 Postal Service + proposed prompt #33 | **Reroute:** prompt #33 becomes `albums/postal-service-give-up.md` |
| NMH — *Aeroplane Over the Sea* (1998) | #23 NMH + proposed prompt #43 | **Reroute:** prompt #43 becomes `albums/neutral-milk-hotel-aeroplane.md` |
| Talking Heads — *Remain in Light* (1980) | #6 Talking Heads + proposed prompt #19 | **Reroute:** prompt #19 becomes `albums/talking-heads-remain-in-light.md` |

After consolidation: 6 proposed prompts get rerouted to `albums/` folder. 5 brand-new album files needed for the multi-album existing-anchor cases (Bowie ×2, LCD ×2, Charli *Charli* + Radiohead *OK Computer*).

**Net new album files needed:** 89 total inputs − 5 already-proposed-as-prompts-which-reroute (BRAT, Kid A, Give Up, Aeroplane, Remain in Light) = **84 net new album-file research prompts**.

---

## The 89 albums catalogued by cluster

Categorization is for **batching efficiency** (research-adjacent albums in the same agent dispatch). Each album gets a tier:

- **S** — extensively documented (multiple S-tier production sources exist; expect ~25–35 chunks per album)
- **A** — well documented (Sound on Sound + Tape Op + multiple interviews; ~15–25 chunks)
- **B** — moderately documented (some specialist sources; ~10–18 chunks)
- **C** — thinly documented (one or two reputable sources; ~5–10 chunks)
- **X** — outsider / obscure (will require careful sourcing; flagged for hallucination risk)

### Cluster 1 — Hip-Hop Production (15 albums)

The deepest production-documented genre in this list after art-rock. Most of these have Tape Op interviews, Genius producer credits, and engineer-interview history.

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 1 | Beastie Boys — *Paul's Boutique* | 1989 | Dust Brothers | **S** | Sample-collage canon; well-documented |
| 2 | Public Enemy — *It Takes A Nation* | 1988 | The Bomb Squad | **S** | Hank Shocklee productions; foundational sampling |
| 3 | Dr. Dre — *The Chronic* | 1992 | Dr. Dre | **S** | G-funk template; analog synth focus |
| 4 | Wu-Tang — *Enter the Wu-Tang (36 Chambers)* | 1993 | RZA | **S** | Lo-fi sampling philosophy |
| 5 | Nas — *Illmatic* | 1994 | Multi-producer (Premier, Pete Rock, etc.) | **S** | Producer-per-track album; documented in *Check the Technique* |
| 6 | GZA — *Liquid Swords* | 1995 | RZA | **A** | Wu-Tang lineage extension |
| 7 | Outkast — *ATLiens* | 1996 | Organized Noize | **A** | Southern psychedelic-hip-hop |
| 8 | Lauryn Hill — *Miseducation* | 1998 | Hill + multiple | **A** | Solo arrangement + arrangement vocabulary |
| 9 | The Roots — *Things Fall Apart* | 1999 | Questlove + multiple | **A** | Live-band hip-hop production |
| 10 | Common — *Like Water for Chocolate* | 2000 | Soulquarians (J Dilla, Questlove, ?uestlove) | **A** | The Soulquarians collective sound |
| 11 | Outkast — *Stankonia* | 2000 | Outkast + Organized Noize | **A** | Maximalist production lineage |
| 12 | Madvillain — *Madvillainy* | 2004 | Madlib | **S** | Madlib's beat-construction philosophy; well-documented |
| 13 | Kanye West — *College Dropout* | 2004 | Kanye + No I.D. + Just Blaze | **S** | Soul-sampling chipmunk-vocal era |
| 14 | Kendrick Lamar — *To Pimp A Butterfly* | 2015 | Multiple (Sounwave, Flying Lotus, etc.) | **S** | Jazz-hip-hop hybrid; deeply analyzed |
| 15 | Kids See Ghosts — *Kids See Ghosts* | 2018 | Kanye + Cudi | **A** | Kanye-era psych-hip-hop |
| 16 | Clipse — *Let God Sort Em Out* | 2025 | Pharrell + Pusha + Malice | **A** | Recent release; expect SOS/Tape Op coverage |

**Cluster batch est:** 3 batches of 5–6 albums. ~280 chunks total.

### Cluster 2 — Art-Rock / Post-Punk / New Wave (12 albums)

Highest documentation density. Most of these have multiple S-tier production sources (SOS Classic Tracks, Mix Online, Tape Op).

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 17 | The Velvet Underground & Nico — *VU & Nico* | 1967 | Andy Warhol (nominal) / Tom Wilson | **S** | Foundational; well-documented |
| 18 | The Velvet Underground — *VU* (1969) | 1969 | The band | **A** | Loaded-with-mythology album |
| 19 | Lou Reed — *Transformer* | 1972 | Bowie + Ronson | **S** | The Reed-Bowie axis |
| 20 | Bowie — *Ziggy Stardust* | 1972 | Ken Scott | **S** | Pre-Berlin Bowie; glam template |
| 21 | Bowie — *Station to Station* | 1976 | Bowie + Harry Maslin | **S** | The transitional album to Berlin |
| 22 | Television — *Marquee Moon* | 1977 | Andy Johns | **S** | Twin-guitar-architecture template |
| 23 | Wire — *Pink Flag* | 1977 | Mike Thorne | **A** | Minimalist punk template |
| 24 | Joy Division — *Unknown Pleasures* | 1979 | Martin Hannett | **S** | Hannett production methodology canonical |
| 25 | Talking Heads — *Remain in Light* | 1980 | Brian Eno + Talking Heads | **S** | **Reroute from prompt #19** |
| 26 | They Might Be Giants — *Lincoln* | 1988 | TMBG + Bill Krauss | **B** | Indie-pop home-recording arc |
| 27 | Depeche Mode — *Violator* | 1990 | Flood + Alan Wilder | **S** | Industrial-pop production canon |
| 28 | Kate Bush — *Hounds of Love* | 1985 | Kate Bush | **S** | Self-production at her home studio; Fairlight CMI vocabulary |

**Cluster batch est:** 3 batches of 4. ~250 chunks. Strongest documentation density in the entire list.

### Cluster 3 — Punk / Hardcore / Post-Hardcore (10 albums)

Mix of canonical (Clash, Dead Kennedys) and aesthetic-outlier (Drive Like Jehu, Fugazi). Production is often deliberately *anti*-pristine — that itself is a teachable approach.

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 29 | Bad Brains — *Bad Brains* (yellow tape) | 1982 | Jay Dublee | **B** | Hardcore + reggae hybrid; recording-on-a-budget |
| 30 | Dead Kennedys — *Plastic Surgery Disasters* | 1982 | Norm + DK | **B** | Faith No More-era Bay Area engineering |
| 31 | The Misfits — *Earth A.D. / Wolf's Blood* | 1983 | Glenn Danzig + Eddie Stasium | **B** | Late-Misfits speed-punk shift |
| 32 | The Misfits — *Static Age* | 1996 (rec. 1977–78) | Dave Achelis | **B** | Lost-and-found archival release |
| 33 | The Slits — *Cut* | 1979 | Dennis Bovell | **A** | Dub-punk hybrid; Bovell's production approach |
| 34 | The Clash — *London Calling* | 1979 | Guy Stevens | **S** | Guy Stevens' famously chaotic production method |
| 35 | Violent Femmes — *Violent Femmes* | 1983 | Mark Van Hecke | **B** | Acoustic-punk minimalism |
| 36 | Fugazi — *Repeater* | 1990 | Fugazi + Ted Niceley | **A** | Inner Ear Studios + Don Zientara |
| 37 | Drive Like Jehu — *Yank Crime* | 1994 | Mark Trombino | **B** | Post-hardcore production |
| 38 | Daughters — *You Won't Get What You Want* | 2018 | Daughters + Seth Manchester | **B** | Noise-rock production resurgence |

**Cluster batch est:** 2 batches of 5. ~150 chunks.

### Cluster 4 — Electronic / Industrial / Trip-Hop / Avant-Pop (10 albums)

Production-deep genre; expect rich documentation for most.

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 39 | Portishead — *Dummy* | 1994 | Geoff Barrow + Adrian Utley | **S** | Trip-hop foundational; SOS coverage |
| 40 | Squarepusher — *Hard Normal Daddy* | 1997 | Tom Jenkinson | **A** | Drum-and-bass-meets-jazz |
| 41 | Björk — *Vespertine* | 2001 | Björk + Matmos + others | **S** | Micro-sound aesthetic; well-documented |
| 42 | Daft Punk — *Discovery* | 2001 | Daft Punk | **S** | Sample-and-house production lineage |
| 43 | Charli XCX — *Charli* | 2019 | A.G. Cook + multiple | **A** | Pre-Brat hyperpop era |
| 44 | Charli XCX — *BRAT* | 2024 | A.G. Cook + George Daniel + others | **A** | **Reroute from prompt #7** |
| 45 | Death Grips — *The Money Store* | 2012 | Zach Hill + Andy Morin (Flatlander) | **A** | Aggressive electronic-rap-noise hybrid |
| 46 | Spellling — *The Turning Wheel* | 2021 | Tia Cabral + multiple | **B** | Maximalist art-pop |
| 47 | Lingua Ignota — *SINNER GET READY* | 2021 | Kristin Hayter | **B** | Self-recorded; Appalachian-folk-meets-industrial |
| 48 | Threebrain — *Weeeeee!* | 2001 | Matt "Threebrain" Wilson | **X** | Outsider / Flash-era cult album; sparse documentation |

**Cluster batch est:** 2–3 batches. ~180 chunks. Threebrain is a hallucination-risk outlier.

### Cluster 5 — Singer-Songwriter / Folk / Soul (8 albums)

Lower production-complexity per album but extremely deep songwriting documentation.

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 49 | Bob Dylan — *The Freewheelin' Bob Dylan* | 1963 | John Hammond | **S** | Folk recording-as-document |
| 50 | Bob Dylan — *The Times They Are A-Changin'* | 1964 | Tom Wilson | **A** | Late acoustic Dylan |
| 51 | Bob Dylan — *Highway 61 Revisited* | 1965 | Bob Johnston + Tom Wilson | **S** | Electric Dylan; "Like a Rolling Stone" session |
| 52 | Bob Dylan — *Blonde on Blonde* | 1966 | Bob Johnston | **S** | Nashville sessions; "thin wild mercury sound" |
| 53 | Nina Simone — *Sings the Blues* | 1967 | Danny Davis | **A** | RCA-era Simone |
| 54 | Belle and Sebastian — *If You're Feeling Sinister* | 1996 | Tony Doogan | **A** | Indie-pop production restraint |
| 55 | The Microphones — *The Glow, Pt. 2* | 2001 | Phil Elverum | **S** | Self-recorded home aesthetic; widely studied |
| 56 | Ms. Lauryn Hill — *Miseducation* | 1998 | (already in hip-hop cluster #8) | — | de-duplicated |

**Cluster batch est:** 2 batches (one Dylan + one mixed). ~140 chunks.

### Cluster 6 — Pop / Rock / Stadium (8 albums)

Highly documented, foundational albums.

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 57 | The Beatles — *The Beatles (White Album)* | 1968 | George Martin | **S** | Faction-split / 8-track / minimal-engineering |
| 58 | The Beatles — *Abbey Road* | 1969 | George Martin + Geoff Emerick | **S** | 8-track session; Emerick's drum recording |
| 59 | Marvin Gaye — *What's Going On* | 1971 | Marvin Gaye | **S** | Self-produced; Motown rebellion |
| 60 | Led Zeppelin — *Physical Graffiti* | 1975 | Jimmy Page | **A** | Double-album, Headley Grange + studio hybrid |
| 61 | Pink Floyd — *Animals* | 1977 | Pink Floyd | **A** | Britannia Row Studios; Roger Waters era |
| 62 | Pink Floyd — *The Wall* | 1979 | Bob Ezrin + Pink Floyd | **S** | Ezrin production; double album |
| 63 | Prince — *Purple Rain* | 1984 | Prince + The Revolution | **S** | Sunset Sound + live-tracking-blended-with-studio |
| 64 | Janet Jackson — *The Velvet Rope* | 1997 | Jam & Lewis + Janet | **A** | Late-Jam-and-Lewis era pop production |

**Cluster batch est:** 2 batches of 4. ~150 chunks.

### Cluster 7 — Prog / Jazz Fusion / Experimental (6 albums)

Niche but deeply documented.

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 65 | Charles Mingus — *The Black Saint and the Sinner Lady* | 1963 | Bob Thiele | **A** | Impulse-era jazz production |
| 66 | King Crimson — *In the Court of the Crimson King* | 1969 | King Crimson + Tony Clarke (uncredited) | **S** | Prog template; Wessex Sound Studios |
| 67 | Miles Davis — *Bitches Brew* | 1970 | Teo Macero | **S** | Macero's tape-editing-as-composition |
| 68 | Mahavishnu Orchestra — *The Inner Mounting Flame* | 1971 | John McLaughlin | **A** | Jazz-fusion + virtuosity peak |
| 69 | Earth — *Earth 2: Special Low Frequency Version* | 1993 | Dylan Carlson | **B** | Drone-metal foundational |
| 70 | Godspeed You! Black Emperor — *Lift Yr. Skinny Fists* | 2000 | GY!BE | **B** | Post-rock chamber-epic |

**Cluster batch est:** 2 batches of 3. ~100 chunks.

### Cluster 8 — Shoegaze / Noise / Drone (4 albums)

Production-philosophy-heavy.

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 71 | My Bloody Valentine — *Loveless* | 1991 | Kevin Shields | **S** | Two-year sessions; ~£250k budget; defining shoegaze sonics |
| 72 | Swans — *Soundtracks for the Blind* | 1996 | Michael Gira | **A** | Late-90s Swans; double album |
| 73 | Swans — *To Be Kind* | 2014 | Michael Gira | **A** | Reunion-era Swans |
| 74 | The Stooges — *Fun House* | 1970 | Don Gallucci | **S** | Live-tracking-with-minimal-overdubs |
| 75 | The Stooges — *Raw Power* | 1973 | Iggy Pop + David Bowie mix | **A** | Bowie-mixed; mythologized post-mix-tape |

**Cluster batch est:** 1 batch of 5. ~100 chunks.

### Cluster 9 — Hard Rock / Metal (4 albums)

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 76 | Nirvana — *Nevermind* | 1991 | Butch Vig + Andy Wallace mix | **S** | Sound City; Wallace mix |
| 77 | Metallica — *Master of Puppets* | 1986 | Flemming Rasmussen | **S** | Sweet Silence Studios; thrash production canon |
| 78 | System of a Down — *Toxicity* | 2001 | Rick Rubin + Daron Malakian | **A** | Cello Studios; Rubin's mid-period |
| 79 | My Chemical Romance — *The Black Parade* | 2006 | Rob Cavallo | **A** | Bob Ezrin-influenced concept-album production |
| 80 | Weezer — *Weezer (Blue Album)* | 1994 | Ric Ocasek | **S** | Electric Lady Studios; Ocasek production |

**Cluster batch est:** 1 batch of 5. ~100 chunks.

### Cluster 10 — Outsider / Cult / Lo-fi (5 albums)

Mixed documentation. Cult-album category — fans have written deeply but mainstream music-tech press hasn't always.

| # | Album | Year | Producer focus | Tier | Notes |
|---|---|---|---|---|---|
| 81 | Tom Waits — *Rain Dogs* | 1985 | Tom Waits | **S** | Marc Ribot guitar; junkyard-percussion era |
| 82 | Tom Waits — *Bone Machine* | 1992 | Tom Waits | **S** | "Mr. Knickerbocker's room"; cement-room recording |
| 83 | Tom Waits — *Blood Money* | 2002 | Tom Waits + Kathleen Brennan | **A** | Late-Waits theater-album mode |
| 84 | The Unicorns — *Who Will Cut Our Hair When We're Gone?* | 2003 | The Unicorns | **B** | Montreal indie-pop cult album |
| 85 | Threebrain — *Weeeeee!* | 2001 | — | **X** | (already flagged in cluster 4) |

**Cluster batch est:** 1 batch of 4 (excluding Threebrain dupe). ~90 chunks.

### LCD + existing-anchor album files

These need album files but don't form a "cluster" — they slot into existing artist anchors.

| # | Album | Year | Notes |
|---|---|---|---|
| 86 | LCD Soundsystem — *Sound of Silver* | 2007 | New album file; cross-link to existing anchor #2 |
| 87 | LCD Soundsystem — *This Is Happening* | 2010 | New album file; cross-link to existing anchor #2 |
| 88 | Radiohead — *OK Computer* | 1997 | New album file; cross-link to existing anchor #8 |
| 89 | Postal Service — *Give Up* | 2003 | **Reroute** from prompt #33 to `albums/postal-service-give-up.md` |

(*Aeroplane*, *Remain in Light*, *Kid A*, *BRAT* already covered in the reroutes above.)

---

## Phase 1 starter pack — 10 albums to research first

These are the highest-leverage cuts: maximum production-vocabulary teaching per chunk, with reliably documented sources. Validate the album-anchored template + workflow on these before fanning out.

1. **Joy Division — *Unknown Pleasures*** — Martin Hannett's production methodology is canonical and exhaustively documented
2. **My Bloody Valentine — *Loveless*** — Two-year session, Kevin Shields' specific moves are widely written about
3. **Talking Heads — *Remain in Light*** (reroute from prompt #19) — Eno + Afrobeat polyrhythmic studio composition
4. **The Beatles — *Abbey Road*** — 8-track session, Geoff Emerick's drum recording techniques canonical
5. **Bowie — *Station to Station*** — Bridge to Berlin; "Stay" rhythm-section method
6. **Miles Davis — *Bitches Brew*** — Teo Macero's tape-editing-as-composition
7. **Radiohead — *Kid A*** (reroute from prompt #24) — Godrich's electronic shift methodology
8. **Beastie Boys — *Paul's Boutique*** — Dust Brothers sample-collage canonical
9. **Björk — *Vespertine*** — Micro-sound aesthetic; Matmos collaboration
10. **Tom Waits — *Rain Dogs*** — Marc Ribot guitar; junkyard-percussion vocabulary

**Phase 1 total:** ~250 chunks across 10 files. ~30 min wall time if 2 parallel batches of 5.

---

## Suggested batch structure (16 batches total for all 89 albums)

Each batch = 5–6 albums (so each agent's context budget is comfortable). After Phase 1's 2 starter batches, remaining ~14 batches across the 79 remaining albums.

| Batch | Cluster | Albums | Files | Wall time |
|---|---|---|---|---|
| **AL1** | Phase 1 starter A | Joy Division *UP*, MBV *Loveless*, Talking Heads *RIL*, Beatles *Abbey Road*, Bowie *Station to Station* | 5 | ~15 min |
| **AL2** | Phase 1 starter B | Miles *Bitches Brew*, Radiohead *Kid A*, Beasties *Paul's Boutique*, Björk *Vespertine*, Waits *Rain Dogs* | 5 | ~15 min |
| **AL3** | Hip-hop A | Public Enemy *INOM*, Dr. Dre *Chronic*, Wu-Tang *36 Chambers*, Nas *Illmatic*, GZA *Liquid Swords* | 5 | ~15 min |
| **AL4** | Hip-hop B | Outkast *ATLiens*, Lauryn Hill *Miseducation*, Roots *Things Fall Apart*, Common *LWFC*, Outkast *Stankonia* | 5 | ~15 min |
| **AL5** | Hip-hop C | Madvillain *Madvillainy*, Kanye *College Dropout*, Kendrick *TPAB*, KSG, Clipse *LGSEO* | 5 | ~15 min |
| **AL6** | Art-rock A | VU&Nico, VU (1969), Lou Reed *Transformer*, Bowie *Ziggy*, Television *Marquee Moon* | 5 | ~15 min |
| **AL7** | Art-rock B | Wire *Pink Flag*, TMBG *Lincoln*, Depeche *Violator*, Kate Bush *Hounds*, Beatles *White Album* | 5 | ~15 min |
| **AL8** | Punk A | Bad Brains, Dead Kennedys *PSD*, Misfits *Earth A.D.*, Misfits *Static Age*, Clash *London Calling* | 5 | ~15 min |
| **AL9** | Punk B / post-hardcore | The Slits *Cut*, Violent Femmes, Fugazi *Repeater*, Drive Like Jehu *Yank Crime*, Daughters *YWGWYW* | 5 | ~15 min |
| **AL10** | Electronic A | Portishead *Dummy*, Squarepusher *HND*, Daft Punk *Discovery*, Death Grips *Money Store* | 4 | ~12 min |
| **AL11** | Electronic B / pop-experimental | Charli *Charli*, Charli *BRAT*, Spellling *Turning Wheel*, Lingua Ignota *SGR*, Threebrain *Weeeeee!* | 5 | ~15 min |
| **AL12** | Folk / soul A | Dylan *Freewheelin'*, Dylan *Times*, Dylan *Highway 61*, Dylan *Blonde* | 4 | ~12 min |
| **AL13** | Folk / soul B | Nina Simone *Sings the Blues*, Belle & Sebastian *Sinister*, Microphones *Glow Pt 2*, Marvin Gaye *What's Going On* | 4 | ~12 min |
| **AL14** | Pop-rock / stadium | Led Zep *Physical Graffiti*, Pink Floyd *Animals*, Pink Floyd *Wall*, Prince *Purple Rain*, Janet *Velvet Rope* | 5 | ~15 min |
| **AL15** | Prog / jazz fusion / experimental | Mingus *BSSL*, King Crimson *ITCOTCK*, Mahavishnu *IMF*, Earth 2, GY!BE *Lift Yr Skinny Fists* | 5 | ~15 min |
| **AL16** | Shoegaze / noise / drone + metal | Swans *SFTB*, Swans *To Be Kind*, Stooges *Fun House*, Stooges *Raw Power* | 4 | ~12 min |
| **AL17** | Metal | Nirvana *Nevermind*, Metallica *Master*, SOAD *Toxicity*, MCR *Black Parade*, Weezer *Blue* | 5 | ~15 min |
| **AL18** | Cult / lo-fi / late-Waits + remaining existing-anchor albums | Waits *Bone Machine*, Waits *Blood Money*, Unicorns *Who Will Cut*, LCD *Sound of Silver*, LCD *This Is Happening*, Radiohead *OK Computer*, Postal Service *Give Up*, NMH *Aeroplane* | 8 | ~22 min |

**Total:** 18 batches, ~89 album files, **~290 min serial / ~30 min if 4 batches in parallel** (with Max 20x headroom).

Realistic phased pacing across "a few days":

- **Day 1:** Phase 1 (AL1 + AL2 in parallel, 10 files, ~15 min wall + verification)
- **Day 2:** Hip-hop trilogy (AL3 + AL4 + AL5 in parallel, 15 files, ~15 min wall)
- **Day 3:** Art-rock + punk (AL6 + AL7 + AL8 + AL9 in parallel, 20 files)
- **Day 4:** Electronic + folk (AL10 + AL11 + AL12 + AL13)
- **Day 5:** Pop-rock + prog + shoegaze + metal + cult (AL14–AL18)

That's a 5-day-ish pacing if you want to validate each wave before firing the next. Or compress to 1–2 days if you trust the template after Phase 1.

---

## Suggested album-anchored master template adjustment

The existing AESTHETIC-PROMPTS.md master template is artist-focused. The album-anchored variant only needs three changes:

1. **Front-matter additions:** `Album:`, `Artist:`, `Year:`, `Producer(s):`, `Studio(s):` — these become structured retrieval keys.
2. **Subtopic guidance:** focus on the *session* — who, where, when, what gear, what unusual production decisions, what the album's place is in the artist's catalog.
3. **Anti-hallucination note:** album-anchored content is especially vulnerable to invented session details (made-up gear, made-up engineer names, made-up studio dates). Tightened guard required.

I'll write the full album-anchored template inside `ALBUMS-PROMPTS.md` when we're ready to fire batches. Same shape as AESTHETIC-PROMPTS.md, just with the album-specific front-matter and 89 rows.

---

## Documentation-density expectations

Per-tier rough chunk estimates after all 18 batches:

| Tier | Album count | Avg chunks | Total chunks |
|---|---|---|---|
| **S** | ~30 | 28 | ~840 |
| **A** | ~30 | 18 | ~540 |
| **B** | ~20 | 13 | ~260 |
| **C** | ~7 | 8 | ~56 |
| **X** | ~2 | 6 | ~12 |
| **TOTAL** | **89** | — | **~1700 chunks** |

That's roughly **2× the current entire-corpus chunk ceiling** if we ingest the whole 89-album set. Realistic: ingest Phase 1, evaluate retrieval quality, then decide whether to fan out the rest or stop at a working subset.

---

## Anti-hallucination notes per cluster

Specific things to watch in agent prompts:

- **Hip-hop sampling claims:** producer-X-sampled-track-Y is often misattributed. WhoSampled.com is the gold reference; agents should cross-check sample claims there.
- **Bob Dylan session dates and personnel:** four albums in three years, lots of overlap with session musicians. Use *Bob Dylan: A Life in Stolen Moments* and Wikipedia album credit tables; don't invent musicians.
- **Brian Eno-related claims:** Eno is mentioned in many albums (Talking Heads, Bowie, U2, etc.) but his actual production credit varies. Wikipedia's clear "Producer:" credit line is the citation anchor.
- **Mythologized albums** (*Bitches Brew*, *London Calling*, *Loveless*, *Paul's Boutique*) have apocryphal stories — agents should prefer verifiable production-magazine sources over fan-forum lore.
- **Outsider/cult albums** (*Threebrain — Weeeeee!*, *The Unicorns*) have light documentation; agents should keep chunks short and stick to what's verifiable rather than padding with speculation.
- **Older albums (pre-1970)** have unclear engineer credits in some cases. Producer credit is reliable; engineer credit varies. Don't invent engineer names.

---

## Acquisition delta

Three new acquisitions worth considering as this list rolls out:

1. **Brian Coleman, *Check the Technique* (Vol 1 & 2)** — track-by-track interviews with the producers of canonical hip-hop albums. Direct insight into about 15 of the 16 hip-hop albums in cluster 1. Worth buying.
2. **Mark Lewisohn, *Tune In* / *The Beatles Recording Sessions*** — definitive Beatles session log; replaces Wikipedia for the two Beatles albums in this list.
3. **Mike Howlett / Trevor Horn / Steve Lillywhite production-school content** — for the British art-rock cluster (Joy Division, Wire, Television-era Andy Johns, Depeche, Kate Bush).

These don't block Phase 1 — agents can do good work on these albums from web sources alone. But the books would upgrade the chunks from "synthesis" to "direct-quote" provenance over time.

---

## What I'd do this turn vs. next turn

**This turn:** the plan you're reading. Decision committed (album-anchored), structure committed (`corpus/albums/`), batches committed (AL1–AL18), Phase 1 starter pack chosen.

**Next turn (or whenever you're ready):**
1. Write `ALBUMS-PROMPTS.md` with the album-anchored master template + 89 prompt rows (full variable sets — same format as `AESTHETIC-PROMPTS.md`)
2. Write `ALBUMS-SESSIONS.md` with the 18 batch kickoff messages
3. Dispatch Phase 1 (AL1 + AL2) as parallel agents from the main session
4. Validate output on those 10 files before firing the rest

Want me to proceed with (1)+(2) — drafting `ALBUMS-PROMPTS.md` and `ALBUMS-SESSIONS.md` now? Or do you want to review the plan and adjust the cluster groupings / duplicate-resolution decisions first?
