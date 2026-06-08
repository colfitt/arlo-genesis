https://www.radialeng.com/blog/the-reamping-workflow
radialeng.com · Radial Engineering (blog) · 2023-05-09

Radial's own written step-by-step reamping primer. First-party, manufacturer-authoritative. Three concrete steps:

## Step 1 — Record the dry guitar track
- Guitar → **DI box** (converts hi-Z instrument to low-Z balanced) → interface → DAW. Record unprocessed.
- Optional monitoring: feed an amp from the **DI's THRU** while tracking.
- Focus on **performance, not tone** at this stage.

## Step 2 — Send the track to the rig via the reamp box
- In the DAW, **assign the recorded DI track to an interface output.**
- Interface **line-level output → reamp box input** (balanced TRS/XLR).
- **Reamp box output → guitar rig** via a standard ¼" instrument cable. **Route into the pedalboard first, then the amp**, if using effects.
- **Adjust the reamp box's volume control AND the DAW track level to match the direct-guitar output level.** Test playback to confirm signal reaches the amp.

## Step 3 — Capture the amplified signal
- Mic the rig. Create a **new DAW track for the mic capture.**
- **Set the mic track's output to the stereo bus — NOT to the reamp box's output** (this is the feedback-loop avoidance: never route the record return back out the reamp send).
- Press record; the DAW plays the dry track through the amp while the mic track records the processed result simultaneously.

## Pro tips (stated)
- **Maximize dry-track output level without clipping** (best reamp S/N).
- **Apply DAW effects (EQ, limiting) on the way out** to shape what hits the rig.
- A combination DI+reamp unit (Reamp Station) streamlines repeated reamping.

## Coverage note
This blog does NOT cover clip LEDs, ground lift / hum, the 180° polarity switch, or parallel/blend reamping — those live in the manual and the X-Amp FAQ (`radial-xamp-faq.md`). It is the clean conceptual skeleton; the X-Amp-specific level/ground/phase detail is in the dossier and manual.
