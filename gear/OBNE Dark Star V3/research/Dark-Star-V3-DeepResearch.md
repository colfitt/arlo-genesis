# Old Blood Noise Endeavors Dark Star V3 — Deep Research

A working dossier for the Dark Star V3 as the **terminus of Board 2 (Middle / Texture)** in a stereo hex-pickup banjo/baritone rig. It is the last pedal before the stereo handoff to Board 3 — sitting after the Walrus QI Etherealizer, with the Hologram Microcosm and OBNE Parting further upstream. Everything degraded, sustained, and granular that Boards 1 and 2 build up arrives here and gets smeared into a single oceanic pad before the time-and-tape stage of Board 3 takes over. A lot of this document is concerned with what happens when an *already-saturated, already-granular* stereo wall hits a reverb-as-synthesizer, and with the honest redundancy question of running Dark Star **and** the H90/Chroma reverbs downstream.

All control behavior below is confirmed against the manual at `manuals/OBNE Dark Star v3.pdf`. Web claims are cited inline; OBNE coverage is thinner than EQD's, so unverified items are flagged.

## 1. Lineage: Dark Star → Dark Star Stereo (V3), the "pad reverb" idea

Dark Star is OBNE's most popular reverb and the pedal that, more than any other, defined the "pad reverb" category — a reverb voiced for slow attack and synthetic pad generation rather than room emulation. The **original Dark Star** (a mono pedal from roughly 2019–2020) was a three-algorithm reverb with a toggle selecting between three *separate and independent* modes — **Pitch / Crush / Delay** — wrapped around one long-trail, warm, deliberately aliased core voice ([Guitar Pedal X](https://www.guitarpedalx.com/news/news/old-blood-noise-endeavors-levels-up-and-stereofies-its-favourite-flagship-dark-star-soundscape-textured-reverb)). Players bonded with its warmth and aliasing and "the way it encouraged you to turn the mix fully up" (manual, p.2).

