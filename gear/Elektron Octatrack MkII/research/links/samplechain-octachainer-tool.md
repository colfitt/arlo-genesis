https://ticticelectro.com/2017/08/26/octachainer-v1-3/
ticticelectro.com · Tic Tic (Norwegian duo) · 2017 (v1.3), v1.3.1 in 2020 — also mirrored/endorsed at sunshine-jones.com

# OctaChainer — free sample-chain + .ot slice-data maker (Mac/Win)

The standard free desktop tool for turning a folder of WAVs into a single chained `.wav` PLUS its companion `.ot` slice-data file the Octatrack reads. Cross-platform (macOS + Windows), free.

## What a sample chain IS (and why it matters on the OT)
A sample chain = many individual samples concatenated into ONE file, loaded onto ONE OT sample slot, then **sliced** so each original sample is a slice you trigger via trigs, p-locks, sample-locks, or MIDI. Why: the OT has limited slots/parts; chains let one Flex/Static slot hold dozens of sounds. Slice mode + per-step slice p-locks = a whole drum/texture kit on a single track.

## The .ot file format
The OT stores per-sample metadata in a sidekick **`.ot` file** next to the `.wav`: slice points, slice count, tempo/bars, loop and timestretch attributes, gain. Chain tools write the `.ot` so the OT loads the chain with slices already defined — no manual slicing.

## OctaChainer workflow
1. Open OctaChainer → load your samples (drag in, reorder to taste).
2. Set target format (bit depth / sample rate), gaps/padding, tempo/bars if relevant.
3. Export → produces `chain.wav` + `chain.ot`.
4. Copy BOTH files into the Set's `AUDIO` folder on the CF card.
5. On OT: assign the chain to a Flex/Static slot; slices are already present (or SRC SETUP → SLICE → it reads the .ot grid).

## Why Sunshine Jones (techno/house, ex-Soul Capsule) endorses it
He runs 3+ hour live OT sets of 10–14 songs and the OT's 4-Parts-per-bank limit makes fast song-to-song transitions hard. Chains let him pack many songs' stems into chains; when adding new material he only slices the NEW samples — prior slice work is preserved. (sunshine-jones.com writeup.)

## Rig use
Print banjo rolls / fuzz-wall fragments / VG-800 pad stabs as individual WAVs, chain them, drop one chain on a track, and p-lock slices per step for "banjo-as-glitch-lead" or a texture kit without burning sample slots.

Related tools (see samplechain-tools-roundup.md): DigiChain (web), OctaEdit (paid, full editor), Lopochain, gtbg.
