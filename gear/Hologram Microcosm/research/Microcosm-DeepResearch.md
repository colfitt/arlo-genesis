# Hologram Electronics Microcosm — Deep Research

A working dossier for the Microcosm as the granular centerpiece of Board 2 (Middle / Texture) in a stereo, hex-pickup banjo/baritone rig. It sits third on the board — after OBNE Parting (filter) and CB Lost & Found (random gate) — and feeds Walrus QI Etherealizer and OBNE Dark Star V3. Board 2's entire job is "Filter · Granular · Smear," and the Microcosm is the granular engine the rest of the board exists to support: it takes the sustained fuzz walls and modeled pads arriving from Board 1's stereo split at the Deco V2 and turns them into the cascading micro-loops, frozen drones, and glitch fragments that define the owner's drone/doom/shoegaze aesthetic.

## 1. Lineage: Hologram's First Pedal and the Granular Concept

The Microcosm was [Hologram Electronics'](https://www.hologramelectronics.com/products/microcosm) debut product — a Detroit-built granular/looper/glitch pedal that launched in 2020 (the manual carries a "© 2020 Hologram Electronics" notice) and effectively created the "ambient cheat code" pedal category that the later [Chroma Console](https://www.hologramelectronics.com) (its Board 3 sibling) and a wave of imitators followed. Where most delay/looper pedals start from a tape or BBD metaphor, the Microcosm starts from **granular synthesis**: it chops incoming audio into short samples ("grains" / micro-loops) and re-sequences, re-pitches, and re-layers them. Per the manual's own framing, it "rearranges and reinterprets your sound… using a variety of granular sampling, delay, and looping techniques. Cascading micro loops can be locked into tight tap-tempo synced rhythms, diffused into glacial ambient textures, woven into hypnotic drones, and much more."

The architecture is **11 distinct effects across 4 categories, each with 4 variations (A–D) = 44 "preset variations."** On top of that sits built-in **Pitch Modulation, a 4-mode stereo Reverb, a resonant Low-Pass Filter, a Hold Sampler, and a 60-second stereo Phrase Looper** with 16 saveable user presets. This is a *lot* of pedal — [Sound On Sound](https://www.soundonsound.com/reviews/hologram-electronics-microcosm) notes it functions as "a looper, granular sampler, delay, reverb, pitch modulator, and filter" at once, and [Guitar World](https://www.guitarworld.com/reviews/hologram-electronics-microcosm-review) calls the results "truly unlike anything else out there."

**Firmware:** The most current public firmware is **v1.13 (released May 2022)** per [Hologram's firmware page](https://www.hologramelectronics.com/pages/microcosm-firmware); pedals shipped June 2022 or later carry it. Updates are pushed over **MIDI** (browser-based WebMIDI updater or a `.syx` SysEx transfer). Earlier triggering quirks in v1.1-era firmware (the Glitch/Strum onset detection) were improved in later builds, and wet-volume handling was boosted. **There is no "firmware 2.0"** — flag any reference to one as inaccurate; the Microcosm's feature set has been stable on the v1.1x line, and Hologram's newer development energy went into the Chroma Console rather than a Microcosm 2.0.

## 2. Controls & the Four Effect Categories

Eight knobs, three footswitches, a Preset Selector dial, and four indicator-bar lights. Each main knob has a **Secondary Control** accessed by holding the **Shift** (TIME) button.

- **ACTIVITY** — density/complexity of the effect; turns up "more" of whatever the engine does. *Function varies per preset.*
- **REPEATS** — effect duration/frequency, works in tandem with Activity. *Secondary: Pitch Modulation depth.*
- **SHAPE** — contours the volume/filter envelope of the effect. *Secondary: Pitch Modulation rate.*
- **FILTER** — resonant low-pass; **100% CW = filter bypassed**, CCW cuts highs (fully CCW kills all effect). *Secondary: filter resonance.*
- **TIME / TAP (Shift)** — sets Subdivision (¼, ½, TAP, 2×, 4×, 8×) or, in Tempo mode, smooth global tempo. *Secondary access button for all Shift functions.*
- **SPACE** — mixes in reverb + delay; fully CW = 100% wet. *Secondary: selects 1 of 4 reverb modes.*
- **MIX** — dry/effect balance. *Secondary: effect master volume.*
- **LOOP LEVEL** — Phrase Looper playback volume. *Secondary: loop fade time.*

The **signal path** is fixed: `Input → Effects → Pitch Modulation → Reverb → Filter → Output`, with the **Looper routable pre- or post-FX**. The four engine categories:

**MICRO LOOP** (layers of short loops at various speeds → new rhythms/tonal colors):
- **MOSAIC** — overlapping loops at multiple speeds. *A:* normal + double (octave-up harmonies); *B:* normal + half (octave-down); *C:* all double-speed; *D:* half/normal/double/quad (octave-down to 2 octaves up). Activity = number of active loopers.
- **SEQ** — short samples rearranged into new rhythmic sequences (filtered/shuffled rhythms, bit-crushed sub-octave layers at D).
- **GLIDE** — short overlapping loops shift pitch over time (A: half↔normal, B: double↔half, C: normal↔double, D: both directions at once). Shape = glide pattern.

**GRANULES** (fragments build atmospheres/textures):
- **HAZE** — clusters of grains form a wash of sound. Activity = grain density and spread.
- **TUNNEL** — cyclical micro-loops generate **hypnotic drones** with modifiers (A: compress/lengthen, B: sub-octave drone w/ filter sweeps, C: resonant bandpass, D: envelope-triggered). Activity = modifier depth. *This is the drone engine.*
- **STRUM** — rhythmic chains of recent note onsets → pointillistic textures (A: repeats most recent note; C/D: cascading chains, D adds double-speed grains).

**GLITCH** (real-time rearrangements at random/controlled intervals):
- **BLOCKS** — incoming audio triggers predictable glitches/random bursts (pitch-shifts at B, bit-crush at D).
- **INTERRUPT** — glitches interrupt the dry signal with pitch-shifted bursts and micro-montages. **At Mix 100% the dry signal is muted entirely.** Repeats = how often glitches fire.
- **ARP** — sequences recent note onsets into arpeggios (Activity = number of steps; random filters at C, bit-crush at D).

**MULTIDELAY** (a multi-tap delay line):
- **PATTERN** — taps arranged into 4 rhythmic patterns (A = classic linear delay). Activity = number of active taps.
- **WARP** — taps manipulated with filters + pitch-shifting for spacious texture (A: envelope filter, B: resonant bandpass, C: pitch-shift, D: cross-fade with double-speed grains).

**Reverb** (Space secondary): **A Bright Room · B Dark Medium · C Large Hall · D Ambient.** **Pitch Modulation, Reverb, and Filter stay active even in Looper-Only mode** — important for the rig.

## 3. Sonic Character

The Microcosm's signature is that it produces *intentional-sounding* artifacts. Granular pedals can sound like a buffer underrun; the Microcosm's grain windows, crossfades, and built-in reverb glue everything into something musical. [Sound On Sound](https://www.soundonsound.com/reviews/hologram-electronics-microcosm) describes it transforming input into "something sounding more magical… expansive pads, deep drones, tempo-locked rhythms or loop-based ambience." [Guitar World](https://www.guitarworld.com/reviews/hologram-electronics-microcosm-review) is blunter: the sounds are "anything but subtle."

Two clear poles:
- **Rhythmic / pulsing engines** — Mosaic, Seq, Pattern, Arp, Blocks. Tap-tempo-locked, these turn a single sustained chord into a sequenced, evolving rhythmic bed. With Subdiv synced to MIDI clock they lock to the rest of the board.
- **Ambient / smeared engines** — Haze, Tunnel, Warp, Glide. These dissolve transients into glacial washes and drones, no rhythmic grid required.

The onboard reverb is generous to the point of being "quite heavy-handed" (SOS), which suits this rig — and the resonant low-pass filter on the output is the tone-shaping safety valve that keeps granular fizz from getting brittle in the high end (relevant for banjo, see §6).

## 4. Behavioral Notes

- **Hold Sampler (right footswitch):** freezes the most recent slice of playing into a continuous playback cycle. Critically, **the held sample keeps feeding the effects section** — so you can freeze a chord and then *change engines, twist Activity/Repeats, sweep the filter* over a sustaining drone. Mix in dry to play lead over the held bed. Configurable Toggle or Momentary in Global Config. This is the single most powerful drone-generation feature on the pedal and the reason it belongs in a doom/drone rig.
- **Freeze vs. Looper:** Hold Sampler = instant, gestural, non-destructive freeze. The Phrase Looper = structured, overdubbable, saveable. They're different tools; Hold for live drones, Looper for built compositions. (Activating the Looper clears the Hold buffer; the two aren't simultaneous.)
- **Reaction to sustained vs. transient input:** Sustained input (fuzz walls, bowed swells, VG-800 pads) is the Microcosm's happy place — the granular engines have a continuous source to sample, so Haze/Tunnel/Mosaic sound dense and seamless. Transient/percussive input (plucked banjo, staccato playing) drives the onset-detection engines (Strum, Arp, Blocks, Interrupt) — these *want* clear note attacks to chain into arpeggios and bursts. Match the engine to the source.
- **Looper layering:** infinite overdubs onto a 60-second base loop; Undo retains the initial phrase. Pre-FX routing records dry and re-processes the loop live; Post-FX (default) prints the effect into the loop. Quantize trims loops to the nearest beat for sync.

## 5. Signal-Chain Placement — Board 2 Granular Core

The Board 2 order is `(stereo in) → OBNE Parting → CB Lost & Found → Microcosm → Walrus QI Etherealizer → OBNE Dark Star V3 → (stereo out)`. Observations for this exact slot:

- **Stereo in is mandatory here.** Board 1 goes stereo at the CE-2W and Deco V2, so the Microcosm must be set to **Stereo Input** in Global Config** (it defaults to Mono). Use a TRS cable into the MONO/STEREO TRS INPUT and L+R out. Get this wrong and you collapse the carefully built stereo image to mono before it even hits the granular engine.
- **Parting + Lost & Found feeding in:** Parting's filter and Lost & Found's random momentary gating arrive *before* the granular sampling. That's the right order — you're shaping and chopping the source, then the Microcosm samples that already-mangled signal. Lost & Found's random cuts will create grain-start variation that the Microcosm turns into rhythmic surprise.
- **Etherealizer + Dark Star V3 catching the output:** this is the "smear out" half of the board's mandate. The Microcosm generates the granular event; the Walrus QI Etherealizer (octave/pitch-reverb) and OBNE Dark Star V3 (a granular/diffusion reverb in its own right) blur it into a wall. **Watch for granular-into-granular mud** — Dark Star is itself a smear machine, so when the Microcosm is already in Haze/Tunnel, pull Dark Star back to a wash rather than a second full granular layer.
- **The fuzz-wall handoff from Board 1:** the Hizumitas dossier explicitly calls out feeding sustained fuzz into the Microcosm — that signal arrives here via the stereo split. A Hizumitas/Longsword wall hitting Mosaic or Tunnel is the rig's headline texture: dense, sustained, octave-stacked, frozen-able.

## 6. Source-Specific Notes

- **Banjo-as-lead (EBM-5 + GK-5 → VG-800):** the central idea. Banjo's fast attack and fast decay are *perfect* for the onset-detection engines — **Strum** and **Arp** chain banjo plucks into cascading pointillistic runs and arpeggios that sustain far past the instrument's natural decay, effectively turning a banjo into a lead voice with infinite tail. For drones, freeze a banjo roll with the Hold Sampler into Tunnel. The output low-pass **Filter is the key control** — banjo's piercing 2–4 kHz content will make the grains brittle, so back the Filter off CCW from full to tame it.
- **Baritone Jazzmaster drones:** low, sustained, harmonically rich — ideal for Tunnel (sub-octave drone, mode B) and Haze. The baritone's extended low end gives the granular engine deep fundamentals to stretch.
- **Modeled VG-800 pads:** when the VG-800 outputs a continuous synth/COSM pad, the Microcosm has an unbroken source to granulate — Mosaic and Haze sound seamless and orchestral. This is the cleanest path to the "huge ambient bed" sound without needing the fuzz.
- **Bass (Jazz Bass):** Multidelay/Pattern for rhythmic dub-style taps; keep Activity low and Filter rolled back so the granular content doesn't smear the low end into mud.

## 7. Famous Users (honest)

- **Ed O'Brien (Radiohead)** — the Microcosm appears on his **2025 Radiohead tour pedalboard** per TheGigRig's board breakdown. Directly relevant: this repo contains Radiohead song work, and O'Brien's ambient/textural guitar role is exactly the use case here. (Reported via gear-tour coverage; treat as well-sourced but secondhand.)
- **Sean Shibe** — classical guitarist; uses the Microcosm on his *Lost & Found* album, notably reinterpreting **Hildegard von Bingen** into a "psychedelic swirl of celestial light" ([Pentatone](https://www.pentatonemusic.com/product/lost-found/), [Art Muse London](https://artmuselondon.com/2022/09/26/sound-and-visions-sean-shibe-lost-and-found/)).
- Widely cited (Equipboard, marketing copy) attributions to **Noel Gallagher** and **Wes Borland** circulate but are **less rigorously sourced** — flag as unverified.

Beyond named artists, the Microcosm's real user base is the ambient/experimental/post-rock community — [Engadget](https://www.engadget.com/hologram-electronics-microcosm-guitar-effect-pedal-review-ambient-music-170002707.html) framed it as "a cheat code for making ambient music," which is the honest center of its reputation.

## 8. Live / Power / I/O

- **Power:** 9V DC, center-negative, 2.1mm barrel. The manual specifies a **400 mA minimum** supply; Hologram and resellers recommend an **isolated supply with ~450 mA+ of headroom** for clean operation. **The brief's "~300 mA" figure is too low** — budget at least 400 mA, ideally 500 mA, on an isolated output. Daisy-chaining or underpowering causes noise and glitches.
- **I/O:** Mono/Stereo TRS Input, Output L (mono-sum), Output R, EXP IN, MIDI In, MIDI Out/Thru. **Stereo in must be enabled in Global Config** (defaults mono).
- **Bypass:** three options in Global Config — **Buffered Bypass (no trails), Buffered Bypass + Trails, or True Bypass** (dual electromechanical relays, L/R independent). **Trails Mode is unavailable in True Bypass.** For a stereo ambient board you almost certainly want **Buffered + Trails** so frozen drones and loops decay naturally on disengage.
- **MIDI Clock:** receives clock via MIDI IN — on a MIDI Start it switches from internal to external clock; MIDI Stop reverts to internal. **It also transmits MIDI clock via MIDI OUT.** Tap Tempo is disabled while slaved to external clock. Listens on Channel 1 by default; full CC and Program Change maps (PC #1–44 for engines A–D, PC #45–60 for the 16 user presets).
- **Expression:** EXP IN assignable to Activity, Shape, Filter, Mix, Repeats, Space, or Loop Level. Assignment persists across power cycles.
- **Presets:** 16 user slots in 4 color banks — saves all parameters **and the recorded loop** (overdubs mixed down). Global Config settings are *not* saved per preset.
- **Footprint:** **7.1 × 4.7 × 2.0 in** — a large enclosure, genuinely the centerpiece of the board (Strymon Big Sky territory). Plan real estate accordingly.

## 9. Pairing Recommendations (by name)

- **Sustained dirt in (Hizumitas / Longsword / VG-800 pads):** the canonical input. The Hizumitas dossier already flags feeding its sustained wall here — Mosaic/Tunnel/Haze on a fuzz wall is the rig's signature texture. VG-800 synth pads are the cleanest seamless-bed source.
- **Into QI Etherealizer + Dark Star V3:** the smear stage. Let the Microcosm be the *event generator* and these two the *diffusers* — don't run all three at maximum granular or you get undefined mush. Microcosm rhythmic engine → Etherealizer pitch-shimmer → Dark Star wash is the cleanest division of labor.
- **Looper vs. CB Blooper (Board 3):** **address the redundancy honestly.** Both loop; they are not the same tool. The Microcosm's looper is *granular-native* — it records the granular output (or pre-FX source) and is best for capturing evolving ambient beds you build *inside* the Microcosm. The **Blooper** is a dedicated, deeply modifiable looper (stability modifiers, layer manipulation, smaller footprint) better suited to structured song-loop performance and live overdub stacking. **Recommendation:** use the Microcosm's looper opportunistically for granular bed-capture and the Hold Sampler for live freezes; reserve the Blooper as the rig's "real" performance looper. Don't try to make the Microcosm replace the Blooper — its strength is the *effects*, not the looper.
- **MIDI clock with the CB / board ecosystem:** the Microcosm can sit in the rig's MIDI clock chain (it both receives and transmits). The Chase Bliss pedals (Generation Loss, Big Time, MOOD MkII, Blooper) and Board 3's H90 all sync to MIDI clock — slaving the Microcosm's rhythmic engines (Mosaic/Pattern/Arp) to the same clock locks its pulses to the delays/loopers downstream. Decide on **one clock master** for the rig (a central MIDI controller or the H90) and slave the Microcosm to it; don't let two pedals fight to be master.

## 10. Reviews & Demos

- [Sound On Sound — Microcosm review](https://www.soundonsound.com/reviews/hologram-electronics-microcosm) — best technical/architectural overview; praises the manual and logical UI.
- [Guitar World — Microcosm review](https://www.guitarworld.com/reviews/hologram-electronics-microcosm-review) — best on the "inspirational, anything-but-subtle" character.
- [Engadget — "a cheat code for making ambient music"](https://www.engadget.com/hologram-electronics-microcosm-guitar-effect-pedal-review-ambient-music-170002707.html) — honest framing of its reputation.
- [Magnetic Magazine — "A Gift From Above to Delay Lovers and Ambient Producers"](https://magneticmag.com/2022/10/hologram-electronics-microcosm-review/) — producer/electronic perspective.
- [SINESQUARES — long-form review](https://www.sinesquares.net/musicgear/hologram-electronics-microcosm-review) — deep dive on engines.
- [Waveform Magazine — Microcosm review](https://waveformmagazine.com/waveform-reviews/microcosm-hologram-electronics/) — synth/modular angle.
- [Joseph Allen Music — demo & review](https://josephallenmusic.com/2023/12/28/hologram-microcosm-demo/) — practical demo.
- [Hologram official product page](https://www.hologramelectronics.com/products/microcosm) — feature list, walkthrough videos.

## 11. Mods / Quirks / Firmware / Known Issues

- **Firmware:** latest is **v1.13 (May 2022)**; no v2.0 exists. Updates via MIDI/SysEx. Early onset-triggering quirks (Strum/Arp/Glitch firing erratically) improved on later firmware; if the pedal is on v1.1, update it.
- **Power-sensitivity is the #1 real-world issue.** Underpowered or daisy-chained supplies cause noise, glitches, and triggering errors that get misdiagnosed as the pedal misbehaving. Always isolated, always ≥400 mA.
- **Mono-by-default trap:** ships in Mono Input mode. In this stereo rig you *must* switch to Stereo Input in Global Config or you lose the stereo image.
- **No dedicated dual L/R input jacks** — single TRS for stereo in (SOS's one stated con). Requires a proper TRS-split cable.
- **Looper clears Hold Sampler** — the two big "capture" features aren't usable simultaneously; know which mode you're in.
- **100% Mix on Interrupt mutes dry** — by design; the dry returns as Mix drops below 100%.
- **Steep learning curve** — universally noted. 44 variations × deep secondary controls × global config = a lot to internalize. The flip side (per SOS) is that the manual is genuinely excellent and hidden features are minimal.
- No widely reported hardware failures; build quality is solid.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Effects | 11 engines × 4 variations = 44 preset variations |
| Categories | Micro Loop · Granules · Glitch · Multidelay |
| Reverb | 4 stereo modes (Bright Room / Dark Medium / Large Hall / Ambient) |
| Other DSP | Pitch Modulation, resonant Low-Pass Filter, Hold Sampler |
| Looper | 60-second stereo Phrase Looper, infinite overdubs, pre/post-FX routable |
| User presets | 16 slots (4 color banks), saves settings + loop |
| Power | 9V DC, center-negative, 2.1mm barrel |
| Current draw | **400 mA minimum** supply (isolated, ~450 mA+ recommended) |
| I/O | Mono/Stereo TRS Input, Output L (mono-sum), Output R |
| Expression | EXP IN, assignable to 7 parameters |
| MIDI | In / Out / Thru; receives **and transmits** MIDI Clock; CC + PC; firmware via MIDI |
| Bypass | True Bypass (relay) / Buffered (no trails) / Buffered + Trails |
| Tap tempo | Yes (disabled when slaved to external MIDI clock) |
| Dimensions | 7.1 × 4.7 × 2.0 in |
| Firmware (latest) | v1.13 (May 2022) |
| Warranty | 1 year |

Sources: [Hologram product page](https://www.hologramelectronics.com/products/microcosm), [firmware page](https://www.hologramelectronics.com/pages/microcosm-firmware), Microcosm manual.

## 13. Starting-Point Settings

Knob positions clock-face, viewed from above. Stereo in enabled, Buffered + Trails bypass.

**(a) Frozen drone bed** — sustained, oceanic, hold-and-evolve
- Engine: **TUNNEL B** (sub-octave drone w/ filter sweeps) or **HAZE A**
- Activity 1–2 o'clock · Repeats 12 · Shape 12 · Filter 1 o'clock (slight roll-off) · Space 2–3 o'clock · Mix 1–2 o'clock
- Feed a Hizumitas/VG-800 pad, play a chord, hit **Hold Sampler** to freeze, then twist Activity over the drone. Play lead on top with dry mixed in.

**(b) Rhythmic granular arp** — pulsing, sequenced, banjo-as-lead
- Engine: **ARP A/B** or **MOSAIC D**
- Activity 12–2 · Repeats 11 · Time synced to MIDI clock (or tap) · Filter 12 (tame banjo highs) · Space 11 · Mix 12
- Pluck banjo rolls; the engine chains onsets into sustaining arpeggiated runs locked to the board's clock.

**(c) Ambient smear wash** — glacial, diffuse, into the smear stage
- Engine: **HAZE B** or **WARP B** (resonant bandpass)
- Activity 1 o'clock · Shape 1 (slow envelope) · Filter 11–12 · Space 3 o'clock (mostly wet) · Mix 1 o'clock
- Let QI Etherealizer + Dark Star V3 catch the output; pull Dark Star back so it diffuses rather than double-granulates.

**(d) Looped banjo layers** — built composition
- Engine: **MOSAIC A** (octave-up harmonies), Looper **Post-FX**, **Quantize on**
- Activity 11 · Mix 12 · Loop Level 12
- Record a banjo phrase (left footswitch), close the loop, overdub octave-stacked layers. For *structured* song loops, prefer the **CB Blooper** downstream — use this for granular bed-building only.

## 14. Versus Alternatives — Why It Earns the Board-2 Slot

- **Chase Bliss MOOD MkII** (already on Board 3) — a micro-looper + dual-effect that overlaps conceptually. The MOOD is more immediate and gestural but shallower; it uses dip switches and is more of a "happy accident" machine. The Microcosm has far more engines, a real UI, true stereo, and a proper reverb/filter back end. They're complementary, not redundant — MOOD for spontaneous chaos on Board 3, Microcosm for *designed* granular texture on Board 2.
- **Chase Bliss Blooper** (on Board 3) — a dedicated looper, not a granular effect. As covered in §9, the Blooper is the rig's real performance looper; the Microcosm's looper is a granular-capture bonus. No real competition — different jobs.
- **Hologram Chroma Console** (sibling, Board 3) — Hologram's later multi-effect "character" pedal. More of a tape/character/modulation playground; less of a dedicated granular engine. The Microcosm is the deeper, more focused *granular* tool — Chroma is the broader texture toolbox. Having both is justified by the division: granular core (Board 2) vs. character/print stage (Board 3).
- **GFI System Cabin / Red Panda Particle 2 / EHX Hog 2** — Particle 2 is the closest standalone granular competitor (smaller, mono-ish, more glitch-forward) but lacks the Microcosm's looper, multi-engine breadth, stereo reverb, and preset system. The Microcosm is the only one of these that can also *be* the looper and the ambient reverb in one box.

In *this* rig — stereo, drone/doom/shoegaze, banjo-as-lead, fuzz walls and modeled pads feeding in — the Microcosm earns the Board 2 centerpiece slot because it is simultaneously (1) the granular event-generator the board's filter/smear pedals are built to support, (2) the freeze/drone engine (Hold Sampler) that turns a sustained wall into an evolving bed, (3) the onset-chaining lead-extender for banjo, and (4) genuinely stereo with a MIDI clock that locks it to the rest of the rig. Nothing else owned does all four at once.

## Sources

- [Hologram Electronics — Microcosm product page](https://www.hologramelectronics.com/products/microcosm)
- [Hologram Electronics — Microcosm Firmware page (v1.13, May 2022)](https://www.hologramelectronics.com/pages/microcosm-firmware)
- [Hologram Electronics — Support](https://www.hologramelectronics.com/pages/support)
- Microcosm Owner's Manual (© 2020 Hologram Electronics) — local: `manuals/Microcosm.pdf`
- [Sound On Sound — Hologram Electronics Microcosm review](https://www.soundonsound.com/reviews/hologram-electronics-microcosm)
- [Guitar World — Hologram Electronics Microcosm review](https://www.guitarworld.com/reviews/hologram-electronics-microcosm-review)
- [Engadget — Microcosm review ("cheat code for ambient music")](https://www.engadget.com/hologram-electronics-microcosm-guitar-effect-pedal-review-ambient-music-170002707.html)
- [Magnetic Magazine — Microcosm review](https://magneticmag.com/2022/10/hologram-electronics-microcosm-review/)
- [SINESQUARES — Microcosm review](https://www.sinesquares.net/musicgear/hologram-electronics-microcosm-review)
- [Waveform Magazine — Microcosm review](https://waveformmagazine.com/waveform-reviews/microcosm-hologram-electronics/)
- [Joseph Allen Music — Microcosm demo & review](https://josephallenmusic.com/2023/12/28/hologram-microcosm-demo/)
- [Pentatone — Sean Shibe, *Lost & Found*](https://www.pentatonemusic.com/product/lost-found/)
- [Art Muse London — Sean Shibe, *Lost & Found*](https://artmuselondon.com/2022/09/26/sound-and-visions-sean-shibe-lost-and-found/)
- [Equipboard — Hologram Electronics Microcosm](https://equipboard.com/items/hologram-electronics-microcosm-5235c3bf-504e-4acc-b937-9ba9f1b67dac)
- [Songbird FX — Power Your Hologram Microcosm on the Go](https://www.songbirdfx.com/power-your-hologram-microcosm-on-the-go-a-complete-guide/)
