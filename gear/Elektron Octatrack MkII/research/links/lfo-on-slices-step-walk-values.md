https://www.elektronauts.com/t/lfos-meet-slices-techniques/28821
Elektronauts · users Voov_ov (#7/#8), astricii (#17), tomes (#18) · thread "LFOs meet Slices. techniques"

# LFO → STRT slice-walk — exact LFO values to step through a sliced sample automatically

The move behind "LFO on STRT scrubs through a chain" (already in the UsageGuide §7) — but with the concrete LFO settings that actually walk slice 1→2→3→…→8 cleanly instead of sticking/jumping.

## The WORKING setting (Voov_ov, post #8) — walks 8 slices in order
- **Waveform = RMP (Ramp)**
- **SPD (speed) = 33**
- **MULT = x2**
- **DEPTH = 16**
- **Trig mode = SYNC TRIG** (re-zeroes the ramp on each trig so it's repeatable)
- **Destination = STRT** (slice start)
- **Slice count = 8**
- Result: clean march "slice 1 - slice 2 - … - slice 8" across the pattern.

## The FAILED setting (Voov_ov, post #7) — documented so you can avoid it
- Sawtooth, SPD 64, MULT x2, DEPTH 8, SYNC TRIG → slices stuck until trig 9 then progressed irregularly. (DEPTH too low + wrong wave for an 8-slice walk.)

## Variant — portamento/sweep hold (astricii, #17)
- **Ramp wave set to HALF** = sweeps from zero-mod up to max then HOLDS until the next trig → glide/portamento-style scrub through the sample rather than discrete slice steps.

## Granular-glitch variant (tomes, #18, and corroborated elsewhere)
- **RAMP LFO at MAX depth → RETRIG amount**, with **retrig TIME very fast** → approaches granular/glitch textures. (Pairs with LFO→STRT for scrub+grain at once.)

## Rig fit
Pickup-capture a banjo phrase or fuzz wall, QUICK-CREATE 8-SLICE GRID, then drop this RMP/SPD33/x2/DEPTH16/STRT LFO on it → the slices auto-resequence into a line the banjo never played (the §4 "re-sequence the wall" recipe, automated). The HALF-ramp portamento variant = a smeared, "recorded-wrong" scrub for drone beds; the granular-retrig variant = shoegaze grain.

PROVENANCE: community (Elektronauts, cited per-post). DEPTH is sample-length-dependent — 16 is for an 8-slice file; scale to slice count.
