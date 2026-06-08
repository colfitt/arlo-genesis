https://www.eventideaudio.com/forums/topic/h90-routing-question/
Eventide official forum · user (Q) / tbskoglund (Eventide staff, A) · Feb 15, 2024
(Plus parallel/series + spillover mechanics corroborated across routing docs and the megathread)

# Routing rules + the spillover-via-duplicate-Programs trick

## Series vs Parallel — the rule that confuses people
- **Parallel requires TWO Presets ON THE SAME PATH.** Staff: *"There needs to be two presets on one path for them to be able to run in parallel."* A single Preset can't "run parallel against nothing."
- You **cannot mix routing modes** (e.g. Path 1 parallel + Path 2 series) in a Pre/Post Dual configuration — parallel is only available when both Presets occupy the same path.
- **Program Mix is global:** *"The Program Mix will be for both Path 1/2 (and both Presets)."* It is not per-path/per-Preset.

## Latency by routing (from the megathread)
- Series ~4.5 ms, Parallel ~3.8 ms; each Insert adds ~3.8 ms.

## Spillover smoothing trick (community)
- For glitch-free routing/level changes, make **DUPLICATE Programs that differ only in routing (e.g. one routing OFF, one parallel)** and switch between them by PC — spillover bridges the change smoothly. (Also the only way to "change Insert Routing via MIDI," since routing itself isn't CC-mappable.)

## Spillover vs switching-speed tradeoff (IMPORTANT)
- Long Spillover Time slows rapid Program changes: if Spillover is, e.g., 30 s and you load several Programs quickly within that window, switching gets sluggish. **Reduce or zero the Spillover Time** if you need fast back-to-back changes; raise it for long ambient tails. Tune per use.

## Kill-dry / wet-only
- The dry path runs through the converters (no analog bypass). For a true wet-only parallel feed, enable **Kill Dry** and blend dry externally (see megathread).

## Rig relevance
End-of-chain stereo into the tape stage: run **Insert/Series, both Presets stereo** for the widest walls (e.g. delay→reverb so repeats get verbed), or **Dual** for a wet/dry-wet split into the PORTA424. For ambient sets keep Spillover moderate-to-long for tail bleed between scenes — but if a song needs fast scene stabs, drop Spillover for that section (or use a HotSwitch instead of a Program change to avoid the reload entirely; see the bugs file).
