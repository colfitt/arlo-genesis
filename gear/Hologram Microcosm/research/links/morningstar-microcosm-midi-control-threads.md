https://forum.morningstar.io/t/microcosm-mix-setting-not-changing-with-mc8/6193
forum.morningstar.io (Morningstar MIDI-controller user forum) · 3 threads consolidated · 2022–2023

# Microcosm + Morningstar MC6/MC8 — MIDI control power-user notes & gotchas

Consolidates the three highest-signal Morningstar threads on driving the Microcosm from a MIDI footcontroller. Relevant because the rig may want a central MIDI brain alongside the Digitakt clock.

## GOTCHA 1 — CC sent immediately after a Program Change gets ignored
Thread: "Microcosm Mix setting not changing with MC8" (user **reydiverson**, 2023-07-27; Morningstar's **james**, 2023-07-31).
- Symptom: a preset-recall message that ALSO sent **CC 9 (Mix) = 127** changed the preset but the Mix knob didn't move on first press; it *did* work in double-tap mode.
- Cause: the Microcosm appears to **drop CCs that arrive while it's still processing the preset (PC) change**. The DSP is busy loading the engine and swallows the immediately-following CC.
- Fix attempted: **insert a delay of 100–500 ms between the PC and the CC** (Morningstar "delay" message). NOTE: the user reported delays up to 4 s still failing in his case, so treat this as **partially unresolved** — but the practical lesson stands: **never fire a parameter CC on the same instant as a preset change; stagger them.**

## GOTCHA 2 — expression-over-MIDI fires once, not continuously
Thread: "Microcosm and expression pedal" (user **Grub71**, 2022-05-08; Morningstar **Benjamin**, 2022-05-09).
- Symptom: a latched preset that assigned the expression pedal to Activity/Repeats/Filter only sent **a single CC value at the moment of preset selection** — no continuous sweep.
- Fix: use Morningstar's **"Select Expression Messages per Preset on the Fly"** feature so the EXP pedal streams continuous CC after the preset loads. Grub71: "Just tried it out and it works great."
- Implication for the rig: if you want a *continuous* swept parameter (e.g. opening the Filter on CC 8 across a build), either use the **Microcosm's own EXP IN jack** (true continuous, assignment persists across power cycles) or a properly configured continuous-expression MIDI stream — not a one-shot CC baked into a preset.

## GOTCHA 3 — no preset up/down CC
Thread: "Microcosm: Scroll through Presets?" (user **MurraysMagicTones** / **moley6knipe** / **funkbuero**, 2021-12 → 2022-01).
- The Microcosm has **no increment/decrement CC** for presets. To scroll, build a **PC Scroll counter** on the controller: set Starting=Min=lowest preset PC, Max=highest preset PC (presets are **PC 45–60**), then bind increment/decrement messages to the counter. funkbuero confirmed it works "after a bit of trying"; reboot the controller after saving.

## Net advice for the rig
- Stagger PC→CC by a delay; don't bundle them on the same press.
- For smooth sweeps, prefer the hardware EXP jack over MIDI one-shots.
- Preset scrolling = counter driving PC 45–60, no native up/down.
