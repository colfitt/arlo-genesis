# ARLO Quick-Dispatch Reference

For each of the 30 batches: **two prompts** to paste into a fresh Claude Code session.

- **Prompt 1 — Kickoff:** paste first, sends the agent off to do the work.
- **Prompt 2 — Verify:** paste after Prompt 1 reports completion (~10–15 min wall time). Validates output without re-running the work.

Both are minimal — they reference the SESSIONS files on disk so you're not pasting 30-line walls of text.

---

## How a session goes

```
1. Open new Claude Code chat
2. Paste Prompt 1
3. Wait for agent to report "files written" (varies by batch: 8–22 min)
4. Paste Prompt 2 in the same chat
5. Agent verifies + flags anything worth spot-checking
6. Move to next session
```

If Prompt 2 finds issues, you can ask the agent to fix the specific file: "Re-run prompt #N from {file} with tighter anti-hallucination on {specific claim}."

---

## Prereq (one-time)

```bash
mkdir -p ~/Dev/arlo/corpus/{albums,artists,techniques}
```

---

## Aesthetic Stream — 12 batches

---

### Session 1 — Batch A1 (Bon Iver + LCD, 4 files)

**Prompt 1 — Kickoff**
```
Run batch A1 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A1 — Bon Iver + LCD" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For each file you wrote in batch A1, verify: (1) front-matter has all required fields including the "Source: Deep-research synthesis" line and Aesthetic-stack relevance line, (2) at least 8 body H2 sections, (3) Cited Retrieval Topics and Sources sections present, (4) inline citations are real URLs not placeholders, (5) word count is within 1500–2500 range. Flag any file with structural issues, any specific factual claim worth spot-checking, and any "weak verification" topics from your initial report that deserve a manual review pass. Provide a one-line summary per file with sizes and chunk counts.
```

---

### Session 2 — Batch A2 (LCD adjacents + Charli, 3 files)

**Prompt 1 — Kickoff**
```
Run batch A2 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A2 — LCD adjacents + Charli" heading, follow the kickoff message verbatim. Note: prompt #7 (charli-xcx-brat-production) overlaps with ALBUMS batch AL11 row #51; default to executing it (Option A in the SESSIONS note). Begin.
```

**Prompt 2 — Verify** (same template as Session 1; substitute batch ID)
```
For each file you wrote in batch A2, verify the standard structural and citation checks. Flag anything weak. Specifically spot-check whether your charli-xcx-brat-production.md (prompt #7) duplicates content that's already in the corpus at corpus/mixing/sos-inside-track-billie-eilish-bad-guy.md — they shouldn't overlap (different artist, but check for accidental over-quoting from that existing file). One-line summary per file.
```

---

### Session 3 — Batch A3 (mk.gee + Bluegrass, 3 files)

**Prompt 1 — Kickoff**
```
Run batch A3 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A3 — mk.gee + Bluegrass artists" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For each file you wrote in batch A3, run standard structural and citation checks. CRITICAL: spot-check the mk.gee file especially carefully — this is the highest-hallucination-risk file in the entire aesthetic corpus given thin technical documentation. Verify 3–5 specific claims against the Dazed/NYT/Switched On Pop sources actually cited. Add explicit "⚠ unverified" inline tags to any claim that's a stretch. For the Billy Strings and Punch Brothers files, run the standard checks. One-line summary per file.
```

---

### Session 4 — Batch A4 (Talking Heads cluster, 2 files; #19 deprecated)

**Prompt 1 — Kickoff**
```
Run batch A4 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A4 — Talking Heads cluster" heading, follow the kickoff message verbatim. Skip prompt #19 (deprecated). Begin.
```

**Prompt 2 — Verify**
```
For the 2 files you wrote in batch A4 (david-byrne-songwriting-philosophy and oblique-strategies-and-studio-as-instrument), run standard structural and citation checks. Specifically verify that the Oblique Strategies file does NOT cover Remain in Light session details (those belong in the album file). Confirm cross-links to album AL1 are noted in your final summary. One-line summary per file.
```

---

### Session 5 — Batch A5 (Ry Cooder + Radiohead cluster, 4 files; #24 deprecated)

