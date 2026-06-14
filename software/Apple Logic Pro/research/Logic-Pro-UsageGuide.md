# Logic Pro — Usage Guide

Logic is the **AU-only studio hub** for this rig — the assembly/studio end of a
hardware-front chain. Get the most out of it by treating it as three things at
once: a **reamp & hardware-commit station** (pedalboards, VG-800, Elektrons
in/out), a **stock-plugin drone/texture engine** (ChromaVerb Freeze, Space
Designer custom IRs, Sample Alchemy granular), and a **degrade box** (Tape Delay
and Bitcrusher as saturators) — all before you ever reach for a third-party
plugin. Lead with the stock tools; they hit this aesthetic with zero
AU-validation risk.

## 1. Essential workflows

**Reamping the pedalboard — two methods.**
- *Print-then-reamp (simplest):* record the **DI first** with amp sims while
  tracking (edit/comp on clean transients — far easier than editing distorted
  waveforms). To reamp: bypass the DI track's plugins, pan center, enable
  **Low-Latency Monitoring**, add a **pre-fader Send → physical Output** (drop it
  ~3 dB), wire that out → **Radial X-Amp** → board → mic the return to new
  tracks. Drop a **sharp click on the DI before the song** so you can nudge the
  reamped take back into sample-alignment afterward. `research/transcripts/reamp-musictechhelpguy.md`, `research/links/lug-reamping-di-to-hardware.md`
- *I/O plugin (cleaner, with auto-latency):* insert **Utility → I/O** on the
  track, set Output→interface outs feeding the pedal and Input→the return.
  **Click Ping** to auto-measure round-trip latency (Logic compensates). Output
  Volume gain-stages *into* the hardware, Dry/Wet blends. **Re-Ping after every
  repatch** or you get comb-filtering. `research/transcripts/io-plugin-analog-gear.md`, `research/links/io-plugin-reamp-ping-latency.md`

**Committing hardware (the silence gotcha).** An **offline** Bounce-in-Place of
an I/O-plugin track produces **silence** — hardware needs real-time playback.
Print either per-track (pre-fader Send → bus → new audio track, record live) or
whole-mix (**File → Bounce → Mode: Real-Time**). `research/transcripts/io-plugin-analog-gear.md`, `research/links/freeze-vs-bounce-in-place-cpu.md`

**Recording the Elektrons multitrack.** Digitakt 2 supports **Overbridge**: add
it as a **multi-output (10-out, stereo) software instrument**, Option-click Bus 1
to auto-assign buses, then relay each bus into an **audio track** (Logic can't
record straight into a bus). On the box: USB Config → Overbridge, untick
per-track sends to Main but leave Delay/Reverb on Main (that becomes the FX
return). **Octatrack MkII has no Overbridge/USB-MIDI** — sync via 5-pin DIN
clock and record its analog outs as plain audio. `research/transcripts/elektron-multitrack-logic.md`, `research/links/elektronauts-digitakt-overbridge-logic-multitrack.md`, `research/links/elektronauts-logic-digitakt-clock-start.md`

**The stock ambient-guitar chain** (banjo-as-lead / baritone walls, zero
third-party): DI → **Squash** (comp, sustain) → **Enveloper** (slow attack =
auto-swell) → **Amp Designer** (AC30 + Alnico cab) → **Delay Designer** (one
~9.5 s tap, high feedback, internal HP/LP) → **Stereo Delay** (quarter-note,
~12% L/R deviation, ~14% crossfeed) → **Chorus "D" mode** (= Roland Dimension D)
→ **ChromaVerb** (Room, decay 1.1→14 s) → glue **Compressor**. `research/transcripts/ambient-guitar-logic.md`

**ChromaVerb Freeze clouds** (the stock "Big Sky"). On an aux: **Tape Delay
first** (quarter-note, light feedback) to offset the bloom → ChromaVerb **Dark
Room**, long decay → hit **Freeze** to hold an infinite tail. Automate Freeze in
**Latch**; *when* you freeze changes the cloud (early = full, late = thin). `research/transcripts/chromaverb-freeze.md`, `research/links/chromaverb-spacedesigner-ambient-freeze.md`

