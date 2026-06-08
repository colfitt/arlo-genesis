https://www.mpc-forums.com/viewtopic.php?f=50&t=220503
mpc-forums.com (MPC Sample subforum) · NearTao (Expert Member) · Apr 10, 2026

AC50-SPECIFIC. Hands-on findings from a power user (NearTao) who loaded the MPC Sample firmware 1.3.0 beta early. This is the on-device "where the new features actually live" report that the press articles don't give in button-combo detail.

## What firmware 1.3.0 actually adds (NearTao, on-device)
NearTao (disclaimer: "install at your own risk", it was a beta drop):

1. **Normalize** — "Normalize is available as SHIFT in the TRIM/MIX/AMP envelope page... it's handy." So you NORMALIZE a sample to 0 dB (between its current start/end points) via **SHIFT in the Trim / Mix / Amp-envelope screen**, not a separate menu. Good for levelling chops/break slices before sequencing without manual gain staging.

2. **New AMP/FILTER envelope "release start" setting** — "AMP/FILTER envelopes have a new SHIFT release start setting... so you can set where release starts from." A genuinely new modulation control (the AC50 is otherwise envelope-poor — no LFOs), letting you set the point the release stage begins. Useful for shaping sustained drone slices.

3. **Knob / Q-Link takeover behavior** — "MIDI CONFIG (SHIFT+PAD8) settings to adjust knob/q-link behavior." This is the fix for the AC50's biggest early complaint (absolute-position knobs/fader jumping when you switch banks/patches). Set it under **SHIFT + PAD 8 (MIDI Config)**.

## The three knob-takeover modes (cross-confirmed by press — kansamples.com, CDM, gearnews)
Settable INDEPENDENTLY for three control groups: **Standard controls, Knob FX, and the Fader**.
- **Pickup** — the knob does nothing until its physical position matches the stored software value, then takes over smoothly (this was the ONLY behavior before 1.3, and the source of the "knobs feel coarse / can't hit precise points" complaint). Safest, no jumps.
- **Scaled** — the parameter moves in the same direction as the hardware control at a scaled rate until position catches up to value (smooth, no dead zone, no jump).
- **Instant** — the value jumps immediately to the knob's physical position the moment you touch it (most responsive, but jumps).
- PRACTICAL: for hands-on tweaking/performance on the AC50, set **Scaled** or **Instant**; keep **Pickup** if you hate accidental jumps. Set per-group so e.g. the Fader can be Instant while Standard knobs stay Pickup.

## NearTao's verdict
"it's not a *huge* update by any means" — mostly QoL. He flagged there might be undocumented bug fixes/hidden features he couldn't find.

## Firmware-version timeline (from CDM cdm.link/mpc-sample-updates and press, for context)
- **1.2.0 / 1.2.1** added: SD Card Access (Project > SD Card Access — mount the card over USB without ejecting it), Export Song to Sequence, and **per-pad Loop Lock** ("locks the loop to the start position, per pad" — in SAMPLE > TRIM), plus saving/disk-streaming fixes.
- **1.3.0** (released ~Apr 13, 2026 GA; beta circulated ~Apr 10): Normalize, three Knob Takeover modes, AMP/FILTER release-start, bug fixes.
- Updates have shipped fast — CDM noted Akai was iterating heavily on "workflow stuff" within weeks of launch. Expect more.