**Prompt 1 — Kickoff**
```
Run batch A5 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A5 — Ry Cooder + Radiohead cluster" heading, follow the kickoff message verbatim. Skip prompt #24 (deprecated). Begin.
```

**Prompt 2 — Verify**
```
For the 4 files you wrote in batch A5, run standard structural and citation checks. Specifically: (1) verify the Coodercaster pickup-configuration claims (Teisco neck from Lindley + Valco bridge) match the qp-slide.com source, (2) verify the In Rainbows file doesn't duplicate content from the Kid A album file in ALBUMS corpus, (3) confirm the open-tunings technique file is generic technique-anchored (not Ry-Cooder-specific — that's row #22's job). One-line summary per file.
```

---

### Session 6 — Batch A6 (Sufjan + Dijon, 2 files)

**Prompt 1 — Kickoff**
```
Run batch A6 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A6 — Sufjan + Dijon" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 2 files in batch A6, run standard structural and citation checks. Verify the Dijon file's gear claims (AKG C414, Octatrack, Eurorack, Ableton) are documented in the cited sources, not inferred. Verify the Sufjan file covers Age of Adz specifically, not generic Sufjan biography. One-line summary per file.
```

---

### Session 7 — Batch A7 (Big Thief + CSH + BCNR, 4 files)

**Prompt 1 — Kickoff**
```
Run batch A7 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A7 — Big Thief + CSH + BCNR" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 4 files in batch A7, run standard structural and citation checks. Verify Big Thief's nomadic-recording specifics (5 locations, James Krivchenia, Sam Owens engineering, "Certainty" four-track-on-car-battery story) match the NPR/UNCUT sources. Verify BCNR's Maschetzko-as-first-time-studio-producer framing is in the cited sources. For the Adrianne Lenker solo file, verify it doesn't accidentally cover material that should be in the Big Thief file. One-line summary per file.
```

---

### Session 8 — Batch A8 (Andrew Bird + FJM, 2 files; #33 deprecated)

**Prompt 1 — Kickoff**
```
Run batch A8 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A8 — Andrew Bird + FJM" heading, follow the kickoff message verbatim. Skip prompt #33 (deprecated). Begin.
```

**Prompt 2 — Verify**
```
For the 2 files in batch A8, run standard structural and citation checks. Verify Andrew Bird's Line 6 looper pedal model and signal-chain order are documented in the TechCrunch/Relix sources, not inferred. Verify Father John Misty file focuses on Wilson production methodology, not Tillman biography. One-line summary per file.
```

---

### Session 9 — Batch A9 (Cameron Winter + Geese + Vulfpeck + AC, 4 files)

**Prompt 1 — Kickoff**
```
Run batch A9 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A9 — Cameron Winter + Geese + Vulfpeck + AC" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 4 files in batch A9, run standard structural and citation checks. Specifically: (1) the Cameron Winter file (#36) and the Geese band-context file (#37) should NOT duplicate each other — verify they cover distinct material (#36 is solo album production, #37 is band context); (2) verify Vulfpeck's "play tight, leave space" philosophy quote is attributable to The Believer or another cited source; (3) verify the Animal Collective Ben Allen / Sweet Tea Studios specifics match the Sound on Sound source. One-line summary per file.
```

---

### Session 10 — Batch A10 (Knopfler + Zevon + Prine + Bowie, 4 files; #43 deprecated)

**Prompt 1 — Kickoff**
```
Run batch A10 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch A10 — Knopfler + Zevon + Prine + Bowie" heading, follow the kickoff message verbatim. Skip prompt #43 (deprecated). Begin.
```

**Prompt 2 — Verify**
```
For the 4 files in batch A10, run standard structural and citation checks. CRITICAL for Bowie file (#44): verify that Eno is described as "collaborator" NOT "producer" — Visconti was the producer. This is a common misattribution. Cross-check Wikipedia's Producer line for Low, Heroes, Lodger. For Knopfler file: verify the pickless-fingerstyle technique claims trace to Premier Guitar's lesson. For Zevon: verify the "Werewolves" seven-rhythm-section story is from Waddy Wachtel's interview, not invented. One-line summary per file.
```

---

### Session 11 — Batch T1 (Vocal + Electronic technique, 4 files)

