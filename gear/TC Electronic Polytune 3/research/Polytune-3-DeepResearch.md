# TC Electronic Polytune 3 — Deep Research

A working dossier for the one true utility pedal on Board 1. The Polytune 3 sits 2nd in the chain — `VG-800 → Polytune 3 → CB Clean → Colour Box V2 → MXR 108 → Hizumitas → ...` — which means it's the first thing the signal hits after the modeler, and its switchable BonaFide buffer is effectively the first buffer in the entire three-board rig. That placement, not the tuning, is the interesting question here: whether to run the buffer on or off given a fuzz section downstream that is normally buffer-sensitive. The tuner part is, honestly, solved — it's the most accurate pedal tuner you can buy and there isn't much drama to report. The buffer-and-placement part is where this document earns its keep.

## 1. What it actually is

The Polytune 3 is the third generation of the world's first polyphonic guitar tuner (the original Polytune landed in 2010). You strum all your strings at once and a ~109-LED display shows you which strings are flat or sharp in one glance — no string-by-string hunting. It's also a full chromatic tuner and a ±0.02-cent strobe tuner. The one feature that defines the **3** versus everything before it: TC dropped the entire circuit of their standalone **BonaFide Buffer** pedal inside the box, switchable against true bypass via internal DIP switches ([Andertons](https://www.andertons.co.uk/tc-electronic-polytune-3-tuner-pedal-bonafide-buffer/), [performerlife Polytune 2 vs 3](https://performerlife.com/polytune-2-vs-polytune-3/)).

Where it sits in the family:

- **Polytune 2 → Polytune 3:** The 2 was true-bypass-only with a strobe mode and a "Total Recall" memory. The 3 adds the BonaFide buffer (the headline change), an upgraded auto-dimming display with the ambient-light sensor, and the same tuning-mode set. If you already had a 2 and a good buffer elsewhere, the 3's only real draw is consolidating the buffer into the tuner footprint ([performerlife](https://performerlife.com/polytune-2-vs-polytune-3/)).
- **Polytune 3 Mini:** Same tuning engine, same BonaFide buffer, smaller enclosure, no 9V power-out jack, fewer LEDs/smaller display. Reviewed well by [Sound On Sound](https://www.soundonsound.com/reviews/tc-electronic-polytune-3-mini). The trade is display real estate, not accuracy.
- **Polytune 3 Noir:** Cosmetic — black enclosure, otherwise identical to the standard 3.
- **Polytune Clip / Clip Noir:** Headstock clip-on. Polyphonic, strobe-capable, but obviously no buffer and no signal path — irrelevant to a pedalboard buffer discussion.

The owner's unit is the **full-size Polytune 3**, which is the right choice here specifically because of the big readable display (relevant for a board with a baritone and a banjo in low/open tunings) and the 9V power-out jack.

## 2. Controls & modes

There are no top-mounted knobs — everything is two rear buttons (Tuning Mode, Display Mode), one footswitch, and two internal DIP switches. From the [manual](manuals/polytune3.pdf):

- **Footswitch.** Tap to engage the tuner; output mutes for silent tuning. Tap again to bypass. Press-and-hold ~3 seconds toggles Drop-D mode on/off.
- **Display Mode button.** Cycles Guitar/Needle, Guitar/Strobe, Bass/Needle, Bass/Strobe. Guitar vs Bass changes the expected string set; Needle vs Strobe changes how the deviation is shown.
- **Polyphonic tuning** is automatic — "you don't [activate it], it just works." Strum, and the display shows every string at once. Pick one string and it falls back to single-note needle/strobe. TC calls this MonoPoly auto-detection.
- **Needle mode** — single-string, a column of LEDs left (flat) / right (sharp) of center, with the target note name at the bottom. The everyday mode.
- **Strobe mode** — ±0.02-cent accuracy via a rotating-segment animation that slows as you approach pitch. This is the fine-tuning/intonation tool. The marketing figure is 0.02 cent (2/10,000ths of a semitone); the *older* Polytune-era manuals quoted ±0.1 cent, and TC's own bundled PDF still carries the old figure in spots — the current spec for the **3** is ±0.02 cent strobe / 0.5 cent chromatic, confirmed by [MusicRadar](https://www.musicradar.com/reviews/tc-electronic-polytune-3-review) and TC's retail listings.
- **Alternate tunings & capo.** Tuning Mode button cycles: Standard (E), then all-strings-flat by 1–5 semitones (Eb, D, Db, C, B), then capo positions 1st–7th fret. Settings are stored across power cycles.
- **Reference pitch.** Press Display Mode + Tuning Mode together; adjust A in **1 Hz steps** (display shows e.g. "440"). Stored on power-down. No published lower/upper bound in the manual, but the standard implementation is roughly 435–445 Hz.
- **True Bypass vs Buffered** — set by two rear DIP switches (see §4). Three states: True Bypass / Buffered Bypass / Buffered Bypass with Display Always-On.

## 3. Tuning accuracy & real-world behavior

This is the part with no drama, so it'll be short. The Polytune 3 is, by spec, the most accurate pedal tuner in common use: **±0.02 cent in strobe**, 0.5 cent chromatic ([MusicRadar](https://www.musicradar.com/reviews/tc-electronic-polytune-3-review)). For context, a Boss TU-3 is ±1 cent (50x coarser than the 3's strobe), and only dedicated Peterson strobes are in the same precision class.

What that means in practice:

- **Polyphonic mode** is for *speed* — get all six strings roughly in tune in one strum between songs. It is coarser than strobe by nature; don't intonate off the poly display.
- **Strobe mode** is for *precision* — setting intonation at the bridge, matching a recorded reference, getting a drone string dead-on so beating stops. For the owner's sustained-wall aesthetic, where one slightly-off note in a held chord will beat audibly forever, strobe is the mode that matters.
- The **auto-dimming display** genuinely earns praise ([MusicRadar](https://www.musicradar.com/reviews/tc-electronic-polytune-3-review)) — bright enough for a stage, dims itself in a dark room so it isn't a beacon.
- TC's own best-accuracy tip (from the manual FAQ): tune electrics in polyphonic mode using the **neck pickup**, strummed with the thumb. The neck pickup gives a cleaner fundamental for the algorithm to lock onto. Worth noting given the rig — but see §6, because the tuner isn't seeing a pickup directly here.

## 4. The BonaFide buffer — what it does, when to engage it

The buffer inside the Polytune 3 is literally TC's standalone **BonaFide Buffer** circuit. It's an all-analog, low-noise, impedance-matching buffer: **1 MΩ input impedance, ~100 Ω output impedance, >112 dB signal-to-noise ratio, unity gain** (it doesn't boost or attenuate level — it transforms impedance) ([Sweetwater spec](https://www.sweetwater.com/store/detail/PolyTune3--tc-electronic-polytune-3-polyphonic-led-guitar-tuner-pedal-with-buffer), [Sound On Sound BonaFide review](https://www.soundonsound.com/reviews/tc-electronic-bonafide)).

What a buffer does, concretely: a high-impedance instrument signal (or here, a line-ish modeler output) loses high-frequency content as it drives long cable runs and the input capacitance of many bypassed pedals. The buffer presents a high-impedance input (so it doesn't load the source down) and re-drives the signal from a low ~100 Ω output, which sails through cable and downstream pedal inputs without treble loss. The Sound On Sound reviewer found the BonaFide "made a significant difference to the high end" and that the guitar "feels more lively" with it inline because unwanted cable capacitance no longer drags on the pickups.

**Setting the mode** (rear DIP switches, two of them, top-left under the backplate):

| DIP configuration | Mode |
|---|---|
| Both switches left | True Bypass |
| Top switch right, lower switch left | Buffered Bypass |
| Both switches right | Buffered Bypass, Display Always-On |

"Display Always-On" keeps the tuner readout live even when you're playing (signal still passes) — handy for a quick glance mid-song without muting. For a studio rig that's often a nice-to-have.

**The one caveat that matters for this rig:** Sound On Sound flags that there are "few pedals that wouldn't be happy following the BonaFide, with the possible exception of some antique **germanium** fuzz boxes that can be rather picky about what's fed into them." That is the entire crux of the placement question below — and the good news is the owner's fuzzes are **not** germanium.

## 5. Signal-chain placement — buffer on or off?

This is the load-bearing section. The Polytune 3 is the rig's **first buffer**, sitting right before the dirt section: `... Polytune 3 → CB Clean → Colour Box V2 → MXR 108 → Hizumitas → ...`. The classic worry is "never put a buffer in front of a fuzz." Here's why that worry does **not** apply to this rig:

1. **The MXR M173 Classic 108 is a *silicon* Fuzz Face (BC108 transistor), not germanium.** Silicon Fuzz Faces have higher input impedance and are far less fussy about source impedance than vintage germanium units. The germanium-fuzz-hates-buffers problem is specifically a germanium problem ([Sound On Sound BonaFide review](https://www.soundonsound.com/reviews/tc-electronic-bonafide), [MXR 108 / Reverb](https://reverb.com/item/16770387-mxr-m173-classic-108-fuzz-bc108-silicon-fuzz-face-with-wah-friendly-buffer-or-true-bypass)).
2. **The MXR 108 has its OWN built-in buffer switch.** Dunlop fitted it with a wah-friendly input buffer specifically so it tolerates buffered/wah signal in front ([Dunlop](https://www.jimdunlop.com/mxr-classic-108-fuzz/), [Reverb listing](https://reverb.com/item/16770387-mxr-m173-classic-108-fuzz-bc108-silicon-fuzz-face-with-wah-friendly-buffer-or-true-bypass)). With its buffer switch on, the 108 is essentially immune to what's upstream. With its buffer off (true-bypass mode, ~10 kΩ output when active), it's still a silicon FF and still buffer-tolerant.
3. **The EQD Hizumitas is a Big-Muff-derivative, and Muffs are buffer-tolerant by topology** — its own dossier notes it "tolerates buffers in front far better than a vintage-style fuzz." It also isn't even first in the dirt order; CB Clean and the Colour Box are between the tuner and the Hizumitas anyway.
4. **The signal the Polytune sees is the VG-800's output, not a raw pickup.** A modeler output is already a relatively low-impedance, line-ish source. The buffer has very little high-impedance loading to fix here — which is the other half of why this isn't a fraught decision.

**Recommendation: leave the Polytune 3 on True Bypass.** Reasoning specific to this rig:
- The buffering job is **already covered downstream by CB Clean**, which sits immediately after the tuner and is itself an always-on buffered Chase Bliss pedal (and your stated "1st" buffer on the board art). Two buffers back-to-back is redundant; the tuner's adds nothing CB Clean isn't already doing.
- The VG-800 source doesn't need impedance rescue.
- Keeping the tuner true-bypass means it has **zero** influence on tone when not tuning, which is the cleanest possible state for a fuzz-heavy front end, and removes any variable from the (already buffer-tolerant) fuzzes.
- **Switch the buffer ON only if** you ever remove or reposition CB Clean, run the VG-800 out passively, or notice high-end loss into the dirt section. In that case use "Buffered Bypass, Display Always-On" so you also get a glanceable tuner. It will not hurt the silicon 108 or the Hizumitas.

In short: the buffer is a genuine asset to *have*, but in this exact chain it's a backup, not a necessity — because CB Clean already buffers and the fuzzes are buffer-friendly.

## 6. Source-specific behavior

**Can it tune the VG-800's output?** Yes, with a caveat. The Polytune sees the VG-800's *summed analog output*, and as long as the VG-800 is passing a clean, monophonic-per-string guitar/modeled-guitar tone, the tuner tracks it like any instrument. Two things to watch:

- **Tune off a clean/dry-ish patch.** The manual is explicit: "place Polytune in your signal chain before your drive, distortion and vibrato pedals. A distorted or modulated signal is harder to analyze." It already *is* before all the dirt — good. But if the VG-800 patch itself has heavy modeled distortion, modulation, or a synth/COSM voice baked in, the tuner's pitch detection will struggle. Tune off a clean amp/clean-guitar model and you're fine.
- **Synth/poly-guitar patches won't tune reliably.** If the VG-800 is outputting a GR-style synth, pad, or a patch with strong harmonic re-synthesis, the fundamental the tuner needs may not be there cleanly. For tuning, momentarily select a clean VG-800 patch, tune, then switch back. (The VG-800 also has its own onboard tuner — see §9 — which can tune the divided GK signal *before* modeling, which is arguably the more correct place.)

**Banjo, open tunings, 5th-string drone.** A polyphonic tuner is built around the standard 6-string guitar (or 4-string bass) layout, so the EBM-5 banjo is an edge case:
- **Use chromatic/needle mode, not polyphonic, for the banjo.** Polyphonic mode is trying to map strings to a guitar's E-A-D-G-B-E expectation; an open-G banjo (gDGBD) with a short 5th-string drone won't line up. In **chromatic** mode the tuner just identifies whatever note it hears, which handles any open tuning and the high re-entrant 5th-string g without confusion. Almost every modern tuner relies on this for banjo, and it works ([Sweetwater banjo tuning guide](https://www.sweetwater.com/sweetcare/articles/banjo-tuning-guide-how-to-tune-a-banjo/)).
- The 5th string (high g, starting at the 5th fret) is a short drone string — tune it one string at a time in needle/strobe; don't strum-all. Banjo's very fast attack/decay also favors strobe mode for a stable read.
- Same as the guitar: tune off a **clean** VG-800 patch, because the EBM-5's GK signal is going into the VG-800 ahead of the tuner.

**Baritone low tunings.** The baritone Jazzmaster's low B (or lower) is well within range — the Polytune 3 has dedicated **Bass mode** for low strings, and its flat-tuning modes go to 5 semitones below standard. For a baritone in B standard, you can either tune chromatically or use Bass/Needle for the lowest strings if the guitar-mode read gets jittery on the fundamental. Low, slow-vibrating strings always read more reliably in strobe.

**Fender Jazz bass.** Switch Display Mode to **Bass** (the algorithm expects a 4-string set and lower fundamentals). Standard, well-behaved.

## 7. Famous users

It's the industry-standard tuner — so the honest answer is "almost everyone with a pedalboard since 2010." It's a fixture on countless touring boards across every genre precisely because it's invisible utility, not a voice. Naming artists would be padding; there's no signature-tone mythology to a tuner, and any "famous user" list is just a list of people who needed to tune. Skip it.

## 8. Live / power / I/O

- **Power:** 9V DC, center-negative, standard 5.5/2.1 mm barrel. Draws **>100 mA** (TC quotes "100 mA or more" required — this is the digital-display tuner's appetite; it's the heaviest current draw of any pedal on Board 1 except the digital modelers). Budget a 100 mA isolated supply slot, not a throwaway 9 mA one.
- **9V power-out jack:** The full-size 3 can daisy-chain power to other pedals from its DC-out (up to 2 A total through that jack). Probably unused in this isolated-supply rig, but it's there.
- **Battery option:** Runs on a 9V battery (not included); pointless on a powered board.
- **Bypass:** True Bypass by default, switchable to buffered — see §4. In true-bypass it passes signal even with no power (mechanical relay-free hard bypass), which is good fail-safe behavior.
- **I/O:** Mono in / mono out, both ¼" TS unbalanced. **Input impedance 1 MΩ, output 100 Ω** (these are the buffered-path figures). Single mono path — no stereo, which is fine: it's at the mono front of the chain, long before the CE-2W stereo split.
- **Dimensions:** 72 × 122 × 50 mm (2.8 × 4.8 × 2.0 in). Standard compact footprint.
- **USB:** Mini-USB for firmware updates only — not audio, not MIDI.

## 9. Pairing / placement alternatives within this rig

- **Tune off the VG-800's own tuner instead?** The VG-800 has a built-in tuner that works on the **divided GK signal pre-modeling** — arguably the more correct tap point, because it tunes the raw per-string pitch before any modeled distortion/synthesis can confuse a pitch detector. The trade: the VG-800's tuner is on a menu/screen, not a one-stomp pedal, and it only covers the GK-equipped instruments (baritone JM, EBM-5). The Polytune is faster for a between-songs strum and covers *every* instrument plugged into the board, including the magnetic-only guitars and the bass. **Verdict: keep both.** Use the VG-800 tuner for fine GK intonation work; use the Polytune for fast, universal, foot-stomp tuning. They're complementary, not redundant.
- **Buffer redundancy with CB Clean right after:** Already covered in §5 — CB Clean is doing the buffering, so the Polytune's buffer stays off. This is the cleanest division of labor.
- **Could the tuner move earlier (before the VG-800)?** No — the GK divided signal and the VG-800's I/O make pre-modeler tuner placement impractical, and you'd lose the ability to tune the magnetic guitars that enter the chain at the VG-800. 2nd-in-chain, post-VG-800, is correct.
- **Could it move to a dedicated tuner-out / mute loop?** If the owner ever wants the tuner fully out of the audio path, a small ABY or a buffer/splitter with a tuner-out would let the Polytune live on a mute send. Overkill for this rig — true-bypass already gives zero tone impact.

## 10. Reviews & demos

- [MusicRadar — Polytune 3 review](https://www.musicradar.com/reviews/tc-electronic-polytune-3-review) — the best written review; confirms the ±0.02 cent strobe / 0.5 cent chromatic figures, praises the 109-LED display and the buffer, notes the only gripe (cramped top panel when fully wired).
- [Sound On Sound — BonaFide Buffer review](https://www.soundonsound.com/reviews/tc-electronic-bonafide) — essential for the buffer half of this pedal; the germanium-fuzz caveat comes from here.
- [Sound On Sound — Polytune 3 Mini review](https://www.soundonsound.com/reviews/tc-electronic-polytune-3-mini) — relevant for the buffer behavior and accuracy, same engine as the full-size.
- [performerlife — Polytune 2 vs Polytune 3](https://performerlife.com/polytune-2-vs-polytune-3/) — clearest writeup of what the buffer addition changed.
- [TC Electronic PolyTune 3 — Demo & Review (YouTube)](https://www.youtube.com/watch?v=YnuBrr02ZDM) — competent video demo of the tuning modes.
- [TC Electronic Polytune 3 With Integrated Buffer Review (YouTube)](https://www.youtube.com/watch?v=YRncFQYcJZg) — focuses on the buffer.
- [Andertons — product page](https://www.andertons.co.uk/tc-electronic-polytune-3-tuner-pedal-bonafide-buffer/) — good plain-language feature rundown.

## 11. Quirks / known issues / firmware

- **The spec-figure confusion:** TC's own bundled Polytune 3 PDF still carries the older "±0.1 cent" strobe figure in the intro text (carried over from earlier Polytune manuals), while the **3's** marketed and reviewer-confirmed strobe accuracy is **±0.02 cent**. Both are "absurdly accurate"; the 0.02 figure is the current/correct one for this model.
- **Firmware is updatable** via mini-USB with TC's updater (Windows/macOS). Updates are rare for a tuner; check tcelectronic.com/support if pitch detection ever misbehaves, but most units never need it.
- **Buffer is internal DIP-switch only** — you have to unscrew the backplate to change True/Buffered. Set it once and forget it; you can't toggle it live.
- **It needs an instrument plugged in to do anything** — a common "it won't turn on" confusion. The footswitch does nothing with no signal at the input (manual FAQ).
- **Polyphonic mode dislikes anything non-clean upstream** — already covered; not a defect, just the nature of poly pitch-detection.
- No widely reported reliability failures. Standard TC/Music-Group build quality; it's a workhorse.

## 12. Spec sheet

| Spec | Value |
|---|---|
| Type | Polyphonic / chromatic / strobe tuner with switchable buffer |
| Strobe accuracy | ±0.02 cent |
| Chromatic accuracy | 0.5 cent |
| Tuning modes | Polyphonic (auto), chromatic needle, strobe; Guitar & Bass |
| Alternate tunings | Drop-D; all-strings-flat 1–5 semitones (Eb/D/Db/C/B); capo 1st–7th fret |
| Reference pitch | Adjustable in 1 Hz steps (A4 ~440 default) |
| Display | ~109 ultra-bright LEDs + ambient-light auto-dimming sensor |
| Bypass | True Bypass (default) / Buffered / Buffered + Display Always-On (rear DIP switches) |
| Buffer | All-analog BonaFide; unity gain, >112 dB SNR |
| Input connector | 1× ¼" TS, unbalanced, mono |
| Input impedance | 1 MΩ |
| Output connector | 1× ¼" TS, unbalanced, mono |
| Output impedance | 100 Ω |
| Power | 9V DC, center-negative, 5.5/2.1 mm; >100 mA required |
| Power out | 9V DC daisy-chain out (≤2 A through jack) |
| Battery | 9V (not included) |
| USB | Mini-USB, firmware only |
| Dimensions | 72 × 122 × 50 mm (2.8 × 4.8 × 2.0 in) |

Sources: [polytune3.pdf manual](manuals/polytune3.pdf), [Sweetwater](https://www.sweetwater.com/store/detail/PolyTune3--tc-electronic-polytune-3-polyphonic-led-guitar-tuner-pedal-with-buffer), [MusicRadar](https://www.musicradar.com/reviews/tc-electronic-polytune-3-review).

## 13. Recommended setup for this rig

- **Buffer:** **True Bypass** (both DIP switches left). CB Clean immediately downstream already buffers the board; the VG-800 source doesn't need impedance help; and the downstream fuzzes are buffer-tolerant silicon/Muff types, so there's no upside to adding a second buffer here. Only flip to **Buffered + Display Always-On** if CB Clean is removed/moved or you hear high-end loss into the dirt.
- **Display mode:** **Guitar / Needle** as the default for fast between-song tuning; switch to **Guitar / Strobe** for intonation and for getting drone strings dead-on (your sustained-wall aesthetic punishes any string that beats).
- **Bass mode** for the Fender Jazz bass; also useful for the baritone's lowest strings if the read gets jittery.
- **Banjo:** chromatic/needle (or strobe) mode, single-string — **not** polyphonic. Tune off a clean VG-800 patch.
- **Reference pitch:** leave at **440 Hz** unless tracking to an acoustic/keys source that's off — then nudge in 1 Hz steps to match. (The studio has an upright piano and accordion; if you ever cut live with the upright, check its pitch and match the board to it.)
- **Tuning workflow:** for GK instruments, do fine intonation on the **VG-800's own tuner** (pre-modeling, divided signal); use the Polytune for fast universal stomp-tuning of everything.
- Set the DIP switches once at the bench; you won't touch them again.

## 14. Versus alternatives

- **Boss TU-3.** The other industry-standard pedal tuner. Rugged, buffered-bypass-only (no true-bypass option — its buffer is *always* in your path), and **±1 cent** accuracy — 50× coarser than the Polytune's strobe. No polyphonic mode. The TU-3's permanent buffer would actually be *worse* for this rig's fuzz-front-end philosophy than the Polytune, which lets you choose true bypass. **Keep the Polytune** for the strobe accuracy + the bypass choice.
- **Peterson StroboStomp HD.** The accuracy king (±0.1 cent strobe with a vastly deeper feature set — sweetened tunings per instrument, including dedicated banjo presets). If banjo/open-tuning precision were the top priority, the Peterson is genuinely the better banjo tuner. But it's bigger, pricier, has no polyphonic strum-and-go, and is buffered. For a rig that's 90% fast guitar/baritone tuning with occasional banjo, the Polytune's poly speed wins day-to-day; the Peterson is the upgrade *only if* banjo intonation becomes a recurring studio bottleneck.
- **The VG-800's own tuner.** Free, already in the box, and taps the divided GK signal pre-modeling — the most "correct" point to read pitch. But menu-driven, not a one-stomp, and GK-instruments-only. Complements the Polytune rather than replacing it (see §9).

**Why keep the Polytune 3 here:** it's the fastest universal tuner on the board (poly strum-and-go), the most accurate in its class (±0.02 strobe for the sustained-wall stuff), it's the *only* one of these that lets you choose true bypass in front of a fuzz section, and the BonaFide buffer is a free insurance policy if the board's buffering ever changes. Nothing else covers all four. It stays.

## Sources

- [TC Electronic Polytune 3 — User Manual (local PDF)](manuals/polytune3.pdf)
- [MusicRadar — TC Electronic PolyTune 3 review](https://www.musicradar.com/reviews/tc-electronic-polytune-3-review)
- [Sweetwater — PolyTune 3 product/spec page](https://www.sweetwater.com/store/detail/PolyTune3--tc-electronic-polytune-3-polyphonic-led-guitar-tuner-pedal-with-buffer)
- [Andertons — PolyTune 3 (w/ BonaFide Buffer)](https://www.andertons.co.uk/tc-electronic-polytune-3-tuner-pedal-bonafide-buffer/)
- [Sound On Sound — TC Electronic BonaFide Buffer review](https://www.soundonsound.com/reviews/tc-electronic-bonafide)
- [Sound On Sound — Polytune 3 Mini review](https://www.soundonsound.com/reviews/tc-electronic-polytune-3-mini)
- [performerlife — Polytune 2 vs Polytune 3](https://performerlife.com/polytune-2-vs-polytune-3/)
- [Dunlop / MXR — Classic 108 Fuzz product page](https://www.jimdunlop.com/mxr-classic-108-fuzz/)
- [Reverb — MXR M173 Classic 108 Fuzz (BC108 silicon, wah-friendly buffer or true bypass)](https://reverb.com/item/16770387-mxr-m173-classic-108-fuzz-bc108-silicon-fuzz-face-with-wah-friendly-buffer-or-true-bypass)
- [Sweetwater — Banjo tuning guide](https://www.sweetwater.com/sweetcare/articles/banjo-tuning-guide-how-to-tune-a-banjo/)
- [TC Electronic PolyTune 3 — Demo & Review (YouTube)](https://www.youtube.com/watch?v=YnuBrr02ZDM)
- [TC Electronic Polytune 3 With Integrated Buffer Review (YouTube)](https://www.youtube.com/watch?v=YRncFQYcJZg)
