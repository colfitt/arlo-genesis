https://www.electronicaudioexperiments.com/blog/2026/4/29/big-time
EAE Big Time blog (John Snyder) + SonicState Superbooth interview + otomachines.com/bim · accessed 2026-06-19

# Big Time heritage as dialing — mapping the early-'80s rackmount / Oto BIM lineage to actual controls

Big Time models early-'80s rackmount delays (analog preamp in, analog limiter inside the feedback loop, digital core). The lineage is well-documented, but it's only useful if you can turn it into knob positions. This note maps each first-party-sourced ancestor onto the **specific Big Time controls** that recreate its character. Each leg is scoped narrowly — an ancestor maps to one or two controls, not the whole pedal.

## Oto Machines BIM character → 0.5X + Warm/Analog + Saturated + moderate COLOR/FEEDBACK

The BIM is Big Time's closest living peer: an analog-preamp-into-12-bit-digital delay whose feedback runs through analog companders / limiters / LPF, giving (Oto's own copy) "a sweet degradation and dark damping that the 100% digital delay boxes can't offer." To get that hybrid degradation on Big Time:

- **0.5X ON** — Snyder-confirmed (Superbooth) this drops 32→12-bit and halves the sample rate, i.e. the BIM's 12-bit AD/DA core.
- **VOICING Warm or Analog** — the analog LPF stage that does the "dark damping."
- **STATE Saturated** — the analog-limited graceful degradation (Saturated is also the manual's *default* destruction state, so you get the dirty recirculation without going all the way to misbias).
- **Moderate COLOR / FEEDBACK** — so repeats actually recirculate through the analog + 12-bit path and accumulate the degradation, rather than dying after one pass.

## PCM42 "disintegration" → low COLOR + high FEEDBACK into COMPRESSED

Snyder's PCM42 trick was throwing the limiter calibration out of whack for hyper-compressed, disintegrating infinite delays — and that influence is scoped to the **COMPRESSED / "Blue Mode" STATE only**, not the whole architecture. To recreate it:

- **STATE COMPRESSED** ("Blue Mode").
- **LOW COLOR + HIGH FEEDBACK** — let the echoes climb into the limiter, which is where the disintegration happens. (Low preamp gain, high recirculation = the "Andy Wallace" limiter-abuse character.)

## VOICING ↔ rackmount LPF (two named cutoffs)

- **Warm ≈ 10 kHz = the PCM42 X2 brickwall.** Snyder, first-party: the PCM42's X2 filter mode is a "steep brickwall at 10kHz… cuts off everything at 10k" — Big Time's Warm voicing recreates that cutoff.
- **Analog ≈ 4 kHz = an EAE Sending V2 callback.** Snyder (Superbooth) says Big Time's Analog VOICING is "a callback to our Sending V2 delay," a gentle ~4 kHz slope — the darker BBD-ish Sending tone lives on as one of the four voicings.

## Ursa Major Space Station → CLUSTER smear

The Space Station's modulated multi-taps are the spiritual influence on the **CLUSTER** slider — scope: Space Station → CLUSTER only, not the limiter architecture. Note that in **MOD** mode CLUSTER becomes a thickener / stereo-widener / secondary-modulation rather than a comb/metallic resonator, so the "smear" character is a SHORT/LONG-mode CLUSTER move.

## One honest line on the crowd lore

The **TC 2290**, **Lexicon Prime Time 93**, and Eventide rack units that owners keep invoking on forums are **crowd associations / lore, not first-party lineage** (ModWiggler: DukeOfPrunes names "old TC 2290 rack effects and some earlier Eventide rack gear"; folpon invokes the Prime Time 93 / Daniel Lanois lore). First-party naming stays **PCM42 + Ursa Major Space Station** (plus EAE Sending / Clean / Halberd / Glaive circuit blocks, and the PDS 20/20 as a sentimental nod). And the **BIM-peer claim itself rests on Oto's OWN architecture description** — a near-identical hybrid topology, "mainly analog processing" with a 12-bit AD/DA delay section — **not** on any Snyder statement. The EAE blog never names the BIM; the "Snyder praises BIM/BAM" line is an unverified forum paraphrase. Keep the scoping honest.

## Sources

First-party
- Electronic Audio Experiments — Big Time blog, John Snyder (electronicaudioexperiments.com/blog/2026/4/29/big-time): PCM42 mis-calibrated-limiter → COMPRESSED/"Blue Mode"; PCM42 X2 10k brickwall; Ursa Major Space Station → CLUSTER; reused circuit blocks (Sending, Clean, Halberd, Glaive); PDS 20/20 sentimental nod
- SonicState Superbooth — John Snyder / EAE interview; corpus transcript `gear/Chase Bliss Big Time/research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md` (lines 46–47 VOICING frequencies + Sending V2 callback; line 58 0.5X = 12-bit + half rate)
- Chase Bliss Big Time manual — local PDF, hybrid topology / I/O (p.4, p.42)

Comparison / lineage
- otomachines.com/bim; reverb.com BIM listing — Oto's own hybrid-topology description (analog processing + 12-bit AD/DA for the delay section)

Community (lore / provenance only — not first-party)
- ModWiggler thread (modwiggler.com/forum/viewtopic.php?p=4463633) + corpus `gear/Chase Bliss Big Time/research/links/modwiggler-bigtime-thread.md` — TC 2290 / Prime Time 93 / Eventide rack crowd associations

Corpus
- `gear/Chase Bliss Big Time/research/links/eae-lineage-artists-and-design.md` (lineage scoping)
- `research/bloops/2026-06-19-chase-bliss-big-time-l2.md` (L2 digest — lineage-as-dialing lens)
