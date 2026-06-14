https://valhalladsp.com/2010/12/03/valhallashimmer-tips-and-tricks-using-diffusion-instead-of-predelay/
+ https://valhalladsp.com/2010/11/30/valhallashimmer-tips-and-tricks-diffusion/
valhalladsp.com · Sean Costello · official Diffusion tips

Shimmer has **NO predelay knob** — Diffusion does that job (and shapes the whole attack).

## Diffusion as the attack / predelay control
- **≥ 0.9** = fast attack (reverb arrives almost immediately).
- **0.5–0.618** = the reverb fades in very SLOWLY (the reverse-reverb / swell range).
- **In between** = a non-instant attack that "sits behind the dry signal in a way that's
  similar to how predelay is often used" → use this to keep the dry banjo/baritone pitch
  legible *before* the wall blooms in. As Diffusion rises, "some frequencies make it
  through quicker than others," so the onset develops naturally.

## Why it matters for this rig
You shape the swell-in of the wall purely with Diffusion (no predelay). For ambient beds
under a played source: drop Diffusion toward 0.55–0.65 so the wall rises slowly *after*
the note, leaving the attack/pitch clear; push toward 0.9 for an immediate dense wash.

## Diffusion also = the reverb "density" engine
Shimmer is a **diffusion-based reverb** (the smooth tail comes from the diffusor network,
not a delay-line reverb like Room). So Diffusion is doing double duty: density/smoothness
AND attack/predelay. Low = grainy echoes; high = smooth dense reverb.
