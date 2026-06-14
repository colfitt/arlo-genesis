https://www.youtube.com/watch?v=pNHC84P5zHU
Onesto · "How To Make Ambient Pads - Sound Design Tutorial" · ~13 min

Not Kontakt-specific but the core "any sound → pad" recipe, fully applicable to a
sampled banjo/field-recording inside Kontakt or printed into Logic. The headline
move: feed a short source into a HUGE reverb and PRINT the tail as a new sample.

## The print-the-reverb-tail technique (the core move)
1. Take any source — a synth pluck, a vocal sample, a banjo note, a field
   recording. (He shows Serum plucked-string + arpeggiator on RANDOM to add
   texture/movement; arpeggiators "create movement in the pad itself.")
2. Send it through a **huge reverb** — FabFilter Pro-R, preset "Huge Sentence
   Space," **~20-second reverb tail**. The long ambiguous tail IS the pad texture.
3. **Print it:** route a "pad generator" track (source + reverb) into a "pad
   receiver" track. Hold one note in the song's key (he holds a D), record/bounce
   the wet output. Let it trail off, delete the MIDI, **trim to length with a
   fade-out**. → You've made a pad sample.
4. Repeat per chord — a vocal sample trimmed before its note changes, +reverb,
   becomes another pad. Each printed at a different root note.

## Stitching pads into a chord progression
- He builds the progression (D / Bm / G) out of these printed pads, one pad per
  chord, **layered/stitched together** rather than played live — "that's more
  interesting than just putting reverb on something."
- A **bass synth** underpins the pads and "guides what key the pads play in."

## Layering / cleanup so stacked pads don't muddy
- Each layer gets its own **frequency territory** via EQ/filter:
  - **High-pass out the lows** (steep slope) since the bass owns the low end.
  - Find the "best part of the sound" and gently boost there.
  - **Hunt resonance peaks** that the heavy reverb created: sweep a narrow band
    (**Q between 6 and 10**), find the nasty ringing, cut "until you don't hear
    it." (Long reverb on a sample builds ugly resonances — clean them.)

## Make boring pads interesting (saturation + glitch)
- **Output Thermal** (distortion/saturation) to brighten/energize a dull pad —
  browse presets ("Wild Harmonics" worked).
- **Output Portal** (granular FX) on another pad for motion/glitch ("Scattergate"
  preset).

## The 20-minute practice drill
- Make a chord progression on a bass synth. Set a 20-min timer. First 10 min:
  make pads from many different sounds/samples/synths to follow the chords. Rest:
  layer them + add FX. Then reflect: what made it "less static and boring"?

### Takeaway for the rig
Print-the-tail is the fastest "recorded-wrong wall" generator: banjo/pedal-tail
note → giant reverb (Valhalla/Space Designer) → bounce the 20s tail → that
bounced wav becomes a Kontakt pad sample (loop it, stretch it, modulate it).
Stack a few at different roots for an instant chord-bed; EQ each into its own
band; Thermal/Portal (or Decapitator/RC-20) to dirty them up.
