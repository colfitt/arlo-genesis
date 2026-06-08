# MXR M173 Classic 108 Fuzz — Deep Research

A working dossier for the one genuinely vintage-circuit dirt box on Board 1. The M173 sits 5th in the chain — after the JHS Colour Box V2 (a buffered preamp) and immediately *before* the EQD Hizumitas — so it is deliberately positioned as the "real, raw, splatty Fuzz Face voice" feeding the Hizumitas sustain-wall. That placement is also the central problem with this pedal in this rig: a silicon Fuzz Face wants to see a passive pickup, and here it sees neither a pickup nor an un-buffered signal — it sees the VG-800's modeled line and the Colour Box's buffer. This document is mostly about whether the M173's onboard Buffer switch rescues that, and how to stack it into the Hizumitas. (Stays consistent with the Hizumitas dossier §5/§6, which already flags the "108 may sound thin behind the Colour Box buffer" issue — this goes deeper.)

## 1. Lineage: What It Actually Is

The Classic 108 is MXR/Dunlop's production **BC108 silicon Fuzz Face** in a pedalboard-friendly chassis. The Fuzz Face is the 1966 Arbiter (later Dallas-Arbiter) two-transistor circuit — a simple feedback-biased pair of NPN transistors that the entire fuzz canon descends from. The earliest units used germanium (NKT275, AC128); by the late 1960s Arbiter had moved to **silicon BC108/BC109/BC183** transistors because they were cheaper, more consistent, and less temperature-sensitive. The "108" in the name is literally the **BC108 silicon transistor** ([Dunlop product page](https://www.jimdunlop.com/mxr-classic-108-fuzz/), [Premier Guitar](https://www.premierguitar.com/gear/quick-hit-mxr-classic-108-fuzz-mini-review)).

