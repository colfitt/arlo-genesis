# Radial X-Amp — Deep Research

A working dossier for the **Radial X-Amp** as the studio's dedicated re-amp box in a hex-pickup banjo/baritone rig. This is a utility, not a tone source: its whole job is to take a balanced line-level track back out of the Apollo x8 and hand it to the VG-800 and the three pedalboards at instrument level and impedance, so a clean DI of the banjo/baritone/guitar can be fuzzed, smeared, and tape-degraded *after* the take. It is the analog backbone of the "commit later, mangle infinitely" workflow — print the performance once, then re-amp it through the chain as many times and as wrongly as you like.

## 1. What It Actually Is

The X-Amp is the **active** member of Radial's Reamp® family — the line that reverses a DI box. A DI takes an instrument and makes it line-level and balanced so a console/interface can record it; a re-amp box does the opposite, taking that recorded **balanced line-level** track and converting it back to the **high-impedance, instrument-level** signal a guitar amp or pedal expects to see ([Radial X-Amp product page](https://www.radialeng.com/product/x-amp)). Per the manual's own framing, amps and recording devices "work at different signal levels, they are not directly compatible… the X-Amp allows these devices to 'speak' to each other" ([XAMP manual, p.1, Overview](manuals/XAMP-Manual-WEB-04-2025.pdf)).

