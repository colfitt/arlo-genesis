Manual: SL MkIII User Guide V2, pp.14, 18 (Part destinations, MIDI Out 2), p.28 (Host Inputs/Outputs)
Novation manual

# The 3 DIN sockets + USB ports — fanning MIDI out to the whole rig

## The three 5-pin DIN sockets
- **MIDI In** — clock/notes/Start-Stop/SPP into the SL; can be forwarded to USB host (see "From DIN 1").
- **MIDI Out (Out 1)** — main MIDI out; clock-capable.
- **MIDI Out 2 / Thru** — Global setting **MIDI Out 2** chooses its behaviour:
  - **"Out"** → a **second independent MIDI output**, also clock-capable. You now have **two separate DIN out streams** (Out 1 + Out 2) → drive two different destination chains.
  - **"Thru"** → copies **MIDI DIN In → out**, hardware-thru style; the SL sends **none of its own** generated MIDI here. (If Parts were routed to Out 2 and you switch it to Thru, the Part destination setting stays but no Part MIDI leaves Out 2.)

## Per-Part destination routing (Part Settings: Shift + Sessions)
Each of the 8 Parts independently routes to **one or more** destinations (set with rotaries above each option; stored in the Session):
- **USB**: Off / On
- **DIN**: Off / **1** / **2** / **Both**
- **CV/Gate**: Off / **1** / **2** / **Both**
Plus each Part has its **own MIDI Channel 1–16** (rotary 6). No global channel. **Channel 16 caution:** reserved for global PC/Song-Select — a Part on ch.16 can change the SL's own Session and lose unsaved work; use **Save Lock**.

## USB host ports (to the Mac)
- Inputs the host sees: **MIDI** (Parts routed to USB), **InControl** (DAW protocol port), **From DIN 1** (forwards DIN-In to the computer → SL acts as a USB-MIDI interface).
- Outputs: **MIDI** (record to SL sequencer), **InControl**, **To DIN 1 / To DIN 2** (host → straight out the DIN, unaltered), **To CV/Gate** (host notes → CV/Gate; **MIDI ch.1 → CV/Gate 1, ch.2 → CV/Gate 2**; CC matching a Mod-CC → that Mod port).

## Fan-out strategies for this rig
- **Two DIN chains:** Out 2 = "Out". Out 1 → one MIDI-thru chain (e.g. CB pedals + Hologram + H90 daisy-chained by MIDI Thru on each pedal, each on its own channel); Out 2 → the VG-800 / a second box. Both carry clock.
- **DIN + USB split:** DAW-less boxes on DIN, soft synths on USB, same Session — each Part picks its lane.
- **Out 2 as Thru:** if you want the SL to merely pass an upstream box's MIDI through to a downstream chain without injecting its own.
- **MIDI interface mode:** "From DIN 1" + "To DIN 1/2" lets the Mac talk to DIN gear through the SL with no extra interface.
