https://www.youtube.com/watch?v=Z_VyQM6xQrM
Ned Rush · Ableton Tutorial — Ambient Sounds with Just Effects (no instruments) · ~2019

> **LITE NOTE (orchestrator-added):** Brilliant concept — make full ambient drones using
> ONLY audio effects, **no instrument and without pressing play** (effects self-oscillate
> / generate from internal noise). BUT the specific devices here are mostly Suite-only:
> the whole thing is built on the **Echo** device's internal **Noise** source —
> **Echo ✗ NOT in Live 12 Lite** — plus a **Resonator ✗ (Standard+)**, a **Max-for-Live
> LFO ✗ (Suite)**, and the "ten reverbs" stack (Reverb ✓ but Lite caps you at 8 tracks).
> Keep this video for the *idea*, not the literal recipe. **Lite translation of the
> concept:** Lite's stock devices that self-generate/feed back are **Reverb (with Freeze
> for an infinite tail)**, **Delay (high feedback → self-oscillation)**, **Erosion** and
> **Redux** (add noise/grit), and **Saturator**. Build the no-instrument drone from
> Reverb-Freeze → Delay feedback → Erosion noise → Auto Filter sweeps, then resample.

## Cleaned transcript (distilled — the source is loose/improvised)

The premise: **you can use Echo as a sound source** because it has a built-in **Noise** generator. Turn the noise up, add the **Morph** control for movement, and run that noise through the Echo itself — "ultra drone, power ambient, stratospheric, pan-dimensional ambient" with just effects, no instruments, never pressing play.

Steps as performed:
- Put a **Glue Compressor** on early "to be on the safe side." *(Lite: use stock Compressor.)*
- Drop tempo from 175 to ~120 BPM. Use the Echo's noise → delay path; modulate **delay time** very slowly (every 8 beats/bars).
- Add a **Max-for-Live LFO** mapped to a parameter for slow movement. *(Lite ✗.)*
- Add a **Resonator** to tune the random frequencies into something vaguely musical — tune the resonators to intervals: **+4 semis (major 3rd), +7 (perfect 5th), +10 (dominant 7th)**; raise the decay/time so harmonics ring out. *(Lite ✗ — Resonators is Standard+.)*
- Stack **multiple Reverbs** (he goes for "ten," decay ~3 s each, randomizing their sizes) to smear everything into space. *(Reverb ✓ but Lite's 8-track ceiling means do this with one Reverb + Freeze, or resample between stages.)*
- Put a **Limiter** somewhere safe at the end. Increase **Echo feedback** for different tones; bring the phasey noise in and out.
- Runs at ~22% CPU. The whole thing is "just effects" — tiny tweaks greatly affect everything because the signal is recirculating.

Takeaway for Lite: the *technique* — effects-only, self-oscillating ambient with no instrument and no transport — is the keeper. Re-create it with **Reverb Freeze + Delay feedback + Erosion/Redux noise + Auto Filter**, then resample the master back into a clip.
