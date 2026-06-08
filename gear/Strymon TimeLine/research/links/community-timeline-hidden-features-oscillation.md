https://www.strymon.net/product/timeline/  +  https://forum.morningstar.io/t/bigsky-infinite-hold-timeline-oscillation-runaway-repeats/10875  +  https://www.strymon.net/this-weeks-preset-timeline-hell-float-trip/
strymon.net (product page + preset blog) + Morningstar forum · multi-source

Hidden features / secondary tricks the community leans on, plus the self-oscillation/freeze mechanism.

## Infinite repeats / freeze / runaway (the headline trick)
- **Hold the active preset footswitch (A or B) → INFINITE REPEATS**, regardless of where the REPEATS knob is set. Release → snaps back to the saved REPEATS value. (Source: Strymon product page — "hold the current preset footswitch … Timeline will go into infinite repeats, no matter what setting repeats are at.")
- This is the **freeze / sound-on-sound** move: hold to lock a wash, play over the held bed, release to let it decay. Great for drone walls.
- **Runaway self-oscillation** (the screaming, building feedback) is reached by cranking **REPEATS past ~3 o'clock toward max** so feedback regenerates >100% — most musical on **dTape, dBucket, Digital**. Combine with riding an **expression pedal mapped to REPEATS** (EXP CC 100) to swell INTO oscillation and back out. The infinite-hold is a clean freeze; pushing REPEATS high is the chaotic, pitch-bending runaway.
- For a MIDI controller, mimic the footswitch with **Press-down on press / Press-up on release** (momentary) or a **Toggle** (latched) action — there is no confirmed dedicated "infinite" CC (see midi-cc-map file).

## Per-machine secondary params worth knowing
- **High Pass PARAM (off → 900Hz):** on Digital (and via filter on others) — the fix for boomy/ice-pick repeats (banjo, baritone). Not on the front panel; lives in PARAMS.
- **Smear** (Digital, Ice, Pattern 16): softens repeat attack. On the **Ice "Hell Float Trip"** preset, Smear is **maxed to soften the attack** of the pitched repeats. Quirk: with Ice **BLEND set all-the-way to ICE, the SPEED & DEPTH knobs do nothing** — they only modulate the dry delay lines, which you're not hearing.
- **Pattern 16** with Smear maxed = a fake early-reflection "reverb" — reverb-adjacent ambience with no reverb engine (useful for the benched-failover case).
- **Boost ±3dB** per preset (PARAMS) — level-match presets or push the next pedal.
- **Tap Division** per preset (incl. dotted-eighth, triplet) — the rhythmic-delay backbone.
- **EP SET:** map the expression pedal to MULTIPLE knobs at once with independent heel/toe ranges per knob — a morph control (e.g. sweep TIME + REPEATS + FILTER together into a dive).
- **Persist / SPLOVR:** trails across presets (see gotchas file).

## Feedback-loop insert (rear switch)
- The rear panel switch turns RIGHT IN/OUT into a **send/return INSIDE the delay feedback path**. Patch a fuzz, filter, or another pedal there and every repeat gets re-processed and compounds — the classic "fuzz-in-the-feedback-loop" runaway/grit trick. (Trade-off: you lose stereo while it's in FEEDBACK LOOP mode.)

## HONESTY / firmware flags
- Infinite-hold + the deep params are all stock; nothing here needs a mod (closed digital platform — no 18V, no clipping swaps).
- "Golden Ratio tap division" is **DIG-exclusive, NOT on the TimeLine** — see the gotchas file. Don't expect it here.
