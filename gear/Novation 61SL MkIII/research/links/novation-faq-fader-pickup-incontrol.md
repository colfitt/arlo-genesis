https://userguides.novationmusic.com/hc/en-gb/articles/25626782085266-SL-MkIII-Global-settings-menu
userguides.novationmusic.com · official Global-settings KB + DAW-control-using-InControl KB · current
(KB 403 WebFetch — distilled from search snippets quoting the official text + SOS review)

The fader-jump / pickup gotcha.

## Faders are NOT motorized or touch-sensitive
- So when a fader's physical position doesn't match the software value, moving it **jumps** the value ("destructive") unless a take-over mode catches it.
- Three take-over modes available for the non-motorized faders/encoders: **Absolute** (jump — default), **Pickup** (value only changes once you pass through the stored value), **Relative**.

## The InControl gotcha
- **Fader Pickup does NOT apply in InControl mode.** In InControl the SL inherits **HUI's / the DAW's** pickup behavior instead of its own. So you cannot rely on the SL's Pickup setting to tame jumps when driving Logic/Ableton via InControl — you're at the mercy of the DAW's surface behavior.

## Rig guidance
- For **standalone / template** control of the VG-800 and Chase Bliss / MIDI pedals, turn **Pickup ON** so a fader move doesn't slam a CC to a wild value mid-performance (a hard CC jump on, say, a Blooper or VG model level is exactly the kind of "destructive" move you don't want live).
- In **InControl (Logic/Ableton)**, set the DAW side to a pickup/relative behavior if it offers one, since the SL's own Pickup is bypassed.
