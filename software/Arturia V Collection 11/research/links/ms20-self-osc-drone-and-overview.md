(roundup — see inline URLs)
Arturia overview + KVR + legacy-forum · "MS-20 V self-oscillating-filter drones, MK1/MK2 character, no-oscillator tone" · 2023–2024 · triangulated (Arturia overview 403s direct fetch; recovered via search excerpts)

== Self-oscillating-filter drone (no VCO needed) ==
- https://legacy-forum.arturia.com/index.php?topic=106850.0 ("Self Oscillating Filter") + Filter MS-20 docs: with **Limit Resonance OFF**, the filters self-oscillate into "very loud" pure tones — "have fun, but go easy on the output volume so you don't break anything."
- Recipe (instrument): turn both VCO levels down/off → push **Peak (resonance)** on the LPF toward oscillation → the filter itself rings as a sine-ish tone. Set the cutoff to your drone pitch. Add the HPF self-oscillating too for a two-tone beating interval. Modulate cutoff slowly (MG triangle, or EG1 in **Loop** mode acting as a 2nd LFO) for a wandering drone.
- This is the same trick as Synthi V's self-resonating filter (its own guide) — MS-20 V's version is grittier/screamier, especially on MK2/OTA.

== MK1 vs MK2 for the aesthetic ==
- **MK1 (KORG 35 chip):** less low end, more noise, raw and gritty when distorting, "less screamy," CPU-heavier (can glitch in Poly). → the dirtier, lo-fi-leaning choice.
- **MK2 (OTA):** more subs, cleaner and *screamier* resonance, smoother at high Peak, lighter CPU. → the choice when you want the howling self-oscillation to sing.

== Overview-page feature confirms (https://www.arturia.com/products/software-instruments/korg-ms-20-v/overview) ==
- "Ultra-fat oscillators, rule-breaking External Signal Processor (ESP), and screaming filters," every non-linear nuance modeled. Two filter emulations: KORG IC-35 chip + OTA.
- 6-voice poly + unison; SQ-10-style 3×12-step sequencer; 4 FX slots (series/parallel, 16 effects); hard sync + ring mod; FM module fed by MG / EGs / **External Signal**; semi-modular patch bay "to push its sound into uncharted territory."
- ESP: "sidechaining to process external audio … run your own audio through the filters + crunchy output, create wild feedback routing, use incoming sound to generate envelope follower signals."

== Why it's the rig-integration star ==
Of the whole V Collection, it's the one with a dedicated external-audio path (ESP + EXTERNAL IN) AND self-oscillating analog filters AND a free effect-version. The drone use (self-osc filters as tone sources) works in any host with no routing; the external-audio mangling is the standout idea but carries the AU-sidechain caveat (separate file).
