# Eventide H90 — Usage Guide

The H90 is the End board's algorithm powerhouse and the rig's **sustained-wall engine** —
two algorithms per Program, 60+ to choose from, deep routing, and footswitch/MIDI control.
You get the most out of it three ways: design **dual-algorithm Programs** (not single
presets), use the **wet-only "super-algorithm" routing trick** to stack reverbs/pitch into
modulated walls without clouding the dry banjo/baritone, and put **Freeze/Warp on
footswitches** to hold and ring out drones. MIDI-clock it from the Digitakt so its
tempo-synced delays lock to the rig.

> Coverage note: the H90 launched 2022 and is well-documented. Some of the deepest
> algorithm walkthroughs (Leon Todd) were filmed on **H9** hardware — the algorithms are
> identical, flagged where it matters. A few community *settings* below came from
> fetch-blocked sites via search snippets (OffsetGuitars, GuitarChalk) — flagged as
> lightly-verified starting points, dial by ear.

---

## 1. Essential workflows

### The hierarchy & routing
- **List (`.lst90`, 99 Programs) → Program (`.pgm90`, two algorithm slots A + B) → Preset
  (one algorithm + params) → Algorithm.** Build in **User List 1** (ships as a duplicate of
  Factory; Factory is locked — fork presets by rename → save as User). *(preset-management)*
- **Two global routing modes:** **Insert** (default — A+B in series/parallel + up to 2 mono
  / 1 stereo insert loop for an external pedal) and **Dual** (two independent stereo paths,
  *no* inserts, and its own separate Playlist). *(official-part3, routing-rules)*

### Build a Program / HotSwitches / morphs
- **HotSwitches (3 per Program)** are an instant **parameter snapshot** — map a range of
  params across both Presets to one footswitch ("three extra Programs for free"). But they
  are a **hard jump and mutually exclusive** (HS2 cancels HS1; no stacking). *(hotswitch-mutually-exclusive)*
- **For gradual morphs use the HotKnob or an expression pedal** — gang **HotKnob A + B onto
  HotKnob P** to sweep both Presets with one control; drive HotKnob P from an exp pedal
  (System → Global → Pedal Ctl) or a ramped MIDI CC (Morningstar / OBNE Ramper V2 work).
  *(hotswitch-gradual-changes, hotknob-morphing)*
- **Performance Parameters persist across HotSwitch toggles** — put latched moves (Freeze,
  Warp) there, not on a HotSwitch. *(perform-mode, hotswitch-mutually-exclusive)*
- **Two-footswitch limit, on-board fix:** press the **Perform knob a second time** for a
  second row of three functions (6 total). Off-board: the two EXP/CTL jacks take **6 aux
  switches** (TRS carries two per jack) → map to the HotSwitches in System → External
  Control. *(external-footswitch-aux, dr-guitar-hotswitch)*

### The wet-only "super-algorithm" trick (the key creative routing)
Set Preset **A Mix = 100%** so only its wet feeds Preset B; build the combined A→B wet
effect (e.g. Blackhole → MangledVerb), then blend the whole thing under a fully dry signal
with the global **Program Mix** (Kill Dry OFF). The dry banjo/baritone stays uncolored while
a modulated/degraded wall rings behind it. *(leon-todd-routing-trick)*

### Insert latency calibration (for a digital pedal in the loop)
Bypass other presets → invert insert **Polarity** → insert **Mix 50%** → set the looped
pedal dry-only → raise **Latency** (0–512 samples) until silent → disengage Polarity.
(Analog pedal = 0.) *(official-part1)*

### MIDI with the rig
- **Slave to the rig's clock:** Tempo menu **Source = MIDI clock**; pick DIN or USB. (Only
  DIN-*input* clock is forwarded downstream; USB clock isn't.) Per-preset **Tempo Sync**
  toggled with Presets+Parameters. Output **Transmit** = H90 masters; **Thru** = slaved and
  passes clock on (use Thru when mid-chain). *(official-part2, midi-clock-tempo-sync)*
- **Scene recall:** PCs load Programs (PC offset 0 = native, PC 1 → Program 1). The H90
  ships with **no default CC map — build your own.** Map a **CC to Active/Bypass** (64 = on,
  1 = off). Send **PC on press, CCs on release, hold ~1 s** so the Program loads before CCs
  land. *(midi-program-change-cc, morningstar-midi)*

---

## 2. Signature programs & settings

