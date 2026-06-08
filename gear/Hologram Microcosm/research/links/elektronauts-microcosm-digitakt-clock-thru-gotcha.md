https://www.elektronauts.com/t/digitakt-micromonsta2-hologram-microcosm-clock-issue/193212
elektronauts.com · thread by "sweevo" (replies from community) · 2023-04-29

# Microcosm not receiving Digitakt MIDI clock — the THRU gotcha

The single most relevant community thread for THIS rig (Digitakt is the clock master). A user chained Digitakt MIDI OUT → Micromonsta2, then tried to feed the Microcosm from the Micromonsta's **MIDI THRU** port and the Microcosm would not pick up the Digitakt clock — even though it synced fine when fed *directly* from the Digitakt's MIDI OUT.

Key clarification from the thread:
- **"Thru does not send midi, only passes along messages from other devices."** A device's MIDI THRU port re-transmits what arrives at that device's *own* MIDI IN. If the Micromonsta is generating/merging, its THRU is not a guaranteed clean copy of the Digitakt clock. The fix is to put the Microcosm earlier in the chain or feed clock from a true OUT/THRU that carries the Digitakt's clock.
- Recommended re-route: **Digitakt OUT → Microcosm IN → (Microcosm OUT/THRU) → Micromonsta**, OR use a dedicated **MIDI hub/splitter** so every device gets the Digitakt clock directly.
- Channel note from the manual cited in-thread: the Microcosm **listens on Ch 1 by default**, and "other devices connected via midi out/thru should be configured to listen on another channel" to avoid PC/CC collisions.

## Direct relevance to the rig
The Microcosm **echoes everything arriving at its MIDI IN out of its MIDI OUT by default** (confirmed in Hologram's MIDI docs), so the cleanest topology is to put the Microcosm directly downstream of the Digitakt and daisy-chain other clock slaves off the Microcosm's MIDI OUT — rather than relying on an intermediate synth's THRU. For the Digitakt specifically, make sure the Digitakt is set to **send Clock** (MIDI SYNC → Clock Send = On) and **send Transport (Start/Stop)** — the Microcosm only switches from internal to external clock when it receives a MIDI **Start** message.
