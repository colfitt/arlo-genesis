# ARLO Albums Corpus — Batch Execution Plan

**18 batches** that together produce all 89 album-anchored seed documents. Same dispatch pattern as `AESTHETIC-SESSIONS.md` — each kickoff reads `ALBUMS-PROMPTS.md` from disk.

---

## Prerequisite

```bash
mkdir -p ~/Dev/arlo/corpus/albums
```

---

## Batch Overview

| # | Batch | Prompts | Files | Wall time |
|---|-------|---------|-------|-----------|
| AL1 | Phase 1 starter A | 1–5 | 5 | ~15 min |
| AL2 | Phase 1 starter B | 6–10 | 5 | ~15 min |
| AL3 | Hip-hop A | 11–15 | 5 | ~15 min |
| AL4 | Hip-hop B | 16–20 | 5 | ~15 min |
| AL5 | Hip-hop C | 21–25 | 5 | ~15 min |
| AL6 | Art-rock A | 26–30 | 5 | ~15 min |
| AL7 | Art-rock B | 31–35 | 5 | ~15 min |
| AL8 | Punk A | 36–40 | 5 | ~15 min |
| AL9 | Punk B / Post-hardcore | 41–45 | 5 | ~15 min |
| AL10 | Electronic A | 46–49 | 4 | ~12 min |
| AL11 | Electronic B / Pop-experimental | 50–54 | 5 | ~15 min |
| AL12 | Bob Dylan folk cycle | 55–58 | 4 | ~12 min |
| AL13 | Folk / Soul / Indie | 59–62 | 4 | ~12 min |
| AL14 | Pop-rock / Stadium | 63–67 | 5 | ~15 min |
| AL15 | Prog / Jazz fusion / Experimental | 68–72 | 5 | ~15 min |
| AL16 | Shoegaze / Noise / Drone / Proto-punk | 73–76 | 4 | ~12 min |
| AL17 | Hard Rock / Metal | 77–81 | 5 | ~15 min |
| AL18 | Cult + Late-Waits + existing-anchor album files | 82–89 | 8 | ~22 min |

**Total:** 18 batches, 89 files. Serial wall time ~265 min. Parallel (4 batches at once): ~30 min total.

---

## Suggested phased pacing

If you want to validate each wave before firing the next:

- **Day 1:** AL1 + AL2 in parallel (Phase 1 starter pack — 10 files)
- **Day 2:** AL3 + AL4 + AL5 in parallel (Hip-hop full cluster — 15 files)
- **Day 3:** AL6 + AL7 + AL8 + AL9 in parallel (Art-rock + punk — 20 files)
- **Day 4:** AL10 + AL11 + AL12 + AL13 in parallel (Electronic + folk — 18 files)
- **Day 5:** AL14 + AL15 + AL16 + AL17 + AL18 in parallel (Pop-rock + prog + shoegaze + metal + cult — 26 files)

If you trust the template after Phase 1, compress to 1–2 days by firing 4 batches at once continuously.

---

## Kickoff Messages

For each batch, paste the entire message into a fresh Claude Code chat OR dispatch as a background sub-agent. Same instruction shape across all 18 — only the prompt numbers change.

---

### Batch AL1 — Phase 1 Starter A (5 files)