**Prompt 1 — Kickoff**
```
Run batch T1 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch T1 — Vocal + Electronic technique" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 4 files in batch T1, run standard structural and citation checks. CRITICAL for hyperpop-sound-design file: verify the MusicRadar Auto-Tune settings (retune speed 0.00 ms, formant +7.20 semitones) are cited accurately, not invented additional specifics. For vocal-stacking file: verify Bon Iver SM57-single-mic origin is attributable to the MusicRadar source. For Auto-Tune lineage file: verify the Cher (1998) → T-Pain → Kanye → Bon Iver → SOPHIE chronology is in the Berklee/Red Bull sources, not fabricated. One-line summary per file.
```

---

### Session 12 — Batch T2 (Guitar + Mix + Theory, 4 files)

**Prompt 1 — Kickoff**
```
Run batch T2 for ARLO. Read /Users/cfitt/Dev/arlo/AESTHETIC-SESSIONS.md, find the "Batch T2 — Guitar + Mix + Theory" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 4 files in batch T2, run standard structural and citation checks. CRITICAL for modal-bluegrass-harmony file: do NOT cite Berklee Press "Beyond Bluegrass Banjo" book directly (not in corpus yet) — only what's publicly discussed about it. For dense-but-clear-mixing file: verify it cross-references corpus/mixing/sos-inside-track-billie-eilish-bad-guy.md (already in corpus) rather than duplicating its content. For reamping-fundamentals file: verify Premier Guitar Recording Dojo citations. For pedal-as-instrument file: verify KNOBs YouTube reference treats their text-on-screen demo format honestly. One-line summary per file.
```

---

## Albums Stream — 18 batches

---

### Session 13 — Batch AL1 (Phase 1 starter A, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL1 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL1 — Phase 1 Starter A" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL1, run standard structural checks: album-anchored front-matter (Artist/Year/Producer(s)/Studio(s)), 8–15 body H2 sections, Cited Retrieval Topics, Sources bibliography. CRITICAL checks: (1) Joy Division — verify Hannett's specific techniques (AMS digital delay, isolated drum mic'ing) are from documented sources not invented, (2) Loveless — verify the £250k budget figure is widely-cited not just Wikipedia, (3) Talking Heads Remain in Light — verify Compass Point Studios is documented, (4) Abbey Road — verify the 8-track Studer J37 claim, (5) Bowie Station to Station — verify Cherokee Studios session. One-line summary per file.
```

---

### Session 14 — Batch AL2 (Phase 1 starter B, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL2 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL2 — Phase 1 Starter B" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL2, run standard structural checks. CRITICAL: (1) Bitches Brew — verify Teo Macero's tape-editing approach is documented, the Columbia 30th Street session dates (Aug 19–21, 1969) are accurate, (2) Kid A — verify Godrich's role and the studio choices, (3) Paul's Boutique — every sample claim cross-checked against WhoSampled.com (the ~105 samples have been documented), (4) Björk Vespertine — Matmos collaboration on field recordings is documented, (5) Tom Waits Rain Dogs — Marc Ribot's first Waits album, RPM Studios. One-line summary per file.
```

---

### Session 15 — Batch AL3 (Hip-Hop A, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL3 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL3 — Hip-Hop A" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 hip-hop files in batch AL3, every sample claim must be cross-checked against WhoSampled.com. Specifically verify: (1) Public Enemy — Bomb Squad's specific James Brown samples on key tracks, (2) Dr. Dre Chronic — Parliament/Funkadelic sample usage, (3) Wu-Tang 36 Chambers — kung-fu film dialog samples (specifics), (4) Nas Illmatic — per-track producer credits (Premier, Pete Rock, Q-Tip, Large Pro, L.E.S.), (5) GZA Liquid Swords — chess-themed sample chain. One-line summary per file plus any sample-attribution flags.
```

---

### Session 16 — Batch AL4 (Hip-Hop B, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL4 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL4 — Hip-Hop B" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 hip-hop files in batch AL4, cross-check all sample claims at WhoSampled.com. CRITICAL: files #18 (Roots Things Fall Apart) and #19 (Common Like Water for Chocolate) are both Soulquarians-era Electric Lady Studios records — verify they don't duplicate session-detail content and cross-link via tags. Verify Organized Noize production credits on both Outkast albums. One-line summary per file.
```

