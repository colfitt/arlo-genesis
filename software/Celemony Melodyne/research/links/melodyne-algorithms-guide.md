https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_AudioAlgorithms?env=standAlone

celemony.com help · "Audio characteristics and algorithms" · accessed 2026-06-11

The algorithm decides how Melodyne hears a recording. **Pick it before editing** — switching algorithms re-analyses the track and **discards any edits/copies you'd already made**.

## The algorithms
- **Melodic** — monophonic, one note at a time. Lead vocals, speech, sax, flute, **single-note bass/guitar/banjo lines**. Auto-detects sibilants and leaves them unaffected by pitch moves. *(Use this for a banjo/baritone single-note lead.)*
- **Percussive (Unpitched)** — drums, percussion, noise, **atmospheric/no-clear-pitch material**. Separates strokes but shows them all at one pitch level; the ruler shows relative semitones, scale functions off.
- **Percussive Pitched** — melodic percussion (808 kick, tabla, berimbau): assigns pitches so you can tune. Sibilant detection off by default (enable in Note Assignment Mode).
- **Universal** — complex signals mixing percussive + tonal. Best when you only want to **transpose / time-stretch / tempo-shift a whole mix or a strummed rhythm part** without per-note editing. Fast, low resource. (Attack Speed tool unavailable; must be chosen manually.)
- **Polyphonic Sustain** — chords where the attack ≈ the sustain: **legato strings, organ, pads, sustained drones**. Chords show as **stacked blobs**.
- **Polyphonic Decay** — chords where the attack differs sharply from the tail: **guitar, banjo, piano, pizzicato**. Also stacked blobs. *(Use this for strummed/fingerpicked banjo or baritone chords — DNA, needs Editor+.)*

## Quick map for this rig
| Source | Algorithm | Edition needed |
|---|---|---|
| Banjo/baritone **single-note lead** | **Melodic** | Assistant |
| Strummed/fingerpicked **banjo or baritone chords** (edit individual notes) | **Polyphonic Decay** | **Editor** (DNA) |
| Sustained string/organ-style **drone chord** | **Polyphonic Sustain** | Editor (DNA) |
| **Whole loop / mix / texture** — just transpose or stretch | **Universal** | Essential+ |
| **Drum / noise / atmospheric** sample to re-time or re-pitch as one block | **Percussive** | Essential+ |

## Note
Get the algorithm right up front. If a strummed banjo imports as Universal (one block) and you want to grab individual chord notes, switch to **Polyphonic Decay** *before* you start editing — switching afterward wipes your edits.
