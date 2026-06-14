# Addictive Drums 2 — Usage Guide

In a drone/doom/shoegaze rig, AD2 is best treated as a **clean-ish drum
*source*** — the kit you build fast, then degrade downstream (RC-20 / SketchCassette
II / Decapitator / Lossy, or reamped through the hardware tape pedals) or bounce to
one-shots for the **MPC Sample / Kontakt 8 / Digitakt 2**. Its two highest-value
features for this aesthetic are **multi-out routing** (so you can crush individual
drums instead of the whole kit) and the **Dead & Dry** kit collection (towel-muffled,
roomless drums that don't fight your own reverbs/tape). The single best dark-music
reference is XLN's own *Stoner Doom* video — layered AD2 instances into a sludge wall.

---

## 1. Essential workflows

**A. Preset-first, then Master-bus tweak (fastest path).** Start in **Explore**,
audition presets, drag the preset's demo groove into the DAW (it brings the MIDI in
*and* auto-loads the preset, following host tempo). Then fine-tune on the periphery —
don't rebuild from scratch. Put EQ/comp/distortion/Tape on the **Master channel**
(Edit page, far right) for a glued sound rather than fiddling every fader.
[transcripts/ad2-getting-started-crash-course-indielab.md; transcripts/ad2-how-to-use-full-walkthrough-hms1.md]

