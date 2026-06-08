https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal
tapeop.com (studio review) + chasebliss.com manual + elektronauts.com forum · accessed 2026-06-03

# Clean stereo: MISO / SPREAD / Bounce + where it sits in a chain (concrete how-to)

Practical notes on Clean's stereo features and chain placement, with an honest read on whether the width is tasteful or a gimmick. SOURCED unless marked FIRST-PRINCIPLES.

## The three stereo dips (how to wire them — SOURCED, manual + video)
- **MISO (Mono In, Stereo Out):** TS cable into the input, **TRS cable out**, flip the MISO dip. Splits a mono source to a true stereo output. This is the dip you need in a mono-front-of-board rig to *start* stereo at Clean.
- **SPREAD:** processes EQ, compressor, and swell each with their own distinct stereo motion, and makes the L/R dynamic/envelope response independent — produces stereo widening even from a mono input. Works in any I/O configuration.
- **Spread routing (Hidden Option, on the Physics toggle):** assign SPREAD to the EQ *or* to volume-based effects independently — e.g. keep identical compression on both channels but take stereo movement only from the EQ. This is the "tasteful" lever.

## Is the width tasteful or a gimmick? (SOURCED — honest)
- Tape Op's verdict on SPREAD: the swell/EQ/compressor are *"all processed in different ways, in endless combinations"* that *"often result in weird and wild stereo widening, even with mono signals."* So the **default SPREAD character is experimental/aggressive, NOT a subtle widener.**
- The Devin Belanger demo (separate transcript in this folder) is the counterpoint: he gets **"really beautiful natural stereo movement that doesn't phase out,"** and stresses it's **"fully mono-compatible because there's no weird tricks, no digital DSP"** — pure analog, no phase cancellation when summed to mono.
- **Honest reconciliation:** the stereo is mono-safe (no phasing) but how wild it sounds is entirely a dialing question. For tasteful width: use **spread-routing to put SPREAD on EQ only** (identical comp both sides), keep **Physics centered** (stable, not twitchy), and **blend Dry up the middle** for a mono core — Belanger explicitly pulls the dry signal back in "for that core mono signal down the middle" when SPREAD gets too intense. (Dry-center technique = SOURCED from his demo.)

## Continuous motion / "Bounce" (SOURCED — manual)
"Bounce" is the LFO-style continuous-motion mode in the CONTROL dip bank: activate the Bounce dip, pick which knob(s) to modulate, set the SWEEP, then use **Sensitivity to set the ramp rate.** The modulated knob's physical position sets the top or bottom of the modulation range (depending on SWEEP). Used on the EQ + SPREAD this is the auto-panning/widening "drift." (NOTE: Clean's clock-sync for Bounce is feature-listed by CB but UNCONFIRMED at the CC level — see Gear/Chase Bliss Blooper/research/links/cb-stack-clock-sync-per-pedal.md. Don't assume Bounce locks to the grid.)

## Chain placement (SOURCED + FIRST-PRINCIPLES)
- **Tape Op uses Clean END-of-chain as a stereo mix-bus compressor** and it excels there — but it *"wants to be manipulated, tweaked, and played like an instrument,"* not set-and-forget.
- An Elektronauts owner runs it **first in the chain** (Clean → Gen Loss → HX One → Lossy → Iridium) — confirming it's equally happy as a front anchor.
- **FIRST-PRINCIPLES for this rig:** Clean lives FRONT (after the tuner) and runs **mono** there, so MISO/SPREAD are dormant by default — the rig doesn't go stereo until the CE-2W much later. Two ways to exploit the stereo:
  1. **Leave it mono front** (its dynamics/level job) and ignore SPREAD — simplest, on-brand for a level anchor.
  2. **Flip MISO front** to split the mono source to stereo immediately, feeding stereo into everything downstream — only worth it if the downstream pedals stay stereo. In this board the dirt stages (Colour Box, 108, Hizumitas) are mono, so front-MISO mostly makes sense if redeployed.
  3. **Redeploy end-of-chain as a stereo bus comp/widener** (Tape Op's preferred use) if the rig ever frees up a stereo end slot — that's where MISO/SPREAD/Bounce actually pay off.

## Other stereo-adjacent tricks (SOURCED)
- **Feedback↔feedforward limiting blend** (Dynamics noon→3:00): the maker and Tape Op both flag this as rare — smooth/natural (feedback) to snappy/aggressive (feedforward) on one knob. Great for a stereo glue comp at the end.
- **Sidechain (1/8" jack):** Tape Op triggers the **Dynamic Swell from a vocal sidechain into reverb** for a "weird, swelling reverb gate." In this rig the sidechain could duck/swell Clean from the Digitakt or another instrument for rhythmic stereo motion.

## Sources
- https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal (SPREAD = wild widening even mono; end-of-chain mix-bus use; "played like an instrument"; feedback/feedforward; vocal sidechain swell)
- https://www.elektronauts.com/t/chase-bliss-clean-the-creative-compressor-pedal/223147 (owner running it first in chain; gains loud with no noise)
- Clean Video Manual transcript (MISO/SPREAD wiring, Bounce, spread-routing): Gear/Chase Bliss Clean/research/transcripts/daily-Chase Bliss - Clean Video Manual (official walkthrough).md
- Devin Belanger transcript (natural mono-safe stereo, dry-center technique): Gear/Chase Bliss Clean/research/transcripts/Devin Belanger - Chase Bliss Clean the most USEFUL pedal I've bought all year.md
