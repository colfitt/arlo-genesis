https://www.electrosmash.com/fuzz-face
electrosmash.com · ElectroSmash (tech circuit analysis) · n.d. (page currently SUSPENDED/down — content below is from a web-search snapshot of the indexed page, 2026-06)

NOTE: Page was account-suspended at fetch time. Distilled from search-engine snapshot of the canonical ElectroSmash Fuzz Face Analysis; treat the verbatim quotes as snapshot-sourced, not freshly re-fetched.

THE BUFFER PROBLEM — WHY A FUZZ FACE HATES A BUFFER IN FRONT (the rig-critical mechanism)
- "The classic Fuzz Face has a relatively low input impedance that loads the pickups, absorbs energy and dampens the pickup's resonant peak." That LOADING is part of the sound, not a bug.
- "The Fuzz Face low input impedance will load the guitar pickups. This is the reason why they do not respond well when they are placed after other pedals. A practical advice is to put your Fuzz Face first on the pedal chain, just after the guitar."
- The FF input has essentially no series input resistor: "There is no resistor in series with the audio input that would otherwise reduce the gain, except when connected directly to a guitar pickup, where the combined resistance and impedance of the pickup will reduce the gain, and prevent the fuzz from going bonkers."
- THE FAILURE MODE WITH A BUFFER: "If you drive the fuzz with a buffer, the output resistance/impedance of the buffer is very low so the result is that the fuzz circuit runs at MAX GAIN with oscillations and other mayhem often as the result."
  -> i.e. a buffer in front = fuzz pinned at full gain, harsh/oscillating/thin. The pickup's own impedance is the thing that normally TAMES the gain. (Germanium especially: "the germanium transistor needs to see the inductance/impedance from the guitar pickups. If they see a buffer at the input, they tend to sound awful.")

VOLUME-KNOB CLEANUP MECHANISM
- The guitar volume pot cleanup is an interaction between the pot and the fuzz's low input Z: an "unaltered guitar's volume pot is heavily loaded with the fuzz face's low impedance, which is akin to an overly exaggerated log pot behavior" — that exaggerated taper is WHY a small roll-off cleans up so dramatically.
- Buffering does NOT fully kill cleanup, it DECOUPLES the pot: "it does not lose that characteristic when you use a buffer, just the rotational angle that does the same thing increases. The action of the guitar's volume pot does change dramatically back to normal, because the latter is now decoupled from the fuzz face." -> With a buffer in front, the pot behaves like a normal volume control instead of a fuzz/clean morph.

RIG TAKEAWAY (M173 in Pedalxly, 5th, behind Colour Box buffer + VG-800 modeled line):
- The whole "max gain / mayhem" risk is exactly what a buffer in front provokes; the M173's onboard BUFFER switch is essentially a clean input buffer that DEFINES a known high input Z (800k) so the fuzz no longer sees the Colour Box's low output Z directly into the raw transistor input. That's why buffer ON tames the thin/gated misbehavior here.
- The classic guitar-volume cleanup is impedance-driven; through the GK -> VG-800 -> Colour Box chain there is no passive pot loading the fuzz, so the magic taper is gone (only a real passive guitar in front would restore it).
