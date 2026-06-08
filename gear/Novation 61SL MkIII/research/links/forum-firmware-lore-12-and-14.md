https://novationmusic.com/en/news/sl-mkiii-firmware-update-12
novationmusic.com + synthanatomy.com · official 1.2 changelog + SynthAnatomy 1.4 coverage (Jun 2020)

Consolidated firmware lore for the SL MkIII. The box shipped late-2018 underbaked; firmware did the heavy lifting.

## Firmware 1.2 (the big sequencer fix)
- **6 micro-steps per step** — off-grid placement for subtle timing shifts, fast triplet runs, glitch repeats.
- **Max gate/step length doubled to 32 steps** — notes can run longer than a bar within a 16-step pattern. (This is the "32 steps is possible" people quote — it's gate length, NOT 32 sequencer steps.)
- **Aftertouch assignable to any MIDI CC** — unlocks the channel-pressure strip for filter/mod-depth on soft synths and MIDI pedals (the dossier's recommended use).
- **NRPN support** — talks to NRPN-enabled devices, higher-than-7-bit resolution. Relevant for any deep-parameter hardware control.
- **Smoother/more responsive rotary encoders.**
- **Pattern scrolling without deselecting the playing pattern.**

## Firmware 1.4 (arp + generative + a CV addition)
Per SynthAnatomy (Jun 2020):
- **Per-part independent arpeggiators** — all 8 parts can arp simultaneously for polyrhythms.
- **Arpeggiator probability** — per-arp randomness → generative/evolving patterns.
- **Step probability/chance** on sequencer steps.
- **Sequencer transposition from the pads** as a live performance tool; **pattern octave transpose**.
- **Per-part swing** (on/off per part) — layer contrasting grooves.
- **Pattern shift** — offset start+end points together.
- **Pitch-bend-to-CV mapping** — *added in 1.4*, not present at launch. (PROVENANCE CORRECTION for the dossier §6, which lists "Pitch wheel can drive CV ±1 to ±12 semitones" as a feature but doesn't note it arrived in 1.4. The CV pitch-bend range is configurable per the CV guide; the *ability to route pitch-bend to CV at all* is a 1.4 addition.)
- **Bug fixes including one specifically for Logic Pro users.**

## State today
Post-1.4 (the version the local V2 user guide reflects) is the mature, well-regarded state. The generative toolset (random direction + per-step chance + per-arp probability + swing) is exactly what suits this rig's aleatoric/degradation aesthetic. No firmware past 1.4 is widely discussed — development effectively stopped there.