**Algorithm deep-dives (from the videos):**
- **Wormhole** ("Blackhole taken further") — ambient swell: **Warp Factor 10, Warp Mix 100,
  Stability DOWN** (more modulation), Length up, Low Decay down / High Decay up, ~65 ms
  pre-delay; assign **Warp to a latching footswitch** to hold and ring. *(leon-todd-wormhole)*
- **Polyphony** (SIFT, chord-capable — the banjo engine): organ = oct-down + oct-up, dotted-8th/
  quarter delays, panned, with feedback; "12 Stringy" = Voice 1 unison+detune, Voice 2
  oct-up+detune; POG-style = oct-down + a little oct-up; chaos = tritone both voices + feedback
  IN. *(leon-todd-polyphony)*
- **PrismShift** — chord → arpeggiated pitch-shifts: Arp Type/Order, Step Length, **Spread**
  full = L↔R panning arps, Feedback; great as a self-generating stereo bed over a drone.
  *(leon-todd-prismshift)*
- **Head Space** — 4-head tape delay; **Boil/Break** = tape speed-up runaway / power-down
  dive (assign to a HotSwitch for pitch-dives before the real tape stage). *(leon-todd-headspace)*

### Harmonizer+ vocal algorithms (the new "vocoder-like" suite — firmware v1.10, Apr 2025)
Four algorithms ported from the flagship **H9000**, free via H90 Control — pitch correction,
formant shifting, and up-to-4-voice diatonic harmony with scale recognition. **Feed them the
banjo/baritone, not just vocals.** *(harmonizer-plus-vocal)*
- **VocalTune** — quantizes pitch to a Root/Scale; **Tuning Speed** sweeps from robotic
  hard-tune to subtle correction (the auto-tune / "vocoder-like" knob the owner is after);
  **Formant** (±600 c) reshapes timbre *without* repitching; built-in EQ + compressor + gate.
  Crank Tuning Speed on a sustained baritone for the hard-tuned effect; back it off to gently
  lock the banjo lead.
- **VocalShift** — 3 voices, each with **Shift / Formant / Gain / Delay / Feedback / Pan**;
  **Formant Link** keeps harmonies natural; per-voice **Solo**, plus **Glide / Hold**
  performance controls. Harmonize a mono drone into a wide, scale-locked stereo chord.
- **VocalShiftMIDI** — 4 voices played from MIDI (the 61SL): set intervals from the keybed
  over a held note; **Freeze**, vibrato, **Spread**, velocity/bend.
- **Quadravox+** — 4-voice diatonic harmonizer with staggered delays + arpeggio feel.

**Copyable Program recipes** (community starting points — dial by ear):
- **Shimmer Pad Wash:** A = Blackhole (Size 90, Gravity Inverse, Feedback 40%, Mix 70%); B =
  PitchFuzz (+1 oct, Mix 50%); **parallel**; exp → reverb Mix 30–80%. *(h90-ambient-pad)*
- **Lo-fi Vinyl Space** (very on-aesthetic): A = LoFi (12-bit, Tape Hiss 40%, Flutter 60%, Mix
  70%) → B = Blackhole (Gravity −25, Feedback 70%, Size 90, Mix 65%); **series**. *(h90-ambient-pad)*
- **Shoegaze ModEchoVerb wall** *(lightly sourced)*: chorus mod, Mix 33, Decay 12.75 s, Size
  55, Delay 330 ms, Low EQ −2 / High EQ −5, EchoFdbk 47, ModRate 63, FlangeMix 67. *(shoegaze-slowdive)*
- **Subtle Shimmer:** +1 oct AND −1 oct, Decay 4–5 s, Mix ~25%. **Reverse Reverb** = instant
  shoegaze. **Pads to solo over:** Polyphony/PolySynth Freeze, or any reverb at INF/Freeze →
  map Freeze to a HotSwitch. *(h90-ambient-pad, freeze-drone-holds)*

**Where to get programs:** **Patchstorage (free, ~350+ Programs)** is the richest well — start
with **"Studio Box List"** (63 programs) and apalazzolo/brock/rustydutch ambient+granular
sets ("Mescalin Mix," "Sunken Bell At Black Nab," "GRANULATE"). Eventide's own Presets page +
paid packs (Worship Tutorials, Jake Fauber "TeddyTones"). **H90 Control reads H9 lists
directly**, so the whole H9 ecosystem transfers. Import via the Playlist ⋮ → Import Program /
Import List (into any list except Factory). *(patchstorage-studio-box, patchstorage-ambient, paid-packs, preset-management)*

