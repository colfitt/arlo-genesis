https://www.thefretboard.co.uk/discussion/73405/streets-have-no-name-on-the-strymon-timeline + https://www.strymon.net/faq/timeline-dual-delay-common-ratio-settings/ + Strymon Swell/Ice machine docs + Hell-Float-Trip preset blog
theFretBoard (user "professorben") + strymon.net (FAQ + machine docs) · multi-source

Concrete, community-sourced recipes. Settings quoted from forum users / Strymon.

## U2 / The Edge — "Where the Streets Have No Name" (Dual machine)
**The most-documented TimeLine patch.** Two approaches:

**(A) Two explicit delay lines (professorben, theFretBoard) — song ~129 BPM:**
- Machine: **Dual**, run in parallel; pan delays slightly L/R if stereo
- **Delay 1:** TIME **523 ms**, MIX ~50/50, **REPEATS = 1**, type **dBucket** if available
- **Delay 2:** TIME **323 ms**, MIX ~30/70, **REPEATS = 3–4**, type dBucket
- Quote: *"Set one for 523ms at 50/50 … one repeat, the 2nd delay line set to 323ms at about 30/70 … with 3-4 repeats."*

**(B) Single dotted-eighth approach (user "Cirrus" / general Edge):**
- ~**360–400 ms** main time, **dotted-eighth** subdivision, MIX ~**40%**, **3–4 repeats**, **fast+shallow modulation ~4–5 Hz**.

**Strymon official Dual ratios** (TAP subdivision → Delay-2 ratio):
| Feel | Delay 2 | Ratio |
|---|---|---|
| triplet | triplet | 1/3 |
| eighth | 8th | 1/2 |
| **dotted-eighth + quarter (the Edge trick)** | dotted 8th | **3/4** |
| sixteenth | 16th | 1/4 |
| unison | quarter | 1/1 |

External deep reference users cite for exact Edge times: **amnesta.net/edge_delay/streets.html**.

## Ambient / drone recipes (Strymon machine guidance + community)
**Swell pads (banjo/baritone-as-lead):**
- Machine: **Swell**. Set **Rise Time ≈ delay time** for natural volume-swell repeats. Turn **MIX full wet** and **REPEATS up** for ethereal washes. Plucked notes "bow in" as pads. (Strymon Swell doc.)

**Ice shimmer — "Hell Float Trip" (Strymon preset):**
- Machine: **Ice**, **BLEND = all the way to ICE**, **Smear = max** (softens the attack of the pitched repeats), interval set with a slight **-25 cent** detune for a seasick float.
- **Quirk:** with BLEND full-ICE, **SPEED & DEPTH do nothing** (they only modulate the dry delay lines you're not hearing). Don't waste time dialing them.
- For +octave shimmer: Ice interval **+1 oct** (or **+oct & 5th**), high repeats, MIX 11–12, High-Pass ~160Hz to keep banjo from ice-picking.

**Reverse swell:** the Reverse machine is **input-triggered** — the backwards swell is "predictable, musical, and repeatable" (not random). Good for intros/lead lines.

**Self-oscillating drone bed:** any of dTape/dBucket/Digital with REPEATS toward max, then **hold the footswitch for infinite** to freeze the wash and play over it.

## Rig notes
- For the failover/Edge patch synced to the Digitakt 2: set that preset **MIDICL = ON** so it locks to the master tempo; use **dotted-eighth tap division**.
- Drone/Swell/Ice presets: **MIDICL = OFF** so the wash isn't yanked to song tempo.
