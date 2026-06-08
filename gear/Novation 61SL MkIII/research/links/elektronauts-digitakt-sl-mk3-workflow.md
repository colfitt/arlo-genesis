https://www.elektronauts.com/t/digitakt-sl-mk3-workflow-question/129020
elektronauts.com · "Digitakt + SL MK3 workflow question?" · 2020, posters: hausland, christd91

Direct rig-relevant thread: playing/sequencing a Digitakt (and downstream synths) from the SL MkIII keybed. Concrete content:

## Recommended physical MIDI chain
- "Keyboard MIDI OUT into Digitakt MIDI IN. Digitakt MIDI OUT into first synth MIDI IN." — daisy-chain through the Digitakt, then onward to each synth's MIDI IN.

## MIDI channel assignment (hausland, Apr 2020)
- Digitakt's MIDI tracks each need their own **inbound** channel AND a matching **outbound** channel to the target synth.
- On the SL you select which MIDI channel a Part/Zone transmits on to address a specific synth via the Digitakt's thru/routing.

## GOTCHA — Digitakt does NOT pass pitch-bend or mod-wheel through
- hausland: "The Digitakt will pass through all MIDI messages from your keyboard EXCEPT pitchbend and modulate (mod wheel)… that's a really dumb limitation." Confirmed no workaround in-thread.
- **Rig implication:** if you want pitch-bend / mod-wheel (or aftertouch→CC) to reach a synth, do NOT route it *through* the Digitakt. Send that Part out the SL's **second DIN (Out2)** directly to the synth, or via USB, and reserve the Digitakt chain for note/CC traffic it will relay. This matters for expressive soft-synth-style playing of any box sitting behind the Digitakt.

## Polyphony ceiling
- "the Digitakt (or any other Elektron sequencer for that matter) can sequence max **4 notes per step**." If you play big chords from the SL into a Digitakt MIDI track, notes beyond 4 per step are dropped.

## Avoiding double-sequencing
- christd91 uses the SL's **InControl** toggle to switch between Ableton control and Digitakt MIDI sequencing so the two sequencers don't fight. Confirms the dossier guidance: pick one master sequencer per song.

Clock-master / transport-sync specifics were not resolved in this thread.
