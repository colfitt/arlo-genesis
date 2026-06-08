https://forum.morningstar.io/t/changing-presets-on-an-h90/5139
Morningstar Engineering user forum · kitemonkey (Q) / thingswithstrings (A) · Jan 31 – Feb 2, 2023

# Switching H90 Programs from a Morningstar (MC6/MC8) — the "no default CC map" gotcha

Community thread (outside Eventide) on driving the H90 from a Morningstar controller.

## The core gotcha
> "the H90 strangely has no pre-fabbed dedicated MIDI CC/PC numbers. you have to do everything."

Unlike many pedals, the H90 ships with **no default CC→parameter map**. Every CC assignment must be created manually — on the pedal in **Parameters mode** (manual §6.4) by mapping a parameter to a CC#, or via Global Control for global functions. Don't expect a factory CC sheet.

## Program change mapping
- Set the MIDI channel in **Global** settings (manual §7.3).
- For Program changes, **send the PC number that matches the Program number in the H90** (PC N → Program N; mind the PC Offset 1–100 vs 0–99 setting).
- The example in-thread conflated CC and PC ("CC #4 ... makes the H90 go to program 4") — the accurate mechanism is: **PC selects Programs**, **CC controls parameters/active-bypass** (corroborated by the Eventide MIDI thread). Use PC for scene recall.

## Compatibility note
- **H90 Control is NOT compatible with the H9** (different app), but H9 presets/lists CAN be loaded/imported into H90 Control (see the H9-import file).

## Rig relevance
Confirms the rig workflow: a Morningstar (or the Digitakt 2) recalls H90 Programs via **PC = Program number**, and any live parameter moves require **manually mapping CCs** on the H90 first (there's no plug-and-play CC template). Build a small CC map (Active/Bypass, tap, a HotKnob or two) once, document the CC#s, and store it with the rig's MIDI sheet.
