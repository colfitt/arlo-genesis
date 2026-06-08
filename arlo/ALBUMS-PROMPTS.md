# ARLO Albums Corpus — Prompt Set

89 album-anchored prompts produced from `ALBUMS-RESEARCH-PLAN.md`. Output: 89 markdown files in `corpus/albums/`, each ~1500–2500 words on a single album's production story.

**Format-friendly note:** rows 1–89 below are compact (~8–12 lines each). Each row gives the agent the minimum it needs — title, producer(s), studio(s) where known, focus subtopics, primary-source pointers (Wikipedia + verified production sources where known, plus search hints), and tags. The agent runs WebSearch to resolve the remaining citations at research-time.

**Folder additions reminder:**

```bash
mkdir -p ~/Dev/arlo/corpus/albums
```

---

## Master template — album-anchored variant

```
You are writing a seed knowledge-base entry for ARLO, a local-first AI songwriting/production assistant. The entry will be parsed into ~8–15 retrievable chunks and cited back to users during conversation about music production.

CONTEXT: ARLO already has a corpus of artist-anchored chunks (in corpus/artists/) and technique-anchored chunks (in corpus/techniques/). This new entry is ALBUM-anchored — focused on a single album's production story, gear, sessions, and decisions.

ALBUM: {{ARTIST}} — {{ALBUM_TITLE}} ({{YEAR}})
PRODUCER(S): {{PRODUCERS}}
STUDIO(S): {{STUDIOS}}
TARGET PATH: corpus/albums/{{FILENAME}}.md

## Your task

Produce a single markdown file on the production of "{{ALBUM_TITLE}}" focused on these subtopics:

{{SUBTOPICS}}

## Primary sources to ground in

Read or reference these sources as your starting evidence. Augment with WebSearch as needed.

{{PRIMARY_SOURCES}}

## Content requirements

- **Album-as-artifact framing.** Tell the *session story* — who was in the room, what gear they used, what unusual decisions they made, what the album represents in the artist's catalog. NOT "philosophy of {{ARTIST}}." That's the artist-overview file's job.
- **Concrete over abstract.** Specific tape machines, specific studios, specific engineers, specific microphones, specific mixing-console models, specific outboard, specific dates, specific track-by-track details where available.
- **Inline citations.** Use markdown links — `[Source Title](URL)` — within sentences where claims originate. Don't save citations only for a bibliography.
- **Anti-hallucination guard.** If you cannot verify a specific producer credit, engineer name, gear model, studio name, or session date through web research, OMIT it. Do not guess. Made-up specifics will poison ARLO's retrieval. When uncertain, prefer qualitative claims over fabricated specifics.
- **Specific anti-hallucination watch list for album content:**
  - Engineer credits for pre-1975 albums are often unclear; verify before naming
  - Brian Eno's production credit varies between "producer," "collaborator," and "atmosphere/textures"; check Wikipedia's "Producer:" credit line specifically
  - Hip-hop sample claims: cross-check WhoSampled.com before citing a sample
  - Mythologized stories (apocryphal session anecdotes) — prefer Sound on Sound / Tape Op / Mix Online over fan-forum lore
- **Length:** 1500–2500 words.
- **Structure:** 8–15 H2 sections, each 100–250 words. Each section is a chunk.
- **Audience:** intermediate musicians/producers. Don't re-explain basic vocabulary.

## Required output format

Begin with this front-matter block:

```
# {{ALBUM_TITLE}} ({{YEAR}})

**Artist:** {{ARTIST}}
**Year:** {{YEAR}}
**Producer(s):** {{PRODUCERS}}
**Studio(s):** {{STUDIOS}}
**Scope:** album
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Aesthetic-stack relevance:** {{AESTHETIC_TAGS}}
**Tags:** {{SUGGESTED_TAGS}}

---
```

Then 8–15 H2 sections covering the subtopics. Recommended skeleton (adapt based on what's actually documented):

1. Album context (where it sits in the artist's catalog)
2. Production team & roles
3. Studio(s) & timeline
4. Key gear / signal-chain choices
5. Unusual or signature production decisions (this is where the chunks become most retrievable)
6. Track-by-track highlights (the 1–3 tracks with the best-documented sessions)
7. Mixing & mastering
8. Reception & legacy in production terms (who cites this album as their reference)

End with these two required sections:

```
## Cited Retrieval Topics

5–10 specific user questions this album's chunks should answer. Phrase them as a musician would actually type — lowercase, conversational, no question marks.

## Sources

Clean bibliography of every URL linked inline above.
```

## What this is NOT

- Not an album review (no opinions on song quality)
- Not a biography of {{ARTIST}} (that's the artist-overview file)
- Not an exhaustive song-by-song breakdown — pick the 2–4 tracks with the deepest documentation

Begin research and produce the markdown now.
```

---

## Worked example — what a fully-substituted prompt looks like

Substituting **row #6 (Miles Davis — *Bitches Brew*)** into the template:

> ALBUM: Miles Davis — *Bitches Brew* (1970)
> PRODUCER(S): Teo Macero
> STUDIO(S): Columbia 30th Street Studio, NYC (August 19–21, 1969)
> TARGET PATH: corpus/albums/miles-davis-bitches-brew.md
>
> ## Your task
> Produce a single markdown file on the production of *Bitches Brew* focused on:
> - Teo Macero's tape-editing-as-composition methodology
> - The 1969 session ensemble (multiple keyboardists, doubled bass, John McLaughlin's electric guitar role)
> - The studio-as-instrument approach — Macero splicing master tapes after-the-fact to create the final structures
> - The transition from acoustic to electric Miles
> - The album's foundational role in jazz-fusion production
>
> ## Primary sources
> - [Wikipedia: Bitches Brew](https://en.wikipedia.org/wiki/Bitches_Brew) (Wikipedia is the canonical session-detail and credit reference)
> - [JazzWax: Teo Macero interviews](https://www.jazzwax.com) (search "Teo Macero")
> - Search Sound on Sound for "Teo Macero" or "Miles Davis Bitches Brew"
> - Search Tape Op for jazz-fusion engineering features
> - [George Avakian / Teo Macero documentary](https://www.jazz.org) and related Columbia Records oral histories
>
> [...rest of template...]
>
> Tags: `bitches-brew`, `miles-davis`, `teo-macero`, `tape-editing`, `jazz-fusion`, `studio-as-composition`, `columbia-records`

The agent fills in the rest from WebSearch + the master template.

---

## The 89 Prompts — Organized by Batch

Each prompt below contains the minimum agent-actionable variables. Wikipedia URLs are constructed reliably (`en.wikipedia.org/wiki/Album_Slug`); other URLs are search hints unless a specific verified link is given.

---

### Batch AL1 — Phase 1 Starter A

#### 1. `joy-division-unknown-pleasures`
- **Album:** Joy Division — *Unknown Pleasures* (1979)
- **Producer(s):** Martin Hannett
- **Studio(s):** Strawberry Studios, Stockport
- **Focus:** Hannett's production methodology (separating drum parts spatially, ambient room mics, AMS digital delay use); Hannett's working-style legend (overnight sessions, manipulating tape mid-mix); Peter Saville cover; Hannett's broader Manchester influence
- **Sources:** [Wikipedia: Unknown Pleasures](https://en.wikipedia.org/wiki/Unknown_Pleasures); SOS classic-tracks search for "Joy Division" or "Martin Hannett"; Tape Op archive search for "Hannett"
- **Tags:** `joy-division`, `hannett`, `strawberry-studios`, `post-punk`, `ams-delay`, `spatial-recording`

#### 2. `my-bloody-valentine-loveless`
- **Album:** My Bloody Valentine — *Loveless* (1991)
- **Producer(s):** Kevin Shields
- **Studio(s):** 19+ studios over ~2 years; ~£250k budget
- **Focus:** "Glide guitar" tremolo-bar bending technique; reverse-reverb vocals; sampler-as-drum-bus; "you wouldn't be able to play any of this live" production rule; Shields' obsessive overdub-and-revise method
- **Sources:** [Wikipedia: Loveless](https://en.wikipedia.org/wiki/Loveless_(album)); [SOS Classic Tracks: Loveless](https://www.soundonsound.com/techniques/classic-tracks-my-bloody-valentine-loveless); Shields interviews via Pitchfork / Quietus retrospectives
- **Tags:** `mbv`, `kevin-shields`, `shoegaze`, `glide-guitar`, `reverse-reverb`, `tremolo-bar`

#### 3. `talking-heads-remain-in-light`
- **Album:** Talking Heads — *Remain in Light* (1980)
- **Producer(s):** Brian Eno + Talking Heads
- **Studio(s):** Compass Point Studios (Bahamas) + Sigma Sound (Philly) + Eventide Studios (NY)
- **Focus:** Polyrhythmic-Afrobeat ensemble construction; studio-as-composition (no pre-written songs); Eno's role as "fifth Head"; "Once in a Lifetime" looping methodology; Adrian Belew's guitar overdubs
- **Sources:** [Wikipedia: Remain in Light](https://en.wikipedia.org/wiki/Remain_in_Light); [Classic Pop on Remain in Light](https://www.classicpopmag.com/features/talking-heads-remain-in-light/); [David Byrne's site on the Eno meeting](https://www.davidbyrne.com/news/40-years-ago-brian-eno-meets-david-byrne-changing-the-talking-heads-career-); [More Dark Than Shark Byrne interview Nov 1980](https://moredarkthanshark.org/eno_int_riu-nov80.html)
- **Tags:** `talking-heads`, `byrne`, `eno`, `compass-point`, `polyrhythmic`, `studio-as-composition`, `afrobeat-inflected`

#### 4. `beatles-abbey-road`
- **Album:** The Beatles — *Abbey Road* (1969)
- **Producer(s):** George Martin
- **Studio(s):** EMI Studios (Abbey Road), London
- **Focus:** First Beatles album on 8-track tape (Studer J37); Geoff Emerick's return after *White Album*; "Side B medley" production approach; Moog use; Ringo's drum sound on this record specifically; "Here Comes the Sun" string arrangement
- **Sources:** [Wikipedia: Abbey Road](https://en.wikipedia.org/wiki/Abbey_Road); [Wikipedia: Geoff Emerick](https://en.wikipedia.org/wiki/Geoff_Emerick); Lewisohn's *Recording Sessions* (acquisition note); search SOS for "Abbey Road" + "Emerick"
- **Tags:** `beatles`, `george-martin`, `geoff-emerick`, `emi-studios`, `studer-j37`, `8-track`

#### 5. `bowie-station-to-station`
- **Album:** David Bowie — *Station to Station* (1976)
- **Producer(s):** David Bowie + Harry Maslin
- **Studio(s):** Cherokee Studios, Los Angeles
- **Focus:** The bridge album from *Young Americans* soul/funk to Berlin; "Stay" rhythm-section method; Earl Slick guitar; Carlos Alomar funk rhythm-guitar foundation; Bowie's cocaine-fueled sessions; the album that sets up Eno collaboration
- **Sources:** [Wikipedia: Station to Station](https://en.wikipedia.org/wiki/Station_to_Station); [Bowie Bible: Station to Station](https://www.bowiebible.com/albums/station-to-station/); search Mix Online / SOS for "Bowie Cherokee Studios"
- **Tags:** `bowie`, `harry-maslin`, `cherokee-studios`, `carlos-alomar`, `thin-white-duke`, `pre-berlin`

---

### Batch AL2 — Phase 1 Starter B

#### 6. `miles-davis-bitches-brew`
- **Album:** Miles Davis — *Bitches Brew* (1970)
- **Producer(s):** Teo Macero
- **Studio(s):** Columbia 30th Street Studio, NYC (Aug 19–21, 1969)
- **Focus:** Macero's post-session tape-splicing as composition; multi-keyboardist ensemble (Corea, Zawinul, Hancock); John McLaughlin's electric guitar role; the "directed improvisation" approach Miles brought; the album's role launching jazz-fusion
- **Sources:** [Wikipedia: Bitches Brew](https://en.wikipedia.org/wiki/Bitches_Brew); search JazzWax + Sound on Sound for "Teo Macero"; Columbia Records oral histories
- **Tags:** `miles-davis`, `teo-macero`, `bitches-brew`, `tape-editing`, `jazz-fusion`, `columbia-30th-street`

#### 7. `radiohead-kid-a`
- **Album:** Radiohead — *Kid A* (2000)
- **Producer(s):** Nigel Godrich
- **Studio(s):** Guillaume Tell (Paris), Medley Studios (Copenhagen), and others
- **Focus:** The electronic shift from *OK Computer*; Godrich's role; ondes martenot and ProTools-era electronic textures; Yorke's deliberate vocal-as-texture approach on "Everything In Its Right Place"; "Idioteque" sample (Paul Lansky)
- **Sources:** [Wikipedia: Kid A](https://en.wikipedia.org/wiki/Kid_A); [Happy Mag: Engineering In Rainbows (covers Godrich method)](https://happymag.tv/engineering-the-sound-radioheads-in-rainbows/); [Nigel Godrich Producer Tumblr archive](https://nigelgodrichproducer.tumblr.com)
- **Tags:** `radiohead`, `godrich`, `kid-a`, `electronic-shift`, `ondes-martenot`, `protools-era`

#### 8. `beastie-boys-pauls-boutique`
- **Album:** Beastie Boys — *Paul's Boutique* (1989)
- **Producer(s):** The Dust Brothers (E.Z. Mike + King Gizmo / John King + Mike Simpson)
- **Studio(s):** Mario Caldato Jr.'s home studio + Record Plant LA
- **Focus:** Sample-collage canon (~105 samples documented); pre-lawsuit-era sampling freedom; Dust Brothers production philosophy; the Beastie Boys' transition from license-to-ill production
- **Sources:** [Wikipedia: Paul's Boutique](https://en.wikipedia.org/wiki/Paul%27s_Boutique); [WhoSampled: Paul's Boutique](https://www.whosampled.com/album/Beastie-Boys/Paul's-Boutique/); [Stereogum: Paul's Boutique production retrospective](https://www.stereogum.com) (search); Brian Coleman's *Check the Technique* Vol 1 has a chapter
- **Tags:** `beastie-boys`, `dust-brothers`, `pauls-boutique`, `sample-collage`, `pre-lawsuit-sampling`, `hip-hop-production`

#### 9. `bjork-vespertine`
- **Album:** Björk — *Vespertine* (2001)
- **Producer(s):** Björk + Matmos + Console (Martin Gretschmann)
- **Studio(s):** Greenhouse Studios (Iceland) + Björk's home + various
- **Focus:** Micro-sound aesthetic ("intimacy at a whisper"); Matmos collaboration on field-recorded sound design (cards being shuffled, ice cracking); the Iceland Symphony Orchestra arrangements; harp / celeste / music-box palette; intimate-headphones mix target
- **Sources:** [Wikipedia: Vespertine](https://en.wikipedia.org/wiki/Vespertine); [Sound on Sound: Björk Vespertine](https://www.soundonsound.com/techniques/recording-bjork) (search confirmation); Matmos interviews on the collaboration
- **Tags:** `bjork`, `vespertine`, `matmos`, `micro-sound`, `intimate-mix`, `field-recording`, `headphones-aesthetic`

#### 10. `tom-waits-rain-dogs`
- **Album:** Tom Waits — *Rain Dogs* (1985)
- **Producer(s):** Tom Waits
- **Studio(s):** RPM Studios, NYC
- **Focus:** Marc Ribot guitar (his first Waits album); junkyard-percussion + brake-drum + dustbin-lid; Larry Taylor bass / Stephen Hodges drums; the Brennan-Waits writing partnership era; the 19-song eclectic structure (vaudeville-meets-blues-meets-Kurt-Weill)
- **Sources:** [Wikipedia: Rain Dogs](https://en.wikipedia.org/wiki/Rain_Dogs); search Tape Op + Mix Online for "Tom Waits Rain Dogs"; Marc Ribot interview archives
- **Tags:** `tom-waits`, `marc-ribot`, `rain-dogs`, `rpm-studios`, `junkyard-percussion`, `brennan-waits`

---

### Batch AL3 — Hip-Hop A

#### 11. `public-enemy-it-takes-a-nation`
- **Album:** Public Enemy — *It Takes a Nation of Millions to Hold Us Back* (1988)
- **Producer(s):** The Bomb Squad (Hank Shocklee, Keith Shocklee, Eric Sadler, Chuck D)
- **Studio(s):** Greene St. Recording, NYC
- **Focus:** The Bomb Squad's layered-noise sampling approach; James Brown horn stabs; the "wall of sound"-meets-hip-hop production; Chuck D vocal sound; Flavor Flav as counter-voice; pre-1991 sample-clearance era
- **Sources:** [Wikipedia: It Takes a Nation](https://en.wikipedia.org/wiki/It_Takes_a_Nation_of_Millions_to_Hold_Us_Back); [WhoSampled](https://www.whosampled.com/album/Public-Enemy/It-Takes-a-Nation-of-Millions-to-Hold-Us-Back/); search Brian Coleman *Check the Technique* references
- **Tags:** `public-enemy`, `bomb-squad`, `hank-shocklee`, `sample-layering`, `pre-clearance-era`, `political-hip-hop`

#### 12. `dr-dre-the-chronic`
- **Album:** Dr. Dre — *The Chronic* (1992)
- **Producer(s):** Dr. Dre
- **Studio(s):** Death Row Studios, Tarzana
- **Focus:** G-funk template (Moog leads, P-Funk samples, sparse drums, deep bass); the Snoop Dogg vocal sound; Dre's mixing approach (deep low end, vocals up front); the post-N.W.A. solo template
- **Sources:** [Wikipedia: The Chronic](https://en.wikipedia.org/wiki/The_Chronic); [WhoSampled](https://www.whosampled.com/album/Dr.-Dre/The-Chronic/); Brian Coleman *Check the Technique* Vol 2 chapter
- **Tags:** `dr-dre`, `the-chronic`, `g-funk`, `death-row`, `moog-lead`, `west-coast`, `hip-hop-mixing`

#### 13. `wu-tang-36-chambers`
- **Album:** Wu-Tang Clan — *Enter the Wu-Tang (36 Chambers)* (1993)
- **Producer(s):** RZA
- **Studio(s):** Firehouse Studio + 36 Chambers (RZA's home basement studio)
- **Focus:** RZA's lo-fi sampling philosophy (dusty kung-fu film dialog, soul samples, rough drum loops); 8-MC posse-cut arrangement; "Method Man" as the breakout track; the cold/abrasive mix aesthetic
- **Sources:** [Wikipedia: 36 Chambers](https://en.wikipedia.org/wiki/Enter_the_Wu-Tang_(36_Chambers)); [WhoSampled](https://www.whosampled.com/album/Wu-Tang-Clan/Enter-the-Wu-Tang-(36-Chambers)/); Brian Coleman *Check the Technique* Vol 1
- **Tags:** `wu-tang`, `rza`, `36-chambers`, `lo-fi-sampling`, `kung-fu-samples`, `posse-cut`

#### 14. `nas-illmatic`
- **Album:** Nas — *Illmatic* (1994)
- **Producer(s):** DJ Premier, Pete Rock, Q-Tip, Large Professor, L.E.S.
- **Studio(s):** D&D Studios, NYC + Battery Studios
- **Focus:** Per-track producer rotation (each beat from a different NYC heavyweight); jazz-sample lineage; Nas vocal recording approach; "N.Y. State of Mind" Premier methodology; the 10-track concise format
- **Sources:** [Wikipedia: Illmatic](https://en.wikipedia.org/wiki/Illmatic); Matthew Gasteier's *Illmatic* (33 1/3 series) — referenced widely; [WhoSampled](https://www.whosampled.com/album/Nas/Illmatic/); Brian Coleman chapter
- **Tags:** `nas`, `illmatic`, `dj-premier`, `pete-rock`, `q-tip`, `large-professor`, `nyc-hip-hop`

#### 15. `gza-liquid-swords`
- **Album:** GZA — *Liquid Swords* (1995)
- **Producer(s):** RZA
- **Studio(s):** 36 Chambers (RZA's home studio)
- **Focus:** RZA's post-*36 Chambers* sonic evolution; chess-themed kung-fu dialog samples; GZA's lyrical density vs RZA's spare beats; the Killer Bee Wu-affiliate template
- **Sources:** [Wikipedia: Liquid Swords](https://en.wikipedia.org/wiki/Liquid_Swords); [WhoSampled](https://www.whosampled.com/album/GZA/Liquid-Swords/); RZA's *Wu-Tang Manual* book reference
- **Tags:** `gza`, `rza`, `liquid-swords`, `wu-tang-affiliate`, `chess-themes`, `kung-fu-samples`

---

### Batch AL4 — Hip-Hop B

#### 16. `outkast-atliens`
- **Album:** Outkast — *ATLiens* (1996)
- **Producer(s):** Organized Noize + Outkast + Mr. DJ
- **Studio(s):** Bobby Brown's Bosstown Recording + Studio LaCoCo, Atlanta
- **Focus:** Organized Noize southern-soul + psychedelic production; transition from the Dungeon Family aesthetic; the breakthrough beyond regional-rap into psychedelic territory
- **Sources:** [Wikipedia: ATLiens](https://en.wikipedia.org/wiki/ATLiens); [WhoSampled](https://www.whosampled.com/album/OutKast/ATLiens/); Brian Coleman *Check the Technique* Vol 2 chapter on Outkast
- **Tags:** `outkast`, `organized-noize`, `atliens`, `dungeon-family`, `southern-hip-hop`, `psychedelic-rap`

#### 17. `lauryn-hill-miseducation`
- **Album:** Ms. Lauryn Hill — *The Miseducation of Lauryn Hill* (1998)
- **Producer(s):** Lauryn Hill (+ Vada Nobles, Tejumold Newton, others)
- **Studio(s):** Tuff Gong Studios (Jamaica) + Chung King + RPM
- **Focus:** Hill's self-production after Fugees breakup; reggae-influence rhythm tracks; the "Doo Wop" string arrangement; vocal layering as choir-of-one; the Mary J Blige / Aretha guest features
- **Sources:** [Wikipedia: Miseducation](https://en.wikipedia.org/wiki/The_Miseducation_of_Lauryn_Hill); Joan Morgan's *She Begat This* book; SOS / Tape Op late-90s neo-soul features
- **Tags:** `lauryn-hill`, `miseducation`, `tuff-gong`, `neo-soul`, `reggae-influence`, `vocal-layering`

#### 18. `roots-things-fall-apart`
- **Album:** The Roots — *Things Fall Apart* (1999)
- **Producer(s):** The Grand Wizzards (Questlove, ?uestlove era), Scott Storch
- **Studio(s):** Electric Lady Studios, NYC
- **Focus:** Live-band hip-hop production; Questlove drum philosophy; the Soulquarians collective context (J Dilla, D'Angelo, Erykah Badu cross-pollination); "You Got Me" arrangement
- **Sources:** [Wikipedia: Things Fall Apart](https://en.wikipedia.org/wiki/Things_Fall_Apart_(album)); Questlove interviews via Pensado's Place, Tape Op, Reverb News; Brian Coleman *Check the Technique* Vol 2
- **Tags:** `the-roots`, `questlove`, `things-fall-apart`, `soulquarians`, `electric-lady`, `live-band-hip-hop`

#### 19. `common-like-water-for-chocolate`
- **Album:** Common — *Like Water for Chocolate* (2000)
- **Producer(s):** Soulquarians (J Dilla, Questlove, James Poyser, D'Angelo, ?uestlove)
- **Studio(s):** Electric Lady Studios, NYC + Greenhouse Studios
- **Focus:** Soulquarians collective approach (live-instrument-meets-sampled-drums); J Dilla's "drunken" feel; D'Angelo's harmonic contributions; "The Light" production methodology
- **Sources:** [Wikipedia: Like Water for Chocolate](https://en.wikipedia.org/wiki/Like_Water_for_Chocolate_(album)); Questlove's *Mo' Meta Blues* book; Soulquarians-era oral histories
- **Tags:** `common`, `soulquarians`, `j-dilla`, `questlove`, `dangelo`, `electric-lady`, `neo-soul-rap`

#### 20. `outkast-stankonia`
- **Album:** Outkast — *Stankonia* (2000)
- **Producer(s):** Outkast (Andre, Big Boi, Mr. DJ) + Organized Noize
- **Studio(s):** Stankonia Studios, Atlanta (the band's own studio)
- **Focus:** Maximalist Atlanta production; "B.O.B." (Bombs Over Baghdad) drum-and-bass-influenced BPM; "Ms. Jackson" arrangement; Andre's growing experimentation; the post-Aquemini move
- **Sources:** [Wikipedia: Stankonia](https://en.wikipedia.org/wiki/Stankonia); [WhoSampled](https://www.whosampled.com/album/OutKast/Stankonia/); Mix Online / Tape Op late-90s southern hip-hop features
- **Tags:** `outkast`, `stankonia`, `andre-3000`, `big-boi`, `stankonia-studios`, `maximalist-rap`

---

### Batch AL5 — Hip-Hop C

#### 21. `madvillain-madvillainy`
- **Album:** Madvillain — *Madvillainy* (2004)
- **Producer(s):** Madlib
- **Studio(s):** Madlib's home / Bomb Shelter studio
- **Focus:** Madlib's beat-construction (sample-flips, short loops, lo-fi aesthetic); MF DOOM verse-as-collage approach; the album's leaked-demo-then-released history; Stones Throw Records context
- **Sources:** [Wikipedia: Madvillainy](https://en.wikipedia.org/wiki/Madvillainy); [WhoSampled](https://www.whosampled.com/album/Madvillain/Madvillainy/); Stones Throw documentary references; Madlib + MF DOOM interviews
- **Tags:** `madvillain`, `madlib`, `mf-doom`, `stones-throw`, `lo-fi-hip-hop`, `sample-flip`

#### 22. `kanye-college-dropout`
- **Album:** Kanye West — *The College Dropout* (2004)
- **Producer(s):** Kanye West (+ No I.D., Just Blaze, others)
- **Studio(s):** Sony Music Studios, NYC + Chalice Recording Studios, LA
- **Focus:** The "chipmunk soul" sampling era (pitched-up soul vocals); Kanye as producer-becoming-artist; the breakthrough from Roc-A-Fella in-house producer role; "Through the Wire" car-accident origin
- **Sources:** [Wikipedia: The College Dropout](https://en.wikipedia.org/wiki/The_College_Dropout); [WhoSampled](https://www.whosampled.com/album/Kanye-West/The-College-Dropout/); Brian Coleman / Pitchfork retrospective
- **Tags:** `kanye-west`, `college-dropout`, `chipmunk-soul`, `roc-a-fella`, `sample-flip`, `no-id`

#### 23. `kendrick-to-pimp-a-butterfly`
- **Album:** Kendrick Lamar — *To Pimp a Butterfly* (2015)
- **Producer(s):** Sounwave, Flying Lotus, Pharrell, Boi-1da, Terrace Martin, Knxwledge, Thundercat
- **Studio(s):** No I.D.'s personal studio + multiple
- **Focus:** Jazz-hip-hop hybrid; Kamasi Washington / Thundercat / Terrace Martin live-jazz contributions; "King Kunta" funk pocket; the Compton record that became a treatise; cohesive sequencing
- **Sources:** [Wikipedia: To Pimp a Butterfly](https://en.wikipedia.org/wiki/To_Pimp_a_Butterfly); Pitchfork TPAB retrospective; Sounwave interviews; Thundercat session-credit interviews
- **Tags:** `kendrick`, `tpab`, `sounwave`, `thundercat`, `kamasi-washington`, `jazz-hip-hop`

#### 24. `kids-see-ghosts-debut`
- **Album:** Kids See Ghosts — *Kids See Ghosts* (2018)
- **Producer(s):** Kanye West + Kid Cudi (+ Plain Pat, Mike Dean)
- **Studio(s):** Diamond Mountain Studios, Wyoming
- **Focus:** Kanye's Wyoming-era 7-song-album format; psych-rock samples + Cudi's vocal approach; "Reborn" arrangement; "4th Dimension" Louis Prima sample; Mike Dean's role
- **Sources:** [Wikipedia: Kids See Ghosts](https://en.wikipedia.org/wiki/Kids_See_Ghosts_(album)); 2018 Wyoming-sessions oral history coverage (NY Times, Pitchfork)
- **Tags:** `kanye-west`, `kid-cudi`, `kids-see-ghosts`, `mike-dean`, `wyoming-sessions`, `7-song-format`

#### 25. `clipse-let-god-sort-em-out`
- **Album:** Clipse — *Let God Sort Em Out* (2025)
- **Producer(s):** Pharrell Williams + Clipse + (others — verify)
- **Studio(s):** TBD via research
- **Focus:** Pharrell production after the long gap; Pusha T + Malice (No Malice) reunion context; reception as a return-to-form; specific production techniques (verify via SOS/Tape Op if covered)
- **Sources:** [Wikipedia: Let God Sort Em Out](https://en.wikipedia.org/wiki/Let_God_Sort_Em_Out); recent (2025) production-press coverage via Pitchfork / Stereogum / Complex
- **Tags:** `clipse`, `pusha-t`, `pharrell`, `let-god-sort-em-out`, `recent-2025`

---

### Batch AL6 — Art-Rock A

#### 26. `velvet-underground-and-nico`
- **Album:** The Velvet Underground & Nico — *The Velvet Underground & Nico* (1967)
- **Producer(s):** Andy Warhol (nominal) + Tom Wilson (engineer-producer)
- **Studio(s):** Scepter Studios, NYC + TT&G Studios, LA
- **Focus:** Warhol's role as cultural enabler vs. Tom Wilson's actual engineering; Cale's viola drone on "Venus in Furs"; the unusual mic placement and dead-room sound; Mo Tucker's drum kit setup (standing, no cymbals on some tracks)
- **Sources:** [Wikipedia: VU & Nico](https://en.wikipedia.org/wiki/The_Velvet_Underground_%26_Nico); Lou Reed / John Cale interview archives; Mix Online / SOS late-60s NYC scene articles
- **Tags:** `velvet-underground`, `nico`, `andy-warhol`, `tom-wilson`, `john-cale`, `mo-tucker`, `1960s-nyc`

#### 27. `velvet-underground-1969`
- **Album:** The Velvet Underground — *The Velvet Underground* (1969)
- **Producer(s):** The Velvet Underground
- **Studio(s):** TTG Studios + Sunset Sound, LA
- **Focus:** Cale-out / Doug Yule-in lineup change; the "closet mix" (intentionally lo-fi mix Reed favored); acoustic approach vs the earlier feedback aesthetic; "Pale Blue Eyes" intimate production
- **Sources:** [Wikipedia: The Velvet Underground (album)](https://en.wikipedia.org/wiki/The_Velvet_Underground_(album)); Lou Reed interview archives
- **Tags:** `velvet-underground`, `doug-yule`, `closet-mix`, `late-vu`, `1969`, `intimate-recording`

#### 28. `lou-reed-transformer`
- **Album:** Lou Reed — *Transformer* (1972)
- **Producer(s):** David Bowie + Mick Ronson
- **Studio(s):** Trident Studios, London
- **Focus:** Bowie's role as producer of his hero; Ronson's string-and-guitar arrangements; Herbie Flowers' double-bass-line on "Walk on the Wild Side" (acoustic + electric overdubs); the glam transformation of Reed
- **Sources:** [Wikipedia: Transformer](https://en.wikipedia.org/wiki/Transformer_(Lou_Reed_album)); [SOS Classic Tracks search "Walk on the Wild Side"](https://www.soundonsound.com); Herbie Flowers interviews on the bass-line
- **Tags:** `lou-reed`, `bowie`, `mick-ronson`, `transformer`, `trident-studios`, `herbie-flowers`, `glam`

#### 29. `bowie-ziggy-stardust`
- **Album:** David Bowie — *The Rise and Fall of Ziggy Stardust and the Spiders from Mars* (1972)
- **Producer(s):** David Bowie + Ken Scott
- **Studio(s):** Trident Studios, London
- **Focus:** The glam concept-album template; Mick Ronson's guitar arrangements; Woody Woodmansey's drum sound; Trident piano "you've heard on every Bowie record" use; Ken Scott's engineering approach
- **Sources:** [Wikipedia: Ziggy Stardust](https://en.wikipedia.org/wiki/The_Rise_and_Fall_of_Ziggy_Stardust_and_the_Spiders_from_Mars); [Sound on Sound: Ken Scott interview](https://www.soundonsound.com) (search "Ken Scott"); Ken Scott's *Abbey Road to Ziggy Stardust* book reference
- **Tags:** `bowie`, `ken-scott`, `mick-ronson`, `ziggy-stardust`, `trident-studios`, `glam-rock`, `concept-album`

#### 30. `television-marquee-moon`
- **Album:** Television — *Marquee Moon* (1977)
- **Producer(s):** Andy Johns + Tom Verlaine
- **Studio(s):** A&R Studios, NYC
- **Focus:** Twin-guitar architecture (Verlaine + Richard Lloyd); the "live in the room" tracking approach; the title track's 10-minute structure; CBGB scene context with deliberate art-rock production refusal
- **Sources:** [Wikipedia: Marquee Moon](https://en.wikipedia.org/wiki/Marquee_Moon); Tom Verlaine interview archives; Andy Johns retrospective
- **Tags:** `television`, `tom-verlaine`, `richard-lloyd`, `andy-johns`, `marquee-moon`, `cbgb`, `twin-guitar`

---

### Batch AL7 — Art-Rock B

#### 31. `wire-pink-flag`
- **Album:** Wire — *Pink Flag* (1977)
- **Producer(s):** Mike Thorne
- **Studio(s):** Advision Studios, London
- **Focus:** 21-track 35-minute minimalist punk template; "compose-by-removal" philosophy (every track strips an element); Thorne's role as producer plus EMI's surprising license
- **Sources:** [Wikipedia: Pink Flag](https://en.wikipedia.org/wiki/Pink_Flag); Wire band interviews; Mike Thorne retrospective archives
- **Tags:** `wire`, `mike-thorne`, `pink-flag`, `advision-studios`, `minimalist-punk`, `compose-by-removal`

#### 32. `they-might-be-giants-lincoln`
- **Album:** They Might Be Giants — *Lincoln* (1988)
- **Producer(s):** TMBG + Bill Krauss
- **Studio(s):** Various NYC small studios
- **Focus:** The Dial-A-Song bedroom-tape origin extending to LP form; accordion + drum-machine arrangements; the John Henry transition from later work; lyrical density vs. pop accessibility
- **Sources:** [Wikipedia: Lincoln (album)](https://en.wikipedia.org/wiki/Lincoln_(They_Might_Be_Giants_album)); John Flansburgh interview archives
- **Tags:** `they-might-be-giants`, `tmbg`, `lincoln`, `dial-a-song`, `accordion`, `drum-machine`, `indie-pop`

#### 33. `depeche-mode-violator`
- **Album:** Depeche Mode — *Violator* (1990)
- **Producer(s):** Flood (Mark Ellis) + Alan Wilder
- **Studio(s):** Logic Studios + Puk Recording Studios + Master Rock Studios, etc.
- **Focus:** Industrial-pop production; Alan Wilder's sound-design role; sampling found percussion sources; "Enjoy the Silence" arrangement (originally a slow ballad reworked); Synclavier use
- **Sources:** [Wikipedia: Violator](https://en.wikipedia.org/wiki/Violator_(album)); [Sound on Sound: Depeche Mode features](https://www.soundonsound.com) (search "Depeche Mode Violator"); Flood interview archives
- **Tags:** `depeche-mode`, `flood`, `alan-wilder`, `violator`, `synclavier`, `industrial-pop`, `synth-pop`

#### 34. `kate-bush-hounds-of-love`
- **Album:** Kate Bush — *Hounds of Love* (1985)
- **Producer(s):** Kate Bush
- **Studio(s):** Wickham Farm Home Studio (Bush's own 48-track studio)
- **Focus:** Self-production at her own home studio; Fairlight CMI as compositional engine; the "Ninth Wave" suite (side B); "Running Up That Hill" Fairlight programming; the rare-female-self-produced-pop-record context
- **Sources:** [Wikipedia: Hounds of Love](https://en.wikipedia.org/wiki/Hounds_of_Love); [Sound on Sound: Kate Bush Hounds of Love](https://www.soundonsound.com/people/kate-bush) (search "Kate Bush"); Fairlight CMI history articles
- **Tags:** `kate-bush`, `hounds-of-love`, `fairlight-cmi`, `home-studio`, `self-production`, `concept-suite`

#### 35. `beatles-white-album`
- **Album:** The Beatles — *The Beatles (White Album)* (1968)
- **Producer(s):** George Martin
- **Studio(s):** EMI Studios (Abbey Road) + Trident Studios
- **Focus:** The faction-split sessions (members tracking separately); 8-track recording at Trident; Geoff Emerick's mid-album departure; "Helter Skelter" volume / "Revolution 9" sound collage; minimal-engineer-overdub vs *Sgt. Pepper* maximalism
- **Sources:** [Wikipedia: The Beatles (album)](https://en.wikipedia.org/wiki/The_Beatles_(album)); Lewisohn's *Recording Sessions* book reference; Geoff Emerick's *Here, There and Everywhere* memoir
- **Tags:** `beatles`, `white-album`, `george-martin`, `geoff-emerick`, `trident-studios`, `faction-split`, `8-track`

---

### Batch AL8 — Punk A

#### 36. `bad-brains-1982`
- **Album:** Bad Brains — *Bad Brains* (yellow tape, 1982)
- **Producer(s):** Jay Dublee
- **Studio(s):** 171-A Studio, NYC
- **Focus:** Hardcore + reggae hybrid; recording on a tight budget; H.R. vocal style; the genre-defining DC hardcore template (before Minor Threat went bigger); Earl Hudson's drums
- **Sources:** [Wikipedia: Bad Brains (album)](https://en.wikipedia.org/wiki/Bad_Brains_(album)); fanzine archives; Mark Andersen / Mark Jenkins's *Dance of Days* book reference
- **Tags:** `bad-brains`, `hardcore-punk`, `reggae-influence`, `dc-hardcore`, `1982`, `171-a-studio`

#### 37. `dead-kennedys-plastic-surgery-disasters`
- **Album:** Dead Kennedys — *Plastic Surgery Disasters* (1982)
- **Producer(s):** Dead Kennedys + Thom Wilson
- **Studio(s):** Mobius Music Recording, San Francisco
- **Focus:** The Bay Area hardcore sound; Jello Biafra vocal approach; East Bay Ray's surf-derived guitar tone; the longer-than-debut song structures; political-art-punk template
- **Sources:** [Wikipedia: Plastic Surgery Disasters](https://en.wikipedia.org/wiki/Plastic_Surgery_Disasters); fanzine interview archives; East Bay Ray guitar-tone interviews
- **Tags:** `dead-kennedys`, `jello-biafra`, `east-bay-ray`, `bay-area-hardcore`, `psd`, `political-punk`

#### 38. `misfits-earth-ad`
- **Album:** The Misfits — *Earth A.D. / Wolf's Blood* (1983)
- **Producer(s):** Glenn Danzig + Eddie Stasium
- **Studio(s):** Ultra Sonic Studios, Long Island
- **Focus:** The faster-darker Misfits late-period shift; Eddie Stasium's hard-rock production sensibility brought to hardcore; Robo's drumming; the album that defined the band's metal-influenced final form
- **Sources:** [Wikipedia: Earth A.D./Wolfs Blood](https://en.wikipedia.org/wiki/Earth_A.D./Wolfs_Blood); Misfits fanzine / band-history archives
- **Tags:** `misfits`, `glenn-danzig`, `earth-ad`, `eddie-stasium`, `hardcore-metal-bridge`

#### 39. `misfits-static-age`
- **Album:** The Misfits — *Static Age* (1996, recorded 1977–78)
- **Producer(s):** Dave Achelis + The Misfits
- **Studio(s):** C.I. Recording Studios, NYC
- **Focus:** The lost-and-found archival release; original recordings from before *Earth A.D.*; the punk-with-fifties-melody template (Danzig's vocal melodicism); how the album finally reached release in 1996
- **Sources:** [Wikipedia: Static Age](https://en.wikipedia.org/wiki/Static_Age); Glenn Danzig interview archives on the recovery
- **Tags:** `misfits`, `static-age`, `1977-78`, `archival-release`, `danzig`, `melodic-punk`

#### 40. `clash-london-calling`
- **Album:** The Clash — *London Calling* (1979)
- **Producer(s):** Guy Stevens
- **Studio(s):** Wessex Sound Studios, London
- **Focus:** Guy Stevens' notorious chaotic production methodology (smashing chairs, swinging from rafters); double-album genre expansion (rockabilly, reggae, jazz, pop); Mick Jones' arrangement role; the cover-as-Elvis-tribute
- **Sources:** [Wikipedia: London Calling](https://en.wikipedia.org/wiki/London_Calling); [Sound on Sound: Classic Tracks "London Calling"](https://www.soundonsound.com) (search); Joe Strummer biographical references
- **Tags:** `the-clash`, `london-calling`, `guy-stevens`, `wessex-studios`, `punk-rock`, `double-album`, `genre-expansion`

---

### Batch AL9 — Punk B + Post-Hardcore

#### 41. `slits-cut`
- **Album:** The Slits — *Cut* (1979)
- **Producer(s):** Dennis Bovell
- **Studio(s):** Ridge Farm Studio + others, UK
- **Focus:** Dub-punk hybrid; Bovell's UK reggae production approach applied to a post-punk band; Ari Up vocal style; the all-women lineup (Viv Albertine, Tessa Pollitt, Palmolive); subverting punk's macho production aesthetic
- **Sources:** [Wikipedia: Cut (The Slits album)](https://en.wikipedia.org/wiki/Cut_(The_Slits_album)); Dennis Bovell production interviews; Viv Albertine's *Clothes, Clothes, Clothes* memoir
- **Tags:** `the-slits`, `cut`, `dennis-bovell`, `dub-punk`, `viv-albertine`, `post-punk`, `women-in-rock`

#### 42. `violent-femmes-debut`
- **Album:** Violent Femmes — *Violent Femmes* (1983)
- **Producer(s):** Mark Van Hecke
- **Studio(s):** Castle Recording, Lake Geneva, Wisconsin
- **Focus:** Acoustic-punk minimalism (no electric guitar / no traditional kit on most tracks); Brian Ritchie acoustic bass guitar; Victor DeLorenzo's "tranceaphone" (snare-on-a-stick); Gordon Gano's voice; the suburban-Milwaukee origin
- **Sources:** [Wikipedia: Violent Femmes (album)](https://en.wikipedia.org/wiki/Violent_Femmes_(album)); Violent Femmes interview archives
- **Tags:** `violent-femmes`, `acoustic-punk`, `mark-van-hecke`, `1983`, `tranceaphone`, `wisconsin`

#### 43. `fugazi-repeater`
- **Album:** Fugazi — *Repeater* (1990)
- **Producer(s):** Fugazi + Ted Niceley
- **Studio(s):** Inner Ear Studios, Arlington VA (Don Zientara engineering)
- **Focus:** Don Zientara's Inner Ear engineering aesthetic; Fugazi's DIY/Dischord ethos applied to production; the dual-guitar-and-shouted-vocal architecture; the politics around recording costs ($5 shows / $10 records)
- **Sources:** [Wikipedia: Repeater](https://en.wikipedia.org/wiki/Repeater_(Fugazi_album)); Don Zientara interview archives; Ian MacKaye Dischord oral histories
- **Tags:** `fugazi`, `repeater`, `inner-ear-studios`, `don-zientara`, `dischord`, `post-hardcore`, `dc-scene`

#### 44. `drive-like-jehu-yank-crime`
- **Album:** Drive Like Jehu — *Yank Crime* (1994)
- **Producer(s):** Mark Trombino + Drive Like Jehu
- **Studio(s):** Westbeach Recorders, Hollywood
- **Focus:** Mark Trombino's post-hardcore production aesthetic; John Reis (Rocket from the Crypt overlap) + Rick Froberg vocal interplay; mathematical guitar parts; the "post-hardcore" template that influenced At the Drive-In etc.
- **Sources:** [Wikipedia: Yank Crime](https://en.wikipedia.org/wiki/Yank_Crime); Mark Trombino interview archives
- **Tags:** `drive-like-jehu`, `mark-trombino`, `yank-crime`, `post-hardcore`, `john-reis`, `rick-froberg`

#### 45. `daughters-you-wont-get-what-you-want`
- **Album:** Daughters — *You Won't Get What You Want* (2018)
- **Producer(s):** Daughters + Seth Manchester
- **Studio(s):** Machines with Magnets, Pawtucket RI
- **Focus:** Noise-rock resurgence; Alexis Marshall vocal approach; the long-gap-return album context; cohesive album-as-statement vs noise-album-as-chaos; cited as one of 2018's best
- **Sources:** [Wikipedia: You Won't Get What You Want](https://en.wikipedia.org/wiki/You_Won%27t_Get_What_You_Want); Daughters / Seth Manchester interview archives
- **Tags:** `daughters`, `noise-rock`, `seth-manchester`, `2018`, `alexis-marshall`, `machines-with-magnets`

---

### Batch AL10 — Electronic A

#### 46. `portishead-dummy`
- **Album:** Portishead — *Dummy* (1994)
- **Producer(s):** Geoff Barrow + Adrian Utley + Portishead
- **Studio(s):** Coach House Studios, Bristol + others
- **Focus:** Trip-hop foundational album; Geoff Barrow's MPC sampling philosophy (lifting vinyl-snippet textures); Adrian Utley's guitar/keys role; Beth Gibbons vocal approach; the Bristol sound's roots
- **Sources:** [Wikipedia: Dummy](https://en.wikipedia.org/wiki/Dummy_(album)); [Sound on Sound: Portishead Dummy](https://www.soundonsound.com) (search "Portishead"); Geoff Barrow / Adrian Utley interview archives
- **Tags:** `portishead`, `dummy`, `geoff-barrow`, `adrian-utley`, `trip-hop`, `bristol-sound`, `mpc-sampling`

#### 47. `squarepusher-hard-normal-daddy`
- **Album:** Squarepusher — *Hard Normal Daddy* (1997)
- **Producer(s):** Tom Jenkinson
- **Studio(s):** Self-recorded
- **Focus:** Drum-and-bass-meets-jazz-fusion; live-bass + programmed-drums hybrid; the Warp Records "Artificial Intelligence" lineage; jazz-chord vocabulary applied to IDM
- **Sources:** [Wikipedia: Hard Normal Daddy](https://en.wikipedia.org/wiki/Hard_Normal_Daddy); Tom Jenkinson interview archives; Warp Records history
- **Tags:** `squarepusher`, `tom-jenkinson`, `hard-normal-daddy`, `warp-records`, `idm`, `jazz-drum-and-bass`

#### 48. `daft-punk-discovery`
- **Album:** Daft Punk — *Discovery* (2001)
- **Producer(s):** Daft Punk (Thomas Bangalter + Guy-Manuel de Homem-Christo)
- **Studio(s):** Daft House (Bangalter's home studio)
- **Focus:** Sample-and-disco hybrid (rooted in late-70s/80s sources); vocoder/talkbox vocal aesthetic; "One More Time" Eddie Johns sample; the album-as-anime-soundtrack concept; pre-streaming peak French Touch
- **Sources:** [Wikipedia: Discovery](https://en.wikipedia.org/wiki/Discovery_(Daft_Punk_album)); [WhoSampled: Discovery](https://www.whosampled.com/album/Daft-Punk/Discovery/); SOS feature on French Touch production
- **Tags:** `daft-punk`, `discovery`, `bangalter`, `homem-christo`, `french-touch`, `vocoder`, `sample-disco`

#### 49. `death-grips-the-money-store`
- **Album:** Death Grips — *The Money Store* (2012)
- **Producer(s):** Zach Hill + Andy "Flatlander" Morin
- **Studio(s):** The Money Store (band's collective name for their setup)
- **Focus:** Aggressive electronic-rap-noise hybrid; Zach Hill's drum-as-noise approach; MC Ride vocal distortion; "Get Got" production; Epic Records' surprised release
- **Sources:** [Wikipedia: The Money Store](https://en.wikipedia.org/wiki/The_Money_Store); Pitchfork retrospective; Zach Hill interview archives
- **Tags:** `death-grips`, `the-money-store`, `zach-hill`, `flatlander`, `electronic-noise-rap`, `mc-ride`

---

### Batch AL11 — Electronic B / Pop-Experimental

#### 50. `charli-xcx-charli`
- **Album:** Charli XCX — *Charli* (2019)
- **Producer(s):** A.G. Cook + multiple
- **Studio(s):** Various, including A.G. Cook's setup
- **Focus:** Pre-*Brat* hyperpop era; the guest-heavy feature album; Cook's production lineage continuing from earlier mixtapes; comparison to *Pop 2* (2017); "Gone" with Christine and the Queens production
- **Sources:** [Wikipedia: Charli (album)](https://en.wikipedia.org/wiki/Charli_(album)); A.G. Cook production interview archives; existing corpus AESTHETIC-RESEARCH-PLAN.md
- **Tags:** `charli-xcx`, `ag-cook`, `charli`, `2019`, `hyperpop`, `pre-brat`

#### 51. `charli-xcx-brat`
- **Album:** Charli XCX — *BRAT* (2024)
- **Producer(s):** A.G. Cook + George Daniel + Finn Keane + Cirkut
- **Studio(s):** Various
- **Focus:** The "tight collection of sounds" minimalism-as-maximalism; London illegal-rave scene as touchstone; the cultural-phenomenon trajectory; specific production-press coverage in 2024
- **Sources:** [Wikipedia: Brat (album)](https://en.wikipedia.org/wiki/Brat_(album)); [Grammy.com Brat feature](https://www.grammy.com/news/charli-xcx-brat-songs-albums-myspace-hyperpop); [MIDiA Research](https://www.midiaresearch.com/case-studies/how-charli-xcx-leveraged-the-hyperpop-scene-into-a-global-movement); reuse from AESTHETIC plan
- **Tags:** `charli-xcx`, `brat`, `ag-cook`, `george-daniel`, `2024`, `rave-revival`

#### 52. `spellling-the-turning-wheel`
- **Album:** Spellling — *The Turning Wheel* (2021)
- **Producer(s):** Chrystia Cabral (Spellling)
- **Studio(s):** Self-recorded
- **Focus:** Maximalist art-pop; orchestral arrangement on a bedroom-recording budget; the 31-musician ensemble approach; vocal layering and storytelling
- **Sources:** [Wikipedia: The Turning Wheel](https://en.wikipedia.org/wiki/The_Turning_Wheel); Pitchfork retrospective; Spellling interviews via Pitchfork/Aquarium Drunkard
- **Tags:** `spellling`, `the-turning-wheel`, `art-pop`, `bedroom-orchestra`, `chrystia-cabral`, `2021`

#### 53. `lingua-ignota-sinner-get-ready`
- **Album:** Lingua Ignota — *SINNER GET READY* (2021)
- **Producer(s):** Kristin Hayter + Seth Manchester
- **Studio(s):** Various
- **Focus:** Appalachian-folk-meets-industrial; self-recorded vocal-and-piano core; Hayter's classical-trained voice over harsh textures; the Pennsylvania-folk-instrumentation context (banjo, hammered dulcimer)
- **Sources:** [Wikipedia: Sinner Get Ready](https://en.wikipedia.org/wiki/Sinner_Get_Ready); Lingua Ignota interview archives
- **Tags:** `lingua-ignota`, `kristin-hayter`, `sinner-get-ready`, `industrial-folk`, `seth-manchester`, `2021`

#### 54. `threebrain-weeeeee`
- **Album:** Threebrain — *Weeeeee!* (2001)
- **Producer(s):** Matt "Threebrain" Wilson
- **Studio(s):** Bedroom / home-made
- **Focus:** Outsider / Flash-era cult album; the way the album spread via early-internet animation culture; the homemade-on-a-PC aesthetic; **HALLUCINATION RISK — keep file short and verified-only**
- **Sources:** [Wikipedia: Threebrain](https://en.wikipedia.org/wiki/Threebrain) (verify exists); MetaFilter / Newgrounds-era archives; do not invent
- **Tags:** `threebrain`, `outsider`, `2001`, `flash-era`, `cult-album`, `low-doc`

---

### Batch AL12 — Bob Dylan Folk Cycle

#### 55. `dylan-freewheelin`
- **Album:** Bob Dylan — *The Freewheelin' Bob Dylan* (1963)
- **Producer(s):** John Hammond
- **Studio(s):** Columbia Studio A, NYC
- **Focus:** Acoustic-folk recording-as-document; live-to-tape with minimal overdubs; the Dylan-Suze Rotolo cover-photo story; "Blowin' in the Wind" session; protest-song era opening
- **Sources:** [Wikipedia: Freewheelin'](https://en.wikipedia.org/wiki/The_Freewheelin%27_Bob_Dylan); John Hammond's *On Record* memoir; Clinton Heylin's *Behind the Shades* biography
- **Tags:** `bob-dylan`, `john-hammond`, `freewheelin`, `1963`, `acoustic-folk`, `columbia-studio-a`

#### 56. `dylan-times-they-are-a-changin`
- **Album:** Bob Dylan — *The Times They Are A-Changin'* (1964)
- **Producer(s):** Tom Wilson
- **Studio(s):** Columbia Studio A, NYC
- **Focus:** Late acoustic Dylan; Tom Wilson taking over from Hammond; protest-song peak; "When the Ship Comes In" / "The Lonesome Death of Hattie Carroll" topical songs; the album that closes the acoustic chapter
- **Sources:** [Wikipedia: The Times They Are A-Changin' (album)](https://en.wikipedia.org/wiki/The_Times_They_Are_a-Changin%27_(album)); Tom Wilson interview archives
- **Tags:** `bob-dylan`, `tom-wilson`, `times-they-are-a-changin`, `1964`, `acoustic-folk`, `protest-songs`

#### 57. `dylan-highway-61-revisited`
- **Album:** Bob Dylan — *Highway 61 Revisited* (1965)
- **Producer(s):** Bob Johnston + Tom Wilson
- **Studio(s):** Columbia Studio A, NYC
- **Focus:** The electric turn; "Like a Rolling Stone" session (Al Kooper organ accident); Mike Bloomfield guitar; Bob Johnston taking over mid-album; the 6-minute single revolution
- **Sources:** [Wikipedia: Highway 61 Revisited](https://en.wikipedia.org/wiki/Highway_61_Revisited); Greil Marcus's *Like a Rolling Stone* book; Al Kooper's *Backstage Passes & Backstabbing Bastards* memoir
- **Tags:** `bob-dylan`, `bob-johnston`, `tom-wilson`, `al-kooper`, `mike-bloomfield`, `highway-61`, `electric-dylan`

#### 58. `dylan-blonde-on-blonde`
- **Album:** Bob Dylan — *Blonde on Blonde* (1966)
- **Producer(s):** Bob Johnston
- **Studio(s):** Columbia Music Row Studios, Nashville
- **Focus:** The Nashville sessions; "thin wild mercury sound" Dylan's self-description; The Hawks (later The Band) backing; Charlie McCoy's multi-instrumentalism; the double-album shape
- **Sources:** [Wikipedia: Blonde on Blonde](https://en.wikipedia.org/wiki/Blonde_on_Blonde); Sean Wilentz's *Bob Dylan in America*; Bob Johnston interviews
- **Tags:** `bob-dylan`, `bob-johnston`, `nashville`, `blonde-on-blonde`, `the-hawks`, `1966`, `thin-wild-mercury`

---

### Batch AL13 — Folk / Soul / Indie

#### 59. `nina-simone-sings-the-blues`
- **Album:** Nina Simone — *Sings the Blues* (1967)
- **Producer(s):** Danny Davis
- **Studio(s):** RCA Studios, NYC
- **Focus:** Simone's RCA-era; "I Put a Spell on You" / "Backlash Blues"; small-combo session arrangement; piano-led arrangements; Simone's classical training emerging through blues idiom
- **Sources:** [Wikipedia: Nina Simone Sings the Blues](https://en.wikipedia.org/wiki/Nina_Simone_Sings_the_Blues); Nina Simone biographies (Alan Light's *What Happened, Miss Simone?*)
- **Tags:** `nina-simone`, `sings-the-blues`, `rca-studios`, `1967`, `danny-davis`, `blues`, `piano-led`

#### 60. `belle-and-sebastian-sinister`
- **Album:** Belle and Sebastian — *If You're Feeling Sinister* (1996)
- **Producer(s):** Tony Doogan
- **Studio(s):** CAVA Studios, Glasgow
- **Focus:** Indie-pop production restraint; the £1000 budget aesthetic; Stuart Murdoch's intimate vocal approach; the 7-piece band arrangement; the Scottish indie-pop template
- **Sources:** [Wikipedia: If You're Feeling Sinister](https://en.wikipedia.org/wiki/If_You're_Feeling_Sinister); Tony Doogan interview archives; Stuart Murdoch's *The Celestial Cafe* book reference
- **Tags:** `belle-and-sebastian`, `if-youre-feeling-sinister`, `tony-doogan`, `cava-studios`, `scottish-indie`, `1996`

#### 61. `microphones-the-glow-pt-2`
- **Album:** The Microphones — *The Glow, Pt. 2* (2001)
- **Producer(s):** Phil Elverum
- **Studio(s):** The Dub Narcotic Studio, Olympia WA (K Records)
- **Focus:** Self-recorded home aesthetic; Elverum's experimental tape-manipulation; K Records / Calvin Johnson context; the Elverum production lineage to Mount Eerie
- **Sources:** [Wikipedia: The Glow Pt. 2](https://en.wikipedia.org/wiki/The_Glow_Pt._2); Phil Elverum interview archives (Pitchfork, Aquarium Drunkard)
- **Tags:** `the-microphones`, `phil-elverum`, `the-glow-pt-2`, `dub-narcotic`, `k-records`, `home-recording`, `2001`

#### 62. `marvin-gaye-whats-going-on`
- **Album:** Marvin Gaye — *What's Going On* (1971)
- **Producer(s):** Marvin Gaye
- **Studio(s):** Hitsville USA + Golden World Studio, Detroit
- **Focus:** Gaye's self-production after the Motown system; James Jamerson bass on "What's Going On"; multi-tracked overlapping-vocal aesthetic; the political/spiritual concept-album rebellion against Berry Gordy
- **Sources:** [Wikipedia: What's Going On (album)](https://en.wikipedia.org/wiki/What%27s_Going_On_(Marvin_Gaye_album)); Ben Edmonds' *What's Going On book*; SOS Classic Tracks search
- **Tags:** `marvin-gaye`, `motown`, `whats-going-on`, `hitsville-usa`, `james-jamerson`, `self-production`, `1971`

---

### Batch AL14 — Pop-Rock / Stadium

#### 63. `led-zeppelin-physical-graffiti`
- **Album:** Led Zeppelin — *Physical Graffiti* (1975)
- **Producer(s):** Jimmy Page
- **Studio(s):** Headley Grange + Olympic Studios + Ronnie Lane's Mobile Studio
- **Focus:** Double album mixing old + new material; "Kashmir" arrangement; Page's production approach to ambience; Bonham's drum sound at Headley Grange; the mobile-studio era
- **Sources:** [Wikipedia: Physical Graffiti](https://en.wikipedia.org/wiki/Physical_Graffiti); Andy Johns interview archives; Jimmy Page production interviews
- **Tags:** `led-zeppelin`, `jimmy-page`, `physical-graffiti`, `headley-grange`, `bonham`, `mobile-studio`, `1975`

#### 64. `pink-floyd-animals`
- **Album:** Pink Floyd — *Animals* (1977)
- **Producer(s):** Pink Floyd
- **Studio(s):** Britannia Row Studios, London
- **Focus:** Waters-era concept album; "Pigs" / "Dogs" / "Sheep" extended structures; Britannia Row in-house studio context; the post-*Wish You Were Here* shift; Snowy White / David Gilmour guitar interplay
- **Sources:** [Wikipedia: Animals (Pink Floyd album)](https://en.wikipedia.org/wiki/Animals_(Pink_Floyd_album)); Pink Floyd biographies; Britannia Row history
- **Tags:** `pink-floyd`, `animals`, `roger-waters`, `david-gilmour`, `britannia-row`, `1977`, `concept-album`

#### 65. `pink-floyd-the-wall`
- **Album:** Pink Floyd — *The Wall* (1979)
- **Producer(s):** Bob Ezrin + David Gilmour + Roger Waters
- **Studio(s):** Super Bear Studios + Britannia Row + Producers Workshop
- **Focus:** Ezrin's production role bringing pop sensibility to a sprawling concept; "Another Brick in the Wall Part 2" disco-influenced rhythm; multiple-studio recording logistics; the album-becoming-movie context
- **Sources:** [Wikipedia: The Wall](https://en.wikipedia.org/wiki/The_Wall); Bob Ezrin interview archives; Roger Waters interviews
- **Tags:** `pink-floyd`, `bob-ezrin`, `the-wall`, `roger-waters`, `david-gilmour`, `concept-album`, `1979`

#### 66. `prince-purple-rain`
- **Album:** Prince — *Purple Rain* (1984)
- **Producer(s):** Prince + The Revolution
- **Studio(s):** Sunset Sound, LA + Warehouse District, Minneapolis (live recording for some tracks)
- **Focus:** Live-recorded tracks ("Purple Rain" title track) blended with studio production; The Revolution as band; Prince's multi-instrumentalism; the film-album-tour convergence
- **Sources:** [Wikipedia: Purple Rain](https://en.wikipedia.org/wiki/Purple_Rain_(album)); Susan Rogers' interviews on Prince's production; Alan Light's *Let's Go Crazy* book
- **Tags:** `prince`, `the-revolution`, `purple-rain`, `sunset-sound`, `susan-rogers`, `1984`, `live-recording-blend`

#### 67. `janet-jackson-velvet-rope`
- **Album:** Janet Jackson — *The Velvet Rope* (1997)
- **Producer(s):** Jimmy Jam + Terry Lewis + Janet Jackson
- **Studio(s):** Flyte Tyme Studios, Minneapolis
- **Focus:** Late-Jam-and-Lewis pop production; deeply personal album content; "Together Again" arrangement; Jam & Lewis's production lineage to Janet's solo career
- **Sources:** [Wikipedia: The Velvet Rope](https://en.wikipedia.org/wiki/The_Velvet_Rope); Jimmy Jam interview archives; Flyte Tyme studio history
- **Tags:** `janet-jackson`, `jimmy-jam`, `terry-lewis`, `flyte-tyme`, `velvet-rope`, `1997`, `personal-pop`

---

### Batch AL15 — Prog / Jazz Fusion / Experimental

#### 68. `mingus-black-saint`
- **Album:** Charles Mingus — *The Black Saint and the Sinner Lady* (1963)
- **Producer(s):** Bob Thiele
- **Studio(s):** Van Gelder Studio (Englewood Cliffs NJ)
- **Focus:** Impulse-era jazz production; Mingus's "ethnic folk-dance suite" concept; Bob Hammer's transcription role; Charlie Mariano alto sax; the through-composed-jazz-as-album-statement template
- **Sources:** [Wikipedia: Black Saint and the Sinner Lady](https://en.wikipedia.org/wiki/The_Black_Saint_and_the_Sinner_Lady); Mingus biographies; Van Gelder Studio history
- **Tags:** `charles-mingus`, `impulse-records`, `bob-thiele`, `van-gelder`, `1963`, `jazz-suite`, `through-composed`

#### 69. `king-crimson-in-the-court`
- **Album:** King Crimson — *In the Court of the Crimson King* (1969)
- **Producer(s):** King Crimson (+ Tony Clarke uncredited)
- **Studio(s):** Wessex Sound Studios, London
- **Focus:** Prog template establishment; "21st Century Schizoid Man" production; Mellotron sound (Ian McDonald); Robert Fripp's guitar approach; Greg Lake vocals
- **Sources:** [Wikipedia: In the Court of the Crimson King](https://en.wikipedia.org/wiki/In_the_Court_of_the_Crimson_King); Robert Fripp interview archives; Ian McDonald Mellotron interviews
- **Tags:** `king-crimson`, `robert-fripp`, `in-the-court`, `wessex-studios`, `mellotron`, `prog-rock`, `1969`

#### 70. `mahavishnu-inner-mounting-flame`
- **Album:** Mahavishnu Orchestra — *The Inner Mounting Flame* (1971)
- **Producer(s):** John McLaughlin
- **Studio(s):** Criteria Recording Studios, Miami
- **Focus:** Jazz-fusion virtuosity; McLaughlin's double-necked Gibson; Billy Cobham's drum approach; Jan Hammer / Jerry Goodman / Rick Laird ensemble; the 1971 jazz-rock peak
- **Sources:** [Wikipedia: The Inner Mounting Flame](https://en.wikipedia.org/wiki/The_Inner_Mounting_Flame); John McLaughlin interview archives; Billy Cobham drum-tone interviews
- **Tags:** `mahavishnu-orchestra`, `john-mclaughlin`, `inner-mounting-flame`, `billy-cobham`, `criteria-studios`, `jazz-fusion`, `1971`

#### 71. `earth-2`
- **Album:** Earth — *Earth 2: Special Low Frequency Version* (1993)
- **Producer(s):** Dylan Carlson + Earth
- **Studio(s):** Avast Studios, Seattle (Stuart Hallerman engineering)
- **Focus:** Drone-metal foundational album; ~70-minute three-track structure; Dylan Carlson's heavily detuned guitars; the album that begat Sunn O))) and the drone-metal genre
- **Sources:** [Wikipedia: Earth 2](https://en.wikipedia.org/wiki/Earth_2_(album)); Dylan Carlson interview archives; Sub Pop history
- **Tags:** `earth`, `dylan-carlson`, `earth-2`, `drone-metal`, `sub-pop`, `1993`, `avast-studios`

#### 72. `godspeed-lift-yr-skinny-fists`
- **Album:** Godspeed You! Black Emperor — *Lift Yr. Skinny Fists Like Antennas to Heaven* (2000)
- **Producer(s):** Godspeed You! Black Emperor (+ Daryl Smith, Howard Bilerman)
- **Studio(s):** Hotel2Tango, Montreal
- **Focus:** Post-rock chamber-epic; multi-track field-recording incorporation; 4-side double-LP structure (each 20-minute side a continuous piece); Hotel2Tango's role as Montreal scene hub
- **Sources:** [Wikipedia: Lift Yr. Skinny Fists](https://en.wikipedia.org/wiki/Lift_Yr._Skinny_Fists_Like_Antennas_to_Heaven); GY!BE interview archives; Hotel2Tango studio history
- **Tags:** `godspeed-you-black-emperor`, `lift-yr-skinny-fists`, `hotel2tango`, `montreal`, `post-rock`, `2000`, `chamber-epic`

---

### Batch AL16 — Shoegaze / Noise / Drone / Proto-Punk

#### 73. `swans-soundtracks-for-the-blind`
- **Album:** Swans — *Soundtracks for the Blind* (1996)
- **Producer(s):** Michael Gira
- **Studio(s):** Various
- **Focus:** Double-album late-90s Swans peak; field recordings + interview tape collages; Jarboe vocal contributions; the album that became Gira's swan-song before the 13-year hiatus
- **Sources:** [Wikipedia: Soundtracks for the Blind](https://en.wikipedia.org/wiki/Soundtracks_for_the_Blind); Michael Gira interview archives; Young God Records context
- **Tags:** `swans`, `michael-gira`, `jarboe`, `soundtracks-for-the-blind`, `young-god`, `1996`, `noise-rock`

#### 74. `swans-to-be-kind`
- **Album:** Swans — *To Be Kind* (2014)
- **Producer(s):** Michael Gira + John Congleton
- **Studio(s):** Sonic Ranch, Texas
- **Focus:** Reunion-era Swans (post-2010 reformation); John Congleton's engineering; the 2-hour album shape; "Bring the Sun / Toussaint L'Ouverture" extended composition; live-band-in-studio approach
- **Sources:** [Wikipedia: To Be Kind](https://en.wikipedia.org/wiki/To_Be_Kind); Michael Gira / John Congleton interview archives
- **Tags:** `swans`, `michael-gira`, `john-congleton`, `to-be-kind`, `sonic-ranch`, `2014`, `reunion-swans`

#### 75. `stooges-fun-house`
- **Album:** The Stooges — *Fun House* (1970)
- **Producer(s):** Don Gallucci
- **Studio(s):** Elektra Sound Recorders, LA
- **Focus:** Live-tracking-with-minimal-overdubs; Gallucci's choice to record in a live-band setup; "L.A. Blues" free-jazz finale; the album that defined proto-punk; Steve Mackay sax
- **Sources:** [Wikipedia: Fun House](https://en.wikipedia.org/wiki/Fun_House_(The_Stooges_album)); Don Gallucci interview archives; Iggy Pop autobiographies
- **Tags:** `the-stooges`, `iggy-pop`, `don-gallucci`, `fun-house`, `elektra-sound-recorders`, `1970`, `proto-punk`

#### 76. `stooges-raw-power`
- **Album:** The Stooges — *Raw Power* (1973)
- **Producer(s):** Iggy Pop (with David Bowie mix in 1973; Iggy remix in 1997)
- **Studio(s):** CBS Studios, London
- **Focus:** James Williamson guitar; Bowie's notoriously thin original mix; the 1997 Iggy remix controversy; the proto-punk-to-glam-bridge moment
- **Sources:** [Wikipedia: Raw Power](https://en.wikipedia.org/wiki/Raw_Power); Iggy Pop / James Williamson interview archives; Bowie mix vs Iggy remix coverage
- **Tags:** `the-stooges`, `iggy-pop`, `david-bowie`, `james-williamson`, `raw-power`, `cbs-studios-london`, `1973`

---

### Batch AL17 — Hard Rock / Metal

#### 77. `nirvana-nevermind`
- **Album:** Nirvana — *Nevermind* (1991)
- **Producer(s):** Butch Vig + Andy Wallace (mix)
- **Studio(s):** Sound City Studios, Van Nuys CA
- **Focus:** Butch Vig's drum production (the famous Neve console at Sound City); Andy Wallace's mix bringing pop-radio readiness; Dave Grohl's drum sound; "Smells Like Teen Spirit" arrangement; the album that ended hair-metal
- **Sources:** [Wikipedia: Nevermind](https://en.wikipedia.org/wiki/Nevermind); Butch Vig interview archives; Dave Grohl's *Sound City* documentary; Andy Wallace mix-engineering features
- **Tags:** `nirvana`, `butch-vig`, `andy-wallace`, `nevermind`, `sound-city`, `neve-console`, `1991`, `grunge`

#### 78. `metallica-master-of-puppets`
- **Album:** Metallica — *Master of Puppets* (1986)
- **Producer(s):** Flemming Rasmussen + Metallica
- **Studio(s):** Sweet Silence Studios, Copenhagen
- **Focus:** Thrash-metal production canon; multi-tracked guitar layering; James Hetfield's rhythm-guitar approach; the long-form song structures; Cliff Burton's bass (last full studio album before his death)
- **Sources:** [Wikipedia: Master of Puppets](https://en.wikipedia.org/wiki/Master_of_Puppets); Flemming Rasmussen interview archives; Mick Wall's *Metallica: Enter Night* biography
- **Tags:** `metallica`, `master-of-puppets`, `flemming-rasmussen`, `sweet-silence-studios`, `thrash-metal`, `cliff-burton`, `1986`

#### 79. `soad-toxicity`
- **Album:** System of a Down — *Toxicity* (2001)
- **Producer(s):** Rick Rubin + Daron Malakian
- **Studio(s):** Cello Studios, Hollywood
- **Focus:** Rubin's mid-period production; Daron Malakian's compositional role; Serj Tankian vocal approach; the Armenian-American cultural-political content; Greg Fidelman engineering
- **Sources:** [Wikipedia: Toxicity (album)](https://en.wikipedia.org/wiki/Toxicity_(album)); Rick Rubin production interview archives; Greg Fidelman engineering features
- **Tags:** `system-of-a-down`, `rick-rubin`, `daron-malakian`, `toxicity`, `cello-studios`, `2001`, `alt-metal`

#### 80. `mcr-black-parade`
- **Album:** My Chemical Romance — *The Black Parade* (2006)
- **Producer(s):** Rob Cavallo
- **Studio(s):** The Paramour Mansion, LA
- **Focus:** Bob-Ezrin-influenced concept-album production; the haunted-mansion recording lore; Cavallo's pop-rock production sensibility; Gerard Way's theatrical vocal approach; the post-emo-arena-rock arc
- **Sources:** [Wikipedia: The Black Parade](https://en.wikipedia.org/wiki/The_Black_Parade); Rob Cavallo interview archives; Paramour Mansion history articles
- **Tags:** `my-chemical-romance`, `rob-cavallo`, `black-parade`, `paramour-mansion`, `concept-album`, `2006`, `emo-arena-rock`

#### 81. `weezer-blue-album`
- **Album:** Weezer — *Weezer (Blue Album)* (1994)
- **Producer(s):** Ric Ocasek
- **Studio(s):** Electric Lady Studios, NYC
- **Focus:** Ocasek's Cars-production-experience applied to a power-pop band; Rivers Cuomo's songwriting approach; the geek-pop template; "Undone (The Sweater Song)" arrangement
- **Sources:** [Wikipedia: Weezer (Blue Album)](https://en.wikipedia.org/wiki/Weezer_(Blue_Album)); Ric Ocasek interview archives; Rivers Cuomo Pinkerton-era retrospectives
- **Tags:** `weezer`, `ric-ocasek`, `blue-album`, `electric-lady`, `power-pop`, `1994`, `geek-pop`

---

### Batch AL18 — Cult / Lo-fi / Late Waits + Remaining Existing-Anchor Albums

#### 82. `tom-waits-bone-machine`
- **Album:** Tom Waits — *Bone Machine* (1992)
- **Producer(s):** Tom Waits
- **Studio(s):** "Mr. Knickerbocker's room" — a cement-walled basement room (Waits' description)
- **Focus:** Cement-room recording / extreme natural reverb; percussion-as-everything ("Bonemen" wood-and-metal junk); Marc Ribot guitar continuation; "Going Out West" / "Earth Died Screaming" arrangements
- **Sources:** [Wikipedia: Bone Machine](https://en.wikipedia.org/wiki/Bone_Machine); Tom Waits interview archives (Magnet, Mojo)
- **Tags:** `tom-waits`, `bone-machine`, `cement-room`, `marc-ribot`, `1992`, `junk-percussion`

#### 83. `tom-waits-blood-money`
- **Album:** Tom Waits — *Blood Money* (2002)
- **Producer(s):** Tom Waits + Kathleen Brennan
- **Studio(s):** Prairie Sun Recording, Cotati CA
- **Focus:** Theater-album mode (composed for Robert Wilson's *Woyzeck*); Marc Ribot's continued role; Brennan's co-writing role; the chamber-orchestral arrangements; released same day as *Alice*
- **Sources:** [Wikipedia: Blood Money](https://en.wikipedia.org/wiki/Blood_Money_(Tom_Waits_album)); Waits / Brennan interview archives
- **Tags:** `tom-waits`, `blood-money`, `kathleen-brennan`, `robert-wilson`, `theater-album`, `2002`, `prairie-sun`

#### 84. `unicorns-who-will-cut-our-hair`
- **Album:** The Unicorns — *Who Will Cut Our Hair When We're Gone?* (2003)
- **Producer(s):** The Unicorns
- **Studio(s):** Hotel2Tango, Montreal
- **Focus:** Montreal indie-pop cult album; lo-fi keyboard arrangements; Alden Penner / Nicholas Thorburn songwriting; the short-lived band's only album; the Arcade Fire-adjacent Montreal scene
- **Sources:** [Wikipedia: Who Will Cut Our Hair](https://en.wikipedia.org/wiki/Who_Will_Cut_Our_Hair_When_We%27re_Gone%3F); Pitchfork retrospective; Montreal scene history articles
- **Tags:** `the-unicorns`, `who-will-cut-our-hair`, `hotel2tango`, `montreal`, `indie-pop`, `2003`, `cult-album`

#### 85. `lcd-sound-of-silver`
- **Album:** LCD Soundsystem — *Sound of Silver* (2007)
- **Producer(s):** James Murphy + The DFA
- **Studio(s):** DFA Studios (Plantain), NYC
- **Focus:** The breakthrough beyond *LCD Soundsystem*; "All My Friends" piano-led arrangement; analog-synth-into-Pro-Tools workflow; the DFA-house-built sound at this point; Pat Mahoney drumming evolution
- **Sources:** [Wikipedia: Sound of Silver](https://en.wikipedia.org/wiki/Sound_of_Silver); existing AESTHETIC plan LCD sources; James Murphy SynthHistory interview
- **Tags:** `lcd-soundsystem`, `james-murphy`, `dfa`, `sound-of-silver`, `2007`, `plantain-studios`, `dance-punk`

#### 86. `lcd-this-is-happening`
- **Album:** LCD Soundsystem — *This Is Happening* (2010)
- **Producer(s):** James Murphy
- **Studio(s):** Mansion in Los Angeles (Murphy + DFA crew rented home)
- **Focus:** The supposed-final-album (pre-2017 reunion); "Dance Yrself Clean" extended structure; mansion-as-studio setup; the album-as-farewell tour context
- **Sources:** [Wikipedia: This Is Happening](https://en.wikipedia.org/wiki/This_Is_Happening); James Murphy retrospective interviews; LCD Soundsystem oral histories
- **Tags:** `lcd-soundsystem`, `this-is-happening`, `james-murphy`, `2010`, `mansion-studio`, `dance-punk`

#### 87. `radiohead-ok-computer`
- **Album:** Radiohead — *OK Computer* (1997)
- **Producer(s):** Nigel Godrich + Radiohead
- **Studio(s):** St. Catherine's Court, Bath (Jane Seymour's manor)
- **Focus:** The manor-recording approach; Godrich's first full Radiohead production; "Paranoid Android" arrangement; the album that bridged guitar-rock to post-rock-electronic; Mellotron and ondes-martenot returning
- **Sources:** [Wikipedia: OK Computer](https://en.wikipedia.org/wiki/OK_Computer); existing Radiohead anchor sources (Happy Mag, Godrich Tumblr); Marvin's *Exit Music* book
- **Tags:** `radiohead`, `ok-computer`, `nigel-godrich`, `st-catherines-court`, `1997`, `art-rock`, `mansion-studio`

#### 88. `postal-service-give-up`
- **Album:** The Postal Service — *Give Up* (2003)
- **Producer(s):** Jimmy Tamborello + Ben Gibbard
- **Studio(s):** Tamborello's LA home + Gibbard's Seattle home (the famous mail-collaboration)
- **Focus:** The CD-R mail-collaboration workflow; Kurzweil K2000 as primary instrument; "Such Great Heights" production; Jenny Lewis features; indie-electronic template
- **Sources:** [Wikipedia: Give Up](https://en.wikipedia.org/wiki/Give_Up); [Life of the Record podcast + transcript](https://lifeoftherecord.com/the-postal-service); [MusicRadar Postal Service piece](https://www.musicradar.com/artists/bands/i-didnt-really-understand-how-any-of-it-worked-we-were-just-young-and-up-for-anything-the-postal-service-on-creating-indie-electronic-classic-give-up); existing AESTHETIC plan sources
- **Tags:** `postal-service`, `give-up`, `tamborello`, `gibbard`, `kurzweil-k2000`, `mail-collaboration`, `2003`

#### 89. `neutral-milk-hotel-aeroplane`
- **Album:** Neutral Milk Hotel — *In the Aeroplane Over the Sea* (1998)
- **Producer(s):** Robert Schneider
- **Studio(s):** Pet Sounds Studio, Denver (Schneider's studio)
- **Focus:** Mangum's surreal-Anne-Frank-themed lyrics; Schneider's "high-art Beatlesque vs lo-fi" production paradox; horn arrangements by Schneider + Scott Spillane; Julian Koster's musical-saw on "Two-Headed Boy"; the Elephant 6 collective context
- **Sources:** [Wikipedia: In the Aeroplane Over the Sea](https://en.wikipedia.org/wiki/In_the_Aeroplane_Over_the_Sea); existing AESTHETIC plan sources; Magnet Magazine Elephant 6 retrospective
- **Tags:** `neutral-milk-hotel`, `jeff-mangum`, `robert-schneider`, `aeroplane-over-the-sea`, `pet-sounds-studio`, `elephant-6`, `1998`

---

## Batch summary table

| Batch | Prompts | Files | Cluster | Est. wall time |
|---|---|---|---|---|
| AL1 | 1–5 | 5 | Phase 1 starter A | ~15 min |
| AL2 | 6–10 | 5 | Phase 1 starter B | ~15 min |
| AL3 | 11–15 | 5 | Hip-hop A | ~15 min |
| AL4 | 16–20 | 5 | Hip-hop B | ~15 min |
| AL5 | 21–25 | 5 | Hip-hop C | ~15 min |
| AL6 | 26–30 | 5 | Art-rock A | ~15 min |
| AL7 | 31–35 | 5 | Art-rock B | ~15 min |
| AL8 | 36–40 | 5 | Punk A | ~15 min |
| AL9 | 41–45 | 5 | Punk B / Post-hardcore | ~15 min |
| AL10 | 46–49 | 4 | Electronic A | ~12 min |
| AL11 | 50–54 | 5 | Electronic B / Pop-experimental | ~15 min |
| AL12 | 55–58 | 4 | Bob Dylan folk cycle | ~12 min |
| AL13 | 59–62 | 4 | Folk / Soul / Indie | ~12 min |
| AL14 | 63–67 | 5 | Pop-rock / Stadium | ~15 min |
| AL15 | 68–72 | 5 | Prog / Jazz fusion / Experimental | ~15 min |
| AL16 | 73–76 | 4 | Shoegaze / Noise / Drone / Proto-punk | ~12 min |
| AL17 | 77–81 | 5 | Hard Rock / Metal | ~15 min |
| AL18 | 82–89 | 8 | Cult + late-Waits + existing-anchor album files | ~22 min |

**Total:** 89 files. Serial: ~265 min. Parallel (4 batches at once): ~30 min wall.

---

## Post-processing checklist

After each batch completes:

- [ ] Files written to `corpus/albums/{artist-album-slug}.md`
- [ ] Front-matter includes Album/Year/Producer(s)/Studio(s)/Aesthetic-stack/Tags
- [ ] At least 8 H2 body sections per file
- [ ] Inline citations to real URLs (Wikipedia + verified production sources)
- [ ] No fabricated engineer names or studio dates
- [ ] Tags include both the album-slug AND the production-vocabulary tags
- [ ] Cross-link in artist-overview file (`corpus/artists/{artist}.md`) where existing anchor applies
- [ ] (Optional) Update `corpus/README.md` to reflect new file count