---

## 3. Power-user tips, tricks & hidden features

- **HotSwitch as a surgical change:** it only moves the params you mapped — a reverb-mix
  HotSwitch leaves the tremolo untouched. *(hotswitch-mutually-exclusive)*
- **Freeze a wall and play over it:** Blackhole = **Feedback fully clockwise**; Polyphony /
  PrismShift have dedicated Freeze (PrismShift freezes High/Low but the **Mid voice stays
  live/playable**). Freeze persists independently of HotSwitch toggles. *(freeze-drone-holds)*
- **Imported H9 presets land as a Program with THRU in slot B** — a free second slot to add a
  reverb/pitch. Import is **blocked in Dual Mode**, needs **H90 Control v1.7.6+**, and
  expression maps must be reassigned by hand. *(import-h9-presets)*
- **Spillover across Programs:** routing/inserts aren't CC-mappable, so **clone a Program with
  different routing** and switch by PC; spillover bridges it. *(routing-rules)*
- **Mono-in → split A to outs 1/2, B to outs 3/4** using a stereo insert as a tap point
  (wet/dry/wet or two-amp). *(insert-loop-setups)*
- **Late-2025 granular firmware** (free): **Cosmic Web** (reverse-pitched grains + Eventide
  reverb), Glitch, GrainMod, Stutter — the standout for "recorded-wrong" texture. *(granular-firmware)*

---

## 4. Notable users & techniques

**Honest headline:** the H90 (2022) has **no documented signature drone/doom/shoegaze artist
program yet** — its mythology belongs to the *algorithms* (Eno + the H3000; Visconti/Bowie
"Heroes" + the H910). Most "how an artist uses it" detail is H9/Space lineage that transfers
directly. *(artists-and-techniques)*
- **Confirmed H90 users:** Tosin Abasi (mid-board, pitch + ambient over a clean platform),
  Vernon Reid, Andrew Huang. *(Yvette Young is only lightly sourced — her published board
  shows no Eventide; treat with caution.)*
- **Ariel Posen** (H9, documented) — names presets by *function* (Hall, distant-mic "Room,"
  ModFilter, Leslie) and keeps **failover copies** of other pedals' sounds. Same logic as the
  board-failover bank below. *(ariel-posen transcript)*
- **Pete Thorn** ran **two H9s** to use two Eventide effects at once — which is *literally* the
  H90's two-Presets-per-Program design. *(artists-and-techniques)*
- **On-aesthetic lineage to borrow from:** Robert Fripp (Frippertronics drone), Lee Ranaldo
  (Sonic Youth noise/drone), Jon Hassell (ambient), Kaitlyn Aurelia Smith. *(artists-and-techniques)*

---

## 5. Rig-specific recipes (using gear actually owned)

- **The End-board core move:** run **Blackhole / Shimmer / Wormhole at 100% Mix into
  MangledVerb** (or a mod/distortion algo), blend under the dry baritone/banjo with Program
  Mix → a degraded, modulated wall that doesn't cloud the fundamental — then print it to the
  downstream **PORTA424 / JHS 424** tape stage for the final "recorded-wrong" finish.
  *(leon-todd-routing-trick)*
- **Unstable-pitch sustained wall:** **Wormhole Warp on a latching Perform footswitch** over a
  held Hizumitas/baritone fuzz chord. *(leon-todd-wormhole)*
- **Banjo-as-lead chordal engine:** **Polyphony with Inst Type = Percussive** for banjo
  transients (oct ±1 + detune + pan = "12-string banjo"/organ pad); **PrismShift with full
  Spread + slow Step Length** over a drone = self-generating stereo arp. *(leon-todd-polyphony, leon-todd-prismshift)*
- **Tape-dive before the tape:** **Head Space Boil/Break** on a HotSwitch for pitch runaways
  ahead of the actual PORTA424 stage. *(leon-todd-headspace)*
- **Sync to the rig:** Tempo **Source = MIDI clock via DIN** to ride with the Chase Bliss
  stack + TimeLine; recall H90 Programs with **PC (offset matched)** alongside CB preset
  changes — but see the delay-warp gotcha in §7. *(midi-clock-tempo-sync, official-part2)*
