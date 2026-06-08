https://www.eventideaudio.com/forums/topic/h90-inserts-im-using-fill-in-the-blanks/
Eventide official forum · many users (MrClean, tomerz, Infection, drews, fiddlercrabseason, Vow3ll, lennyderoma) / tbskoglund (staff) · Jan 2023 – Jan 2025

# How people actually use the H90 insert loops (real rigs)

The insert loop = patch an external pedal/amp INTO the H90's signal path (Pre-A, Mid between A/B, Post-B, or parallel). Real-world setups people posted:

## Concrete setups
- **MrClean (Jan 5 2023):** Insert 1 → Vox AC15; stereo outs → Roland JC-40 — a configurable **wet/dry/wet** with per-Preset amp selection.
- **tomerz (Jan 6 2023):** Insert 1 → Iridium (return to input 3); insert 2 → amp; outs → interface. KEY: *"mix on insert 2 to amp must be 0%"* to avoid a doubled signal.
- **drews (Mar 19 2023):** Simple — Bogner Burnley on insert 1, Darkglass Duality on insert 2 (drive pedals inside the chain).
- **Infection (Apr 23 2023):** Stereo loop with Strymon Ventris + TimeLine **in parallel** with the H90's own effects. Found W/D/W limits with some wet effects (e.g. Leslie).
- **Vow3ll (Jan 6 2024):** **Hologram Chroma Console as a stereo insert** in one H90; Walrus Meraki + Poly Verbs in a second H90; ES-8 for routing. (Directly relevant — see below.)
- **fiddlercrabseason (July 2 2023 / Jan 2024):** Dual Zoia/Beebo in parallel, patches swapping which effect feeds which insert every 3 beats; uses H90 **HotSwitches to freeze delays**. Desktop variant: H90 → Scarlett 4i4 → laptop (MAX/VCV/Live) → 4i4 → H90, full MIDI via MC-8.

## Insert-loop technical gotchas (staff-confirmed)
- **You CANNOT change Insert Routing via MIDI CC** (tbskoglund, July 31 2023). Workaround: make **duplicate Programs with different routing states** and switch them by PC.
- Insert **send/return/mix levels cannot currently be mapped to external controllers** — instead control the external device's output gain.
- **Parallel + kill-dry can double volume** when inserting parallel delays (lennyderoma, Jan 2025) — unresolved; watch levels.
- When sending an inserted device to its own amp, set that insert's **Mix to 0%** so you don't also hear it doubled at the H90 outs (tomerz).

## Rig relevance (this is notable)
A user runs the **Hologram Chroma Console as a stereo insert inside the H90** — exactly the two pedals that are neighbors on this End board. If the owner ever wanted Chroma to sit INSIDE an H90 reverb (e.g. Chroma's character smearing the pre-reverb signal, then the tail wrapping it), the insert loop supports it: place a stereo insert Mid (between A and B) or Pre-A and patch Chroma in. Match insert **Latency = 0** if Chroma is treated as analog-ish, or trim 0–512 samples if comb-filtering appears. Today the rig runs them in series (Chroma → H90), but the insert option is real.
