---
type: cover
title: "Weird Fishes/Arpeggi"
artist: Radiohead
album: In Rainbows
year: 2007
date: 2026-06-10
key: Em
tempo: 148
time_signature: 4/4
---

# Weird Fishes/Arpeggi — Cover Plan

## The Song

Built on interlocking, phase-offset arpeggios in the tradition of Steve Reich — three guitar parts weaving against each other over a driving bass and drums, building to a distorted climax before dissolving into a ghostly outro. Key of Em, ~148 BPM. The magic is in the *lattice* — no single part carries the song; the interlock does.

## Arrangement Strategy

Solo performer covering a five-piece. The approach: **build the arpeggio lattice via looping/sampling, play the lead lines live, use the Octatrack as the rhythmic spine.**

### Sections

| Section | Bars | What Happens |
|---------|------|-------------|
| Intro | 1-8 | Single arpeggio (Guitar 1), drums fade in |
| Verse 1 | 9-24 | Guitar 2 enters, bass locks in, vocal |
| Verse 2 | 25-40 | Guitar 3 joins the lattice, fuller dynamics |
| Chorus/Build | 41-56 | All parts at full intensity, vocal climax |
| Climax | 57-72 | Distorted lead, aggressive strumming |
| Outro/Dissolve | 73-end | Parts drop away, ghostly decay |

## Signal Chain & Role Assignment

### Rhythm Section — Elektron Octatrack MkII
- **Role:** Master clock, drum sequencing, bass sample playback
- Program Phil Selway's drum pattern (driving 16ths on hi-hat, snare on 2 & 4, kick pattern syncopated)
- Sample or synthesize Colin Greenwood's bass line (octave root movement: Em - G - D - A pattern)
- Use scene crossfader for the build — thin/filtered drums in intro, open up through verses
- MIDI clock out to sync TimeLine and any clocked effects

### Guitar 1 — Thom Yorke's Arpeggio (Looped)
- **Chain:** Guitar > Boss CE-2W (CE-2 mode, subtle) > Strymon Iridium (Chime, clean Vox-style) > Octatrack input (sample and loop)
- 16th-note arpeggio pattern on upper strings, capo-dependent voicing
- Record into Octatrack as a loop on Track 1 — this is the foundation layer
- CE-2W adds the slight chorused shimmer Thom's clean tone carries

### Guitar 2 — Jonny Greenwood's Counter-Arpeggio (Looped)
- **Chain:** Guitar > Chase Bliss Clean (light compression, clean tone) > Strymon Iridium (Chime) > Octatrack input
- Second arpeggio pattern — offset rhythm against Guitar 1, different string set
- Record into Octatrack Track 2
- Bring in at Verse 1 via Octatrack scene/mute

### Guitar 3 — Ed O'Brien's Textural Arpeggio (Looped)
- **Chain:** Guitar > Strymon TimeLine (dotted-eighth delay, ~50% mix) > Strymon Big Sky (Shimmer or Bloom, moderate) > Octatrack input
- Ed's part is the most atmospheric — rhythmic delay creates the phase-drift effect
- TimeLine synced to Octatrack MIDI clock for tight dotted-eighth lock
- Record into Octatrack Track 3, bring in at Verse 2

### Live Lead / Vocal Guitar — Climax Section (Played Live)
- **Chain:** Guitar > Oxford Drive (gain at noon — Marshall ShredMaster bark) > Strymon Deco V2 (Saturation side, tape warmth) > Strymon Iridium (Punch, driven amp) > front-of-house / Apollo x8
- The Oxford Drive is *literally* voiced after Radiohead's hometown and the ShredMaster lineage — this is the correct distortion for the climax
- Deco adds tape compression and thickness behind the drive
- Play the aggressive strummed chords and lead bends live over the looped lattice

### Outro / Dissolve
- **Chain:** Guitar > Chase Bliss Generation Loss (wow + flutter up, hiss in) > OBNE Dark Star V3 (Pitch mode, long decay, freeze) > Strymon Big Sky (Cloud, infinite)
- As loops drop out one by one on the Octatrack, play sparse notes through this chain
- Generation Loss degrades the signal into tape-ghost territory
- Dark Star freezes the final chord into a shimmer pad
- Big Sky Cloud washes everything into infinity