---

### Session 17 — Batch AL5 (Hip-Hop C, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL5 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL5 — Hip-Hop C" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL5, run standard checks plus WhoSampled cross-check. CRITICAL for Clipse Let God Sort Em Out (2025): if specific session details aren't yet publicly documented, the file should be SHORT and qualitative — do NOT fabricate session details for this recent release. Verify Kanye Wyoming-era 7-song-album format claim. Verify Madvillain's Stones Throw / leaked-demo history. Verify Kendrick TPAB producer credits (Sounwave, Flying Lotus, Pharrell, Boi-1da, Terrace Martin, Knxwledge, Thundercat). One-line summary per file.
```

---

### Session 18 — Batch AL6 (Art-Rock A, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL6 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL6 — Art-Rock A" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL6, run standard checks. CRITICAL: late-60s/early-70s engineer credits are often unclear — be especially careful about engineer-vs-producer attribution. Wikipedia's "Producer:" line is the citation anchor. For Transformer (#28) and Ziggy Stardust (#29): both Trident Studios 1972, cross-link via studio+producer tags. For Marquee Moon (#30): verify Andy Johns producer credit. For both VU albums: verify Tom Wilson role distinction from Warhol's "production." One-line summary per file.
```

---

### Session 19 — Batch AL7 (Art-Rock B, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL7 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL7 — Art-Rock B" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL7, run standard checks. CRITICAL: (1) Kate Bush Hounds of Love — verify Fairlight CMI use and her 48-track home-studio setup against Sound on Sound coverage specifically, (2) Beatles White Album — cross-link with Abbey Road file (#4 from AL1), both EMI Studios but distinct production phases, (3) Depeche Mode Violator — verify Flood + Alan Wilder roles and the Synclavier use, (4) Wire Pink Flag — verify Mike Thorne credit, (5) TMBG Lincoln — verify Dial-A-Song bedroom-tape lineage. One-line summary per file.
```

---

### Session 20 — Batch AL8 (Punk A, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL8 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL8 — Punk A" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 punk files in batch AL8, run standard checks. Early hardcore documentation is thin — verify files lean on confirmed sources (Wikipedia producer credits, fanzine archives where citable) rather than padding. Bad Brains and Misfits files should run on the SHORTER side (~1500 words) if verifiable content runs out — prefer short and verified. For Clash London Calling: verify Guy Stevens' chaotic-production methodology is in cited sources not just mythologized. One-line summary per file.
```

---

### Session 21 — Batch AL9 (Punk B / Post-hardcore, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL9 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL9 — Punk B / Post-hardcore" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL9, run standard checks. CRITICAL: (1) Slits Cut — verify Dennis Bovell as producer + the dub-punk hybrid framing, (2) Fugazi Repeater — Don Zientara at Inner Ear Studios is the citation anchor for many Dischord albums, (3) Drive Like Jehu Yank Crime — verify Mark Trombino credit, (4) Daughters You Won't Get What You Want — verify Seth Manchester at Machines with Magnets. One-line summary per file.
```

---

### Session 22 — Batch AL10 (Electronic A, 4 files)

**Prompt 1 — Kickoff**
```
Run batch AL10 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL10 — Electronic A" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 4 files in batch AL10, run standard checks. CRITICAL: (1) Portishead Dummy — verify Geoff Barrow MPC-sampling philosophy and Adrian Utley role from documented sources, (2) Daft Punk Discovery — sample claims cross-checked at WhoSampled.com (Eddie Johns "One More Time" chain is well-documented), (3) Death Grips The Money Store — verify Zach Hill + Flatlander roles, (4) Squarepusher Hard Normal Daddy — verify Warp Records context. One-line summary per file.
```

---

### Session 23 — Batch AL11 (Electronic B / Pop-experimental, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL11 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL11 — Electronic B / Pop-experimental" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL11, run standard checks. CRITICAL: (1) Threebrain Weeeeee! — this file should be SHORT (~1000–1500 words) and STRICTLY verified-only. Do NOT pad with speculation; if you cannot verify enough to fill a chunk, omit the chunk. (2) Both Charli files (#50 Charli + #51 BRAT) should cross-reference but not duplicate each other; cross-link via tags. (3) Spellling and Lingua Ignota: 2021-era thin documentation; verify what's confirmed via Pitchfork retrospectives. One-line summary per file.
```

