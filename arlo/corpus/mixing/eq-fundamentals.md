# EQ Fundamentals

**Scope:** mixing
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Mike Senior, *Mixing Secrets for the Small Studio*; Roey Izhaki, *Mixing Audio*; iZotope *Mixing Guide*; Bobby Owsinski, *Mixing Engineer's Handbook*
**Tags:** `mixing`, `EQ`, `subtractive`, `low-end`, `principle`, `recipe`

---

## The four filter types and what each does

A parametric EQ exposes four core filter shapes, and choosing the right one for the problem is the first decision. The **bell (peak)** filter boosts or cuts a band around a center frequency, with Q controlling bandwidth — it is the most flexible shape and the workhorse for both surgical and tonal moves, according to [FabFilter's introduction to EQ](https://www.fabfilter.com/learn/equalization/introduction-to-eq). **Shelves** (high or low) tilt everything above or below a corner frequency by a fixed gain; they are the right choice for broad tonal shaping like adding "air" or warmth, as [Soundfly's Flypaper](https://flypaper.soundfly.com/produce/shelf-eq-vs-bell-eq-when-and-how-to-use-them-both/) notes that shelves "make broad overall changes" while bells handle resonances. The **low-cut (high-pass)** removes energy below a corner with a slope of 6, 12, 18, or 24 dB/octave; the **high-cut (low-pass)** does the opposite, taming brittle top end on tracks with no useful air. [Music Guy Mixing](https://www.musicguymixing.com/eq-filters/) recommends a low-pass around 100 Hz on tracks with no real low content to free space for the kick and bass that own that region.

## Subtractive vs. additive philosophy

The discipline most pros teach is "cut narrow, boost wide" — diagnose what is in the way first, then shape what remains. [LedgerNote](https://ledgernote.com/columns/mixing-mastering/subtractive-eq-vs-additive-eq/) describes subtractive EQ as a philosophy of restraint: well-recorded sources usually already contain what you want, so the job is to remove obstacles rather than pile on enhancements. The mechanical advantage is that subtractive moves reduce signal energy rather than adding it — less risk of clipping the next stage, no amplification of noise, less mud accumulating across a 40-track session. But subtractive-only dogma is a myth. [Sound on Sound](https://www.soundonsound.com/sound-advice/q-better-to-cut-eq) points out that "cut don't boost" was originally about analog circuit noise; with modern digital EQ, boosts are valid when you actually need more of something. The working rule: start subtractive to clear room, then add character with gentle boosts.

## Setting Q and gain by intent

Q (bandwidth) is the most-misused parameter. [Production Expert](https://www.production-expert.com/production-expert-1/5-mistakes-people-make-when-mixing-with-eq) and [iZotope](https://www.izotope.com/en/learn/16-common-eq-mistakes-mixing-engineers-make) both flag a recurring pattern: engineers boost with a narrow Q, which sounds "over-focused" and unnatural. The convention is *narrow Q for cuts, wide Q for boosts*. A surgical cut of a resonant ring at high Q is invisible; a high-Q boost of the same band sounds pinched and synthetic. Magnitude matters too — [Magnetic Magazine](https://magneticmag.com/2025/01/eq-mistakes/) warns that boosts over 3–5 dB usually indicate a recording problem better solved with a different mic, source EQ, or take, not with more EQ. If you find yourself adding 8 dB at any band, stop and reconsider whether the track is wrong.

## Mud zone: 200–500 Hz

The 200–500 Hz region is the single most common source of a cloudy, congested mix. Body and warmth of nearly every instrument lives here — kick shells, snare body, vocal chest, guitar warmth, piano tone — and when they all stack, the mix sounds blanketed. The [iZotope EQ cheat sheet](https://www.izotope.com/community/blog/eq-cheat-sheet) and [HomeStudioRecordings](https://homestudiorecordings.com/eq-frequency-cheat-sheet/) both identify this as the "mud" or "boxiness" band. The technique: sweep a narrow bell with 4–6 dB of boost through 200–400 Hz on each track, find the offender, then cut a couple of dB with moderate Q. Doing this on three or four offenders (typically background vocals, room mics, electric guitars, and electric piano) usually cleans up a mix more than any single fader move.

## Harshness zone: 2–5 kHz

The 2–5 kHz range is where presence lives, but it is also where listening fatigue starts. [iZotope](https://www.izotope.com/community/blog/eq-cheat-sheet) and the [Orphiq vocal cheat sheet](https://orphiq.com/resources/vocal-eq-cheat-sheet) flag this as the band where harshness hides — most often around 2.5–3.5 kHz on distorted guitars, snare cracks, and bright vocals. Excessive boost here is the single most common cause of mixes that sound great in the studio and brittle on consumer speakers. If you need presence, a wide-Q boost of 1–3 dB is usually plenty; for fatigue problems, sweep with a narrow cut to find a specific resonance rather than chopping the whole band. Pair the move with a complementary check around 8–10 kHz: sometimes what reads as harshness at 3 kHz is actually unmasked once you tame nasal energy around 1–1.5 kHz.

## Kick drum starting points

Kick anatomy is roughly: sub fundamental, beater click, and a messy middle that usually wants to go away. The [Native Instruments blog on kick EQ](https://blog.native-instruments.com/kick-drum-eq/) describes the punch region as 60–100 Hz and the beater click around 4–6 kHz. [TonyOso](https://tonyosomusic.com/blogs/fighting-through-the-pain/posts/7603237/how-to-eq-kick-drum-my-step-by-step-process) and [Audiospectra](https://audiospectra.net/kick-drum-eq/) both call 250–600 Hz the kick's "boxy" zone — a place to cut, not boost. A typical move chain on a rock kick: high-pass around 30–40 Hz to kill subsonics, a few dB cut around 300–400 Hz to lose cardboard, a small wide boost at 60–80 Hz for thump, and a narrower boost around 4 kHz for beater click. On a programmed pop kick that already has its character baked in, you often need *less* — sometimes just a high-pass and a small click boost.

## Snare starting points

Snare body lives around 150–250 Hz and crack lives around 4–6 kHz, with boxiness around 400 Hz that usually wants attenuation. [Music Guy Mixing](https://www.musicguymixing.com/snare-eq/) recommends a high-pass around 70 Hz to remove kick bleed while keeping the snare's body, a cut around 400 Hz to remove boxiness, and a boost around 5 kHz for stick crack. [Sonicbids](https://blog.sonicbids.com/the-engineers-guide-to-the-perfect-snare-sound) suggests 3–5 kHz adjustments for crispness while warning that aggressive boosts here quickly become brittle. Mid-range buzz and ring (around 800 Hz to 1.2 kHz) is also a common offender — sweep with a narrow cut to find it. If the snare needs more weight, a small 200 Hz boost adds body; if it needs more crack, push around 5 kHz but keep an eye on cymbal bleed riding the same band.

## Vocal starting points

Vocals share the mud and harshness zones with everything else, plus an air shelf above 10 kHz that defines modern pop sheen. The [iZotope vocal EQ guide](https://www.izotope.com/en/learn/how-to-eq-vocals.html) and [BChillMix](https://bchillmix.com/pages/vocal-eq-cheatsheet) both teach the same four moves: high-pass around 80–100 Hz to kill rumble, gentle cut around 200–400 Hz to clear mud, a 3–5 kHz nudge for presence, and a high shelf above 10 kHz for air. The presence move is where most beginners overdo it — 1–3 dB of wide-Q boost goes a long way, and pushing harder usually moves the vocal from "forward" to "abrasive." Watch for sibilance riding in the 5–8 kHz range; if it screams, that is a de-esser job, not an EQ job. The air shelf is the cheapest "expensive-sounding" move in mixing.

## Bass guitar starting points

Bass anatomy splits into fundamentals around 80–200 Hz, growl around 400–800 Hz, and pick or finger attack around 1–2.5 kHz. [Behind the Mixer](https://www.behindthemixer.com/art-bass-eq-using-eight-key-frequency-ranges/) and [StockMusicMusician](https://www.stockmusicmusician.com/blog/how-to-eq-bass-guitar) both note that bass that disappears on phones and laptops needs more 800 Hz–1 kHz, not more 80 Hz — small speakers can't reproduce the fundamental, so the ear locks onto the harmonics. The classic kick-and-bass carve: if the kick owns 60 Hz with a small boost, cut the bass a couple of dB at 60 Hz and let it own 80–100 Hz instead. A high-pass around 30–40 Hz keeps inaudible subsonics from eating mastering headroom, and a small boost around 700–1000 Hz pulls the bass forward in dense mixes.

## Electric guitar starting points

Electric guitar lives in the midrange, and the most useful EQ moves are aggressive low-cuts. [StockMusicMusician's electric guitar tips](https://www.stockmusicmusician.com/blog/electric-guitar-eq-tips) and [Neural DSP's electric guitar EQ guide](https://neuraldsp.com/articles/electric-guitar-eq-guide) both recommend cutting below 100 Hz on rhythm guitars — there is almost nothing useful there, only mud that fights the bass. Presence boosts of 1–3 dB around 3 kHz help guitars cut through dense arrangements without the harshness that lives just above at 4–5 kHz. For a layered guitar arrangement with a left/right doubled rhythm part plus a center lead, complementary EQ helps: scoop the rhythms slightly at 1 kHz so the lead has room to speak there, and boost the lead 1–2 dB at the same band.

## Mid/side EQ basics

Mid/side EQ splits a stereo signal into its mono (mid) and stereo-difference (side) components and lets you EQ each independently. The [iZotope explainer on mid/side processing](https://www.izotope.com/en/learn/what-is-midside-processing) and [Mastering The Mix's guide](https://www.masteringthemix.com/blogs/learn/how-to-use-mid-side-eq-to-elevate-your-masters) cover the two most useful moves: high-passing the sides between 80 Hz and 250 Hz to tighten the low end (the kick and bass become more focused because their stereo bleed is removed), and gently shelving up the side channel above 8 kHz to widen perceived stereo image without affecting the mono center. Use sparingly — half a dB to a couple of dB at most. [Streaky.com](https://www.streaky.com/blogs/blog/mid-side-eq-in-mastering-how-to-use-it-without-wrecking-someones-mix) warns that heavy mid/side processing often falls apart on mono playback (phone speakers, Bluetooth puck speakers, club sub mono).

## Inconsistent high-pass across tracks

One of the cheapest mix improvements is auditing every track's high-pass setting. A common pattern: the kick is high-passed at 40 Hz, the bass at 30 Hz, but the acoustic guitar, electric guitar, organ, and background vocals are all running flat down to DC. Their inaudible low energy stacks up, eats limiter headroom, and muddies the bus. [Production Expert](https://www.production-expert.com/production-expert-1/5-mistakes-people-make-when-mixing-with-eq) flags this as one of the top recurring mistakes. The fix: a quick audit pass where every non-low-end track gets a high-pass at a frequency that is *just below* its lowest useful note. For most pop instruments that lands between 80 Hz and 200 Hz; for vocals, 80–120 Hz is typical; for hi-hat overheads, 200–400 Hz is fine.

## The "boost-cut-boost" trap

Beginners often EQ in passes, listening to the soloed track each time, and end up with EQ curves that look like saw blades — boost, cut, boost, cut, boost. The [Audio Issues warning signs piece](https://www.audio-issues.com/music-mixing/warning-signs-eq/) describes a related failure: hearing a resonance, cutting it, then hearing another, cutting that, until the sound is hollow. Two habits prevent this. First, EQ in the mix, not in solo — soloing exposes problems that are masked by other tracks and would have stayed inaudible. Second, use bypass aggressively: A/B every move against the bypassed version, level-matched, and ask whether the EQ actually improved the mix or just changed it. If the bypassed version sounds more natural, undo the move. The goal is not to add EQ; the goal is to fix the specific problem in front of you.

## When EQ isn't the answer

EQ is a frequency rebalancer, not a fixer. If a vocal sounds dull, EQ might help, but if the problem is poor mic technique or a dark room, no high-shelf will replace what wasn't captured. [Sound on Sound's "EQ: A New Perspective"](https://www.soundonsound.com/techniques/eq-new-perspective) frames EQ as psychoacoustic manipulation rather than tone control, and the implication is practical: EQ shifts the listener's attention, but cannot synthesize information the recording does not contain. If you are reaching for more than 4–5 dB to fix a track, the answer is probably a different processor (saturation for thickness, transient designer for attack, multiband for resonance) or a different take. The cheap moves — high-pass, mud cut, presence nudge, air shelf — handle 80% of mix EQ work. Save the surgical stuff for the remaining 20%.

## Cited Retrieval Topics

- "what frequency is mud in a mix"
- "how do i eq a kick drum to sound punchy"
- "why does my mix sound muddy in the low mids"
- "subtractive eq vs additive eq when to use each"
- "what's the difference between a shelf and a bell filter"
- "how do i use mid side eq"
- "how much should i boost on an eq"
- "where is harshness in vocals"
- "what should i high pass at on my tracks"
- "how do i make electric guitars cut through a mix"

## Sources

- [FabFilter — Introduction to EQ](https://www.fabfilter.com/learn/equalization/introduction-to-eq)
- [Soundfly Flypaper — Shelf EQ vs. Bell EQ](https://flypaper.soundfly.com/produce/shelf-eq-vs-bell-eq-when-and-how-to-use-them-both/)
- [Music Guy Mixing — The 6 EQ Filters](https://www.musicguymixing.com/eq-filters/)
- [LedgerNote — Subtractive EQ vs Additive EQ](https://ledgernote.com/columns/mixing-mastering/subtractive-eq-vs-additive-eq/)
- [Sound on Sound — Q. With EQ, is it better to cut than to boost?](https://www.soundonsound.com/sound-advice/q-better-to-cut-eq)
- [Sound on Sound — EQ: A New Perspective](https://www.soundonsound.com/techniques/eq-new-perspective)
- [Production Expert — 6 Mistakes People Make When Mixing With EQ](https://www.production-expert.com/production-expert-1/5-mistakes-people-make-when-mixing-with-eq)
- [iZotope — 16 Common EQ Mistakes](https://www.izotope.com/en/learn/16-common-eq-mistakes-mixing-engineers-make)
- [Magnetic Magazine — 9 EQ Mistakes New Producers Make](https://magneticmag.com/2025/01/eq-mistakes/)
- [iZotope — EQ Cheat Sheet](https://www.izotope.com/community/blog/eq-cheat-sheet)
- [HomeStudioRecordings — Ultimate EQ Frequency Cheat Sheet](https://homestudiorecordings.com/eq-frequency-cheat-sheet/)
- [Orphiq — Vocal EQ Cheat Sheet](https://orphiq.com/resources/vocal-eq-cheat-sheet)
- [iZotope — How to EQ Vocals](https://www.izotope.com/en/learn/how-to-eq-vocals.html)
- [BChillMix — Vocal EQ Cheatsheet](https://bchillmix.com/pages/vocal-eq-cheatsheet)
- [Native Instruments — Kick Drum EQ Essentials](https://blog.native-instruments.com/kick-drum-eq/)
- [TonyOso Music — Kick EQ Step-by-Step](https://tonyosomusic.com/blogs/fighting-through-the-pain/posts/7603237/how-to-eq-kick-drum-my-step-by-step-process)
- [Audiospectra — Punchy Kick Drum EQ Settings](https://audiospectra.net/kick-drum-eq/)
- [Music Guy Mixing — Complete Snare EQ Guide](https://www.musicguymixing.com/snare-eq/)
- [Sonicbids — Engineer's Guide to the Perfect Snare Sound](https://blog.sonicbids.com/the-engineers-guide-to-the-perfect-snare-sound)
- [Behind the Mixer — The Art of Bass EQ](https://www.behindthemixer.com/art-bass-eq-using-eight-key-frequency-ranges/)
- [StockMusicMusician — How to EQ Bass Guitar](https://www.stockmusicmusician.com/blog/how-to-eq-bass-guitar)
- [StockMusicMusician — 8 Essential Electric Guitar EQ Tips](https://www.stockmusicmusician.com/blog/electric-guitar-eq-tips)
- [Neural DSP — Electric Guitar EQ Guide](https://neuraldsp.com/articles/electric-guitar-eq-guide)
- [iZotope — What is Mid/Side Processing](https://www.izotope.com/en/learn/what-is-midside-processing)
- [Mastering The Mix — How to Use Mid/Side EQ](https://www.masteringthemix.com/blogs/learn/how-to-use-mid-side-eq-to-elevate-your-masters)
- [Streaky — Mid Side EQ in Mastering](https://www.streaky.com/blogs/blog/mid-side-eq-in-mastering-how-to-use-it-without-wrecking-someones-mix)
- [Audio Issues — 6 Warning Signs of EQ Problems](https://www.audio-issues.com/music-mixing/warning-signs-eq/)
