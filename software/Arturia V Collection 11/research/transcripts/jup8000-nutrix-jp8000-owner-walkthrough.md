https://www.youtube.com/watch?v=Ct88V3UyQK4
Nu-Trix The Synth Guy · "Jup-8000V from @ArturiaOfficial *** finally a JP-8000 #plugin ***" · 2025-04-24

A 25-year synth-school teacher / 10-year real-JP-8000 owner walks through what's
special in Arturia's recreation. The single most authority-grounded source on this synth.
(Distilled to prose from auto-captions.)

## Why the JP-8000 matters
First commercially-sold virtual-analog synth from Roland (1997-ish), a hit in an era when
ROM-sample playback was mainstream. It did analog-expected things digitally, put all the
classic features into one box, AND added controls "that did not exist in the real analog
world." Famously "one-knob-job" — everything is on the panel, ready to go.

## OSC 1 = the special oscillator (the whole point)
OSC 1 and 2 both do traditional pulse / saw / triangle. But **OSC 1 has extra shapes
Roland designed to each behave like more than one oscillator**:
- **SUPERSAW** — the marquee. Where every other synth's "supersaw" traces back. Instead of
  switching the WHOLE synth into unison+detune (like you'd do on a Prophet-5 or Jupiter-8),
  the JP put **six/seven/eight detuned saws into ONE oscillator**. Workflow: default patch,
  you hear ONE saw; bring the **DETUNE** control up and you hear the other saws fanning out;
  it's "already massive with only one oscillator." (He stresses: at zero detune they're all
  the same pitch so it sounds thin — the detune is what creates the wall.) You can still
  ALSO bring in OSC 2 (e.g. its own saw) for even more.
- **FEEDBACK osc** — "the fun one if you like feedback-distortion guitar sound." It's a saw,
  but you need to bring the **feedback** up — feeding output back into the oscillator —
  then sweep the **harmonics** control for a very wide range of frequency/sound. (His
  highlight as the experimental/drone-leaning mode.)
- **TRIANGLE MOD** — a triangle with a **shape** variation control (like PWM but for a
  triangle — "not something you usually can change"). LFO it for constant evolving movement.
  Same shape-morph idea is available for the saw too.

## Replacing the original's "Motion Control" with Arturia modulators
The real JP-8000 had **Motion Control** — record knob/fader motion in real time, plays back
as you play. The plugin has no on-panel motion control; **instead you open the Advanced
window and assign a modulator (e.g. a slow Function generator) to a panel knob** — e.g. park
a slow Function on the feedback-osc HARMONICS so it drifts by itself. "This replaces the
original motion control." Any Arturia modulator can drive any panel knob/fader. (This IS the
universal evolving-pad trick, native here.) He also LFOs the square's pulse-width and the
triangle-mod shape for organic, never-static movement — "what makes analog sound organic is
it's never exactly the same place."

## SYNC / RING / CROSS-MOD + the pitch envelope
Key JP feature trio. The magic is pairing them with the dedicated **AD (attack-decay) PITCH
envelope**:
- **SYNC** — OSC 2 retriggers to OSC 1. Boring static, but route the AD pitch-env to OSC 2
  only and sync → classic "massive sync sweep."
- **RING** — similar setup, weirder/metallic.
- **CROSS-MOD** = "basically FM" — one osc modulates the other's pitch. Route the short AD
  pitch-env to cross-mod amount → an "aggressive nasty tone at the attack" with the filter
  fully open (it's the cross-mod, not the filter, making the bite).

## Filter / amp (standard)
LP / BP / HP, switchable **12 or 24 dB**; env + LFO + key-follow on cutoff. Amp: ADSR,
velocity, LFO (tremolo), **LFO-able PAN**. Plus a Tone section: bass + treble.

## Modern additions over the hardware
- Real **aftertouch** routing (the original's ribbon was half-aftertouch and weird; Advanced
  panel lets AT do "the right thing," e.g. → cutoff).
- **Multi-Arp = 4 arpeggiators** (way more powerful than the original's single arp).
- **On-panel FX**: Trance Gate, (Super) Unison, Chorus, Delay, Reverb — click a slot name to
  swap engine (Trance Gate→Super Unison→Chorus→Delay→Bitcrusher…), panel follows and you can
  reorder; full deep controls behind each. Wider/deeper than the hardware's FX.
- **Polyphony to 12 / 16** (hardware was 8) — "CPU goes with that."

## Honest gotcha
- **No split/layer mode.** The real JP-8000 could reserve voices (e.g. 2 bass + 6 lead split).
  The plugin is single-timbral — "doesn't have a split." Workaround: load two instances and
  split on the keyboard / in the DAW.
