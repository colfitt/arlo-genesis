https://modwiggler.com/forum/viewtopic.php?t=144656
MOD WIGGLER · forum thread "Guitar / Octatrack" · (search-snippet capture; page 403'd to WebFetch, detail from Google result excerpt)

# GUITAR-INTO-OT 4-TRACK FX CHAIN — Thru → Neighbor → Pickup → Flex (a near-exact rig blueprint)

A guitarist's pedalboard-style chain built entirely from OT machines (inspired by reverb+fuzz and bitcrusher pedals). This is the closest published per-track FX-assignment map for the user's "live-mangle the strings through the OT" goal. Concrete machine + FX layout:

## Track 1 — THRU machine (the input stage)
- **FX1 = Filter**, **FX2 = Plate Reverb**.
- **Reverb TIME set LONG** — deliberately, "so the FX in subsequent tracks swell after it" (the reverb tail becomes source material the downstream tracks process).

## Track 2 — NEIGHBOR machine (takes Track 1's output)
- **FX1 = LoFi**, **FX2 = Delay**.
- **LoFi: Bit-Rate Reduction set near the MIDDLE** of its range (audible crush, not destroyed).
- **Ring-mod section configured as a TREMOLO** (low ring-mod freq → amplitude wobble rather than metallic ring).

## Track 3 — PICKUP machine (live loop + heavy modulation)
- **FX1 = Filter**, **FX2 = Spring Reverb**.
- **LFO1 → PITCH, waveform = RANDOM** (drifting detune on the loop).
- **LFO2 → filter WIDTH**, **LFO3 → filter Q/resonance** (two LFOs moving the filter independently = constantly-shifting timbre).

## Track 4 — FLEX machine (resample-and-reprocess)
- **Record Trig**, **record source = Track 1 output**.
- **FX1 = LoFi**, **FX2 = Spring Reverb** (re-crush + re-verb the captured Thru signal).

## Why this is the rig blueprint
Front-board strings (banjo/baritone via VG-800) → OT input → this exact chain gives: filtered+plate-reverbed input, lo-fi tremolo delay, a randomly-detuned spring-reverbed live loop, and a resampled lo-fi layer — all four crossfader-morphable. Maps 1:1 onto the "degraded / sustained wall / banjo-as-lead" aesthetic. Neighbor's "long reverb on T1 → T2 swells after it" is a clean trick for blooming the wall. Pairs with the Y thee Asinine transcript (Thru→Neighbor×3→Pickup×2→Master) already on disk — this one names the actual FX in each slot.

PROVENANCE: community (MOD WIGGLER, cited). Per-track FX assignments verified from search excerpt; exact filter/delay numeric values not stated in source (flagged).