What sets the X-Amp apart within the Reamp line is that it is a **100% discrete class-A active** circuit with **two transformer-isolated outputs**, where the cheaper [ProRMP](https://www.radialeng.com/product/prormp/faq) and the flagship [Reamp JCR](https://www.radialeng.com/product/jcr/jcr-faq) are *passive* (transformer-only, single output). Radial frames the active-vs-passive choice as ["condenser vs. dynamic microphones – both get the job done and sound great, but many engineers will have their preference"](https://www.radialeng.com/comparing-reampers); the active X-Amp is described as having "more top end shimmer" while the passive JCR "sounds a touch smoother." The dual output is the X-Amp's headline feature: it can drive two amps (or two destinations) simultaneously and in phase.

Crucially for this rig, the X-Amp is a **send-only** device — there is **no return path** on it, unlike the Radial EXTC (an effects-loop re-amper with onboard return + wet/dry blend) or the owner's EHX Effects Interface (a USB round-trip). The X-Amp throws the signal out to the amp/pedals; you capture the result on another input — here, back into the Apollo ([Gearspace: X-Amp vs EXTC](https://gearspace.com/board/so-much-gear-so-little-time/1271686-can-radial-x-amp-reamp-effects-like-radial-extc.html)). It is pure analog, with no computer in the audio path.

## 2. Controls & I/O

Every control and jack, from the manual's Input and Output panels (pp. 2–3):

**Input panel (back):**
- **LINE-LEVEL LOCKING XLR INPUT** — balanced female XLR, wired pin-2 hot (AES standard). Fed from the line output of a recorder or mixing console — i.e. an Apollo line out.
- **GROUND (INPUT-SIDE) LIFT switch** — disconnects pin-1 ground at the XLR input. "Lifting the ground often helps reduce hum or buzz caused by so-called ground loops."
- **POWER jack** — 15 VDC / 400 mA supply (included). The unit is active and **must** be powered to pass signal; the power LED lights immediately when connected.
- **Cable clamp / no-slip pad / I-beam bookend chassis** — mechanical: secures the power cable, isolates the box from amp-frame vibration, and armors the connectors.

**Output panel (front):**
- **LEVEL control** — recessed "set & forget" pot adjusted with a guitar pick or flat-head screwdriver; sets the instrument-level volume going to the amps. Recessed so it can't be knocked out of position.
- **CLIP LED** — lights if the incoming line signal overloads the X-Amp's input. The manual's level-setting procedure: turn LEVEL to roughly 12 o'clock, raise the recorder/mixer output until CLIP "occasionally blinks with peaks," then back off until it never blinks.
- **POWER LED** — confirms the 15 VDC supply is live.
- **DIRECT OUT-1** (¼") — *transformerless, direct-coupled* output. This is the **primary** output and **"must always be connected to a properly grounded amplifier"** — it provides the ground path for the whole box.
- **ISOLATED OUT-2** (¼") — *transformer-isolated* second output, for a second amp/destination without ground-loop hum.
- **POLARITY 180° switch** — flips the phase of the transformer-coupled OUT-2 so two amps play in phase.
- **GROUND LIFT OUT-2** (recessed internal switch, accessed through a side-panel hole) — factory-set to *lifted*; flip to *grounded* only if lifting the input ground didn't cure a hum.

## 3. What It Does to the Signal

The conversion is the entire point. Inside, a discrete class-A buffer/amp takes the **+4 dBu-ish balanced line signal** (max input +22 dBu) and the LEVEL control attenuates it down to **High-Z instrument level** on OUT-1 (direct) and a transformer-isolated copy on OUT-2 ([XAMP manual, Block Diagram & Specs, p.9](manuals/XAMP-Manual-WEB-04-2025.pdf)). Input impedance is **600 Ω** (it's *receiving* a line source, so a low input is correct); the outputs are voiced as high-impedance instrument-level so a fuzz, drive, or amp front end sees what it would from a guitar.

Fidelity is the selling point. Frequency response is **20 Hz – 15 kHz (±1.0 dB)**, dynamic range **119 dB**, THD **0.02% @ −15 dBu**, S/N **88 dB below instrument level** ([manual specs, p.9](manuals/XAMP-Manual-WEB-04-2025.pdf)). [Sound on Sound's roundup review](https://www.soundonsound.com/reviews/guitar-technology-6) found the re-amped result "essentially indistinguishable from the sound you get when plugging the guitar directly into the amplifier… it won't compromise your sound." That transparency matters here: the X-Amp adds no character of its own, so whatever gets ruined downstream is ruined *by the chain*, not by the re-amp box. (The faint "shimmer" Radial attributes to the active design vs. the passive JCR is the only coloration on the table, and it's subtle.)

The transformer on OUT-2 also provides **galvanic isolation** — the reason you can hang a second amp/board off it without a ground loop.

## 4. Behavioral Notes

- **Set the level by the CLIP LED, not by ear first.** The manual is explicit: drive the recorder/mixer output up until CLIP just peaks, then back off, so the X-Amp's *output* is clean. Then use LEVEL to match what the amp/pedal saw when the guitar was plugged in directly.
- **OUT-1 is the ground anchor — keep it connected.** Because OUT-1 is the direct-coupled, grounded output, the manual warns that if you use OUT-2 (the isolated output) you should leave a grounded amp on OUT-1 **at all times, even if it's off or unused** — "the amp serves as an important safety ground."
- **Two layers of ground-loop defense.** Input-side ground lift first; if hum persists with a second amp, toggle the internal OUT-2 ground-lift. Standard re-amp hygiene.
- **Phase-check whenever you change destinations.** Any time you swap an amp or add a pedal chain on OUT-2, A/B the 180° switch and keep the setting that "sounds the fullest" — re-patching can introduce a phase flip.
- **No return, no blend, no computer.** Unlike the EXTC/EHX, the wet signal must come back on a separate Apollo input. There's no onboard wet/dry mix; blend the re-amped track against the dry DI in the DAW.

## 5. Role in the Studio — the Re-Amp Workflow

This is the box's reason for existing in this rig. The aesthetic is degraded, drone/doom/shoegaze, "recorded-wrong" — and the cleanest way to get there without committing on the way *in* is to **print clean, ruin later**. The X-Amp is what makes "later" possible in pure analog.

**The loop:**
1. **Print a clean DI** of the source (banjo, baritone, guitar, bass) to the Apollo x8 — the dry, uncolored performance. (For the GK instruments, also/instead print the VG-800's output.) The manual recommends capturing through a quality DI like the Radial JDI/J48 so the source track is "as clean and natural sounding as possible."
2. **Send a line out of the Apollo** (the recorded track) into the X-Amp's balanced XLR input.
3. **X-Amp converts** that line track back to instrument level on OUT-1 (and optionally OUT-2).
4. **Feed the chain:** OUT-1 → the front of Board 1 (into the VG-800 / Polytune / CB Clean) → through all three boards (texture → time → tape) → and/or directly into the VG-800 if you want amp/cab/synth modeling first.
5. **Re-capture** the mangled wet result on a fresh Apollo input. Repeat with different settings, different pedals, different amounts of destruction — the player never has to perform again.

Because the X-Amp is transparent, you can **re-amp the same DI a dozen times** and stack the passes (the manual explicitly notes the dual output lets you "layer multiple tracks for full, lush guitar tones"). Print a take dry, then build the wall in the box afterward: a clean banjo line becomes a Hizumitas drone on one pass and a Microcosm granular wash on the next, both committed at leisure. This is the "commit later, mangle infinitely" backbone — the performance is sacred, the texture is disposable and infinitely re-rollable.

## 6. Source-Specific Notes

- **Banjo DI (Gold Tone EBM-5).** The banjo's fast attack / fast decay and bright transient content are brutal to dial in live through fuzz. Re-amping is the fix: print the dry banjo (or the VG-800-processed banjo) once, then re-amp it through Board 1 as many times as it takes to tame the 2–4 kHz spike — adjust the VG-800 amp model, the Colour Box, the Hizumitas Tone, with the source frozen. No re-performance, no fatigue.
- **Baritone Jazzmaster (GK-equipped).** Print the magnetic DI *and* the VG-800 output as separate tracks; re-amp either. The baritone's low fundamental survives the X-Amp's 20 Hz–15 kHz response fine.
- **Bass (Pro Jazz Bass).** The manual calls out re-amping bass directly; print a clean DI, re-amp through a drive/amp for grit while keeping the clean DI underneath for low-end weight — classic parallel bass distortion, done analog and after the fact.
- **The VG-800 path (double re-amp).** The most rig-specific trick: the VG-800 is already a modeled/COSM source. Print its output dry, then **re-amp the model back through real pedals** — a modeled tweed amp re-fuzzed through the MXR 108 + Hizumitas, or a VG-800 synth/pad patch re-amped into the End Board's reverbs to become a distorted drone. You can also **double-re-amp**: re-amp a DI through the VG-800 first (capture that), then re-amp *that* through the pedalboards. Each pass is a new generation of "wrong."
- **Two destinations at once (OUT-1 + OUT-2).** Split a single DI to two parallel chains — e.g. OUT-1 → clean amp/Board for body, OUT-2 → full mangled board for texture — and blend in the Apollo. Phase-align with the 180° switch.

## 7. Famous Users

Re-amping with a Radial box is a studio *standard*, not a signature-artist statement, so the user mythology is engineer-side rather than artist-side. The technique itself was popularized by **John Cuniberti** (the original Reamp inventor; the JCR carries his circuit), and the X-Amp lives on countless commercial sessions where engineers commit guitars clean and shape amps in the mix. Treat any specific "famous user owns an X-Amp" claim as unverified — it's a behind-the-glass utility, and that's the honest framing. *(Unverified: named artist endorsements.)*

## 8. Power / I/O

- **Power:** **15 VDC / 400 mA**, center-pin (2.5 mm), supply included. *Note: this is higher than the typical 9 V pedal supply* — it will **not** run off a standard 9 V isolated pedalboard slot; use the included adapter or a 15 V outlet on a multi-voltage supply. It is active and **requires power to pass signal**.
- **Input:** 1 × balanced female XLR, line-level, pin-2 hot (AES), 600 Ω, max +22 dBu, with input-side ground lift.
- **Outputs:** 2 × ¼" — OUT-1 direct-coupled (primary, must be grounded), OUT-2 transformer-isolated with 180° polarity and its own internal ground-lift.
- **Bypass:** none — it's a converter, not an effect; there is no true-bypass mode. Signal only passes when powered.

## 9. Pairing Recommendations (by name)

- **UA Apollo x8 (the source + the destination).** The Apollo prints the clean DI and provides the balanced line out that feeds the X-Amp; it also catches the re-amped return on a separate input. The whole loop is Apollo → X-Amp → chain → Apollo. Use Apollo's line outs (not headphone/monitor outs) for a clean +4 dBu feed.
- **Boss/Roland VG-800.** Both a *source* (print its modeled output to re-amp later) and a *destination* (re-amp a dry DI back through its amp/cab/synth models). The X-Amp's instrument-level OUT-1 is exactly what the VG-800's guitar input wants.
- **Board 1 front end (Polytune → CB Clean → Colour Box → MXR 108 → Hizumitas → Brothers AM…).** The primary re-amp destination. OUT-1's high-Z instrument output hands the front of the board what a real guitar would; the CB Clean buffer downstream is harmless.
- **vs. the EHX Effects Interface (owned).** Complementary, not redundant. **X-Amp = pure analog, transformer-isolated, no computer, no latency, no converter, two outputs, send-only.** **EHX = USB-C "hardware plugin," DAW-integrated, the re-amp lives *inside* the session** (automatable level, recallable, wet return on its own track, plugins-as-pedals). Reach for the **X-Amp** for fast, clean, latency-free analog re-amping and two-destination splits; reach for the **EHX** when you want the re-amp to be a recallable plugin in the DAW or to drop software effects onto the physical board. See §14.

## 10. Reviews & Demos

- [Radial X-Amp product page](https://www.radialeng.com/product/x-amp) — manufacturer spec/feature reference.
- [Radial — Comparing Reampers](https://www.radialeng.com/comparing-reampers) — the active-vs-passive (X-Amp vs ProRMP vs JCR) framing and the dual-output rationale.
- [Radial — Reamping: Exploring the Differences](https://www.radialeng.com/blog/reamping-exploring-the-differences) — Radial's own primer on re-amp box types.
- [Sound on Sound — Guitar Technology roundup (includes X-Amp)](https://www.soundonsound.com/reviews/guitar-technology-6) — "indistinguishable from plugging the guitar directly into the amplifier." *(Multi-product roundup, not a standalone X-Amp review.)*
- [Sweetwater — X-Amp product page + user reviews](https://www.sweetwater.com/store/detail/XAmp--radial-by-amp-2-channel-active-re-amping-device) — retailer specs and owner feedback ("clean, strong, sounds exactly as the original guitar output").
- [Reverb — Radial X-Amp listing](https://reverb.com/p/radial-x-amp) — price history / market context.
- [Reamp Box Shootout: JCR vs ProRMP (YouTube)](https://www.youtube.com/watch?v=KEI_1qVK5P0) — audible passive-reamper comparison (X-Amp is the active sibling).
- [Seymour Duncan forum — Reamping: X-Amp vs ProRMP](https://forum.seymourduncan.com/forum/amplifier-central/282999-reamping-radial-x-amp-vs-prormp) — user discussion on active vs passive in practice.

## 11. Quirks / Known Issues

- **15 V supply, not 9 V.** The single biggest gotcha for a pedalboard owner: it needs the included **15 VDC / 400 mA** adapter, not a 9 V slot. Don't lose the brick.
- **OUT-1 must always be connected to a grounded amp** when using OUT-2 — it's the safety ground and the box's ground reference. Floating OUT-1 while driving OUT-2 is a safety/noise mistake.
- **Ground loops** are the classic re-amp problem; the X-Amp has *three* mitigations (input lift, OUT-2 isolation transformer, OUT-2 internal lift) — work through them in that order.
- **No return / no blend / no bypass** — by design. You need a second Apollo input to capture the wet pass, and you blend in the DAW. Don't expect EXTC-style send/return convenience.
- **Recessed LEVEL pot** — needs a pick/screwdriver to adjust; deliberate ("set & forget"), but mildly annoying if you tweak levels often.
- **Phase flips on re-patch** — always re-check the 180° switch after changing destinations.
- No widely reported failures; Radial's I-beam build and 3-year transferable warranty are studio-grade.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Active class-A studio re-amper (send-only, dual output) |
| Audio circuit | 100% discrete class-A |
| Frequency response | 20 Hz – 15 kHz (±1.0 dB) |
| Signal-to-noise | 88 dB below instrument level (−20 dBu) |
| Dynamic range | 119 dB |
| Noise floor | OUT-1 −110 dBu; OUT-2 −108 dBu |
| Max input | +22 dBu |
| THD | 0.02% @ −15 dBu |
| IMD | 0.02% @ −20 dBu |
| Input impedance | 600 Ω |
| Input | Balanced line-level XLR, AES standard (pin-2 hot) |
| Input ground lift | Disconnects pin-1 at the XLR |
| Output level | Adjustable (recessed LEVEL pot) |
| Output type | High-Z instrument level; OUT-1 direct-coupled, OUT-2 transformer-isolated |
| Polarity | 180° reverse on OUT-2 |
| Ground lifts | Input-side + internal OUT-2 lift |
| Power | 15 VDC / 400 mA, supply included (NOT 9 V) |
| Construction | 14-gauge steel chassis + outer shell, welded I-beam, powder-coat |
| Size | 3.3" × 5.0" × 2" (84 × 127 × 48 mm) |
| Weight | 1.55 lb (720 g) |
| Bypass | None (active converter; requires power) |
| Price | ~$200 US street *(approximate — verify current)* |
| Warranty | Radial 3-year, transferable |

Sources: [XAMP manual (rev. R870-1040-10 / 04-2025), Specifications p.9](manuals/XAMP-Manual-WEB-04-2025.pdf); [Radial X-Amp product page](https://www.radialeng.com/product/x-amp).

## 13. Recommended Setups for THIS Rig

**(a) Single re-amp into Board 1** — the everyday move
- Apollo line out (recorded clean DI) → X-Amp XLR in. OUT-1 → front of Board 1 (VG-800 / Polytune / CB Clean in). End of Board 1 (Deco stereo out) → back into Apollo on a new track.
- Set LEVEL by the CLIP LED (peak then back off), then match the level the guitar saw live. Re-roll the chain settings freely; the source is frozen.

**(b) Parallel two-destination split** — body + texture, blended in the box
- OUT-1 → a clean-ish destination (e.g. VG-800 clean amp model, or Board 1 with dirt off) for body.
- OUT-2 → the full mangled chain (Hizumitas → Longsword → End Board) for texture.
- A/B the 180° polarity, keep the fuller setting, capture both returns to the Apollo, blend.

**(c) Banjo re-amp** — taming the bright transient source after the fact
- Print the EBM-5 banjo dry (and/or its VG-800 output). Re-amp through Board 1 with the VG-800 on a darker amp model and the Hizumitas Tone past noon. Iterate on the frozen DI until the 2–4 kHz spike is a wall, not an ice pick — no re-performance.

**(d) Double-print / generational decay** — the "recorded-wrong" deep cut
- Re-amp a dry DI through the VG-800 → capture. Re-amp *that* capture through the three boards → capture. Optionally re-amp *again* through the End Board's tape stages (Generation Loss, PORTA424, JHS 424). Each pass adds a generation of degradation; stack the passes for an infinitely-ruinable wall.

## 14. Versus Alternatives

- **EHX Effects Interface (owned).** The DAW-integrated counterpart. The X-Amp is the **pure-analog, transformer-isolated, zero-latency, no-computer, two-output, send-only** re-amp; the EHX is a **USB-C "hardware plugin"** where the re-amp lives inside the session (recallable, automatable level, wet return on its own track, and it can also put software plugins on the physical board). Use the **X-Amp** for fast clean analog passes and two-destination splits with no computer in the path; use the **EHX** when you want the re-amp to be a session-recallable plugin or need plugins-as-pedals. Owning both is justified — different workflows, not duplicate function. *(Cross-ref: `Gear/EHX Effects Interface/research/Effects-Interface-DeepResearch.md`.)*
- **Radial EXTC / EXTC-SA.** An effects-*loop* re-amper: it has an onboard **return** and **wet/dry blend**, so the pedal send-and-return is a single box. The X-Amp has **no return** — you bring the wet signal back on a separate Apollo input. Reach for an EXTC if you want a self-contained pedal-as-outboard send/return with blend; the X-Amp's edge is the **second output** (two chains/amps) and pure send simplicity ([Gearspace: X-Amp vs EXTC](https://gearspace.com/board/so-much-gear-so-little-time/1271686-can-radial-x-amp-reamp-effects-like-radial-extc.html)). Not owned; the X-Amp + Apollo covers the loop manually.
- **Radial Reamp JCR.** The passive flagship — John Cuniberti's original transformer with a MuMETAL shell, three-position filter, mute, single output. "Smoother" than the X-Amp's "shimmer," needs no power. Reach for the JCR for the most pedigreed single-amp passive tone; reach for the **X-Amp** for the active character, dual output, and not needing a separate filter/mute.
- **Radial ProRMP.** The budget passive box — single output, no power. The X-Amp's active class-A design and dual output are the upgrade; the ProRMP is the answer only if you want the cheapest, no-power, one-amp solution.
- **UA Apollo x8 outputs straight into an amp/DI.** You *can* re-amp by sending an Apollo line out directly into an amp's input, but a raw line level into a guitar front end mismatches level/impedance and invites ground-loop hum. The X-Amp exists precisely to fix that — proper instrument level/impedance and transformer isolation. The Apollo is the source/capture; the X-Amp is the converter between them.

**Bottom line for this rig:** the X-Amp is the dedicated **analog re-amp backbone** — print clean to the Apollo, re-amp through the VG-800 and the three boards, capture the wreckage, repeat. It's transparent (so the chain does the damage, not the box), it splits to two destinations, and it keeps the computer out of the audio path. Use the **EHX Effects Interface** when you want that same re-amp to be a recallable DAW plugin; use the **X-Amp** when you just want to commit clean and mangle infinitely in pure analog.

## Sources

- [Radial Engineering — X-Amp product page](https://www.radialeng.com/product/x-amp)
- [Radial Engineering — Comparing Reampers](https://www.radialeng.com/comparing-reampers)
- [Radial Engineering — Reamping: Exploring the Differences](https://www.radialeng.com/blog/reamping-exploring-the-differences)
- [Radial Engineering — Reamp family overview](https://www.radialeng.com/reamp)
- [Radial Engineering — ProRMP FAQ](https://www.radialeng.com/product/prormp/faq)
- [Radial Engineering — Reamp JCR FAQ](https://www.radialeng.com/product/jcr/jcr-faq)
- [Radial Engineering — EXTC-SA product page](https://www.radialeng.com/product/extc-sa)
- [XAMP User Guide PDF (rev. R870-1040-10 / 04-2025)](manuals/XAMP-Manual-WEB-04-2025.pdf)
- [Sound on Sound — Guitar Technology roundup (X-Amp)](https://www.soundonsound.com/reviews/guitar-technology-6)
- [Sweetwater — Radial X-Amp product page & reviews](https://www.sweetwater.com/store/detail/XAmp--radial-by-amp-2-channel-active-re-amping-device)
- [Reverb — Radial X-Amp](https://reverb.com/p/radial-x-amp)
- [Reamp Box Shootout: JCR vs ProRMP (YouTube)](https://www.youtube.com/watch?v=KEI_1qVK5P0)
- [Gearspace — Can the X-Amp reamp effects like the EXTC?](https://gearspace.com/board/so-much-gear-so-little-time/1271686-can-radial-x-amp-reamp-effects-like-radial-extc.html)
- [Seymour Duncan forum — Reamping: X-Amp vs ProRMP](https://forum.seymourduncan.com/forum/amplifier-central/282999-reamping-radial-x-amp-vs-prormp)