**B. Multi-out routing (the key move for this rig).** Load the **multi-out plugin
variant** (labeled "4× Stereo, 10× Mono" — the plain stereo variant has *no* extra
outs). Each AD2 mixer channel gets a **green down-arrow** at the bottom; click it to
route Kick / Snare / Hi-hat / 4 Toms / 3 Flexi / OH / Room / Bus to its own output,
and choose **Pre-Fader** (raw drum *before* AD2's channel FX — the cleanest source for
external degrading) or **Post-Fader** (keeps AD2's processing).
- **Logic:** insert AD2 as **Multi-Output**, then click the **[+]** in the mixer to
  auto-spawn Aux channels (Addict 3 = Kick, Addict 4 = Snare…).
- **Ableton:** per channel set each audio track's **Audio From → AD2 + the bus**,
  Monitor In. (Mind the Live 12 **Lite** track ceiling — see §7.)
[links/ad2-xln-separate-outputs-multiout.md; links/ad2-multiout-logic-pro-setup.md; links/ad2-multiout-ableton-live.md; links/ad2-airfix-separate-outputs-howto.md]

**C. Layering via Flexi + Link.** Kick and snare slots have a **Link icon**
(top-right) — drag it onto a **Flexi slot** to layer a second piece that triggers with
the main one. Switching the main snare leaves the linked Flexi piece intact. Use a
Flexi copy for **parallel compression** (smash the copy, blend it under the dry main).
[transcripts/ad2-build-your-own-kit-flexi-link.md; transcripts/ad2-how-to-use-full-walkthrough-hms1.md]

**D. MIDI / Beats → DAW.** In **Beats**, pick a groove, enable **Sync Tempo**, drag the
name to the timeline (host snap on). Per-beat realism knobs: **Velocity** (+ randomize
so hits aren't machine-gun-equal), **Timing** (loosen / "sloppy"), **Accents** (8th vs
16th); each beat has variants (Main / alternates / clap / ghost). **Transform**
time-stretches a groove with no quality loss before you drag the MIDI out. Each ADpak
ships beats tuned to that pack.
[transcripts/ad2-drag-and-drop-midi-and-audio.md; links/ad2-midi-grooves-import-drag-sampling-out.md]

**E. Sampling AD2 out → hardware/Kontakt (the rig's sample-factory path).** There's
**no native one-shot export** — the community method: solo a drum (or use multi-out),
trigger single hits at chosen velocities, **bounce short regions** (dry for tight
one-shots, with tail for natural), optionally **RC-20-stamp** them first, then load to
the **MPC Sample / Kontakt 8 / Digitakt 2**. For loops: set the loop to tempo, play 2
bars, drop the recorded WAV, chop. AD2 becomes a vintage-kit sample bank.
[links/ad2-midi-grooves-import-drag-sampling-out.md; transcripts/ad2-drag-and-drop-midi-and-audio.md]

---

## 2. Signature presets & settings (copyable)

**Kits / ADpaks for this aesthetic** (verified against XLN product pages + reviews):
- **Dead & Dry Collection** (Ingrid Studios, towel/blanket/moon-gel dampening) — the
  anchor for degraded/dry drums:
  - **Vintage Dead** — concert toms, dead/dry, preset **"Hard and Icky"**; sound-target
    Tame Impala / Khruangbin / QOTSA / Death From Above 1979.
  - **Vintage Dry** — 1968 Ludwig Silver Sparkle; widely cited as *the* indie sound
    (Men I Trust / Mac DeMarco target).
- **Indie ADpak** — 2″ tape, analog preamps, Keith Moon Premier snare; warm out-of-box.
- **Boutique Mallets** — soft swells for ambient/post-rock.
- **Fairfax Vol. 1/2** (Sound City) — roomy vintage.
- **United Pop / United Heavy** — clean do-anything sources; United Heavy = the doom floor.
- **Avoid Studio Pop / Studio Rock** — community consensus "very dated."
- 3rd-party **Prod Shadow "DIY Drums"** — 30 presets purpose-built for
  shoegaze/slowcore/post-punk.
[links/ad2-kits-adpaks-for-moody-vintage-dry.md]

**De-stock / sound-design values:**
- **Tone Designer:** select a piece → pull the **END value DOWN** to taper ring while
  keeping punch (tame a ringy snare); push **UP** for more tone. Also sets
  decay/attack/release. [transcripts/ad2-tweak-your-sound-edit-fx-snapshots.md]
- **Per-piece pitch offset:** drop main kick pitch for thunder; offset pitch
  *differently* in OH vs Room vs close mics to fake real-room detuning. [hms1]
- **Width per piece:** keep the snare centered but tighten its width inside the OH.
- **Internal Noise module:** tube / DC / muff / **vinyl** noise per channel — a first
  pass of lo-fi grit before any external plugin. [indielab]
- **Tape/Shape on Master:** tape sat + bottom-end + an automatable **Cut** filter. [indielab]
- **Humanize:** never program 127-only (triggers one sample, kills nuance); ghost notes
  ~**30–50 velocity**; AD2's MIDI is intentionally slightly off-grid.

**Delerb (the two send units):** delay tempo-syncs (11 values or free ms), **feedback to
100% = infinite washes** (drone tails); reverb is Ambience/Room/Hall/Plate with a
**"Swirl"** chorus that thickens tails (shoegaze-friendly). Reverb has its own EQ/width/
pan. Route Delerb **Post Master Insert** to keep the wash *out* of master compression
("smash the dry kit, keep the wash clean"). [links/ad2-delerb-bus-fx-internal-routing.md]

**Shoegaze drum settings:** 90–120 BPM, simple/repetitive, drums tucked low under the
guitar wall, Hall/Plate decay **1–3 s**, LPF cymbals ~**12–14 kHz**, gentle comp, ghost
notes + cymbal swells, layer AD2 with electronic one-shots. [links/ad2-shoegaze-postrock-drum-approach.md]

---

## 3. Power-user tips, tricks & hidden features

- **Pre-Fader output = raw drum before AD2's channel FX** — the cleanest signal to feed
  external degrade chains. [links/ad2-airfix-separate-outputs-howto.md]
- **Multi-out BYPASSES AD2's Master / Delerb / Bus FX** — your in-AD2 glue and washes
  will *not* carry to the routed outputs. Rebuild glue/wash downstream in the DAW (which
  is where this rig's character plugins live anyway). [links/ad2-xln-separate-outputs-multiout.md]
- **The Bus channel** — send any channel to a submix, **distort the Bus**, blend into
  Master = in-box parallel drum distortion. [links/ad2-delerb-bus-fx-internal-routing.md]
- **5 Snapshots** — revertible A/B of clean vs degraded mixer states. [tweak-your-sound]
- **Hidden MIDI import:** Help (?) menu → "Open external MIDI folder" → drop a pack in →
  "Refresh MIDI library." AD2 reads GM mapping. [links/ad2-midi-grooves-import-drag-sampling-out.md]
- **Beats grid-searcher** filters grooves by which hits you place on the basic grid;
  **Transform** stretches grooves losslessly. [links/ad2-cpu-library-management.md; ad2-midi-...]
- **Audio Recorder per pad** captures a hit/loop you can drag straight out as WAV. [drag-and-drop]

---

## 4. Notable users & techniques

Honest flag: **no verifiable interview** of a moody/indie artist tracking with AD2 turned
up. What exists:
- **Otto (XLN "Stoner Doom" feature)** — the one concrete documented dark-music technique:
  re-scored Electric Wizard / Sleep–style drums in AD2 by layering multiple instances
  (see §5). [transcripts/ad2-stoner-doom-sleep-electric-wizard.md]
- **DLR** (drum & bass) — official AD2 features overview (Loopmasters).
- **Sound-target references** (NOT confirmed users): Vintage Dry → Men I Trust, Mac
  DeMarco; Vintage Dead → Tame Impala, Khruangbin, Glass Beams, QOTSA, DFA1979. Treat
  these as "sounds like," not documented sessions. [links/ad2-kits-adpaks-for-moody-vintage-dry.md; links/ad2-vs-superior-drummer-kvr.md]

---

## 5. Rig-specific recipes

**1) Doom / sludge wall (Otto's layered build — direct match).** Stack separate AD2
layers, each a different job:
1. **Lo-fi layer** — United Heavy / Black Velvet: EQ out highs *and* lows, compress to
   dig out quiet hits, kill the snare bottom-mic buzz, **lower snare pitch** for a big
   smack, a touch of room.
2. **Sub layer** — same kit, all highs EQ'd out + lows boosted (or trigger a tuned sine
   off the kick for rumble).
3. **Vintage-compressed layer** — Retroplex, crushed flat/flabby, sat low.
4. **Punchy dry layer** + **5) roomy layer** (boosted room, adjusted OH, snare tuned down).
   **Pull the hi-hat mic down on every kit** — doom/sludge OHs carry almost no high end.
[transcripts/ad2-stoner-doom-sleep-electric-wizard.md]

**2) Degrade individual drums (Logic, multi-out).** One AD2 multi-out instance →
green-arrow the drums → Logic mixer **[+]** to auto-create auxes → insert **RC-20 /
DS-10 / Decapitator / SketchCassette II / Lossy per drum**. Crush only Room/OH, keep the
kick clean underneath. [links/ad2-multiout-logic-pro-setup.md; links/ad2-lofi-dusty-drum-recipe.md]

