# Manual — Knob FX / Compressor / Sample-Edit Parameter Reference (authoritative ranges)

Source: **MPC Sample User Guide v1.3.0 (RevA)** — Akai Professional, on file at
`manuals/MPC Sample - User Guide - v1.3.pdf` (extracted with `pdftotext -layout`, June 2026).
This file pins the **exact parameter ranges** for the degrade/punch patches so the values
below aren't guessed — they're the literal knob ranges printed in the manual (pp. 24–56).

## Sample-edit pages (per pad/sample)
- **Mix** — Volume `-INF, -74.00 – +6.00 dB`; Kit Volume same range (Shift+K2); Pan `50L – C – 50R`.
- **Amp Env** — Attack `0–127`; Decay `0–127` (One Shot) / **Release `0–127`** (Note On);
  **Shift+K2 = Decay From → Start or End**; **Vel Sens `0–127`** (127 = most dynamic, 0 = always full velocity).
- **Tune** — Semi `-24 – 0 – +24`; Fine `-90 – 0 – +90 ¢`; **Warp `Off, 50–200%, Seq`**
  (Time Stretch = length/tempo only; Pitch = length + pitch, disables Semi/Fine; Seq = locks to sequence tempo);
  Shift+K3 = `# Beats`.
- **Play** — Polyphony `Mono / Poly`; **Mute Group `Off, 1–16`**; **Pad Link `Off, 1–16`** (Shift+K2 — fires a 2nd pad in the same bank simultaneously); **Offset `0–100%`** (delays sample start = old-school in-front-silence swing trick).
- **Filter** — Cutoff `0–127`; Reso `0–127`; **Type: Off, Classic, LPF2, LPF4, HPF2, HPF4, BPF2, BPF4**
  — **"Classic" is modeled on the MPC3000 drum-machine filter** (warmer as reso climbs).
- **Filt Env** — Attack/Decay(or Release)/Depth all `0–127`; Shift+K2 = Decay From Start/End.
- **Chop** — `K3 Chop Type: Threshold, Regions 4/8/16, Manual`; **Shift+K3 = Threshold `0–100%`
  (higher threshold = FEWER slices)**; Shift+K1/K2 = Zoom Start/End.
- **Loop Lock** (Shift+B1) — locks Loop Start to Sample Start; disengage to set them independently (drone-slice loops).
- **Reverse** (Shift + Chop button area) — reverse playback for the current pad/slice.
- **Resample** = **PAD 11** — auto-resamples all audio from the current sequence to a new pad (FX printed).

## Knob FX — relevant degrade/punch effects (exact ranges)
- **Transient** — Attack `-100 – +100%`, Shape `0–100%`, Sustain `-100 – +100%`.
  ⚠️ Correction to prior notes: the AC50 **does have a transient designer** (it's a Knob FX), so "no transient shaper" is wrong — it's just per-pad Knob FX, not a sample-edit page.
- **LoFi** — K1 Bitcrush `24.00 – 2.00`, K2 Decimator `0–100%`.
- **Vintage Emulator** — K1 Type only: `MPC3000, MPC60, SP1200, SP1200Ring` (no other knobs).
- **Vinyl Emulator** — Tone `0–100`, Crackle `0–100%`, Pitch `10–100%`.
- **Tape Emulator** — Wow `10–100%`, Noise `10–100%`, Pitch `20–100%`.
- **Color** (Pad-FX list, #11) — K1 Mode: `Cassette, Flutter, Tube Amp, Vinyl, Saturation, Radio`.
- **Tube Drive** — Drive `0–100%`, Headroom `-30.0 – 0.0 dB`, Saturation `0–100%`.
- **Soft Clipper** — Drive `1.0 – 10000.0%`, Shape `Tanh/Sine/Parabolic`, Mix `0–100%`, Shift+K3 Post Lvl `-Inf, -80.0 – 0.0 dB`.
- **Pumper** (sidechain-style) — Speed `Bar…1/32T`, Shape `0–100%`, Depth `0–100%`, Shift Attack/Hold/Release `0–100%`.
- **Granulator** — Density `1.0/s – 300.0/s`, Feedback `0–100%`, Grain Len `10.0 – 200.0 ms`.
- **Reverb Small/Med/Large** — Pre-Delay `0–250 ms`, **Time `0.4 – 71.5 s, +inf s`**, Mix `0–100%`,
  Shift ER/Tail `0–100%`, Density `0–100%`, Low Cut `1–1000 Hz` (the `+inf` = infinite drone tail).
- **Spring Reverb** — Pre-Delay `0–250 ms`, Time `1.0–10.0 s`, Mix, Width, Diffusion, Low Cut `20 Hz–1 kHz`.
- **Tape Delay** — Time `1…1/16`, Feedback `0–100`, Mix `0–100`, Shift Wow/Flut `0–100`, Ramp `0–100`, Spread `0–100`.

## Color-Compressor (Shift + Pad 5) — master glue
- B1 = **Color toggle** (parallel bass boost + minor pitch instability + harmonic saturation = "tape warmth").
- K1 **Attack `0.100 – 150 ms`**, K2 **Release `3.0 – 300 ms`**, K3 **Amount `0.00 – 100.00%`**.
- **Shift+K3 = In Boost** (drives the input harder = more aggressive, snaps transients).
- Makeup gain is auto-calculated.

These are the canonical ranges every patch below cites.
