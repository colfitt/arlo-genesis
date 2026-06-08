---
title: Spotify Taste Profile
source: Spotify Extended Streaming History export (2015-06-11 → 2025-11-06)
scope: Personal listening-derived taste profile that ARLO uses to taste-match workflows to the user
records_analyzed: 31106
primary_metric: total ms_played (hours listened)
excluded: ["Tapir! (Spotify metadata error, per user)"]
generated: 2026-05-28
tags: [taste-profile, personal-context, cluster-workflows]
---

# Spotify Taste Profile

This profile is derived from 31,106 audio streams (2015–2025). It is **personal context**,
not general-corpus knowledge. ARLO reads it to surface workflows whose `taste_cluster` /
`anchor_artists` match the user's listening, and to anchor conversation in artists the user
actually loves.

## Top artists by total hours (all-time, excl. Tapir!)

| Hours | Plays | Artist |
|------:|------:|--------|
| 88 | 1871 | Radiohead |
| 38 | 536 | LCD Soundsystem |
| 33 | 503 | Car Seat Headrest |
| 28 | 480 | Talking Heads |
| 26 | 651 | Bon Iver |
| 25 | 386 | Sufjan Stevens |
| 20 | 342 | David Bowie |
| 20 | 369 | Modest Mouse |
| 17 | 272 | The Postal Service |
| 16 | 302 | Arcade Fire |
| 15 | 253 | Daft Punk |
| 15 | 300 | Death Cab for Cutie |
| 15 | 475 | The Mountain Goats |
| 14 | 220 | Leonard Cohen |
| 13 | 243 | Big Thief |
| 13 | 281 | Future Islands |
| 12 | 307 | Neutral Milk Hotel |
| 12 | 254 | The Decemberists |
| 12 | 275 | Tyler, The Creator |
| 11 | 148 | Black Country, New Road |

## Recent window (2023–2025) confirms the same core

Radiohead (60h), LCD Soundsystem (25h), Sufjan (22h), Bon Iver (21h), Talking Heads (19h),
Car Seat Headrest (18h), The Postal Service (17h). Notable recent risers: Sufjan and Bon Iver
(folk lean up), Swans and Adrianne Lenker appearing. Taste is stable across the decade.

## The 5 clusters

### 1. Art-rock / studio-as-instrument — `art-rock-studio-as-instrument`
Anchors: **Radiohead, Talking Heads, David Bowie.** The arrangement/studio is the
compositional act; songs emerge from sound-design and re-contextualization.

### 2. Indie-folk / confessional — `indie-folk-confessional`
Anchors: **Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker.** Lyric-and-intimacy-first;
capture the performance, build outward sparingly.

### 3. Electronic / dance-leaning — `electronic-groove-first`
Anchors: **LCD Soundsystem, Daft Punk, The Postal Service.** Groove-first, loop-and-arrangement
driven; the rhythm section is the hook.

### 4. Lo-fi / prolific — `lo-fi-prolific-volume`
Anchors: **Car Seat Headrest, Modest Mouse.** Volume and speed over polish; the demo is the song.

### 5. Post-punk / experimental — `post-punk-texture-dynamics`
Anchors: **Black Country New Road, Swans, Joy Division.** Texture, repetition, dynamics, and
build over conventional verse-chorus.

## How ARLO uses this

1. Match the user's `taste_cluster` to surface fitting workflows from `arlo/workflows/`.
2. Anchor examples in the user's own artists when explaining a technique.
3. Over repeated songs, track which clusters produce *finishes* (noted in each song's `ARLO.md`).