**3) Lo-fi drum bus (downstream).** AD2 clean → **DS-10** (set punch first) → **RC-20**
(Magnetic + small Distort + Digital crush) → **SketchCassette II** (wow/flutter) →
**Decapitator** (low drive) → **Goodhertz Lossy** (codec crush last). Rule: **one
wow/flutter source per layer** — don't stack RC-20 Wobble *and* SketchCassette on the
same drum. [links/ad2-lofi-dusty-drum-recipe.md]

**4) In-box trashy chain (no extra plugins).** Per-channel Tape Sat + Distortion →
Transient Shaper to recover knock → send to **Bus**, distort hard, blend → **Snapshot**
A/B against clean. [links/ad2-lofi-dusty-drum-recipe.md; links/ad2-delerb-bus-fx-internal-routing.md]

**5) Reamp through the pedalboard / tape pedals.** AD2 multi-out **Room pair (Pre-Fader)**
→ Logic aux → **Radial X-Amp** → Middle/End boards (**Big Time / Generation Loss**) →
interface in → new track. **Phase-align sample-by-sample, null-test, blend 20–40% under
the dry kit** (out-and-back is never sample-accurate). [links/ad2-reamp-drums-through-pedals.md]

**6) AD2 as a sample factory → MPC / Kontakt / Digitakt.** Bounce hits (dry for tight
one-shots; with tail for natural), optionally RC-20-stamp, load into the **MPC Sample /
Kontakt 8 / Digitakt 2**. The fastest way to turn AD2's vintage kits into your own chop
material. [links/ad2-midi-grooves-import-drag-sampling-out.md]

