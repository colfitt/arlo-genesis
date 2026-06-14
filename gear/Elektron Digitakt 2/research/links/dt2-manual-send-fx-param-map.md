Digitakt-2-User-Manual_ENG_OS1.15A_250708.pdf (§12 FX & Mixer, pp.61–63; §11 p.58; §11.9 p.58)
elektron.se · Elektron official manual (OS 1.15A) · 2025-07-08

# DT2 — Send-FX (Delay / Reverb / Chorus) PARAMETER MAP + per-track FX page

The authoritative knob list for the three send FX and the per-track FX page, so the
ambient/dub send recipes (EZBOT delay≈88 / reverb≈90, Amiva all-wet, DROWNED Supervoid)
can be set against the real parameter names. Send FX are PATTERN-level (one setting shared by
all tracks); each track has its own SEND levels. Edit send-FX via **[FUNC]+[FX]** (FX page 2).

## Per-track FX page ([FX], §11.8)
- **BR** — Bit Reduction, range **16 bits → 1 bit**.
- **OVER** — Overdrive gain into the digital overdrive.
- **SRR** — Sample-Rate Reduction amount.
- **ROUT** — SRR routing **PRE / POST** filter.
- **OD.RT** — Overdrive routing **PRE / POST** filter machine.
- **DEL / REV / CHR** — the three SEND levels (to Delay / Reverb / Chorus).

## DELAY (send FX page 1, [FUNC]+[FX])
- **TIME** — relative to BPM, in 128th notes, **1.00–128.00** (table maps to 1/128 … 1/4;
  so common musical values: 32.00≈1/8, 48.00≈dotted-1/8, 64.00≈1/4).
- **X** — Ping-pong: **OFF** (manual pan via WID) / **ON** (auto L↔R, WID = amount).
- **WID** — Stereo Width, bipolar.
- **FDBK** — Feedback Gain; high = "infinite and/or swelling delays" (can get very loud).
- **VOL** — Delay output volume (set with LEVEL/DATA).
- **HPF / LPF** — delay's own high-/low-pass (the EZBOT "top filtered" move = lower LPF).
- **REV** — Reverb Send (how much delay output feeds the reverb; range 0.00–127.00).

## REVERB (send FX page 2)
- **PRE** — Pre-delay time.
- **DEC** — Decay Time (= size of the space; high/max ≈ the "INF"/freeze swell).
- **FREQ** — FB Shelving Freq (with GAIN, damps the tail above that frequency).
- **GAIN** — FB Shelving Gain (max = bright tail; lower = darker, more muffled tail).
- **VOL** — Reverb output volume.
- **HPF / LPF** — pre-reverb input filters (carve mud out of the wash here).

## CHORUS (send FX page 3)
- **DPTH** — chorus LFO modulation depth.
- **SPD** — chorus LFO speed.
- **HPF** — high-pass on the chorus input.
- **WDTH** — chorus stereo width.
- **VOL** — chorus output volume.
- **DEL / REV** — send the WET chorus on to Delay / Reverb.
  ⚠️ Sending chorus → reverb collapses the chorus to MONO (flange-y/phase-y) — keep chorus
  and reverb in PARALLEL for wide ambient (matches the existing send-FX gotcha file).

## Anchored ambient send recipe (EZBOT values, now param-named)
- **Delay:** X = ON (ping-pong), WID hard, **track DEL send ≈ 88**, REV (delay→reverb) a
  touch, LPF lowered ("top filtered").
- **Reverb:** **track REV send ≈ 90**, DEC long, HPF/LPF to taste, GAIN lower for a darker
  drone tail.
- **Tempo ≈ 80 BPM.** TIP (EZBOT): hold **[FUNC] + press an encoder** to read the exact
  numeric value in the secondary FX menus.

NOTE: ranges/param names are manual-verbatim; the 88/90/80 send+tempo figures are EZBOT's
(already in the ezbot recipe file) — captured here mapped onto the correct knob names so a
patch can be entered directly.
