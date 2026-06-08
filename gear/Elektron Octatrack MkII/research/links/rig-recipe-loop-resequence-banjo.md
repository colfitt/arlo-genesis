Manual: Octatrack MkII User Manual, §17.1.4 (p.105), §17.2.1 (p.107), §13 slice/attributes, Appendix A.2 Flex (p.118)
Elektron manual

# RECIPE — "Loop the banjo and re-sequence it" (banjo-as-glitch-lead)

Capture a Gold Tone EBM-5 banjo phrase (GK-5 → VG-800 → board → OT input), then turn it into a sliced, re-triggered, re-pitched sequence the banjo never actually played.

## Capture
1. Banjo feed → OT **input A** (mono GK-5/VG-800 print) or **A/B** if stereo'd by the board.
2. **Track 1 = Flex machine**, assign **recorder buffer 1** (top of Flex slot list).
3. **RECORDING SETUP 1**: INAB = A (or A B), RLEN = e.g. 16 or MAX, TRIG = ONE2. **QREC = PLEN** so capture starts at the next pattern wrap (bar-aligned).
4. Play a banjo roll; **[TRACK 1]+[REC1]** to capture (or a one-shot recorder trig in GRID mode). The capture inherits the OT BPM.

## Slice
5. Open buffer in audio editor ([TRACK 1]+[BANK]); TRIM to the phrase. **SLICE** ([AMP]) → CREATE SLICE GRID → 16 SLICES. For transient-accurate slicing on picks, set **TSNS** high (BEAT timestretch) so each slice = one note/pick.
6. **SRC SETUP: SLIC = ON**, **TSTR = AUTO** (loop stays in BPM).

## Re-sequence into glitch-lead
7. GRID RECORDING ([RECORD]); clear trigs ([FUNC]+[PLAY]); place a sample trig per step.
8. **CREATE RANDOM LOCKS** to scatter the slices, or hand-lock **STRT** (slice) per step for a composed line.
9. Per-step **PITCH p-locks** → the banjo climbs/falls into runs it can't physically play. Add **RTRG/RTIM** (retrig) on a couple of steps for rolls; negative **RATE** on others for reversed picks.
10. **Conditional / probability trigs** (e.g. 60–80% chance, or 1:2 / 1:4) so the line mutates each loop — generative banjo-as-lead.
11. FX: light **Lo-Fi** + **Spring Reverb** for the degraded, dustbowl character; keep it on-aesthetic.

## Perform it
- Two scenes: A = the sliced line dry/open; B = filter swept + Lo-Fi crushed + freeze-delay catching fragments. Crossfade to dissolve the lead into texture.
- Or sync this to a live Pickup-machine banjo loop ([TRACK]+[TEMPO]) so the played loop and the re-sequenced slices interlock.

## Alt — live looper version
Skip slicing: use a **Pickup machine** (pickup-machine-live-loop-setup.md) to capture + overdub the banjo as a straight loop, then re-pitch (PITCH) / reverse (DIR=REV) it live. Faster, more performative; less surgical than the Flex/slice route.
