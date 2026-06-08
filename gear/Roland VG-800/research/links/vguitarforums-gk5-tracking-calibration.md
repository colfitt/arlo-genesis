https://www.vguitarforums.com/smf/index.php?topic=36028.0
vguitarforums.com · "GM-800 - Tips and Tricks to obtain best tracking" thread (Elantric/mod + Allomerus, Mikejames, Giffenf) · 2023–2025

NOTE: This is the GM-800 tracking thread, but it is the *same Serial GK / GK-5 platform* as the VG-800 — the GK SETTING calibration menus and per-string SENS behavior are shared. Treated as directly applicable to GK-5 tracking on the VG-800; values verified against multiple posters.

## Per-string SENS (sensitivity) — concrete starting numbers
- **Default SENS = 65 for all strings.** Multiple posters call this too hot — it over-drives the divided pickup and causes ghost/hanging notes and wobble.
- **Elantric (mod) recommends lowering to ~35 as a starting point**, then fine-tune per string.
- **Allomerus (June 2025): the two highest strings needed SENS above 40**, while the lower strings sat lower — i.e. SENS is NOT uniform across strings; thin strings often want MORE sensitivity than fat ones.
- **Mikejames (Aug 2023): tune SENS until the on-screen graphic bar reaches ~75% on a normal-strength pick.** That visual target (bar ~3/4 full) is the practical calibration goal, not a fixed number — "values differ based on the pickup's distance to the string and the strength of your picking."
- Access path: **MENU > GK SETTINGS > (2nd page) > per-string sensitivity.** On the VG-800 this is the GK SETTING / SENS + DISTANCE routine (up to 10 saved GK profiles, one per guitar — calibrate each instrument once).

## DISTANCE
- Separate page where you enter the actual physical distance (pickup center → saddle) per string. Improves pitch detection math. Do this per instrument.

## False-trigger / wobble taming (Master-section params)
Three settings reduce false triggers and ghost notes (per-scene on GM-800; VG-800 exposes the equivalents in GUITAR-TO-MIDI / INST):
- **Low Velocity Cut**
- **Dynamics**
- **Play Feel**
Elantric: these "are unique per each SCENE and user's preference to tame false triggers."

## Pickup-height / converter note
- For legacy GK-3 → GKC-AD converter users (not GK-5), Giffenf (Feb 2024) found **dropping the converter GAIN from 3 to 2 eliminated "ghost and hanging notes all over the place."** Lesson that transfers: when in doubt, REDUCE input level/sensitivity rather than raise it.

## Rig takeaway (baritone JM + banjo)
- Start every string at SENS ~35, then raise the high/thin strings (and the banjo 5th drone) toward 40+ until the on-screen bar hits ~75%. Fat/low baritone strings stay LOW to stop wobble. Set DISTANCE accurately. Save one GK profile per instrument.