```
Run albums research batch AL1 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/ALBUMS-PROMPTS.md — master album-anchored template + all 89 topic rows.
- /Users/cfitt/Dev/arlo/ALBUMS-RESEARCH-PLAN.md — strategic context (skim only).
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 5 markdown files by executing prompts #1, #2, #3, #4, #5 from ALBUMS-PROMPTS.md, in that order:

1. Prompt #1 (joy-division-unknown-pleasures) → /Users/cfitt/Dev/arlo/corpus/albums/joy-division-unknown-pleasures.md
2. Prompt #2 (my-bloody-valentine-loveless) → /Users/cfitt/Dev/arlo/corpus/albums/my-bloody-valentine-loveless.md
3. Prompt #3 (talking-heads-remain-in-light) → /Users/cfitt/Dev/arlo/corpus/albums/talking-heads-remain-in-light.md
4. Prompt #4 (beatles-abbey-road) → /Users/cfitt/Dev/arlo/corpus/albums/beatles-abbey-road.md
5. Prompt #5 (bowie-station-to-station) → /Users/cfitt/Dev/arlo/corpus/albums/bowie-station-to-station.md

FOR EACH PROMPT:
1. Read the topic row from ALBUMS-PROMPTS.md (Album/Producer/Studio/Subtopics/Sources/Tags).
2. Mentally render the master template with that row's variables.
3. Execute deep research using WebSearch and WebFetch. Start by WebFetch-ing the Wikipedia URL and any verified primary-source URL listed in the row. Then augment with WebSearch for 4–8 additional reputable sources per album.
4. Write the rendered output to the target path. The file MUST include:
   - Album-anchored front-matter (# Album Title, **Artist:**, **Year:**, **Producer(s):**, **Studio(s):**, **Scope:** album, **Source:** Deep-research synthesis (2026-05), **Aesthetic-stack relevance:**, **Tags:**)
   - 8–15 H2 body sections, each 100–250 words of dense, specific content
   - "## Cited Retrieval Topics" footer with 5–10 lowercase conversational query phrases
   - "## Sources" bibliography with markdown-link URLs

CRITICAL CONSTRAINTS:
- ALBUM-AS-ARTIFACT framing — tell the session story, not the artist biography.
- Concrete over abstract — specific gear, specific studios, specific engineers, specific dates.
- ANTI-HALLUCINATION: if you cannot verify a specific producer credit, engineer name, gear model, studio name, or session date through web research, OMIT it. Do not guess. Specific watch-outs:
  - Engineer credits for pre-1975 albums are often unclear; verify before naming
  - Brian Eno's production credit varies; check Wikipedia's "Producer:" line specifically
  - Mythologized stories (apocryphal session anecdotes) — prefer SOS / Tape Op / Mix Online over fan-forum lore
- Length: 1500–2500 words per file.
- Inline markdown link citations.
- Audience: intermediate musicians/producers.

WHEN ALL 5 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline-citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch AL2 — Phase 1 Starter B (5 files)

```
Run albums research batch AL2 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/ALBUMS-PROMPTS.md — master template + 89 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.
- /Users/cfitt/Dev/arlo/corpus/mixing/sos-inside-track-billie-eilish-bad-guy.md — existing in-corpus example of a deep-production file (for stylistic reference).

YOUR TASK:
Produce 5 markdown files by executing prompts #6, #7, #8, #9, #10 from ALBUMS-PROMPTS.md, in that order:

1. Prompt #6 (miles-davis-bitches-brew) → /Users/cfitt/Dev/arlo/corpus/albums/miles-davis-bitches-brew.md
2. Prompt #7 (radiohead-kid-a) → /Users/cfitt/Dev/arlo/corpus/albums/radiohead-kid-a.md
3. Prompt #8 (beastie-boys-pauls-boutique) → /Users/cfitt/Dev/arlo/corpus/albums/beastie-boys-pauls-boutique.md
4. Prompt #9 (bjork-vespertine) → /Users/cfitt/Dev/arlo/corpus/albums/bjork-vespertine.md
5. Prompt #10 (tom-waits-rain-dogs) → /Users/cfitt/Dev/arlo/corpus/albums/tom-waits-rain-dogs.md

[same FOR EACH / CRITICAL CONSTRAINTS / WHEN ALL FILES ARE WRITTEN body as AL1 — see AL1 for the full instruction set; this batch follows the same pattern]

Additional batch-specific instruction: for prompt #8 (Paul's Boutique), cross-check sample claims against WhoSampled.com before citing them. The Beastie Boys / Dust Brothers sample-collage has been documented to ~105 individual samples — do not invent samples.

