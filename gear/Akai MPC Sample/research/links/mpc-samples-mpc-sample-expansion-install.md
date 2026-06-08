https://www.mpc-samples.com/article/mpc-sample-expansion-installation
mpc-samples.com · MPC-Samples (Andy "MPC-Tutor" Avgousti's store) · 2026

The dedicated install guide for getting expansions onto the **MPC Sample (AC50)**. This is the single most important source for the kits/expansions facet — it confirms expansions DO work on the AC50 but via a *Sample-specific edition*, not the generic standalone-MPC `.xpm` package. (WebFetch 403'd on the raw page; content distilled from MPC-Samples' own indexed text via search — verify exact wording on-site, but the workflow is consistent across multiple MPC-Samples pages.)

## Key fact: the AC50 needs the "MPC Sample Edition"
- MPC-Samples builds packs with multiple installers in one download. For the AC50 you use the folder **"MPC Sample Edition"** inside the extracted ZIP — NOT the generic standalone MPC/Force installer and NOT the `.xpn` (which is MPC Software/MPC Beats only).
- This exists because the Sample runs its own firmware, not MPC OS 3 (see loopop transcript). Generic standalone expansions are built around `.xpm` programs in an `Expansions` folder that the bigger MPCs auto-scan; the Sample doesn't share that browser, so packs are repackaged as a "Sample Edition."

## Install steps (distilled)
1. Download the expansion from your File Bank; extract the ZIP anywhere on your computer.
2. Locate the **"MPC Sample Edition"** folder inside the extracted contents.
3. Insert your microSD card fully into the MPC Sample's SD slot; connect the Sample to your computer via USB-C.
4. Power on; hold **[SHIFT] + [PAD 16] (PROJECT)** → turn the **encoder** to highlight **"SD Card Access"** → click the encoder to select. The SD card now mounts as a drive on your computer.
5. On the SD card, create a new folder at the root (no required naming convention), open it, and copy the "MPC Sample Edition" expansion folder inside.
6. **Safely eject** the SD card from your computer's OS first; then press **[B1]** on the Sample to exit SD Card Access mode.
7. Browse to the expansion on-device via the sample/file browser (SD card location) to load kits/samples onto pads.

## Caveats / flags
- **Internal 8 GB is not USB-mountable** (loopop confirms) — so third-party packs realistically live on the **microSD card**, not internal storage. The AC50's limited internal space makes a large SD card the practical home for expansions. DIBIA$E runs a 512 GB card.
- **No kit auto-import as a single playable kit on chops** and **single-kit limitation** (dossier §11) still apply — a "Sample Edition" pack is laid out for the Sample's loader, but you still load one kit at a time.
- Verify per-pack: not every MPC-Samples title ships a Sample Edition yet (young product). Check the product's tech-specs/compatibility note before buying. Generic-only or `.xpn`-only packs will NOT load.

## Bottom line for the rig
Expansions are usable on the AC50 — buy/download ones that explicitly include an **"MPC Sample Edition,"** copy via SD Card Access to a folder on the microSD, and load from there. For anything without a Sample Edition, fall back to loading the pack's raw **WAV** files (the universal path — see goldbaby/free-sources files).
