https://www.elektronauts.com/t/seamless-live-looping-ambient/132931
elektronauts.com (+ ambient-transitions thread #19122, + Cuckoo loopbox tutorial) · community · 2016–2021

# Ambient / drone live-looping on the OT — concrete techniques (the rig's closest aesthetic match)

This rig is drone/doom/shoegaze, so the OT's ambient-looping practice is the most on-target body of technique. These are real community settings, not lore.

## Holding material indefinitely (continuous play)
- **Turn OFF "silence on pattern start"** so trigs sound INTO the next pattern until the next trig comes — set via `[FUNC]+[BANK]` → **CHAIN BEHAVIOUR / CHAIN AFTER** per pattern. This is what lets a drone sustain across pattern changes instead of retriggering.
- **Different track lengths per track** (polymetric) + sparse trigs at slow tempo (**30–60 BPM**) = generative, ever-evolving bed with no abrupt transitions.
- **15-minute sample chains** of individual sounds each **10–90 s long**, played at low tempo, sliced playback modulated live.
- Pre-render **seamless loops externally** (e.g. 32-bar ambient beds) and import as backing — match sample levels in the DAW first to avoid level-jump clicks.

## Avoiding clicks at the loop point (important OT caveat)
- **Fin/Fout do NOT crossfade a captured Pickup loop** — the loop file's in/out don't overlap, so pure sine/low-harmonic drones click at the seam. The more harmonically dense the source (fuzz walls, banjo — good for this rig), the less audible the click.
- Apply **amp envelopes (long ATTACK)** and use the sample's inherent envelope so soundscape switches fade rather than snap.
- **Pickup silent-loop trick**: record a first loop pass with **gain all the way down** (a silent loop establishes the length cleanly), then after the loop point bring gain up and start overdubbing — gives a clean loop boundary.

## FX routing for ambient
- The OT's **per-track FX get cut off when Parts change** — for long-evolving reverb tails, route to an **external reverb/delay via the mixer/cue sends** (Eventide/Strymon mentioned by users) so tails survive Part switches. In this rig: send to the H90 / Big Sky / TimeLine off the cue bus so reverb doesn't gate when you change Parts.

## Pickup-machine loopbox (Cuckoo method)
- Pickup machines = the OT's built-in **looper-pedal** tracks (record/overdub/play states), "way more immediate and spontaneous" than recorder-trig + Flex. Good for **looping guitar/pedalboard input live**; manual SEND knob to a delay, with `[FUNC]` shortcuts for delay-time subdivisions. (Full steps in Cuckoo's video — elektronauts.com/t/octatrack-loopbox-pickup-machine-cuckoo-tutorial/17807.)

## Rig application
Pickup-machine the pedalboard's stereo print directly (loop the live drone), set polymetric track lengths + slow tempo for generative drift, and route reverb externally to the H90 so tails don't cut. This is the "Ambient Drone Bed" workflow (dossier §13d) with the click-avoidance details filled in.

Sources: elektronauts.com/t/seamless-live-looping-ambient/132931, elektronauts.com/t/octatrack-ambient-transitions/19122, elektronauts.com/t/octatrack-loopbox-pickup-machine-cuckoo-tutorial/17807
