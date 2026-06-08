# Compression Fundamentals

**Scope:** mixing
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Mike Senior, *Mixing Secrets for the Small Studio*; Roey Izhaki, *Mixing Audio*; iZotope *Mixing Guide*
**Tags:** `mixing`, `compression`, `transient`, `parallel-processing`, `vocal-mixing`, `recipe`

---

## The five parameters as moves, not abstractions

Compression is easier to learn when you treat each parameter as a question, not a number. **Threshold** asks "at what level should the compressor start working?" — anything louder gets reduced. **Ratio** asks "how hard should it pull?" — a 4:1 ratio means every 4 dB above threshold becomes 1 dB at the output. **Attack** asks "how fast should it react?" — slow attacks let transients punch through, fast attacks clamp them. **Release** asks "how fast should it let go?" — too fast pumps, too slow keeps the compressor stuck. **Knee** asks "how gradually should it engage near threshold?" — a soft knee starts ratcheting up the ratio gradually for transparency, a hard knee snaps in for aggression. [Audio University's compression explainer](https://audiouniversityonline.com/compression-explained/) and [Mastering.com](https://mastering.com/compression-explained-threshold-ratio-and-knee/) both teach the parameters in roughly this order, and the order itself is instructive: set threshold last, after you've decided what kind of move you want.

## Attack as transient sculpting

The attack control is the single most misunderstood parameter, because the intuitive guess is wrong. To make a snare *more* punchy with compression, you use a *slower* attack, not a faster one. [Mixing Lessons](https://www.mixinglessons.com/compression-attack-explained/) and [StockMusicMusician's snare guide](https://www.stockmusicmusician.com/blog/snare-drum-compression) explain why: a slow attack lets the initial stick transient pass through uncompressed, then clamps down on the body — so the relative loudness of the transient vs. body increases, which the ear reads as "more punch." A fast attack does the opposite: it catches the transient itself and squashes it, which can sound tame or flat. The corollary is that fast attack is the right move when you actually want to tame a transient — controlling a peaky vocal consonant, taming a clicky bass note, or limiting a drum bus.

## Release as breathing and groove

Release is where over-compression usually shows up. Set it too fast and the compressor pumps audibly between hits; set it too slow and gain reduction never recovers, killing the dynamic envelope. The practical rule, taught in [Music Guy Mixing's compression guides](https://www.musicguymixing.com/snare-compression/) and elsewhere, is to time the release so the meter needle returns to zero just before the next hit. On a snare with a backbeat at 100 BPM, that lands around 150–250 ms; on a held vocal note, much slower (300–500 ms or auto); on a hi-hat with constant 16ths, fast (around 50 ms). Many modern compressors offer "auto" release that follows program material — this is a great safety net on busy program like drum bus or mix bus, where a fixed release would inevitably catch a fill or transition wrong.

## Ratio choice and the limiter threshold

Ratios from 1.5:1 to 4:1 are gentle and tend to read as "shaping" rather than "compressing." 4:1 to 8:1 is the working range for noticeable control — pop vocals, snare drums, bass guitar. Anything above 10:1 is, per [HighQualityBeats](https://www.highqualitybeats.com/post/explain-every-button-on-a-compressor) and most engineers, effectively limiting — past that point, additional ratio increase barely changes behavior. The trap is reaching for high ratios when you should be lowering the threshold instead: 4:1 with -12 dB of gain reduction is much more invasive than 8:1 with -3 dB. Watch the gain-reduction meter, not the ratio knob. The right amount of compression is usually less than you think — most pop vocal moves land in the 2–6 dB GR range on the main compressor.

## VCA character

VCA (voltage-controlled amplifier) compressors are clean, fast, and accurate. [Mastering.com's compressor types overview](https://mastering.com/compression-explained-fet-vca-optical-variable-mu/) and [SimplyMixing](https://www.simplymixing.com/blog/audio-compressor-types) describe them as the "transparent" workhorses — minimal color, precise time constants, great for surgical control. Classics: the dbx 160 and the SSL G-series bus compressor. VCAs are the default choice for drum-bus glue and mix-bus glue because they handle complex program without imparting obvious character. On individual tracks, VCAs can sound clinical if pushed hard, which is why engineers often chain them after a more colored stage.

## Opto character

Optical compressors use a light element coupled to a light-dependent resistor; the resistor lags slightly, producing program-dependent attack and release that feel smooth and musical. The [iZotope analog-compression overview](https://www.izotope.com/en/learn/4-types-of-analog-compression-and-why-they-matter-in-a-digital-world.html) and [MusicRadar's LA-2A guide](https://www.musicradar.com/news/producers-guide-la-2a) describe the LA-2A as the archetype — fixed ratio around 3:1, fixed time constants averaging ~10 ms attack and ~60 ms release. Opto is the classic "set and forget" vocal compressor: feed it a vocal, twist gain until the needle wiggles 3–6 dB, done. It rounds peaks gently rather than catching transients, which makes it less useful for transient-heavy material (snares, plucked basses) and excellent for sustained material (vocals, sustained synth pads, electric piano).

## FET character

FET (field-effect transistor) compressors emulate the behavior of the Universal Audio 1176. They are *fast* — attack times measured in microseconds — and they color the signal with a midrange-forward, slightly distorted character when pushed. [UA's 1176 tips page](https://www.uaudio.com/blogs/ua/1176-collection-tips) and [Audiospectra](https://audiospectra.net/how-to-use-the-1176-compressor/) cover the classic moves: 4:1 ratio with moderate attack and release for vocals, 8:1 for harder vocal control, and the famous "all buttons in" mode (4-8-12-20 simultaneously) for aggressive parallel drum smashing. FET works well on snares, lead vocals, electric guitar, and as the front-end of a vocal compressor chain ahead of an opto. The character is the point — if you want clean, reach for a VCA instead.

## Variable-mu character

Variable-mu compressors compress by varying the bias of a vacuum tube. They are slow, program-dependent, and add harmonic warmth. [Mastering.com](https://mastering.com/compression-explained-fet-vca-optical-variable-mu/) notes that the effective ratio increases with gain reduction — the louder a peak, the harder the compressor pulls — which produces a self-balancing behavior on dense program. The Manley Variable-Mu and Fairchild 670 are the references. The classic application is mix-bus or mastering-chain glue with a tube character. Less common for individual track compression because of the slower time constants and the warm coloration, both of which usually serve the whole mix better than a single instrument.

## Vocal compression starting point

A reliable lead-vocal starting point, drawn from [LedgerNote's vocal compression guide](https://ledgernote.com/columns/mixing-mastering/how-to-compress-vocals/) and [Music Guy Mixing](https://www.musicguymixing.com/compressor-settings-for-vocals/): ratio 3:1 or 4:1, attack around 10–30 ms (fast enough to catch peaks but slow enough to preserve word transients), release 50–150 ms (or auto), targeting 3–6 dB of gain reduction on the loudest phrases. Pop vocals often use the "two compressor" approach: a gentler first compressor (LA-2A style, slow, 2–4 dB GR) doing broad leveling, followed by a faster, harder second compressor (1176 style, 4:1 or 8:1, 2–4 dB GR) catching the remaining peaks. The two-stage chain controls dynamics with less audible artifacts than asking one compressor to do all the work.

## Snare and kick compression

Drum compression is mostly about transient shaping, not level control. For a punchy snare, [StockMusicMusician](https://www.stockmusicmusician.com/blog/snare-drum-compression) and [Audiospectra](https://audiospectra.net/snare-compression-settings/) consistently recommend a ratio around 3:1 or 4:1, an attack of 20–30 ms (slow enough to let the stick through), and a release timed to the groove (150–250 ms at moderate tempos), with 2–5 dB of gain reduction. Kicks follow similar logic — slow attack preserves beater click while compressing body. The most common failure mode is fast attack on snare or kick: the transient gets sliced off and the drum loses its impact entirely. If your drum feels flatter after compression, the attack is almost certainly too fast.

## Bass compression

Bass needs more consistent compression than most sources because the goal is even level throughout the song — every note should land at roughly the same loudness on the listener's speakers. The [Nail The Mix bass compression guide](https://www.nailthemix.com/how-to-use-compression-on-bass-guitar) and [eMastered](https://emastered.com/blog/bass-compression) recommend starting with an opto-style compressor (LA-2A) at gentle 2:1 to 4:1 with 3–6 dB of GR for smoothing, then optionally adding a faster compressor afterwards to catch peaks. Heavy fingerstyle bass often benefits from a chain: opto for leveling, then 1176 or VCA for peak control. Slap bass typically wants more aggressive compression than fingerstyle because the dynamic range of the attack is larger.

## Parallel compression (the "New York" trick)

Parallel compression sends a copy of a track to an auxiliary bus, crushes it on the aux, and blends it back under the dry. The dry track carries transients and dynamics; the crushed track adds density, sustain, and excitement. The classic drum-bus version, described in [Pro Audio Files](https://theproaudiofiles.com/parallel-compression/) and [SonicScoop](https://sonicscoop.com/parallel-compression/), uses an 1176-style FET compressor with fast attack, fast release, and ratio 8:1 or higher (or "all buttons in"), aimed at 10–15 dB of gain reduction. You blend in 10–20 dB below the dry — the result is drums that feel bigger and more sustained without losing their snap. The same technique applies to vocals (subtle aggression and presence) and full mixes (the famous "smash bus" used on hip-hop drums).

## Serial compression: gentle then peak

Serial compression chains two or more compressors with light-to-moderate gain reduction at each stage, doing less audible damage than one heavy stage. The canonical vocal chain — also widely used on bass — is opto (slow, 2–4 dB GR, leveling the take overall) followed by FET or VCA (fast, 2–4 dB GR, catching peaks the opto missed). Each stage handles the dynamic range it's best at. Serial chains also let you split jobs: a multiband compressor handling sibilance frequencies separately from a broadband compressor handling level, or a slow LA-2A managing breath-to-breath dynamics while a fast 1176 polices individual word peaks. The principle: small moves stacked beat one big move every time.

## Mix-bus glue

Mix-bus compression is its own discipline. The conventional starting point on an SSL G-style bus compressor, per [Music Guy Mixing's bus compression guide](https://www.musicguymixing.com/bus-compression/) and the [Nail The Mix master bus tutorial](https://www.nailthemix.com/andrew-wade-master-bus-compression), is ratio 2:1 or 4:1, attack 10–30 ms, release auto, threshold set for 1–3 dB of gain reduction on the loudest sections. The point is *glue*, not control — a slight, consistent breathing across the whole mix that helps separately-mixed elements feel like they're in the same room. Pushing harder than 3 dB on the bus tends to flatten drum transients and lose punch in a way that can't be undone in mastering. Some engineers print with mix-bus compression on from the start so balances are made through it.

## Over-compression warning signs

The four classic symptoms, catalogued in [iZotope's signs of over-processing](https://www.izotope.com/community/blog/5-signs-of-over-processing-in-a-mix) and [Mastering The Mix's compression mistakes](https://www.masteringthemix.com/blogs/learn/7-compression-mistakes-that-can-ruin-your-music): (1) audible pumping — the noise floor and reverb tails breathe in time with the kick; (2) lost transients — kicks and snares that used to crack now thud; (3) lifeless dynamics — the chorus sounds the same loudness as the verse despite identical fader positions; (4) ear fatigue within minutes of listening. The diagnostic test is the bypass A/B: level-match the compressed and bypassed versions and listen for which feels more alive. If "bypassed" wins, dial the compression back. The temptation to push for "louder" or "fatter" almost always overshoots; less compression with better tone usually beats more.

## Cited Retrieval Topics

- "what's a good attack time for vocal compression"
- "how do i make a snare drum punchier with compression"
- "what's the difference between vca and opto compressors"
- "parallel compression settings for drums"
- "how much gain reduction should i use on the mix bus"
- "why does my mix sound lifeless after compression"
- "1176 vs la-2a on vocals which to use first"
- "how do i compress bass guitar"
- "what ratio should i use on a pop vocal"
- "what does the knee setting do on a compressor"

## Sources

- [Audio University — How to Use a Compressor](https://audiouniversityonline.com/compression-explained/)
- [Mastering.com — Compression Explained: Threshold, Ratio and Knee](https://mastering.com/compression-explained-threshold-ratio-and-knee/)
- [Mastering.com — Compression Explained: FET, VCA, Optical, Variable-Mu](https://mastering.com/compression-explained-fet-vca-optical-variable-mu/)
- [Mixing Lessons — Compression Attack Explained](https://www.mixinglessons.com/compression-attack-explained/)
- [High Quality Beats — How to Use a Compressor](https://www.highqualitybeats.com/post/explain-every-button-on-a-compressor)
- [iZotope — 4 Types of Analog Compression](https://www.izotope.com/en/learn/4-types-of-analog-compression-and-why-they-matter-in-a-digital-world.html)
- [SimplyMixing — Audio Compressor Types](https://www.simplymixing.com/blog/audio-compressor-types)
- [Universal Audio — 1176 Tips & Tricks](https://www.uaudio.com/blogs/ua/1176-collection-tips)
- [Audiospectra — How to Use the 1176 Compressor](https://audiospectra.net/how-to-use-the-1176-compressor/)
- [MusicRadar — Producer's Guide to the Teletronix LA-2A](https://www.musicradar.com/news/producers-guide-la-2a)
- [LedgerNote — How to Compress Vocals](https://ledgernote.com/columns/mixing-mastering/how-to-compress-vocals/)
- [Music Guy Mixing — Best Compressor Settings for Vocals](https://www.musicguymixing.com/compressor-settings-for-vocals/)
- [StockMusicMusician — How to Compress Snare](https://www.stockmusicmusician.com/blog/snare-drum-compression)
- [Music Guy Mixing — Snare Compression Settings](https://www.musicguymixing.com/snare-compression/)
- [Audiospectra — Snare Compression Settings](https://audiospectra.net/snare-compression-settings/)
- [Nail The Mix — How to Use Compression on Bass Guitar](https://www.nailthemix.com/how-to-use-compression-on-bass-guitar)
- [eMastered — Bass Compression: The Definitive Guide](https://emastered.com/blog/bass-compression)
- [Pro Audio Files — 6 Favorite Ways to Use Parallel Compression](https://theproaudiofiles.com/parallel-compression/)
- [SonicScoop — Comprehensive Guide to Parallel Compression](https://sonicscoop.com/parallel-compression/)
- [Music Guy Mixing — Bus Compression Guide](https://www.musicguymixing.com/bus-compression/)
- [Nail The Mix — Andrew Wade on Master Bus Compression](https://www.nailthemix.com/andrew-wade-master-bus-compression)
- [iZotope — 5 Signs of Over-Processing in a Mix](https://www.izotope.com/community/blog/5-signs-of-over-processing-in-a-mix)
- [Mastering The Mix — 7 Compression Mistakes](https://www.masteringthemix.com/blogs/learn/7-compression-mistakes-that-can-ruin-your-music)
