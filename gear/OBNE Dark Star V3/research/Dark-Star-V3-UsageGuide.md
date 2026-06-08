# Old Blood Noise Endeavors Dark Star V3 — Usage Guide

How people *actually* use the Dark Star Stereo, to complement the spec/reference dossier in `Dark-Star-V3-DeepResearch.md`. In this rig it's the Board 2 terminus: get the most out of it by treating it as a **reverb-as-synthesizer** — drop a chord into a high-Decay/high-Multiply field, then *perform the knobs* (Pitch + Filter) and the **Aux freeze** rather than setting-and-forgetting. The two highest-leverage skills are the off-noon pitch-tuning trick (so it sits in a song instead of "horror-movie chaos") and the freeze/Hold drone for banjo-as-lead.

> Captured this wave: 8 video transcripts + 12 distilled link files (see §8). Two dossier corrections surfaced — **firmware latest is now V3.0R, not V3.0Q** ([changelog](links/obne-firmware-changelog-darkstar.md)), and the **knob's mechanical noon is NOT pitch-unity** ([Antoine Michaud](transcripts/antoine-michaud-settings-non-chaotic.md)). Both folded in below.

---

## 1. Essential workflows

**The "drop a chord and scan" performance (the core way to play it).** Set **Multiply high + Decay high**, drop in a chord, then morph the texture by hand-sweeping **Pitch 1 / Pitch 2** and sculpting **Filter** — Premier Guitar calls the result "Ligeti-inspired orchestral," self-generating textures ([premierguitar-review-recipes](links/premierguitar-review-recipes.md)). This is the pedal's signature interaction model: it's an instrument you operate, not a set-and-forget reverb.