---

### Session 24 — Batch AL12 (Bob Dylan folk cycle, 4 files)

**Prompt 1 — Kickoff**
```
Run batch AL12 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL12 — Bob Dylan folk cycle" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 4 Dylan files in batch AL12, run standard checks. CRITICAL Dylan watch-outs: (1) Producer transitions across the four albums — John Hammond → Tom Wilson → Bob Johnston. Verify each. (2) Session musician overlaps between albums; use Wikipedia credit tables as the anchor. (3) The "thin wild mercury sound" is Dylan's self-description for Blonde on Blonde (1966) ONLY — do NOT apply it to the earlier albums. (4) "Like a Rolling Stone" session (Highway 61) has well-documented details — Al Kooper organ accident, Mike Bloomfield guitar — these are real. Cross-link the four files via shared tags. One-line summary per file.
```

---

### Session 25 — Batch AL13 (Folk / Soul / Indie, 4 files)

**Prompt 1 — Kickoff**
```
Run batch AL13 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL13 — Folk / Soul / Indie" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 4 files in batch AL13, run standard checks. CRITICAL: (1) Marvin Gaye What's Going On — verify self-production after Motown system; James Jamerson bass on title track is well-documented, (2) Belle and Sebastian If You're Feeling Sinister — verify Tony Doogan + £1000 budget aesthetic, (3) The Microphones The Glow Pt. 2 — verify Phil Elverum self-recording at Dub Narcotic / K Records context, (4) Nina Simone Sings the Blues — verify Danny Davis producer credit at RCA Studios. One-line summary per file.
```

---

### Session 26 — Batch AL14 (Pop-Rock / Stadium, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL14 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL14 — Pop-Rock / Stadium" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL14, run standard checks. CRITICAL: (1) Prince Purple Rain — Susan Rogers' interviews are the primary citation anchor for studio specifics, (2) The Wall — Bob Ezrin's role is the central production story; multiple-studio recording logistics, (3) Physical Graffiti — Headley Grange + Olympic + Ronnie Lane's Mobile Studio; verify mobile-studio era context, (4) Pink Floyd Animals — Britannia Row Studios in-house context, (5) Janet Jackson The Velvet Rope — Jam & Lewis at Flyte Tyme. One-line summary per file.
```

---

### Session 27 — Batch AL15 (Prog / Jazz fusion / Experimental, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL15 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL15 — Prog / Jazz fusion / Experimental" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL15, run standard checks. CRITICAL: (1) Mingus Black Saint — Van Gelder Studio + Rudy Van Gelder engineering context, Bob Thiele Impulse era, (2) King Crimson — Wessex Sound Studios, Mellotron-as-instrument (Ian McDonald), (3) Mahavishnu — Criteria Recording Studios, John McLaughlin double-necked Gibson, (4) Earth 2 — Avast Studios Seattle + Stuart Hallerman, (5) Godspeed You! — Hotel2Tango Montreal + Howard Bilerman. One-line summary per file.
```

---

### Session 28 — Batch AL16 (Shoegaze / Noise / Drone / Proto-Punk, 4 files)

**Prompt 1 — Kickoff**
```
Run batch AL16 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL16 — Shoegaze / Noise / Drone / Proto-Punk" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 4 files in batch AL16, run standard checks. CRITICAL: (1) Stooges Raw Power — the Bowie mix vs Iggy 1997 remix controversy is well-documented; cover both, do not erase the original-Bowie-mix's existence, (2) Stooges Fun House — verify Don Gallucci's live-tracking approach, Steve Mackay sax, (3) Both Swans albums — verify Michael Gira role, John Congleton on To Be Kind, Sonic Ranch studio, Hotel2Tango context. Cross-link Swans files via tags. One-line summary per file.
```

---

### Session 29 — Batch AL17 (Hard Rock / Metal, 5 files)

**Prompt 1 — Kickoff**
```
Run batch AL17 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL17 — Hard Rock / Metal" heading, follow the kickoff message verbatim. Begin.
```