- **Board-failover bank:** keep H90 Programs that recreate the **Big Sky / TimeLine** sounds so
  the H90 can cover a dead pedal live (Ariel Posen's failover logic). *(ariel-posen)*
- **Insert the Chroma Console** (or another texture pedal) into the H90's insert loop to sit it
  *inside* a reverb/pitch Program. *(insert-loop-setups)*
- **Vocoder-like banjo/baritone (Harmonizer+, firmware v1.10):** **formant-shift** the string
  source ±600 c with **VocalTune** (no repitch) for talkbox/vowel textures, or harmonize a mono
  drone into a scale-locked 3–4-voice chord with **VocalShift / Quadravox+**; play live harmony
  intervals from the **61SL** via **VocalShiftMIDI**, with Glide/Hold mapped to footswitches.
  Stack into the wet-only super-algorithm for a "singing wall." *(harmonizer-plus-vocal)*

---

## 6. Best learning resources

- **Eventide Audio (official)** — the **3-part Joe Cozzi tutorial IS the video manual**
  (overview → tempo/MIDI → Dual/routing); plus a per-algorithm playlist. Start here.
- **Leon Todd** — the deepest, most musical algorithm walkthroughs (ambient/post-rock); real
  settings. Best third-party source by far.
- **Eventide official forum** — the highest-signal community; staff answer in-thread (the
  "H90 questions" megathread, "bugs and issues," "delay glitches with MIDI PC changes").
- **Morningstar forum** — best for MIDI-controller ↔ H90 mapping specifics.
- **Patchstorage (Eventide H90)** — the free Program well; **H90 Control** is the librarian
  (build/reorder lists, import H9). *(official tutorials, patchstorage, h90-control-librarian)*

---

## 7. Common pitfalls / gotchas

- **Delay-warp on Program change (biggest live caveat):** loading a Program via PC warbles
  delay trails — turning spillover/tails off **doesn't fix it** (staff acknowledged). **Use a
  HotSwitch within one Program instead of PC-loading** when delays are ringing. *(bugs-gotchas)*
- **~0.5 s Program load latency** — change on a downbeat/gap. *(bugs-gotchas)*
- **HotSwitches don't ramp and don't stack** — use HotKnob/exp for morphs; Performance Params
  for persistent latches. *(hotswitch-gradual-changes, hotswitch-mutually-exclusive)*
- **Power: center-POSITIVE, ~600 mA @ 12 V / 800 mA @ 9 V.** A low-current port (e.g. 375 mA)
  under-powers it and causes faults — give it a dedicated high-current outlet. *(bugs-gotchas)*
- **H90 Control (Windows) can crash with data loss** (and after Patchstorage imports) — save
  often. *(bugs-gotchas, h90-control-librarian)*
- **Dry path runs through the converters** (no analog bypass) — for pure-wet parallel use
  **Kill Dry** + external blend. *(h90-questions-megathread)*
- **Calibrate aux switches** (System → I/O → Exp & Aux) or external switches act dead; don't
  double-assign one aux switch. *(external-footswitch-aux)*
- **Spillover vs switching speed:** long spillover slows rapid back-to-back changes — lower it
  for fast sections. *(routing-rules)*
- **H9 import** is blocked in Dual Mode and needs H90 Control v1.7.6+. *(import-h9-presets)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `eventide-official-h90-tutorial-part1-essential-overview.md` — architecture, Programs/Presets/routing, inserts + latency, HotKnobs/HotSwitches
- `eventide-official-h90-tutorial-part2-tempo-midi-deep-options.md` — tempo source, full MIDI (clock slaving, Transmit/Thru, PC offset), EXP/aux
- `eventide-official-h90-tutorial-part3-dual-routing-creative-connections.md` — Insert vs Dual, 4-cable, wet/dry/wet, insert-as-splitter
- `leon-todd-h90-wormhole-cinematic-reverb.md` — Wormhole params + ambient/Warp settings
- `leon-todd-h90-polyphony-algorithm.md` — Polyphony chordal pitch, concrete interval/delay/pan patches
- `leon-todd-h90-prismshift-algorithm.md` — PrismShift chord→arp, all controls
- `leon-todd-h90-headspace-deep-dive.md` — Head Space multi-head tape delay + Boil/Break
- `leon-todd-h90-routing-trick-wet-only-superalgorithm.md` — the 100%-wet-into-Program-Mix technique
- `dr-guitar-h90-hotswitch-tricks-ep392.md` — HotSwitch-as-mix + Perform second-row
- `ariel-posen-favorite-eventide-h9-sounds.md` — Posen's named H9 presets + failover philosophy

**Links** (`research/links/`)
- `eventide-h90-preset-management-import-export.md` — file types + import/export + H9-import + ranked sources
- `patchstorage-studio-box-list-artist-programs.md` — 63-program free Studio Box List
- `patchstorage-ambient-drone-granular-programs.md` — ambient + granular Program sets
- `eventide-h90-paid-preset-packs.md` — Worship Tutorials / TeddyTones / etc.
- `eventide-shoegaze-slowdive-settings.md` — ModEchoVerb/Shimmer/Reverse shoegaze recipes *(lightly sourced)*
- `h90-ambient-pad-settings-recipes.md` — copyable pad/drone Program recipes + pad-soloing menu
- `eventide-h90-artists-and-techniques.md` — artists + transferable techniques (honestly sourced)
- `eventide-forum-hotswitch-gradual-changes.md` — HotSwitch can't ramp; ramp workarounds
- `eventide-forum-hotswitch-mutually-exclusive.md` — HS mutual exclusivity + Performance-Param persistence
- `eventide-forum-external-footswitch-aux-mapping.md` — 6 aux switches, TRS wiring
- `eventide-forum-two-scales-one-footswitch.md` — one-stomp 2-scale HotSwitch recipe
- `eventide-forum-h90-questions-megathread.md` — dry-path, MIDI, tempo, spillover, H9-vs-H90
- `eventide-forum-midi-program-change-cc-bypass.md` — PC loads Programs; CC for Active/Bypass; timing
- `eventide-forum-insert-loop-real-world-setups.md` — real insert rigs (incl. Chroma Console as insert)
- `eventide-forum-midi-clock-tempo-sync.md` — MIDI clock vs CC-tap; routing≠clock gotcha
- `eventide-forum-import-h9-presets-howto.md` — H9→H90 import steps + Dual-Mode/v1.7.6 limits
- `eventide-forum-freeze-drone-holds.md` — which algos Freeze + mapping
- `eventide-perform-mode-performance-moves.md` — Warp/Pitch Jump/Boil-Break/Freeze, momentary rules
- `eventide-h90-granular-firmware-update.md` — Cosmic Web/Glitch/GrainMod/Stutter
- `eventide-h90-harmonizer-plus-vocal-algorithms.md` — VocalTune/VocalShift/VocalShiftMIDI/Quadravox+ params + rig uses (firmware v1.10)
- `eventide-forum-hotknob-morphing.md` — HotKnob gang/expression morphing
- `morningstar-forum-h90-midi-preset-switching.md` — no default CC map; PC=Program N
- `eventide-forum-routing-rules-dual-mode.md` — parallel/series rules + spillover tradeoff
- `eventide-forum-bugs-gotchas-delay-warp-power.md` — delay-warp-on-PC, power under-current, app crashes
- `eventide-h90-control-librarian-workflow.md` — Favorites/User filters, list-building, reorder

## Sources

Video (YouTube): Eventide official `5y14LwN9oAk`, `tfd3wQHzxcA`, `0G_WtfUatSc` · Leon Todd
`ujAdlx2HHDY`, `xyiMDam0jkQ`, `xIso_kHM158`, `JZcYl40Leg0`, `jxWh3LG-MY8` · Dr Guitar
`BE8Ffb-Q8j8` · Ariel Posen `tSz8nakVlx4`.
Community: eventideaudio.com/forums (H90 questions, bugs and issues, delay glitches, gradual
changes, footswitch external, two-scale, inserts, freeze, import-H9, routing) ·
forum.morningstar.io · gearspace (snippets only).
Presets/docs: patchstorage.com/platform/eventide-h90 · eventideaudio.com/presets ·
eventideaudio.com/software/h90-control · cdn.eventideaudio.com H90 manual · worshiptutorials.com.
Artists: eventideaudio.com/artists · Premier Guitar / Equipboard (lightly sourced).
Shoegaze/ambient settings: offsetguitars.com · guitarchalk.com *(both via search snippets)*.
Harmonizer+ vocal algos (firmware v1.10, 2025-04-29): cdn.eventideaudio.com H90 manual
(harmonizer-plus) · eventideaudio.com press release · kvraudio.com · intro video `caepdHqAzY8`.