Silicon vs germanium, briefly: germanium is warmer, rounder, softer-clipping, and notoriously drifts with heat; silicon is **brighter, edgier, more aggressive, higher-gain, and far more stable** ([PedalPlayers](https://pedalplayers.com/silicon-vs-germanium-fuzz/)). The 108 is the silicon voice — the "searing, pure nastiness" end ([Premier Guitar](https://www.premierguitar.com/gear/quick-hit-mxr-classic-108-fuzz-mini-review)). For a drone/doom/shoegaze player that brightness and bite is an asset feeding a dark Muff, not a liability.

MXR's history with this circuit: Dunlop owns the Fuzz Face trademark and has made silicon and germanium reissues for years. The full-size **M173 Classic 108 Fuzz** is the version in this rig — a Phase 100-sized hammertone-turquoise box (the original Fuzz Face's color) with battery door, optional AC, true bypass + LED, and the added **Buffer switch** ([Dunlop](https://www.jimdunlop.com/mxr-classic-108-fuzz/)). A mini version exists separately (**M296 Classic 108 Fuzz Mini**, ~$99–100, released early 2018) carrying the same BC108 circuit and buffer in a smaller enclosure ([SixStringSensei](https://sixstringsensei.com/1813/mxr-classic-108-fuzz-mini-review/)). The Buffer toggle is the modern feature that distinguishes the current Classic 108 from a vanilla Dallas-Arbiter or Dunlop FFM-series Fuzz Face — older full-size Classic 108 units circulated without it. (I could not pin a single authoritative date to when the buffer was added to the *full-size* M173 specifically — treat the version timeline as approximate.)

## 2. Controls

Three controls plus footswitch. Note the chassis labels two of the knobs twice — outer ring vs printed function — which trips people up:

- **OUTPUT / VOLUME** (left knob) — overall effect output level. Plenty of makeup gain on tap; unity is well below max. Per the manual, output impedance runs **16 kΩ at max volume, 160 kΩ at –6 dB** ([M173 manual](https://www.jimdunlop.com/content/manuals/M173.pdf)).
- **INPUT / FUZZ** (right knob) — the gain/saturation control. Clockwise = more fuzz. This is the only voicing knob; there is no tone control, which is normal for a Fuzz Face and is why placement and source matter so much.
- **BUFFER switch** — the headline feature. Per the manual it "removes high-end roll off and oscillation caused by some wah wahs." Functionally it is an **input buffer** that raises the pedal's input impedance from **10 kΩ (buffer OFF) to 800 kΩ (buffer ON)** ([M173 manual](https://www.jimdunlop.com/content/manuals/M173.pdf)). That 80x impedance jump is the whole story (see §5). Reviewers consistently report buffer ON = **brighter** and "behaves much more predictably" with something in front; buffer OFF = **darker, fuller, more raw/unpredictable** ([Premier Guitar](https://www.premierguitar.com/gear/quick-hit-mxr-classic-108-fuzz-mini-review)).
- **FOOTSWITCH** — true-hardwire bypass, blue LED indicates ON.

## 3. Sonic Character vs Other Fuzzes

The 108 is a **splatty, bright, gated, dynamic** fuzz — the opposite end of the spectrum from the Hizumitas's dense distortion-wall.

- **vs a germanium Fuzz Face (e.g. Dunlop FFM3 / FFM1):** brighter, more aggressive, higher-gain, more stable; less of the "horn-like, woody sustain" germanium sings on single notes. The silicon edge is exactly what you want stacking *into* a dark Muff.
- **vs Big Muffs incl. the Hizumitas:** completely different topology. A Muff is a four-stage cascaded-diode distortion — thick, sustaining, wall-like. The 108 is a two-transistor fuzz — **rawer, spittier, more touch-reactive, and it gates** (note tails clamp and sputter out rather than sustaining forever). In this rig the 108 supplies the splat and the Hizumitas supplies the sustain; they are complementary, not redundant. Per the Hizumitas dossier, the Muff smooths the 108's gated pre-stage into a sustained wall.
- **vs a RAT:** the RAT is a hard-clipping op-amp distortion with a real tone (filter) control — tighter, more mid-focused, far more controllable. The 108 is looser, brighter, more vintage-unruly, and has no tone knob. Reach for the RAT-class voice (here, the downstream Oxford/Longsword) for control; reach for the 108 for character and chaos.

Base voice per Premier Guitar: "rich and perhaps darker and fuller than you might associate with a silicon Fuzz Face" — i.e. MXR tuned out some of the brittle ice-pick that plagued '90s silicon FF reissues. Good news for a banjo source.

## 4. Dynamic Behavior — the Fuzz Face Party Trick

The single best thing about a silicon Fuzz Face is **guitar-volume cleanup**: roll the instrument's volume knob back and the fuzz decongests into a glassy, edge-of-breakup near-clean, then dirties up again as you turn up — all without touching the pedal. BC108-style silicon transistors "react very well to the use of the guitar's volume pot" ([Dunlop](https://www.jimdunlop.com/mxr-classic-108-fuzz/)), and users confirm the 108 "cleans up real nice with the guitar volume knob, both with the buffer on or off" ([SixStringSensei](https://sixstringsensei.com/1813/mxr-classic-108-fuzz-mini-review/)).

**Here is the rig-critical caveat.** That cleanup trick depends on the guitar's volume pot interacting with the fuzz's low input impedance *directly* — passive pickup → fuzz, nothing in between. In this rig there is no passive volume pot in that position: the source is the **VG-800's modeled, buffered, line-ish output**, and there's a **Colour Box buffer** further muting the interaction. So **the classic volume-knob cleanup is largely unavailable from the instrument**. You can still get a cleanup *effect* by riding the VG-800's patch volume or the Colour Box level, but it will feel more like a level change than the magic impedance-driven decongestion. The Buffer switch makes this worse, not better — see §5. If you want the real trick, you need a passive guitar (SG, Jazzmaster) plugged somewhere ahead of the 108 with no buffer between, which this board doesn't offer in the GK path.

## 5. Signal-Chain Placement — the Buffer Problem (read this twice)

This is the crux. A vintage Fuzz Face is **buffer-sensitive at its input**: it is designed to be loaded by a high-impedance passive pickup, and putting a low-output-impedance buffer in front of it (buffer OFF, ~10 kΩ input) makes it sound **thin, sterile, gated, and "wrong"** — it loses the bloom. The Colour Box V2 is a buffered preamp, and it sits directly in front of the 108. So out of the box, **buffer OFF, the 108 will likely sound thin and clipped behind the Colour Box** — exactly the symptom the Hizumitas dossier warned about.

What the onboard **Buffer switch actually does:** it raises the 108's *input impedance to 800 kΩ* and removes high-end roll-off / wah-induced oscillation. It is an **input buffer to make the fuzz tolerate things in front of it** — precisely the Colour-Box-in-front scenario. So:

- **Recommendation 1 — turn the Buffer switch ON in this rig.** With the Colour Box (and the VG-800) feeding it, buffer ON is the correct default: it stops the thin/gated misbehavior, brightens the tone, and stabilizes it. The classic warning "never buffer a Fuzz Face" assumes you're trying to preserve the pickup-loading magic — but that magic is *already gone* here because of the VG-800 + Colour Box, so there's nothing left to protect. Embrace the buffer.
- **Recommendation 2 — if buffer ON sounds too bright/brittle into the banjo, two options:** (a) flip Buffer OFF and accept a darker, gated, more "broken" splat (on-aesthetic for doom/shoegaze, and the Hizumitas downstream will fatten it back up anyway), or (b) keep buffer ON and darken the source at the VG-800 (treble down / darker cab model).
- **Recommendation 3 — fuzz-before-Muff (108 → Hizumitas) is the unconventional order, and it works here.** Conventionally a Muff goes *first* (it's buffer-tolerant) and the Fuzz Face goes *second*. Inverted here, the 108 is a gated/splatty pre-stage and the Hizumitas smooths it into a sustained wall — a genuinely huge, articulate doom texture. Keep this order for the wall sound. **But** if the 108 ever sounds thin or unstable even with buffer ON, the dossier-sanctioned fix is to **swap them (Hizumitas → 108)**: the Hizumitas's low-impedance output drives the 108 cleanly and the 108 sounds great into a Muff's input. That A/B is worth doing once on the board.
- **Downstream is fine:** Brothers AM, Longsword, Oxford, and all the time/mod gear want the stable line-level the fuzz-into-Muff stage delivers.

## 6. Source-Specific — Silicon Fuzz Face Meets the VG-800 (CRITICAL)

The honest verdict: **a Fuzz Face fed by a modeled/divided digital line instead of a passive pickup loses a chunk of its soul, and there's no published documentation of anyone running a Classic 108 behind a VG-800 — this is circuit-behavior inference.**

- **What you lose:** the impedance-interaction magic. The Fuzz Face's character — the bloom, the volume-knob cleanup, the way it "talks" to the pickup — is an artifact of a passive high-impedance source loading a low-impedance fuzz input. The VG-800 outputs a buffered, modeled, summed signal; the hex separation is already collapsed and there's no passive pot in the loop. So expect a **more static, more uniform, less interactive fuzz** than a Jazzmaster-into-108 would give. It will still fuzz — silicon doesn't care what feeds it — it just won't *breathe* the same way.
- **What you keep / can exploit:** the 108 will happily saturate a modeled amp/cab signal, producing dense, slightly artificial-sounding fuzz that is **on-aesthetic for "recorded-wrong" textures**. Fuzzing an already-modeled cab IR is a "wrong" sound in a good way here.
- **Banjo (Gold Tone EBM-5 + GK-5):** the EBM-5's fast, bright, transient, low-mass signal is the hardest case for a fuzz with **no tone control**. The 108 has no way to darken a piercing banjo on its own. Two compensations: (a) Buffer **OFF** runs darker/fuller and may actually suit the banjo better than buffer ON; (b) lean on the Hizumitas's clockwise Tone sweep immediately downstream (per its dossier §6, that 3n3-cap sweep is what tames banjo brightness). Realistically, **for banjo the 108→Hizumitas pair is the unit** — the 108 alone will be ice-picky; the Hizumitas is the EQ rescue.
- **Baritone Jazzmaster (via GK-5/VG-800):** closer to fuzz home territory — more low-end mass to work with. Still buffered/modeled, so still less interactive, but the splat sits well. If you ever run the baritone's *magnetic* output (not the GK path) into the front of the board ahead of the buffers, that's where you'd get the real Fuzz Face response back.
- **Bass (Jazz Bass):** a Fuzz Face on bass loses low end (the circuit is not bass-friendly and thins the fundamental). Usable as a gnarly grind layer, not as a standalone bass fuzz; blend or stack with something that preserves lows.

## 7. Famous Users

Be precise: there is no signature-artist mythology around the **MXR M173** specifically — it's a modern production reissue. The lineage that matters is the **silicon BC108 Fuzz Face**:

- **Jimi Hendrix** — most likely used a **BC108 silicon Fuzz Face** for the **Band of Gypsies / Fillmore East (1970)** period ([Mitchakes Music](https://www.mitchakesmusic.com/post/all-hail-the-mighty-fuzz-face-part-2)). (His earlier, more famous tones were germanium.)
- **David Gilmour** — used a **silicon Fuzz Face** on *The Dark Side of the Moon* — "Time," "Money" ([gilmourish](https://www.gilmourish.com/?page_id=4306)). *(Correction: the widely-repeated "**BC109**" attribution is contested — gilmourish, the authority, says it was a **BC108** and disputes the BC109 claim; Analog Man only supplied him a BC109 later, in 2015. So the M173's **BC108** circuit is arguably **closer** to his DSOTM tone than the BC109 myth — verified during the usage-research pass, see `research/links/artist-gilmour-bc108-vs-bc109-flag.md`.)*
- **Eric Johnson, Gary Clark Jr.** — associated with silicon Fuzz Faces ([Mitchakes Music](https://www.mitchakesmusic.com/post/all-hail-the-mighty-fuzz-face-part-2)).

Attribute the *silicon Fuzz Face sound* to these players; don't claim any of them used this MXR box.

## 8. Live / Power / I/O Notes

- **Power:** one 9V battery (remove bottom plate) or 9V DC center-negative adapter (Dunlop ECB003, DC Brick/Iso-Brick, etc.). **Do not exceed 9V.**
- **Current draw:** **2.2 mA** ([M173 manual](https://www.jimdunlop.com/content/manuals/M173.pdf)) — trivially low, any isolated supply slot handles it.
- **Bypass:** **true hardwire** bypass with blue LED. Unlike the relay-bypass Hizumitas, the 108 is genuinely true bypass — signal passes even with power dead (though the buffer obviously won't function unpowered).
- **I/O:** mono in / mono out, standard 1/4". Input impedance **10 kΩ (buffer OFF) / 800 kΩ (buffer ON)**; output impedance 16 kΩ (max vol) to 160 kΩ (–6 dB). Max output level –4 dBV, max gain 55 dB at 1 kHz.
- **Live note:** if you rely on buffer ON for the rig's voicing, remember the buffer needs power — a dead supply drops you to raw, thin, buffer-OFF fuzz, not silence.

## 9. Pairing Recommendations — This Rig, By Name

- **Colour Box V2 (immediately before):** keep the 108's **Buffer ON** to coexist with the Colour Box buffer. The Colour Box can also pre-shape the fuzz — use its EQ/level to tame brightness before the 108, since the 108 has no tone control of its own.
- **EQD Hizumitas (immediately after):** the marquee pairing. **108 = splat/gate, Hizumitas = sustain/EQ.** Run the 108 for character and let the Hizumitas's Tone knob do the tone-shaping the 108 lacks (especially for banjo). For the biggest wall, both on; for a rawer punk-fuzz, 108 alone. Consider the A/B swap (Hizumitas → 108) if the 108 ever misbehaves (§5).
- **CB Brothers AM (downstream drive platform):** use Brothers as a clean-ish boost/EQ after the fuzz stage to tighten lows and reclaim upper-mids — same role it plays for the Hizumitas. Don't pile more gain; shape.
- **EAE Longsword (downstream "wall"):** stacking the high-gain Longsword after 108+Hizumitas is destructive-in-a-good-way but over-saturates fast. Back its gain way off; use it as a one-stomp intensifier, not added gain.
- **JHS Oxford Drive (downstream):** at this chain position it bricks the whole front end into one texture. Fine as a kill-switch intensifier; useless as a tone shaper this late.
- **General rule:** the 108 wants to be **early and feeding dirt** (which it is), with all time/mod/space strictly downstream — exactly the current layout.

## 10. Reviews & Demos

- [Premier Guitar — Quick Hit: MXR Classic 108 Fuzz (Mini) Review](https://www.premierguitar.com/gear/quick-hit-mxr-classic-108-fuzz-mini-review) — best written review; directly addresses buffer on/off voicing and the darker-than-expected silicon base tone.
- [Pedal Authority — MXR Classic 108 Fuzz Mini Review](https://pedalauthority.com/2018/04/07/review-mxr-classic-108-fuzz-mini/) — practical buffer/usability notes.
- [SixStringSensei — Classic 108 Fuzz Mini Review](https://sixstringsensei.com/1813/mxr-classic-108-fuzz-mini-review/) — confirms volume-knob cleanup behavior buffer on/off.
- [Guitar.com — MXR Sugar Drive & Classic 108 Fuzz Mini Review](https://guitar.com/reviews/mxr-sugar-drive-classic-fuzz/) — context vs other MXR dirt.
- [Dunlop — official MXR Classic 108 Fuzz (M173) page](https://www.jimdunlop.com/mxr-classic-108-fuzz/) — official description + power/feature list.
- [M173 owner's manual (PDF)](https://www.jimdunlop.com/content/manuals/M173.pdf) — authoritative spec sheet (impedances, current draw, sample settings).

## 11. Mods / Quirks / Known Issues

- **Buffer-OFF unpredictability with anything in front** is by design, not a defect — wahs and buffers can cause oscillation/thinning. Buffer ON cures it ([Premier Guitar](https://www.premierguitar.com/gear/quick-hit-mxr-classic-108-fuzz-mini-review)).
- **Gating** on note decay is inherent to the silicon Fuzz Face topology and intensifies at high Fuzz with single-coil/bright sources — embrace it for the degraded aesthetic, or feed it more level to mask it.
- **No tone control** is the main practical limitation; voicing is set by source and by the buffer switch only. Reviewers list "limited control range" as the chief con.
- **No reported reliability problems**; standard Dunlop build, battery door, true bypass.
- **DIY note:** the circuit is a well-documented two-transistor BC108 Fuzz Face; transistor selection/bias is the classic mod target on clones, but the MXR is a sealed production unit — no user-serviceable bias trim.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Circuit | BC108 silicon Fuzz Face |
| Controls | Volume (Output), Fuzz (Input gain), Buffer switch |
| Buffer switch | Input buffer; raises input Z, removes HF roll-off / wah oscillation |
| Input impedance | 10 kΩ (Buffer OFF) / 800 kΩ (Buffer ON) |
| Output impedance @ 1 kHz | 16 kΩ (max volume) / 160 kΩ (–6 dB) |
| Max output level | –4 dBV |
| Max gain @ 1 kHz | 55 dB |
| Bypass | True hardwire bypass (blue LED) |
| Power | 9V battery or 9V DC center-negative |
| Current draw | 2.2 mA |
| Max voltage | 9V (do not exceed) |
| I/O | Mono in / mono out |
| Finish | Hammertone turquoise (Phase 100-sized enclosure) |
| MIDI / expression | None |

Source: [M173 owner's manual](https://www.jimdunlop.com/content/manuals/M173.pdf), [Dunlop product page](https://www.jimdunlop.com/mxr-classic-108-fuzz/).

## 13. Starting-Point Settings

Clock-face, looking down at the pedal. Defaults assume the VG-800 + Colour Box source.

**(a) Raw vintage splat** — gnarly, gated, classic silicon FF
- Volume: 11–12 · Fuzz: 2–3 (high) · Buffer: **OFF** (darker, rawer)
- 108 alone, Hizumitas bypassed. Accept the gating; it's the sound.

**(b) Volume-cleanup edge** — decongested, glassy edge-of-fuzz
- Volume: 12 · Fuzz: 1 · Buffer: **ON**
- Ride the VG-800 patch volume / Colour Box level down for the "clean" (instrument volume-pot trick is unavailable through the GK path — see §4).

**(c) 108-into-Hizumitas wall** — the rig's signature doom texture
- 108: Volume 12 · Fuzz 1–2 · Buffer **ON** → Hizumitas: Sustain ~12, Tone ~1 (bass side), Volume 12
- Both engaged. 108 supplies splat/grind, Hizumitas supplies sustain + tone-shaping. Long verb/delay downstream.

**(d) Banjo lead** — EBM-5 single-note lead through the wall
- 108: Volume 12 · Fuzz 12 · Buffer **OFF** (darker for the bright banjo) → Hizumitas Tone 1–2 o'clock to roll off the ice-pick
- Lean on the Hizumitas for tone; the 108 can't darken on its own. VG-800 darker cab model helps.

## 14. Versus Alternatives

- **Dunlop FFM3 (Hendrix, silicon mini):** the most direct silicon-FF alternative — arguably more "authentic" Hendrix-silicon voicing, but **no buffer switch**, so it would misbehave behind the Colour Box exactly the way an un-buffered Fuzz Face does. The M173's buffer is the reason it earns the slot in a buffered chain like this; the FFM3 would not.
- **Dunlop FFM1 (germanium):** warmer, rounder, softer — but germanium drifts with temperature and is even *more* buffer-sensitive. Wrong tool for a buffered, modeled, line-level source; you'd lose the warmth you bought it for. The silicon 108 is the pragmatic choice for this rig.
- **JHS / other silicon FF clones (e.g. JHS-style "Smiley"-derived builds):** comparable voices; some add a buffer or input-impedance switch. The M173 wins on price/availability and a known, documented buffer that specifically fixes the in-front-of-it problem this board has.

**Why it earns its slot:** in a chain that is *already* buffered and modeled (VG-800 + Colour Box), a normal Fuzz Face would either oscillate or go thin. The Classic 108's **switchable input buffer is the one feature that lets a vintage Fuzz Face circuit survive 5th in a buffered chain** — and its bright silicon splat is the perfect raw pre-stage to feed the dark Hizumitas wall. It supplies the one texture nothing else on Board 1 does: genuine vintage Fuzz Face character. That's the slot.

## Sources

- [MXR / Dunlop — Classic 108 Fuzz (M173) product page](https://www.jimdunlop.com/mxr-classic-108-fuzz/)
- [MXR M173 Classic 108 Fuzz — owner's manual (PDF)](https://www.jimdunlop.com/content/manuals/M173.pdf)
- [Premier Guitar — Quick Hit: MXR Classic 108 Fuzz (Mini) Review](https://www.premierguitar.com/gear/quick-hit-mxr-classic-108-fuzz-mini-review)
- [Pedal Authority — MXR Classic 108 Fuzz Mini Review](https://pedalauthority.com/2018/04/07/review-mxr-classic-108-fuzz-mini/)
- [SixStringSensei — MXR Classic 108 Fuzz Mini Review](https://sixstringsensei.com/1813/mxr-classic-108-fuzz-mini-review/)
- [Guitar.com — MXR Sugar Drive & Classic 108 Fuzz Mini Review](https://guitar.com/reviews/mxr-sugar-drive-classic-fuzz/)
- [PedalPlayers — Silicon vs Germanium Fuzz](https://pedalplayers.com/silicon-vs-germanium-fuzz/)
- [Mitchakes Music — All Hail The Mighty Fuzz Face, Part 2 (famous users)](https://www.mitchakesmusic.com/post/all-hail-the-mighty-fuzz-face-part-2)
- [gilmourish — Fuzz buyer's gear guide (Gilmour silicon FF)](https://www.gilmourish.com/?page_id=4306)
- [Fuzz Face — Wikipedia (circuit/transistor history)](https://en.wikipedia.org/wiki/Fuzz_Face)
- [MXR Classic 108 Fuzz Mini (M296) product page](https://www.jimdunlop.com/mxr-classic-108-fuzz-mini/)
