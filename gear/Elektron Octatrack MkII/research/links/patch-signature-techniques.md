SYNTHESIS · distilled from the captured artist + template + workflow sources in this links/ dir
(no single URL — cross-references: artist-*, template-*, samplechain-* files here, + dossier §4/§13)

# Octatrack "signature techniques & settings" — copyable starting points

The OT has no presets; these are the repeatable *moves* that show up across verified artists and community templates. Copyable where the OT allows fixed values.

## 1. Cortini's "32 sounds → a whole set" (sampler-as-synth)
- Load a small bank of short source recordings (here: ~32 fuzz/banjo/baritone/VG-800 fragments).
- Use **scenes + PTCH** locks to play chords/pitch from one source; build multiple tracks from the same few samples. Crossfader = main performance gesture.

## 2. Panda Bear "DJ the stems" (template)
- Bounce a song to ~7 stems → one per track 1–7; **track 8 = master** (comp + reverb).
- Two identical OTs (or OT + Digitakt) cued with the same content → crossfade song-to-song, laptop-free.

## 3. Mumdance one-shot live build
- Pre-load OT with a curated **one-shot library** (records, synths, field recordings, degraded guitar stabs).
- Lay them live over a steady drum source (Digitakt 2 as the "909"); improvise via sample-locks + trigs by hand. Nothing pre-sequenced.

## 4. Surgeon hands-on / no-menu
- OT = steady **6 drum sounds + backing tracks** foundation; map filter cutoff + FX to an **external knob box (61SL MkIII)** so you perform without menu-diving. Glue with a master comp.

## 5. Stimming OT-as-mixer
- External sources on input pairs **A/B and C/D**; per source choose **through-the-FX-engine (Thru, DIR=0)** or **straight-to-output (DIR=127)**. One OT mixes its 8 tracks + 2 external stereo sources.

## 6. Live resampling loop (Dataline / community standard) — the capture-and-destroy core
- Track recorder buffer + a **REC trig** on the sequencer to capture input pair (AB/CD) or the **internal master** (resampling). All captures at **unity gain** per the FX-template default.
- A **Flex machine** plays the buffer back; **chop into sections** (don't just loop the whole thing); switch live↔resampled with **fast crossfader snaps** + **conditional/FILL trigs**.
- Use **Cue outputs as a send-FX** bus (independent of mains) — and as a clean stem to the Apollo x8 / Babyface.

## 7. Ambient drone hold (rig's aesthetic match)
- **CHAIN BEHAVIOUR**: turn OFF silence-on-pattern-start (`[FUNC]+[BANK]`) so drones sustain across patterns.
- **Polymetric**: different track length per track + sparse trigs at **30–60 BPM** = generative drift.
- **Click avoidance**: dense sources hide loop seams; **long-attack amp env**; Pickup **silent-loop-then-overdub** trick (gain down for first pass). Route long reverb tails **externally (H90/Big Sky)** because per-track FX cut off on Part change.

## Fixed defaults worth standardizing (from the Ultimate FX template)
- Tempo **120 BPM**, pattern length **64 steps (4 bars)**, recordings start at **step 1**, captures at **unity gain**, compressor per input pair (A/B and C/D), freeze-delay parked on **tracks 1 and 5** (the input-pair tracks).

## Universal save discipline
Work auto-caches, but **SAVE PROJECT** before pulling the CF card; use **Part Reload (`[FUNC]+[CUE]`)** to snap back after heavy live tweaking. Parts (not patterns) hold the sound.