Begin.
```

---

### Batch AL3 — Hip-Hop A (5 files: Public Enemy, Dr. Dre, Wu-Tang, Nas, GZA)

```
Run albums research batch AL3 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/ALBUMS-PROMPTS.md — master template + 89 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 5 markdown files by executing prompts #11, #12, #13, #14, #15:

1. #11 (public-enemy-it-takes-a-nation) → /Users/cfitt/Dev/arlo/corpus/albums/public-enemy-it-takes-a-nation.md
2. #12 (dr-dre-the-chronic) → /Users/cfitt/Dev/arlo/corpus/albums/dr-dre-the-chronic.md
3. #13 (wu-tang-36-chambers) → /Users/cfitt/Dev/arlo/corpus/albums/wu-tang-36-chambers.md
4. #14 (nas-illmatic) → /Users/cfitt/Dev/arlo/corpus/albums/nas-illmatic.md
5. #15 (gza-liquid-swords) → /Users/cfitt/Dev/arlo/corpus/albums/gza-liquid-swords.md

[same general instruction body as AL1]

HIP-HOP-SPECIFIC INSTRUCTION: every sample claim must be cross-checked against WhoSampled.com or another verified sample-database source before citing. Brian Coleman's *Check the Technique* (Vol 1 & 2) covers most of these albums; reference what's publicly discussed about those chapters when grounding production-specific claims.

Begin.
```

---

### Batch AL4 — Hip-Hop B (5 files: Outkast ATLiens, Lauryn Hill, Roots, Common, Outkast Stankonia)

```
Run albums research batch AL4 for ARLO.

[same context-files + general-instruction body as AL3]

YOUR TASK:
Prompts #16–#20:

1. #16 (outkast-atliens) → corpus/albums/outkast-atliens.md
2. #17 (lauryn-hill-miseducation) → corpus/albums/lauryn-hill-miseducation.md
3. #18 (roots-things-fall-apart) → corpus/albums/roots-things-fall-apart.md
4. #19 (common-like-water-for-chocolate) → corpus/albums/common-like-water-for-chocolate.md
5. #20 (outkast-stankonia) → corpus/albums/outkast-stankonia.md

[same hip-hop-specific WhoSampled instruction as AL3]

Additional note for #18 and #19: both are Soulquarians-era albums recorded at Electric Lady Studios. They cross-reference each other heavily — Questlove drums on both; the J Dilla / D'Angelo / James Poyser collective worked across both. Cross-link the two files via tags.

Begin.
```

---

### Batch AL5 — Hip-Hop C (5 files: Madvillain, Kanye, Kendrick, KSG, Clipse)

```
Run albums research batch AL5 for ARLO.

[same context-files + general-instruction body as AL3]

YOUR TASK:
Prompts #21–#25:

1. #21 (madvillain-madvillainy) → corpus/albums/madvillain-madvillainy.md
2. #22 (kanye-college-dropout) → corpus/albums/kanye-college-dropout.md
3. #23 (kendrick-to-pimp-a-butterfly) → corpus/albums/kendrick-to-pimp-a-butterfly.md
4. #24 (kids-see-ghosts-debut) → corpus/albums/kids-see-ghosts-debut.md
5. #25 (clipse-let-god-sort-em-out) → corpus/albums/clipse-let-god-sort-em-out.md

[same hip-hop-specific instructions]

Additional note for #25 (Clipse 2025): this is a recent (2025) release with less mature documentation than the older albums. Focus on what's been published in 2025 production-press coverage (Pitchfork, Stereogum, Complex). If specific session details aren't yet publicly documented, keep claims qualitative. Do NOT fabricate session details for this one.

Begin.
```

---

### Batch AL6 — Art-Rock A (5 files: VU&Nico, VU 1969, Lou Reed, Bowie Ziggy, Television)

```
Run albums research batch AL6 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #26–#30:

1. #26 (velvet-underground-and-nico) → corpus/albums/velvet-underground-and-nico.md
2. #27 (velvet-underground-1969) → corpus/albums/velvet-underground-1969.md
3. #28 (lou-reed-transformer) → corpus/albums/lou-reed-transformer.md
4. #29 (bowie-ziggy-stardust) → corpus/albums/bowie-ziggy-stardust.md
5. #30 (television-marquee-moon) → corpus/albums/television-marquee-moon.md

ART-ROCK-SPECIFIC INSTRUCTION: late-60s/early-70s engineer credits are often unclear or contested. Be especially careful about engineer-vs-producer attribution. Wikipedia's "Producer:" credit line is the citation anchor; secondary engineer credits should be backed by at least one other source.

For #28 (Transformer) and #29 (Ziggy): both involve Bowie production work, both at Trident Studios in 1972. Cross-link via studio and producer tags.

Begin.
```

---

### Batch AL7 — Art-Rock B (5 files: Wire, TMBG, Depeche, Kate Bush, Beatles White Album)

```
Run albums research batch AL7 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #31–#35:

1. #31 (wire-pink-flag) → corpus/albums/wire-pink-flag.md
2. #32 (they-might-be-giants-lincoln) → corpus/albums/they-might-be-giants-lincoln.md
3. #33 (depeche-mode-violator) → corpus/albums/depeche-mode-violator.md
4. #34 (kate-bush-hounds-of-love) → corpus/albums/kate-bush-hounds-of-love.md
5. #35 (beatles-white-album) → corpus/albums/beatles-white-album.md

Additional note for #34 (Hounds of Love): Kate Bush's self-production at her own 48-track studio is exceptional — verify gear claims (Fairlight CMI, etc.) against Sound on Sound coverage specifically.

Additional note for #35 (White Album): cross-link with #4 (Abbey Road) from Phase 1; both are Beatles + George Martin + EMI Studios but distinct production phases. Reference Lewisohn's *Recording Sessions* book content where publicly discussed.

Begin.
```

---

### Batch AL8 — Punk A (5 files: Bad Brains, Dead Kennedys, Misfits ×2, Clash)

```
Run albums research batch AL8 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #36–#40:

1. #36 (bad-brains-1982) → corpus/albums/bad-brains-1982.md
2. #37 (dead-kennedys-plastic-surgery-disasters) → corpus/albums/dead-kennedys-plastic-surgery-disasters.md
3. #38 (misfits-earth-ad) → corpus/albums/misfits-earth-ad.md
4. #39 (misfits-static-age) → corpus/albums/misfits-static-age.md
5. #40 (clash-london-calling) → corpus/albums/clash-london-calling.md

PUNK-SPECIFIC INSTRUCTION: early hardcore documentation is thinner than studio-rock documentation. Where session details are hazy, lean on what *has* been confirmed (producer credits via Wikipedia, fanzine archives where citable) rather than padding with speculation. The Bad Brains and Misfits files in particular should run on the shorter side (~1500 words) if verifiable content runs out — prefer short and verified over long and made-up.

Begin.
```

---

### Batch AL9 — Punk B / Post-Hardcore (5 files: Slits, Violent Femmes, Fugazi, Drive Like Jehu, Daughters)

```
Run albums research batch AL9 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #41–#45:

1. #41 (slits-cut) → corpus/albums/slits-cut.md
2. #42 (violent-femmes-debut) → corpus/albums/violent-femmes-debut.md
3. #43 (fugazi-repeater) → corpus/albums/fugazi-repeater.md
4. #44 (drive-like-jehu-yank-crime) → corpus/albums/drive-like-jehu-yank-crime.md
5. #45 (daughters-you-wont-get-what-you-want) → corpus/albums/daughters-you-wont-get-what-you-want.md

Additional note for #43 (Fugazi Repeater): Don Zientara's Inner Ear Studios is the citation anchor for this and many other Dischord albums. His engineering approach is widely-cited.

