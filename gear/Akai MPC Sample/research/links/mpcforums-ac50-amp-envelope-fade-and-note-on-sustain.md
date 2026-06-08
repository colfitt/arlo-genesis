https://www.mpc-forums.com/viewtopic.php?f=50&t=220644
mpc-forums.com (MPC Sample subforum) · "joebataz" (Q) + answers citing official manual · 2026

AC50-SPECIFIC, BUTTON-PRECISE. Two of the most common new-owner confusions on the AC50, with exact on-device steps. Both answers cite the official MPC Sample User Guide v1.3.0 (RevA) PDF:
https://cdn.inmusicbrands.com/akai/sample/MPC%20Sample%20-%20User%20Guide%20-%20v1.3.0%20%28RevA%29.pdf

## GOTCHA: "My own samples fade out in volume" (the AMP envelope DECAY)
Symptom (joebataz): loaded WAVs that "play fine outside" the MPC start "fading of the volume" once on a pad; factory/demo samples don't. Cause: the **AMP envelope DECAY** is ramping the level down.
FIX (manual pg 26), exact steps:
- In Sample mode with the sample shown, tap the **B1 button (top-left) TWICE to reach AMP ENV**.
- Push the data wheel once → cursor moves to **DECAY**.
- Rotate the data wheel; watch the green decay line at the end move. **Rotate fully left to "0" = no fade-out.**
- **Hold SHIFT** and DECAY changes to **"DECAY FROM"** — while holding SHIFT, rotate the wheel to choose whether decay starts from the **start or end** of the sample.
- TAKEAWAY for this rig: long sustained drone slices need DECAY = 0 (or DECAY FROM end) or they'll fade out unexpectedly.

## TIP: "Keep a sample playing until I release the pad" = NOTE ON (gate/hold)
FIX (manual pg 32), exact steps:
- In Sample mode with the sample shown, **hold SHIFT and press the blue CHOP button** — its under-label reads **NOTE ON**. The white note block in the sample window lights up = NOTE ON engaged for that note/sample.
- "Try this on a long loop." With NOTE ON, the pad behaves as a gate (sounds while held, stops on release) instead of a one-shot.

## General principle stated in-thread (worth remembering)
"SHIFT is for engaging/enabling the text underneath the buttons/pads." → On the AC50, almost every hidden/secondary function is the **blue text printed beneath a button/pad, reached via SHIFT**. When hunting for a feature, SHIFT + the relevant button is the first thing to try (e.g. SHIFT+CHOP = Note On, SHIFT in Trim = Normalize, SHIFT+Pad 8 = MIDI/knob config).
