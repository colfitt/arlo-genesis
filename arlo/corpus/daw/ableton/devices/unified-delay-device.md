# The Unified Delay Device (Live 10.1+)

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Delay; Ableton Live 10.1 release notes (Delay unification); Ableton blog — Beyond the Echo Chamber
**Tags:** `daw-ableton`, `live-12`, `device`, `delay`, `mixing`

---

## What the unified Delay device is

The **Delay** device that ships with Live 12 is the modern, unified delay that combines and replaces the older **Simple Delay** and **Ping Pong Delay** devices. It was introduced in **Live 10.1** (May 2019), not Live 11 — confirmed by Ableton's [Live 10.1 release blog](https://www.ableton.com/en/blog/live-10-1-is-here/) and CDM's [Live 10.1 first-look coverage](https://cdm.link/2019/05/ableton-live-10-1-top-tips/). Per the [Ableton Live 12 Reference Manual — Delay](https://www.ableton.com/en/manual/live-audio-effect-reference/), the unified device exposes Ping Pong behavior, the three delay-time-change modes (Jump, Fade, Repitch), a built-in band-pass filter, freeze, and modulation — all from a single front panel. Older Sets that used Simple Delay or Ping Pong Delay show an Upgrade button when loaded into Live 12, which converts the legacy device to the unified Delay with parameters preserved. The older Filter Delay device is still available separately in the device browser as a legacy option.

## Position in the delay lineup

Live 12 ships three delay devices in active use. **Delay** is the modern unified device (covered here); **Echo** (introduced in Live 10 Suite) is the character-forward analog/tape emulation modeled on the Roland Space Echo, WEM Copicat, and Morley Oil Can, per the [Ableton "Everything Echo" blog with Slynk](https://www.ableton.com/en/blog/everything-echo-slynk/); and **Filter Delay** is the older three-band delay device that survives in legacy form for parallel-band delay work. The rule for choosing: reach for **Delay** when you want a clean, predictable, modulation-capable digital delay; reach for **Echo** when you want analog/tape character — wow, flutter, saturation, the Echo Tunnel display — and a creative reverb section in the delay's feedback path; reach for **Filter Delay** only when working with legacy sets or specifically wanting independent band-split delays in one device.

## The three transition modes: Repitch, Fade, Jump

The unified Delay's most distinctive feature is its three **delay-time-change modes**, which determine what happens audibly when you sweep the delay-time control or automate it. Per the [Ableton Live 12 Reference Manual — Delay](https://www.ableton.com/en/manual/live-audio-effect-reference/), the three modes are:

- **Repitch** — produces a pitch variation when delay time is changed, mimicking the behavior of old tape delay units. Speeding up the tape pitches the existing repeats up, slowing it pitches them down. This is the choice for dub-style tape-echo sweeps and time-stretch-style pitch effects on the wet signal.
- **Fade** — crossfades between the old and new delay times. The result sounds similar to granular synthesis, especially when delay time changes gradually. This is the smoothest, most artifact-free choice for continuous time modulation, but it dulls transients during the crossfade window.
- **Jump** — switches immediately to the new delay time. The result can produce audible clicks if delay time changes while the previous repeats are still decaying. This is the choice for rhythmic delay-time switches between discrete sync values where you want no smoothing — common in glitchy or breaks-style processing.

Note that the plan-document framing of four modes including "Insert" is incorrect — only three modes exist. The mode is selected from the Delay device's mode chooser on the front panel.

## Sync vs free-running time

Each channel of Delay can operate in either **Sync** mode or **Time** mode. In Sync mode, the delay time is set in beat divisions — quarter, dotted-eighth, sixteenth, etc. — locked to the project tempo. In Time mode, delay time is set in milliseconds and runs free of project tempo. Sync vs Time is set independently for the left and right channels, which is what enables the classic asymmetric-delay trick: L on dotted-eighth sync, R on quarter sync, producing the rhythmic complex repeats associated with U2's "Where the Streets Have No Name" or modern dotted-eighth pop guitar production. The **Stereo Link** toggle locks L and R to identical settings; with Link off, you can dial them in separately. The **Offset** controls per channel let you nudge each side slightly off the grid for further width.

## Ping Pong mode

The **Ping Pong** toggle, when activated, makes the delay signal alternate between the left and right channels — the same behavior as the older Ping Pong Delay device, now built into the unified Delay's front panel. Ping Pong replaces the standard parallel-L/R repeat pattern with a bouncing alternation; combined with dotted-eighth sync it produces the canonical dub/dance ping-pong delay sound. Ping Pong respects the same Repitch/Fade/Jump mode setting, so a Ping Pong delay with Repitch mode and slow modulation produces the warbly bouncing tape-echo sound that comes up on countless shipped electronic records.

## The Filter section

The Delay device has a **band-pass filter** in the feedback path (not separate HP and LP filters as on some other devices). The filter has two controls: **Frequency** (center) and **Width** (bandwidth, controlling Q). The filter switch toggles the filter on and off. With the filter engaged, each repeat through the feedback loop is band-pass filtered again, so over multiple repeats the delay tails narrow into the band-pass center frequency — the classic "filtered delay" effect where repeats progressively darken or take on a midrange-focused character. For dub delay, narrow the bandwidth and place the center around 800 Hz to 1.5 kHz; for cleaner echo, widen the bandwidth substantially or turn the filter off.

## Freeze

The **Freeze** button locks the current contents of the delay buffer into infinite cycling at the moment it is pressed, per the [Ableton Live 12 Reference Manual — Delay](https://www.ableton.com/en/manual/live-audio-effect-reference/). New incoming audio is suppressed while Freeze is active. The result is an instant infinite-sustain effect — useful for ambient drones, drop-into-breakdown moments, and live-performance freezes where you sustain the tail of a sound while changing the underlying source. Freeze is mappable to a controller or to a Live 12 Modulator, which makes it a performable parameter. Combined with the Repitch mode and slow modulation, Freeze produces the "frozen tape loop" sound that the Hybrid Reverb's Vintage parameter approximates but Delay does more aggressively.

## Modulation: LFO on time and filter

Delay has a built-in LFO with **Rate**, **Time Modulation** depth, and **Filter Modulation** depth controls, per the [Ableton Live 12 Reference Manual — Delay](https://www.ableton.com/en/manual/live-audio-effect-reference/). The LFO simultaneously modulates both delay time and filter frequency, with independent depth controls for each. Slow rates with small time-modulation depth in Repitch mode produce subtle pitch wobble in the repeats — the canonical "tape wear" effect. Faster rates with larger depth in Fade mode produce the granular-style smear that characterizes some modern texture-driven delays. The modulation is internal to the device — for external modulation (sidechain envelope, automation curve, etc.) use a Live 12 Envelope Follower or Shaper Modulator routed to Delay's time parameter from outside.

## Tape-echo emulation recipe

The canonical "tape echo" patch on the unified Delay: set mode to **Repitch**, engage the **Filter** with narrow bandwidth centered around 1–1.5 kHz, set the LFO rate to a slow value (0.3–0.8 Hz), set time-modulation depth to a small amount (5–15%), set filter-modulation depth to a small amount, set feedback in the mid-range (40–60%), and set Sync mode to dotted-eighth or quarter depending on the groove. The result approximates the wow-and-flutter pitch instability, band-limited frequency response, and feedback character of a Space Echo or similar tape delay — without reaching for the more character-heavy (and more CPU-intensive) Echo device. For more extreme tape character, switch to the Echo device instead, which models the saturation and modulation more aggressively.

## Ducking the delay with a separate compressor

The unified Delay does **not** have a built-in sidechain or ducking section — that capability lives in the Echo device but not in Delay. To duck the delay against a kick or vocal in the same way you'd duck a reverb send, place a Compressor after the Delay on the return track, set up the Compressor's external sidechain input from the source you want to duck against, and let the Compressor reduce the delay's level on every trigger hit. The Live 12 alternative is the **Envelope Follower modulator**: place an Envelope Follower on the return track, route its source from the trigger, and map its output to the Delay's Dry/Wet or to a Utility's gain. This achieves the same ducking effect with finer envelope shaping than a compressor provides, and is the Live-12-native way to do this. Cross-link D2 (sidechain ducking) for the full discussion.

## When to reach for Delay vs Echo vs Filter Delay

**Delay** is the right default for digital delay work — clean, predictable, modulation-capable, CPU-light, ping-pong-capable. Use it on vocal slap delays, dotted-eighth guitar delays, ambient lead repeats, sync-locked rhythmic delays. **Echo** is the right choice when you want explicit analog/tape character — its three "Character" modes (Bucket Brigade, Tape, Digital), its built-in reverb in the feedback path, its more aggressive modulation, and its "wobble" parameter set. Reach for Echo for dub, lo-fi, and character-forward production. **Filter Delay** is mostly legacy at this point, retained for set compatibility. The working rule: start with Delay; reach for Echo when Delay sounds too clean and you want tape-style imperfection baked into the sound, per [MusicTech's Echo and Delay tutorial](https://musictech.com/tutorials/ableton-live-echo-delay/).

## Common mistakes with the Delay device

Three traps recur. **First**, ignoring the mode chooser and leaving it on whatever default loaded — Repitch on a continuous-automation delay time produces noticeable pitch artifacts that are usually unwanted; Jump on a slow ramp produces clicks; the mode should match the intended motion. **Second**, leaving the band-pass filter engaged with narrow bandwidth on every delay — it makes repeats dark and quiet, sometimes wanted but often a hidden cause of "the delay disappeared in the mix." **Third**, expecting Delay to have a sidechain — it doesn't, and the workaround (Compressor after the Delay, or Envelope Follower modulator) needs to be in the chain explicitly. Engineers coming from Echo often miss this difference and assume Delay can duck on its own.

## Cited Retrieval Topics

- "what's the difference between delay and echo in ableton"
- "ableton delay repitch fade jump modes"
- "how to make a tape echo sound in ableton delay"
- "ableton ping pong delay where is it"
- "what version of ableton added the unified delay"
- "how to duck a delay in ableton live 12"
- "ableton delay freeze button what does it do"
- "ableton delay vs echo when to use"
- "ableton delay built in filter how to use"
- "how to do dotted eighth delay in ableton"

## Sources

- [Ableton Live 12 Reference Manual — Live Audio Effect Reference (Delay)](https://www.ableton.com/en/manual/live-audio-effect-reference/)
- [Ableton Blog — The free Ableton Live 10.1 update is here](https://www.ableton.com/en/blog/live-10-1-is-here/)
- [CDM — Ableton Live 10.1 is out now; first things you should try](https://cdm.link/2019/05/ableton-live-10-1-top-tips/)
- [Ableton Blog — Everything Echo: Slynk Explores Live's New Delay](https://www.ableton.com/en/blog/everything-echo-slynk/)
- [Ableton Blog — Beyond the Echo Chamber: Inventive Effects Using Live's Delay Devices](https://www.ableton.com/en/blog/beyond-the-echo-chamber-inventive-effects-using-lives-delay-devices/)
- [MusicTech — Understanding Ableton Live's Echo and Delay effects](https://musictech.com/tutorials/ableton-live-echo-delay/)
- [Mixitecture — How to get vintage tape-echo sound using Ableton delay plugins](https://mixitecture.com/learn/delay-modes)
- [Ableton Forum — Simple Delay is gone!?](https://forum.ableton.com/viewtopic.php?t=234819)

See also: [`corpus/mixing/reverb-and-delay-architecture.md`](../../../mixing/reverb-and-delay-architecture.md), [`corpus/mixing/vocal-mixing.md`](../../../mixing/vocal-mixing.md)
