---
type: chain
title: "Lost & Found Random-Event Texture, MOOD Capture"
date: 2026-06-15
artists: []
instrument: "guitar / synth"
gear:
  - Chase Bliss Lost & Found
  - Chase Bliss MOOD MkII
  - Novation 61SL MkIII
---

# Lost & Found Random-Event Texture, MOOD Capture ⭐

A constantly mutating texture that picks a new pair of weird effects every pass — never the same twice — then gets smeared and captured into coherent space. The Lost & Found is the spotlight: the 61SL fires **CC114 (Random Both Modes)** at it so both slots jump to a fresh on-aesthetic combination each trigger, while an armed **BOUNCE on MODIFY** keeps the chosen modes churning between jumps. The MOOD sits downstream as a granular catcher — its Reverb wet swallows whatever chaos the L&F throws and blooms it into a long, musical tail, so the result is unpredictable at the source but always lands in coherent space.

🟣 DOUG-designed integration. No artist played *this* chain — the per-unit patches carry their own provenance. This is "the Random use case" the rig is built around, with the Lost & Found in the spotlight.

## Signal path

guitar / synth → **CB Lost & Found — "Random Event (Live Mode-Shuffle)"** (`L+R` parallel, both slots loaded on-aesthetic; **CC114 Random Both** fired from the 61SL, **BOUNCE armed across L/R MODIFY**) → **CB MOOD MkII — "Chaos Catcher (Reverb-Stretch Capture)"** (Wet **Reverb**, Looper **Stretch/Env** to catch and bloom; LATCH freeze on cue) → amp / DAW, stereo.

The **Novation 61SL MkIII — "Per-Pedal CC Template"** is the brain: one encoder/button page mapped to the L&F's MIDI so CC114 is one button-press away, with the looper/freeze CCs of the MOOD on the same template for hands-free capture.

## Per-unit

- **CB Lost & Found — "Random Event (Live Mode-Shuffle)"** (reused) — ROUTING **`L+R` parallel**, both channels loaded with an on-aesthetic pair (e.g. Grain Tumbler + Spectral Modulator, or Gen Lite + Sympathetic Resonator), BLEND ~noon, MIX (RAMP) ~noon–1:00. The driver here is **CC114 = Random Both Modes** sent from the 61SL: each press jumps *both* slots to a new mode/variant combo — that's the "new pair of weird effects every pass, never the same twice." Between jumps, **arm BOUNCE across L MODIFY + R MODIFY** (Control-bank dips) so the current pair of modes is in constant hands-free motion rather than static; MIX (RAMP) sets the bounce speed. **6A Ensemble HOLD = RANDOM** adds smooth non-cyclical drift on top. SPREAD on for a wide field; GLUE ~10–11:00 tames the spikes when a harsh combo lands. Save a favourite combo to a preset so you can also recall a known-good scene on cue. *(The standard L&F MIDI CCs and BOUNCE/Glue character are sourced; specific BLEND/MIX/GLUE clock positions are a dialable recipe — dial by ear.)*
- **CB MOOD MkII — "Chaos Catcher (Reverb-Stretch Capture)"** (new) — Wet MODE **Reverb** (long/blooming) as the catch-and-smooth stage; Looper MODE **Stretch** (or **Env** for a more reactive, attack-carved capture) so the incoming random texture is granulated and time-smeared rather than passed through raw. CLOCK low for a grainier swallow. The job is to take an unpredictable, harsh-on-some-passes input and **tail it into coherent space**: the Reverb provides the musical landing, the looper provides the grain-smear that hides the seams between L&F mode jumps. **HOLD the LEFT (Wet) footswitch to FREEZE** the current bloom into an infinite bed when a great combo lands — capture the chaos and hold it — then let the L&F keep mutating quietly underneath, or kill the L&F and play over the frozen capture. **LATCH on** so the freeze holds hands-free; **TRAILS on** so toggling mid-performance doesn't drop the wash. *(MOOD publishes character, not numbers — clock-face positions are a dialable recipe.)*
- **Novation 61SL MkIII — "Per-Pedal CC Template"** (reused) — one template page driving the L&F over MIDI: a button mapped to **CC114 (Random Both)** for the one-press re-roll (momentary, any value triggers), encoders on the L&F's knob CCs if you want fader control of BLEND/MIX, and a dip-bank button to arm/disarm BOUNCE remotely. Put the MOOD's freeze/looper CCs on the same page (per the deep-CC template) so one controller fires the L&F re-roll and the MOOD capture without bending down.

