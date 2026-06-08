# Inside Track: Billie Eilish 'Bad Guy'

**Source:** Sound on Sound, "Inside Track" series by Paul Tingen
**URL:** https://www.soundonsound.com/techniques/inside-track-billie-eilish-bad-guy
**Captured:** 2026-05-24
**Tags:** `mixing`, `vocal-mixing`, `low-end`, `parallel-processing`, `plugin-chain`, `example`

---

## Credits & Context

Album *When We All Fall Asleep, Where Do We Go?* (Billie Eilish, 2019) credits only four:

- Billie Eilish (artist)
- Finneas O'Connell (producer)
- Rob Kinelski (mixer)
- John Greenham (mastering)

Mixer Kinelski's mindset on minimalism: *"I was imagining being slammed on gearslutz.com. I loved it, but I wondered how it would translate to the world."*

## Kinelski's General Mix Methodology

- Hip-hop-derived order: **drums → vocals → bass → keys → additional elements**, grouped
- Stems load at unity into a template; effect-aux tracks are routed
- For Eilish album: minimal effects — primarily a **"Width" aux track using Soundtoys MicroShift**
- Vocal editing (pencil-tool artifact removal) done at end of mix because she sings very quietly

Quote: *"It is really easy in this day and age to overdo surgery. You're mixing visually... you swear you can hear the difference. It's really easy to fall down that rabbit hole."*

## 'Bad Guy' Pro Tools Session

- **68 total tracks; 49 audio tracks**
- 21 drums/percussion, 21 vocals, 4 bass, 1 synth
- **Seven aux groups**: Kick, Main Snare, Sub Bass, Lead Vocals, Lead Vocal Doubles, Lead Vocal Harmonies, Backing Vocals
- Eight stereo sends to **Dangerous 2-Bus summing mixer**:
  - DBuss 1-2: drums
  - 3-4: bass
  - 5-6: synths
  - 9-10: lead vocals
  - 11-12: backing vocals
  - 15-16: Width processing

## Kick aux chain

- Waves SSL Channel Strip (cutting 260 Hz on individual kick; on aux: gating, **4:1 compression**, fast attack, quick release, +9 dB at 3 kHz, +3 dB at 90 Hz)
- FabFilter Pro-Q 2 (cut 500 Hz, boost 60 Hz / 200 Hz / 800 Hz)

## Snare aux chain

- Waves SSL Channel (**5:1 compression**, slow attack, slow release, ~4 dB transient compression; gating for punch)

## Sub Bass aux chain (two main bass tracks + one "dirtybass")

- Waves SSL Channel Strip (boost ~800 Hz, cut ~400 Hz, fast attack, slow release, **6:1**)
- Waves Renaissance Compressor (**20:1**, fast attack, medium release, **sidechained to first kick**)

## Synth (chorus only) chain

- Waves SSL Channel (+1 dB, used as a fader)
- Sonnox Oxford Inflator (50% — for mid-range harmonics)
- Send to Width aux with Soundtoys MicroShift

## Vocal chain (identical across all 4 vocal groups, varied only by EQ)

1. FabFilter Pro-Q 2 (low-cut)
2. Waves PuigChild 670 (smoothing compressor)
3. Waves De-Esser at **6557 Hz** (surgical, post-compression sibilance)
4. FabFilter Pro-Q 2 (cut 200 Hz – 2 kHz midrange)
5. UAD Neve 1073 EQ (color only — engaged without adjustment)
6. Waves Vocal Rider (~1.5 dB)
- Manual level automation via Avid Artist Mix
- **No timing correction or tuning** on Eilish's vocals

## Drum bus

- UAD Pultec EQP-1A (+2 dB at 60 Hz)
- Steven Slate Virtual Mix Rack (British 4k console modeling, input clipping for harmonic distortion)

## All group busses

- Steven Slate Virtual Mix Rack
- Backing vocal bus also gets Oxford Inflator

## Master chain (after Dangerous 2-Bus summing)

1. UAD Ampex ATR-102 tape (30 ips, half-inch; hiss disabled per artist preference)
2. UAD Thermionic Culture Vulture (minimal drive)
3. FabFilter Pro-L 2 (preset: **'EDM-Aggressive and Tight'**)
4. TC Electronics Clarity M meter

This identical master chain applied to all album tracks.

## Hardware

- Pro Tools HD Native, Avid I/O 16x16, 8-fader Avid Artist Mix
- Outboard: Dangerous 2-Bus, Dangerous compressor (4:1 stereo-linked, bass-cut + sibilance-boost sidechain), Dangerous Convert-AD+, Dangerous Monitor ST
- Monitoring: ProAc Studio 100s, NS10s, Avantone CLA-10s, Auratones

The 2-Bus: **+6 dB input, ~4 dB output reduction** — produces *"more harmonics, and some more depth, and a little bit more separation"*.

## Cited Retrieval Topics

- Specific compression ratios per source (kick 4:1, snare 5:1, sub 6:1 + 20:1 parallel, bass-to-kick sidechain)
- Vocal de-esser frequency (6557 Hz)
- Plugin order for vocal chains
- Master chain template for hip-hop-adjacent pop
- Parallel summing-mixer workflow (in-the-box hybrid)
- Restraint principle: *"sometimes mixing involves literally doing nothing"*
