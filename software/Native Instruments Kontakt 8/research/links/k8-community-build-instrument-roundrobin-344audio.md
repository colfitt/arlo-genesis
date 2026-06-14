https://www.344audio.com/post/article-how-to-build-a-kontakt-instrument-a-complete-guide-for-composers-sound-designers-part-3
344audio.com · "How To Build A Kontakt Instrument — Part 3" · current

# Building your own Kontakt instrument: groups, round-robins, loops

The "sample the rig into Kontakt" payoff — turning recorded hardware/pedalboard sounds into a playable .nki.

**Mapping & groups.** Organize your recorded takes into **groups** for velocity layers and round-robin variations. Example structure: RR1–RR4 (four round-robin versions), each holding soft/medium/hard velocity samples.

**Round-robin (so repeated notes don't sound machine-gunned):**
1. Open the **Group Editor**.
2. Choose **Group Start Options**.
3. Select each group in turn and set Group Start to **"cycle round robin."**
4. Assign each group's slot in the sequence (position 1, 2, 3, 4…). Kontakt then cycles through them on successive note-ons.

**Loop points & crossfade (Wave Editor).** Enable the **Sample Loop** tab; set **Loop Start / Loop End** to define the section, then dial the **X-Fade** value for a clean natural loop (longer fade = smoother but can dip volume).

**Polish.** Add dynamics/EQ via **Post Amp FX** and **Insert FX** tabs; add arpeggiators via the **Script Editor** sequencing presets.

**Rig note (drone/ambient).** For sustained-wall instruments you often DON'T need round-robins (you hold one note), so skip straight to loop+crossfade. Round-robins matter when you sample a *percussive/plucked* source (banjo pluck, MPC drum hit) and want repeats to feel alive — record 3–4 takes per note, drop them into RR1–RR4, cycle-round-robin.
