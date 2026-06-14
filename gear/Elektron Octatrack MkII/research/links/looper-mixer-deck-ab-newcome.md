https://audiodestrukt.wordpress.com/2024/02/19/setting-up-the-octatrack-as-a-looper-mixer/
audio destrukt (blog) · author "newcome" · Feb 19 2024

# LOOPER/MIXER TEMPLATE — two-deck (A=T1-4 / B=T5-8) with min/max crossfader volume locks

A clean, concrete template for the OT as a two-deck looper/mixer (the Stimming-style A/B split, with values).

## Track layout
- **Deck A = Tracks 1–4** (crossfader LEFT), **Deck B = Tracks 5–8** (crossfader RIGHT).
- **Tracks 1 & 5 = THRU** machines (the two input/processing channels — these are the tracks that can host the input pairs).
- **Tracks 2 & 6 = FLEX** machines (the loop/resample channels).

## Recording setup (per loop track)
- **One-shot RECORD trig at step 1** + a **note trig to start the loop, also at step 1**.
- **Pattern length = 64 steps (4 bars)**.
- **Thru track input level = +64** (described as "the maximum" for the Thru input).

## Crossfader scenes
- **Lock the VOLUME (XVOL) parameter min/max on either side** — Deck A tracks XVOL = MAX @ Scene A / MIN @ Scene B; Deck B opposite → equal-power A↔B deck crossfade, no center dip.

## Rig fit
A turnkey two-deck shell: put the pedalboard print on the Track-1 Thru (Deck A) and a banjo/VG-800 loop deck on Track-5 Thru (Deck B), crossfade between two live sources. The +64 Thru input level and the step-1 one-shot-rec + note-trig pairing are the two concrete details that make a Thru loop actually capture and play. Combine with the per-deck XVOL min/max locks (already the rig's equal-power scene method) for laptop-free A/B performance.

PROVENANCE: community (audio destrukt / newcome, cited). Conceptual on FX; concrete on layout, +64 input, 64-step length, step-1 trig pairing, XVOL min/max.