## Routing

Mono or stereo in → **Lost & Found** (`L+R` parallel keeps both random slots audible at once) → **MOOD** wet-Reverb capture → out, stereo. The L&F runs **first** on purpose: it is the chaos *generator* (spotlight), and the MOOD is the *resolver* that catches and tails it. Keep the L&F **GLUE** working (~10–11:00) so when CC114 lands on a hot/harsh combo the level spikes don't slam the MOOD's input — the Glue is the safety valve that lets you re-roll freely without riding a volume knob. **Watch the MOOD freeze timing:** freeze right *after* a re-roll settles, not during the jump, or you'll capture a transient artifact instead of the texture. The L&F's SPREAD width is preserved into the MOOD (both stereo), so the random texture keeps its width into the bloom — if you want a tighter capture, narrow at the L&F rather than the MOOD. Clock-syncing the L&F BOUNCE LFO is *not* useful (fastest MIDI sync ≈ once/beat); leave BOUNCE free-running and let CC114 be the rhythmic event.

## Sound

A texture that is never the same twice at the source — every CC114 press reaches into the L&F and pulls a different pair of weird effects, churning between jumps via BOUNCE — but always resolves into a coherent, blooming reverb space because the MOOD catches and smears whatever arrives. Unpredictable input, musical output. Freeze a great pass and it becomes an infinite bed you can solo over while the next chaos brews underneath.

**Taste-ref:** generative / aleatoric ambient à la Brian Eno's *Music for Airports* tape-loop indeterminacy and Hainbach's "let the machine pick" texture jams — controlled chaos that lands in a usable bed, not noise.

## Play

Set the L&F to `L+R` with an on-aesthetic pair loaded and BOUNCE armed, then just play and **press CC114 on the 61SL** whenever you want a new pair of effects — each press re-rolls both slots, so you conduct the mutation rate by how often you trigger. When a combination lands that you love, **HOLD the MOOD's LEFT footswitch to freeze** the bloom into an infinite bed (LATCH holds it hands-free), then either let the L&F keep quietly mutating under the frozen capture or stop triggering and play a line over the held space. To end, kill the L&F and let the MOOD Reverb tail decay, or do one last CC114 re-roll into a final freeze. Save the current L&F combo as a preset before a re-roll if you want to be able to get back to it.

## Sources

- Basis: designed integration; chains **L&F "Random Event (Live Mode-Shuffle)"** (reused) → **MOOD "Chaos Catcher (Reverb-Stretch Capture)"** (new), driven by **61SL "Per-Pedal CC Template"** (reused). The Random use case — CC114 Random Both, `L+R` parallel, BOUNCE on L/R MODIFY for hands-free churn, Ensemble HOLD = RANDOM, GLUE as safety valve — is documented in `Patches/Chase Bliss Lost & Found/random-event-live-mode-shuffle.md` (Bay Mud "Randomizing Effects with MIDI"; CC112/113/114 from the L&F MIDI manual) and the BOUNCE/MIX-RAMP behavior in `stereo-pinging-phaser-bounce-sweep.md`.
- MOOD capture-and-tail (Reverb wet + Stretch/Env looper, LATCH/TRAILS freeze, low CLOCK = grainier) from `Patches/Chase Bliss MOOD MkII/freeze-pad.md`, `stretching-101-frozen-grain-wall.md`, `reverb-env-dynamic-interactive.md`, and the MOOD MkII manual.
- 61SL deep-CC driving (CC114 button, knob CCs, dip-bank arm, MOOD looper/freeze CCs on one page) from `Patches/Novation 61SL MkIII/per-pedal-cc-template.md`.
- Taste-ref: Brian Eno, *Music for Airports* (tape-loop indeterminacy); Hainbach (machine-picks texture jams).
