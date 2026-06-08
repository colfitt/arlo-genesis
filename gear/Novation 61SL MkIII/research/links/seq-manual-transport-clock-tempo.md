Manual: SL MkIII User Guide V2, p.18, p.21–22
Novation manual

# Transport, clock (Rx/Tx), tempo & swing — running the sequencer

## Transport (Start/Stop/Continue) — only sends if MIDI Clock Tx is On
- **Play** → starts sequencer playback + sends MIDI **Start**.
- **Stop** → stops + sends MIDI **Stop**.
- **Shift + Play** → starts from the **current position** + sends MIDI **Continue**.
- **Play while running** → sends Stop then Start (restarts the sequencer from the start of the Session).
- **External control (received at DIN/USB In):** Start → playback starts; Stop → stops; Continue → continues from current position; Start *during* playback → ignored.
- **Song Position Pointer (SPP):** while the sequencer is **stopped**, an incoming SPP updates internal song position and retransmits. While **running**, SPP is ignored.

## MIDI Clock (Global Settings → Global button)
- **MIDI Clock Rx** (rotary): On/Off. On = SL syncs to external clock at USB **or** DIN. **Send clock to only one (USB or DIN), not both**, or you get loss of sync / erratic tempo. Press Tempo to confirm "External" + synced tempo. If clock is lost mid-play → "Sync Lost"; won't revert to internal clock until you Stop.
- **MIDI Clock Tx** (rotary): On/Off. On = SL is **clock master**, sends **24 PPQN** to USB MIDI AND both DIN ports.
- **Clock Out PPQN** (analogue clock out): 1, 2 (default), 4, 8, or 24.
- **MIDI Out 2:** 'Out' = second independent DIN out (clock to two destinations). 'Thru' = copies DIN In → DIN Out, SL sends no internally-generated MIDI to it.

## Tempo / Swing view (Tempo button)
- **Set Tempo:** left-most rotary → **40–240 BPM** integer (only when not following external clock).
- **Display Clock Source:** shows "External" when receiving clock (Rx on); tempo follows received clock, fluctuates then settles, not adjustable by knob. Clock source only changes while Transport stopped.
- **Swing:** moves notes off the grid for feel. **20%–80%**, default 50% (no swing). >50% = positive swing (pushes even beats 2 & 4 later toward 3 & 1); <50% = negative.
- **Swing Per Track** (Tempo menu, firmware 1.4): On/Off per track. Off = that track's sequencer + arp steps ignore global swing (defaults to 50%). Stored in the session.
- **Swing Sync Rate:** default **1/16** (swings pairs of 1/16ths). Triplet rates denoted with "T."
- **Tap Tempo:** tap the **Tap** button ≥3 times at the intended tempo. Unavailable when synced to external clock.

## CV/Gate notes (sequencer relevance)
- Routing a Part to CV/Gate sends note info to that port; MIDI notes **24–108 → 0–7 V** (out-of-range clamps).
- CV/Gate is **monophonic** — the poly note stream collapses to **most-recently-played note** priority. Gate high while a note is active, low when all released.
- A Part routed to CV/Gate also drives the matching **Mod** port (CC→voltage 0 to +5V; CC# set in Global Settings; range −5/+5V or 0/+5V per Global). So a sequenced/automated CC on that Part becomes CV.
