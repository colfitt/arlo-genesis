https://help.uaudio.com/hc/en-us/articles/13621234251284-UAFX-Del-Verb-Ambience-Companion-Manual + MusicRadar/Delicious-Audio/Gear-forum
Distilled from official manual + reviews + forum confirmations · 2026-06

# Stacking & placement recipes (Del-Verb)

## Fixed internal order: DELAY → REVERB (not changeable)
- The pedal's signal flow is delay first, reverb after, internally (confirmed: "the delay is positioned before the reverb in the signal chain, which is a traditional approach"). You cannot reorder reverb-before-delay on the hardware. If you want reverb-into-delay smear, you'd need an external reverb in front and use only the Del-Verb's delay (or vice-versa) — the box itself is delay→reverb only.
- Each engine is a SEPARATE STEREO instance, so reverb processes the already-delayed signal in stereo for "three-dimensional stereo depth."

## Where it goes in a chain
- **End of chain** (its design intent): after drives/modulation, last before amp/PA/interface. It sees a summed, processed signal — source-agnostic. This is the rig's intended slot.
- **Amp FX loop / 4-cable:** because it's buffered with analog dry-through and silent switching, it sits happily in a series FX loop after preamp gain (time-based fx belong post-gain). UAFX users commonly run UAFX boxes "to a power amp, into an amp's fx loop, or directly to a PA." For a clean amp + Del-Verb-in-loop, that keeps the spring/plate/hall behind the amp's distortion instead of being smeared by it.
- **In front of a dirty amp:** delay/reverb in front of high gain = mush. Avoid unless you want lo-fi wash. The pedal's place is post-gain.

## Stacking with drives / fuzz (the rig's instruments)
- Drive/fuzz FIRST, Del-Verb LAST. For the doom/shoegaze rig: fuzz (Hizumitas / MXR 108 / Longsword / Brothers AM) → [texture] → Del-Verb at the end. The Del-Verb's reverb blooms on top of the fuzz wall rather than gating it.
- Internal trick instead of a separate drive: push **Analog DMM Color past noon** to bake overdrive into the repeats (saturated delay tails) without another pedal — useful for the dub/doom feedback patch.

## Stereo at the end of the chain
- Two TS outs → stereo amps / stereo DI / two interface inputs. Input 2 = stereo R in, Output 2 = stereo R out. Dual-mono mode (app) lets you run two separate mono paths if you don't want true stereo. Trails On for ambient spillover between sections.

## Parallel / aux (studio)
- Feed from an aux/parallel send, set Mix and/or Reverb fully CW (KILL DRY → 100% wet), return in stereo. Proper outboard-style send reverb; the dry stays untouched on the console/Apollo. (See tips file for kill-dry.)

## THE TRAVEL / FLY BOARD BUILD (the endorsed home for this pedal)
This is the Del-Verb's one genuine win in this rig. A complete carry-on ambient rig in a backpack:
- **Tuner** (Polytune 3) → **one drive/fuzz** → **Del-Verb** (end), into amp/PA/interface.
- Dossier-suggested single drive in front: **JHS Kilt v10** or **Chase Bliss Brothers AM** (both versatile, bench-able for travel). A real user's reported minimal board: "Del-Verb on a small board with a tuner, fuzz, filter, and a noise gate."
- The Del-Verb alone replaces a separate delay + reverb (or two Strymons), saving space/power. One ~400 mA box = legit spring/plate/hall + tape/BBD/digital delay, stereo.
- If you need preset-like recall on the road, add a USB-host MIDI controller (see midi-*.md) — but that adds a controller + passive USB hub and erodes the "one simple box" appeal. For a pure simplicity fly board, skip MIDI and pre-set one good voicing per engine in the app before you leave.

## Travel-board patch shortcuts (clock-face)
- Instant ambient: Hall 224 ~11–12; Precision delay, dotted-8th (CC-25 = 1), Feedback 9–10, Mix 9, Color noon, Mod off.
- Doom wall: Hall 224 1–2 o'clock; Analog DMM long time, Feedback 1–2 o'clock, Mix noon, Mod → Chorus, Color past noon for grit.
- Dub: Spring '65 ~9; Tape EP-III, Feedback edge-of-oscillation (~2–3 o'clock), Mix 11, Mod → Worn tape; ride/kill feedback by hand.

## Placement DON'Ts
- Don't put it on the FULL home board — it's redundant behind the H90 / Dark Star / QI (the bench verdict). Stacking value is travel-only or all-UA-studio-only.
- Don't run the runaway-oscillation patch into a quiet passage without a plan to drop Feedback (bypass won't kill it).