**7) Shoegaze / post-rock framing.** Drums tucked low under the guitar wall, Hall/Plate
1–3 s, LPF cymbals ~12–14 kHz, ghost notes + cymbal swells, layer with electronic
one-shots; soft mallets (Boutique Mallets) for ambient swells. [links/ad2-shoegaze-postrock-drum-approach.md]

---

## 6. Best learning resources

- **XLN Audio (official) — Spotlight series** (Build / Tweak / Find / Drag-and-Drop) +
  topic shorts. **The "Stoner Doom" feat. Otto video is the must-watch** for this rig.
  Highest signal-per-minute. [transcripts/ad2-stoner-doom-…; ad2-tweak-your-sound-…; ad2-build-your-own-kit-…; ad2-drag-and-drop-…]
- **The Indie Music Lab** — best beginner→intermediate full crash course, indie/alt-rock
  framing (closest genre adjacency). [transcripts/ad2-getting-started-crash-course-indielab.md]
- **Home Music Studio 1 (Dave Maxi)** — most thorough technical walkthrough: multi-out,
  Flexi parallel comp, per-piece controls. [transcripts/ad2-how-to-use-full-walkthrough-hms1.md]
- **Groove3 — "Addictive Drums 2 Explained" (Todd Tatnall)** — paid; the exhaustive A-to-Z
  series (referenced, not captured — paywalled).
- **The REAPER Blog — "Trashy & Lo-Fi Drums in AD2"** — the strongest lo-fi-degrade
  tutorial; flagged but not captured (video belongs to a future pass if wanted).
- Threads: **KVR — AD2 vs Superior Drummer 3** (honest strengths/weaknesses);
  **Gearspace — AD2 CPU spikes**. [links/ad2-vs-superior-drummer-kvr.md; links/ad2-cpu-library-management.md]

---

## 7. Common pitfalls / gotchas

- **Multi-out bypasses AD2's Master / Delerb / Bus** — in-AD2 glue won't carry; rebuild
  downstream. [links/ad2-xln-separate-outputs-multiout.md]
- **Wrong plugin variant** — load the **multi-out** AU/device, not the stereo one, or no
  extra outputs appear (a common Logic "[SOLVED]" confusion). [links/ad2-multiout-logic-pro-setup.md]
- **Ableton Live 12 Lite track ceiling** — a full ~13-track drum explosion can exhaust
  Lite's budget before guitars/synths. Route only 2–3 drums separately in Lite, or do
  the heavy drum work in **Logic**. [links/ad2-multiout-ableton-live.md]
- **CPU / RAM** — RAM-heavy; **the dual reverb engine is the main CPU cost** (turn it off
  and wash externally); the **Beats browser lags** with lots of 3rd-party MIDI loaded
  (runtime unaffected). Run **one** multi-out instance, not many; freeze/bounce. [links/ad2-cpu-library-management.md]
- **Reamp phase drift** — out-and-back is never sample-accurate; align + null-test before
  blending. [links/ad2-reamp-drums-through-pedals.md]
