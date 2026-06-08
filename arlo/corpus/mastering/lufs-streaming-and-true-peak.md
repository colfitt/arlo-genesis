# LUFS, Streaming Targets, and True Peak

**Scope:** mastering
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Spotify Loudness Normalization docs (in corpus at `reference/spotify-loudness-normalization.md`); Apple Mastered for iTunes / Apple Digital Masters; Bob Katz, *Mastering Audio* (3rd ed., 2015); iZotope streaming-mastering guide
**Tags:** `mastering`, `LUFS`, `streaming`, `true-peak`, `reference-fact`, `delivery`

---

## Integrated, short-term, and momentary LUFS

LUFS measurements come in three time windows, all defined under [ITU-R BS.1770 and EBU R128](https://en.wikipedia.org/wiki/EBU_R_128). **Momentary** uses a sliding 400 ms window — useful for catching the loudest instant in a track. **Short-term** uses a sliding 3-second window — closer to perceived loudness on a vocal phrase or chorus hit. **Integrated** is the gated measurement across the entire track and is the value streaming platforms actually use for normalization. Integrated LUFS uses two gating thresholds (an absolute gate at –70 LUFS and a relative gate 10 LU below the running mean) so that silent passages and intros don't artificially lower the result. When a platform says "we target –14 LUFS," they mean integrated. When a meter shows your chorus hitting –9, that's short-term — and your integrated will still be lower because the verses pull the average down.

## Per-platform integrated LUFS targets

The cross-platform reference table (also in `corpus/reference/spotify-loudness-normalization.md`):

| Platform | Integrated LUFS target | True-peak ceiling | Behavior |
|---|---|---|---|
| Spotify (Normal) | –14 LUFS | –1 dBTP (Spotify recommends –2 dBTP for safety on louder masters) | Up- and down-normalizes |
| Spotify (Loud, premium) | –11 LUFS | –1 dBTP, limiter applied | Down-normalizes only above –11; pushes limiter on quieter |
| Spotify (Quiet, premium) | –19 LUFS | n/a | Down-normalizes |
| Apple Music (Sound Check on) | –16 LUFS | –1 dBTP | Down-normalizes only — never boosts |
| YouTube Music | –14 LUFS | –1 dBTP | Down-normalizes only |
| Tidal | –14 LUFS | –1 dBTP | Down-normalizes |
| Amazon Music | –14 LUFS | –2 dBTP | Down-normalizes |
| Deezer | –15 LUFS | –1 dBTP | Track normalization |
| SoundCloud | No normalization | (mastering choice) | Original file plays as-is |

[iZotope's streaming-mastering guide](https://www.izotope.com/en/learn/mastering-for-streaming-platforms) and [Production Expert's Apple Music writeup](https://www.production-expert.com/production-expert-1/apple-choose-16lufs-loudness-level-for-apple-music-heres-why) confirm these values as of 2026. Note: a small number of secondary sources cite Amazon at –13 LUFS, but the prevailing figure across mastering-engineer references is –14.

## Up-normalization vs. down-normalization (this changes the strategy)

Not every platform handles loud-vs-quiet symmetrically. **Spotify up-normalizes** — if your track lands at –20 LUFS integrated, Spotify will *raise* the playback gain toward –14, applying its own limiter on the way up. **Apple Music, YouTube Music, Tidal, and Amazon only turn things down** — if your track is at –20 LUFS, it plays at –20 LUFS. [Critical Listening Lab](https://www.criticallisteninglab.com/en/learn/loudness/apple-music) and [Meterplugs](https://www.meterplugs.com/blog/2022/03/23/apple-switch-to-lufs.html) both make this distinction explicit. Practical consequence: a master at –18 LUFS sounds noticeably quieter than the catalog on Apple Music, but on Spotify it'll be raised. If you intentionally master dynamic (–16 or quieter), Apple's listeners hear the dynamics; Spotify's listeners hear a louder, more limited version because of Spotify's loudness compensation limiter.

## Why mastering louder than the platform target hurts you

The loudness war made sense when CDs and radio rewarded peak loudness. Streaming normalization inverts that incentive. If you master to –9 LUFS to "win" the loudness race, streaming services normalize you back down to their target anyway — and the audience hears your overcompressed master at the same playback level as the engineer who left dynamics intact. [Lost Stories Academy](https://www.loststoriesacademy.com/blogs-and-tutorials/why-mastering-for-streaming-is-different-in-2025) frames it as a zero-sum trade: "excessive loudness only compresses the music unnecessarily." The dynamic master wins on perceived punch. The over-limited master also accumulates lossy-codec distortion (see below) that wasn't audible at higher playback levels. Recommended posture: master to what serves the song, then check it lands in a sensible window (–14 to –9 LUFS for modern pop/rock; –16 to –12 for indie/folk; –10 to –7 for EDM/trap if that's the genre convention).

## True peak vs. sample peak — the inter-sample problem

A sample peak meter only sees the digital samples. The continuous analog waveform that a D/A converter or a lossy codec reconstructs *between* those samples can be higher. These are **inter-sample peaks**, measured in dBTP (decibels true peak). [Mastering The Mix](https://www.masteringthemix.com/blogs/learn/inter-sample-and-true-peak-metering) and [Sound on Sound](https://www.soundonsound.com/sound-advice/q-inter-sample-peaks-causing-mix-distortion) both explain that a file showing 0 dBFS sample peak can have reconstructed peaks at +0.5 dBTP or higher — and when an AAC encoder hits that, you get audible distortion. [LuvLang's true-peak writeup](https://luvlang.studio/blog/true-peak-limiting-explained) cites cases where true peaks rose by **1.73 dB after MP3 encoding**, with pathological cases reaching +10 dB. This is why true-peak limiting (not just sample-peak limiting) is essential for any master destined for streaming.

## True-peak ceiling conventions

The universally safe ceiling is **–1 dBTP**. That's what [Spotify's mastering guidelines](https://support.spotify.com/us/artists/article/loudness-normalization/) ask for; what [Apple Digital Masters](https://www.criticallisteninglab.com/en/learn/loudness/apple-music) requires as part of its certification; and what AES streaming-loudness recommendations cite. Spotify additionally recommends **–2 dBTP** specifically for masters louder than about –14 LUFS, because Spotify's own down-normalization-plus-limiter chain on the Loud profile can re-add headroom problems. [Remasterify's true-peak guide](https://blog.remasterify.com/true-peak-101-everything-you-need-to-know/) notes some mastering engineers go to –1.5 dBTP routinely for any lossy-bound delivery. The cost of headroom is tiny: 1 dB of ceiling is inaudible against the loudness changes from normalization, but it preserves the master from codec artifacts the engineer can't audition.

## Measuring with free meters (Youlean, Loudness Meter, etc.)

The free [Youlean Loudness Meter 2](https://youlean.co/youlean-loudness-meter/) is the de-facto standard. It reads integrated LUFS, short-term, momentary, LRA, true peak, and includes presets for every major streaming platform — load the Spotify preset and it shows compliance against –14 LUFS / –1 dBTP at a glance. iZotope Insight, TC Electronic Clarity M, and the DAW-native meters in Pro Tools, Logic, and Reaper all measure to the same ITU-R BS.1770 standard. Free web-based file analyzers like [Youlean's file meter](https://youlean.co/file-loudness-meter/) accept a WAV upload and return integrated LUFS, LRA, and true peak — useful for double-checking a bounced master without re-opening the session.

## Loudness Range (LRA) and what's normal per genre

LRA measures the difference (in LU) between the quiet and loud portions of a track, excluding the very quietest and very loudest moments via percentile gating. [Youlean's standards table](https://youlean.co/loudness-standards-full-comparison-table/) gives typical LRA ranges per genre: **modern pop / EDM / trap: 3–6 LU**, **rock / hip-hop: 5–8 LU**, **indie / folk: 8–12 LU**, **jazz / classical / film score: 12–20 LU**. LRA is a guide, not a target — a low LRA isn't worse than a high LRA, it just reflects how the track moves. But unexpected LRA values are a flag: a hip-hop track at LRA 14 is probably under-compressed in the mix; a folk ballad at LRA 4 is probably over-compressed at master.

## The dynamic master vs. loud master trade

Two strategies coexist in modern mastering. **The "dynamic master"** approach (Bob Katz's K-system, and what Apple Digital Masters effectively rewards) targets –14 LUFS or quieter with LRA 6–10 and –1 dBTP ceiling. Result: on Apple Music it sounds open and punchy because nothing's turned down; on Spotify it gets raised toward the catalog level. **The "competitive loud master"** approach targets –9 to –7 LUFS with LRA 3–5 and tighter limiting. Result: on SoundCloud (no normalization) it competes; on Spotify it gets turned down and the dynamics are gone permanently. The current industry trend ([iMusician's 2025 loudness-war update](https://imusician.pro/en/resources/blog/mastering-and-the-loudness-war-an-update)) favors the dynamic-master approach for streaming-first releases, though dance music and certain hip-hop subgenres remain loud-master territory.

## Album LUFS vs. track LUFS

Streaming platforms have two normalization modes: **track mode** (each track normalized independently) and **album mode** (all tracks normalized as a unit, preserving relative loudness). Spotify and Apple Music both implement album mode when the listener is playing through an album in order. If you master an album, set per-track LUFS so that the *relative* loudness from track to track is what you want, then bounce — the platform will preserve those relationships when album mode is on, and reset them when listeners shuffle into a playlist. This is why a mastering engineer might land an album opener at –16 LUFS and a banger at –10 LUFS without "fixing" the gap: the gap is intentional and album-mode preserves it.

## Practical defaults for the intermediate musician

If you're not sure: **target around –14 LUFS integrated, –1 dBTP ceiling, LRA appropriate to your genre, and confirm in a meter before bouncing.** That lands cleanly on Spotify, YouTube, Tidal, and Amazon; gets a small turndown on Apple Music; and avoids codec artifacts on every platform. If you're chasing the EDM/trap loud master, push to –9 LUFS but keep the true-peak ceiling at –1 dBTP — never sacrifice the ceiling for loudness. If you're mastering folk, jazz, or classical: stay at –16 to –18 LUFS and don't fight it. Streaming normalization makes that the louder-sounding choice on Apple Music anyway.

---

## Cited Retrieval Topics

- "what lufs should i master to for spotify"
- "what's the loudness target for apple music"
- "what's the difference between integrated and short term lufs"
- "what is true peak vs sample peak"
- "why does -1 dbtp matter for streaming"
- "should i master louder for streaming"
- "what's a good lra for pop music"
- "does spotify turn up quiet tracks"
- "what's the best free lufs meter"
- "what lufs target for youtube and tidal"

## Sources

- [Spotify for Artists: Loudness normalization](https://support.spotify.com/us/artists/article/loudness-normalization/)
- [iZotope: How to master for streaming platforms](https://www.izotope.com/en/learn/mastering-for-streaming-platforms)
- [Production Expert: Apple Choose -16 LUFS Loudness Level For Apple Music](https://www.production-expert.com/production-expert-1/apple-choose-16lufs-loudness-level-for-apple-music-heres-why)
- [Meterplugs: Apple Switches to LUFS, Enables Sound Check by Default](https://www.meterplugs.com/blog/2022/03/23/apple-switch-to-lufs.html)
- [Critical Listening Lab: Apple Music Loudness](https://www.criticallisteninglab.com/en/learn/loudness/apple-music)
- [Lost Stories Academy: Why Mastering for Streaming is Different in 2025](https://www.loststoriesacademy.com/blogs-and-tutorials/why-mastering-for-streaming-is-different-in-2025)
- [Mastering The Mix: Inter-Sample and True Peak Metering](https://www.masteringthemix.com/blogs/learn/inter-sample-and-true-peak-metering)
- [Sound on Sound: Q. Are inter-sample peaks causing my mix to distort?](https://www.soundonsound.com/sound-advice/q-inter-sample-peaks-causing-mix-distortion)
- [LuvLang: True Peak Limiting Explained](https://luvlang.studio/blog/true-peak-limiting-explained)
- [Remasterify: True Peak 101](https://blog.remasterify.com/true-peak-101-everything-you-need-to-know/)
- [Youlean Loudness Meter 2](https://youlean.co/youlean-loudness-meter/)
- [Youlean: Loudness Standards Comparison Table](https://youlean.co/loudness-standards-full-comparison-table/)
- [Wikipedia: EBU R 128](https://en.wikipedia.org/wiki/EBU_R_128)
- [iMusician: Understanding the Loudness War in Mastering in 2025](https://imusician.pro/en/resources/blog/mastering-and-the-loudness-war-an-update)
