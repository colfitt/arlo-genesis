---
name: XLN Audio (suite)
brand: XLN Audio
category: software
subcategory: bundle
formats: [vst3, au, aax]
host_in: [logic, ableton]
installed: true
version: latest
status: owned
tags: []
related: []
---

# XLN Audio (suite)

**Summary** — Addictive Drums 2 + RC-20 Retro Color + DS-10 Drum Shaper (all installed;
see CONTENTS.md). Usage research done for **RC-20 Retro Color** →
`research/RC-20-Retro-Color-UsageGuide.md` (5 transcripts + 10 links) and **Addictive
Drums 2** → `research/Addictive-Drums-2-UsageGuide.md` (7 transcripts + 12 links) and
**DS-10 Drum Shaper** → `research/DS-10-Drum-Shaper-UsageGuide.md` (Tier-C, 6 sources:
3 transcripts + 3 links). **All three XLN units now researched.**

## Why I have it
**RC-20 Retro Color** is the rig's *overt lo-fi suite* — six character modules
(Noise / Wobble / Distort / Digital / Space / Magnetic) behind one **Magnitude**
master wet/dry. It's the breadth/recall tool for *cartoon, statement* degradation
and the one-knob dry→destroyed morph (incl. on the master bus) — the in-the-box
counterpart to the hardware tape pedals, sitting alongside SketchCassette
(believable cassette), Decapitator (analog harmonics), and Lossy (codec
artifacts). **Addictive Drums 2** is the rig's **production drum *source*** — a sampled
acoustic-kit instrument used clean-ish, then **degraded downstream** (RC-20 /
SketchCassette / Decapitator / Lossy, or reamped through the tape pedals) or **bounced to
one-shots** for the MPC Sample / Kontakt / Digitakt. Earns its place in a doom/shoegaze
rig via **multi-out routing** (crush individual drums, not the whole kit) and the **Dead &
Dry** kits (towel-muffled, roomless — don't fight your own reverbs).

## Signature uses
- **RC-20 — the Magnitude morph:** automate the single Magnitude knob lo-fi→hi-fi
  (or dry→"full-blast mayhem") across a section; the headline workflow.
- **RC-20 — "found in the dirt" banjo/baritone lead:** Noise (vinyl, Duck) +
  Magnetic Wear + small Distort + short Space on the stem.
- **RC-20 — "old sample" stamp** on hardware sampled into Logic/Kontakt (Noise
  Duck + Magnetic + Digital rate-crush) before chopping.
- **RC-20 — Wobble chorus trick:** Mix ~50% + Stereo on = instant lush chorus.
- **RC-20 — lo-fi bus glue** across a group, Magnitude ~30–50% automated up.
- **AD2 — multi-out to degrade individual drums:** load the multi-out variant, route per
  drum (Pre-Fader = raw source), insert RC-20/DS-10/SketchCassette/Decapitator/Lossy per
  drum in Logic; crush Room/OH, keep the kick clean.
- **AD2 — doom/sludge layering** (Otto/Stoner-Doom): stack 3–5 instances (United Heavy /
  Retroplex / Pork Pie kick) as lo-fi / sub / vintage-crushed / punchy / roomy layers;
  pull the hi-hat mic down on every kit.
- **AD2 — Dead & Dry source:** Vintage Dry (1968 Ludwig) / Vintage Dead ("Hard and Icky")
  for towel-dead drums to degrade or sample without fighting their own room.
- **AD2 — sample factory:** bounce hits (optionally RC-20-stamped) → MPC Sample / Kontakt
  8 / Digitakt 2 for chop material.
- **DS-10 — punch FIRST in the drum bus:** AD2 → **DS-10** (Natural algo; Attack up, Mojo
  Tightness to clamp boom) → RC-20 → SketchCassette → … — set knock before the degraders
  eat it.
- **DS-10 — parallel knock-recovery:** blend a parallel DS-10 (Logic aux send — it has no
  internal dry/wet) to restore attack lost to lo-fi crush; great on MPC/Digitakt breaks
  (Sustain down to de-room, Attack up per chop).

## Notes
*(RC-20 specifics — full detail in the UsageGuide)*
- **Magnitude is the MASTER wet/dry slider, NOT a module.** The 6th module is
  **Magnetic** (tape volume-wear/dropouts). Many web sources conflate the two.
- **Module order is FIXED** (Noise→Wobble→Distort→Digital→Space→Magnetic); only
  exception = **Noise can route to the very end** (post-Master-EQ).
- **No auto-gain** (ride In/Out); **no delay**; **Space reverb is the weak module**
  (use Valhalla for tails). **Default low/high cuts keep it musical** even cranked.
- **Flux** (per module) = the analog-randomness engine; the "dice" = just a
  preset-NAME randomizer. **CPU is low** (~7–10% / 3 modules); **online-only
  installer**. AU for Logic; VST3/AU for Ableton 12 Lite.
- Reach for SketchCassette (realistic cassette) / Decapitator (harmonic color) /
  hardware Generation Loss + Big Time (played-in tape) instead when those fit —
  don't double-degrade the same wow/flutter on one layer.

*(AD2 specifics — full detail in `research/Addictive-Drums-2-UsageGuide.md`)*
- **Multi-out BYPASSES AD2's Master / Delerb / Bus FX** — in-AD2 glue/wash won't carry to
  routed outputs; rebuild downstream (where this rig's character plugins live anyway).
  Load the **multi-out variant** ("4× Stereo, 10× Mono"), not the stereo one.
- **No native one-shot export** — sampling-out is the community bounce method (solo/multi-
  out → trigger hits → bounce short regions). **Delerb feedback to 100% = infinite drone
  washes**; the **Bus** channel = in-box parallel distortion; **5 Snapshots** for clean↔
  degraded A/B.
- **Ableton Live 12 Lite** track ceiling — a full ~13-track drum explosion can exhaust
  Lite; route only 2–3 drums or do heavy drum work in Logic. **Dual reverb engine = main
  CPU cost** (turn off, wash externally); Beats browser lags with lots of 3rd-party MIDI.
- **No documented artist sessions** — Vintage Dry/Dead kit names are *sound-targets*
  (Men I Trust, Mac DeMarco / Tame Impala, QOTSA), not confirmed AD2 users. Avoid the
  dated Studio Pop / Studio Rock kits.

*(DS-10 specifics — full detail in `research/DS-10-Drum-Shaper-UsageGuide.md`)*
- **Strong at ADDING attack, weak at REDUCING sustain** — use it for punch/knock, not to
  gate a tail (NI Transient Master / Logic stock / SPL go further there). **Pick the
  algorithm first** (Natural = transparent default; Smooth = parallel-comp-like for buses;
  Classic = pumping). **Mojo** = the frequency-focused punch (Tightness/Body/Presence).
- **No internal dry/wet, no input gain, no multiband, very low CPU.** Logic AU-only;
  in Ableton Lite watch the track/return ceiling alongside AD2 multi-out. Utility, not a
  sound — **no documented artist uses**. Community depth is thin (≈6 usable sources total).