Begin.
```

---

### Batch AL10 — Electronic A (4 files: Portishead, Squarepusher, Daft Punk, Death Grips)

```
Run albums research batch AL10 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #46–#49:

1. #46 (portishead-dummy) → corpus/albums/portishead-dummy.md
2. #47 (squarepusher-hard-normal-daddy) → corpus/albums/squarepusher-hard-normal-daddy.md
3. #48 (daft-punk-discovery) → corpus/albums/daft-punk-discovery.md
4. #49 (death-grips-the-money-store) → corpus/albums/death-grips-the-money-store.md

Additional note for #48 (Discovery): cross-check sample claims at WhoSampled.com. The Eddie Johns "One More Time" sample chain is well-documented; many other samples on the album are too.

Begin.
```

---

### Batch AL11 — Electronic B / Pop-Experimental (5 files: Charli ×2, Spellling, Lingua Ignota, Threebrain)

```
Run albums research batch AL11 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #50–#54:

1. #50 (charli-xcx-charli) → corpus/albums/charli-xcx-charli.md
2. #51 (charli-xcx-brat) → corpus/albums/charli-xcx-brat.md
3. #52 (spellling-the-turning-wheel) → corpus/albums/spellling-the-turning-wheel.md
4. #53 (lingua-ignota-sinner-get-ready) → corpus/albums/lingua-ignota-sinner-get-ready.md
5. #54 (threebrain-weeeeee) → corpus/albums/threebrain-weeeeee.md

CRITICAL FLAG for #54 (Threebrain *Weeeeee!*): this is an X-tier outsider album with minimal verifiable documentation. The file should be SHORT (~1000–1500 words if needed) and STRICTLY verified-only. Do NOT pad with speculation. If you cannot verify enough to fill a chunk, omit the chunk. The corpus is better served by a short honest file than a long fabricated one.

Begin.
```

---

### Batch AL12 — Bob Dylan Folk Cycle (4 files: Freewheelin', Times, Highway 61, Blonde on Blonde)

```
Run albums research batch AL12 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #55–#58:

1. #55 (dylan-freewheelin) → corpus/albums/dylan-freewheelin.md
2. #56 (dylan-times-they-are-a-changin) → corpus/albums/dylan-times-they-are-a-changin.md
3. #57 (dylan-highway-61-revisited) → corpus/albums/dylan-highway-61-revisited.md
4. #58 (dylan-blonde-on-blonde) → corpus/albums/dylan-blonde-on-blonde.md

DYLAN-SPECIFIC INSTRUCTION: four albums in three years with overlapping session musicians and producers. Specific watch-outs:
- John Hammond vs Tom Wilson vs Bob Johnston producer transitions across these four albums — verify each
- Session-musician credit lists vary between sources; use Wikipedia's credit table as the anchor
- The "thin wild mercury sound" quote is Dylan's self-description for Blonde on Blonde (1966) — don't apply it to the earlier albums
- "Like a Rolling Stone" session (Highway 61) has well-documented details — Al Kooper organ accident, Mike Bloomfield guitar — use those

Cross-link the four files via shared tags (`bob-dylan`, year tags, producer tags).

Begin.
```

---

### Batch AL13 — Folk / Soul / Indie (4 files: Simone, Belle & Seb, Microphones, Marvin Gaye)

```
Run albums research batch AL13 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #59–#62:

1. #59 (nina-simone-sings-the-blues) → corpus/albums/nina-simone-sings-the-blues.md
2. #60 (belle-and-sebastian-sinister) → corpus/albums/belle-and-sebastian-sinister.md
3. #61 (microphones-the-glow-pt-2) → corpus/albums/microphones-the-glow-pt-2.md
4. #62 (marvin-gaye-whats-going-on) → corpus/albums/marvin-gaye-whats-going-on.md

Additional note for #62 (What's Going On): Marvin Gaye's self-production after the Motown system is the canonical story; Berry Gordy's initial resistance is well-documented. James Jamerson bass on the title track is widely cited.