- **AD2 vs SD3 weaknesses** — shallower velocity sampling, fixed instrument slots,
  compressed samples, harsh-ish cymbals; mostly irrelevant for buried/degraded drums. [links/ad2-vs-superior-drummer-kvr.md]
- **No native one-shot export** — the sampling-out workflow is the community bounce
  method, not an official feature; check by ear when building kits. [links/ad2-midi-grooves-import-drag-sampling-out.md]
- **AU for Logic; VST3/AU for Ableton.** Online installer (XLN Online Installer, online
  auth); large ADpak disk footprint.

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `ad2-stoner-doom-sleep-electric-wizard.md` — XLN/Otto, layered doom/sludge wall (★ rig-fit crown jewel)
- `ad2-tweak-your-sound-edit-fx-snapshots.md` — official: Edit/FX, Snapshots, Tone Designer, Delerb
- `ad2-build-your-own-kit-flexi-link.md` — kit-piece browser, Link→Flexi layering
- `ad2-drag-and-drop-midi-and-audio.md` — dragging MIDI + WAV out (sampler-source workflow)
- `ad2-getting-started-crash-course-indielab.md` — best full beginner→intermediate tour
- `ad2-how-to-use-full-walkthrough-hms1.md` — most thorough technical walkthrough (multi-out, Flexi)
- `ad2-schmack-dead-dry-drums.md` — Vintage Dead ADpak promo ("Hard and Icky"), distilled

**Links** (`research/links/`):
- `ad2-xln-separate-outputs-multiout.md` — multi-out concept + master-FX-bypass gotcha
- `ad2-multiout-logic-pro-setup.md` — Logic multi-out, the [+] auto-aux trick
- `ad2-multiout-ableton-live.md` — Live setup + Lite track-ceiling warning
- `ad2-airfix-separate-outputs-howto.md` — Pre-Fader vs Post-Fader output modes
- `ad2-delerb-bus-fx-internal-routing.md` — internal mixer FX, Delerb, Bus, Snapshots
- `ad2-cpu-library-management.md` — CPU/RAM, reverb cost, Beats-browser lag *(Gearspace 403'd; triangulated)*
- `ad2-reamp-drums-through-pedals.md` — reamp flow, phase/null, mapped to X-Amp + tape pedals
- `ad2-vs-superior-drummer-kvr.md` — honest AD2 vs SD3 pros/cons
- `ad2-kits-adpaks-for-moody-vintage-dry.md` — kit/ADpak picks + kits to avoid *(XLN page 403'd; triangulated)*
- `ad2-shoegaze-postrock-drum-approach.md` — genre drum craft mapped to AD2 + degrade chain
- `ad2-lofi-dusty-drum-recipe.md` — dusty values, in-box + downstream lo-fi chains
- `ad2-midi-grooves-import-drag-sampling-out.md` — MIDI import/drag + sampling out to MPC/Kontakt/Digitakt

**QC notes:** 19 sources total (7 transcripts + 12 links). Gearspace and some XLN
support/product pages 403 bots — those files are triangulated from search-indexed text +
mirrors (Airfix, Ableton forum, KVR, SoundOnSound) and are labeled as such. **No
documented artist-uses-AD2 interview exists** — artist names are sound-targets, not
confirmed users. The AD2→degrade-into-hardware/RC-20 chain and the one-shot sampling-out
method are **community/inferred**, assembled by analogy from Otto's lo-fi layer +
AD2's internal vinyl-noise/tape — not a single first-party "do this" source.

## Sources

See §8 for the full local capture index. Originals: youtube.com (XLN Audio, The Indie
Music Lab, Home Music Studio 1), xlnaudio.com + support.xlnaudio.com, soundonsound.com,
gearspace.com, kvraudio.com, forum.ableton.com, airfixmusic.com, theproaudiofiles.com,
cedarsoundstudios.com, lofiweekly.com, oddgrooves.com, drumspy.com. All URLs recorded on
line 1 of each captured file.
