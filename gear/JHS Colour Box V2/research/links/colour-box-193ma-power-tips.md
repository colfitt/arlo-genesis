https://www.guitarchalk.com/jhs-colour-box-v2-preamp-power-requirements/
guitarchalk.com · Bobby Kittleberger · 2025 (retrieved 2026-06-04, direct fetch 404'd; details corroborated via JHS product page + manual + Pixel Pro Audio + TalkBass search snippets)

# The 193 mA / 9V power gotcha — and how people actually solve it

The single most common real-world Colour Box V2 support question. The number is the headline: **9V DC center-negative ONLY, but it draws 193 mA.** That is enormous for a 9V pedal (most isolated supply ports are rated 100 mA), and it traps people migrating from the V1, which ran **18V**.

## The hard facts (cross-checked)
- **9V only — "DO NOT PLUG IN ANYTHING GREATER THAN 9V."** JHS's own product page states this verbatim. The V1 ran 18V; do NOT reuse a V1 18V supply on a V2 — you'll over-volt it. The V2 trades voltage for current.
- **193 mA draw.** Confirmed in the local JHS V2 manual. (Note: the JHS *web* product page omits the mA figure entirely — only the manual/3rd-party sources give 193 mA, which is why owners get caught out.)
- **Do not daisy-chain it.** 193 mA blows past what a daisy chain or a typical 100 mA isolated slot can deliver; an undersized slot browns it out (volume drop, noise, or no power).

## How owners solve it (community consensus from threads + supply maker docs)
1. **Use a single isolated output rated ≥193 mA** — i.e. a *high-current* port. Real boards people run it from:
   - **Strymon Zuma / Ojai** high-current (500 mA) outputs.
   - **CIOKS DC7 / CIOKS 8** high-current ports (multiple 9V@660 mA-capable outs).
   - **MXR Iso-Brick / Voodoo Lab Pedal Power** high-current outputs.
   - **Friedman Power Station** high-current slots.
2. **Dedicate the slot.** Because it eats ~200 mA, that port is gone for anything else — budget one whole high-current output to the Colour Box and nothing else.
3. **Pixel Pro Audio** and others sell a standalone 9V supply spec'd specifically for the Colour Box / V2 for people who just want a wall-wart that won't sag.

## Rig action item (Board 1)
The Colour Box is "always-on when able" and sits 4th, in front of the fuzz wall — so it must have a guaranteed clean 9V@≥193 mA slot of its own. Do not co-share its isolated output with the MXR 108 / Hizumitas. If it ever sounds weak, noisy, or dies, suspect an undersized power slot first.

Sources also drawn on: JHS product page (https://jhspedals.info/products/colour-box-v2), Pixel Pro Audio Colour Box supply (https://www.pixelproaudio.com/products/9v-power-supply-for-jhs-pedals-colour-box-colour-box-v1-colour-box-v2).
