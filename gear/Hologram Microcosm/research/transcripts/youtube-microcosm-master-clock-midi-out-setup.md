https://www.youtube.com/watch?v=9M1ysTqGGK0
YouTube · "Easy How to Set Up Master Clock to Sync Hologram Microcosm & Other MIDI Effects" · auto-caption transcript, distilled to prose

# Microcosm as MIDI CLOCK MASTER — exact global-config steps (and the inverse for slaving)

The most useful clip for the rig's MIDI-clock question. The creator uses the **Microcosm as the master clock** to tap-sync a chain of pedals (Chase Bliss Habit + Mood, Meris LVX, Strymon Volante). For THIS rig the Digitakt is the intended master, but the **exact button sequence to enable the Microcosm's clock OUT** is identical to what you need to know, and the slaving notes apply directly.

## Confirmed: the Microcosm DOES transmit MIDI clock out
"The microcosm does actually send out midi clock if you set it up that way." MIDI is fully separate from the audio path — "the midi signal has no effect on the audio path."

## EXACT steps to turn on the Microcosm's MIDI clock OUT
1. Enter Global Configuration: **hold the Shift selector + the Phrase Looper footswitch for ~2 seconds** — "everything starts dancing and blinking."
2. **Turn the FILTER knob** — this selects the MIDI clock/echo configuration.
3. Use the **selector switch to pick option 1, 2, 3, or 4.** For **clock-out**, use **position 1 or 3.** The presenter uses **1** because "it still sends any other midi controls coming into it back out" (i.e. position 1 = clock out + echo/THRU of incoming MIDI).
4. **Press the selector switch again** to confirm — it blinks, then stays solid **white** = clock-out armed.
5. **Hit the on/off (bypass) footswitch** to exit Global Config.

## Adjusting the transmitted tempo
- The **TIME knob adjusts the BPM/tempo being sent** — handy so you don't have to tap-tempo while setting up. (When the Microcosm is a slave instead, Tap is disabled and Time is overridden by incoming clock.)

## Routing the clock to a chain (splitter pattern)
- Microcosm MIDI OUT → a **MIDI splitter/box** (he uses a Disaster Area Designs MIDI Box 4) → fans out to each slave; the box's THRU continues the chain (e.g. into a Meris LVX IN, whose OUT-set-to-THRU then feeds the next pedal's IN).
- **Chase Bliss pedals** auto-receive MIDI clock — no config needed.
- **Meris LVX:** set its MIDI OUT mode to **"through"** (not just "out") if it sits mid-chain, so incoming clock is passed along.
- **Strymon Volante:** clock-receive is **saved per preset** — hold Feedback buttons 1+4 and turn the Record-Level knob: **red = does NOT receive clock, green = receives clock.**

## Takeaway for the rig (Digitakt as master)
The same Global-Config path (Shift+Looper → Filter knob → selector 1/3 → confirm white) governs the Microcosm's clock behavior. With the **Digitakt** as master you want the Microcosm to **receive** (slave) and pass clock through — so set the option that **echoes incoming MIDI out** (position 1), feed Digitakt OUT → Microcosm IN, and let the Microcosm's OUT continue to the rest of the chain. Remember the slave only follows external clock **after a MIDI Start** message.
