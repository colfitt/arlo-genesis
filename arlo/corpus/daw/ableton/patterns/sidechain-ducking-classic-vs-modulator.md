# Sidechain Ducking in Live — Classic Compressor vs Envelope Follower Modulator

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** [Ableton Live 12 Reference Manual — Compressor and Envelope Follower](https://www.ableton.com/en/manual/live-audio-effect-reference/); [Ableton Blog — Sidechain Compression: Part 2](https://www.ableton.com/en/blog/sidechain-compression-part-2-common-and-uncommon-uses/); Mike Senior, *Mixing Secrets for the Small Studio*; Sound on Sound — Pushing The Envelope
**Tags:** `daw-ableton`, `live-12`, `production-pattern`, `sidechain`, `envelope-follower`, `mixing`, `recipe`

---

## Two tools, one job, very different reach

Sidechain ducking — using one track's signal to attenuate another — has two idiomatic implementations in Live 12. The **classic Compressor sidechain** is the decade-old, dance-music staple where a kick triggers gain reduction on a bass or pad track. The **Envelope Follower modulator** (Live 12+) is a separate device that converts any audio signal into a continuous modulation curve and then drives *any mapped parameter on the same track* — Volume, a filter cutoff, a Send level, a reverb wet knob, the depth of an LFO modulating something else. The Compressor handles the case where the goal is "duck the level when the kick hits"; the Envelope Follower handles every other case (and also handles the duck-the-level case, just less concisely). They are not competitors — they are different tools with overlapping range.

## The classic Compressor sidechain — signal flow

The canonical kick-to-bass duck in Live 12: drop the [Compressor](https://www.ableton.com/en/manual/live-audio-effect-reference/) on the bass track. Open the device, click the small triangle at the top-left of the Compressor to reveal the Sidechain panel, enable the Sidechain toggle, and from the "Audio From" dropdown pick the kick track. The dropdown below that — "Pre FX / Post FX / Post Mixer" — controls the tap point. **Pre FX** is safest for sidechain duty because it ignores any kick-track plugins that might colour the trigger signal. The compressor then reacts to the kick instead of the bass: every kick hit ducks the bass, every silence releases it back up. This is the "pump" — the audible breathing that defines most house and EDM mixing.

## Classic-sidechain settings by genre

For a tight, audible pump (deep house, tech house, future bass), the [Production Music Live "easy way"](https://www.productionmusiclive.com/blogs/news/how-to-sidechain-in-ableton) and [Sonic Academy](https://www.sonicacademy.com/blog/how-to-sidechain-in-ableton-live-step-by-step-guide) recipes converge: ratio 4:1 to 8:1, threshold pulled to 8–12 dB of gain reduction, attack at 0 ms or 1 ms lookahead (Compressor in Peak mode), release timed by ear so the bass recovers fully just before the next kick — often 100–250 ms at 124 BPM. For subtle pop ducking on a music bed under vocals, ratios drop to 2:1 with much slower attack (10–20 ms) and longer release (300–500 ms). For rock bass ducking, the goal is rarely pumping — set ratio 2:1, attack 5 ms, release 80 ms, threshold for 1–3 dB of gain reduction, just enough to give the kick some space.

## The Sidechain EQ filter

A critical and frequently-skipped step: in the Compressor's Sidechain panel, enable the EQ filter (the small EQ button) and set it to bandpass around 60–100 Hz. This makes the compressor react only to the kick's fundamental — not to a snare bleed or a clap on the same trigger bus. The [Ableton manual](https://www.ableton.com/en/manual/live-audio-effect-reference/) describes the filter shapes as low-shelf, peak, high-shelf, low-pass, band-pass, and high-pass; for kick triggering, band-pass at 60 Hz with moderate Q is the conventional starting point. The benefit is that you can sidechain off a full drum bus rather than a kick-isolated track and still get clean ducking. This is one of the biggest deltas between "sidechain works" and "sidechain sounds professional."

## The Envelope Follower — what it actually is

The [Envelope Follower](https://www.ableton.com/en/manual/live-audio-effect-reference/) (Live 12+) is a Modulator — a separate device class that does not process audio. It analyzes an audio source's amplitude and emits a continuous modulation curve. Drop it on a track, open its Audio Routing panel, enable Sidechain, and pick the trigger source (e.g., the kick). The device exposes Gain (boosts the input before analysis), Rise (smooths the attack of the envelope), Fall (smooths the release), and Min/Max sliders to scale the modulation range. Then click the Map button at the top of the device and click any parameter on the track to assign it as a modulation target. The modulator now drives that parameter following the kick's amplitude. Up to eight parameters per Envelope Follower. The Modulation/Remote toggle changes whether the mapped parameter remains user-adjustable after mapping (Modulation) or is overwritten (Remote).

## When the Envelope Follower beats the classic sidechain

Three cases. **First: ducking parameters that are not Volume.** A filter cutoff that closes on every kick, a reverb wet knob that ducks under the kick, a delay feedback that pulls down on transient sources — the Compressor cannot do this; the Envelope Follower does it as one parameter map. **Second: per-track Send-level ducking.** Map the Envelope Follower to a Send knob and the kick now duck-modulates how much of the track hits a Return — for example, ducking a reverb return's input only when the lead is loud, leaving the reverb tail audible between phrases. [Ableton's blog](https://www.ableton.com/en/blog/sidechain-compression-part-2-common-and-uncommon-uses/) calls this approach an "ecosystem" of interacting sidechains. **Third: bipolar modulation** — the Envelope Follower in Bipolar mode swings around the base value in both directions, which lets you create boosts on top of ducks, or vice versa.

## When the classic Compressor sidechain is still the right choice

Three counter-cases. **First: when you want compression at the same time as ducking.** A Compressor sidechain doesn't only duck — it adds glue and density to the ducked sound. The Envelope Follower mapped to Volume just turns the level up and down; there is no nonlinear gain reduction adding character. **Second: when you want CPU-efficient ducking on many tracks at once.** A track with one Compressor sidechain costs less than a track with a Compressor *and* a separate Envelope Follower-to-Volume map. **Third: when you want the classic "pump" sound that defines whole genres.** That sound *is* the sound of a Compressor reacting to a sidechain trigger, with its specific knee and detection behaviour. Replacing it with a clean amplitude follower changes the character even if the level dip is mathematically identical.

## The hybrid pattern — Compressor for level, Envelope Follower for everything else

The most flexible Live 12 sidechain architecture combines both. Put a Compressor sidechain on the bass track for the level pump (the timeless dance-music move). Then put an Envelope Follower on the *same* bass track, sidechained from the same kick, mapped to the bass filter cutoff at moderate depth. Now every kick pulls the bass's level down (Compressor) *and* opens its filter slightly (Envelope Follower in Bipolar mode), so the bass returns brighter rather than just louder — a subtle "wow" that flatters the recovery. This is the kind of move the Compressor alone could not produce, and it is one of the major reasons Modulators was the headline workflow change in Live 12.

## Setting Rise and Fall on the Envelope Follower

Rise and Fall are the Envelope Follower's analogues of attack and release, but they work on the *envelope curve*, not the source signal. Short Rise means the curve responds instantly to transients; long Rise smooths the envelope so only sustained loudness moves the modulation. Short Fall means the modulation snaps back; long Fall means it lingers. For kick-driven ducking the conventional starting point is Rise 0 ms (catch every transient), Fall 100–200 ms (long enough that the envelope makes it to the next kick at ~120 BPM). For vocal-driven ducking (e.g., duck a music bed when the vocal is loud), Rise 30–50 ms and Fall 200–500 ms feel natural — slow enough to ride syllable-level dynamics rather than every consonant.

## Sidechaining from a Group Track or Return

A useful Live-specific pattern: route all kicks to a Group Track or a "trigger Return," then sidechain from that group. Now you have one consistent trigger source for every sidechain in the project, and changing the kick (Drum Rack swap, sample replacement) automatically updates every ducked track. [Ableton's sidechain blog](https://www.ableton.com/en/blog/sidechain-compression-part-2-common-and-uncommon-uses/) calls this "drum kit sourcing." Important Live gotcha: a Return Track itself cannot be a sidechain destination's source if the destination's "Audio From" cannot see it; for that, route the kick to a dedicated Group track instead.

## The "ghost kick" trigger trick

A timeless production move that pre-dates the Envelope Follower by a decade: sidechain off a kick that is *muted in the mix*. Create a "Ghost Kick" MIDI track with a four-on-the-floor kick pattern, mute it from the main output via routing (or set its output to "Sends Only"), then point every sidechain's Audio From at that ghost kick. Now you get perfect rhythmic ducking even on parts of the song where the real kick is silent (breakdowns, intros), without the ghost kick being audible. This works identically with both Compressor sidechain and Envelope Follower because both tap audio routing the same way. It is the standard workflow for sustained pads and atmospheric leads in genres where the breakdown should still pump.

## The Live 10 LFO Tool / Max-for-Live legacy

Pre-Live 12, the only way to get "Envelope Follower to any parameter" was the Max for Live LFO and Envelope Follower devices (which still ship with Live but are now redundant for most purposes). Pre-Live-12 tutorials show this Max for Live workflow as if it is the modern way — it is not. In Live 12.x, the native Modulators (Envelope Follower, Shaper, LFO) replaced this M4L layer with a faster, lower-CPU, and more deeply-integrated equivalent. The factory M4L "Envelope" and "LFO" devices still appear in the browser under Max for Live → Audio Effects; they are version-neutral and work, but for Live 12 you reach for the native Modulators first. Cross-link to `corpus/daw/ableton/timeless/classic-compressor-sidechain-ducking.md` for the pre-modulator workflow file (I8 in the stream).

## Cited Retrieval Topics

- "how do i sidechain in ableton live 12"
- "ableton envelope follower modulator how to"
- "kick sidechain bass ableton settings"
- "duck a reverb send with sidechain ableton"
- "sidechain a filter cutoff ableton"
- "compressor sidechain vs envelope follower live"
- "ghost kick sidechain trick ableton"
- "sidechain EQ filter ableton compressor"
- "how do i make pumping bass in ableton"
- "modulate a parameter from audio in ableton"

## Sources

- [Ableton Live 12 Reference Manual — Live Audio Effect Reference](https://www.ableton.com/en/manual/live-audio-effect-reference/)
- [Ableton Live 12 Reference Manual — Max for Live Devices](https://www.ableton.com/en/live-manual/12/max-for-live-devices/)
- [Ableton Blog — Sidechain Compression: Part 2 — Common and Uncommon Uses](https://www.ableton.com/en/blog/sidechain-compression-part-2-common-and-uncommon-uses/)
- [Sound on Sound — Pushing The Envelope](https://www.soundonsound.com/techniques/pushing-envelope)
- [Sonic Academy — How to Sidechain in Ableton Live: Step By Step Guide](https://www.sonicacademy.com/blog/how-to-sidechain-in-ableton-live-step-by-step-guide)
- [Production Music Live — How To Sidechain In Ableton (The Easy Way)](https://www.productionmusiclive.com/blogs/news/how-to-sidechain-in-ableton)
- [Magnetic Magazine — Sidechaining in Ableton 12: A Creative Guide](https://magneticmag.com/2025/12/sidechaining-in-ableton-12/)
- [Icon Collective — Sidechaining in Ableton 12: A Comprehensive Guide](https://www.iconcollective.edu/sidechaining-in-ableton-12-a-comprehensive-guide)
- [macProVideo — Ableton Live 10: Sidechain Any Parameter With Envelope Follower](https://www.macprovideo.com/article/ableton-live/ableton-live-10-sidechain-any-parameter-with-envelope-follower)

See also: `corpus/mixing/compression-fundamentals.md`, `corpus/mixing/low-end-management.md`, `corpus/daw/ableton/devices/compressors-glue-multiband-drumbus.md`, `corpus/daw/ableton/live-12/modulators-shaper-lfo-envelope-follower-note-modulator.md`, `corpus/daw/ableton/timeless/classic-compressor-sidechain-ducking.md`, `corpus/daw/ableton/patterns/parallel-compression-in-live.md`
