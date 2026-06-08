https://www.thegearpage.net/board/index.php?threads/chase-bliss-lost-found.2684103/
thegearpage.net + community video deep-dives · compiled 2026-06 · FORUMS/COMMUNITY facet

# Lost + Found — community power-user tips, hidden behaviors, gotchas & firmware lore

Synthesis of the highest-signal community material for the Lost + Found. **Honest framing: peer-to-peer text-forum coverage is THIN and largely un-scrapeable.** The richest community knowledge is in two long-form demo/teardown videos (transcribed in `../transcripts/`), not in forum prose. Forum threads exist but block automated reading (403 / paywall proxy) — listed at bottom for the human to read directly. Nothing here is fabricated; un-confirmed items are flagged.

## Best community sources (annotated)
- **Mark Johnston, "Secret Weapons" (70 min, Aug 2025)** — best routing/workflow tutorial; recorded on **beta firmware** (flagged). Transcript: `../transcripts/secret-weapons-mark-johnston-walkthrough.md`.
- **BachelorMachinesTV, "Let's Do Some Science" Pt 1 & 2 (Oct–Nov 2025)** — deepest *technical* teardown on a **shipping** unit; documents the Sympathetic Resonator firmware change. Transcripts: `../transcripts/bachelormachinestv-science-part1.md` and `-part2.md`.
- **TheGearPage megathread** (URL above) — most active owner thread (29+ pages by mid-2026) but served via a paywall/Tollbit proxy (HTTP 402/307) — read in a browser.
- **The Gear Forum** thread 9471, **TalkBass** "...I'm in" (bass angle), **MOD WIGGLER** (modular angle) — all 403 to scrapers; see coverage-state file for URLs.