**Sample Alchemy granular drones / drag-to-sample.** Drag any region (or
recorded hardware take) onto the **track header → Sample Alchemy** — instant
resample, no bounce. Granular mode, grain **5–20 ms** (wash) or **50–100 ms**
(fragments), modulate **Position with a slow LFO 0.1–0.5 Hz** to evolve; Bow/
Scrub for sustained tones; Motion-record live moves; layer 4 sources. `research/transcripts/sample-alchemy-explained.md`, `research/links/sample-alchemy-granular-drones.md`

**Space Designer custom IRs.** Drag **any audio file** in as the impulse — a
pedalboard tail, a field recording, a banjo pluck. Best when **same key**
(controlled resonances) and **same tempo**; set **Quality = Lo-Fi**, stretch
Length, **Reverse** for ghost echoes, "Synthesized IR" to mangle. `research/transcripts/space-designer-custom-irs.md`, `research/links/sos-space-designer-custom-ir.md`

## 2. Signature presets & settings (copyable)

**Shimmer reverb — octave-spiral (MusicTech).** Pre-fader send → **Pitch
Shifter** (+12 st, Mix 100%, Delay 60 ms, Crossfade 62%) → **ChromaVerb** "Greek
Wash," Decay **30 s**, Width 100%; feed the reverb output back through the pitch
shifter so each pass climbs an octave. Two **Tape Delays** ("1/4 Note Flutter,"
0/100 wet) panned hard L/R with different Flutter; keep the feedback bus < 0 dB. `research/links/musictech-ambient-shimmer-pads.md`

**Shimmer — Paul White / SOS (with filter freqs).** Send → **Opto Comp** (~6 dB
GR) → **Pitch Shifter** (+12 st, +3 cents, Mix 60%; alt +7 / −5 / −12) → **Tape
Delay** (HP 580 Hz, LP 1.6 kHz) → **SilverVerb** (Size/Reflectivity max, low-cut
~900 Hz, hi-cut >3–4 kHz, 100% wet, Density 60–70%) → **Ensemble** "Vintage
Dimension." `research/links/sos-shimmer-reverb-paul-white.md`

**ChromaVerb drone settings.** Long wash: **Reflective Hall**, Decay 14–30 s,
Width 100%, Wet 100. Modulated pad: **Dense/Strange Room**, Mod Speed 3.90 Hz,
Mod Depth 40. Infinite: automate **Freeze**. `research/links/chromaverb-ambient-room-types.md`

**Stock tape/lo-fi degrade.** **Bitcrusher** as parallel saturation: Mix ~18%,
Resolution 8-bit (heavy) / 12-bit (vintage-sampler), drive hard. **Tape Delay as
a saturator** (no echo): Dry 0 / Wet 100, **Tempo Sync off, time 0 ms**, then use
Character (head modes + Spread), Flutter, and the **LFO "tape drift"** for washy
pitch movement. **Compressor as saturator:** Ratio 1:1, push Makeup Gain, pick
the **Soft → Hard → Clip** distortion model. `research/transcripts/tape-saturation-logic.md`, `research/links/stock-tape-saturation-lofi-phatfx.md`

## 3. Power-user tips, tricks & hidden features

- **Quick-sample the rig in:** drag audio onto the **track-header list** (not the
  timeline) → Logic builds a Sampler / Drum Machine Designer / Alchemy instrument
  from it. Fastest path from a recorded banjo/pedalboard take to a playable
  instrument. `research/links/sos-logic-hidden-features.md`
- **External Instrument + audio input on one track** — play the VG-800/Elektron-
  as-synth like a VI (MIDI out + audio return + plugins on the return), commit
  via Realtime Bounce. `research/links/musictech-hardware-synths-external-instrument.md`
- **Virtual MIDI controllers in the Environment** (Layer → Multi-instrument →
  faders → CC/SysEx) to drive knobless/deep-SysEx hardware like the VG-800. `research/links/musictech-hardware-synths-external-instrument.md`
- **MIDI Chase Notes** so long sustained drones still sound when you drop the
  playhead mid-note. `research/links/sos-logic-hidden-features.md`
- **Plug-in Manager colon-naming** (`Synth:Analog`) folds a big AU collection
  into sub-menus; **import plugin chains** from another project via Browser →
  Project icon → All Files (build a "drone starter" chain once, reuse it). `research/links/sos-logic-hidden-features.md`
