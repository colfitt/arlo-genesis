# Buchla Easel V — Usage Guide

Arturia's model of the 1973 Buchla Music Easel — Don Buchla's **"West-Coast"** approach:
electricity as the instrument, **low-pass gates instead of resonant filters**,
**wavefolding instead of subtraction**. For this rig it's the generative/Krell drone +
plucky-organic-texture machine (4-voice vs mono hardware). Workflow ethos across every
source: **"hit record, play with the patching, cherry-pick the best."**

## 1. The engine

**Complex Oscillator (the heart):** core is a sine/triangle hybrid; add harmonics two ways
— (1) **wave mixing** (a Timbre *switch* picks the second wave — triangle/impulse/square —
and a dial mixes it), (2) **wave folding** via the **Timbre slider** (folds the signal under
a CV ceiling, generating harmonics additively → the classic Buchla metallic sheen). For a
fixed-pitch drone, detach keyboard control and set a fixed pitch. `research/transcripts/vc-drone-buchla-omahs-ep2-complex-osc.md`

**Dual Low-Pass Gates (the soul):** the LPG's natural ring/decay is what makes the plucky,
organic, percussive Buchla sound — treat it like a combined VCA+filter that "rings." Users
single this out as the best part. `research/links/vc-drone-buchla-kvr-thread.md`

**Modulation Oscillator:** a second source doing audio-rate **FM** into the Complex Osc for
grit/inharmonics; flip to **LFO mode** and the same routing is a slow wobble. `research/transcripts/vc-drone-buchla-omahs-ep4-mod-osc.md`

**Sequencer = a modulation source, not a tone source:** the **5-step** sequential voltage
source (the odd default-5 forces polyrhythm). Patch it → osc pitch/timbre/LPG with a mod
amount; gate it with an envelope so it doesn't "runaway-train." `research/transcripts/vc-drone-buchla-omahs-ep8-seq-voltage.md`

**Random voltage = the generative engine:** four white output jacks → many destinations at
once. **The single highest-value move: randomize the Period (rate) plus pitch/timbre/LPG for
ever-evolving texture.** `research/transcripts/vc-drone-buchla-omahs-ep9-random-voltage.md`

**Gravity (Arturia's added gesture tool):** an XY pad with a **bouncing ball** + walls/
portals/gravity objects — the ball's physics path modulates parameters. The most "set it and
let it drift" generative control in the bundle. `research/links/vc-drone-buchla-databroth-review.md`

## 2. Copyable generative-drone recipes

- **★ Generative random texture (the canonical patch):** Random source's white outputs →
  **Period (rate)**, Complex-Osc pitch, **Timbre (wavefold)**, and LPG amount. Set the
  Modulation Osc to LFO for an extra slow wobble into FM depth. Hit record, let it drift,
  cherry-pick. Add **Gravity** with a couple of bounce-walls modulating timbre + cutoff. `research/links/vc-drone-buchla-idmmag-review.md`
- **Pluck/bongo sequence under a drone:** 5-step sequencer → Complex-Osc pitch (small mod
  amount, gated by an envelope); the LPGs give the natural percussive ring. Run a **second
  fixed-pitch Complex-Osc voice as a sustained drone underneath** (4-voice poly). The odd-5
  steps self-evolve against any 4/4. `research/transcripts/vc-drone-buchla-omahs-ep8-seq-voltage.md`
- **Metallic fold drone:** fixed-pitch Complex Osc, push the **Timbre wavefold** up for the
  buzzy sheen, slow Random → Timbre for a shifting harmonic wall, LPG held open.

## 3. Rig integration

Generative bed under banjo/baritone → Valhalla + EchoBoy; the Random/Gravity engines mean it
evolves hands-free while you play the banjo. Bounce the best drift to audio early (CPU + you
can't exactly re-roll it). Definitive learning resource for the hardware concepts: **Todd
Barton**. `research/links/vc-drone-buchla-kvr-thread.md`

## 4. Best learning resources

1. **One Man And His Songs — "Buchla Easel V Tutorial" series** (Eps 2/4/8/9) — *the* deep
   dive, component by component. ★
2. **Arturia — "Buchla Easel V Ep.2: Modulation & Control Sources"** — clean official
   walkthrough.
3. **databroth / IDM Mag reviews** + the **KVR thread** (→ Todd Barton) for West-Coast theory.

## 5. Pitfalls / gotchas

- **Counterintuitive by design** — e.g. envelope attack/decay are long at the bottom, short
  at the top; LPGs aren't resonant filters. Expect to explore, not dial a known sound. `research/links/vc-drone-buchla-idmmag-review.md`
- **Generative = not exactly repeatable** — bounce the take you like.
- **CPU** adds up with poly + Gravity → freeze.

## 6. Captured sources

**Transcripts (6)** — `research/transcripts/`: vc-drone-buchla-omahs-ep2-complex-osc ·
omahs-ep4-mod-osc · omahs-ep8-seq-voltage · omahs-ep9-random-voltage · arturia-ep2-mod-control
· automaticgainsay-p8-seq.
**Links (3)** — `research/links/`: vc-drone-buchla-databroth-review · vc-drone-buchla-idmmag-review ·
vc-drone-buchla-kvr-thread.

## Sources

All claims cite a captured file in `research/transcripts/` or `research/links/` (first line =
the original URL). Primary: One Man And His Songs, Arturia tutorials, databroth, IDM Mag, KVR
(→ Todd Barton). **Honesty flag:** Arturia's Tips FAQ 403'd; recipes synthesized from the
component tutorials + reviews rather than a single ready-made drone-patch walkthrough.
