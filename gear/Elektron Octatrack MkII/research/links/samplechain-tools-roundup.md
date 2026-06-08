https://github.com/brian3kb/digichain
github.com / digichain.brianbar.net + elektronauts "definitive list" #32418 · various authors · 2017–2024

# Octatrack sample-chain & prep TOOLS — roundup (how to build chains + slice grids)

The OT doesn't share "presets"; the shareable atoms are **Sets/Projects** and **sample chains + their `.ot` slice files**. These are the tools to make/convert them.

## DigiChain (free, web — best modern option)
- URL: **https://digichain.brianbar.net/** (also offline executables on itch.io). Free, browser-based, works offline after load.
- Builds sample chains; **batch-converts to 44.1k/24-bit stereo** (the format the OT expects); downloads a **zip with folder structure intact, ready to drop on the OT's CF card**.
- Also IMPORTS existing **`.ot` files to re-slice** to individual samples for re-export/joining. (Note: per its docs it focuses on chain-building + .ot import/extract; OctaChainer is the dedicated .ot-slice-grid generator.)
- Multi-device (OP-1 Field, OP-XY, OP-Z, Digitakt, OT, M8) — useful across this rig's Digitakt 2 / OP-1 Field too.

## OctaChainer (free, desktop — the classic)
- ticticelectro.com/2017/08/26/octachainer-v1-3/ (v1.3.1, 2020). Mac + Windows. Tic Tic (Norway).
- Concatenates WAVs → one `chain.wav` + writes the companion **`.ot` slice-data file** so the OT loads it pre-sliced. See samplechain-octachainer-tool.md for full workflow. Sunshine Jones-endorsed for long live sets.

## OctaEdit (paid, ~$99 — full editor)
- The comprehensive desktop OT manager/editor: edit Projects, samples, slices, parts, chains on the computer. Heaviest tool; overkill unless you manage many Projects. (Windows; check current availability/macOS support — flag.)

## Others mentioned
- **Lopochain** — Mac sample-chain utility. **gtbg** (github.com/ClintH/gtbg) — sample preparer for OT + Machinedrum. **Max for Live** OT-compatible devices exist (free).

## The on-device slice-grid step (no tool needed)
On the OT you can always slice a loaded sample manually: **SRC → SLICE → CREATE SLICE GRID** (choose number of slices; answer **YES to zero-crossings** to reduce clicks). Tools just pre-bake this into the `.ot`.

## The .ot file (format note)
Each sample can carry a sidecar **`.ot`** holding slice points, slice count, tempo/bars, loop + timestretch mode, and gain. Copy the `.wav` AND `.ot` together into the Set's AUDIO folder.

## Where to get chains/packs
- **Official Elektron packs** (~€30 ea): Octa Pak Vol.1–6 (Dubstep/Electro/Tech&Techno/DnB/House/Indie Dance), plus genre titles; **free "Drum Enthusiast" pack**.
- Third-party w/ chains: Driven Machine Drums, Replicant Sounds (TB-606/Drumatix), various free TB-303/DX7 chains. Loopmasters sells "Octatrack Set" / "Octatrack Programs" format packs.

Sources: github.com/brian3kb/digichain, digichain.brianbar.net, ticticelectro.com/2017/08/26/octachainer-v1-3/, elektronauts.com/t/definitive-list-octatrack-packs-chain-tools/32418, github.com/ClintH/gtbg
