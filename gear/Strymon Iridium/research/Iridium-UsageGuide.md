# Strymon Iridium — Usage Guide

How to *actually* get the most out of the Iridium, to complement the spec/reference dossier in `Iridium-DeepResearch.md`. Be honest up front: in this rig it's **benched for the main GK-driven board** (the VG-800 owns amp/cab modeling for the banjo/baritone), but it's the *right* tool the moment a **magnetic-pickup guitar** is in hand — the **Gibson SG, MIJ Jazzmaster, and Jazz Bass have no GK pickup**, so the Iridium is their natural amp+cab+room straight into the **Apollo x8**, plus the clean-DI, travel-rig, and VG-800-failover box. Three truths shape use: it's an **all-direct DI** (there's no amp to mic in this studio), its real depth is the **IR system** (factory + custom 24/96 IRs, and AMP DISABLE turns it into a general convolution box), and the **INPUT LEVEL switch is the #1 gotcha** — leave it on Instrument with a hot source and you clip it.

> Captured this wave (second pass, Tier B, 2 agents): **6 video transcripts + 9 distilled links = 15 artifacts** (see §10). All video attributions verified via `yt-dlp --print channel`. **Dossier correction folded in (§7):** the dossier said "no verified marquee users" — that's now outdated. Verified touring users found: **Chris Shiflett** (Foo Fighters — Iridium *instead of an amp* on his solo tour), **Mark Bowen** (IDLES — runs *two*, cabs even the drummer; the most rig-relevant, noise-leaning use), **Larkin Poe** (FOH redundancy) — and one *refuted* attribution (Russian Circles' Mike Sullivan actually runs Verellen/Loucks tube heads). §7 patched. Coverage honesty: strong on the official Pete Celi tour + IR depth + workflow, but the deepest authority is the manual; community IR threads were partly paywalled (TGP 402, Equipboard 403).

---

## 1. Essential workflow — the magnetic-guitar DI

The Iridium replaces the amp/mic/cab chain: plug a magnetic guitar into the 1 MΩ **IN**, pick one of three amps, a cab IR, and a room, and go direct to the Apollo or FOH. Three amps ([transcripts/pete-celi-in-depth-tour.md](transcripts/pete-celi-in-depth-tour.md) is the authoritative tour):
- **Round** (Fender Deluxe Reverb) — clean, bright, big headroom. The SG/Jazzmaster pristine-clean voice.
- **Chime** (Vox AC30 Top Boost) — jangly, airy, bites when you dig in.
- **Punch** (Marshall Plexi) — mid-forward crunch → the doom/wall voice.

- **INPUT LEVEL = the clipping trap:** default is **Instrument**; any hot source (a loud board, the JHS Colour Box V2, the VG-800 line out) needs **Line** (+10 dB headroom) or it clips. Single most common mistake ([links/tips-hidden-behaviors.md](links/tips-hidden-behaviors.md)).
- **Output modes** (hold the ON footswitch at power-up, turn DRIVE): **Normal** (red — amp+cab+room), **Cab Bypass** (amber — amp+room, no cab → feed a real power amp/FX return), **Amp Bypass** (green — cab+room, no amp → load an external preamp into the IR engine). ROOM is always active ([links/stack-placement-output-modes.md](links/stack-placement-output-modes.md)).
- **Rear MONO/STEREO/SUM** selector: STEREO (TRS) is a true stereo *input* (aimed at synth/keys); SUM collapses to mono. **LEVEL TRIM** is a global output volume that is *not* saved per preset.

---

## 2. The amps & copyable settings

**The MIDDLE knob is the most amp-specific control** ([links/settings-amp-cheatsheet.md](links/settings-amp-cheatsheet.md), [transcripts/jamesransom-iridium-101-dial-in-tone.md](transcripts/jamesransom-iridium-101-dial-in-tone.md)):

| Amp | MIDDLE does | DRIVE behavior |
|---|---|---|
| **Round** | Noon = stock Deluxe mids; back = scoop; **MAX = tweed mids + a secondary gain** that pushes the power stage | Most headroom — push to ~1 o'c to wake it |
| **Chime** | A **HIGH-CUT** (lower = more top presence, raise = tames highs; interacts with TREBLE) | **Top of DRIVE = a frequency-shaped front-end boost** (treble-booster-in-front; adds gain, tightens lows) |
| **Punch** | Real Plexi tone-stack mids | **~2 o'c = a real Super Lead's max; past 2 o'c = hot-rodded gain** |

