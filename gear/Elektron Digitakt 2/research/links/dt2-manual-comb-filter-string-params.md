Digitakt-2-User-Manual_ENG_OS1.15A_250708.pdf (Appendix A, pp.105–108) + elektronauts.com/t/222328
elektron.se · Elektron official manual (OS 1.15A) · 2025-07-08

# DT2 — Comb+ / Comb− filter PARAMETER MAP for plucked-string / banjo resonator

Anchors the long-standing "Comb filter = strings but nobody posted the numbers" gap with the
**authoritative parameter list straight from the OS 1.15A manual**, so the banjo-resonator
recipe can be dialed against real knobs. (The community thread t/222328 confirmed the
technique but had no numeric preset — see that file. This one supplies the param names +
ranges that the recipe plugs into.)

## Manual facts (verbatim, condensed)
- **Comb+ has POSITIVE feedback → "string-like" sound.** (Use this for banjo/harp/strings.)
- **Comb− has NEGATIVE feedback → "more hollow, tube-like" sound.** (Use for hollow/clavi.)
- Both are "metallic sounding, pitch-tuned, resonant overtones."
- **Comb+ / Comb− parameter set (8 knobs):**
  - **ATK / DEC / SUS / REL** — filter envelope ADSR.
  - **FREQ** — "sets the resonant frequencies of the comb filter" (this is the perceived pitch).
  - **FDBK** — "sets the gain of the feedback signal." Manual warning on Comb+: **"setting
    FDBK to a high value can create a very loud sound."** → more FDBK = longer ring / more
    sustained "string."
  - **LPF** — "low-pass filter in the feedback signal." Lower LPF = darker, less zingy string
    (plucky→stringy tone control lives here, per Dave Mech's OS 1.10 note).
  - **ENV** — Env. Depth, bipolar (±) cutoff modulation from the filter envelope.
- **Key tracking** lives on the **filter page 2** dedicated Keytrack param (every filter can
  be aligned to note pitch); set it so **FREQ tracks the keyboard** and the comb plays in
  tune across the trig keys. (LyingDalai, t/222328: "every filter can be aligned on note
  pitch through the dedicated Keytrack parameter.")

## Banjo / plucked-string starting patch (param-anchored, dial by ear)
- **FLTR machine = Comb+.**
- **Source** = a short excitation: a click/noise burst one-shot, OR a real banjo pluck.
- **FREQ** = to taste (or let Keytrack set it from the played note).
- **Keytrack ON** (filter page 2) at high depth so it tracks the 12-tone scale.
- **FDBK** = mid for a defined pluck; **high (carefully — loud)** for a sustained bowed drone.
- **LPF** in the feedback = plucky↔stringy tone (open = zingy banjo, lower = mellow).
- **AMP/filter env**: short ATK + medium DEC for a pluck; **DEC/REL long or AMP DECAY=INF**
  for a sustained metallic drone.
- **ENV (Env Depth)** small + a slow LFO → FREQ for a detuning, breathing resonator.

NOTE: ADSR/FDBK/FREQ integers are NOT published by anyone — these are the manual-correct
param NAMES + their documented behavior, so the dial-by-ear recipe is now grounded. Comb+
is DT2-only (OG Digitakt has no comb). Confirmed: Comb+ = string (positive FB),
Comb− = tube (negative FB).
