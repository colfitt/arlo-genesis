# Tracking Vocals in the Small Studio

**Scope:** recording
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Mike Senior, *Recording Secrets for the Small Studio*; Bobby Owsinski, *Recording Engineer's Handbook*; Howard Massey, *Behind the Glass*
**Tags:** `recording`, `tracking`, `vocal`, `mic-placement`, `comping`, `recipe`

---

## Matching the mic to the voice

There is no universal "best vocal mic" — each of the three transducer families has a specific personality that suits some voices and fights others. **Large-diaphragm condensers (LDCs)** capture the widest frequency range and the fastest transient response, flattering breathy or detailed singers and reproducing air above 10 kHz that dynamics miss ([Sweetwater](https://www.sweetwater.com/insync/dynamic-vs-condenser-vs-ribbon-microphones-how-are-they-different/), [B&H](https://www.bhphotovideo.com/explora/pro-audio/tips-and-solutions/overview-of-microphones-from-large-diaphragm-condensers-to-ribbons)). **Dynamic mics** (Shure SM7B, SM58, EV RE20) trade detail for durability, lower self-noise immunity in poor rooms, and the ability to handle loud, aggressive sources without distortion — they're the default for rock and metal vocals and the standard for podcasters working in untreated bedrooms ([Soyuz Microphones](https://soyuzmicrophones.com/articles/difference-between-microphones)). **Ribbon mics** have a softer, slightly rolled-off top end and a "vintage" midrange forwardness that suits crooning, jazz, and folk vocals, but they are fragile and require a high-gain preamp because of their low output ([Perfect Circuit](https://www.perfectcircuit.com/signal/microphone-types-explained)). A useful first test: track the same chorus on whatever mics you have and pick the one that sounds least like work to mix.

## When a dynamic mic beats a condenser

The conventional wisdom that condensers are "better" for vocals collapses in untreated rooms. A condenser captures everything — the singer, the room, the fridge, the neighbor's TV — while a dynamic mic's lower sensitivity and tighter cardioid pattern reject more of the environment ([Pro Audio Files](https://theproaudiofiles.com/shure-sm7b/), [SoundGuys](https://www.soundguys.com/shure-sm7b-review-28438/)). The Shure SM7B has become the standard bedroom-vocalist mic precisely because it rejects room sound aggressively and tolerates poor acoustics. The trade is gain: the SM7B is famously gain-hungry, typically requiring +60 dB or more of clean preamp gain, which many entry-level interfaces cannot supply without raising the noise floor ([Shure](https://www.shure.com/en-US/products/microphones/sm7b), [Sound on Sound](https://www.soundonsound.com/reviews/cloud-microphones-cloudlifters)). A Cloudlifter or Fethead inline booster adds ~25 dB of clean phantom-powered gain, letting the preamp work in its quiet range. Rule of thumb: if your room is bad and your budget is small, a dynamic mic with a Cloudlifter beats a $1,000 condenser in a closet.

## Polar pattern and room rejection

For vocals in a small room, the cardioid pattern is the default for a reason: maximum pickup at 0°, ~6 dB attenuation at the sides (90°), and near-complete rejection at the rear (180°) ([Sonarworks](https://www.sonarworks.com/blog/learn/microphone-polar-patterns-guide), [LEWITT](https://www.lewitt-audio.com/blog/polar-patterns)). Hyper- and supercardioid patterns reject the sides even more aggressively but pick up a lobe of sound at the rear, which means the wall behind the singer becomes the critical reflection surface. **Figure-8 (bidirectional)** rejects everything at the sides but accepts sound equally from front and rear — useful when there's a treated rear surface and the side walls are problematic, less useful when the singer's back faces a hard plaster wall ([Sound on Sound](https://www.soundonsound.com/techniques/using-microphone-polar-patterns-effectively)). **Omnidirectional** captures everything, which sounds great in a treated room and terrible in a bedroom. Practical default for untreated rooms: cardioid pointed at the singer with absorbers placed *behind the microphone* (behind the singer's reflection path) rather than behind the singer, because cardioid rejects what's directly behind the mic, not what's in front of it bouncing back from behind the singer.

## Distance, proximity effect, and the pop filter

The standard pop vocal distance is **6–8 inches mouth-to-mic** for an intimate detailed sound, or **10–14 inches** for a more open, less proximity-affected tone ([Hollyland](https://www.hollyland.com/blog/tips/how-much-distance-is-good-for-recording-vocals), [Roswell Pro Audio](https://roswellproaudio.com/pages/microphone-position-for-vocal-recording)). All directional (cardioid, figure-8, hyper) mics boost low frequencies as the source gets closer — the **proximity effect** — which can add 6–10 dB of bass below 200 Hz at typical close-mic distances. Use this deliberately: lean in for warmth on a soft verse, lean out for a brighter sound on a screaming chorus. **Pop filter placement**: the mesh should sit 2–4 inches in front of the mic capsule, with the singer's mouth another 2–6 inches in front of the mesh, giving a total mouth-to-capsule distance of 4–10 inches ([Pure Audio Insight](https://pureaudioinsight.com/blogs/microphone-accessories/professional-tips-for-optimizing-your-pop-filter-usage), [RØDE](https://help.rode.com/hc/en-us/articles/9423808397199-How-to-Properly-Position-a-R%C3%98DE-Microphone-and-Pop-Filter)). The pop filter does one job — diffusing the blast of air from plosives (P, B, T) before it slaps the capsule — and is non-negotiable on any directional condenser.

## Mic angle for sibilance and consistency

A mic pointed dead-on at the mouth captures the most direct signal but also the most plosive air and the harshest sibilance. Two practical adjustments soften the worst of it without losing presence. **Tilt the mic 10–15° off-axis from the mouth**, pointing slightly above or below the lip line so the capsule sees the mouth at an angle rather than straight on ([Sound on Sound](https://www.soundonsound.com/techniques/techniques-vocal-de-essing), [Produce Like A Pro](https://producelikeapro.com/blog/pro-de-esser-tips-better-sounding-vocals/)). Pointing slightly above the mouth (singer looks up at the mic) softens lower-frequency proximity and aims sibilance past the capsule; pointing slightly below (singer sings over the top of the mic) reduces top-end harshness while keeping body. The other classic technique: place a pencil vertically taped across the front of the pop filter to break up sibilance arriving at the capsule. Setting the angle once and marking the stand position keeps takes consistent across multiple sessions — distance and angle drift are common reasons "yesterday's takes don't match today's."

## Gain staging the vocal chain

Aim for vocal peaks hitting **−12 to −6 dBFS** on the loudest moments of the performance, with average levels sitting around **−18 dBFS RMS** ([Ledger Note](https://ledgernote.com/columns/studio-recording/gain-staging/)). This is the safe target for 24-bit recording: low enough to leave headroom for unexpected peaks, high enough to use plenty of bits and stay well above the noise floor of any plugin downstream. Set gain by recording the loudest section the singer is likely to deliver (usually the bridge or final chorus), not the verse — singers get louder as they warm up. A Cloudlifter or Fethead on a dynamic mic lets the preamp work at a quieter, cleaner setting; without it, an entry-level interface running the gain knob past 3 o'clock often introduces audible hiss into the recording ([Producer Hive](https://producerhive.com/buyer-guides/studio-gear/what-does-a-cloudlifter-do/)). Print without a compressor unless you commit deliberately; a hardware comp on the way in is fine for character, but ratchet attack and ratio gently because you cannot undo an over-compressed take.

## Treating an untreated room for vocals

In an untreated bedroom, the goal is not to make the room *sound treated* — it's to keep the room out of the microphone. Position the singer **away from corners and parallel walls**, ideally in the middle of the longest dimension of the room facing inward, so reflections are weaker and arrive later. Hang a **king-size high-tog duvet behind the microphone** (i.e., behind the cardioid pattern's null zone if you've turned the singer to face into the room) — Sound on Sound's Hugh Robjohns notes a heavy duvet often outperforms thin acoustic foam tiles, especially with a 1–2 inch air gap between duvet and wall to extend low-frequency absorption ([Sound on Sound](https://www.soundonsound.com/sound-advice/q-how-do-set-acoustic-treatment-recording-vocals)). For the front and sides, wrap the mic position in two more blankets, mattresses, or absorbers in a U or arc shape. Avoid the bare-closet trick unless the closet is full of clothes — an empty closet is six hard parallel surfaces and sounds boxy.

## The mattress fortress and reflection filters

When even mattresses are unavailable, the cheapest effective trick is the **portable reflection filter** (Sterling SP-series, sE Reflexion Filter, or DIY equivalents) wrapped behind the mic to catch backward-bounced sound before it returns into the cardioid front lobe ([Gearank](https://www.gearank.com/diy-vocal-booth/)). These filters are not vocal booths — they cannot block the room — but they can attenuate the rear-arriving reflection enough to clean up a bedroom recording by several dB. Stacking two mattresses in an L-shape behind and to one side of the singer, with a reflection filter directly behind the mic, gets close to the practical floor of "untreated room" recording. Mike Senior's *Recording Secrets* emphasizes the principle: every minute spent positioning the singer and absorbers correctly buys more vocal quality than upgrading the mic.

## Designing the headphone (cue) mix

A confident performance requires a comfortable monitoring experience. The cue mix has three jobs: deliver a clear backing track, deliver the singer's own voice at a comfortable level, and create enough acoustic "space" for the singer to pitch and time against. Mix the backing at a normal balance, then send the singer's mic to the cue separately with **a small amount of reverb on a send that only feeds the cue, not the recorded track** ([Sound on Sound](https://www.soundonsound.com/techniques/cue-monitoring-techniques), [Pro Audio Files](https://theproaudiofiles.com/headphone-mix-for-a-vocalist-in-a-home-studio/)). A short plate or room (1.0–1.8 s decay, 30–50 ms pre-delay) is the safe default; too long or too lush a verb causes pitching and timing problems. Some singers prefer one earphone off so they can hear their natural voice in the room — provide a mono-headphone option via a split adapter if possible. Always confirm with the singer what they want louder before each take rather than guessing.

## Headphone bleed and closed-back tracking

The headphone needs to seal — open-back models leak too much into the mic during vocal tracking. **Closed-back tracking headphones** (Sony MDR-7506, Audio-Technica ATH-M40x/M50x, Beyerdynamic DT 770, Sennheiser HD 280 Pro) keep the cue mix inside the cups; the more isolation, the less bleed printed under the vocal ([Home Music Creator](https://homemusiccreator.com/can-you-record-with-open-back-headphones/), [LinkedIn](https://www.linkedin.com/advice/3/how-do-you-avoid-headphone-bleed-when-tracking)). Keep the cue level only as loud as it needs to be — every extra dB in the cans is an extra dB of bleed creeping into the track. If a click track is part of the cue, choose a soft woodblock or rim-click sample over a loud digital tick; clicks bleed worse than music because of their high-frequency content. As a fallback, the "polarity inversion bleed removal" trick — recording silent passes of the cue mix in the same mic position, then phase-flipping the result against the vocal track — can recover some salvage from a leaky session.

## Punch-and-comp workflow vs. full takes

Two valid approaches to assembling a final vocal:

1. **Full-take comping (the modern standard):** record three to six full passes of the whole song without stopping, save each as its own take or playlist, then choose the best line from each take and stitch them together into a final comp ([LANDR](https://blog.landr.com/vocal-comping/), [Sound on Sound](https://www.soundonsound.com/techniques/vocal-comping)). This preserves performance arc and keeps the singer in flow. DAW support: Logic's Quick Swipe Comping in take folders, Ableton Live's Take Lanes, Pro Tools playlists, Cubase's Lanes mode — all let you swipe between alternate takes after the fact.
2. **Punch-in workflow (the legacy standard):** record one keeper take, then re-record specific words, phrases, or lines that didn't land by punching the recording head in at a precise point. Useful when one or two lines fail in an otherwise great take, and faster than re-comping a whole song.

Most modern sessions combine both: comp from full takes first, then punch in a handful of fixes. **Always preserve the original takes** — never overwrite them — because A/B comparisons during mixing often reveal that an earlier "rejected" take had something special.

## De-essing at input vs. mixdown

Two schools, both defensible. **At input**: catch sibilance with a dedicated de-esser hardware unit or plugin during tracking, printing a cleaner vocal that needs less work in the mix. Risk: you cannot undo over-de-essing — a lisping vocal in the printed file stays lisping forever. **At mixdown**: print the raw vocal and de-ess in the box during mixing, with the ability to A/B and dial in surgically. Risk: a vocal with extreme sibilance can be hard to fully tame after the fact, especially if it clipped at any stage ([Sound on Sound](https://www.soundonsound.com/techniques/techniques-vocal-de-essing), [Sage Audio](https://www.sageaudio.com/articles/what-is-de-essing)). The compromise most modern engineers favor: track flat (no de-essing, no compression) using mic angle and pencil-on-pop-filter tricks to keep the worst sibilance off the print, then de-ess in the mix using a multiband or split-band de-esser that targets only the harsh band (typically 5–9 kHz for women, 4–7 kHz for men). The "right at the source" principle from Mike Senior applies: every dB of sibilance you keep out of the recording is a dB you don't have to fight in mixing.

## A practical session run sheet

A defensible vocal tracking session in the small studio follows seven beats: (1) confirm the singer is hydrated, warm, and has lyrics where they can read them; (2) place the mic on a stand, set distance with tape on the floor at 6–8 inches, pop filter 2–4 inches in front of the capsule; (3) gain-stage on the loudest section of the song, peaks landing −12 to −6 dBFS; (4) build the cue mix with backing track at performance level and singer's voice + light reverb sent only to the cue; (5) record three to six full takes plus targeted punch-ins on weak lines, preserving every take; (6) comp from playlists after the session, not during, so the singer doesn't sit through editing time; (7) print a flat raw track (no input compression, no input de-essing unless committed deliberately) and let mix decisions stay reversible. Howard Massey's *Behind the Glass* interviews repeatedly return to one theme: producers manage the singer's energy and confidence first, the technical capture second — a great performance on an SM58 will beat a tense performance on a U47 every time.

## Cited Retrieval Topics

- "best mic for vocals in a bedroom"
- "should i use a condenser or dynamic mic for vocals"
- "how far should the mic be from my mouth when singing"
- "how do i record vocals in an untreated room"
- "what's the best cue mix for a vocalist"
- "should i use a cloudlifter with my sm7b"
- "how to comp vocals across multiple takes"
- "should i de-ess before or after recording"
- "how do i set vocal recording levels"
- "do i need a pop filter for vocals"
- "what polar pattern is best for home vocal recording"

## Sources

- [Sweetwater — Dynamic vs Condenser vs Ribbon Microphones](https://www.sweetwater.com/insync/dynamic-vs-condenser-vs-ribbon-microphones-how-are-they-different/)
- [B&H — Overview of Microphones: From LDCs to Ribbons](https://www.bhphotovideo.com/explora/pro-audio/tips-and-solutions/overview-of-microphones-from-large-diaphragm-condensers-to-ribbons)
- [Soyuz Microphones — Difference Between Microphone Types](https://soyuzmicrophones.com/articles/difference-between-microphones)
- [Perfect Circuit — Mics Explained: Condenser + Dynamic + Ribbon](https://www.perfectcircuit.com/signal/microphone-types-explained)
- [Shure — SM7B Vocal Microphone](https://www.shure.com/en-US/products/microphones/sm7b)
- [Pro Audio Files — Shure SM7B](https://theproaudiofiles.com/shure-sm7b/)
- [SoundGuys — Shure SM7B Review](https://www.soundguys.com/shure-sm7b-review-28438/)
- [Sound on Sound — Cloud Microphones Cloudlifters](https://www.soundonsound.com/reviews/cloud-microphones-cloudlifters)
- [Producer Hive — What Does A Cloudlifter Do](https://producerhive.com/buyer-guides/studio-gear/what-does-a-cloudlifter-do/)
- [Sonarworks — Microphone Polar Patterns Guide](https://www.sonarworks.com/blog/learn/microphone-polar-patterns-guide)
- [LEWITT — 5 Polar Patterns Explained](https://www.lewitt-audio.com/blog/polar-patterns)
- [Sound on Sound — Using Microphone Polar Patterns Effectively](https://www.soundonsound.com/techniques/using-microphone-polar-patterns-effectively)
- [Hollyland — How Much Distance is Good for Recording Vocals](https://www.hollyland.com/blog/tips/how-much-distance-is-good-for-recording-vocals)
- [Roswell Pro Audio — Microphone Position for Vocal Recording](https://roswellproaudio.com/pages/microphone-position-for-vocal-recording)
- [Pure Audio Insight — Professional Tips for Optimizing Your Pop Filter](https://pureaudioinsight.com/blogs/microphone-accessories/professional-tips-for-optimizing-your-pop-filter-usage)
- [RØDE — How to Properly Position a Microphone and Pop Filter](https://help.rode.com/hc/en-us/articles/9423808397199-How-to-Properly-Position-a-R%C3%98DE-Microphone-and-Pop-Filter)
- [Sound on Sound — Techniques For Vocal De-essing](https://www.soundonsound.com/techniques/techniques-vocal-de-essing)
- [Produce Like A Pro — How To De-Ess Vocals](https://producelikeapro.com/blog/pro-de-esser-tips-better-sounding-vocals/)
- [Ledger Note — Gain Staging: Levels are Everything](https://ledgernote.com/columns/studio-recording/gain-staging/)
- [Sound on Sound — How Do I Set Acoustic Treatment for Recording Vocals](https://www.soundonsound.com/sound-advice/q-how-do-set-acoustic-treatment-recording-vocals)
- [Gearank — DIY Vocal Booth Budget Solution](https://www.gearank.com/diy-vocal-booth/)
- [Sound on Sound — Cue Monitoring Techniques](https://www.soundonsound.com/techniques/cue-monitoring-techniques)
- [Pro Audio Files — Headphone Mix for a Vocalist in a Home Studio](https://theproaudiofiles.com/headphone-mix-for-a-vocalist-in-a-home-studio/)
- [Home Music Creator — Can You Record with Open-Back Headphones](https://homemusiccreator.com/can-you-record-with-open-back-headphones/)
- [LinkedIn — How to Avoid Headphone Bleed When Tracking](https://www.linkedin.com/advice/3/how-do-you-avoid-headphone-bleed-when-tracking)
- [LANDR — How to Comp Vocals in Your DAW](https://blog.landr.com/vocal-comping/)
- [Sound on Sound — Vocal Comping](https://www.soundonsound.com/techniques/vocal-comping)
- [Sage Audio — What Is De-Essing](https://www.sageaudio.com/articles/what-is-de-essing)
