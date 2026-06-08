https://jhspedals.info/products/colour-box-v2
jhspedals.info + JHS V2 manual + Tape Op · JHS / engineers · 2025 (retrieved 2026-06-04)

# The I/O gotchas: "stereo" myth, wrong-input silence, XLR-off-when-bypassed

These are the recurring "why isn't it working / why isn't it stereo" support questions. None are defects — all are documented behavior.

## 1. The STEREO MYTH (people get this wrong constantly)
The Colour Box V2 has **two outputs (1/4" + XLR)** and many owners — and this rig's own metadata — assume that means stereo. **It does not. It is a MONO device.** The two outputs are **parallel mono**: the *same* mono signal sent to two destinations at once (e.g. 1/4" → amp + XLR → FOH, or amp-track + DI-track). It splits; it does not pan. JHS's own product page and manual list it mono in / mono out. There is no stereo image, no L/R. (Action item: the GearProfile's `io: stereo-in/stereo-out` is WRONG and should be fixed.)

## 2. Wrong-input SILENCE
There's an **INST / XLR** input-select switch. If it's set to the input you're NOT using, **no signal passes at all** — dead silence. This is the #1 "my pedal is broken" panic. Always check the side switch first.

## 3. XLR out is OFF when the pedal is bypassed
The **XLR output only passes signal when the pedal is ON.** If you feed FOH or your interface off the XLR and then bypass/kill the Colour Box, you kill that feed. For an "always-on" board this is fine, but plan around it — don't stomp it off mid-set if FOH is hanging off the XLR. (The 1/4" out passes effected-when-on, and clean-bypass-when-off in INST mode.)

## 4. The 20 dB PAD is XLR-only
The PAD attenuates the **XLR input only** — it does nothing on the 1/4"/INST input. Use it when a hot line-level or mic source clips the front end. Works whether the pedal is on or off.

## 5. Loud volume jumps are normal
Because PRE-VOL sets both gain and level, every gain change bumps output — trim MASTER each time. Not a fault; build the muscle memory.

## Rig relevance
On Board 1 the Colour Box runs as a *mono* front-end into the mono fuzz chain (no stereo to lose). The live gotcha that matters: if the XLR ever feeds a DI/print path, remember it dies when the pedal is bypassed — keep it always-on, which the rig already does.
