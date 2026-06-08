https://www.youtube.com/watch?v=51vhEOrD6es
BachelorMachinesTV · (Part Two) Lost + Found: Let's Do Some Science with Chase Bliss's Audio Chemistry Set · 2025-11-10 (59:51)

[Auto-captions, cleaned to prose and de-duplicated. Part Two of the deepest technical teardown available. Covers categories 4-6 (Delay, Synth, Bend), the UNSYNC dip, the LATCH/HOLD behavior, a firmware discrepancy on Sympathetic Resonator, and the routing/mixer section (BLEND + SPILL). [Music] markers denote demo passages; spoken parameter detail preserved.]

Welcome back to part two. Part one covered the first six algorithms (left side by default); 7-12 are on the right side by default. Same interface: three categories per side via the toggle, choose the two effects in a category with MODIFY (left of noon = first algorithm, right of noon = second).

## Category 4 — DELAY: Tape Echo (L) / Grain Tumbler (R)
**Tape Echo** — a take on the overall tape-echo concept (not a full RE-201 clone; no spring reverb, no multiple play heads). Controls:
- **TIME = delay time** (emulated record-to-playback-head distance).
- **MODIFY = intensity / feedback** — number of repeats from one to infinite. Note: unlike a Space Echo it does NOT self-oscillate when pushed; it just plays back the last sound forever. Like the other delays, if it hears a new sound loud and long enough, it ditches its buffer and refills (easy to hear: TIME all the way down, MODIFY all the way up, play chords back to back).
- **ALT = "stability"** (he argues it should be called *in*stability — more stable at minimum, less at maximum). Controls the virtual tape's "age": turning it up (1) loses high-frequency capture ability (acts like a high-pass filter — and because it's inside the delay loop, infinite loops eventually filter away), and (2) introduces "warble" (tape moving through unreliable hardware, like Generation Loss's wow or the Valhalla delay plugin's wow). Confirmed via spectrum: high frequencies above ~5kHz are attenuated, hard stop at ~16kHz, slight low-end reduction with a midrange bump even before adding age.

**IMPORTANT — the TIME knob is stepped/musical by default (applies to ALL L+F delays):** "By default the time control is not a continuously variable control. It moves in musically useful increments — like the intervals on a Theremin pedal or the clock intervals on a MOOD. This is true of all the delays: Slow-verb, Useful Ambience, Pitch Repeater and Orchestral Swell too." If you want continuous time instead, **the UNSYNC dip switch** (OFF by default, so sync is ON by default) lets you get between subdivisions and do continuous pitch sweeps of the delay buffer. **Critically: if Lost & Found is receiving MIDI clock through its MIDI input, that OVERRIDES the UNSYNC dip — it will sync to MIDI clock whether UNSYNC is on or not.** (Direct relevance to a Digitakt-clocked rig: clock presence forces synced behavior regardless of the dip.)
SPREAD on Tape Echo splits the mono echo's time into a left and right echo (effectively doubling tempo and panning L/R). The warble is calculated in stereo (independent per side), so it's not a copy on both sides. Demos: syncs to clock and steps cleanly 16th → 8th → quarter; the sound it makes when switching subdivisions is itself a cool artifact. Without clock the un-synced echo is very short (slap-back territory) on a clean guitar.

