https://www.youtube.com/watch?v=jxWh3LG-MY8
Leon Todd · Try This Routing Trick | Eventide H90 Tips & Tricks · 2023-03-08 · 7:07

A genuinely useful workflow trick that exploits the H90's dual-algorithm structure to build custom "super-algorithms" that don't exist as a single preset. Cleaned to prose.

## The problem with plain series routing
Default pedalboard-style routing (e.g. Chorus → Reverb in series) feeds your DRY signal through both effects, so the dry tone gets modulated/colored, not just the wet tail.

## The trick: 100%-wet Preset A into Preset B, then blend with PROGRAM MIX
1. Route the two presets in **series** (A → B).
2. Set Preset A's **Mix to 100%** (fully wet) — so the only thing entering Preset B is the wet signal of A. (Equivalently, set the FIRST effect to 100% wet.)
3. Build your combined wet effect across A → B (e.g. a Reverb at 100% mix running INTO a Chorus, so only the reverb tail is chorused, not your dry guitar).
4. Use the **Program-level Mix** to blend that wet "super-block" against your fully dry signal.

Result: your dry signal stays totally dry (no wobble/color), and the A+B combination behaves like one custom algorithm running in parallel with your dry tone. He calls it creating "super algorithms that aren't available otherwise."

## Examples demonstrated
- **Chorused reverb** — SP2016 Reverb at 100% mix into a Chorus; Program Mix blends the chorused reverb tail under a clean dry signal. Only the reverb tail wobbles; the dry note doesn't.
- **Panning delay** — Vintage Delay wet mix 100% into a "pulsing trim" (tremolo/panner); Program Mix ~50%. The wet delay pans around the stereo field while the dry signal does NOT pan (which is what you want from a panning delay). Make sure Kill Dry is OFF for this. (He offered the patch as a free download.)
- Other suggested combos: Reverb → Tremolo; Reverb → Pitch detune; Compressor ↔ Reverb (either order); any block → EQ to EQ only the wet signal; Crystals → a Distortion algorithm while leaving the dry sound completely clean.

Rig note: this is the core technique for the End-board role. Run Blackhole/Shimmer/Wormhole at 100% mix into MangledVerb or a modulation/distortion algorithm, then use Program Mix to sit the wet wall under the dry baritone/banjo — get a degraded, modulated reverb tail without muddying the fundamental. Pairs perfectly with feeding the result to the downstream tape stage.
