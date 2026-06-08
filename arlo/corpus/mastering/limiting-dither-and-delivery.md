# Limiting, Dither, and Delivery

**Scope:** mastering
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Bob Katz, *Mastering Audio: The Art and the Science* (3rd ed., 2015); iZotope, *Mastering with Ozone* / Ozone Help (in corpus); FabFilter Pro-L 2 manual
**Tags:** `mastering`, `limiting`, `dither`, `delivery`, `file-format`, `recipe`

---

## What the brickwall limiter actually does

The final-stage mastering limiter is a **brickwall** limiter: it sets a hard ceiling that the output cannot exceed, no matter how loud the input drives in. Mechanically, it combines a fast peak-catcher (with lookahead) and a slower release envelope that responds to average dynamics. Push the input above the ceiling and the limiter pulls gain down by exactly the amount needed to stay under the ceiling, then releases back. The [FabFilter Pro-L 2 manual](https://www.fabfilter.com/help/pro-l/using/advancedsettings) describes the two stages as a "transient" stage (the lookahead-based peak catcher) and a "release" stage (the slower envelope that responds to program loudness). Both stages matter — the transient stage controls peak distortion, the release stage controls how much pumping you hear.

## The four limiter parameters (ceiling, threshold, release, lookahead)

**Ceiling (output level):** the absolute maximum the limiter will output, set to the platform's true-peak requirement. For streaming, –1 dBTP is universal; –1.5 dBTP is the safer default that mastering engineers like Mat Leffler-Schulman recommend for any lossy-bound master ([Leffler-Schulman on true peaks](https://matlefflerschulman.com/mastering-articles/true-peak-vs-inter-sample-peaks)). Always enable True Peak limiting on the plugin — sample-peak limiting alone doesn't stop inter-sample distortion.

**Threshold (input gain):** how hard you drive into the limiter. The [FabFilter Pro-L manual](https://www.fabfilter.com/help/ffprol-manual.pdf) frames this as "adding gain to a signal that hits this ceiling will increase the amount of limiting." Aim for 1–4 dB of gain reduction on the loudest sections of a mainstream pop master; less for dynamic genres. More than ~6 dB of limiting flattens transients audibly.

**Release:** how fast the limiter recovers after pulling gain down. Short release (5–30 ms) sounds more aggressive and louder but pumps audibly; long release (100–300 ms) sounds smoother but reduces apparent loudness. Most modern limiters offer auto-release that adapts per-signal — a sensible default unless you want a specific character.

**Lookahead:** how far ahead the limiter "sees" incoming audio so it can begin reducing gain before the peak arrives. Short lookahead (0.5–1 ms) preserves transients and pushes loudness but risks distortion; long lookahead (3–5 ms) is safer and smoother but transients can lose snap.

## Limiter character — transparent vs. colored

Modern limiters offer multiple algorithms with different sonic fingerprints. [FabFilter Pro-L 2](https://www.fabfilter.com/products/pro-l-2-limiter-plug-in) ships with eight: Transparent, Punchy, Dynamic, Allround, Aggressive, Modern, Bus, and Safe. The two ends of the axis:

- **Transparent** algorithms ([Pro-L 2's "Transparent" mode](https://www.fabfilter.com/help/pro-l/using/advancedsettings), iZotope Ozone Maximizer's IRC IV, Waves L3): stay neutral, no audible character, ideal when the mix already has the tone and you just need ceiling control. Best for acoustic, classical, jazz, and any genre where preserving micro-dynamics matters.
- **Colored** algorithms (FabFilter "Modern" or "Aggressive," Slate FG-X, Newfangled Audio Elevate's clip mode, plus classic hardware emulations like the Maselec MPL-2): add saturation, soft clipping, or shaping that imparts character. Useful for pop, EDM, and trap where some grit and "glue" from the limiter is part of the sound. The trade is some harmonic distortion in exchange for perceived loudness without as much gain reduction.

The practical rule: if you're doing more than 3 dB of gain reduction with a transparent limiter and it sounds flat, switch to a colored algorithm before pushing harder. The colored algo will get you the same loudness with less audible transient loss.

## Dither — what it is and when to use it

Dither is **low-level noise added when reducing bit depth** to mask truncation distortion. Without dither, 24→16-bit conversion truncates the lower 8 bits of each sample, producing a quantization error that correlates with the signal — audible as a granular, harsh artifact most obvious on fadeouts, reverb tails, and quiet passages. [iZotope's dither explainer](https://www.izotope.com/en/learn/what-is-dithering-in-audio) and [Wisseloord Studios](https://wisseloord.org/academy/what-is-dithering-and-when-do-you-need-it) both describe truncation as "everything sounds grainy and loses that natural smoothness." Dither converts that correlated distortion into uncorrelated low-level noise — much less perceptually objectionable, and below the noise floor of most listening environments anyway.

## TPDF, RPDF, and noise shaping

Dither comes in flavors that trade noise floor against perceptual transparency:

- **RPDF (rectangular)**: simplest, doesn't fully decorrelate quantization errors. Rarely used in modern mastering.
- **TPDF (triangular probability density function)**: the standard mastering choice. Fully decorrelates quantization at the cost of slightly higher noise (~3 dB above RPDF). Noise floor sits around –93 dBFS A-weighted ([Goodhertz Good Dither manual](https://goodhertz.com/good-dither/manual/)).
- **Noise-shaped TPDF**: starts with TPDF, then frequency-shapes the noise so its energy moves above ~15 kHz where the ear is least sensitive. Perceived noise floor can be 10–12 dB lower, but high-frequency noise content above 16 kHz is higher. [FabFilter Pro-L 2's dither documentation](https://www.fabfilter.com/help/pro-l/using/dithering) and iZotope Ozone offer multiple noise-shaping curves (light, medium, aggressive).

Default for streaming/CD delivery: **TPDF with moderate noise shaping** is safe across all genres. Aggressive noise shaping is fine for full-range modern pop but can audibly tilt the top end on quiet acoustic material.

## When (and when not) to apply dither

Apply dither **exactly once**, at the **very last** word-length reduction step. The most common mistake — dithering at multiple stages of a chain — accumulates noise rather than canceling earlier errors. [Mat Leffler-Schulman's dither deep-dive](https://matlefflerschulman.com/mastering-articles/dither-in-mastering-a-deep-dive) is direct about this: "Each pass is not replacing the previous error. It is adding to it."

**Apply dither when:**
- Bouncing 24-bit → 16-bit for CD or any 16-bit deliverable: TPDF (with or without noise shaping).
- Bouncing 32/64-bit float → 24-bit for streaming delivery: gentle TPDF (audibly inaudible but conceptually correct).

**Do NOT apply dither when:**
- Exporting 24-bit from a 24-bit session destined for further mastering. The next engineer needs full precision; you'll dither at the final step.
- Bouncing at the same or higher bit depth than the source (e.g., a 24-bit session out at 24-bit float).

## Bit depth and sample rate decisions

Three common scenarios:

- **CD master:** 16-bit / 44.1 kHz, dithered. Required by the Red Book CD spec.
- **Streaming master (DistroKid, TuneCore, etc.):** 16-bit or 24-bit / 44.1 kHz WAV is universally accepted. 24-bit is preferred when the distributor allows it because it preserves dynamic resolution before the streaming service's own AAC/Opus transcode.
- **Apple Digital Masters / high-res streaming:** **24-bit / 88.2 kHz or higher** WAV file is required, with true peak never above –1 dBTP ([Apple Digital Masters documentation](https://www.apple.com/apple-music/apple-digital-masters/docs/apple-digital-masters.pdf)). Apple's encoder uses the extra resolution to produce AAC files that the company claims are "virtually indistinguishable from the original 24-bit studio masters."

For sample rate: master at the session rate (typically 48 kHz or 96 kHz). Don't upsample for the sake of upsampling — there's no audio quality benefit and you risk a clumsy SRC down at delivery. [Sonarworks](https://www.sonarworks.com/blog/learn/sample-rate) notes that "most listeners can't distinguish between a well-recorded 44.1 kHz file and its 96 kHz counterpart in blind tests."

## Sample rate conversion (SRC) quality

When you do need to convert (e.g., 96 kHz session → 44.1 kHz CD master), use a high-quality SRC. Modern DAW-native SRC (Pro Tools Master, Logic, Reaper SRC mode 4+) is generally excellent. Older or lower-mode SRC can introduce subtle aliasing — high frequencies folding back as inaudible-but-measurable artifacts. If you're SRC'ing a heavily-limited master, do the SRC *before* the final limiter if possible, because limiting introduces inter-sample peaks that the SRC then has to handle. The professional workflow: bounce a full-resolution master, then SRC and re-limit at the target rate.

## WAV vs. AIFF vs. FLAC for delivery

For streaming distribution, **WAV is the universal default**. Every aggregator (DistroKid, TuneCore, CD Baby, AWAL) accepts WAV; most also accept FLAC and AIFF. [The Pro Audio Files](https://theproaudiofiles.com/audio-mastering-format-and-delivery-guide-2014/) and [Chroma Mastering](https://www.chromamastering.com/master-formats-and-metadata-a-comprehensive-guide-for-music-distribution/) both name WAV as the de-facto standard.

- **WAV (Windows)**: PCM, uncompressed, universal support, limited metadata. Default delivery format.
- **AIFF (Apple)**: PCM, uncompressed, mathematically identical to WAV, slightly better metadata embedding (ID3 tags). Common in Apple-centric workflows.
- **FLAC**: lossless compression — bit-identical to PCM on decode, ~40–60% smaller files. Good for archive and high-res download stores (Bandcamp, Qobuz). Not all CD-replication pipelines accept FLAC.

For streaming distribution: deliver **24-bit WAV at session sample rate** (44.1 kHz minimum, 48 kHz or higher if the master was done at that rate). For CD: deliver **16-bit / 44.1 kHz WAV with dither** — or a DDP image (see below).

## DDP for album / CD delivery

A **DDP (Disc Description Protocol) image** is a digital container holding all the audio tracks, track IDs, CD-Text (album title, track titles, artist), ISRC codes, and Red Book sequencing metadata for an album. [JustMastering's DDP writeup](https://www.justmastering.com/article-ddpfileformat.php) and [Critical Listening Lab](https://www.criticallisteninglab.com/en/learn/delivery-formats/cd-ddp) both call DDP the universal preferred format for CD replication. The advantage over individual WAV files: track gaps, fade-outs that overlap into the next track, CD-Text, and ISRCs are all baked in and can't be reshuffled by the replicator. Submitting individual WAVs to a CD plant invites sequencing errors, missing CD-Text, and even subtle audio drift from how the plant assembles the disc.

DDP is **not** used for streaming distribution. Aggregators want individual files (one WAV per track). The workflow split: streaming gets individual 16- or 24-bit WAVs; CD/vinyl manufacturing gets a DDP. Album mastering sessions produce both deliverables from the same masters.

## Vinyl-specific considerations (brief)

A vinyl master differs from a streaming master in three ways: (1) low-end below ~150 Hz must be tightly mono'd or the cutter lathe can't track the groove; (2) sibilance and bright transient content above ~10 kHz needs to be tamed because of the limited tracking ability of the stylus; (3) overall LUFS is necessarily quieter (around –12 to –14) because the lathe has physical limits on peak velocity. If the album is going to vinyl, ask the cutting engineer for their preferred delivery — typically high-resolution WAV (24-bit / 96 kHz) with the streaming-master loudness moves *backed off* a couple dB.

## Final-bounce checklist

Before delivering, confirm:

1. **Ceiling**: master is below –1 dBTP (or –2 dBTP for Spotify safety). Verify on a true-peak meter, not just sample peak.
2. **LUFS**: integrated LUFS is appropriate for genre/platform (–14 LUFS is the safe streaming default).
3. **Dither**: applied exactly once at the final word-length conversion. Not applied if delivering 24-bit to another engineer.
4. **Format**: WAV, correct bit depth and sample rate per spec.
5. **Mono check**: passes without low-end collapse.
6. **No clicks or pops at the boundaries**: trim the head with a tiny fade-in, end with a clean fade-out (a sample-accurate cut at a non-zero amplitude can click on some players).
7. **File naming**: `Artist - Title.wav` with no extra punctuation; some aggregators reject files with brackets or special characters.
8. **Bounce, listen back end-to-end**: catch dropouts, render glitches, and last-minute plugin freezes before delivery.

---

## Cited Retrieval Topics

- "what release time should i use on a mastering limiter"
- "what's the difference between transparent and colored limiters"
- "do i need to apply dither when bouncing"
- "what is tpdf dither vs noise shaping"
- "what bit depth and sample rate for streaming delivery"
- "should i deliver wav or flac to my distributor"
- "what is a ddp file and when do i need one"
- "how much gain reduction is too much on a limiter"
- "what file format does apple digital masters require"
- "do i dither a 24 bit master going to a mastering engineer"

## Sources

- [FabFilter Pro-L 2 manual (PDF)](https://www.fabfilter.com/downloads/pdf/help/ffprol2-manual.pdf)
- [FabFilter Pro-L 2 — Advanced Settings](https://www.fabfilter.com/help/pro-l/using/advancedsettings)
- [FabFilter Pro-L 2 — Dithering and Noise Shaping](https://www.fabfilter.com/help/pro-l/using/dithering)
- [FabFilter Pro-L 2 product page](https://www.fabfilter.com/products/pro-l-2-limiter-plug-in)
- [iZotope: What Is Dithering in Audio?](https://www.izotope.com/en/learn/what-is-dithering-in-audio)
- [Goodhertz Good Dither manual](https://goodhertz.com/good-dither/manual/)
- [Wisseloord Studios: What is dithering and when do you need it?](https://wisseloord.org/academy/what-is-dithering-and-when-do-you-need-it)
- [Mat Leffler-Schulman: Dither in Mastering — A Deep Dive](https://matlefflerschulman.com/mastering-articles/dither-in-mastering-a-deep-dive)
- [Mat Leffler-Schulman: True Peak vs Inter-Sample Peaks](https://matlefflerschulman.com/mastering-articles/true-peak-vs-inter-sample-peaks)
- [The Pro Audio Files: Mastering Guide to Audio Formats and Delivery Mediums (2026 update)](https://theproaudiofiles.com/audio-mastering-format-and-delivery-guide-2014/)
- [Chroma Mastering: Master Formats and Metadata Guide](https://www.chromamastering.com/master-formats-and-metadata-a-comprehensive-guide-for-music-distribution/)
- [JustMastering: DDP File Format Explained](https://www.justmastering.com/article-ddpfileformat.php)
- [Critical Listening Lab: CD & DDP — Red Book Standard](https://www.criticallisteninglab.com/en/learn/delivery-formats/cd-ddp)
- [Apple Digital Masters — Mastering Engineer Documentation (PDF)](https://www.apple.com/apple-music/apple-digital-masters/docs/apple-digital-masters.pdf)
- [Sonarworks: Understanding Sample Rate](https://www.sonarworks.com/blog/learn/sample-rate)
