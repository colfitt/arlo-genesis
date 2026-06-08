# Low-End Management

**Scope:** mixing
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Mike Senior, *Mixing Secrets for the Small Studio* (low-end chapter); SOS Inside Track articles; Bobby Owsinski, *Mixing Engineer's Handbook*
**Tags:** `mixing`, `low-end`, `kick`, `bass`, `sidechain`, `mono`, `principle`

---

## Why low end is the hardest mix problem

Low end is the part of the mix that consumer playback systems disagree about most, and small-studio rooms reproduce least reliably. Mike Senior's *Mixing Secrets for the Small Studio* dedicates entire chapters to it ("Low-End Damage Limitation," "The Power of Side Chains") precisely because it's the single biggest translation failure for home mixers. As discussed in [Sound on Sound's coverage of Senior's approach](https://www.soundonsound.com/sound-advice/q-should-i-mix-high-end-headphones-or-low-end-monitors), even expensive monitors can't fix a room that sounds bad below 200 Hz — modal resonances pile up at specific frequencies and dips appear at others, so you trust what you hear at 80 Hz at your peril. The corollary is procedural: low-end decisions need verification on a second system before they're done, and every move you make in the bottom octaves should be conservative, structural, and supported by a meter or spectrum analyzer rather than ears alone.

## Kick-and-bass frequency carving

The classic carve assigns the **sub-fundamental to one source and the punch/body to the other**. A widely-cited starting point per [Mixing Monster's kick-and-bass guide](https://mixingmonster.com/mixing-kick-and-bass/) is **kick fundamental 40–60 Hz, bass 80–200 Hz for warmth**, with their attack registers separated: kick "click" boosted at **2–5 kHz** while the same band is dipped on the bass (or vice versa for bass-pick-attack songs). The carve is reciprocal: wherever you boost one, cut the other. The other variant flips the assignment — bass owns the sub (40–60 Hz), kick owns the punch (80–120 Hz) — which is common in rock and indie where the kick is more of a beater-attack than a sub bomb. Either model is defensible; the rule is *pick one and commit*, because both sources fighting for the same band is what produces unfocused, undefined low end on consumer systems.

## Sidechain compression: dance vs. subtle settings

Sidechain ducking the bass off the kick is the most reliable way to give the kick a window of dynamic space. The dance/EDM "pump" version uses an aggressive setting — [EDMProd's sidechain guide](https://www.edmprod.com/sidechain-compression/) and [Sonarworks](https://www.sonarworks.com/blog/learn/sidechain-compression) converge on **fast attack (around 1–2 ms or all the way to 0), ratio 4:1 to 8:1 or higher, release tuned to the song (often quarter-note length)**, with the release setting the audible "pump" because it's how fast the bass returns after each kick hit. The subtle mix version dials all of that back: **ratio 2:1, fast attack still, release 20–75 ms** so the duck is felt but not heard. Mike Senior is on record (per [Gearspace discussion of *Mixing Secrets*](https://gearspace.com/board/so-much-gear-so-little-time/592077-mixing-secrets-mike-senior-3.html)) recommending **multiband sidechain** — only ducking the bass's low octaves so the upper-midrange of the bass keeps its presence and pick attack while the sub gets out of the way. Gain reduction of **3–6 dB** is the standard target.

## Mono the low end below roughly 120 Hz

Stereo content below ~120 Hz creates problems for vinyl cutting, club PA systems, and any single-sub playback (2.1, 5.1, single-subwoofer Atmos). [Flotown Mastering's monoization guide](https://flotownmastering.com/blog/center-that-sub) explains the practical reasons and notes that "the frequencies between 50 Hz and 120 Hz make up the bulk of the low end, and those frequencies need to be at the center." The simplest move is an **M/S EQ with a high-pass on the Side channel** at roughly 100–150 Hz — the Side signal carries only the L–R difference, so cutting its low end forces the bottom octaves to mono without affecting the L+R center. Plug-ins built for this include Tone Projects Basslane Pro, Nugen Monofilter, the iZotope Ozone Imager, and HoRNet's [ElliptiQ elliptical EQ](https://www.hornetplugins.com/plugins/hornet-elliptiq/) — the historical term "elliptical EQ" comes from vinyl cutting, where uncontrolled stereo bass made the cutter trace an elliptical path that could jump the groove.

## The 30 Hz HPF question: when to filter sub-bass

A near-universal mix bus and per-track cleanup move is a high-pass somewhere below the lowest musical content to strip subsonic rumble from air handling, mic-stand vibration, and traffic. The conventional range is **20–30 Hz on the mix bus** with a gentle slope (6 or 12 dB/oct) — [iZotope's 6-ways-to-use-an-HPF article](https://www.izotope.com/en/learn/6-ways-to-use-a-high-pass-filter-when-mixing.html) covers this as a cleanup pass. Push it higher than 30 Hz on the mix bus only if the lowest musical content is above that line; sub-bass-heavy genres (trap, dubstep, modern pop bass drops) often have meaningful fundamentals at 40–50 Hz and you'll feel the difference if you cut too aggressively. The right approach on individual tracks is more permissive — vocals, guitars, keys, and overheads can all live with a 60–100 Hz HPF — but the kick and bass should usually be filtered only at 25–40 Hz to preserve their fundamentals.

## Kick phase coherence between mics

Two-mic kick captures (typically an inside-the-shell beater mic and an outside-the-resonant-head body mic) almost never arrive at the DAW phase-aligned. Distance between the two capsules causes the outside mic to land milliseconds later, and depending on capsule orientation the polarity can be inverted. [JZ Microphones' phase guide](https://usashop.jzmic.com/blogs/blog/drum-tracking-avoiding-phase-issues) and [Sonnox's drum phase alignment article](https://sonnox.com/articles/drum-phase-alignment-when-to-nudge-flip-or-leave-alone) describe the standard workflow: **solo both kick mics in mono, then flip the polarity switch on one** — the version with more low-end body and weight is correct. If polarity-flipping isn't enough, nudge the later mic earlier (typically the outside mic) by sample-level adjustment until the transients align — this is the "transient alignment" technique. Without these steps a two-mic kick will sound thin and "whispy," the bottom octave will partially cancel, and no amount of EQ will recover it.

## Monitoring problems in the small studio

Senior's central thesis is that the room is the limiting factor in untreated home studios. Per the [Sound on Sound monitor-vs-headphones piece](https://www.soundonsound.com/sound-advice/q-should-i-mix-high-end-headphones-or-low-end-monitors), Senior argues that mixing on quality headphones in a bad-sounding room often beats mixing on speakers in the same room — the room can't add 6–12 dB peaks and nulls to a headphone signal. The practical workflow is **mix on monitors for stereo image and midrange balance, but verify low end on headphones AND a spectrum analyzer AND a consumer system**. Engineers including Joe Chiccarelli (cited in [Patreon discussion of Senior's references](https://www.patreon.com/posts/reference-of-1-33041129)) keep a spectrum analyzer on the master bus specifically to watch the bottom-end octave balance — looking for too much 30 Hz vs. too little 50 or 80 Hz — because the room won't tell them.

## Subs in headphones vs. monitors vs. consumer playback

Each playback context lies about the low end differently. **Headphones** under-represent the felt component — you'll hear sub content but won't feel it the way a club system or even a 5" monitor with a sub will, which makes it easy to leave too much sub in the mix. **Untreated rooms with ported monitors** routinely add room-mode boosts at 60–100 Hz that simply aren't in the file, so you'll over-cut at those frequencies. **Phone speakers** roll off entirely below ~300 Hz, so the bass on a phone is mostly heard via the second harmonic — which means a bass with strong 80 Hz fundamental but no upper-harmonic content will disappear on phones. The fix is harmonic enhancement: distortion, saturation, or a parallel-distorted bass track that adds 160 Hz / 240 Hz / 320 Hz energy so the line stays audible on small speakers. The cross-system check is non-negotiable — Senior's recommendation is to listen on at least a phone, headphones, and a car before declaring a low-end balance done.

## Bass saturation as the small-speaker insurance policy

Because phone speakers and laptop speakers can't reproduce sub fundamentals, mixers add harmonic content above the fundamental so the brain reconstructs the missing low octave from the harmonic series. This is the "missing fundamental" psychoacoustic effect: a bass note with strong harmonics at 160/240/320 Hz reads as the 80 Hz fundamental even when 80 Hz is absent. Practical recipes include a **parallel saturated bass** (a copy of the bass through tube/tape/transistor distortion, summed back in at low level) and **plug-in saturators** (FabFilter Saturn 2, Soundtoys Decapitator, iZotope Trash) on the bass directly. Senior's *Mixing Secrets* and the SOS Inside Track series both describe this as standard pop practice — the goal is a bass that translates from a club PA down to AirPods without going missing on either.

## Reference-track checks for low end

Loudness-matched reference tracks are the most reliable low-end check available. Pull two or three commercial tracks in the same genre, level-match by integrated LUFS (more on this in the translation file), and A/B their low-end balance against yours on the same system. The reference will tell you if your kick is too loud, your bass too quiet, or your sub-bass eating headroom. iZotope's **Tonal Balance Control** plug-in formalizes this — it overlays your mix's spectral curve against a genre-specific target derived from reference tracks. Senior's translation thesis (covered in detail in the mix-translation file) treats this kind of comparison as the primary anti-self-delusion tool: the small-studio mixer's ears are unreliable in the bottom octaves, so external evidence has to drive the decisions.

## Multiband and dynamic EQ for low-end control

When static EQ can't fix a bass that bloats during sustained notes or a kick that masks the bass only on certain hits, dynamic EQ and multiband compression are the cleaner solutions. A **dynamic EQ** on the bass (FabFilter Pro-Q's dynamic mode, iZotope Neutron, Pro-MB) can be tuned to attenuate 80 Hz only when 80 Hz exceeds a threshold — so legato notes don't pile up, but staccato notes keep their punch. **Multiband sidechain** (the Mike Senior recommendation per the gearspace summary) splits the bass into low and high bands and only ducks the low band off the kick, so the upper midrange — where the bass-pick attack and harmonic body live — stays present through the sidechain pump. Both approaches let you carve more aggressively in the time domain without static-EQ side effects like a thin-sounding bass between kick hits.

## Common low-end mistakes and quick fixes

The recurring problems in home-studio mixes: **too much sub-bass below 40 Hz** (HPF the kick at 30 Hz, HPF non-bass tracks at 60–100 Hz); **kick and bass both occupying 80 Hz** (carve — boost one, cut the other); **stereo bass below 120 Hz** (M/S EQ with HPF on the Side channel); **bass invisible on phones** (add harmonic saturation 160–400 Hz); **two-mic kick that's thin** (polarity-flip one mic, align transients); **mix that's bass-heavy on monitors and thin on headphones** (the room is lying — trust the meter and the reference track over the room); **bass that pumps too obviously** (multiband sidechain or lower the ratio); **subsonic rumble eating limiter headroom on master** (mix-bus HPF at 20–30 Hz, 12 dB/oct). Each of these has a structural fix — none of them is solved by twisting the bass EQ harder.

## Cited Retrieval Topics

- "how do i make my kick and bass not fight"
- "sidechain compression settings for kick and bass"
- "should i mono my bass below 100 hz"
- "mike senior low end mixing"
- "30 hz high pass filter mix bus"
- "why does my bass disappear on phones"
- "kick drum phase flip inside outside mic"
- "elliptical eq low end mono"
- "multiband sidechain bass"
- "how to check low end in untreated room"

## Sources

- [Sound on Sound — Q: Should I mix on high-end headphones or low-end monitors?](https://www.soundonsound.com/sound-advice/q-should-i-mix-high-end-headphones-or-low-end-monitors)
- [Sound on Sound — Mike Senior author page](https://www.soundonsound.com/author/mike-senior)
- [Mike Senior — Reference Of The Week #1 (Patreon)](https://www.patreon.com/posts/reference-of-1-33041129)
- [Gearspace — Mixing Secrets by Mike Senior discussion thread](https://gearspace.com/board/so-much-gear-so-little-time/592077-mixing-secrets-mike-senior-3.html)
- [Mixing Monster — Pro Secrets For Mixing Kick And Bass](https://mixingmonster.com/mixing-kick-and-bass/)
- [Flotown Mastering — Center That Sub! A Guide to Monoing Your Low End](https://flotownmastering.com/blog/center-that-sub)
- [HoRNet — ElliptiQ elliptical equalizer](https://www.hornetplugins.com/plugins/hornet-elliptiq/)
- [EDMProd — Sidechain Compression: 5 Simple Tips](https://www.edmprod.com/sidechain-compression/)
- [Sonarworks — Maximize Your Mix's Clarity and Groove with Sidechain Compression](https://www.sonarworks.com/blog/learn/sidechain-compression)
- [iZotope — 6 ways to use a high-pass filter when mixing](https://www.izotope.com/en/learn/6-ways-to-use-a-high-pass-filter-when-mixing.html)
- [JZ Microphones — Drum Tracking: Avoiding Phase Issues](https://usashop.jzmic.com/blogs/blog/drum-tracking-avoiding-phase-issues)
- [Sonnox — Drum Phase Alignment: When to Nudge, When to Flip, and When to Leave It Alone](https://sonnox.com/articles/drum-phase-alignment-when-to-nudge-flip-or-leave-alone)