All three are **non-master-volume** (DRIVE = amp volume, LEVEL = pedal output only; the analog front end adds up to ~20 dB before DSP).

**Copyable presets:**
- **Chime jangle** (bridge pickup): DRIVE just-below-11 · BASS noon · MIDDLE/high-cut 9–10 · TREBLE 2.
- **Round clean/headroom:** DRIVE 1 o'c · BASS noon · MIDDLE 10–10:30 · TREBLE up (stays clean under loud picking).
- **Default cab picks** (balanced): Round → cab **C** (2×10 Vibrolux), Chime → cab **A** (2×12 AC30 Alnico), Punch → cab **A** (4×12).
- **Drive-stacking:** pedals in front go fizzy as gain rises → dial drives darker/more mid-rangey; two drives max, three loses the amp character.

*(vs the Walrus ACS1, the canonical A/B: the Iridium edges it on IR quality, a rounder/fuller amp-in-a-room, stereo field, and high-gain; the ACS1's only edge is per-preset memory + boost — irrelevant for a studio DI. [transcripts/eytschpi42-acs1-vs-iridium-shootout.md](transcripts/eytschpi42-acs1-vs-iridium-shootout.md))*

---

## 3. The IR system — the real depth

The cab IRs are the Iridium's actual edge over the VG-800 (premium stereo 24-bit/96 kHz, 500 ms convolution). The 9 factory IRs come from OwnHammer / Celestion / cabIR.eu / Valhallir; you can swap any of them via **Impulse Manager** ([transcripts/westbrook-impulse-manager-tips.md](transcripts/westbrook-impulse-manager-tips.md), [links/customir-impulse-manager-workflow.md](links/customir-impulse-manager-workflow.md)):

- **The hard constraint:** Impulse Manager loads **only 24-bit/96 kHz WAV, ≤500 ms**. Most packs ship 24/48 or 44.1 → SRC to 96 k or buy the 96 k variant (off-spec files are silently rejected). Drag into the **LEFT / RIGHT / MONO** of any of 9 slots; per-side level/treble/bass trim to balance; **click SYNC CHANGES before unplugging USB**; Collections save to `~/Documents/Strymon/collections`.
- **Stereo-IR widening trick:** load a **darker IR on LEFT + a brighter IR on RIGHT** of one cab slot (uncheck "Match left channel") → a wide drone pad. Blend *same-vendor* IRs (cross-vendor blends phase-cancel).
- **AMP DISABLE** (fw 1.32+) → the Iridium becomes a **general convolution box**: cab+room on any source, and you can load *any* 24/96 WAV (bass cab, acoustic body, even music samples).

**Where to get custom IRs** ([links/customir-vendor-sources.md](links/customir-vendor-sources.md)):
- **York Audio** — the community standard ("best sounding," balanced/polished/smooth) → best for this rig's clean/jangle DI (loved: MES 212 V30, KW 412 M25-SH).
- **cabIR.eu** (vintage Orange — "crispy cleans, smooth crunch, no tweaking"; ships 500 ms RAW), **Celestion** (buy the exact speaker, 96 k available), **OwnHammer** (huge range, "up front/balanced").
- **Valhallir** — **proof of Iridium purchase = one free V2 cab pack**; their *ambient* cabs are loved for wide/drone work (mix a little ambient IR with a close-mic'd IR + panning).
- **Free for auditioning:** Redwirez 1960A, Overdriven.fr (Celestion, multi-rate), GuitarHacks; **ambienttrash** (paid, ambient-leaning) for the drone aesthetic.

---

## 4. Rig-specific recipes & pairings

- **SG / Jazzmaster → Apollo (the home use):** SG humbuckers love **Punch** (Plexi mids) or **Round** for pristine clean; the Jazzmaster's single-coils sparkle through **Chime** (the jangle preset above). Input = Instrument, small/medium room. This is the role the VG-800 simply can't serve ([links/settings-amp-cheatsheet.md](links/settings-amp-cheatsheet.md)).
- **Punch wall — doom/shoegaze direct:** Punch · CAB **c** (8×12, bright) · DRIVE past 2 o'c (hot-rodded) · BASS low · MIDDLE low · TREBLE noon · **ROOM high + LARGE** · stereo out → sustained chord blooms into a wide ambient wall, no extra pedals. The closest the Iridium gets to the home aesthetic.
- **VG-800 FX-BYPASS → Iridium IR engine (the one non-redundant pairing):** on the VG-800, `[▲]+[CTL 1]` = FX BYPASS (raw INST model, no Boss cab) + OUTPUT = LINE/PHONES → Iridium in **Amp Bypass** (cab+room only), **INPUT = LINE** (the Boss line out is hot; the bench EHX Effects Interface reconciles level if it clips). Strymon's superior IRs then cab the raw Boss model ([links/stack-placement-output-modes.md](links/stack-placement-output-modes.md)).
- **Amp Bypass + an external preamp:** run the **JHS Colour Box V2** (or a Riverside-style preamp) into the Iridium's IR engine → the Colour Box does preamp/dirt, the Iridium just convolves cab+room to the Apollo.
- **Travel board:** Polytune 3 → Iridium (FAV) → UAFX Del-Verb → interface/FOH — a complete amp+verb fly rig, no real amp. **Bass DI:** Jazz Bass → AMP DISABLE + a bass-cab IR.
- **Don't stack it after the VG-800's modeled output** — that's a second cab on the first (muddy). The Iridium and the GK divided path never meet.

---

## 5. MIDI & preset workflow

- **300 presets in 3 banks**, recalled over the **EXP jack** (no 5-pin DIN) via a Strymon MIDI EXP cable / Conduit / TRS-MIDI interface; set **EXP = DIGITAL** (hold FAV at power-up, LEVEL until the ON LED is blue). Default channel 1 ([links/midi-control-workflow.md](links/midi-control-workflow.md)).
- **The bank trap:** banks are 0 (PC 0–127), 1 (128–255), 2 (256–299). PC alone works in bank 0; for banks 1/2 you must send a **Bank Change (CC#0) before each PC**. It powers up in bank 0.
- **CC map:** Amp = **CC19** (1=Round, 2=Chime, 3=Punch) · Cab = CC20 · Room Size = CC18 · Drive = CC13 · Level = CC12 · Bass/Mid/Treble = CC14/15/16 · Amp Disable = CC21 · Bypass = CC102 · Expression = CC100. So an H90 or Blooper *could* flip Iridium presets if it were ever in the chain.

---

## 6. Power-user tips & hidden features

- **AMP DISABLE = a convolution box** for non-guitar sources (bass, synth, or any 24/96 WAV impulse).
- **Stereo-IR widening** (dark L + bright R in one slot) for wide drone pads.
- **ROOM IR is fixed** — only size/level adjust, and it gets boxy if pushed; let the downstream H90/Big Sky do the long tails and keep the Iridium's room modest.
- **LEVEL TRIM** sets a global output that doesn't bake into presets — match unity across patches without re-saving.
- **Buffered bypass needs power** (it's a DSP box, ~500 mA — dedicate a high-current isolated slot, don't daisy-chain).
- **Cab Bypass → a real power amp/FX return** if you ever want the modeled amp through a physical cab.

---

## 7. Notable users (honest — corrected from the dossier)

A ubiquitous studio/silent-stage/direct-to-FOH DI, big in worship/modern-church circles — and, contrary to the dossier's original "no marquee users," there *are* verified touring users (none has a tone "named after" it; all use it as a direct-amp/FOH tool) ([links/artist-notable-users.md](links/artist-notable-users.md)):
- **Chris Shiflett** (Foo Fighters) — used the Iridium **instead of an amp** on his UK/Ireland solo tour, leaning on **Round** (his Deluxe voice).
- **Mark Bowen** (IDLES) — **the most rig-relevant:** runs **two Iridiums** for all cab emulation on a noise/experimental board, even cabbing the **drummer's signal** (real AMP-DISABLE-on-non-guitar use).
- **Larkin Poe** (Rebecca & Megan Lovell) — Iridium wired in "as a redundancy, and to provide sonic options for our FOH engineer" — the canonical failover/FOH role.
- **Refuted:** Russian Circles' Mike Sullivan is *not* an Iridium user (his rig is Verellen Meat Smoke / Loucks tube heads) — do not attribute.

---

## 8. Best learning resources

- **strymon (official) — [the Pete Celi in-depth tour](transcripts/pete-celi-in-depth-tour.md):** the authoritative source on amp/IR/room behavior and the MIDDLE-knob logic.
- **Michael Westbrook — [the deepest Impulse Manager / IR tutorial](transcripts/westbrook-impulse-manager-tips.md)** (stereo dual-mono IR blending, phase rules, convolution use). **James Ransom — [the most copyable knob values](transcripts/jamesransom-iridium-101-dial-in-tone.md).**
- **Sam Wittek — [real all-direct→FOH chain + custom-IR workflow](transcripts/samwittek-worship-board-iridium.md).** **EytschPi42 — [the ACS1 A/B shootout](transcripts/eytschpi42-acs1-vs-iridium-shootout.md).** **Guitar Center — [concise DI overview](transcripts/guitarcenter-hayley-briasco-overview.md).**
- The **manual** is the real I/O/MIDI reference; **[Impulse Manager](https://www.strymon.net/support/impulse-manager/)** for custom IRs; the IR vendors in §3.

---

## 9. Common pitfalls / gotchas

- **INPUT LEVEL Instrument vs Line** — switch to Line for any hot source or it clips.
- **IRs must be 24-bit/96 kHz WAV ≤500 ms** — off-spec files are silently rejected; SRC or buy 96 k; click SYNC CHANGES before unplugging.
- **The MIDI bank trap** — send Bank Change (CC#0) before PC for presets above 127.
- **ROOM IR is fixed** and gets boxy if pushed — keep it modest, let downstream verbs do tails.
- **Buffered bypass needs power** (~500 mA, no daisy-chaining).
- **Don't stack it after the VG-800's modeled output** (double cab) — use the FX-BYPASS→IR pairing instead.
- **Output-mode LED mapping** is easy to confuse: GREEN = Amp Bypass (amp removed → cab+room), AMBER = Cab Bypass (cab removed → amp+room).

---

## 10. Captured sources

**Transcripts** (`research/transcripts/`, 6):
- `pete-celi-in-depth-tour.md` — Strymon (official) — the authoritative amp/IR/room tour.
- `westbrook-impulse-manager-tips.md` — Michael W. Westbrook — deepest IR / Impulse Manager tutorial.
- `jamesransom-iridium-101-dial-in-tone.md` — James Ransom — the most copyable knob values.
- `eytschpi42-acs1-vs-iridium-shootout.md` — EytschPi42 — the ACS1 A/B.
- `samwittek-worship-board-iridium.md` — Sam Wittek — real direct→FOH chain + custom IRs.
- `guitarcenter-hayley-briasco-overview.md` — Guitar Center — concise DI overview + default cabs.

**Links** (`research/links/`, 9):
- `settings-amp-cheatsheet.md` — per-amp MIDDLE/DRIVE behavior + copyable presets + the Punch wall.
- `ir-impulse-manager-and-output-modes.md` — factory IRs, Impulse Manager mechanics, output modes.
- `customir-impulse-manager-workflow.md` — the 24/96 ≤500 ms loading workflow + gotchas.
- `customir-vendor-sources.md` — York/cabIR/Celestion/OwnHammer/Valhallir + free packs; rig picks.
- `stack-placement-output-modes.md` — output modes, the VG-800 FX-BYPASS→IR pairing, Amp Bypass + preamp, travel/bass.
- `midi-control-workflow.md` — EXP-jack MIDI, 300 presets, the bank trap, CC map.
- `tips-hidden-behaviors.md` + `tips-soundonsound-poweruser.md` — input-level trap, stereo-IR widening, AMP DISABLE, LEVEL TRIM.
- `artist-notable-users.md` — the verified users + the refuted attribution.

## Sources

All claims above cite a captured file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Iridium-DeepResearch.md`](Iridium-DeepResearch.md); the manual is in `manuals/`.

> **Honest coverage notes:** strong on the official Pete Celi tour (the deepest authority on amp/IR/room behavior), the best IR-depth and copyable-numbers practitioner videos, the canonical ACS1 shootout, and real direct→FOH workflow demos. The deepest spec reference is the manual (already in the dossier). Community IR threads were partly blocked (TheGearPage 402, Equipboard 403, modwiggler/jazzguitar 403) and were distilled from snippets + official Strymon pages. **Dossier correction:** §7 originally said "no verified marquee users" — corrected to name **Chris Shiflett, Mark Bowen/IDLES, and Larkin Poe** (all direct-amp/FOH users, none with a tone "named after" the Iridium) and to **refute** the Russian Circles attribution. No AMP-DISABLE-as-synth-convolution video surfaced (covered via Strymon's FAQ + the IR logic). All six video attributions yt-dlp-verified — no mis-credits.
