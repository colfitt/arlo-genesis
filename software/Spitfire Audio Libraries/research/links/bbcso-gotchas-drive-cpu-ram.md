https://vi-control.net/community/threads/bbc-so-and-bbc-abbey-road-heavy-cpu-use-advice.106321/
vi-control.net (CPU/RAM threads) + support.spitfireaudio.com/en/articles/11815356-moving-libraries + 11815389 · accessed 2026-06-11 · forum specifics via search snippets (VI-C 403s); Spitfire support pages = vendor

# BBC SO — pitfalls/gotchas for THIS rig (offline drive, Logic AU, mic load)

## 1. Offline-drive relink (the recurring one)
- BBC SO content lives on the offline **`PlaySomeGodDamnMusic`** drive. The dedicated
  AU **plugin** is on the system drive and always loads, but the multi-GB samples need
  the drive → **mount it BEFORE launching Logic**, or patches show "not found."
- Relink: **Spitfire Audio app → the library → Repair** (or per-product cog → Locate),
  point at the install location, hit REPAIR. Moving content moves only the
  registration; drag the folder first, then Repair. (Spitfire support: "Moving
  Libraries" / "one hard drive with two machines.")
- Discover-tier content is tiny (~200 MB) — if the installed edition is Discover it can
  live on the system drive and **sidestep the offline-drive dance entirely.** Worth
  doing if it IS Discover.

## 2. Mic count = RAM multiplier (Core/Pro only — Discover has no mic mixer)
- **Each added mic position ~doubles the RAM/streaming load** (2 mics ≈ 2×, 3 ≈ 3×…).
  Fully loaded with all mics, BBCSO can hit "~40 GB RAM."
- Forum experience: an i7 quad + 64 GB "could not run more than 2 mics" cleanly; even a
  6-core handled ~3 mics, with **dropouts at 4 mics across 10–12 instances.**
- **Community rule of thumb: 2–3 mics per instance, max.** For THIS rig that's a freebie
  — the ghost workflow wants **Close (+ maybe Leader/spill) only** anyway, then your own
  reverb. Don't load Ambient/Balcony/Atmos: they cost RAM AND ring under Valhalla.
- Streaming from the external drive (esp. an HDD) makes the CPU/dropout risk worse than
  an internal SSD — another reason to keep mic count to 1–2 for held string beds.

## 3. Bounce held beds (kills the streaming cost)
The single best perf move for the drone use case: once a held BBC SO bed is right,
**offline-bounce it to audio** (same move the Cells/LABS guides use). Frees all the RAM
+ streaming, and the resulting "wall" is what you actually degrade/loop — see
`bbcso-bounce-to-wall-evolving-technique.md`.

## 4. Host notes
- **Logic = AU**: the dedicated plugin is native AU, no Kontakt, loads fine. No AU
  gotcha beyond the drive mount.
- **Ableton Live 12 Lite (secondary)**: Lite caps total scenes/tracks and has reduced
  device set, but it DOES host AU/VST3 plugins — BBC SO loads. The constraint is Lite's
  track/return ceiling for big templates, not the plugin itself. (Inferred from Lite's
  general limits; not a BBC-SO-specific source.)