## Recording Path

All stereo outs to **UA Apollo x8** — Octatrack stereo out on inputs 1-2, live guitar (post-Iridium stereo) on inputs 3-4. Track in your DAW.

## Performance Flow

1. **Pre-session:** Program Octatrack — drum pattern + bass on dedicated tracks, empty tracks ready for guitar loop capture
2. **Start Octatrack.** Drums come in filtered/sparse. Play and capture Guitar 1 arpeggio loop.
3. **Verse 1:** Unmute Octatrack drums full, bring in bass. Capture Guitar 2 loop. Sing.
4. **Verse 2:** Capture Guitar 3 (delay/reverb) loop. All three arpeggios now interlocking. Sing.
5. **Chorus/Build:** All loops running. Push Octatrack scenes for energy. Sing the climax vocal.
6. **Climax:** Swap to Oxford Drive chain. Play distorted lead/strums live over the lattice.
7. **Outro:** Swap to Generation Loss > Dark Star > Big Sky chain. Mute Octatrack loops one by one. Let the last notes freeze and decay.

## Gear Used

| Gear | Role |
|------|------|
| Elektron Octatrack MkII | Master clock, drums, bass, loop capture/playback |
| Strymon Iridium | Amp tone (Chime for cleans, Punch for climax) |
| Boss CE-2W | Chorus shimmer on Guitar 1 |
| Chase Bliss Clean | Compression on Guitar 2 |
| Strymon TimeLine | Dotted-eighth delay on Guitar 3 (Ed's part) |
| Strymon Big Sky | Reverb (Bloom for Guitar 3, Cloud for outro) |
| Oxford Drive | Climax distortion — ShredMaster lineage, Radiohead DNA |
| Strymon Deco V2 | Tape saturation behind drive |
| Chase Bliss Generation Loss | Outro tape degradation |
| OBNE Dark Star V3 | Outro freeze/shimmer |
| UA Apollo x8 | Recording interface |

## Notes

- The Octatrack is the linchpin — it replaces the band. Practice the loop-capture workflow before attempting a full take.
- The Oxford Drive is a poetic fit here. A pedal named after Radiohead's hometown, voiced after the ShredMaster Jonny used on early records.
- Godrich's "print and commit" philosophy from the In Rainbows sessions applies: capture each guitar loop in one pass and live with it. Don't re-do. Let the slight imperfections create the phase-drift that makes the original magical.
- Consider using the Radial X-Amp if you want to re-amp any of the DI'd arpeggio takes through different pedal chains after the fact.

## Sources

- `gear/Oxford Drive/GearProfile.md` — ShredMaster/Guv'nor lineage, Radiohead connection
- `gear/Strymon Iridium/GearProfile.md` — Round/Chime/Punch amp models
- `gear/Strymon TimeLine/GearProfile.md` — 12 delay machines, MIDI sync
- `gear/Strymon Big Sky/GearProfile.md` — reverb algorithms
- `gear/Chase Bliss Blooper/GearProfile.md` — looper reference (Octatrack chosen instead for multi-track capability)
- `gear/Elektron Octatrack MkII/GearProfile.md` — 8-track sampler/sequencer
- `gear/Boss CE-2W/GearProfile.md` — Waza Craft chorus
- `gear/Chase Bliss Clean/GearProfile.md` — VCA compressor
- `gear/Chase Bliss Generation Loss/GearProfile.md` — tape degradation
- `gear/OBNE Dark Star V3/GearProfile.md` — ambient reverb with freeze
- `gear/Strymon Deco V2/GearProfile.md` — tape saturation
- `gear/Roland VG-800/GearProfile.md` — guitar synth (available for bass if sampling isn't preferred)
- `gear/UA Apollo x8/GearProfile.md` — recording interface
- `gear/Radial X-Amp/GearProfile.md` — re-amp option
- `arlo/corpus/artists/radiohead-in-rainbows-production.md` — In Rainbows production notes, "Weird Fishes" as Steve Reich phasing, Godrich's "print and commit" method
