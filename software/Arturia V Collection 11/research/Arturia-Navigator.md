# Arturia V Collection 11 — Navigator

The front-end, the shared architecture, and the "which of the 44 for what" map for a
drone/doom/shoegaze rig. Deep flagship guides live beside this:
**`CS-80-V-UsageGuide.md`**, **`Mellotron-V-UsageGuide.md`**, **`Synthi-V-UsageGuide.md`**,
**`Buchla-Easel-V-UsageGuide.md`**, **`Emulator-II-CMI-UsageGuide.md`** — and (2nd pass, 2026-06-11)
**`Matrix-12-V2-UsageGuide.md`**, **`Jup-8000-V-UsageGuide.md`**, **`KORG-MS-20-V-UsageGuide.md`**,
**`Augmented-Strings-Voices-UsageGuide.md`** (20 new sources).

## 1. What's new in V Collection 11 (verified — released April 2025)

VC11 Pro = **45 instruments** (the bundle grew 39→45). `research/links/vc-nav-musictech-whats-new-vc11.md`, `research/links/vc-nav-musicradar-vc11-pro-review.md`
- **Genuinely new:** **Jup-8000 V** (JP-8000, supersaw walls, 18-FX rack — the flagship new synth) · **Augmented Mallets** + **Augmented Yangtze**. (**Pure LoFi** also shipped here but is an *instrument*, filed separately at `Software/Arturia Pure LoFi/` after the scanner-misfiling catch.)
- **Added to the bundle (earlier standalones):** **MiniBrute V** (8-voice poly), **Synthx V** (Elka Synthex).
- **Major overhauls:** **SEM V → V3** (rebuilt, now **8-voice poly** → lush chords/textures); **Augmented Series 2** (new UI, better morph curves, randomizing arp, new content).
- **Clarification:** **Acid V and MiniFreak V are NOT new in VC11** — both shipped in V Collection X (Dec 2023). (Common error.)
- Pricing: Pro $699; new **Intro** tier $199 (10 curated plugins).

## 2. Analog Lab V — the unified front-end (fastest path to a pad)

