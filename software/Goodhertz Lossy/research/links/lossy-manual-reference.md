https://manuals.goodhertz.com/3.13/lossy/
manuals.goodhertz.com · Official Lossy manual (v3.13) · authoritative parameter reference

The complete, authoritative control map for "Ghz Lossy 3" (the installed build).
Lossy is a CREATIVE codec-artifact effect — explicitly **not based on any real
codec/standard** ("not an MP3 codec checker"); it generates the *sound* of heavily
compressed audio in a tweakable realtime plugin. Signal flow is, roughly:
Preprocess gain → (Verb if Pre) → Filter → Loss → (Verb if Post) → output.

## PRIMARY CONTROLS

### Verb section
- **Verb Position** — **Pre** or **Post** (default Pre). Pre = reverb is fed *into*
  the loss processing, so the verb tail itself gets "Lossified" → "more full and
  expansive." Post = reverb sits after, as conventional space.
- **Verb Amount** — reverb intensity. Default 0%.

### Filter section
- **Filter Mode** — **Normal** (bandpass) or **Inverted** (bandreject).
- **Low Cut Freq** — default 20 Hz.
- **High Cut Freq** — default 20.0 kHz.
- **Filter Slope** — shared slope for both cuts. Default **24 dB/Oct** (steeper =
  more abrupt/telephone-band sound).

### Loss section (the core)
- **Loss Mode** — **Standard · Inverse · Phase Jitter · Packet Repeat · Packet Loss
  · Standard + Packet Loss · Standard + Packet Repeat**. (Standard = the core MP3-
  style spectral crush; Phase Jitter = the swirly/warbly artifact; Packet Loss /
  Repeat = dropouts / stuttering "bad-connection" glitches; the hybrids combine
  the steady crush with intermittent packet glitches.)
- **Loss Amount** — compression/degradation intensity. Default 0%.
- **Loss Speed** — "**slower speeds have more spectral smear, faster speeds tend to
  sound more garbled.**" Default 100%. (The character knob: slow = smeared/swirly,
  fast = garbled/glitchy.)
- **Loss Gain** — output level (embedded peak meter). Default 0.0 dB.

### Master
- **Master Mix** — global wet/dry. Default 100%. (A TRUE global dry/wet — unlike
  SketchCassette, which lacks one.)
- **Master On/Off** — bypass. Default On.

## ADVANCED CONTROLS (1 page)
- **Verb Decay** — 0%–200%. Default 100%.
- **Auto Gain** — "helps keep the perceived volume the same even when much of the
  audio information has been removed." Default 0%. (Turn up so heavy loss doesn't
  drop the level.)
- **Gate Threshold** — silence/gate threshold. Default −96.0 dB. (Mutes the noise/
  artifact tail in the gaps — see the ad-libs transcript's "jagged" trick.)
- **Stereo Mode** — **Stereo · Joint Stereo · Mono**. (Joint Stereo is the source
  of the classic MP3 "stereo collapse / swirly side-channel" artifact; Mono =
  mono-collapsed loss; Stereo = independent L/R loss.)
- **Weighting** — **Perceptual** (psychoacoustic, codec-like) or **Flat**. Perceptual
  removes "least audible" content first (more codec-realistic); Flat treats the
  spectrum evenly.
- **Preprocess Input Gain** — default 0.0 dB (drive into the processing).
- **Postprocess Output Gain** — default 0.0 dB.

## FACTORY PRESETS (named)
**General:** Default · 128/96/64/32 kbps · Digital Garbage · Singing Glasses ·
Cellphone Muzak (I & II) · Detroit Factory · Bad Cell Connection · Bad Video
Streaming · Digital Blizzard · Static · Ghost in the MP3 · Can't Acquire Signal ·
Enter the Matrix · Infinite Hold · Deep Space Network · Digital Raindrops · Weak
Satellite · Jitterverb variations.

**Verb:** 32 kbps Verb · Bad Live Streaming · Spectral Blur · Atlantic Cathedral ·
Siney Verb · Deeper Space Network · Whale Song · Supermarket @ 3:00 AM ·
Packetlossgate · Broken Left/Right Pair · Digital Raindrops (in a Cave).