**Prompt 2 — Verify**
```
For the 5 files in batch AL17, run standard checks. CRITICAL: (1) Nevermind — Butch Vig + Andy Wallace separation of roles (producer vs mixer) is the citation anchor; Sound City + Neve console are documented via the Dave Grohl Sound City documentary 2013, (2) Master of Puppets — Flemming Rasmussen at Sweet Silence Studios Copenhagen; Cliff Burton's last full studio album, (3) SOAD Toxicity — Rick Rubin + Daron Malakian production, (4) MCR Black Parade — Rob Cavallo + Paramour Mansion, (5) Weezer Blue Album — Ric Ocasek at Electric Lady Studios. One-line summary per file.
```

---

### Session 30 — Batch AL18 (Cult + Late-Waits + Existing-anchor album files, 8 files)

**Prompt 1 — Kickoff**
```
Run batch AL18 for ARLO. Read /Users/cfitt/Dev/arlo/ALBUMS-SESSIONS.md, find the "Batch AL18 — Cult + Late-Waits + Existing-Anchor Album Files" heading, follow the kickoff message verbatim. This is the largest batch (8 files); pace your context budget. Begin.
```

**Prompt 2 — Verify**
```
For the 8 files in batch AL18, run standard checks. CRITICAL: (1) Tom Waits Bone Machine — "Mr. Knickerbocker's room" cement-room recording is well-documented; verify, (2) Tom Waits Blood Money — verify the Robert Wilson Woyzeck commission context, (3) The Unicorns Who Will Cut — verify Hotel2Tango Montreal context, (4) For the 4 existing-anchor album files (LCD Sound of Silver, LCD This Is Happening, Radiohead OK Computer, Postal Service Give Up, NMH Aeroplane): note which existing artist-overview file in corpus/artists/ each should be cross-linked to in your final summary. Do NOT modify the existing files — just flag for manual cross-linking. One-line summary per file.
```

---

## Quick-reference table

| # | Batch | Files | Source file | Wall time |
|---|-------|-------|-------------|-----------|
| 1 | A1 | 4 | AESTHETIC | ~10 |
| 2 | A2 | 3 | AESTHETIC | ~9 |
| 3 | A3 | 3 | AESTHETIC | ~9 |
| 4 | A4 | 2 | AESTHETIC | ~8 |
| 5 | A5 | 4 | AESTHETIC | ~12 |
| 6 | A6 | 2 | AESTHETIC | ~8 |
| 7 | A7 | 4 | AESTHETIC | ~12 |
| 8 | A8 | 2 | AESTHETIC | ~8 |
| 9 | A9 | 4 | AESTHETIC | ~12 |
| 10 | A10 | 4 | AESTHETIC | ~12 |
| 11 | T1 | 4 | AESTHETIC | ~10 |
| 12 | T2 | 4 | AESTHETIC | ~10 |
| 13 | AL1 | 5 | ALBUMS | ~15 |
| 14 | AL2 | 5 | ALBUMS | ~15 |
| 15 | AL3 | 5 | ALBUMS | ~15 |
| 16 | AL4 | 5 | ALBUMS | ~15 |
| 17 | AL5 | 5 | ALBUMS | ~15 |
| 18 | AL6 | 5 | ALBUMS | ~15 |
| 19 | AL7 | 5 | ALBUMS | ~15 |
| 20 | AL8 | 5 | ALBUMS | ~15 |
| 21 | AL9 | 5 | ALBUMS | ~15 |
| 22 | AL10 | 4 | ALBUMS | ~12 |
| 23 | AL11 | 5 | ALBUMS | ~15 |
| 24 | AL12 | 4 | ALBUMS | ~12 |
| 25 | AL13 | 4 | ALBUMS | ~12 |
| 26 | AL14 | 5 | ALBUMS | ~15 |
| 27 | AL15 | 5 | ALBUMS | ~15 |
| 28 | AL16 | 4 | ALBUMS | ~12 |
| 29 | AL17 | 5 | ALBUMS | ~15 |
| 30 | AL18 | 8 | ALBUMS | ~22 |

**Total:** 30 sessions, ~127 files (38 aesthetic active + 89 albums), ~360 min serial OR ~30–60 min in parallel.
