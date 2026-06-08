https://www.youtube.com/watch?v=ofs27Qq0Plw
Akai Professional · Getting Started with MPC Sample | Resampling · 2026 · 4:08

> Official, AC50-specific. The exact resampling + sample-recall button sequences. (Auto-captions mis-transcribe "MPC Sample" as "MPC Souncloud" — ignore.) Cleaned to prose.

## Method 1 — full Resample workflow (bake FX into a new pad)
Scenario: a loop is playing with a **Tape Emulator** Knob FX on it; you want that processed loop as its own sample.
1. Go to **Sample**, pick an **empty pad** (he uses Pad 13).
2. **Sample Record** → change **Source = Resample**.
3. Set **sample length with Knob 2**:
   - **Free** = no fixed length.
   - **Sequence** = uses the **sequence length** as the sampling time (recommended for loops — gives an exact loop).
4. **Strike the pad** → it waits for signal → **press Play**. It records, then **stops automatically at the end of the sequence**.
5. Press Stop. You now have the exact loop, **resampled with effects baked in**. Turn off the original live FX.
6. The resampled pad can now be **chopped** (Chop mode) or retuned.

## Method 2 — one-shot Resample shortcut
- **Sample + Pad 11** auto-resamples the current source (a vinyl sample, with its effects on) straight to that pad with the FX printed. Then retune / chop as normal.

## Sample Recall (background buffer)
- The MPC Sample is **continuously recording a ~20-second background buffer**.
- If you played something good and didn't capture it: **Shift + Sample Recall** → it drops onto the **next available pad**.
- Select that pad → **Trim** → use **Pad 13 to truncate** → zoom to the front, refine the start point → **Shift + Pad 13** confirms. Now it's a clean sample with the FX + recall.
- Then **Chop mode** → use over the beat; change tuning.

Takeaway for THIS rig: this is the "resample bed → re-mangle" generative loop in the dossier §13(d). Source = Resample + Sequence length is the clean way to bounce a 1–2 bar loop with LoFi/Color FX printed, then Chop *that* and rebuild a degraded variation.
