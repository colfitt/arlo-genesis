# Reverb and Delay Architecture

**Scope:** mixing
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Mike Senior, *Mixing Secrets for the Small Studio*; iZotope *Mixing Guide*; Bobby Owsinski, *Mixing Engineer's Handbook*
**Tags:** `mixing`, `reverb`, `delay`, `depth`, `principle`, `recipe`

---

## The five reverb families and what each is for

Reverbs split into three physical-space simulations (room, chamber, hall) and two mechanical/electromechanical types (plate, spring). Sound on Sound's [Choosing The Right Reverb](https://www.soundonsound.com/techniques/choosing-right-reverb) frames the practical split: plate reverbs are "still the first choice for most pop work" because they produce a dense tail very quickly with no audible early reflections, so they read as a musical effect rather than a literal space. Hall reverbs simulate large performance spaces and run long — often well over two seconds of decay — which is why [Sweetwater's reverb-type breakdown](https://www.sweetwater.com/insync/5-types-of-reverb-explained-hall-chamber-room-plate-and-spring/) flags them as best for strings and pads and warns they will muddy a dense pop mix. Chamber reverbs sit between room and hall — lush like a hall but more articulate, useful on vocals and acoustic instruments. Room reverbs are short and intimate; they add space without announcing themselves. Spring reverbs carry a metallic "twang" baked into surf, dub, and vintage guitar-amp tones and don't usually belong on vocals unless you want that exact character.

## A working three-bus send-and-return template

Most working mixers don't put reverb on individual channels — they run **shared aux sends to dedicated return buses** so a coherent space wraps the whole mix. [Sound on Sound's aux-send guide](https://www.soundonsound.com/techniques/using-aux-sends-returns) describes the standard topology: load the reverb on an aux/return channel, set its wet/dry to 100% wet, and feed it from each track via a send. A pragmatic starting template is three returns: **(1) a short room or ambience** (decay roughly 0.6–1.2 s) to glue drums and percussion; **(2) a medium-to-long plate** (decay 1.2–2.0 s) for vocals and lead instruments; **(3) a slap or mono delay** for rhythm and width tricks. Keeping the count low forces consistent space and prevents the "every track in its own room" smear. Pre-fader sends will keep reverb level constant when you ride the dry fader (useful for fades); post-fader (the default) keeps wet/dry ratio constant as the channel level moves.

## Pre-delay as separation: typical ranges

Pre-delay is the silent gap between the dry signal and the first reverb energy, and it is the single most useful knob for keeping a wet mix legible. [iZotope's pre-delay primer](https://www.izotope.com/en/learn/reverb-pre-delay) gives concrete by-source ranges: **vocals 20–80 ms**, **guitars 40–100 ms**, **drums 5–50 ms**. The Sound on Sound piece [Choosing The Right Reverb](https://www.soundonsound.com/techniques/choosing-right-reverb) offers a more specific recipe: "a plate reverb emulation with a decay time of 1.2 seconds or so and a pre-delay of 60–80 ms" is a typical pop-vocal treatment. The mechanism is psychoacoustic — the dry attack lands first and the brain locks onto it as the source, so even with a long, lush tail the lyric or transient stays intelligible. [Sound on Sound's reverb-quality article](https://www.soundonsound.com/techniques/improving-sound-your-reverb) warns that pre-delays under about 20 ms with audible first reflections can sound "phasey and unnatural," so if you want intimacy go to zero pre-delay, but don't park the knob in the comb-filter zone in between.

## Why short pre-delay reads as "close" and long reads as "big"

Longer pre-delay implies a larger room because in a real space the first reflection arrives later as the walls get further away. That same principle works in reverse for depth: tracks with **shorter** pre-delay and **wetter** sends sit further back, while tracks with **longer** pre-delay and dryer sends sit forward. [iZotope](https://www.izotope.com/en/learn/reverb-pre-delay) demonstrates this with a 29 ms pre-delay on a kick: the punch survives because the reverb arrives after the transient has already announced itself. Staggering pre-delays across instruments — short on background pads, longer on lead vocal — produces front-to-back depth without a buildup of overlapping early energy that would otherwise turn into midrange congestion.

## EQ the return: high-pass and low-pass tame the wash

Reverb returns almost always sound better with the extremes filtered off. Bottom end on a reverb bus muddies the kick and bass without contributing audibly to the sense of space, so a high-pass filter on the return is near-universal practice. [Sweetwater's reverb HPF tip](https://www.sweetwater.com/insync/effect-tip-use-a-high-pass-filter-before-reverb/) and [SoundGym's overview](https://www.soundgym.co/blog/item?id=high-pass-filter) both point to **roughly 100–300 Hz** as the working range, with the Abbey Road technique cited at a higher **500–600 Hz** for vocal-plate dryness. At the top end, real concert halls already roll off — Paul White's [Improving The Sound Of Your Reverb](https://www.soundonsound.com/techniques/improving-sound-your-reverb) notes "little is going on above 5 kHz" in real halls and gives reference low-pass targets including **plate around 5 kHz, concert hall 6 kHz, pop vocal 7 kHz, small room 10 kHz**. Pulling the highs darkens the tail and psychoacoustically pushes the reverb further back in the depth field.

## Decay-time picking: match it to the song, not the source

Decay time (RT60) decides how literally the reverb will participate in the arrangement. [Sound on Sound's reverb guide](https://www.soundonsound.com/techniques/choosing-right-reverb) frames the practical range as **under 1 second for tight intimate ballads up to around 2 seconds for big ballads**, with hall settings going longer if the arrangement is sparse enough to support them. Two practical rules: first, match decay to tempo so the tail dies before the next downbeat — at slow tempos you can afford 2–3 s, at 140 BPM up-tempo pop a 1.0–1.2 s plate stays out of the way. Second, dense arrangements need shorter decays; a sparse piano ballad will swallow a 3 s hall and ask for more, while a wall-of-guitars chorus needs the reverb to be felt more than heard.

## Delay throws as tempo-locked space

Delay is the "dry but big" alternative to reverb — it adds width and depth without filling every gap with diffuse energy. Tempo-synced delay values are the bread and butter. At 120 BPM, the quarter note is 60,000 ÷ 120 = **500 ms**, the eighth is **250 ms**, the dotted eighth is **375 ms**, and the sixteenth is **125 ms** — see any [BPM-to-delay calculator](https://sengpielaudio.com/calculator-bpmtempotime.htm) for the formula 60,000/BPM × note-fraction. The **dotted eighth** is the signature setting of [The Edge's U2 sound](https://www.amnesta.net/edge_delay/) — picking eighth notes against a 75%-of-a-beat repeat produces a cascading sixteenth-note feel from half the actual playing. **Quarter-note** delays feel anthemic and on-the-grid (vocal throws on the last word of a phrase). **Eighth-note** delays double up rhythmic density without altering feel.

## Slap delay: the short-throw vocal trick

A slapback is a single, near-instant repeat with zero feedback — a pillar of rockabilly and modern indie production. The working range is **roughly 75–150 ms**, with Sun Records-era Elvis recordings sitting around 90–150 ms depending on the source (see [Waves' slap-delay primer](https://www.waves.com/tips-for-mixing-with-slap-delay) and [Strymon's El Capistan article](https://www.strymon.net/this-weeks-favorite-el-capistan-slapback-echo/)). Set feedback to 0%–10% — past 10% it stops sounding like slap and starts sounding like a regular delay. The effect adds body to a thin vocal without the diffuse tail of reverb, and because it's a discrete repeat it sits in the mix without competing with the kick or snare for the ambient pocket. Tape-style emulations (filtered, slightly wow-and-flutter modulated) blend better than pristine digital slaps because the repeat is already darker than the dry.

## Reverb EQ in the chain: pre vs. post

Two places to filter: **before** the reverb (sculpts what enters the algorithm) and **after** the reverb (sculpts the tail). High-passing the send before the reverb keeps the algorithm from generating low-frequency mush in the first place — [Sweetwater's tip](https://www.sweetwater.com/insync/effect-tip-use-a-high-pass-filter-before-reverb/) recommends this specifically when reverbing bass-heavy sources. Filtering after the reverb shapes the tail's tonal character. Many algorithmic and convolution plug-ins have damping controls built in — these are an internal low-pass on the diffusing energy, not the output, and they color the tail more naturally than a fixed post-reverb EQ. For mix-bus glue use both: an HPF at 200 Hz on the send to keep low end clean, and a low-shelf cut of 2–3 dB above 8 kHz on the return to push the tail back.

## Using delay instead of reverb for "dry but big"

A modern pop trick is to skip reverb entirely on lead vocals and use a single short delay (one repeat, 80–150 ms, panned opposite the dry or in mono) plus a stereo widener. The dry signal stays present and consonants stay sharp, but the vocal still feels three-dimensional. The 2019 Billie Eilish/Finneas/Rob Kinelski production captured in [SOS Inside Track: Bad Guy](/Users/cfitt/Dev/arlo/corpus/mixing/sos-inside-track-billie-eilish-bad-guy.md) is a public example — the documented session uses a "Width" aux with Soundtoys MicroShift rather than a wet reverb send across the lead vocal groups, which is part of why the vocal sits so far forward despite being whispered. The technique scales: replace a long hall return with a 1/4-note tempo delay set to one repeat and 0% feedback, low-passed at 4–5 kHz, and the mix will feel "big" without the dense reverb wash.

## Routing tricks: pre-delay the send, sidechain the return

Two architectural moves worth knowing. **Manual pre-delay via a send-side delay** — insert a short delay plug-in *before* the reverb on the aux to get pre-delay values your reverb plug-in might not offer, or to modulate the pre-delay in tempo with the song. **Sidechain-duck the reverb return** off the lead vocal or kick, so the tail compresses out of the way during sung phrases and blooms in the gaps. [iZotope's pre-delay article](https://www.izotope.com/en/learn/reverb-pre-delay) discusses front-to-back depth as the goal of these techniques; ducking the return is the cleanest way to get a long, lush hall on a dense vocal without losing intelligibility — the tail effectively only exists between lines.

## Common architecture mistakes

The biggest one is **per-channel reverb plug-ins** instead of shared sends — every track ends up in its own slightly different room, and the mix smears without cohering. The second is **same pre-delay on everything** — without staggering, all the reverb energy arrives at once and the midrange (roughly 300 Hz – 2 kHz) builds up into a wash. The third is **untreated reverb returns** — letting the low end of the reverb through wastes bass headroom you needed for the kick and bass. The fourth is **decay time too long for the tempo** — at fast tempos a 3 s hall will still be ringing through the next bar's transients. The fix in each case is structural: consolidate to two or three shared returns, stagger their pre-delays by source, filter both ends of the return, and trim decay to die before the next downbeat.

## Cited Retrieval Topics

- "what pre-delay should i use on a vocal reverb"
- "how do i set up reverb sends in my mix"
- "what's the difference between plate and hall reverb"
- "delay time at 120 bpm dotted eighth"
- "how do i high pass a reverb return"
- "what is slapback delay and what ms value"
- "how do i get a dry but big vocal sound"
- "why does my reverb sound muddy"
- "the edge u2 delay setting"
- "decay time for vocal plate reverb"

## Sources

- [Sound on Sound — Choosing The Right Reverb](https://www.soundonsound.com/techniques/choosing-right-reverb)
- [Sound on Sound — Improving The Sound Of Your Reverb](https://www.soundonsound.com/techniques/improving-sound-your-reverb)
- [Sound on Sound — Using Aux Sends & Returns](https://www.soundonsound.com/techniques/using-aux-sends-returns)
- [iZotope — Reverb Pre-Delay Explained](https://www.izotope.com/en/learn/reverb-pre-delay)
- [Sweetwater — 5 Types of Reverb Explained](https://www.sweetwater.com/insync/5-types-of-reverb-explained-hall-chamber-room-plate-and-spring/)
- [Sweetwater — Use a High-Pass Filter Before Reverb](https://www.sweetwater.com/insync/effect-tip-use-a-high-pass-filter-before-reverb/)
- [SoundGym — The High-Pass Filter](https://www.soundgym.co/blog/item?id=high-pass-filter)
- [Sengpielaudio — BPM to Delay Time Calculator](https://sengpielaudio.com/calculator-bpmtempotime.htm)
- [Tim Darling — A Study of The Edge's Guitar Delay](https://www.amnesta.net/edge_delay/)
- [Waves — Tips for Mixing with Slap Delay](https://www.waves.com/tips-for-mixing-with-slap-delay)
- [Strymon — El Capistan Slapback Echo](https://www.strymon.net/this-weeks-favorite-el-capistan-slapback-echo/)
