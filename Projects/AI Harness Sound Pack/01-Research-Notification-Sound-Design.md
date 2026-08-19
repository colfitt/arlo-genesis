# Research — how the big companies design notification sounds

Everything in the spec and production plan traces back to something here. Sources are
linked inline; the last section distills what this pack actually adopted.

## Slack — the sound as workplace etiquette

- The default **"Knock Brush"** came from a musician friend of Stewart Butterfield who
  spent a day at a drum kit: a wire brush swept across a drum head plus knuckles rapped
  quickly — an *expedited door knock*. A knock is the perfect workplace metaphor: polite,
  attention-getting, not an alarm ([Hii Magazine](https://hii-mag.com/article/phonenoti-lds),
  [CNBC interview with Butterfield](https://www.cnbc.com/video/2019/06/20/slack-ceo-explains-the-messaging-companys-knock-brush-notifcation-sound.html)).
- Slack's sounds largely derive from **Glitch**, the game Tiny Speck built before Slack —
  game-audio assets became product identity ([Glitch — Wikipedia](https://en.wikipedia.org/wiki/Glitch_(video_game))).
  The **"Hummus"** option is Head of Brand Communications Anna Pickard saying the word
  ([TechCrunch](https://techcrunch.com/2019/05/30/the-slack-origin-story/)).
- Philosophy: percussive/atonal so it cuts through without a melody that wears out;
  heavy user control (per-channel sounds, quiet hours, silence as an option).
- Huddles' "jukebox" hold music brief, per designer Mikey Maleki: "simple, functional
  and not disruptive… but still playful" ([Malfred](https://malfred.co/SLACK-Huddles-Jukebox)).

## Apple — a thousand no's for every yes

- **Tri-tone** was built in 1998 by engineer Kelly Jacklin as a CD-burn *completion*
  alert: **marimba playing root–fifth–octave** — consonant and unambiguous. It became
  the iPhone SMS default in 2007 ([Twenty Thousand Hertz](https://www.20k.org/episodes/the-sound-of-apple)).
- **Rebound** (iOS 17 default): a gentle two-note *rising* figure replacing the falling
  Tri-tone — and the backlash ("too quiet") forced Apple to make the default changeable
  in 17.2. Lesson: **calm is a value, but audibility is a requirement**
  ([Macworld](https://www.macworld.com/article/2156872/ios-17-2-change-default-alert-notification-sound-tri-tone-rebound.html)).
- The **Apple Watch team recorded the device's actual materials** (steel, aluminum,
  gold) so alerts feel like they come from the object. Calendar uses **kalimba**
  because it's characterful but uncommon ([WWDC17 "Designing Sound"](https://developer.apple.com/videos/play/wwdc2017/803/)).
- WWDC17 (Hugo Verweij) is the canonical craft talk. A good notification sound is:
  **distinguishable, matched to the product's aesthetic, unobtrusive under repetition**
  ("live with it for a week"), and **clean enough to cut through noise without being
  abrasive**. Also: **filter out lows** phone speakers can't reproduce, keep sounds
  short so they don't duck music for long, sync sound + haptic to ~10 ms, and
  "**silence is golden**."
- Design lead Billy Sorrentino: "we find an instrument and record it beautifully" and
  "a thousand no's for every yes" ([20k.org part 2](https://www.20k.org/episodes/the-sound-of-apple-2)).

## Google — designed silence and a sound taxonomy

- Material's sound guidance (Conor O'Sullivan, Head of Sound & Haptics) treats
  **silence as the audio equivalent of negative space** — some events deliberately get
  no sound ([Designing Sound and Silence](https://medium.com/google-design/designing-sound-and-silence-1b9674301ec1),
  [Material sound attributes](https://m2.material.io/design/sound/sound-attributes.html)).
- Taxonomy: **hero sounds** (rare brand moments) → **primary system sounds**
  (alerts/notifications, the most restrained) → **secondary/decorative**. Bright
  timbres read as "important" in noisy rooms without extra loudness.
- Pixel sounds are **real recordings of simple acoustic sources** because tiny
  speakers reward pure timbres: the boot sound is a real piano, two notes an octave
  apart, deliberately "flammed"; the camera shutter is processed scissors — recorded in
  O'Sullivan's home studio ([design.google](https://design.google/library/sound-and-vision),
  [blog.google](https://blog.google/products/pixel/google-pixel-sound-design/)).
- Three functional categories: **gesture feedback**, **semantic feedback**,
  **attention sounds** ([Method Podcast Ep. 13](https://design.google/library/google-pixel-sound-design-ux-conor-osullivan)).
- Platform guardrail worth copying: Android **rate-limits notification sounds to one
  per second per app** ([Android Authority](https://www.androidauthority.com/android-8-1-limits-notification-sounds-one-per-second-every-app-810207/)).

## Microsoft — calm, rounded, non-instrumental

- Windows 11's sounds (audio direction lineage: **Matthew Bennett**, who did Win 8/10)
  were "led by the idea of calm": literally **rounder waveforms** — softer attacks and
  decays mirroring the rounded corners — that alert without startling
  ([CNBC](https://www.cnbc.com/2021/08/22/microsoft-delivers-calm-system-sounds-in-windows-11.html),
  [Windows Central](https://www.windowscentral.com/microsoft-rounded-sounds-not-just-corners-when-designing-windows-11)).
- Deliberately **not evocative of any recognizable instrument**, to avoid cultural
  associations; the notification shrank from four notes to two close, slightly
  ascending ones ([Ctrl blog](https://www.ctrl.blog/entry/windows-alert-sounds.html)).
- **Dark mode gets its own, softer sound variants** ([MakeUseOf](https://www.makeuseof.com/windows-11-different-audio-profiles-light-dark-mode/)).
- The startup sound returned ("Petals") partly for **accessibility** — blind users
  needed an audible "system ready" cue. Win 10's sounds were modeled on **human vocal
  intonation** (the calendar alert is melodically "Ready to go?")
  ([Windows Experience Blog](https://blogs.windows.com/windowsexperience/2018/08/28/story-labs-how-microsofts-matthew-bennett-cuts-through-noise-to-create-a-sound-world/)).

## Others, briefly

- **Netflix "Ta-dum"**: sound designer Lon Bender's wedding ring knocking a cabinet,
  ~2.5–3 s — proof a hero sound can be foley ([20k.org](https://www.20k.org/episodes/netflix)).
- **Zoom's** join/leave chime is a literal **doorbell** — an auditory icon whose
  metaphor does the explaining.
- **Duolingo's** correct-answer ding (studio: Proper Sounds) is engineered
  positive reinforcement.
- Most relevant precedent for an AI harness: **VS Code accessibility signals** — quiet
  earcons for "Copilot suggestion appeared", "line has an error", "agent task
  finished". Sound as an ambient state channel for agentic tools
  ([GitHub accessibility docs](https://accessibility.github.com/documentation/guide/github-copilot-vsc/),
  [vscode #250915](https://github.com/microsoft/vscode/issues/250915)). AI products
  are largely a sonic blank slate today — an actual identity here is differentiation.

## Craft numbers

**Duration.** Interaction blips ≤ 250 ms; notifications ≤ 1 s (research found 0.5–1 s
earcons preferred over 2 s; iOS hard-caps custom sounds at 30 s)
([CHI study](https://dl.acm.org/doi/10.1145/1518701.1518932), [uisfx.com](https://uisfx.com/ui-sound-design)).

**Frequency.** Ear sensitivity peaks ~2–4 kHz; target roughly 1.5–6 kHz for
cut-through, but keep mid-band fundamentals because age-related hearing loss takes the
highs first. High-pass the sub-lows — small speakers can't make them and they eat
loudness (Apple WWDC17, [NCBI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8125668/)).

**Loudness.** No universal UI-sound standard, but: Google's earcon spec is **−16 LUFS
stereo / −19 LUFS mono, true peak ≤ −1.5 dBTP**
([Google audio-loudness](https://developers.google.com/assistant/tools/audio-loudness));
practice guidance puts alerts around −14 to −12 LUFS and subtle ticks −18 or below;
keep true peaks ≤ −1 dBTP minimum because lossy codecs add inter-sample peaks. UI
feedback < notifications < alarms, and all of it below speech and music.

**Semantics.** Rising contour ↦ incoming/positive; falling ↦ done/outgoing; low,
dense, or dissonant ↦ error. But pitch–valence mapping is weak on its own — encode
meaning **redundantly** in contour + rhythm + timbre + register
([Wayfindr guidelines](https://www.wayfindr.net/open-standard/guidelines/mobile-app-development/guidelines-for-sound-design),
[Cognitive Science 2026](https://onlinelibrary.wiley.com/doi/abs/10.1111/cogs.70253)).
Vocabulary: **earcons** (abstract learned motifs, Blattner 1989) vs **auditory icons**
(caricatures of real-world sounds, Gaver) — auditory icons test better on
learnability; earcons form tighter families.

**Fatigue.** Exposure frequency is the fatigue driver: "a cue heard once a day can be
expressive; a cue heard fifty times an hour should be quiet, brief, or absent."
Wooden/mallet timbres (marimba, kalimba, glockenspiel) recur across Apple, Slack, and
Futurice guidance as pleasant-under-repetition. For very frequent cues, ship 5–12
randomized micro-variants ([Not Boring — The Sound of Software](https://notbor.ing/words/the-sound-of-software)).

**Accessibility.** Never rely on sound alone (pair with visuals); WCAG 1.4.2 requires
user control of audio > 3 s; honor OS mute/DND; sound can *be* the accessibility
feature (Windows startup for blind users, VS Code signals for screen-reader parity).

## Production knowledge (condensed — the plan applies it)

- **Three approaches, all professional:** pure synthesis (Windows 11), recorded
  acoustic sources (Pixel's piano and scissors), and **hybrid layering** — the default
  pro move: one organic voice + a sine sub-layer an octave down + a tiny transient
  layer ([Not Boring](https://notbor.ing/words/the-sound-of-software)).
- **Family first:** "narrow down to one particular timbre consistent throughout" before
  designing any individual sound ([Microsoft Kaizala case study](https://medium.com/sound-experience-design/how-i-designed-the-notification-sound-for-microsoft-kaizala-caa20f593a6)).
- **Capture:** 96 kHz/24-bit when recording (headroom for pitch work), deliver at
  48 kHz; quiet room beats treated room at these durations; small-diaphragm condensers
  with low self-noise are the standard pick ([Boom Box Post](https://www.boomboxpost.com/blog/2017/5/31/designing-sound-effects-with-high-sample-rates)).
- **Post:** trim to onset, 2–5 ms fade-in, high-pass, transient-shape, gentle
  true-peak limiting to −1.5 dBTP; normalize the family relative to itself, then
  final-trim by ear.
- **Delivery:** mono WAV 48k masters + OGG (lowercase names, Android) + M4A/AAC
  (Apple/web); < 30 s hard iOS cap; machine-sortable versioned filenames.
- **Testing gauntlet:** loop each sound 50–100×; play over speech and music; phone
  speaker + laptop speaker + earbuds + monitors; live with the set for a week.
- **Market context:** marketplace licensing $1–5/sound (no identity), freelance custom
  15-sound family ≈ $1.5k–8k over 2–6 weeks, agency sonic branding €15k+
  ([Twine rates](https://www.twine.net/blog/sound-designer-hourly-rates/),
  [Supadark pricing guide](https://supadark.com/notes/sonic-branding-pricing-guide)).

## What this pack takes from all of it

1. **One family voice** (struck-bell/kalimba hybrid) — Apple's kalimba calendar,
   Material's pure acoustic timbres, and Kaizala's one-timbre rule all point here.
2. **Rising = incoming, falling-resolving = done, low-damped = trouble**, encoded
   redundantly in contour *and* timbre *and* register — per the semantics research.
3. **Calm without the Rebound mistake**: quiet errors, tiered loudness, but Tier 1
   attention cues stay genuinely audible.
4. **Everything under 1 s**, ticks near 100 ms — squarely inside the research window.
5. **Mirrored pairs** (connect/disconnect, approve/deny) — the AirDrop up/down pattern.
6. **Designed silence**: the harness plays nothing for most events; 15 cues is the
   ceiling, not the floor.
7. **Google's loudness spec** (−19 LUFS mono, −1.5 dBTP) as the mastering anchor.
8. **Variants for frequent cues** and Android-style rate limiting in the harness.
