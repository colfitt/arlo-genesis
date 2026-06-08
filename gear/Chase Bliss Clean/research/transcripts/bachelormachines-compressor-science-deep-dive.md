https://www.youtube.com/watch?v=cMQYERrLV2Y
BachelorMachinesTV · Let's Do Some Compressor Science with the Chase Bliss Clean pedal · 2025-09-11 (38:52)

# Compressor Science — BachelorMachinesTV (deepest workflow video)

The single most useful "how to actually use it" video found. After a compression-history primer (tube/variable-mu → optical → FET → VCA — Clean is a VCA compressor, like the dbx 160), the back half is concrete, demonstrated workflows in an Ableton test harness. Settings and recipes distilled below; history section condensed.

## Compression history (condensed)
Compression was invented to keep AM radio audio in a Goldilocks dynamic range. Lineage: variable-mu/tube (control voltage on a tube's control grid; "mu" = gain) → optical (control voltage drives a light next to a light-dependent resistor; slow characteristic response, great on vocals; the vactrol/cadmium issue) → FET (UREI 1176, the first FET comp, ~$3,000 new) → VCA. **Clean is a VCA compressor:** rather than relying on a component's physical characteristics to do gain reduction (which colors the sound), a VCA analyzes the loudness of the incoming signal and turns down an amplifier based on how loud it is. The most conceptually straightforward type. First commercial VCA comp was the dbx 160 (1976).

## How the controls actually behave (demonstrated)
- **Sensitivity is the inverse of a threshold.** All the way down = threshold all the way up = pedal won't react no matter how loud. As Sensitivity goes up, it reacts to quieter and quieter sounds.
- **If either Dynamics OR Sensitivity is all the way down, the first-stage compressor is doing nothing.** (The second-stage limiter can still be doing something.)
- **Dynamics zones:** ~9:00 = 2:1 (cuts signals above threshold in half); climb toward noon = infinity:1 (a limiter). At noon it's a **feedback** limiter; sweep toward 3:00 and it becomes a **feedforward** limiter (keys off the uncompressed signal, so it's faster and more aggressive). Past 3:00 = **Sag**: pushes the compressed signal all the way to the ground so you only hear the parts that weren't affected — loud sounds become silent, quiet sounds become loud.
- **The red LED tells you exactly when the compressor is acting.** Use it to design your settings — it flashes only at the moments compression is actually happening.
- **Attack does not turn on instantaneously.** Fastest is 0.5 ms. The attack starts when a transient exceeds the Sensitivity threshold, so by necessity it never compresses the very first instant across the threshold. Clean has **no look-ahead**, so at extreme settings you'll see/hear the beginnings of transients escaping — this is normal, not a flaw.
- **Release:** fast ≈ 50 ms, slow ≈ 1.5 s (good for whole-mix glue), middle = user-set by holding both footswitches and sweeping the Attack knob.

## Recipes / workflows
**Drums (the "right" way to beef them up — important).** Trying to use the first-stage compressor as a limiter to beef drums fails — its attack isn't fast enough, you get snappy transients on every note. Instead, **engage the second-stage limiter by pushing the DRY signal** — that gives you all the body. Then use the first-stage compressor purely as a *transient designer*: turn Dry all the way down, shape the transient you want with Sensitivity / Dynamics / Attack / Release, then mix Wet and Dry together for the best of both worlds. The second-stage limiter is a **clipping circuit** — driving it hard adds harmonics/overdrive (that's the sound; that's also the basis of Dusty).

**Sag as a transient/slapback designer (drums).** All the way into Sag, hearing only wet: increasing Attack lengthens the transient that escapes the compressor. A slow-attack/fast-release Sag setting boosts the drum transient AND adds a slapback-reverb-like return on the snare. Blend the dry back in for a huge, groovy drum sound.

**Sag on electric piano (turns one part into three instruments).** Attack fast-ish (not super fast), Dynamics in Sag, Sensitivity ~10:00, Release fast. The initial attacks turn into a transient-gate, long chords become a swelling pad, and quiet noodling that never crosses the threshold plays through untouched — one loop sounds like three instruments. Add delay for more.

**Swell (left footswitch).** Makes the signal silent until something crosses the Sensitivity threshold, then triggers a dedicated swell envelope. Presenter leaves **LATCH engaged** so the left footswitch is a regular toggle (finds momentary hard to work with). Set swell attack with Wet, swell release with Dry (hold both switches); **~noon for both = a nice swelling pad** (tempo-dependent).

**Physics.** Electrically models a bouncing spring to destabilize the amount of compression. Left = wobbling (push a spring sideways, let it wobble back); right = twitchy (stretch a spring and let it snap). Sounds great on drum loops and on long reverb tails (mimics a complex physical space — stadium/canyon where reverberations get broken up). Pairs naturally with surf guitar.

**EQ modes.**
- **Middle (Manual):** CCW attenuates highs, CW attenuates lows, noon = nothing. Because EQ only affects the *wet* signal, you can mix frequencies louder than others — e.g. add low end to a kick: cut all highs on the wet, blend it in, let the mixer + limiter do the work (no first-stage compression even needed).
- **Left (Shifty):** EQ shifts to full frequency when the signal crosses threshold, shifts back as the compressor disengages — a filter on an envelope follower governed by Attack/Release. Best use: an interactive harmonic swell.
- **Right (Modulated):** attaches the EQ to an LFO whose rate is set by Attack — a harmonic tremolo. Presenter calls this "low-key one of the best things about this pedal."
- **MOTION dip** (alternative): leave EQ on Manual and turn on MOTION to attach the LFO to the compression response (like Physics but as a chosen-frequency oscillation). Mix and match MOTION with Physics, EQ modes, Sag, and Dusty freely.

**Dusty.** Lowers the second-stage clipping threshold into distortion territory and turns Sensitivity into a threshold selector — a fuzzy overdrive with a distinctive sound. Go into Sag on Dynamics for a "looming" distortion. Dusty + Swell combine.

**Two-stage / headroom note.** Diagram: audio in → signal follower → control center → compressor → mix with dry → output limiter. You can add unlimited gain at the front and it won't exceed the output limiter's threshold — but that's not transparent (the limiter is a clipping circuit, so hard driving adds harmonics).

**Spread** (on all CB stereo pedals): adds stereo movement; sounds particularly nice on Swell and especially on the EQ/MOTION tremolos.

## The user journey (and the point of the pedal)
The pitch is "can clean guitar be as fun as overdriven guitar?" — the answer here is an unqualified yes. The typical Clean-user arc: start using it as a compressor → start playing with the other dynamic options → fall in love with Dusty → end up loving it as a tremolo pedal. The presenter says Clean made clean electric guitar his favorite instrument and changed what he plays (e.g. two-hand tapping, rewarded with a tremolo "as a treat").
