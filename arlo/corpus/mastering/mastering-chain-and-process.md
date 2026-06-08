# The Mastering Chain and Process

**Scope:** mastering
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Bob Katz, *Mastering Audio: The Art and the Science* (3rd ed., 2015); iZotope, *Mastering with Ozone* / Ozone Help (in corpus); Sound on Sound mastering features
**Tags:** `mastering`, `mastering-chain`, `principle`, `methodology`

---

## The canonical mastering chain

A working default chain for stereo mastering is: **corrective EQ → multiband compression (or dynamic EQ) → glue compression → saturation/exciter → stereo imaging → limiter**. [iZotope's signal-chain breakdown](https://www.izotope.com/community/blog/what-is-an-ideal-mastering-signal-chain) frames the same idea as "corrective before sweetening, linear before non-linear" — fix tone with EQ first so that downstream compressors react to a balanced signal rather than chasing problem frequencies. The limiter (or "Maximizer" in Ozone terminology) is always last because everything before it shapes what the limiter has to manage. Most projects don't need every module — iZotope's own guidance is that "most songs can be mastered with an EQ or two, the occasional compressor, and a limiter," and that loudness should be built earlier in the chain rather than created by the limiter at the end ([iZotope: advanced mastering tips](https://www.izotope.com/en/learn/advanced-mastering-tips)).

## When to deviate from the canonical order

The order is a starting point, not a law. Two common, defensible deviations: (1) putting a colored compressor or tape saturator *before* corrective EQ when the compressor is being used as a tone-shaping device rather than as level control, and (2) putting a gentle "glue" compressor first to set a consistent envelope before fine-tuning EQ. [Mastering Chain Order Explained](https://luvlang.studio/blog/mastering-chain-order-explained) notes that some engineers prefer compression before corrective EQ when the compressor's nonlinearity is part of the desired tone. The rule of thumb: if you're *fixing* something, do it linearly first; if you're *coloring* something, position is taste. Dynamic EQ often replaces multiband compression entirely in modern mastering because it's more surgical — useful when a mix has, say, a 250 Hz buildup only on choruses.

## Step zero — listen and reference before any plugin

Before inserting a single plugin, mastering engineers do two things: (1) listen to the unprocessed mix in full at a calibrated monitoring level (Bob Katz advocates 83 dB SPL C-weighted per channel as a reference standard in [*Mastering Audio*, 3rd ed.](https://www.routledge.com/Mastering-Audio-The-Art-and-the-Science/Katz/p/book/9780240818962)), and (2) pull up two or three reference tracks in the same genre. The reference establishes target tonal balance, loudness, and stereo width. As [Sound on Sound's review of Katz's book](https://www.soundonsound.com/reviews/bob-katz-mastering-audio) summarizes, "loudness can be made almost objective by adopting carefully calibrated monitoring levels." Without calibration, every loudness judgement is a guess.

## Reference-track loudness matching first

The most important step before A/B-ing against a reference is loudness matching. [Mastering The Mix](https://www.masteringthemix.com/blogs/learn/how-to-use-reference-tracks-when-mastering) makes this point bluntly: "we instinctively perceive louder music as clearer, punchier, and fuller in the low end, even when it's not better. This illusion is the silent saboteur behind countless poor mix decisions." Match the integrated LUFS of your mix to your reference (within ~0.5 LU) before judging tone or dynamics. Many DAWs have a "loudness match" toggle in the meter; if not, drop both into a meter like Youlean Loudness Meter and offset the reference channel until integrated LUFS reads the same.

## Tonal balance check

After loudness matching, listen for broad spectral tilt against your reference. A practical diagnostic [Mastering The Mix](https://www.masteringthemix.com/blogs/learn/how-to-use-reference-tracks-when-mastering) recommends: instantiate a 3-band EQ on the master with a low shelf at 100 Hz, a peak band at 400 Hz, and a high shelf at 8 kHz, all wide and gentle. A/B against the reference and look at how much you have to push each band to match. If you're boosting the low shelf by 3 dB just to match a reference, that's a tonal-balance call that EQ should make permanently — not a "louder is better" illusion. iZotope's Tonal Balance Control plugin automates this comparison against curated genre curves.

## Mono check and low-end discipline

Mid-process and again before bouncing, fold the master to mono and listen. The two things that go wrong: (1) low end gets weaker because of phase cancellation between L/R sub content, and (2) reverb/widening effects collapse and reveal balance issues. The accepted fix is to **mono everything below ~100–120 Hz** with a stereo-imager band-split or a mid/side EQ that cuts the side signal in the low end. [Audiospectra](https://audiospectra.net/mono-compatibility-mastering/) notes that "most club PA systems run mono below the crossover point (~100–120 Hz), and if your sub-bass has stereo content, it will partially cancel on these systems." Phone speakers and many Bluetooth speakers are mono as well, so this isn't a club-only concern. A small loss of high-frequency air in mono is acceptable; a hollow or thin low end is a red flag.

## Corrective EQ moves

Corrective EQ in mastering is small and targeted. Typical surgical moves: a wide low-shelf cut of 0.5–1.5 dB around 200–300 Hz to clear mud, a narrow ~3 dB cut at a specific resonance the mix engineer didn't catch (often a vocal honk around 700 Hz or a snare ring around 900 Hz), and a gentle high shelf to either add air (+1 dB at 12 kHz) or tame sibilance (–1 dB at 6 kHz). The discipline: **if you're moving more than 3 dB anywhere on a mastering EQ, the mix probably needs to go back to the mix engineer**. Big EQ moves at the mastering stage almost always indicate an unresolved mix problem. [iZotope's mastering chain guide](https://www.izotope.com/en/learn/what-is-an-ideal-mastering-signal-chain.html) recommends "as little as possible to effectively achieve the desired result."

## Multiband compression and dynamic EQ

Multiband compression splits the spectrum into 3–4 bands and compresses each independently. Common bands: sub (below 120 Hz), low-mid (120–800 Hz), mid (800 Hz–5 kHz), high (5 kHz+). Use it to tame a single misbehaving range — e.g., if the low-mid pumps inconsistently across a track, a multiband band at 200–400 Hz with a 2:1 ratio and slow attack/release will even it out without affecting the rest of the mix. Dynamic EQ is the modern alternative: it only engages when a band exceeds a threshold, so it's gentler than a static EQ cut. iZotope's [advanced mastering tips](https://www.izotope.com/en/learn/advanced-mastering-tips) suggests inserting dynamic EQ early in the chain specifically to handle these moment-by-moment spectral spikes before they hit the glue compressor.

## Glue compression

The "glue" compressor is a gentle, full-band bus compressor that ties the mix together — typically a VCA-style unit (think SSL bus comp) or its emulation. Defaults in the genre: 2:1 ratio, slow attack (10–30 ms) to preserve transients, auto-release, threshold set for 1–3 dB of gain reduction on the loudest sections. More than ~3 dB of gain reduction at this stage tends to flatten dynamics in a way listeners can hear as lifelessness. The job is cohesion, not loudness — loudness comes from the limiter.

## Saturation and exciter placement

Saturation adds harmonic content that makes the master feel louder at the same LUFS, and it can add perceived "warmth" or "air" depending on the algorithm. Standard placement is *after* compression — saturating before compression makes the compressor chase harmonics rather than the original transients. [iZotope's advanced mastering tips](https://www.izotope.com/en/learn/advanced-mastering-tips) recommends multiband saturation focused on mids and highs (10–30% mix), and explicitly warns against saturating sub frequencies because it muddies low-end clarity. Tape emulation is a common subtle choice; aggressive exciter is genre-specific (pop, EDM yes; folk, classical no).

## Limiter as final stage, not the loudness creator

The limiter's job is to set the final ceiling and catch peaks that snuck through everything else — not to be the primary loudness tool. If you need more than 3–4 dB of gain reduction from the limiter to hit your LUFS target, push the upstream compression and saturation harder instead. Enable True Peak limiting (essential for streaming; see the LUFS reference doc in `corpus/reference/spotify-loudness-normalization.md`). [iZotope](https://www.izotope.com/en/learn/advanced-mastering-tips) puts it directly: "Build loudness earlier in chain and let limiter finalize, not create, loudness."

## One-pass vs. two-pass mastering

One-pass mastering means processing the mix in a single chain on the master bus. Two-pass means rendering after the corrective stage, then re-loading the bounced file into a fresh session for the sweetening + limiting chain. The advantage of two-pass: you can listen fresh to the corrected version and make better creative decisions for the sweetening stage, and you avoid plugin-CPU artifacts in long chains. The cost: more time. Most modern in-the-box mastering is one-pass with a well-organized chain; engineers who came up on analog gear often still print between stages out of habit and because it forces a commitment.

## Album mastering vs. single mastering

Mastering an album is fundamentally a *relative* problem; mastering a single is an *absolute* problem. For a single, the goal is to be competitive in genre context. For an album, the goal is internal consistency — perceived vocal level, tonal balance, and energy across tracks should feel continuous, even if individual track LUFS varies. [Alexander Wright Mastering](https://alexanderwright.com/blog/mastering-albums-vs-singles) notes that "consistency doesn't mean making everything the same loudness level" — an atmospheric intro shouldn't be slammed to the same LUFS as the lead single. The album-specific moves: matching perceived vocal level track-to-track (a –14 LUFS ballad and a –9 LUFS banger should sound like the same singer); setting track spacing (typically 2–4 seconds of silence, sometimes overlap fades); and confirming a smooth tonal arc from track 1 to track 12.

## Bounce, sleep, listen elsewhere

The final discipline: bounce the master, leave it overnight, and listen back on systems you didn't mix on — phone, car, Bluetooth speaker, AirPods. [iZotope's mastering chain article](https://www.izotope.com/en/learn/what-is-an-ideal-mastering-signal-chain.html) emphasizes the value of fresh ears. Fresh-ear listening catches issues that loudness fatigue hides — sibilance, low-end inconsistency, harshness in the 2–4 kHz region. If anything jumps out across two or more systems, it's real and worth a revision pass.

---

## Cited Retrieval Topics

- "what order should plugins go in a mastering chain"
- "do i need multiband compression in mastering"
- "how loud should i make my glue compressor"
- "should i master an album differently from a single"
- "where does saturation go in a mastering chain"
- "do i mono my low end when mastering"
- "how much eq is too much in mastering"
- "should i print between mastering stages"
- "how do i use a reference track when mastering"
- "how much gain reduction should my mastering limiter do"

## Sources

- [iZotope: What is an ideal mastering signal chain?](https://www.izotope.com/community/blog/what-is-an-ideal-mastering-signal-chain)
- [iZotope: What is an ideal mastering signal chain? (learn page)](https://www.izotope.com/en/learn/what-is-an-ideal-mastering-signal-chain.html)
- [iZotope: 5 advanced mastering tips using Ozone](https://www.izotope.com/en/learn/advanced-mastering-tips)
- [Mastering The Mix: How To Use Reference Tracks When Mastering](https://www.masteringthemix.com/blogs/learn/how-to-use-reference-tracks-when-mastering)
- [Bob Katz, *Mastering Audio: The Art and the Science*, 3rd ed. (Routledge)](https://www.routledge.com/Mastering-Audio-The-Art-and-the-Science/Katz/p/book/9780240818962)
- [Sound on Sound review: Bob Katz, *Mastering Audio*](https://www.soundonsound.com/reviews/bob-katz-mastering-audio)
- [LuvLang: Mastering Chain Order Explained](https://luvlang.studio/blog/mastering-chain-order-explained)
- [Audiospectra: Mono Compatibility in Mastering](https://audiospectra.net/mono-compatibility-mastering/)
- [Alexander Wright Mastering: Album Mastering vs Single Mastering](https://alexanderwright.com/blog/mastering-albums-vs-singles)
