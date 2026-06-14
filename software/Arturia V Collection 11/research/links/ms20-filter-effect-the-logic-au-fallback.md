https://cdm.link/2022/12/free-arturia-ms-20-filter-plugin/
CDM (Create Digital Music) · Peter Kirn · 2022-12 · (cross-ref: https://www.arturia.com/products/software-effects/filter-ms-20/overview)

The free **Filter MS-20** *effect* plugin — for this rig it's the clean, no-sidechain way to get MS-20 filter crunch onto the banjo/pedalboard *inside Logic* (insert it on an audio track; no instrument-sidechain headache).

== What it is ==
- Arturia's standalone recreation of the MS-20 filter, as an insert **effect** (not the instrument). Was free Dec 2022 → Jan 2; now ~$99. AU/VST/VST3/AAX + VCV Rack (so it loads fine in Logic as an AU insert).

== The filters ==
- Both MS-20 filters in series: **high-pass + low-pass, both resonant, both stereo.** One **Master Cutoff** knob sweeps both with visual feedback (or set them independently).
- **Limit Resonance** switch (ON by default) prevents self-oscillation. **Turn it OFF** to drive the filters into "screaming distortion and brutal self-oscillation" — go easy on output level.

== Distortion (modeled on the MS-20 ESP) ==
- Drive, Wet/Dry, High/Low cut, and crucially **Pre/Post routing** vs the filters — filter→distortion or distortion→filter. (= the "crunchy output" character, now in front of any source.)
- **Preamp modes:** Dirty (boost + saturate) or Clean.

== Modulation ==
- **Envelope Follower** (adjustable attack/release) — responds to the incoming signal → route to Master Cutoff for an auto-wah/self-playing filter on the banjo. (Arturia's own tip: ~800 Hz cutoff, 50% resonance, Envelope Follower → Master Cutoff = auto-wah.)
- **16-step Step Sequencer** (variable length, swing, multiple play modes) → rhythmic filter gating on a sustained source.
- **Function Generator** (preset or hand-drawn shapes) → slow LFO-style cutoff sweeps for evolving filtered washes.

== Why it matters here ==
Logic is AU-only and the MS-20 *instrument's* sidechain-input is unreliable in AU (see ms20-sidechain-daw-au-vst3-gotcha.md). This effect sidesteps that entirely: drop it on the banjo/baritone/pedalboard-reamp track, kill Limit Resonance, push Drive + Peak, ride the Envelope Follower → Cutoff, and you have the "screamed-through-an-analog-filter" treatment with zero routing fuss. Stack it before Decapitator/RC-20/Valhalla in the degrade chain. Free Filter MS-20 patch packs exist (e.g. SynthAnatomy "Filter Bites").
