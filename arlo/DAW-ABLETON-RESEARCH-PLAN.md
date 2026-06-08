# ARLO DAW Stream — Ableton Live 12 Research Plan

A targeted research pass that teaches ARLO Ableton Live as it actually ships in 2026. The general corpus already covers DAW-agnostic production technique (EQ, compression, song form, etc.); this stream adds the *Ableton-specific* layer — what each stock device does, which Live-12-only features changed the workflow, the production patterns that emerge from Ableton's signal flow, and the timeless techniques that working producers still reach for after 15+ years on the platform.

The target is **the current shipping version of Live (12.x as of 2026-05).** Many existing online tutorials describe Live 9 / 10 / 11 workflows that are now subtly wrong — devices have been replaced, modulators changed sidechain conventions, the Delay device was unified, Hybrid Reverb arrived, and Live 12 added scale-aware MIDI, generators/transformations, and three new synths (Drift, Meld, Granulator III). Stale information here is worse than no information.

---

## Sourcing philosophy

Same tiering as the aesthetic and albums streams. Specific to DAW research, **version-stamping is mandatory** — every cited tutorial or article must name the Live version it was produced in, and pre-Live-12 content must be verified against the current manual before claims are written.

| Tier | Source type | Why it's useful |
|---|---|---|
| **S** | Ableton's official Live 12 Reference Manual + Live 12 Release Notes | The single canonical source — version-correct by definition. Always prefer over creator interpretation. |
| **S** | Ableton's Learn Live video series (official) with timestamps | Authoritative on workflow intent. Cite with the specific timestamp where the move is demonstrated. |
| **A** | Ableton Loop talk transcripts (Ableton's own conference) | Long-form workflow discussion by working producers. Strong for production-pattern files. |
| **A** | Sound on Sound's Ableton-specific columns and reviews | Mature production-journalism coverage going back to Live 8 — well-cited, slow-decay. |
| **A** | Version-stamped creator tutorials from established voices (Mad Zach, Slynk, Mr. Bill, Tom Cosm, Ill Gates, Andrew Huang, Ned Rush, Jonas Aden, Ableton Certified Trainers) | Concrete moves, with the Live version visible on screen. |
| **B** | MusicRadar, Attack Magazine, Reverb Machine, Splice, Production Music Live tutorials | Concrete how-to content, generally well-cited; verify the Live version before quoting numerics. |
| **B** | Push 3 documentation; Push-specific tutorials from Mad Zach et al. | Authoritative for the standalone-Push workflow files. |
| **C** | Ableton forums and r/ableton threads | **Triangulation only.** Use to find a verifiable source — never cite a forum post as the source. |
| **NOT** | AI-generated tutorial sites, generic listicles, plugin-marketing content, 2019-or-older tutorials describing Live-current features | Filler. Often actively wrong about Live 12. |

The **anti-hallucination master rule** from the existing streams holds verbatim: *"If you cannot verify a specific number, setting, technique, or attribution with web research, OMIT it. Do not guess."* In this stream there is an additional rule: **if a tutorial source predates Live 12 and you cannot verify the technique still works in Live 12, omit it or flag it inline as `⚠ verify against Live 12 manual`.** Made-up device parameters, wrong default-state claims, or features attributed to the wrong Live version are the failure modes most likely to poison retrieval here.

---

## The taxonomy — 9 areas, ~62 corpus files

Each row produces one focused markdown file under `corpus/daw/ableton/{area}/{filename}.md`. Word target per file is 1500–2500 words (same chunk shape as the general corpus). All files end with the standard Cited Retrieval Topics + Sources footer.

### A. Fundamental Workflows (7 files) — `corpus/daw/ableton/workflows/`

The things every Live user does on every session. Files here are foundational; everything in B/D/E builds on them.

| # | Filename | Why this file exists |
|---|---|---|
| A1 | `session-vs-arrangement-view` | The Session/Arrangement split is Live's defining feature. Most Logic/Pro Tools converts misread when to use which. |
| A2 | `track-types-audio-midi-return-group` | Track-type gotchas (e.g., Return tracks can't be sidechain destinations, Group track delays are odd) are constant new-user friction. |
| A3 | `routing-input-output-sends-sidechain` | Routing is the single most-asked Live question — input/output menus, sends, "audio from" routing tricks. |
| A4 | `recording-workflows-loop-comp` | One-take, loop-record, and Live 11+ takes-lane comping — when each is appropriate. |
| A5 | `clip-launching-and-follow-actions` | Session-view performance and generative-arrangement core. Live 12 added new Follow Action behaviors. |
| A6 | `freeze-flatten-consolidate-bounce` | The CPU-and-commitment toolkit. Live 12 simplified this with Bounce-in-Place. |
| A7 | `instrument-racks-effect-racks-macros` | Racks are how every shipped Live preset is built. Macro mapping, chain selectors, MIDI/key zones. |

### B. Stock Devices (11 files) — `corpus/daw/ableton/devices/`

One file per device family, each covering what the device does, its parameters, when to reach for it, and Live-12-specific changes. The "stock device" framing matters because Live ships ~50 devices and most users only know ~10 of them.

| # | Filename | Coverage |
|---|---|---|
| B1 | `eq-eight-and-eq-controls` | EQ Eight in depth; the simpler **Channel EQ** device (Live 10+) as the lightweight stock alternative; high-quality mode trade-offs. **Correction:** the original plan named a nonexistent "EQ Controls" device — the real stock options are EQ Eight, Channel EQ, and EQ Three. |
| B2 | `compressors-glue-multiband-drumbus` | Compressor (peak/RMS, OPTO/FET-style models), Glue Compressor, Multiband Dynamics, Drum Buss as a one-knob drum processor. |
| B3 | `reverbs-classic-and-hybrid-reverb` | The original Reverb device vs. Hybrid Reverb (Live 11+) — algorithmic + convolution hybrid; when to reach for which. **Note:** Hybrid Reverb has a continuous **Vintage** degradation parameter (Off → Extreme), not "Vintage/Modern modes" as the original plan implied. |
| B4 | `unified-delay-device` | The unified Delay device (Live **10.1+**, May 2019) replaced Simple Delay and Ping Pong Delay. **Three** modes — Repitch, Fade, Jump (the original plan listed a fourth "Insert" mode that does not exist). Sync, modulation, freeze. |
| B5 | `utility-modulation-autopan-autofilter-autoshift-gate` | Utility (where it should live in every chain), Auto Pan, Auto Filter, **Auto Shift (Live 12.1+, not 12.0)**, Gate. |
| B6 | `saturator-vs-roar` | Saturator (the classic) vs. Roar (Live 12 new) — when each fits, parallel/series Roar configurations. |
| B7 | `pedal-amp-cabinet` | Live's stock guitar-color chain. Often used on non-guitar sources for character. |
| B8 | `spectral-resonator-spectral-time-pitch-time-machine` | The spectral-processing family. Spectral Resonator/Time arrived Live 11; Pitch and Time Machine are the unsung utility plugins. |
| B9 | `operator-analog-synths` | Operator (FM workhorse) and Analog (subtractive). Patch-design primers, not full sound-design (that's in Timeless). |
| B10 | `wavetable-drift-meld-synths` | Wavetable (Live 10+), **Drift (Live 11.3+, bundled with Live 12 Suite as standard — small subtractive)**, Meld (Live 12+ — MPE-first dual-oscillator). |
| B11 | `sampler-simpler-drum-rack-granulator-3` | The sampling instrument family. Granulator III shipped with Live 12. |

### C. Live 12 Features (7 files) — `corpus/daw/ableton/live-12/`

The "latest and greatest" — features that did not exist in Live 11. This section is where stale online tutorials hurt the most.

| # | Filename | Coverage |
|---|---|---|
| C1 | `modulators-shaper-lfo-envelope-follower-note-modulator` | The Modulators rack — devices you place on a track that modulate *any* mapped parameter on that track. Single biggest workflow change in Live 12. **Correction:** "Note Modulator" does NOT exist as a shipped device. The MIDI-triggered modulation family is: Envelope MIDI, Shaper MIDI, Expression Control, MPE Control. The filename keeps the legacy "note-modulator" stub for retrieval continuity but the body debunks the false claim. |
| C2 | `scale-aware-midi-and-global-scale` | Live 12's project-wide Scale setting; per-clip scale; how every MIDI device respects scale. |
| C3 | `midi-generators-and-transformations` | The new MIDI Tools sidebar. **Generators (verified):** Stacks, Rhythm, Seed, Shape, Euclidean. **Transformations (verified):** Arpeggiate, Chop, Connect, Ornament, Quantize, Recombine, Span, Strum, Time Warp, Velocity Shaper; Live 12.1 added Glissando and LFO MPE. ("Arp" is *Arpeggiate*, a transformation, not a generator.) |
| C4 | `tuning-systems-and-microtonal-support` | Live 12 added .scl/.ascl scale-file import and **per-project tuning** (not per-device as the original plan said) — first-class microtonal support. |
| C5 | `stem-separation` | **Stem Separation arrived in Live 12.3 (November 25, 2025), not 12.1.** Browser-native, four-stem output (Vocals/Drums/Bass/Others). Workflow, quality limits. |
| C6 | `push-3-standalone-workflow` | Push 3 in standalone mode is a Live-12 instrument. Browser workflow, project transfer, current limits vs. tethered mode. |
| C7 | `live-12-point-releases-changelog` | 12.1 / 12.2 / and later — pull only verified additions from Ableton's release notes. This file is the changelog file specifically. |

### D. Production Patterns in Live (7 files) — `corpus/daw/ableton/patterns/`

Recipes that live above the device level. These are the highest-leverage files for retrieval because they're how users phrase their questions ("how do I do a vocal chain in Live", "how do I do parallel comp in Live").

| # | Filename | Coverage |
|---|---|---|
| D1 | `parallel-compression-in-live` | The NY-drum / Motown parallel chain implemented in Live — Return track architecture, the dry/wet alternative on a single Compressor. |
| D2 | `sidechain-ducking-classic-vs-modulator` | Stock Compressor sidechain (the classic way) vs. Envelope Follower modulator (the Live-12 way). When each fits. Cross-link to I8 Timeless classic-sidechain file. |
| D3 | `vocal-chains-in-live` | The HPF → de-ess → comp → EQ → saturation → reverb-send chain implemented with Live stock devices. |
| D4 | `drum-bus-chains-in-live` | Drum Buss + Glue + Saturator chains; the parallel-Drum-Buss trick. |
| D5 | `mix-bus-and-2bus-chains-in-live` | Master-track conventions; Glue + Tilt EQ + Limiter; the case for/against mastering inside Live. |
| D6 | `mastering-in-live-and-its-limits` | When Live IS the right mastering host (album-of-Live-sessions, in-the-box workflow) and when it's not (true 2-pass mastering, DDP delivery). |
| D7 | `sound-design-with-stock-synths` | Concrete patches across Operator / Wavetable / Drift / Meld. Cross-link to I16 Timeless Operator FM file. |

### E. Comping and Editing (4 files) — `corpus/daw/ableton/editing/`

| # | Filename | Coverage |
|---|---|---|
| E1 | `comping-in-live-11-plus` | The takes-lane comping workflow. Crossfades, lane order, comp-to-arrangement. |
| E2 | `warp-modes-by-ear` | Beats, Tones, Texture, Re-Pitch, Complex, Complex Pro — what each sounds like, audible artifacts, when to use which. |
| E3 | `warping-discipline` | Warp marker placement, transient detection, warping a mix in vs. warping to a tempo map, anti-warping (Warp off + Re-Pitch). |
| E4 | `slicing-audio-to-midi` | Slice to MIDI / Slice to Drum Rack — modes (Warp, Transients, Beat, Region), sensitivity, manual marker placement. Cross-link to existing general-corpus `chopping-resampling-and-warping.md`. |

### F. Practical Frictions and Recovery (5 files) — `corpus/daw/ableton/friction/`

The diagnostic files. Often searched by users in trouble — these are some of the highest-retrieval-value files in the stream.

| # | Filename | Coverage |
|---|---|---|
| F1 | `silent-track-diagnostic-flow` | "Why is my track silent" decision tree: monitoring state, arm state, routing, send-only, mute solo, frozen track, AU/VST scan errors. |
| F2 | `monitoring-loop-fixes` | The In/Auto/Off monitoring matrix; killing feedback loops when tracking with effects on. |
| F3 | `latency-pdc-gotchas` | Live's plugin delay compensation, Reduced Latency When Monitoring mode, external-hardware send-and-return latency. |
| F4 | `cpu-optimization` | Freeze vs. flatten vs. bounce-in-place; Reduce Disk Overhead settings; Warp-mode CPU cost; Hyper-Threading toggle on macOS. |
| F5 | `project-crash-recovery` | Auto-saves, Backup folder, recovering from a corrupted .als, undo-history retention across sessions. |

### G. Keyboard Shortcuts (1 file) — `corpus/daw/ableton/reference/`

| # | Filename | Coverage |
|---|---|---|
| G1 | `keyboard-shortcuts-reference` | Flat, citation-rich shortcut list. macOS + Windows where they differ. Pull from Ableton's official shortcut documentation. |

### H. Logic Parity Map (1 file) — `corpus/daw/ableton/reference/`

| # | Filename | Coverage |
|---|---|---|
| H1 | `ableton-to-logic-parity-map` | For each Ableton concept above (Session view, Drum Rack, EQ Eight, Hybrid Reverb, modulators, follow actions, etc.), the Logic Pro equivalent — or `(no direct equivalent)`. Sets up the future Logic stream and keeps ARLO's Live instructions translatable when the user is on Logic. |

### I. Timeless Techniques (19 files) — `corpus/daw/ableton/timeless/`

Pre-Live-12 producer wisdom that is still bedrock. Every technique in this section **must be verified to still work in Live 12** before inclusion. Cite both the original creator (with the Live version stamped) and the Live 12 verification source (manual section or current tutorial). When a newer Live-12 tool partially supersedes the technique, the file should show both with notes on when to reach for which.

| # | Filename | Coverage |
|---|---|---|
| I1 | `resampling-discipline` | Record into a new audio track, then manipulate. The single most-used producer technique in Live. |
| I2 | `audio-to-midi-extraction` | Convert Audio to MIDI (Drums / Melody / Harmony) — Live-9 vintage, still the fastest way to lift a groove or chord from a reference. |
| I3 | `groove-pool-and-extracted-grooves` | Extract a swing/pocket from one clip, apply to others. Groove Pool, commit-groove-to-clip workflow. |
| I4 | `beat-repeat-stutter-and-glitch` | The Beat Repeat device for stutter and glitch edits — classic Live sound. |
| I5 | `drum-rack-as-multizone-instrument` | Drum Rack used as a multi-zone playable instrument (not just for drums) — chain selectors, velocity ranges, key zones. |
| I6 | `instrument-and-effect-racks-macro-mapping` | The macro-mapping discipline that underlies every Live preset. Min/max ranges, curve, the eight macros, MIDI-mapping macros to a controller. |
| I7 | `reamping-through-pedal-amp-cabinet` | Re-amping synth or DI sources through Live's stock guitar chain for character. |
| I8 | `classic-compressor-sidechain-ducking` | The stock Compressor's sidechain input fed from a kick — the bread-and-butter ducking trick that predates the Envelope Follower modulator by a decade. Cross-link to D2 Production-Patterns sidechain file. |
| I9 | `send-return-as-parallel-bus` | Using a Return track as a parallel processing bus (parallel comp, parallel saturation, reverb-only bus). Older than Live itself; defines how Live's signal flow works in practice. |
| I10 | `velocity-randomization-and-humanization` | Velocity randomization patterns for humanization on MIDI tracks; classic Random + Velocity device pairings. |
| I11 | `classic-midi-effect-chains-scale-random-notelength` | Scale → Random → Note Length stacks for generative melodic patterns. Useful contrast with C3 Live-12 MIDI generators. |
| I12 | `live-as-looper-and-performance-instrument` | Clip launching, follow actions, scene-based song construction — Live's original pitch and still a working performer's reason to choose Live. |
| I13 | `eight-bars-first-discipline` | The loop-based pre-production school (Tom Cosm / Ill Gates). How to know when to break out of it into Arrangement view. |
| I14 | `bounce-in-place-commit-discipline` | When to commit a sound (free CPU, lock the decision) vs. keep flexibility. The producer-judgment file complementing A6's technical-mechanism file. |
| I15 | `frequency-shifter-and-ring-modulator-sound-design` | Sound design via Frequency Shifter and Ring Modulator — clangy / metallic / inharmonic transformations. |
| I16 | `operator-fm-sound-design-fundamentals` | The Operator FM patches that show up in everyone's projects (e-piano, bell, FM bass) and why. Cross-link to B9. |
| I17 | `wavetable-mpe-workflow` | MPE-aware Wavetable patches (Live 10+ feature) — per-note pressure, slide, glide. |
| I18 | `drag-clip-onto-drum-pad-and-saving-personal-library` | Drag-a-clip-onto-a-Drum-Rack-pad as the fastest sample-load workflow; right-click "Save" of racks/chains/presets to build a personal Library of go-to patches over time. |
| I19 | `live-mixing-discipline-utility-everywhere` | Foundational Live mixing discipline: gain staging in-the-box, headroom budget, why Utility belongs almost everywhere, Master section conventions, color-coding tracks for navigation. |

---

## Cross-references to the existing corpus

Several existing general-corpus files touch Ableton already. The DAW stream should cross-link rather than re-research.

| Existing file | Overlap with DAW stream | Resolution |
|---|---|---|
| `corpus/sampling/chopping-resampling-and-warping.md` | Already Ableton-flavored: Slice-to-MIDI, Drum Rack workflow, warp modes, resampling | E4 and I1 cross-link via "See also" footer. Don't re-research the same material; DAW files go deeper on workflow and friction. |
| `corpus/sampling/loop-based-arrangement.md` | Mentions Session view briefly | A1 cross-links to it. |
| `corpus/rhythm/groove-construction-and-pocket.md` | DAW-agnostic groove principles | I3 cross-links to it. The DAW file focuses on Live's Groove Pool mechanism specifically. |
| `corpus/rhythm/drum-programming-by-genre.md` | DAW-agnostic drum programming with Ableton as a cited manual | No conflict — DAW files don't re-cover genre conventions. |
| `corpus/synthesis/subtractive-synthesis-fundamentals.md` | DAW-agnostic subtractive primer | B9, B10, I16 cross-link to it for the conceptual foundation. |
| `corpus/synthesis/fm-and-wavetable-synthesis.md` | DAW-agnostic FM/wavetable primer | I16, I17 cross-link to it. |

The pattern: existing files cover the DAW-agnostic concept; new DAW-stream files cover the Ableton-specific implementation. ARLO retrieval gets both layers.

---

## Verified Live 12 release timeline (cite this in all version claims)

| Version | Release date | Highlights |
|---|---|---|
| Live 12.0 | March 5, 2024 | Modulators (Shaper/LFO/Envelope Follower), scale-aware MIDI, MIDI Generators & Transformations, tuning systems, Meld, Roar, Granulator (initial), browser/Library overhaul |
| Live 12.1 | October 8, 2024 | Auto Shift, Glissando transformation, LFO MPE transformation, slicing-preset redesign |
| Live 12.2 | June 11, 2025 | **Bounce Track in Place** (supersedes Freeze-and-Flatten), Auto Pan/Tremolo redesign, Auto Filter redesign |
| Live 12.3 | November 25, 2025 | **Stem Separation**, Granulator III, GPU acceleration (macOS 26.4+), Time-Selection stem split, Merge Stems |
| Live 12.4 | May 5, 2026 | Current at time of writing |

## Things that DO NOT exist in any shipped Live 12 release (debunked claims)

- **Note Modulator** as a device — the real MIDI-triggered modulation family is Envelope MIDI, Shaper MIDI, Expression Control, MPE Control
- **EQ Controls** as a device — the real lightweight stock EQ is Channel EQ (Live 10+)
- **A fourth "Insert" mode on the unified Delay** — there are exactly three modes (Repitch, Fade, Jump)
- **"Vintage/Modern modes" on Hybrid Reverb** — Vintage is a continuous degradation parameter (Off → Extreme), not a mode chooser
- **Native LUFS meter inside Live** — none ships; users still need Youlean or similar
- **DDP export** — not supported; hand off to Wavelab or similar for album mastering

## Anti-hallucination notes — Live-version-specific

In addition to the master anti-hallucination rule, this stream has version-specific traps to flag in every prompt:

1. **Hybrid Reverb is Live 11+.** Pre-Live-11 tutorials show only the older Reverb device. Do not retrofit Hybrid Reverb claims into older content.
2. **The unified Delay device is Live 11+.** Older tutorials reference Simple Delay, Filter Delay, Ping Pong Delay as separate devices. They still exist as Legacy but the unified Delay is the modern reach.
3. **Modulators are Live 12+.** Shaper, LFO, Envelope Follower, and Note Modulator as track-level modulators of *any* parameter did not exist in Live 11. Pre-Live-12 tutorials show LFO Tool / Max-for-Live LFO as workarounds — do not present those as the modern way.
4. **Scale-aware MIDI is Live 12+.** Global Scale and per-clip Scale did not exist in Live 11. The MIDI Tools sidebar (Generators / Transformations) is also Live 12+.
5. **Drift, Meld, Roar, Auto Shift, Granulator III are Live 12+.** No retrofitting these into Live-11 tutorials.
6. **Stem separation is Live 12.1+ (not in 12.0).** Confirm point-release before claiming.
7. **Push 3 standalone is its own product.** Tethered Push 3 is a different workflow file from standalone. C6 covers standalone specifically.
8. **macOS-vs-Windows shortcut differences must be cited per shortcut.** A flat list that says "Cmd-Shift-T" without the Ctrl-Shift-T Windows pair is not acceptable in G1.

Any prompt that asks for a feature claim should require the agent to verify against the **Live 12 Reference Manual** as the primary source. Pre-Live-12 creator tutorials are valid sources for the Timeless section (I), but only with version-stamping AND a Live-12 verification citation.

---

## Target file count

| Area | Files |
|---|---|
| A. Fundamental Workflows | 7 |
| B. Stock Devices | 11 |
| C. Live 12 Features | 7 |
| D. Production Patterns | 7 |
| E. Comping and Editing | 4 |
| F. Practical Frictions | 5 |
| G. Keyboard Shortcuts | 1 |
| H. Logic Parity Map | 1 |
| I. Timeless Techniques | 19 |
| **Total** | **62** |

At ~1500–2500 words per file and ~8–15 retrieval chunks per file, the DAW: Ableton stream produces an estimated **~600–900 chunks** in `corpus/daw/ableton/`.

---

## Tagging conventions for the stream

Every file in this stream gets at minimum these tags:

- `daw-ableton` (the stream marker — retrievable as "in Ableton" / "Live")
- `live-12` (year-current marker — distinguishes from older content)
- Area tag: `workflow`, `device`, `live-12-feature`, `production-pattern`, `editing`, `friction`, `reference`, or `timeless`
- Topic-specific tags as appropriate (`sidechain`, `vocal-chain`, `drum-bus`, `comping`, `warping`, `fm-synthesis`, etc.)

The Timeless section additionally carries `daw-ableton-timeless-*` for filtering when ARLO needs to favor old-but-verified techniques (e.g., when the user asks for a "classic" Live workflow).

---

## What this stream does NOT cover

Out of scope, by user instruction:

- **Windows.** Stream targets macOS Live 12.x only. Where macOS and Windows shortcuts/paths/frictions diverge, give the macOS form. A future Windows-parity pass can branch from these files later.
- **`.als` file format internals.** Separate technical-reference research; lives in patchbay-ai, not ARLO.
- **Max for Live device-building and the Live Object Model (LOM).** Separate technical-reference stream. But — factory M4L devices that ship bundled with Live and behave as built-in (Convolution Reverb Pro, the LFO/Envelope MIDI devices, the older Granulator, Pitch Hack, Buffer Shuffler) ARE in scope when idiomatic to a workflow. Cite them with their bundled-pack name (e.g., "Max for Live Essentials → Convolution Reverb Pro").
- **Push 1 and Push 2.** Push 3 (standalone and tethered) is covered in C6. Older Push hardware is deferred to a future hardware-controllers stream.
- Third-party plugin walkthroughs.
- Genre-conventions (covered DAW-agnostically in the general corpus rhythm/structure files).

The DAW stream is *Ableton Live as ARLO uses it to advise a producer mid-session on macOS.* Internals and Max programming are a different audience.
