https://uadforum.com/general-discussion/37271-reamping-my-radial-x-amp-apollo-twin.html
UAD Forum · community thread · "Reamping with my Radial X-amp and Apollo Twin?"
(also: https://uadforum.com/apollo-arrow-interfaces/30301-reamping-apollo-twin-radial-x-amp-need-di-box.html — "Reamping Apollo Twin to Radial X-Amp: Need for DI box?")

(Distilled from search-surfaced content; uadforum.com blocks direct fetch. Real-world reamp signal-flow advice from Apollo + Radial X-Amp users.)

DO YOU NEED A DI BOX BETWEEN APOLLO AND X-AMP? No. The X-Amp is balanced line level, and so is the Apollo's line output — so you do NOT need a separate DI/level box between the Apollo and the X-Amp. Send a spare Apollo line output straight into the X-Amp, which converts line → instrument level for the amp/pedal front end. (A DI box is for the reverse direction — instrument → line.)

ROUTING:
- Use a spare line output (Line Out 3 on a Twin; the x8 has 3–8 free) for the dry-DI send, connected to the X-Amp via balanced TRS or XLR.
- Critically: do NOT assign the reamped RECORD track's output to the same Line Out 3 as the dry-send track — that creates a feedback loop. The record track outputs to the main monitor bus; the dry-send track outputs to the spare line out.

LATENCY / SAMPLE ALIGNMENT (the key gotcha):
- The reamp loop incurs round-trip latency (DAW → D/A → X-Amp → amp → mic → A/D → DAW), so the reamped take lands LATE versus the original.
- Method to fix: reamp the DRY DI back into a DI input first to measure exactly how many samples to compensate, then nudge the reamped track back by that offset. One user set the buffer to 64 samples and found alignment "pretty much spot on."

FEEDBACK / BLEED:
- If the amp is in the same room, turn down the monitors and switch to HEADPHONES while recording the reamp pass — prevents feedback and mic bleed.

LEVELS:
- Push the dry-DI send as hot as possible without clipping for best reamp signal-to-noise (matches the Radial Reamp Academy advice).
