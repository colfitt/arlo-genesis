https://valhalladsp.com/2019/06/13/valhalladelay-the-diffusion-section/
valhalladsp.com · Sean Costello · official "The Diffusion Section"

The single most important section for using ValhallaDelay as an ambient wall-maker. The
Diffusion network is what turns a delay into a reverb — Costello's co-designer Don Gunn
said they kept it because "we liked the reverbs we could make in ValhallaDelay more than
most of our usual suspects."

## Two controls
- **Amount** — diffusor coefficients (sets decay length + attack):
  - **0%** = diffusion bypassed (saves CPU; pure delay).
  - **68%** = "the diffusion attack is the exact length as the decay" = a reverb with a
    natural fade (works on its own).
  - **91%** = a "**pure diffusion reverb that doesn't rely on FEEDBACK for its decay**" —
    i.e. you get a full reverb wash WITHOUT cranking feedback (safer than runaway feedback
    for an infinite-ish wall).
- **Size** — diffusion network length as a % of the delay length. **Small = blurs the
  attack but still sounds like a delay; Large = transforms the delay into a reverberant
  sound.** 100% = network exactly the displayed delay length.

## Design notes
- Hardwired modulation depth (scaled by Size) prevents pitch artifacts.
- The network "can span 20 seconds of delay space without sounding sparse or grainy" →
  huge, smooth reverb textures from a delay plugin. The dial goes from slight smear → full
  ethereal reverb on one knob.

## Takeaway recipe (for this rig)
**Delay → reverb wash:** set DIFF Amount **91%** + DIFF Size large + a long delay time =
a dense reverb you can build without dangerous feedback. Combine with a Ghost/Pitch mode
to get a *pitched/spectral* reverb wash. This is the core reason to own Delay over a plain
delay for the ambient aesthetic.
