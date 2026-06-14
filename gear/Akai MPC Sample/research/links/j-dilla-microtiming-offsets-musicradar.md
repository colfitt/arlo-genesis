# J Dilla micro-timing — concrete ms offsets (for hand-played AC50 swing)

URL: https://www.musicradar.com/artists/djs-producers/every-producer-bows-down-to-dilla-whether-they-like-it-or-not-how-j-dilla-and-his-mpc-changed-beatmaking-forever ·
https://gearspace.com/board/rap-hip-hop-engineering-and-production/864711-j-dilla-quot-swing-quot-his-beats.html
site · musicradar.com · gearspace.com · accessed June 2026

Supplements the existing `musicradar-j-dilla-mpc-technique.md` with the concrete ms figures.

## The numbers
- MusicRadar states the Dilla feel as **"a kick hits 30 ms early here, a snare drags by 20 ms there"**
  + irregular per-element swing, quantize off, played by hand on an MPC3000.
- ⚠️ **Direction is reported inconsistently across sources** — MusicRadar's flagship piece says
  *kick early / snare late*, while several others phrase it *kick late / snare early*. The
  load-bearing fact is the **magnitude (~20–30 ms) and the asymmetry**, not a fixed direction;
  the user should nudge by feel, not dogma.
- He used the MPC3000's **time-shift / nudge tool** to move individual notes by tiny increments
  rather than relying on the global swing setting.

## AC50 translation
- **Quantize OFF**, play by hand (the AC50 honors this — it's the whole point of the box).
- Use the **Step Edit** page: select an event, move the **FADER** up/down to nudge its timing
  forward/back (the AC50's equivalent of the time-shift tool) — apply asymmetric ~20–30 ms nudges
  to kick vs snare.
- Or use the **Offset** parameter (0–100% sample-start delay) to drag a specific pad late
  (the DIBIA$E "silence-in-front" trick already in this folder).
