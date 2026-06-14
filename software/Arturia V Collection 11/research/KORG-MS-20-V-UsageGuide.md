# KORG MS-20 V — Usage Guide

The MS-20 V is the bundle's **rig-integration star**: a semi-modular mono synth with an
**External Signal Processor (ESP)** designed to take *external audio in* (the original was built
for guitarists), pitch-track it, and mangle it through **two self-oscillating filters (HP + LP)**
and a patch bay. For this rig that means **strangled banjo / pedalboard-reamp textures** and
**screaming self-oscillating-filter drones** — *but read the Logic gotcha in §3 first*, because
the audio-in trick has a real catch in an AU-only host.

---

## 1. Essential workflows

1. **Self-oscillating-filter drone (no oscillators):** VCO levels down → push **Peak** on the LPF
   toward oscillation (it rings as a near-sine) → set cutoff = drone pitch; add HPF self-osc for a
   beating two-tone. **Two filter models:** **MK1 (KORG-35)** = gritty/noisy/less-screamy/heavier
   CPU; **MK2 (OTA)** = more subs, cleaner *and* screamier, lighter CPU.
2. **Self-playing wall:** Noise gen → **ESP SIGNAL IN** → Amplifier → Bandpass (Low/High Cut to
   tame) → **ENV OUT** (envelope follower) back to filter **Cutoff**; **EG1 in Loop mode** = a free
   second LFO for slow cutoff wander.
3. **External-audio mangling:** define the source as the plugin's **sidechain input** → it appears
   at the **Ext Out** patch point → cable into **ESP SIGNAL IN** (process / pitch-track / envelope-
   follow) or **EXTERNAL IN** (mix with the VCOs pre-filter; also enables internal feedback).
[transcripts/ms20-xnb-complete-guide-walkthrough.md; links/ms20-manual-esp-sidechain-patchbay.md]

---

## 2. Signature settings for this rig

- **Filter-howl drone:** MK2, LPF Peak ~max, both VCOs off, slow MG-triangle → cutoff.
- **Strangled banjo:** banjo → ESP → narrow bandpass → LPF near self-osc, Peak high → ENV OUT →
  cutoff (the banjo's own dynamics open/close the scream).
- **Dirty poly drift:** click the KORG logo → **Dispersion Controls** (6 trimpots) toward 1.00 →
  instant detuned "recorded-wrong" analog instability on a held cluster.
[transcripts/ms20-xnb-complete-guide-walkthrough.md; links/ms20-self-osc-drone-and-overview.md]

---

## 3. Rig recipes — feeding external audio (⚠️ honest Logic caveat)

The documented path is **DAW sidechain input → Ext Out patch point → patch anywhere**; Arturia
explicitly says your DAW must support **sidechaining on virtual instruments**.

**⚠️ VERIFIED PROBLEM:** users report the MS-20 V **AU** does *not* expose a side-chain menu in
Logic's instrument window, and the suggested fix is the **VST3 build — which Logic can't host
(AU-only)**. So the banjo-into-ESP trick may be **unavailable inside Logic**. Confirmed fallbacks,
in order:
1. **Filter MS-20 (free AU effect)** as an insert on the banjo/reamp track — the same KORG-35/OTA
   filters + distortion + envelope-follower→cutoff, **no sidechain needed.** Turn off **Limit
   Resonance** for self-oscillation. **This is the recommended in-Logic move** for processing the
   banjo. [links/ms20-filter-effect-the-logic-au-fallback.md]
2. **MS-20 V standalone** (Audio Settings → Input Channels → hardware input → Ext Out) — cleanest
   documented audio-in path, but outside the DAW.
3. **Ableton Live 12 Lite** (secondary DAW) for VST3 audio-into-instrument routing — verify Lite's
   track/routing caps allow it.

Then degrade downstream: MS-20 / Filter MS-20 → **Decapitator → RC-20 → SketchCassette →
Valhalla / EchoBoy**.

**→ Single most important thing to verify:** open MS-20 V (AU) on a Logic instrument track and
check the top-right plugin header for a **"Side Chain"** menu. If it's absent, default to the
**Filter MS-20** effect for banjo processing. [links/ms20-sidechain-daw-au-vst3-gotcha.md; links/ms20-arturia-faq-sidechain-routing.md]

---

## 4. Notable users & techniques
No ambient-specific artist credit found; relevance is by technique. The lineage anchor is
designer Fumio Mieda's original intent — **guitarists playing the synth via the ESP** — which is
exactly the banjo-into-MS-20 idea. [links/ms20-self-osc-drone-and-overview.md]

## 5. Pitfalls / gotchas
- **The AU-sidechain issue (§3)** — the biggest one for a Logic rig.
- MK1 can glitch/drop out in Poly (CPU); self-oscillation gets **very loud** — watch output.
- ESP pitch-tracking (F→V) needs a **clean, monophonic, stable** source — banjo single-notes, not
  strums.

## 6. Captured sources & QC
- Transcript: `ms20-xnb-complete-guide-walkthrough` (patch-by-patch, the ESP/EXTERNAL-IN detail)
- Links: `ms20-manual-esp-sidechain-patchbay` (authoritative), `ms20-arturia-faq-sidechain-routing`,
  `ms20-sidechain-daw-au-vst3-gotcha`, `ms20-filter-effect-the-logic-au-fallback`, `ms20-self-osc-drone-and-overview`.

**QC:** the ESP/patch-bay/filter detail is from the **official manual** (high confidence). The
**AU-vs-VST3 sidechain problem** is triangulated from MOTUnation/Logic/MusicTech user reports +
the Arturia FAQ (which 403'd) — it's the kind of host-specific gotcha worth a 60-second on-machine
check (above). No ambient artist credit (technique-based).

## Sources
See §6. Originals: youtube.com (XNB), dl.arturia.net manual, support.arturia.com, cdm.link,
MOTUnation/Logic forums. URLs on line 1.