The current pedal — sold as **Dark Star Stereo**, branded **Dark Star V3** by most retailers (Perfect Circuit, Empire Guitars, The Midium) — is a ground-up expansion. The crucial architectural change: it **collapses the three-mode toggle into a single voice** where pitch, crush, and delay all run *simultaneously and continuously*, "with more options and a far higher degree of granularity" ([Guitar Pedal X](https://www.guitarpedalx.com/news/news/old-blood-noise-endeavors-levels-up-and-stereofies-its-favourite-flagship-dark-star-soundscape-textured-reverb)). On top of that it adds **full stereo I/O, a Filter, a Multiply feedback loop, Lag predelay, Stereo Spread, three onboard presets, expression over every knob, and MIDI** (manual, pp.2–5).

> Naming caveat: the version mythology is muddy. OBNE's own product page calls it simply **Dark Star Stereo** ($329, [oldbloodnoise.com](https://oldbloodnoise.com/pedals/p/dark-star-stereo)); it launched at $299 ([Guitar Pedal X](https://www.guitarpedalx.com/news/news/old-blood-noise-endeavors-levels-up-and-stereofies-its-favourite-flagship-dark-star-soundscape-textured-reverb)). Premier Guitar describes it as the "third iteration (following mono Dark Star and Dark Star V2)" ([Premier Guitar](https://www.premierguitar.com/gear/reviews/old-blood-noise-dark-star)), while some Reverb listings tag the Stereo edition itself as "V2." There is **no standalone "Dark Star Mini"** in OBNE's line as of this writing — that's a model name to treat as unverified/non-existent. The owner's pedal is the stereo, preset, MIDI-capable unit; that is the only thing the rig needs to be true.

## 2. Controls

The face plate carries **eight knobs in two rows**, a **Volume / Mix / Spread** column on the left, a **Presets** button with three LEDs, and **two footswitches** (Aux / On-Off). All knob descriptions are from the manual (p.2).

**Top row:**
- **Filter** — bipolar. At noon it gently rolls highs (the original Dark Star's native response). Below noon it's a **low-pass** whose cutoff drops until no signal passes (fully closed = silence). Above noon it becomes a **high-pass** that climbs to cut lows and low-mids. One knob, two filter types, useful as a wet-only tone shaper.
- **Pitch 1** — pitch shift on the **Left** channel. Noon = unity (bypassed). Near noon = slight detune up/down. Further out it snaps to **semitones**, then **±1 octave**, with **±2 octave** settings at the extremes.
- **Pitch 2** — same behavior on the **Right** channel. Note: **in mono mode**, if Pitch 2 isn't at noon it's added *in parallel* to Pitch 1 — recreating the original Dark Star's dual-interval Pitch mode.
- **Crush** — bipolar distortion. Noon = clean. Below noon = **sample-rate reduction / bit-crush aliasing** (the original Crush mode). Above noon = a **soft-clipping overdrive** in the reverb with increasing gain.

**Bottom row:**
- **Lag** — **predelay** time; lets the reverb trail start well after the note.
- **Multiply** — global **feedback** into the whole system; intensifies every effect and enables **self-oscillation** at higher settings.
- **Decay** — reverb decay, from very short to **nearly infinite**.
- *(Crush sits above; the bottom-row fourth position is Decay.)*

**Left column:**
- **Volume** — overall output level.
- **Mix** — wet/dry, 100% dry to 100% wet, roughly unity at center. **Analog dry-through**: the dry path is never digitized and has **zero latency**.
- **Spread** — stereo image. Full up = normal (L reverb left, R reverb right). Center = both signals summed to both outs. Full down = **fully reversed** (L on right out, R on left). A continuous L/R crossfade, not a width knob.

**Footswitches:** **On/Off** (tap-latch, hold-momentary) and **Aux** (assignable — see §4).

## 3. Sonic character

Premier Guitar's framing is the right one: this is **"a reverb-based synthesizer,"** not a room emulator ([Premier Guitar](https://www.premierguitar.com/gear/reviews/old-blood-noise-dark-star), 4.6/5). At neutral settings it makes responsive, **textural pads** the review explicitly likens to Harold Budd and Brian Eno. The native voice is warm, long-trailed, and slightly aliased — "lo-fi" by design, "as synthetic as but less sparkly than a shimmer" ([Effects Database](https://www.effectsdatabase.com/model/oldbloodnoise/darkstar/stereo)).

The voicing levers:
- **Pitch shifters** give a quantized **four-octave span** in half-steps across the two knobs. Subtle settings thicken (octave-up sparkle, octave-down weight); extreme settings turn into "orchestral," detuned, faintly seasick clusters. The detune zone right around noon is where the pad gets its chorused shimmer without committing to an interval.
- **Crush** is the degradation engine. Counter-clockwise pulls bit-rate down toward "early samplers to cell phones" grit; clockwise adds overdrive saturation into the tail. This is the control that makes Dark Star read as *broken/lo-fi* rather than hi-fi ambient.
- **Filter** keeps the wash from getting muddy or shrill — LPF to sink the pad under the dry signal, HPF to make a thin, glassy bed.

Net: it occupies the **dark, degraded, synthetic** end of ambient reverb. It is not a pristine hall. That is exactly why it earns a slot in a drone/doom/shoegaze rig built around degraded sustained walls.

## 4. Behavioral notes (freeze/hold, self-oscillation, expression)

- **Hold / freeze (Aux).** Holding Aux (when assigned to Hold) creates **nearly infinite sustain** — it maxes Decay beyond the knob and **blocks new input**, so the current wash freezes into a static bed; releasing returns Decay to its prior setting (manual, p.3). This is the **frozen-drone footswitch** and the single most performance-critical feature for this rig.
- **Aux is one of three assignable jobs:** **Hold** (freeze), **Filter** (slams the low-pass closed while held — a swell/duck move), or **Pitch** (jumps both pitch shifters to **+1 octave** while held). Assign by holding Aux and moving the related knob (Decay / Filter / Pitch 1); saved per preset.
- **Self-oscillation.** **Multiply** feeds the system back on itself; at high Decay + Multiply the pedal builds runaway sustained textures. Premier Guitar's warning is apt: "spend too much time there and you might need a name for your new ambient band."
- **Expression.** The **TRS expression jack** can map **any combination of knobs** with custom heel/toe endpoints: hold On/Off, sweep the knob(s) from start to end position, release. Knobs you don't move are unaffected. Saved per preset. (The owner already runs expression on the Parting and Microcosm upstream — same workflow.)
- **Aux doubles as a preset stepper:** tap Preset while holding Aux to cycle presets from the Aux switch.

## 5. Signal-chain placement — Board 2 terminus

Board 2 order: `OBNE Parting → CB Lost & Found → Hologram Microcosm → Walrus QI Etherealizer → **Dark Star V3** → (stereo to Board 3)`. Observations for this exact slot:

- **It is correctly placed last.** Dark Star wants a developed, stable signal to smear, and that's precisely what arrives: filtered (Parting), randomized (Lost & Found), granular (Microcosm), already-ambient (QI Etherealizer). Putting the pad reverb at the end means everything upstream becomes *source material* for the wash rather than something competing with it.
- **Stereo handoff.** Because it's the last stereo device on Board 2, set **Routing = Stereo** (hold On/Off + Preset to cycle Mono / Mono-In-Stereo-Out / Stereo; manual p.3). The Spread knob then determines how the L/R image lands on Board 3's stereo chain. Keep Spread up (normal) unless you specifically want the reversed-image disorientation.
- **Trails on.** With Generation Loss → … → H90 downstream, you almost certainly want **trails enabled** (global setting; manual p.3) so the pad doesn't hard-cut when you bypass — Board 3 keeps chewing the tail.
- **Stacking with QI Etherealizer immediately upstream.** The QI is itself an ambient/reverb texture box. Running it *into* Dark Star is additive smear, not redundancy — let QI shape the pre-reverb texture, let Dark Star be the long-trail terminus. If it gets soupy, pull Dark Star's **Mix** back toward unity and use **Filter** (LPF) to seat the pad under the QI's output.
- **Microcosm two slots up** gives Dark Star granular/glitch grain to reverberate; the pad makes the Microcosm's chopped output sound intentional rather than stuttery — the same trick the Hizumitas's sustain pulls for granular pedals on Board 1.

## 6. Source-specific notes (banjo, baritone, VG-800, bass)

This pedal sees the **summed, modeled, stereo** output of Board 1 — never a raw pickup — so its behavior is dominated by what the VG-800 and the dirt/mod stages did first.

- **GK-5 banjo (EBM-5).** Banjo transients are fast-attack/fast-decay; Dark Star's **Lag + Decay** are the antidote — predelay the wash so the dry pluck speaks, then let an infinite-ish tail bloom behind it. **Hold/freeze** turns a single banjo roll into a static drone bed for banjo-as-lead lines over the top. Watch brightness: banjo content sits high, so favor the **LPF side of Filter** and avoid big octave-**up** Pitch settings that ice-pick.
- **Baritone Jazzmaster.** Home territory. Octave-**down** Pitch (one or both shifters) on a baritone drone produces genuinely subterranean doom-pad weight. Crush below noon adds the degraded edge.
- **VG-800 modeled/synth patches.** When Board 1 outputs synth/pad COSM patches, Dark Star reverberating an already-continuous waveform makes the most seamless walls in the rig — no transient to smear, just sustain into sustain. Polyphonic guitar-synth patches will artifact under heavy Pitch/Crush, which for this aesthetic is a feature.
- **Bass (Jazz Bass).** Use sparingly: the **analog dry-through** keeps low-end punch intact while a low-mixed, LPF'd, octave-down pad sits underneath. Keep Mix well below unity so the fundamental stays defined.

## 7. Famous users (honest)

OBNE coverage is thin and **artist documentation for Dark Star specifically is sparse** — treat this section as low-confidence. The pedal is a known quantity in ambient/post-rock/shoegaze circles, and gear roundups consistently place it among OBNE's flagship pedals ([DeathCloud, "Top OBNE Pedals"](https://deathcloud.com/blogs/guitar-gear-articles/10-obne-pedals-to-try-in-2025)). Specific named users surface only in passing (e.g., guitarist James Duke posting about the Dark Star on Instagram per search aggregation) and could not be firmly verified from primary sources. **No marquee signature artist is reliably attributable.** The honest read: this is a pedal whose reputation lives in the ambient/experimental community and on countless atmospheric pedalboards rather than on one famous player's board. Anyone claiming a definitive artist roster is guessing.

## 8. Live / power / I/O

- **Power: 9V DC center-negative, 2.1mm — 350 mA** (manual, p.3; [OBNE](https://oldbloodnoise.com/pedals/p/dark-star-stereo)). This is a **heavy draw** — 35× the Hizumitas. It needs a high-current isolated outlet (e.g., a 500 mA digital slot on a Cioks/Strymon-class supply). Do not assume a generic 100 mA slot will run it.
- **I/O: true stereo in / stereo out**, plus **MIDI In + MIDI Out** as **3.5mm TRS Type A**, a **USB-C** jack (firmware), and a **TRS Expression** jack.
- **MIDI: full CC + PC.** Default **Channel 1** (changeable via CC 102). Every knob and setting is CC-addressable (Volume 7, Mix 14, Decay 15, Pitch 1 16, Pitch 2 17, Lag 18, Crush 19, Filter 20, Multiply 21, Spread 22, Expression 11, plus switches/routing/trails). **127 presets** are reachable over **PC**; MIDI Out acts as Thru. This makes Dark Star fully recallable from a board-wide MIDI controller alongside the rig's other MIDI pedals (Microcosm upstream; Generation Loss / Big Time / MOOD / Blooper / Chroma / H90 downstream).
- **Presets: 3 onboard** (LED-indicated: top/middle/bottom = 1/2/3, none = live mode); save by holding Preset 5 s. Aux/Expression settings save *per preset*.
- **Bypass: soft-touch relay; switchable true-bypass or trails** (global). Like most relay bypass, it needs power to pass signal.
- **Routing modes:** Mono / Mono-In-Stereo-Out / Stereo (global).

> ⚠️ **GearProfile.md correction:** the profile front-matter says `midi: false`. The manual is explicit that the V3 has **MIDI In/Out (3.5mm TRS Type A), Channel 1 default, full CC + PC**. The profile should read `midi: true`.

## 9. Pairing recommendations (by name)

**Immediately upstream (Board 2):**
- **Walrus QI Etherealizer →** lets QI build the pre-reverb ambient texture; Dark Star is the long-trail closer. Don't double the "lush" — assign one role each.
- **Hologram Microcosm (2 up) →** granular grain into pad reverb is a documented win; freeze a Microcosm phrase, then Hold on Dark Star to stack two static beds.
- **OBNE Parting (board opener) →** OBNE-ecosystem bookends. Parting's filter/swell at the front and Dark Star's pad at the back are a natural matched pair; if you ever go MIDI-deep, both expose expression/CC for synced sweeps.

**Downstream (Board 3) — the redundancy question:**
- **vs Eventide H90 + Hologram Chroma Console.** This is the honest one. You have *three* reverb-capable boxes. They are **not redundant if you assign lanes**: Dark Star = the **degraded, pitched, self-oscillating pad** at the *source* of the texture board; H90 = clean/algorithmic hall, shimmer, and spectral processing (BlackHole, MangledVerb) at the *end*; Chroma = lo-fi character/modulation reverb in the print stage. Dark Star feeding H90 means H90 processes an *already-pad* signal — spectral reverb on a pad is a different sound than spectral reverb on a dry note. If you want to thin the herd, the overlap is **Dark Star vs Chroma** (both lo-fi), not Dark Star vs H90.
- **Into Generation Loss → Big Time → MOOD → Blooper:** Dark Star's sustained pad is ideal loop/delay fodder — Blooper capturing a frozen Dark Star drone is exactly this rig's stated aesthetic.

**The signature move:** sustained fuzz on Board 1 (Hizumitas/Longsword) → … → Dark Star pad here. That fuzz-wall-into-pad-reverb path is the spine of the drone aesthetic; Dark Star is its terminus.

## 10. Reviews & demos

- [Premier Guitar — Dark Star Stereo review](https://www.premierguitar.com/gear/reviews/old-blood-noise-dark-star) — 4.6/5; the "reverb-based synthesizer" framing, best written review.
- [Guitar Pedal X — Dark Star Stereo announcement / lineage](https://www.guitarpedalx.com/news/news/old-blood-noise-endeavors-levels-up-and-stereofies-its-favourite-flagship-dark-star-soundscape-textured-reverb) — original-3-modes vs combined-mode history, launch price.
- [Gearnews — "The Lo-Fi-iest Reverb Pedal of them all?"](https://www.gearnews.com/obne-dark-star-stereo-guitar/) — features overview.
- [Guitar Bomb — "A New Era Of Ambient Reverb"](https://guitarbomb.com/dark-star-stereo-era-ambient-reverb/) — context piece.
- [Effects Database — Dark Star Stereo entry](https://www.effectsdatabase.com/model/oldbloodnoise/darkstar/stereo) — spec aggregation, the "less sparkly than a shimmer" line.
- [OBNE official product page](https://oldbloodnoise.com/pedals/p/dark-star-stereo) — authoritative specs, $329.
- [Perfect Circuit — Dark Star V3 listing](https://www.perfectcircuit.com/old-blood-noise-dark-star-v3.html) — retailer feature summary.

## 11. Mods / quirks / firmware

- **Firmware via USB-C** at https://firmware.oldbloodnoise.com. Patch history: **V3.0J** initial → **V3.0K** fixed pot-override on preset recall → **V3.0L** faster processing / memory routines → **V3.0M** fixed unity-pitch preset recall → **V3.0Q** fixed pitch-recall regressions from 3.0M and improved factory reset → **V3.0R** fixed a MIDI-comms hang where power-cycling an external MIDI controller halts MIDI to the Dark Star until the pedal is also restarted (OBNE updater changelog, verified 2026-06). **Keep it on V3.0R** — the K/M/Q cluster are pitch-preset bugs that directly affect a preset-driven board, and R's fix matters for any board-wide MIDI controller. Check the owner's installed version.
- **Quirks worth knowing:** Filter fully counter-clockwise = **complete silence** (it's a closeable LPF, not just a tone roll) — surprises people. Pitch is **stepped/quantized**, so small knob moves near the octave boundaries snap; for smooth detune, stay in the wide center "Detune" zone (CC 42–85). **Mono-mode Pitch 2** behaves differently than stereo (parallel-summed) — don't expect identical results when you collapse routing.
- **Factory reset:** hold On/Off + Aux 10 s, confirm with Aux. Wipes all presets/settings.
- No widely reported hardware failures; OBNE build quality is solid boutique-tier. No common analog mods (it's a DSP pedal).

## 12. Spec sheet

| Spec | Value |
|---|---|
| Type | Stereo lo-fi pad/soundscape reverb w/ dual pitch shift + bit-crush/OD + predelay |
| Power | 9V DC center-negative, 2.1mm |
| Current draw | **350 mA** (high — needs digital/high-current slot) |
| I/O | Stereo in / stereo out; analog dry-through (zero-latency dry) |
| MIDI | **Yes** — In + Out, 3.5mm TRS Type A; default Ch 1; full CC + PC |
| Presets | 3 onboard (LED) / 127 via MIDI PC |
| Expression | TRS jack; any-knob assignment, custom heel/toe, per-preset |
| Firmware | USB-C; latest known **V3.0R** (MIDI-hang fix; supersedes V3.0Q) |
| Bypass | Soft-touch relay; switchable true-bypass / trails (global) |
| Routing | Mono / Mono-In-Stereo-Out / Stereo (global) |
| Controls | Filter, Pitch 1, Pitch 2, Crush, Lag, Multiply, Decay, Volume, Mix, Spread + Aux/On-Off |
| Pitch range | ±2 octaves per shifter, quantized semitones + detune zone |
| Dimensions | 4.25" W × 5" H × 2" D ([OBNE](https://oldbloodnoise.com/pedals/p/dark-star-stereo)) |
| Price | $329 (launched $299) |
| Warranty | OBNE standard |

Source: [OBNE Dark Star Stereo page](https://oldbloodnoise.com/pedals/p/dark-star-stereo) + `manuals/OBNE Dark Star v3.pdf`.

## 13. Starting-point settings

Clock-face positions, viewed from above. All assume **Stereo routing, trails on**.

**(a) Infinite shimmer drone** — endless, rising, glassy
- Mix: 2–3 (mostly wet) · Decay: 4–5 (near infinite) · Multiply: 1–2 · Filter: 1 (HPF, glassy) · Pitch 1: +1 oct · Pitch 2: +1 oct (or +12 right, detune left) · Crush: 12 (clean) · Lag: 11
- Aux → **Hold**. Strum a baritone chord, freeze, let it ring under banjo leads.

**(b) Octave-down doom pad** — subterranean, heavy
- Mix: 1 · Decay: 3 · Multiply: 11 · Filter: 10 (LPF, dark) · Pitch 1: −1 oct · Pitch 2: −1 oct (or −2 on one side) · Crush: 11 (light bit-crush) · Lag: 12
- Pair with sustained fuzz upstream (Hizumitas wall) and an octave-down VG-800 baritone patch.

**(c) Crushed ambient wash** — degraded, lo-fi, "recorded wrong"
- Mix: 12 (unity blend) · Decay: 2 · Multiply: 10 · Filter: 11 · Pitch 1: detune up · Pitch 2: detune down (chorused width) · Crush: 9 (heavy sample-rate reduction) · Lag: 1
- Let the Microcosm's granular output feed it; this is the QI → Dark Star lo-fi terminus.

**(d) Frozen banjo bed** — static drone under a lead
- Mix: 1 · Decay: 12 (you'll freeze it) · Multiply: 12 · Filter: 12 · Pitch: noon/noon (clean bed) or +12 right for sparkle · Crush: 12 · Lag: 1
- Aux → **Hold**. Play a banjo roll, **freeze**, then solo over the static pad. The defining banjo-as-lead move.

## 14. Versus alternatives — why it earns the Board-2 terminus slot

- **Strymon Big Sky (on the bench).** Big Sky is the cleaner, more "produced," more *pristine* big-reverb. It can do shimmer and modulated halls beautifully — but it is **hi-fi by temperament**. Dark Star earns the texture-board terminus precisely because it is *lo-fi, degraded, pitched, and self-oscillating* — it adds character Big Sky sands off. Big Sky stays benched as the H90 understudy; Dark Star is not interchangeable with it.
- **Eventide H90 (Board 3).** H90 is the algorithmic powerhouse and the rig's *reverb of record*. But it lives at the **end** and is voiced clean/spectral. Dark Star at the **source** of Board 2 means H90 receives an already-textured pad. Different job, different position. Keeping both is defensible; see §9.
- **Hologram Chroma Console (Board 3).** The closest *character* overlap — both lo-fi, both modulation-flavored. If anything in the rig competes with Dark Star, it's Chroma. But Chroma is a multi-effect "character" box in the print stage; Dark Star is a dedicated **pad-generation reverb** with freeze, dual pitch, and feedback self-oscillation that Chroma's reverb engine doesn't match. They coexist by lane (source-texture vs print-character).
- **Walrus QI Etherealizer (immediately upstream).** Adjacent ambient box. QI shapes the *pre*-reverb texture; Dark Star is the *long-trail closer*. Sequential, not redundant.

In this rig — banjo/baritone, modeled VG-800 sources, drone/doom/shoegaze aesthetic, sustained fuzz walls arriving from Board 1 — Dark Star V3 earns the Board-2 terminus because it is the one box that turns *any* developed stereo signal into an **infinite, pitched, degraded pad** with a footswitch-freeze, then hands a clean stereo image to Board 3. Nothing else in the rig does the pad-generation-with-degradation job at this position. That, plus per-preset expression and full MIDI recall, is why it's the smear that closes the texture board.

## Sources

- [OBNE — Dark Star Stereo product page](https://oldbloodnoise.com/pedals/p/dark-star-stereo)
- [OBNE — original Dark Star Pad Reverb page](https://oldbloodnoise.com/pedals/p/dark-star)
- [OBNE Dark Star v3 instruction manual (local PDF)](../manuals/OBNE%20Dark%20Star%20v3.pdf)
- [OBNE firmware updater](https://firmware.oldbloodnoise.com)
- [Premier Guitar — Dark Star Stereo review (4.6/5)](https://www.premierguitar.com/gear/reviews/old-blood-noise-dark-star)
- [Guitar Pedal X — Dark Star Stereo lineage/announcement](https://www.guitarpedalx.com/news/news/old-blood-noise-endeavors-levels-up-and-stereofies-its-favourite-flagship-dark-star-soundscape-textured-reverb)
- [Gearnews — OBNE Dark Star Stereo](https://www.gearnews.com/obne-dark-star-stereo-guitar/)
- [Guitar Bomb — Dark Star Stereo: A New Era Of Ambient Reverb](https://guitarbomb.com/dark-star-stereo-era-ambient-reverb/)
- [Effects Database — Dark Star Stereo](https://www.effectsdatabase.com/model/oldbloodnoise/darkstar/stereo)
- [Perfect Circuit — Dark Star V3](https://www.perfectcircuit.com/old-blood-noise-dark-star-v3.html)
- [Empire Guitars — OBNE Dark Star V3 listing](https://empireguitars.com/products/obne-dark-star-v3-blue)
- [Equipboard — Old Blood Noise Endeavors Dark Star](https://equipboard.com/items/old-blood-noise-endeavors-dark-star)
- [DeathCloud — Top OBNE Pedals](https://deathcloud.com/blogs/guitar-gear-articles/10-obne-pedals-to-try-in-2025)
