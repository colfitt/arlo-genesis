https://www.strymon.net/faq/clipping-or-distorted-audio-from-bigsky-plug-in/  (+ Fractal & Gearspace owner threads, SOS forum)
strymon.net / forum.fractalaudio.com / gearspace.com / soundonsound.com forum · multiple · retrieved 2026-06-03

# Input level / clipping — the line-level gotcha (DIRECTLY relevant to VG-800 feed)

This is the single most rig-relevant community gotcha: the Big Sky can be **overdriven on its input** by hot line-level sources, which is exactly the VG-800 → (EHX FXI) → Big Sky concern.

## The problem
- Max input level is **+8 dBu**. Many synths/modelers output true line level (+4 dBu nominal, peaking higher), and a hot send **clips the Big Sky's input** → distorted/crunchy reverb even though the pedal "accepts line level."
- Community quote (paraphrased from owner threads): *"all my synths were too hot for it at anything over half output volume."*
- Fractal forum (effects-loop clipping thread): putting the Big Sky in a hot **+4 dBu effects loop** clips it; the loop send level has to be dropped.

## Fixes the community uses
1. **Turn the source down.** Drop the VG-800 / synth output until the Big Sky stops clipping (often below ~50% on hot synths).
2. **Passive attenuator / pad** between source and Big Sky to bring +4 dBu line level down toward instrument level.
3. **Run line-level sources through a mixer** and set the send level so the Big Sky sees a clean signal (Strymon's own recommendation for "true line levels").
4. Note: the **plug-in** has an explicit INPUT level control; the **hardware does not** — on hardware you must attenuate upstream. (Don't conflate the two.)

## Rig action item
Gain-stage the VG-800 (and anything feeding the Big Sky if it ever subs in) so peaks stay under +8 dBu. If the Big Sky ever sounds gritty on synth/modeled sources and you didn't ask for grit, the input is too hot — attenuate before the pedal, the Big Sky has no input trim on the hardware.
