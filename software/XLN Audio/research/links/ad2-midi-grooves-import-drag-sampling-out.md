https://oddgrooves.com/how-to-add-oddgrooves-midi-beats-to-xln-audio-addictive-drums/
oddgrooves.com · Per Ulfhielm · 2020-07-20 (+ Groove Monkee "free MIDI loops for AD" + XLN MIDIpak page for context) · accessed 2026-06-11

# AD2 MIDI grooves: import IN, drag OUT, and sampling AD2 OUT to MPC/Kontakt/Digitakt

## Import external MIDI INTO AD2's Beats library (hidden help-menu trick)
1. AD2 → **Help menu (the "?" icon, top-right)** → **"Open external MIDI folder."**
2. **Copy the MIDI pack folder** (OddGrooves / Groove Monkee / any GM MIDI) into the
   **"External MIDI files"** folder that opens.
3. Back in the **Help menu → "Refresh MIDI library."**
4. The grooves now appear in AD2's **Beats** browser alongside the built-in MIDIpaks.
- AD2 reads **General MIDI** drum mapping, so generic GM MIDI loops work; pre-mapped
  "for Addictive Drums" packs map cleanest.

## Drag AD2 grooves OUT to the DAW
- In the **Beats** tab: audition a groove, optionally hit **Transform** (change the
  groove's parameters / time-stretch without quality loss), then **drag the groove
  straight onto an AD2 MIDI track** in Logic/Ableton. Now it's editable MIDI — quantize,
  rearrange, humanize, thin it out for slowcore.
- **Edit Play / humanize / velocity** live in the Beats/Edit area for performance feel
  before you commit.

## Sampling AD2 OUT → one-shots for MPC Sample / Kontakt / Digitakt (owner's goal)
No native "export one-shot" button; the reliable workflow:
1. Put each drum on its own AD2 **multi-out** track (or solo one drum at a time).
2. **Trigger a single hit** (one MIDI note at the velocity you want) and **bounce a
   short region per drum** — or bounce a few velocities for layers/round-robins.
   - To capture AD2's natural decay/room, include the tail; to get a tight one-shot,
     bounce dry (FX off) and add space later.
3. **Degrade the bounce** here if you want a "found" sample: run the one-shot through
   **RC-20 (Noise Duck + Magnetic + Digital rate-crush)** before chopping — the same
   "old sample" stamp the rig already uses on hardware-sampled material.
4. Load the resulting WAVs into:
   - **Akai MPC Sample** — assign to pads, slice/chop, build beats (the owner's main
     beat box). Bounce a few velocity layers for playable dynamics.
   - **Kontakt 8** — drop into a multi-sample instrument for velocity/round-robin
     mapping and key-spanning.
   - **Digitakt 2** — transfer one-shots via Transfer; tune/trim on-device. Keep them
     short (Digitakt sample memory is finite) — bounce trimmed, normalized hits.
- This makes AD2 a **sample FACTORY** for the owner's own kits, not just a play-along
  instrument: dial a vintage/dead kit, add AD2's tape sat, bounce hits, degrade,
  chop on the MPC.
