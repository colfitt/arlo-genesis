https://www.youtube.com/watch?v=FZ3E3a-N9K0
Gear Sounds · Boss VG-800 Full Tutorial In Depth, VG800 Tips & Tricks · 2025-10-06

(Auto-captions, cleaned to prose. This is a ~43-min livestream-format deep walkthrough. It is the most thorough hands-on navigation video found, but interleaved with off-topic livestream chatter and opinionated rants — trimmed here to the workflow content. Some of the presenter's "this doesn't work / can't do this" moments are user error or patch-specific, flagged inline.)

## Starting point: pick a patch you like first
The presenter's core method: do NOT build from scratch. Select a factory patch that already sits near the sound you want, then modify. The main "home" screen is your stage view — quick access to toggle things like alternate tuning on/off and swap instruments fast in a live setting. He demonstrates a patch in OPEN G alt tuning (guitar physically tuned down to match), layering the modeled instrument signal with the NORMAL (real magnetic pickup) signal. Turning ALT TUNING off returns to standard tuning; the NORMAL/guitar signal can be blended up or down independently of the model.

## The EFFECTS view = the signal chain / "pedalboard"
Press [EFFECTS] to see the whole chain as a row of blocks. Left-most is the INST block (the modeled instrument — e.g. the synthesized acoustic tone), then the NORMAL guitar tone, then the effects chain. Each block toggles on/off with the [SELECT] button. He calls it "basically a pedalboard" and gripes about the small monochrome screen (wishes it were color like the GX-10).

**Parallel vs series routing (DIV):** the chain visibly splits into two parallel paths. Running effects/preamps in parallel gives roughly 50% of each (a blend); stacking them in series combines/cascades the gain so preamps and amps build on each other. This is the DIV / two-amp-path architecture.

**Page navigation:** within a block, a dot-and-arrow indicator at the bottom shows extra pages; use the [◄][►] page buttons to move between them. Example block contents seen while paging: acoustic resonance, flanger, pitch shift, chorus.

## Swapping instruments fast (INST)
From the main screen you can swap the INST type on the fly. He cycles: acoustic → DUAL GUITAR → ELECTRIC BASS → VIO GUITAR → SYNTH. Tip he stresses repeatedly: **turn your guitar's physical volume knob down while auditioning models** so the real electric signal doesn't mask the modeled tone.

- **Electric bass** model: "pretty convincing," tracks single notes with no problem; gets "wacky" / less convincing high up the neck and on polyphonic playing, but far more real than a pitch-shifter or bass-sim. He credits the hex pickup: six separate string signals = ~6× easier processing, hence better tracking and tone. Monophonic (single-note) tracking is essentially flawless; polyphonic is "pretty good."
- **GR-300 synth:** noted as using different technology than the rest of the VG-800 (the same engine that lived in the SY-1000), and praised — "this voice is incredible."

## Instrument deep-edit (press [INST])
Pressing [INST] opens the instrument editor. The TYPE field changes the model; the tabs/menu options below change per instrument category. Examples:
- **Acoustic types** cycled: MA28 (Martin), TRP0, GB48, GLD, **Nylon** — he calls the nylon his favorite acoustic model, "the best acoustic guitar simulator in the world as of now."
- **Synth params:** VBR (vibrato) on/off; DUET switch (duplicates/thickens the voice — "sounds kind of cool"); SWEEP switch with SWEEP FALL / SWEEP RISE; MODE = VCO / VCO+VCF (V+D) / distortion — "these really change everything." Plus CUTOFF and RESONANCE (resonance at 0 = no filter character; raise for the classic resonant-synth squelch).
- **Strings/Other page:** per-string PAN (pan each of the six strings independently), per-string EQ switch.

## Dual-channel amp routing (the two parallel paths)
Inside the amp block, MODE = SINGLE or DUAL, with CHANNEL A and CHANNEL B selectable (the on-screen line highlights which path is active). SINGLE = one amp path; DUAL = both paths run in parallel and sum. He builds an A/B with panning — A panned left, B panned right — for a wide two-amp sound. Note: an **AB BALANCE** parameter sets the A↔B mix; it operates around a center (he finds it's centered at 50, not 100), which matters when trying to fully isolate one path.

**Important gotcha he discovered live:** his per-string and A/B PAN edits seemed not to work — because an **ACOUSTIC RESONANCE effect** active in the chain was collapsing the stereo image. Turning acoustic resonance OFF restored true stereo and his pan edits became audible. Lesson: stereo-collapsing blocks (acoustic resonance, etc.) downstream will mask panning done upstream.

## NORMAL MIX
On the INST edit pages: NORMAL MIX off/on plus LEVEL (he sees 100) and PHASE (normal). This is the blend of the real magnetic pickup under the model. Turning it on "separates it in a nicer way."

## Effects loop (SEND/RETURN)
There's a dedicated effects-loop block, MODE = NORMAL (send/return). It's a full stereo loop — you can patch an entire external pedalboard (or another unit) into it, placed wherever you put the block in the chain. He used it in a prior episode to run the VG-800 + an RT-2 in full stereo through the loop.

## KEY workflow finding: fixed-position effect blocks
The single biggest takeaway he arrives at: **most effect blocks are fixed in position and type — you cannot freely add blocks or reorder the time/space effects.** Specifically:
- Blocks labeled **FX (FX2, FX3, etc.)** = freely changeable effect type (he changes one to a phaser, another to a delay). These are the user-assignable slots.
- Blocks labeled **CHORUS, DELAY 1, DELAY 2, REVERB, the FX LOOP** = dedicated, forcibly placed in their correct architectural position, on/off only — type cannot be changed and they cannot be moved.
- Net: you get roughly **two assignable FX before the amp + one assignable FX after the amp**; everything else (chorus, two delays, reverb, loop) is locked to position. He's frustrated by this vs the GX-10's free drag-and-drop, but it's the actual architecture (matches the dossier's fixed signal chain). Starting from an INIT memory you're stuck with the locked layout.
- The dedicated effects loop is "not a true loop" in his view because there is no separate virtual cabinet block — there's a virtual amp but no movable cab, so you can't put time-based effects between amp and speaker the way a real FX loop allows.

## Other tips
- **Knob lock:** press the two relevant buttons together → "KNOB LOCK ON" (prevents accidental knob bumps on stage); press again to release.
- **Fine increments:** press/click the [SELECT] knob down (you feel a detent) and scroll while held to step values in increments of 10 — fast coarse adjustment.
- **MST / memory page:** has MEMORY LEVEL, a **GK SET** selector (you can assign different GK SETTING profiles per memory — "GK SET / SYSTEM SET 1"), and a **KEY** field used by any pitch-altering effect (harmonizer/pitch shifter) — set the song key here for in-key harmony.
- **SLOW GEAR** is available as an effect (volume-swell auto-swell). **SLICER** with selectable patterns.
- **Volume curve** (NORMAL / FAST) for an expression/volume pedal.

## Save / write flow
Hold the two write buttons together → choices: EXCHANGE, WRITE, INSERT (insert between existing patches), INITIALIZE. To name: click [SELECT] to insert a character, scroll to choose character (capital/small), move cursor, delete; press [SELECT] to execute the write. The patch saves into the chosen memory (overwriting an "INIT" slot).

## Honest opinion the presenter repeats
- Acoustic and synth modeling = the strengths, genuinely useful.
- Electric-guitar modeling = the weak point ("sounds bad / fake"; argues an EQ pedal beats the Strat-to-Les-Paul transformation). Amp/cab sims he rates poorly and the reverbs "ugly/digital."
- He "hated it at first" but values it for versatility, the acoustic/synth voices, and being bulletproof Boss hardware.