- **Low Latency Mode** (Options) auto-bypasses any plugin adding >~0.5 ms so you
  can track through a heavy chain; toggle off for playback. `research/links/low-latency-mode-monitoring-buffer.md`

## 4. Notable users & techniques

Honest framing: **clean, sourced "makes ambient records in Logic" attributions
are scarce** — that scene skews Ableton + Max/MSP, and the big "famous Logic
users" lists are pop/EDM and largely unsourced. So lead with *techniques*, not
name-drops:
- **Hammock** — documented **12+-layer guitar wall, double/triple the lead**
  (Guitar World): the clearest real blueprint for this aesthetic, reproducible
  via Summing Track Stacks + the reverb recipes. (Technique reference; no source
  names their DAW.) `research/links/hammock-ambient-layering-reference.md`
- **Dual-print + Q-Lock edit** — record a wet amp and a parallel clean DI, then
  Group and **Edit-Group Q-Lock** to quantize the transient-less distorted track
  off the DI's transients. The stock answer to editing degraded/distorted takes,
  and a reamp path. `research/transcripts/record-shoegaze-guitar-bass-logic.md`
- **Tim Hecker** — *forum-sourced, partial*: reportedly uses Logic only to
  **compile** final results, designing in Max/MSP + Audiomulch. Don't state he
  "produces in Logic." Eno/Björk appear on listicles but are **unverified**. `research/links/artists-logic-ambient-shoegaze-honesty.md`

## 5. Rig-specific recipes (your gear by name)

- **Reamp path:** I/O plugin out → **Apollo x8** line out → **Radial X-Amp**
  (impedance bridge) → board / **VG-800** → back into the Apollo; **re-Ping**
  after every repatch. `research/links/io-plugin-reamp-ping-latency.md`
- **Digitakt 2** stems via Overbridge multi-out relay; **Octatrack MkII** = DIN
  clock + record analog outs as audio (no stems). `research/links/elektronauts-digitakt-overbridge-logic-multitrack.md`
- **MIDI clock out** to Digitakt/OT/MPC: Project Settings → Synchronization →
  MIDI → tick **Clock** per destination; per-destination **Delay[ms]** nudges a
  dragging box; Clock Mode = Pattern (Elektron) or Song/SPP. Expect tiny 24-ppqn
  drift when Logic is master. `research/links/apple-sync-midi-clock-external-hardware.md`
- **Sample the banjo/pedalboard in** via the track-header drag → Sampler / Sample
  Alchemy; turn recorded pedalboard tails into **Space Designer IRs**. `research/links/sos-logic-hidden-features.md`, `research/transcripts/space-designer-custom-irs.md`
- **Apollo x8 + RME Babyface together (Aggregate Device):** latency drops to the
  slower interface and a **clock-master conflict causes intermittent crackle** —
  designate one clock master, or run one interface per session. Monitor
  zero-latency through **UA Console / RME TotalMix**, Logic software-monitoring
  off. `research/links/aggregate-device-templates-gotchas.md`, `research/links/low-latency-mode-monitoring-buffer.md`
- **Drone session template:** one sustained source → **3–4 pre-fader sends**,
  each a different processor (e.g. ModeAudio's 4-bus Space-Designer fan-out, one
  IR reversed, de-synced tremolo panning per bus). `research/links/modeaudio-ambient-drones-send-buses.md`, `research/links/loopmasters-background-drone-design.md`

## 6. Best learning resources

- **Why Logic Pro Rules (Chris)** — the deepest routing/integration content; the
  I/O-plugin video is the single best hardware-commit reference.
- **Jono Buchanan Music** — thorough stock-plugin deep-dives (ChromaVerb Freeze,
  Sample Alchemy, Beat Breaker, Delay Designer, Ringshifter). Best for the
  drone/texture angle.
- **Chords of Orion (Bill Vencel)** — ambient *guitar* through Logic stock
  plugins; the closest aesthetic match for banjo/baritone walls.
- **MusicTechHelpGuy** — the clearest reamp tutorial + Logic 11 essentials.
- **Production Expert / Eli Krantzberg, Sean Divine** — concise pro tips and
  stock-plugin saturation/tape tricks.