`research/transcripts/vc-nav-analog-lab-v-full-tutorial.md` — Browse by **Type tiles** (Pad/Lead/Strings…) → audition across all engines without owning the standalone; filter by **Styles/Characteristics** (a "Reverb" tag → drenched ambient presets) and **Genre** (there's an **Ambient** tag). **4 smart macros** per preset (Brightness/Chorus/Delay/Release) — raising **Delay + Release** pushes any preset toward a long ambient wash. **Edit Preset** opens the shared FX "pedals" rack; Likes/tags/Playlists for recall; **Multis** for layers/splits.

## 3. The common architecture (learn one, know them)

`research/links/vc-nav-common-architecture-advanced-panel.md` — modern V instruments share an **Advanced panel**: a **multi-arp** (up to 4 stacked layers); **3 modulator slots** each = ADSR / **Function generator** / **Random** / Voice Mod / Mod Sequencer with drag-and-drop routing; a **4-slot FX rack (17+ effects** incl. **convolution / reverb / delay / lo-fi / tape** — the same rack you see in Analog Lab); **Unison** up to 18 oscillators/key; full **MPE + MTS-ESP microtuning**; resizable UI. Legacy panels (Mini V4, CS-80 V4, Prophet-5 V) keep period mod but share the FX rack + browser.

> **★ Universal "evolving" technique (works on ANY of them):** park 2–3 Advanced-panel
> modulator slots on **Function/Random at unrelated, unsynced rates** → cutoff /
> pitch-detune / FX amount. The conflicting cycles never line up → the pad never
> audibly repeats. Long release + chorus + delay + reverb sell it. `research/links/vc-nav-ambient-drone-reach-for.md`

## 4. Logic AU / CPU / management

`research/links/vc-nav-logic-au-install-apple-silicon.md`, `research/links/vc-nav-cpu-freeze-lore.md`
- Install/activate via **Arturia Software Center** (5 devices). Logic AU-only → the
  `.component` loads under **AU Instruments → Arturia**; if missing, **Plug-in Manager →
  Reset & Rescan**. Verify **Apple Silicon native** (About → ARM64).
- **CPU: these are heavy.** The **Augmented series (Strings/Voices) are the worst
  offenders**; high unison + oversampling on CS-80/Jup-8/Modular/Matrix-12 also bite.
  **Mitigation = freeze/bounce committed parts early** (biggest win); lower internal
  oversampling; bounce long drone/pad washes to audio.

## 5. The reach-for map — all 44, for drone/doom/shoegaze

**Lush pads & walls** — **CS-80 V4** (the wall; dual-layer, ribbon/poly-AT — *own guide*) ★ · **Jup-8000 V** (supersaw walls → degrade through Decapitator/Valhalla) · **Prophet-VS V** (vector **self-morphing** pad — plot a multi-point vector loop with per-segment Rates) · **Matrix-12 V2** (the deepest evolving-texture machine — 5 LFOs + 5 envs/voice, 15 filter modes) · **Jup-8 V4 / OP-Xa V / Prophet-5 V / SEM V3** (poly analog pads) · **Solina V2** (string-machine shoegaze bed — POLY on, ensemble light, phaser whoosh) · **CZ V / Synclavier V** (digital pads). `research/links/vc-pads-prophet-vs-vector-musicradar.md`, `research/links/vc-pads-matrix12-sos-review.md`, `research/links/vc-pads-solina-sos-review.md`

**Drone & noise** — **Synthi V** (pin-matrix + self-resonating filter = no-oscillator drone — *own guide*) ★ · **Buchla Easel V** (West-Coast generative/Krell — *own guide*) ★ · **Modular V3** (deliberate generative webs) · **ARP 2600 V3** (fastest semi-modular drone) · **KORG MS-20 V** (the rig-integration star — **run the banjo / a pedalboard reamp into its ESP + screaming self-oscillating filters**) · **MiniFreak V** (modern digital evolving textures — Cycling Envelope + mod sequencer). `research/links/vc-drone-other-synths-modular-roundup.md`

**Lo-fi sampling / degraded** — **Emulator II V** (8-bit DPCM grit — *own guide*) ★ · **CMI V** (Fairlight gritty resampling — *own guide*) ★ · **Synclavier V** (Timbre Slices = 2–5-min morphing drone bed). All accept **your own samples** — sample the banjo/pedalboard → run through EMU II/CMI for the "recorded-wrong" treatment.

**Shoegaze strings/choir & vintage keys** — **Mellotron V** (tape Flutter/Saturation/Mechanics — *own guide*) ★ · **Augmented STRINGS/VOICES/MALLETS/YANGTZE** (modern evolving texture engines, but **freeze them — CPU-hungry**) · **DX7 V / CZ V** (FM / phase-distortion glass-bell pads) · **CP-70 V** (dusty felt-ish piano — push the output-noise level) · **Farfisa V / VOX Continental V2 / B-3 V2** (reedy/swirling organ beds) · **Stage-73 V2 / Wurli V3 / Clavinet V** (degradable vintage keys under banjo) · **Vocoder V** (Kraftwerk→Burial vocal-texture design). `research/links/vc-lofi-dx7-v-fm-glass-recipes.md`, `research/links/vc-lofi-vintage-keys-character.md`

## 6. Notable users / the Arturia-in-ambient angle (sourced)

The strong, citable thread is **producers using these as evolving-texture sources into
a post chain**, not specific-artist patch credits. The Vangelis *Blade Runner* CS-80
lineage is the one hard artist anchor (its own guide). `research/links/vc-nav-inside-the-box-producer-uses.md` Honest gap: no named shoegaze act tied to a specific V instrument — relevance is by technique.

## 7. Flagship sub-guides (deep dives beside this navigator)

- **CS-80 V4** → lush brass/pad walls, ribbon + poly-AT expression, copyable patches.
- **Mellotron V** → tape strings/choir/flute, Flutter/Saturation/Mechanics, shoegaze walls.
- **Synthi V** → pin-matrix drones, self-oscillating-filter walls, joystick animation.
- **Buchla Easel V** → West-Coast generative drones, random-voltage → Period, Gravity.
- **Emulator II V / CMI V** → 8/12-bit lo-fi sampling of your own gear.
- **Matrix-12 V2** → deepest evolving-texture machine; matrix self-modulation, keyboard-tracked self-osc filter, 24-osc wall, the Brecker single-note drone-chord trick.
- **Jup-8000 V** → supersaw walls (non-linear Detune/Mix), Feedback-osc drone, into Decapitator/Valhalla.
- **KORG MS-20 V** → self-oscillating-filter drones + the ESP rig-integration (banjo/reamp in) — **⚠️ AU-sidechain caveat in Logic; use the free Filter MS-20 effect instead**.
- **Augmented STRINGS / VOICES** → two-layer morphing texture/choir walls; Additive/Custom Morph; **freeze early (worst CPU in VC)**.

## 8. Captured sources (61 across 4 facets)

`vc-nav-*` (12): what's-new (×4 reviews), Analog Lab, common architecture, Logic/CPU,
reach-for/producer-uses, Synthi-drone + Jup-8000 pointers. `vc-pads-*` (16): CS-80
(×6) + Jup-8 / Matrix-12 / Prophet-VS / Prophet-5 / Solina. `vc-drone-*` (17): Synthi
(×4) + Buchla (×8) + ARP/MS-20/Modular/MiniFreak. `vc-lofi-*` (16): Mellotron (×4) +
EMU II (×4) + CMI (×3) + Synclavier/DX7/CZ/vintage-keys. (Full filenames in
`research/transcripts/` and `research/links/`, prefixed by facet.)

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first
line = the original URL). Primary: MusicTech / Sound on Sound / SynthAnatomy /
MusicRadar reviews, Arturia official tutorials + sound-design pages, CatSynth TV, One
Man And His Songs, Jon Audio, Reverb Machine. **Honesty flags:** Arturia's own support
"what's new"/Tips FAQ pages 403 automated fetch → triangulated across ≥4 independent
reviews (consistent on all material points); some deep courses (Sonic Academy, Groove3)
are paywalled (intros only); no named shoegaze artist verified.