**Grain Tumbler** — seems based on the "Time Scramble" algorithm of the Eventide SP2016 (1982, arguably the first commercial granular effect). Mental model: like Tape Echo but the playback head jumps to random positions in a digital circular buffer. Controls:
- **TIME governs THREE things at once: the length of the loop, the rate at which the playhead bounces, and the number of playheads.** TIME all the way down = a single playhead bouncing a lot, often not touching the loop. Toward noon = jumps less often, plays longer moments. East of noon = longer loop + MORE playheads (multiple grains at once).
- **MODIFY = the likelihood that a played-back grain routes past the erase head back into the loop.** Just past noon = ~0% chance (grains don't accumulate); all the way up = 100% (the loop builds up with all grains — clears if you turn MODIFY all the way down, captures again when raised).
- **ALT = fade-in/fade-out per grain.** ALT down = playhead clicks on/off instantly (glitchy); ALT up = grains fade gradually (smoother, ambient).
**LATCH dip + HOLD:** with the LATCH dip on, holding the footswitch freezes the circular buffer in place AND stops recalculating grains — so the playhead jumps the same way every pass (a repeatable pattern); grain size still governed by TIME. SPREAD adds separate playheads per side (same idea, offset). Demos on drum loops and clean guitar show the buffer is short (erase head clears old chords); MODIFY up lets chords pile up and "fight."

## Category 5 — SYNTH: Impulse Synthesizer (L) / Sympathetic Resonator (R)
**Impulse Synthesizer** — a guitar synth seemingly based on pedals like the Boss SY-1 (its string settings sound similar). Detects input pitch and generates a synth voice; polyphonic with limits. The "stringiness" comes from a phasy PWM character plus multiple oscillators, at least one widely detuned (synth-string detune). Controls:
- **MODIFY = brightness of the string sound** (brighter farther from noon; "fizzier," more high end).
- **TIME = portamento / glide time** to a newly detected pitch.
- **ALT = attack AND release time.** Note the trade-off he found: a LONG attack gives a SHORT release and vice versa. Also: the synth only triggers while a note is sustained — if the input goes away before the attack completes, the attack won't happen.
Behavior notes: it cares about register — higher chords get less synth than lower chords (play down an octave for full synth on all chords). The manual recommends playing block chords all at once; rolled chords make it play "the last impulsive thing it heard" (it listens for the beginnings of sounds — hence "impulse"). It will even try to pitch-track DRUMS (weird but a fun background texture).

**Sympathetic Resonator** — manual: a polyphonic pitch-tracking resonator made of chromatically tuned pipes. **FIRMWARE DISCREPANCY (flag):** the presenter's unit does NOT behave like the Chase Bliss demos or other YouTube reviews. The pre-release video shows MODIFY adding upper harmonics / turning the resonator into a square-wave synth, but on his unit (and per the manual) **MODIFY controls feedback amount.** His hypothesis: a last-minute change during beta testing, and the manual-matching behavior (feedback) is the intended/shipping one. (Honest unverified — he asks viewers for evidence.) Controls on his (shipping) unit:
- **MODIFY = feedback amount** — near noon it resonates only for a moment; maxed = resonates forever.
- **TIME = onset time of the resonators** (per manual) — VERY subtle; he could barely find an audible difference (seemed like milliseconds, e.g. slight change on a drum clap/kick). He honestly can't fully explain this knob.
- **ALT = octave of the resonators** — also subtle; makes no difference if you don't change it WHILE resonating, but sweeping the octave during a held resonance does something cool.
Character: glassy reverb / vibraphone-like sustained tone that follows your playing (less dissonant/wild than Impulse Synth). Tracks the synced guitar well.

## Category 6 — BEND: Ensemble Expander (L) / Gen Lite (R)
**Ensemble Expander** — tribute to early rack choruses (Roland Dimension D, Dytronics CS-5). A chorus that scales from a plain chorus into an ensemble. Controls:
- **ALT = number of voices, 2 up to 8.** At 2 voices it's a chorus; more voices = ensemble.
- **TIME = LFO speed.**
- **MODIFY = modulation depth.** Note: modulation depth is divided as voices increase — DEEPER mod at few voices, SHALLOWER at many voices. (Depth and speed are interrelated: raising speed pushes the comb-filter effect down into lower frequencies.)
Like the phaser, it sounds best when you crank ONE control with the others backed off. He reproduced a Roland Alpha Juno chorus closely with **TIME ~10:00, MODIFY ~8:00, ensemble (ALT) ~noon (≈4 voices)** — and notes L+F can also go beyond what a real Juno offers because you can vary rate and depth.

**Gen Lite** — a cut-down Generation Loss MKII tape sim. What it KEEPS: a combination of wow + flutter, plus "failure." What it OMITS (vs the full Gen Loss): no selectable EQ/tape-model profile, no noise/hiss, no saturator. Controls:
- **TIME = modulation SPEED** — minimum = full flutter (fast pitch/volume oscillation), maximum = more like wow (slow large-scale pitch drift). NOTE: unlike the full Gen Loss you must CHOOSE between flutter and wow with TIME (you can't have both at once).
- **MODIFY = modulation DEPTH** (how "broken" the machine is).
- **ALT = "failure" amount** — the TAPE itself being ruined (vs the machine): crinkles and snags (the cassette-caught-in-the-machine sound).
**Two usage notes:** (1) To sound like real tape emulation, go FULL WET — any dry blend makes the dry chorus against the wet (random chorus). (2) Different from the full Gen Loss: if SPREAD is on, flutter is calculated separately per stereo side, so even at full wet the two sides chorus against each other — a pseudo-random stereo chorus rather than realistic tape. (Crinkle/ALT all the way down + spread = just a big wide stereo chorus.)

## Mixer / routing section (the two middle knobs)
Walked through with Slow-verb (L) + Gen Lite (R), dirty guitar:
- **PARALLEL (spread/middle position):** both algorithms get the signal at the same time; the BLEND knob mixes between the two outputs (e.g. dry-degraded guitar on one side vs Slow-verb on the other).
- **SERIES (point toward one side):** whichever side the routing points to becomes a dry/wet for the second effect. Point left → fully dry/only-Slow-verb to start, mix in Gen Lite to the right so Gen Lite degrades the Slow-verb signal. Point right → Gen Lite first, then add Slow-verb after.
- **SPILL (the ALT for the top knob in series):** lets dry signal pass the FIRST algorithm into the SECOND, so the second effect acts on BOTH the dry signal AND the output of the first. Example: Gen Lite on the Slow-verb AND on some dry guitar simultaneously — engage SPILL via ALT to add dry Gen Lite alongside the series chain.

[End. He notes the 144 combinations are out of scope but the mixer spin-through shows how to combine elements.]