- **Forums:** Logic Users Group, Elektronauts (hardware sync), KVR (AU
  validation reality), Sound on Sound (shimmer/IR builds), r/Logic_Pro.

## 7. Common pitfalls / gotchas

- **AU-only host:** VST/VST3/AAX are ignored. The whole current inventory
  (Komplete, Kontakt, Arturia, Soundtoys, Spitfire, Antares, Valhalla, Neural,
  Goodhertz, Melodyne) ships **AU**, so no casualties today; **Ableton Live 12
  Lite is the fallback** for any future VST-only purchase. `research/links/au-only-validation-troubleshoot.md`
- **AUv2 detection is broken at the OS level** (devs confirm on KVR): newly
  installed AUs often need a **reboot** to appear. Fix order: relaunch → reboot →
  Plug-in Manager Reset & Rescan → delete
  `~/Library/Caches/com.apple.audiounits.cache` → "Open Anyway"/"use anyway"
  override. Apple Silicon vs Rosetta launch mode also changes what validates. `research/links/kvr-au-validation-reality.md`
- **Offline bounce of an I/O-plugin (hardware) track = silence** → use Real-Time
  bounce / bus-record. `research/links/freeze-vs-bounce-in-place-cpu.md`
- **Reamp latency is unavoidable** (double AD/DA) — compensate, re-Ping after
  repatch.
- **MIDI clock isn't sample-accurate** — expect tiny tempo drift as master.
- **Aggregate Device clock conflict → crackle**; pick one clock master.
- **Freeze:** Source Only (lighter, inserts stay editable) vs Pre Fader (whole
  chain, max CPU relief); **extend the region before freezing** so long reverb
  tails aren't truncated. **Summing** stacks = real bus; **Folder** stacks =
  organization only (no FX bus). `research/links/freeze-vs-bounce-in-place-cpu.md`, `research/links/track-stacks-summing-vs-folder.md`
- Reach for **stock Tape Delay / Bitcrusher / Phat FX before SketchCassette /
  RC-20** — same aesthetic, zero AU-validation risk. `research/links/stock-tape-saturation-lofi-phatfx.md`

## 8. Captured sources

**Transcripts (9)** — `research/transcripts/`: reamp-musictechhelpguy ·
io-plugin-analog-gear · elektron-multitrack-logic · ambient-guitar-logic ·
chromaverb-freeze · sample-alchemy-explained · space-designer-custom-irs ·
tape-saturation-logic · record-shoegaze-guitar-bass-logic.

**Links (27)** — `research/links/`: reamp & hardware (lug-reamping-di-to-hardware,
io-plugin-reamp-ping-latency, low-latency-mode-monitoring-buffer,
aggregate-device-templates-gotchas, musictech-hardware-synths-external-instrument,
apple-sync-midi-clock-external-hardware, elektronauts-digitakt-overbridge-logic-multitrack,
elektronauts-logic-digitakt-clock-start) · stock-plugin/drone
(chromaverb-ambient-room-types, chromaverb-spacedesigner-ambient-freeze,
sample-alchemy-granular-drones, sos-space-designer-custom-ir,
delay-sample-alchemy-textures, modeaudio-ambient-drones-send-buses,
loopmasters-background-drone-design, transition-studio-stock-plugins,
stock-tape-saturation-lofi-phatfx, musictech-ambient-shimmer-pads,
sos-shimmer-reverb-paul-white) · workflow/CPU (freeze-vs-bounce-in-place-cpu,
track-stacks-summing-vs-folder, sos-logic-hidden-features) · AU/host
(au-only-validation-troubleshoot, kvr-au-validation-reality) · templates/artists
(logic-templates-shoegaze-darkambient, hammock-ambient-layering-reference,
artists-logic-ambient-shoegaze-honesty).

## Sources

All claims above cite a captured file in `research/transcripts/` or
`research/links/` (each file's first line is the original URL). Primary video
channels: Why Logic Pro Rules, Jono Buchanan, Chords of Orion, MusicTechHelpGuy,
Sean Divine. Primary text sources: Logic Users Group, Elektronauts, KVR, Sound
on Sound, MusicTech/MusicRadar, Apple Support Communities.