**Freeze / Hold drone (the rig's most performance-critical move).** Assign Aux to freeze by **holding Aux + turning Decay** (pre-assigned to infinite). Hold maxes Decay beyond the knob *and mutes new input*, freezing the current wash into a static bed; release returns Decay to its prior setting. Latching or momentary ([obne-official "Dan Explains It All"](transcripts/obne-official-dan-explains-it-all.md); [AndyDemos](transcripts/andydemos-dark-star-stereo.md)). The defining banjo-as-lead move: play a banjo roll, freeze, solo over the static pad.

**Dual-pitch shimmer build.** Pitch 1 = **Left** channel, Pitch 2 = **Right** channel, ±2 oct. Both pitches **+1 octave** plus a little **Multiply** (regeneration) gives ascending shimmer; the octave-up makes the shimmer, a slight detune between the two adds a chorusy "drop" — tame runaway with the **LPF side of Filter** so the regenerating pitches don't escape ([obne-official "3: Mono vs Stereo"](transcripts/obne-official-3-mono-vs-stereo-dark-star.md); [Mark Johnston](transcripts/mark-johnston-secret-weapons-dark-star-stereo.md)).

**100%-wet degraded drone.** Crush below noon (sample-rate reduction), **Mix at 100% wet** — no dry signal, just a bit-crushed drone bed. Tune the pitch first, pick the crush amount, and you've got a standalone "recorded-wrong" texture ([Antoine Michaud](transcripts/antoine-michaud-settings-non-chaotic.md)).

**Expression sweeps.** Hold On/Off + move the target knob(s) to set heel (start) / toe (end); unmoved knobs are unaffected; saved per preset. A standout: **expression → Lag** on a random/LFO source = "sunbaked lo-fi tape modulation" ([Pedal Zone](transcripts/pedal-zone-dark-star-stereo-soundscape.md)). Expression is widely considered far more musical than the footswitch Pitch/Filter jumps.

---

## 2. Signature patches & settings

OBNE publishes no preset chart and has no preset-sharing platform, so most "patches" are **directional knob recipes** from reviews/demos. Flagged where directional vs. directly quoted. These extend dossier §13 rather than repeat it.

| Sound | Settings | Source / confidence |
|---|---|---|
| **Neutral reference pad** | Filter / Pitch 1 / Pitch 2 / Crush all at **noon** (all detented) — "as synthetic as but less sparkly than a shimmer" | Quoted, [premierguitar](links/premierguitar-review-recipes.md) + [guitar-com](links/guitar-com-big-review.md) |
| **Stacked-octave pad** | **Pitch 1 = octave up, Pitch 2 = octave down** simultaneously; center-zone detune for width | Directly described, [premierguitar](links/premierguitar-review-recipes.md) |
| **Drone "scan"** | **Multiply high + Decay high**, drop a chord, sweep Pitch + Filter by hand | Quoted, [premierguitar](links/premierguitar-review-recipes.md) |
| **Octave-down doom** | Both Pitch knobs **CCW**, high Decay + Multiply | Directional, [russomusic](links/russomusic-review-recipes.md) |
| **Lo-fi / crushed wash** | **Crush CCW** (fewer bits → broken) | Quoted, [russomusic](links/russomusic-review-recipes.md) |
| **Overdriven stereo reverb** | **Crush CW** ("the absolute best sound on offer") | Quoted, [guitar-com](links/guitar-com-big-review.md) |
| **Mono-rig shimmer trick** | Stereo routing into ONE amp, use **Spread** to bleed the Pitch-2 (oct-up) output toward the unused channel = dial-in shimmer amount on a mono setup | Copyable technique, [guitar-com](links/guitar-com-big-review.md) / [gearnews](links/gearnews-multiply-crush-power-tips.md) |
| **Freeze bed** | Aux = **Hold**; **Multiply carefully** (tips into self-oscillation at high Multiply + Decay) | [russomusic](links/russomusic-review-recipes.md) + [premierguitar](links/premierguitar-review-recipes.md) |

**The pitch-tuning trick (single most practical setting).** The knob's mechanical **noon is NOT clean unity** — it's slightly detuned and sounds out of tune over chords. Fix: nudge a hair right of noon — Antoine aims the pointer at the center of the **"a" in the printed word "Dark."** This is the difference between "sits in a song" and "horror movie" ([Antoine Michaud](transcripts/antoine-michaud-settings-non-chaotic.md)). For chorused width, mirror Pitch 2 to Pitch 1 then nudge it a hair off.

---

## 3. Power-user tips, tricks & hidden features

- **Pitch quantization is a feature, not a limitation** — the stepped intervals let you build **reverb chords** across the two shifters, not just detune ([gearnews](links/gearnews-multiply-crush-power-tips.md)).
- **Multiply in moderation** = "yowling, wobbly" chorus character; a lot = self-oscillation. It reprocesses the reverb through itself (trails + pitch + lag + filter + crush all fed back), so cascading pitch jumps go "Blade Runner / Rainbow Machine" ([Mark Johnston](transcripts/mark-johnston-secret-weapons-dark-star-stereo.md)). The **Volume** knob exists to recover level lost at full-wet Mix.
- **Stereo Spread inverts the WET image only, not the dry** — fully CCW puts a right-channel note's reverb on the *left* out while its dry stays right. Center sums reverb to both. Killer move: invert Spread against a ping-pong delay downstream for cross-panned width ([Mark Johnston](transcripts/mark-johnston-secret-weapons-dark-star-stereo.md)).
- **Aux = three jobs:** Hold (freeze) / Pitch (momentary +1 oct both shifters, auto-returns) / Filter (momentary LPF slam). Assign by holding Aux + moving the related knob; saved per preset.
- **Foot-stepping presets hands-free:** hold Aux + tap Preset to cycle presets from the Aux switch.
- **Crush is two effects in one knob:** below noon = sample-rate/bit reduction ("early samplers to cell phones"); above noon = soft-clip overdrive *into the tail* ("the absolute best sound on offer," per guitar.com). The OD side is the under-used half.

---

## 4. Notable users & techniques

Artist documentation for the Dark Star is genuinely sparse — one solid name beats padding.

- **VERIFIED — Evan Patterson** (Emma Ruth Rundle's live band; also Jaye Jayle / Young Widows) runs an **Old Blood Noise Dark Star** on his board in Premier Guitar's Emma Ruth Rundle Rig Rundown (PG page tagged "old-blood-noise-endeavors"; pedal visible ~26:37; corroborated by Equipboard). It's the **original mono Dark Star** (2019), not the V3 — but it's a dead-on lane match: long, dark, atmospheric beds under heavy, slow doom-folk material, the same terminus-of-texture role this rig assigns the V3. HIGH confidence on use; no documented knob settings ([evan-patterson-emma-ruth-rundle-rig](links/evan-patterson-emma-ruth-rundle-rig.md)).
- **UNVERIFIED leads:** *James Duke* (Instagram, praising the Dark Star) recurs in search aggregation but couldn't be pinned to a primary dated source. The OBNE "Signature Edition" pedals are signed by the **OBNE founder (Brady Smith)**, not an outside artist — do not list as a famous-user endorsement ([artists-unverified-and-leads](links/artists-unverified-and-leads.md)).
- **Reputation signal:** the community has cloned the original modes — a PatchStorage **ZOIA "Neutron Star"** patch emulates Dark Star modes 1+3 ([patchstorage-neutron-star-zoia-emulation](links/patchstorage-neutron-star-zoia-emulation.md)).

---

## 5. Rig-specific recipes (this banjo/baritone drone rig)

Dark Star sits as the **Board 2 terminus**: `OBNE Parting → CB Lost & Found → Hologram Microcosm → Walrus QI Etherealizer → Dark Star → (stereo to Board 3)`. Set **Routing = Stereo, trails on** so Board 3 (Generation Loss → Big Time → MOOD → Blooper, then H90 + Chroma) keeps chewing the tail.

- **Frozen banjo bed → solo over it.** Aux = Hold. Predelay with **Lag** so the dry banjo pluck speaks (banjo transients are fast), high **Decay**, then **freeze** a roll and play banjo-as-lead over the static pad. Favor the **LPF side of Filter** — banjo content sits high and octave-**up** Pitch will ice-pick. *Caveat from the gotchas: while frozen, notes you play over the pad pass DRY — lean on the dry path + downstream H90 verb for the lead, or use expression swells instead of re-triggering.*
- **Octave-down doom pad (baritone home turf).** Both Pitch **CCW** (octave-down on the baritone Jazzmaster), high Decay + Multiply, Filter to LPF, Crush a hair below noon for the degraded edge. Pair with a sustained-fuzz wall upstream (Hizumitas/Longsword on Board 1) and an octave-down VG-800 baritone patch.
- **Granular smear (Microcosm two slots up).** Let the Microcosm's chopped/granular output feed Dark Star; freeze a Microcosm phrase, then Hold on Dark Star to stack two static beds. The pad makes the Microcosm's stutter read as intentional.
- **QI Etherealizer immediately upstream = additive, not redundant.** Let QI shape the *pre*-reverb texture; let Dark Star be the long-trail terminus. If it soups up, pull **Mix** back toward unity and LPF the pad to seat it under QI's output.
- **VG-800 synth/pad patches** = the most seamless walls in the rig — sustain into sustain, no transient to smear. Poly guitar-synth patches will artifact under heavy Pitch/Crush, which is on-aesthetic here.
- **Cross-panned stereo into Board 3.** Use the Spread-inverts-wet-only trick against the downstream ping-pong delays for width before the tape stage.

---

## 6. Best learning resources

**Video — channels/clips worth following:**
- **Old Blood Noise Endeavors (official)** — ["Dan Explains It All"](transcripts/obne-official-dan-explains-it-all.md) is the canonical knob-by-knob reference; ["3: Mono vs Stereo"](transcripts/obne-official-3-mono-vs-stereo-dark-star.md) explains the architecture (V3 = three chained mono Dark Stars + Lag/Multiply/Spread).
- **Mark Johnston / Secret Weapons** — [deepest single demo](transcripts/mark-johnston-secret-weapons-dark-star-stereo.md): true-stereo Spread theory, Aux + expression setup.
- **Antoine Michaud** — [best "make it musical" technique](transcripts/antoine-michaud-settings-non-chaotic.md): the off-noon pitch-tuning trick, crush taming, 100%-wet drone (covers the original mono unit; maps cleanly to V3).
- **The Pedal Zone** — [most-viewed](transcripts/pedal-zone-dark-star-stereo-soundscape.md): hearing textures + the expression-on-Lag idea.
- **AndyDemos** — [clean layer-by-layer build](transcripts/andydemos-dark-star-stereo.md). **B's Music Shop** — [manual-read + hands-on test](transcripts/bs-music-shop-dark-star-v3-ultimate-test.md).

**Text — reviews/community (forum-grade chatter is thin; these are review-grade):**
- [Premier Guitar review](links/premierguitar-review-recipes.md) (4.6/5) — the "reverb-based synthesizer" framing + the drone-scan move.
- [guitar.com "Big Review"](links/guitar-com-big-review.md) — Crush/shimmer directions, mono-shimmer Spread trick.
- [Russo Music review](links/russomusic-review-recipes.md) — octave-down doom, lo-fi crush, self-oscillation warning.
- [OBNE firmware changelog](links/obne-firmware-changelog-darkstar.md) — authoritative version history (now **V3.0R**).

---

## 7. Common pitfalls / gotchas

- **Bone-dry Hold (the big one).** Engaging Hold freezes the wash but **locks new input out of the reverb** — anything you play over a frozen pad is *dry*. By design, surprises everyone. Work around it with expression swells, downstream reverb on the lead, or reassign Aux to preset-toggling ([community-hold-aux-expression-gotchas](links/community-hold-aux-expression-gotchas.md)).
- **Closeable filter.** Filter fully CCW = **complete silence** (it's a closeable LPF, not a tone roll). Catches people who think the pedal died.
- **Pitch snapping.** Pitch is stepped/quantized — small knob moves near octave boundaries jump. For smooth detune, stay in the wide center "Detune" zone, and remember mechanical noon ≠ pitch-unity (§2 trick).
- **Mono-mode pitch differs.** In Mono routing, Pitch 2 sums *in parallel* to Pitch 1 (recreating the original dual-interval Pitch mode) — don't expect identical results when you collapse routing.
- **350 mA power draw.** Heavy — needs a high-current isolated slot (e.g. a 500 mA digital outlet); a generic 100 mA slot won't run it. Relay bypass needs power to pass signal.
- **Footswitch Pitch/Filter jumps** are widely called limited vs. expression — assign Aux to **Hold** and put Pitch/Filter motion on the expression pedal instead.
- **Firmware:** the K/M/Q cluster were all pitch/preset-recall bug fixes — a preset-driven board should stay current. **V3.0R (latest)** fixes a MIDI hang where power-cycling an external MIDI controller halts MIDI to the Dark Star until the pedal is also restarted — directly relevant to a board-wide-MIDI rig ([obne-firmware-changelog-darkstar](links/obne-firmware-changelog-darkstar.md)). Check the owner's installed version.

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `obne-official-dan-explains-it-all.md` — OBNE official knob-by-knob walkthrough (canonical reference).
- `obne-official-3-mono-vs-stereo-dark-star.md` — OBNE official; V3 = 3 chained mono Dark Stars + Lag/Multiply/Spread.
- `mark-johnston-secret-weapons-dark-star-stereo.md` — deepest demo; true-stereo Spread, Aux & expression setup.
- `pedal-zone-dark-star-stereo-soundscape.md` — most-viewed; open-canvas design + expression-on-Lag.
- `antoine-michaud-settings-non-chaotic.md` — the "aim for the a" pitch-tuning trick; 100%-wet drone (original mono unit).
- `andydemos-dark-star-stereo.md` — layered build; Aux filter-sweep / pitch-ramp / freeze.
- `bs-music-shop-dark-star-v3-ultimate-test.md` — full manual read + hands-on.
- `antoine-michaud-crush-mode-bitcrusher.md` — original-DS crush texture *(no captions — notes only)*.

**Links** (`research/links/`):
- `obne-firmware-changelog-darkstar.md` — verbatim J→R changelog; **R is latest** (MIDI-hang fix).
- `premierguitar-review-recipes.md` — noon baseline, stacked octaves, the drone-scan move.
- `guitar-com-big-review.md` — Crush/shimmer directions, mono-shimmer Spread trick, Filter-direction note.
- `russomusic-review-recipes.md` — octave-down drone, Crush-CCW lo-fi, Hold, self-oscillation warning.
- `gearnews-multiply-crush-power-tips.md` — Multiply-in-moderation, reverb chords, routing toggle, no-plate verdict.
- `gearpedalx-lineage-original-vs-stereo.md` — original-vs-V3 lineage, what changed/added.
- `community-hold-aux-expression-gotchas.md` — bone-dry-Hold gotcha, Aux three-modes, expression procedure.
- `community-comparisons-vs-other-reverbs.md` — vs Big Sky / Microcosm / NightSky / Cloudburst verdicts.
- `obne-marketing-sound-descriptions.md` — manufacturer voice/feature framing; confirms no published preset sheet.
- `evan-patterson-emma-ruth-rundle-rig.md` — the one VERIFIED named user.
- `artists-unverified-and-leads.md` — honest record of unverified leads + Brady-Smith clarification.
- `patchstorage-neutron-star-zoia-emulation.md` — community ZOIA clone (reputation signal).

## Sources

All claims above cite a captured `transcripts/` or `links/` file. Original URLs are recorded on the first line of each captured file. Authoritative spec/reference lives in [`Dark-Star-V3-DeepResearch.md`](Dark-Star-V3-DeepResearch.md); the manual is at [`manuals/OBNE Dark Star v3.pdf`](../manuals/OBNE%20Dark%20Star%20v3.pdf).
