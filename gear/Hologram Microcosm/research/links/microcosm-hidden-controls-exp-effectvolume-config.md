https://www.hologramelectronics.com/pages/microcosm-manual
hologramelectronics.com (manual) + community-surfaced tips (Delicious Audio, castiron-seasoning manual guide, Elektronauts) · accessed 2026-06

# Hidden / easily-missed controls: effect volume, EXP auto-assign, global config entry

A consolidated list of the Microcosm behaviors that aren't obvious from the front panel and that the community most often re-discovers.

## "Effect Volume" — the hidden output level (the level-match fix)
- **Hold Shift + turn MIX** → adjusts the **Effect Volume** (master output level of the wet effects), independent of the dry/wet MIX balance. Fully CW = effect volume max. (MIDI: **CC 16**.)
- Why it matters here: a hot **fuzz wall feeding in** can overdrive the granular engine and make the output jump in level when engaged. Effect Volume is the dedicated trim to **level-match the Microcosm's wet output to the dry/bypass level** — set it once so engaging the pedal doesn't cause a volume jump on the board.

## Expression-pedal auto-assign GOTCHA (the "no sound" trap)
- If an expression pedal is **plugged into EXP IN when the Microcosm powers on**, the pedal **auto-assigns EXP to the FILTER** and parks it at the **heel-down = filter fully closed** position. Result: **no wet signal appears to come through** and people think the pedal is broken.
- Fix: rock the EXP pedal toe-down (opens the filter), or re-assign EXP to a different parameter in Global Config. EXP assignment **persists across power cycles**, so this can bite again on next power-up if left on Filter.
- EXP IN can be assigned to: **Activity, Shape, Filter, Mix, Repeats, Space, or Loop Level** (0–3 V input, pot >10 kΩ).

## Entering Global Configuration
- **Hold Shift (selector/TIME) + Phrase Looper footswitch for ~2 s** → LEDs start blinking = you're in Global Config. Then specific knobs change specific global settings (e.g. **Filter knob = MIDI clock config**; selector positions 1–4 choose clock/echo behavior). Exit by hitting the on/off (bypass) footswitch.
- Global Config holds: **Mono/Stereo input** (defaults MONO — must switch to STEREO for this rig), **bypass mode** (True / Buffered / Buffered+Trails), **Hold = momentary vs toggle**, MIDI channel/clock, EXP assignment. **Global Config settings are NOT saved per preset.**

## Reverb-mode + secondary-control quick reference
- **Shift + Space** = pick reverb mode (Bright Room / Dark Medium / Large Hall / Ambient).
- **Shift + Filter** = filter resonance. **Shift + Repeats** = pitch-mod depth. **Shift + Shape** = pitch-mod rate. **Shift + Loop Level** = loop fade time.