Begin.
```

---

### Batch AL14 — Pop-Rock / Stadium (5 files: Zep, Floyd ×2, Prince, Janet)

```
Run albums research batch AL14 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #63–#67:

1. #63 (led-zeppelin-physical-graffiti) → corpus/albums/led-zeppelin-physical-graffiti.md
2. #64 (pink-floyd-animals) → corpus/albums/pink-floyd-animals.md
3. #65 (pink-floyd-the-wall) → corpus/albums/pink-floyd-the-wall.md
4. #66 (prince-purple-rain) → corpus/albums/prince-purple-rain.md
5. #67 (janet-jackson-velvet-rope) → corpus/albums/janet-jackson-velvet-rope.md

Additional note for #66 (Purple Rain): Susan Rogers (Prince's engineer) has done extensive recent interviews about the production. Reference her insights as the primary citation anchor for studio specifics.

Begin.
```

---

### Batch AL15 — Prog / Jazz Fusion / Experimental (5 files: Mingus, King Crimson, Mahavishnu, Earth, Godspeed)

```
Run albums research batch AL15 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #68–#72:

1. #68 (mingus-black-saint) → corpus/albums/mingus-black-saint.md
2. #69 (king-crimson-in-the-court) → corpus/albums/king-crimson-in-the-court.md
3. #70 (mahavishnu-inner-mounting-flame) → corpus/albums/mahavishnu-inner-mounting-flame.md
4. #71 (earth-2) → corpus/albums/earth-2.md
5. #72 (godspeed-lift-yr-skinny-fists) → corpus/albums/godspeed-lift-yr-skinny-fists.md

Additional note for #68 (Black Saint): Van Gelder Studio in Englewood Cliffs is a well-documented jazz-recording institution. Rudy Van Gelder's engineering practices on Impulse Records albums of this era are widely-covered.

Begin.
```

---

### Batch AL16 — Shoegaze / Noise / Drone / Proto-Punk (4 files: Swans ×2, Stooges ×2)

```
Run albums research batch AL16 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #73–#76:

1. #73 (swans-soundtracks-for-the-blind) → corpus/albums/swans-soundtracks-for-the-blind.md
2. #74 (swans-to-be-kind) → corpus/albums/swans-to-be-kind.md
3. #75 (stooges-fun-house) → corpus/albums/stooges-fun-house.md
4. #76 (stooges-raw-power) → corpus/albums/stooges-raw-power.md

Additional note for #76 (Raw Power): the Bowie mix vs Iggy 1997 remix is a well-documented controversy. Cover both; do not erase the original-Bowie-mix's existence.

Begin.
```

---

### Batch AL17 — Hard Rock / Metal (5 files: Nirvana, Metallica, SOAD, MCR, Weezer)

```
Run albums research batch AL17 for ARLO.

[same context-files + general-instruction body as AL1]

YOUR TASK:
Prompts #77–#81:

1. #77 (nirvana-nevermind) → corpus/albums/nirvana-nevermind.md
2. #78 (metallica-master-of-puppets) → corpus/albums/metallica-master-of-puppets.md
3. #79 (soad-toxicity) → corpus/albums/soad-toxicity.md
4. #80 (mcr-black-parade) → corpus/albums/mcr-black-parade.md
5. #81 (weezer-blue-album) → corpus/albums/weezer-blue-album.md

Additional note for #77 (Nevermind): Sound City Studios and the Neve console are well-documented via the Dave Grohl *Sound City* documentary (2013). Butch Vig + Andy Wallace separation of roles (producer vs mixer) is the citation anchor.

