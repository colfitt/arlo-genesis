https://www.arturia.com/products/software-instruments/pure-lofi/overview
Arturia (official overview) + CDM (cdm.link/v-collection-11) editorial · 2025

> Spec snapshot + independent editorial framing. Reinforces the central correction: this is an Arturia INSTRUMENT, not a Cableguys effect.

## Official spec (Arturia overview page)
"Your go-to instrument for authentic lofi sound." **Type: software instrument** (synth/sampler), not an effect. **Formats: Standalone, VST, VST3, AU, AAX.** Resizable GUI, MPE, NTS-ESP microtuning, NKS.
- **Sound sources:** 40+ multisampled realistic instruments (bells, winds, guitars, pianos, strings, synths); 130+ custom LoFi-oscillator waveforms (analog-inspired, harmonic, tonal artifacts); 130+ melodic samples + 190 texture/transient noise layers.
- **Two engine slots** (parallel) each running Realistic / Creative Sampler / LoFi Oscillator.
- **9 per-engine Hardware modes:** CMI, EMU (Emulator II), SK-1, SP-1200, S900, MPC60 + Arturia Deteriorate / Damage / Crush.
- **LoFi Processor:** 6 coloration styles (Golden Age, Velvet Frost, Vintage Glow, Dim Memories, Cathodic Tube, Fuzzy Line) × 6 params (Drive, Wobble, Wear, Speaker, Tone, Vintage).
- **3 filter types:** Clean, Analog, LoFi (downsampling).
- **Effects rack:** 4 slots, 18 studio FX.
- **Advanced panel:** drag-and-drop modulation (ADSR, Function, Random, Voice Modulator, Mod Sequencer), macros.
- **250+ presets.** ~£149 standalone; also in V Collection 11 Pro.

## CDM editorial (independent, Apr 2025)
Calls Pure LoFi **"the love child of Arturia's Augmented series and the Baby Audio BA-1"** — borrowing the Augmented-series approach (instrument model + synthesis + texture + filter). The nine vintage emulations are swappable engines you "toggle on the fly by clicking the disks." Verdict: **"a gem... the best stress-relieving instrument Arturia has made yet,"** interface "joyous," ideal for "dreamy and lo-fi stuff" and ambient work. Notable workflow line: **"you can make an entire ambient/lo-fi album in a preset, more or less"** — using the Advanced page to modulate things like the noise-texture level. Pairs well with the Augmented series.

## Why this matters for the repo
The repo files Pure LoFi under **Cableguys** (`Software/Cableguys/`), and GearList.md separately lists it (correctly) under **Arturia V Collection 11** ("38 instruments detected"). The Cableguys `SoftwareProfile.md` summary ("ShaperBox, Pure LoFi, HalfTime") is wrong — Pure LoFi is an Arturia product; only the framing as a Cableguys plugin is the error, the .app/.component/.vst/.vst3 files genuinely on disk are Arturia's. **On-disk proof (see `purelofi-MISATTRIBUTION-it-is-arturia.md`):** the AU component Info.plist = `CFBundleIdentifier com.arturia.component.Pure-LoFi`, manufacturer `Artu`, name "Arturia: Pure LoFi", **type `aumu` (music instrument, NOT effect `aufx`)**; the app installs to `/Applications/Arturia/Pure LoFi.app`. `scripts/scan_plugins.py`'s brand-grouping heuristic mis-bucketed it into the Cableguys group, and CONTENTS.md / SoftwareProfile.md inherited the error.
