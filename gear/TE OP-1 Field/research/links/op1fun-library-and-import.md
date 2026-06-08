https://op1.fun/
op1.fun · Jordan Sitkin (GitHub: dustMason) · community patch library, ongoing (accessed 2026-06-03)

# op1.fun — the primary OP-1 patch library + how to download/import

op1.fun is the de-facto community repository for OP-1 / OP-1 Field patches. Free, user-uploaded, "a personal project for the benefit of the community" (creator Jordan Sitkin, jordan@op1.fun). Hosts **12,500+ patches** organized by **type: synth, sampler, drum**, plus user-curated **packs** and a **tape** archive.

## What's on it
- **Patches** — individual synth-engine presets, sampler patches, and drum kits, each as a downloadable .aif (the format documented in `op1-patch-file-format.md`). Each patch page shows sample rate (44.1 kHz), length, FX/LFO settings, download count, and likes.
- **Packs** — users bundle their patches into named collections (e.g. creators re-host Red Means Recording sets; search by user).
- **Tapes** — a 4-track web player to save/play back OP-1 tape recordings (subscriber feature).

## Three ways to get a patch onto the device

### 1. Manual drag-and-drop (works for any source, no app)
1. Connect OP-1 Field to the computer by USB-C.
2. Put it in content/disk mode: **hold `shift` + press `com`, then press `T4`** to enable the USB (MTP) connection. The unit mounts as a disk with `synth/` and `drum/` folders.
3. Download the .aif patch (or unzip a pack) on the computer.
4. **Drag the patch file (or pack folder) into the `synth/` or `drum/` folder** — synth presets and sampler patches go in `synth/`, drum kits go in `drum/`.
5. Press **`T4` again to eject**.
6. On the device go to **synth** or **drum** and load the new sounds (`shift`+`T1` opens the browser).

### 2. op1.fun Mac companion app (one-click load)
- A **free macOS menubar app** (`dustMason/op1.fun.app`, Electron) loads a patch straight from the website to a connected OP-1 with a single click — it handles the mount/copy/eject for you. Download from its GitHub releases. macOS only.

### 3. Web MIDI audition (no download, in browser)
- You can **audition drum and sampler patches in the browser**: plug the OP-1 in over USB and op1.fun plays the patch through it via Web MIDI before you commit to downloading. (Chromium-based browser required for Web MIDI.)

## Drum Patch Builder (make a kit in the browser)
- op1.fun has an in-browser **Drum Patch Builder**: drop a collection of individual one-shot samples in and it assembles a single OP-1 drum-kit .aif with the 24 slice markers written for you (the same start/end-marker logic as schollz/teoperator). Lets you build kits without owning the hardware or running CLI tools. Output is a standard drum .aif you then load by method 1 or 2.

## Named patches/packs worth knowing (from community threads)
- Stock OP-1 drum kits **"Bronze"** and **"Tantalum"** are repeatedly cited favorites (Elektronauts).
- **Cuckoo's** patch sets (via his Patreon) are widely recommended.
- **Red Means Recording** sets are re-hosted on op1.fun (user `avikabir`, pack "red-means-recording") and sold direct (see RMR capture).
- Honest flag: op1.fun patch pages list FX/LFO settings and length, but the precise per-knob parameter values **cannot be read from the web UI** — you have to download the .aif and dump its JSON (`op1-dump`, op1tools) to see the actual `knobs`/`adsr`/`fx_params`. So "real parameter values" for a specific named op1.fun patch require the file in hand; I did not download-and-dump individual patches here.

## Other libraries to follow
- **teenage.engineering/downloads/op-1/sound-packs** — official TE sound packs (free), with the official drag-drop install steps.
- **op1.center** — curated sample/sound packs (Classic/Genre/Create/VIP ranges), OP-1 Field compatible, drag-and-drop.
- **SoundGhost** (soundghost.net, tag op-1-field) — paid Field packs (e.g. "Float" — 100 ambient presets).
- **Patchstorage** — has an OP-1 section but it is thin compared to op1.fun; op1.fun is the real hub.
- **op1essentials.com**, **soundpacks.com** — free drum-sampler kit collections (130+ kits).
