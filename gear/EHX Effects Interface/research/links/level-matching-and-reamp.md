https://www.ehx.com/wp-content/uploads/2025/11/EIHP_manual_Web_v1.pdf
EHX · EIHP Manual v1.0 — Hardware Overview (sliders/meters) + level/re-amp practice · 2025-11
(synthesized with MusicRadar's "pedalboard-friendly levels / no DI box" point and the Guitar World "gain matching" + "input meters crucial" notes)

The level-matching and re-amp workflow — how the sliders and meters do the VG-800-line-↔-instrument-level job without a transformer re-amp box.

THE CONTROLS (manual, Hardware Overview):
- INPUT Sliders L/R: "Sets the level of the signal INTO the Effects Interface from the INPUT L and R jacks." (Trims the wet RETURN coming back from your pedals.)
- OUTPUT Sliders L/R: "Sets the level of the signal SENT by the Effects Interface on the OUTPUT L and R jacks." (Sets how hot the board/pedals are driven — the instrument-vs-line knob.)
- INPUT Meter LEDs: "The orange LED lights when the signal level is above -6 dB, and the red LED lights when the signal is above -3 dB." → SET THE RETURN so it peaks orange, never red.
- Jack roles for re-amp: "To use a physical guitar pedal as a plugin in your DAW, plug that pedal's OUTPUT into one of these [INPUT] jacks… plug this [OUTPUT jack] into that pedal's INPUT jack."
- DIRECT MONITOR: hear the INPUT jacks directly (interface/standalone). Headphone jack carries the OUTPUT (L/R) signal.

THE LEVEL-MATCHING CLAIM (MusicRadar / guitar.com): inputs and outputs run at "pedalboard-friendly levels," which "eliminates the need for additional converters or DI boxes" / "separate converters or direct boxes." The 2 MΩ input and 330 Ω output + +7/+8 dBu headroom mean it both ACCEPTS a hot/line source (trim with INPUT sliders) and DELIVERS instrument level to a pedal front-end (set with OUTPUT sliders) — no passive re-amp transformer required. (Guitar World frames the sliders as "level/monitor sliders for gain matching" and calls the stereo input meters "crucial.")

RE-AMP WORKFLOW (the practical recipe, consistent across the manual + Sweetwater/Fluff + PedalScapes):
1. Record the source dry to a DAW track (DI, VG-800 output, synth, drums, vocal).
2. Patch OUTPUT jacks → front of your pedal chain; end of chain → INPUT jacks (mono loop or stereo).
3. Insert the Effects Interface plugin on the dry track; connect Audio > Stereo (or Mono).
4. Set OUTPUT sliders so the pedals see the level they expect (instrument level for a guitar front-end); set INPUT sliders so the return peaks orange (−6) not red (−3).
5. Use the plugin's MIX (Audio Mode only) to blend dry track with the wet pedal return — lets you "dial something back just a little" that an on/off pedal can't (Fluff), or bring back the natural attack/clarity of the dry source (EHX official demo, on horns).
6. Record/print the wet return in REAL TIME to a new track (no offline bounce).

WHY IT FITS THE VG-800 PROBLEM: the VG-800's hotter, line-ish output goes into the INPUT (trim with INPUT sliders, watch meters), or — for re-amping — record it dry first and drive the board from the OUTPUT sliders at instrument level. Either way the level reconciliation is done with the gain sliders + meters in the computer workflow, not a transformer. (Per the dossier, for purely LIVE level fixes the VG-800's own output level + the board's tolerance is simpler; reserve the Effects Interface for studio commitment passes.)

DUAL-MONO BONUS (MusicRadar / EHX demo): the two channels can carry independent mono signals at once (e.g. a phaser on a Wurlitzer track left, a compressor+delay on a drum bus right) — handy for processing two different sources through two different pedal paths in one pass.
