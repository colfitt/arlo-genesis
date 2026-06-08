# Classic Compressor Sidechain Ducking

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** [Live 12 Reference Manual — Compressor](https://www.ableton.com/en/live-manual/12/audio-effect-reference/#compressor); [Live 12 Reference Manual — Routing and I/O](https://www.ableton.com/en/live-manual/12/routing-and-io/); [Attack Magazine — Sidechain Compression Explained](https://www.attackmagazine.com/technique/passing-notes/sidechain-compression/); [Ableton Learn Live — Sidechaining](https://www.ableton.com/en/blog/sidechain-compression-bass-mix-tips/)
**Tags:** `daw-ableton`, `live-12`, `daw-ableton-timeless`, `sidechain`, `compression`, `ducking`, `mixing`, `recipe`

---

## What "classic sidechain" means in Live

Before Live 12 added the Envelope Follower modulator that can duck any parameter on any device, sidechain ducking in Ableton meant exactly one thing: a stock **Compressor** on the destination track, with its sidechain input fed from another track via the **Audio From** routing menu. That workflow shipped in Live 8 (when the Compressor's sidechain panel got its current form) and is still in the [Live 12 Reference Manual Compressor entry](https://www.ableton.com/en/live-manual/12/audio-effect-reference/#compressor) unchanged in concept. Every existing online tutorial older than 2024 assumes this workflow when it says "sidechain in Ableton." The technique is foundational because it predates Live's modulator system by more than a decade, is CPU-light, and is perfectly predictable — a Compressor is just a Compressor. The Live-12-era alternative (Envelope Follower modulator) is covered in this corpus' D2 production-patterns file and the Modulators file in the live-12 area; this entry covers the pre-modulator approach in full so users following any classic tutorial can implement it correctly in Live 12.

## Opening the sidechain panel on the Compressor

Drop a stock **Compressor** on the track you want to duck. Click the small triangle (▶) at the top-left of the Compressor's UI to expand the sidechain panel — it slides out and adds three columns to the device: the Audio From section (source selection), the Gain and Mix controls, and the EQ section (a small filter you can apply to the keying signal before it hits the detector). The sidechain panel has two activation toggles: **Sidechain** at the top enables the external key signal as the detector input, and **EQ** below it enables the inline filter. Both must be on for the EQ to actually shape what the compressor reacts to. The [Live 12 Reference Manual Compressor section](https://www.ableton.com/en/live-manual/12/audio-effect-reference/#compressor) documents the panel layout. If you don't see the triangle, you're looking at the device collapsed — click the device's title bar to expand the full UI first.

## Routing the kick into the bass Compressor — the canonical recipe

The textbook deep-house/EDM kick-ducks-bass move: insert a Compressor on the **bass track**, expand its sidechain panel, set **Audio From** to the kick track, leave the post-channel dropdown on **Post FX** (the kick's processed signal feeds the detector, which is usually what you want). The kick track stays full-volume in the mix — only the bass track's Compressor is reacting to the kick. The kick's own signal is unaffected. The routing is documented in [Ableton's Routing and I/O manual section](https://www.ableton.com/en/live-manual/12/routing-and-io/). If the kick is buried in a Drum Rack, set Audio From to the Drum Rack and use the chain dropdown to pick the kick chain specifically — sending the whole rack as the key signal will trigger ducking on every drum hit, not just the kick.

## Settings for a punchy kick-ducks-bass duck

For a hard four-on-the-floor duck where the bass gets out of the kick's way: **Threshold** low enough that every kick triggers (typically -20 to -30 dB depending on kick level), **Ratio** 4:1 or higher (some producers go to ∞:1 for a hard gate-like duck), **Attack** as fast as possible (0–1 ms — you want the duck to start instantly when the kick hits), **Release** tuned to the tempo so the bass swells back in just before the next kick (typically 100–250 ms at 120–128 BPM, longer at slower tempos). Watch the gain-reduction meter — aim for 4–8 dB of reduction on each kick hit for a clearly audible pump. [Attack Magazine's sidechain guide](https://www.attackmagazine.com/technique/passing-notes/sidechain-compression/) and Ableton's own [sidechain blog post](https://www.ableton.com/en/blog/sidechain-compression-bass-mix-tips/) both document this range. The release is the musical knob — too short and the pump is choppy, too long and the bass never fully returns.

## The chest-pump master bus trick

Beyond bass ducking, the same routing produces the deep-house "breathing" master-bus pump. Drop a Compressor on the **master track** (or a Glue Compressor on a 2-bus group), sidechain it from a four-on-the-floor kick (often a dedicated "pump kick" that drives the sidechain but isn't audible in the final mix). Settings differ from bass-ducking: **Ratio** lower (2:1 to 4:1), **Threshold** set so every kick gives ~3–5 dB of reduction, **Attack** medium-fast (5–15 ms — slightly slower than bass-duck attack so the kick's transient survives), **Release** tempo-tuned (200–400 ms). The whole mix breathes with the kick. This is the [Eric Prydz "Call on Me" sound](https://www.attackmagazine.com/technique/passing-notes/sidechain-compression/) and the deep-house chest-pump signature. The master bus pump is a stylistic effect, not a corrective one — use it on tracks where the pump is part of the genre vocabulary, not on songs where it isn't.

## The kick-key-then-mute trick

The classic problem: you want the bass to duck against a kick rhythm that isn't actually in your final track — maybe you're producing a half-time song but want a quarter-note pump, or you've muted the kick during a breakdown but still want the bass to breathe. The fix is the **kick-key-then-mute trick**: create a dedicated MIDI track with a kick pattern at the rate you want to drive the ducking, route the bass Compressor's sidechain Audio From that track (with the post-channel dropdown left at **Post FX** so it sees the audio), then **mute** the kick-key track's mixer fader. Muting the fader silences the kick in the master mix, but the post-FX signal feeding the sidechain is still generated — the Compressor on the bass continues to duck on every "phantom" kick. This works because Ableton's routing pulls the signal at the source's post-FX point regardless of mixer mute state. Document this in your project notes (color-code the muted kick-key track in red); future-you will not remember why the bass is pumping with no kick visible.

## EQing the key signal before detection

The sidechain panel's EQ section lets you filter what the Compressor's detector "hears" without affecting what's in the mix. A common move: HPF the keying signal at ~80–100 Hz so only the kick's body triggers the duck, not the kick's click. The reverse — LPF at ~200 Hz — makes the ducker respond to the sub-thump and ignore the click and shell, useful when the kick has a lot of high-frequency content you don't want triggering the duck. The EQ has three bands (LowCut/LowShelf, Bell, HiCut/HiShelf) like a stripped EQ Three. The keying-signal EQ is documented in the [Live 12 Reference Manual Compressor section](https://www.ableton.com/en/live-manual/12/audio-effect-reference/#compressor). Use the **Listen** button (headphone icon) on the EQ section to monitor what the detector is hearing — playing back with Listen on is the fastest way to dial in the filter.

## Why "Post FX" usually beats "Pre FX" as the sidechain pickup point

The Audio From dropdown has a second selector (Pre FX / Post FX / Post Mixer) that determines where on the source track the signal is tapped. **Post FX** (the default and the right choice 95% of the time) means the detector sees the source track after its insert effects but before the mixer fader — so the kick's EQ, transient shaping, saturation, and compression are all baked into the keying signal. **Pre FX** taps the raw track input before any insert. **Post Mixer** taps after the fader, sends, and mute — meaning a muted source produces no keying signal (which is exactly why the kick-key-then-mute trick uses Post FX, not Post Mixer). For normal ducking, Post FX is the natural choice because what the listener hears is what the detector reacts to. Switching to Pre FX is occasionally useful when you want the duck to respond to the kick's raw amplitude regardless of how heavily you've processed it.

## Settings drift: house vs. trap vs. rock

The "right" sidechain settings are genre-bound. For **deep house / EDM** the goal is audible pump as a stylistic feature: high ratio, deep reduction (6–10 dB), fast attack, release tuned to the kick interval — the bass should clearly swell between kicks. For **trap / hip-hop** the goal is usually subtler: lower ratio (2:1 to 3:1), shallower reduction (2–4 dB), so the kick and 808 share frequency space without the listener consciously hearing a pump. For **rock and indie**, classic sidechain is rarely used at all — frequency-domain separation (EQ-based kick/bass carving) is the convention. Use a Compressor sidechain in rock only when you need surgical kick/bass interaction during a specific dense section, and keep the reduction shallow (1–3 dB). Cross-reference the general-corpus [kick-bass-relationship.md](../../../rhythm/kick-bass-relationship.md) for the DAW-agnostic principles behind genre-specific ducking depth.

## CPU and predictability — why the classic approach still wins for tracking

The stock Compressor is one of Live's cheapest devices on CPU. A bass track with a classic sidechain Compressor costs negligibly more than a track with a regular Compressor. The Envelope Follower modulator (Live 12+) is also light, but adds a layer of indirection — its behavior is shaped by Rise/Fall/Delay/Gain knobs that don't directly map to compressor parameters, and dialing a clean duck takes practice. The classic approach has a 15-year corpus of tutorials, presets, and producer muscle memory behind it. For session work where you're moving fast and want a predictable result, the stock Compressor's sidechain is still the default reach. The Envelope Follower wins when you need to modulate something a Compressor can't — filter cutoff, send level, oscillator frequency — but for plain ducking, the classic Compressor is the right tool. The [Live 12 modulators file in this corpus](../live-12/modulators-shaper-lfo-envelope-follower-note-modulator.md) covers when to switch.

## Glue Compressor sidechain — same workflow, different character

The Glue Compressor (Ableton's SSL-style bus compressor) has the same sidechain panel architecture as the regular Compressor, with the same Audio From routing and the same expand-triangle to open it. The Glue's sound is different — slower, more analog-flavored, with a softer knee — so it's a common choice for master-bus pump where you want the duck to feel musical rather than surgical. Use the Glue's sidechain for the chest-pump trick on the master bus or on group tracks; use the regular Compressor's sidechain for fast bass-ducking on the bassline. Both devices' sidechain inputs accept the same Audio From sources, so you can run multiple sidechained Compressors on different tracks all keyed from the same kick. The [Live 12 Reference Manual Glue Compressor section](https://www.ableton.com/en/live-manual/12/audio-effect-reference/#glue-compressor) documents the panel.

## When to switch to the Envelope Follower modulator instead

The classic Compressor sidechain has three real limits. First, it only ducks volume — if you want to duck a filter cutoff, a send amount, or a synth's oscillator level, the Compressor can't. Second, the ducking is volume-only on the whole signal path through that Compressor — you can't easily duck different processing in different ways on the same track. Third, the response shape is fixed to compressor-style (instant attack, exponential-ish release) — for slower, more wave-shaped ducking you want a custom curve. The Envelope Follower modulator (Live 12+) handles all three: it produces a modulation signal from any audio source and can be mapped to any parameter on any device with arbitrary Rise/Fall shaping. Use it when you need parameter-level ducking the classic Compressor can't deliver. For plain "kick ducks bass" ducking — still classic Compressor. The D2 production-pattern file ([sidechain-ducking-classic-vs-modulator.md](../patterns/sidechain-ducking-classic-vs-modulator.md)) covers the decision matrix in full.

## Cited Retrieval Topics

- "how do i sidechain in ableton"
- "ableton compressor sidechain not working"
- "how do i duck the bass with a kick in live"
- "what attack and release for sidechain compression in ableton"
- "how do i make the bass pump without showing the kick"
- "ableton sidechain key signal vs envelope follower"
- "deep house chest pump master bus settings"
- "how to set up the compressor sidechain panel in live"
- "ableton glue compressor sidechain"
- "post fx vs pre fx sidechain in ableton"

## Sources

- [Live 12 Reference Manual — Compressor](https://www.ableton.com/en/live-manual/12/audio-effect-reference/#compressor)
- [Live 12 Reference Manual — Glue Compressor](https://www.ableton.com/en/live-manual/12/audio-effect-reference/#glue-compressor)
- [Live 12 Reference Manual — Routing and I/O](https://www.ableton.com/en/live-manual/12/routing-and-io/)
- [Attack Magazine — Sidechain Compression Explained](https://www.attackmagazine.com/technique/passing-notes/sidechain-compression/)
- [Ableton blog — Sidechain Compression: Bass Mix Tips](https://www.ableton.com/en/blog/sidechain-compression-bass-mix-tips/)

## See also

- [corpus/daw/ableton/patterns/sidechain-ducking-classic-vs-modulator.md](../patterns/sidechain-ducking-classic-vs-modulator.md) — the production-pattern file comparing classic vs. modulator workflow
- [corpus/daw/ableton/live-12/modulators-shaper-lfo-envelope-follower-note-modulator.md](../live-12/modulators-shaper-lfo-envelope-follower-note-modulator.md) — the Envelope Follower modulator alternative
- [corpus/daw/ableton/devices/compressors-glue-multiband-drumbus.md](../devices/compressors-glue-multiband-drumbus.md) — the Compressor family deep-dive
- [corpus/daw/ableton/workflows/routing-input-output-sends-sidechain.md](../workflows/routing-input-output-sends-sidechain.md) — the routing layer underneath this technique
- [corpus/rhythm/kick-bass-relationship.md](../../../rhythm/kick-bass-relationship.md) — DAW-agnostic kick-bass interaction principles
- [corpus/mixing/low-end-management.md](../../../mixing/low-end-management.md) — DAW-agnostic low-end mixing principles