Begin.
```

---

### Batch AL18 — Cult + Late-Waits + Existing-Anchor Album Files (8 files)

```
Run albums research batch AL18 for ARLO. This is the largest batch (8 files); pace your context budget.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/ALBUMS-PROMPTS.md — master template + 89 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.
- /Users/cfitt/Dev/arlo/corpus/workflow/sos-inside-track-lewis-capaldi-someone-you-loved.md (already in corpus; example of session-detail-style file)
- /Users/cfitt/Dev/arlo/corpus/lyrics/sos-pattison-writing-better-lyrics-interview.md (already in corpus; example of in-depth chunk shape)

YOUR TASK:
Produce 8 markdown files by executing prompts #82–#89, in that order:

1. #82 (tom-waits-bone-machine) → corpus/albums/tom-waits-bone-machine.md
2. #83 (tom-waits-blood-money) → corpus/albums/tom-waits-blood-money.md
3. #84 (unicorns-who-will-cut-our-hair) → corpus/albums/unicorns-who-will-cut-our-hair.md
4. #85 (lcd-sound-of-silver) → corpus/albums/lcd-sound-of-silver.md
5. #86 (lcd-this-is-happening) → corpus/albums/lcd-this-is-happening.md
6. #87 (radiohead-ok-computer) → corpus/albums/radiohead-ok-computer.md
7. #88 (postal-service-give-up) → corpus/albums/postal-service-give-up.md
8. #89 (neutral-milk-hotel-aeroplane) → corpus/albums/neutral-milk-hotel-aeroplane.md

[same general instructions as AL1]

THIS BATCH IS LARGER (8 PROMPTS). Pace your context budget. If you start running low after 5–6 files, complete the in-flight file fully, then summarize the remaining work in your final report so it can be picked up in a new session.

Additional note for #85, #86, #87, #88, #89: these albums have existing artist-overview files in corpus/artists/. After writing each album file, briefly note in your final summary which existing artist file should be cross-linked. Do not modify the existing files — just flag for manual cross-linking.

Begin.
```

---

## Tracking checklist

- [x] AL1 — Phase 1 Starter A (5)
- [x] AL2 — Phase 1 Starter B (5)
- [x] AL3 — Hip-Hop A (5)
- [x] AL4 — Hip-Hop B (5)
- [x] AL5 — Hip-Hop C (5)
- [x] AL6 — Art-Rock A (5)
- [x] AL7 — Art-Rock B (5)
- [x] AL8 — Punk A (5)
- [x] AL9 — Punk B / Post-Hardcore (5)
- [x] AL10 — Electronic A (4)
- [x] AL11 — Electronic B / Pop-Experimental (5)
- [x] AL12 — Dylan folk cycle (4)
- [x] AL13 — Folk / Soul / Indie (4)
- [x] AL14 — Pop-Rock / Stadium (5)
- [x] AL15 — Prog / Jazz Fusion / Experimental (5)
- [x] AL16 — Shoegaze / Noise / Drone / Proto-Punk (4)
- [x] AL17 — Hard Rock / Metal (5)
- [x] AL18 — Cult + Late-Waits + Existing-Anchor (8)

When all 18 are checked: 89 album files in `corpus/albums/`, ~1200–1700 chunks added across all production-vocabulary clusters.

---

## After all batches complete

Three follow-up tasks:

1. **Cross-link artist-overview files.** For each album that has an existing artist-overview file (Bon Iver, LCD, Charli, Radiohead, Postal Service, NMH, Talking Heads, Bowie, plus secondary references), add a brief "See also: `corpus/albums/...`" footer linking the relevant album file. Manual edit, ~10–15 files.

2. **Threebrain quality audit.** This file is the highest hallucination risk in the entire 89-album batch. Specifically read it and verify or trim any suspicious claims before adding to retrieval.

3. **Update `corpus/README.md`** to reflect the new `corpus/albums/` folder and file count. Add a brief note on the album-anchored vs artist-anchored distinction so future ingest decisions are easier.

If you want, also harvest the "Cited Retrieval Topics" footers from all 89 new files into the `RETRIEVAL-INDEX.md` test set — gives you a ~800-question test corpus for validating ARLO's ingest pipeline once it's built.