## POWER-USER TIPS (concrete)
1. **MODIFY noon = effect OFF on purpose.** Every channel passes signal but does nothing at MODIFY=noon, so you can run the **GLUE** compressor/saturator alone, or park one side silent. (Both videos stress it; #1 "is it broken?" trap.)
2. **Hidden options live under hold-both-footswitches:** ALT (mode's headline param), EQ (turn that channel's MODIFY — CW thins lows, CCW darkens highs), SPILL, GLUE, SPREAD-routing, plus global DRY KILL / WET VOLUME.
3. **WET VOLUME unity = MIX at noon.** To trim wet level: hold RIGHT footswitch, turn MIX; noon is ~unity for all modes (official manual phrasing). Use this if a wet mode jumps in volume.
4. **L SWAP / R SWAP = run any two engines together, including two of the same.** Dual tape delay, dual reverb, synth→GenLite, etc. This is the move that unlocks the "build-your-own-reverb / build-your-own-shimmer" recipes.
5. **Tap tempo with per-engine subdivisions:** double-tap BOTH footswitches to enter tap mode; hold one side + turn its TIME to set that engine's own subdivision; tap right to exit; side LEDs keep flashing while following tempo.
6. **GLUE is the cohesion glue for multi-effect stacks** — Johnston: stacked modulation/effects "always have something missing — compression"; a touch of GLUE makes disparate engines read as one effect. Also usable as a standalone comp.

## HIDDEN / non-obvious BEHAVIORS
- **Delays are tempo-stepped by default** (Tape Echo, Grain Tumbler, Slow-verb, Useful Ambience, Pitch Repeater, Orchestra Swell). TIME snaps to musical subdivisions "like a MOOD's clock." **UNSYNC dip OFF by default.** Turn UNSYNC ON for continuous TIME + smooth pitch-sweeps of the buffer.
- **MIDI clock overrides the UNSYNC dip.** With clock present at the MIDI in, modes sync regardless of the dip. (Critical for this rig — Digitakt 2 is clock master; cross-ref `Gear/Chase Bliss Blooper/research/links/cb-stack-clock-sync-per-pedal.md`. NOT re-deriving the MIDI deep-dive here.)
- **Tape Echo does NOT self-oscillate** at max feedback — it loops the last sound forever instead. And all delay/echo buffers **dump-and-refill** if they hear a loud-enough, long-enough new sound (feature for "latch a new chord," surprise for sustained drones).
- **Grain Tumbler + LATCH dip + hold = frozen, *repeatable* grain pattern** (buffer frozen AND grain calc stopped → same jumps every pass) vs. its normal random scatter. Strong move for a locked evolving texture into the Microcosm.
- **Ensemble (6A) hold = sine LFO becomes a smooth RANDOM waveform** — non-cyclical chorus movement (this is the per-mode "RANDOM" the rig wants).
- **Spectral Modulator (3B)** = synthy resonant filter, not a normal modulation — lo-fi low-pass → "laser-gun tremolo" → glacial wide filter sweeps.
- **Pinging Phaser (3A): changing pole count *while playing* throws happy-accident artifacts** ("not intentional but very cool").

## COMMON PITFALLS / GOTCHAS
- **Gen Lite (6B) gotcha #1:** for a real tape sound you MUST go **full wet** — any dry blend makes dry chorus against wet (random-chorus artifact, not tape).
- **Gen Lite gotcha #2:** with **SPREAD on, flutter is computed per-side**, so even full-wet the two sides chorus against each other → wide pseudo-random chorus, NOT realistic tape. (Differs from the standalone Generation Loss pedal.) Turn SPREAD off for believable mono-ish tape; leave it on if you want the wide chorus.
- **Impulse Synth (5A) is register- and onset-dependent:** higher chords get less synth (play down an octave for fuller tracking); roll/arpeggiate and it voices only the *last* note struck — **strike block chords together** for chordal pads. Not for fast leads ("it will not keep up with you").
- **ALT attack/release trade-off on 5A:** long attack ⇒ short release and vice versa — you can't have both long.
- **Sympathetic Resonator (5B): documented beta-vs-shipping discrepancy.** Pre-release demos show MODIFY making a square-wave/upper-harmonic synth; shipping units (and the manual) have **MODIFY = feedback amount.** ⚠️ If a demo shows the "square-wave resonator," that's likely beta behavior, not what ships. TIME (onset) and ALT (octave) on 5B are very subtle — octave only audibly does something when swept *during* resonance.
- **Many stereo jacks are dual-mono TRS** — may need TRS→dual-TS cables (manual). Same TRS-MIDI caveat as other CB pedals (5-pin needs a MIDIBox).
- **High current draw (~200 mA)** — give it a dedicated high-current isolated supply outlet.

## FIRMWARE LORE (honest / largely UNVERIFIED)
- It shipped Sept 2025; demoers explicitly ran **beta firmware** with an unfinished **synth engine** (tracking expected to improve in shipping units) and at least one **changed Sympathetic Resonator behavior** between beta and release (above). So: **distrust pre-release synth/resonator demos vs. a shipping unit.**
- Search engines repeatedly surface a "**Lost + Found firmware 1.0.0 / 1.1.0**" claim, but every direct fetch of the chasebliss.eu manuals page attributes those version numbers to **Generation Loss MKII**, not Lost + Found. **Flag: the existence of an L+F 1.1.0 update is UNVERIFIED** — I could not confirm a Lost + Found changelog. Updates would come via the **Bliss Programmer** (firmware.chasebliss.com) / CB firmware interface; check there for the actual current version before assuming.
- No user hardware mods (sealed digital platform); "modding" = dips, hidden options, firmware.

## Forum threads to read directly (auto-fetch blocked)
- TheGearPage megathread: https://www.thegearpage.net/board/index.php?threads/chase-bliss-lost-found.2684103/ (402/paywall proxy)
- The Gear Forum: https://thegearforum.com/threads/chase-bliss-lost-found.9471/ (403)
- TalkBass (bass/sub-octave angle): https://www.talkbass.com/threads/chase-bliss-lost-found-im-in.1675322/
- MOD WIGGLER (modular angle): https://www.modwiggler.com/forum/viewtopic.php?t=298348
