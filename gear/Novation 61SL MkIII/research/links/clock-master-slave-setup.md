Manual: SL MkIII User Guide V2, pp.18–19, 21–22 (MIDI Clock Rx/Tx, Tempo, Transport, Clock Out PPQN)
Novation manual

# Clock — making the SL the master vs slaving it; routing clock to the rig

## MIDI Clock (24 PPQN) — the digital clock to USB + both DIN
Set in **Global** (press Global button; settings are device-wide, persist on power-switch-off but NOT if you pull the power cable):
- **MIDI Clock Tx** (On/Off via rotary): On → SL **sends** its internal clock at **24 PPQN to USB MIDI and BOTH MIDI DIN ports simultaneously**. Devices set to receive sync now follow the SL.
- **MIDI Clock Rx** (On/Off): On → if the SL detects clock at **either** USB **or** DIN input it **slaves** to it. **Send clock to USB OR DIN, not both** — feeding both can cause sync loss / erratic tempo.
- Confirm sync: press **Tempo** — shows synced BPM + the word **"External"**. Lost sync while playing → **"Sync Lost"**, and the SL won't fall back to internal clock until you **stop the transport**.
- Clock source can only change while **transport is stopped**.

## Transport messages (master mode)
With **MIDI Clock Tx On**, the SL sends **Start / Stop / Continue** with the transport buttons:
- **Play** = Start (restarts from session start). **Stop** = Stop. **Shift+Play** = Continue (from current position). Play while running = Stop then Start.
- These Start/Stop/Continue messages **only send if MIDI Clock Tx is On.**

## External control (slave mode)
The SL responds to incoming **Start / Stop / Continue** (System Real-time) at DIN-In or USB-In, and to **Song Position Pointer (SPP)** when the sequencer is stopped (updates + retransmits internal song position; ignored while running).

## Analog Clock Out (the 3.5 mm jack — for non-MIDI gear)
- Separate from MIDI clock. Sends a pulse per quarter note while transport runs.
- **Clock Out PPQN** (Global): **1, 2 (default), 4, 8, or 24** — match it to whatever the analog/modular destination expects (e.g. many Eurorack clock-ins want 1 PPQN = quarter-notes; some want 2/4/24).

## Tempo
- **Tempo** button → left rotary sets BPM (integers **40–240**). **Tap** tempo = tap ≥3× (unavailable while synced to external clock).
- **Swing** 20–80% (50% = none), **per-track** swing on/off, swing sync rate (default 1/16).

## Master decision for this rig (per dossier §5)
- **SL as master:** Tx On. Clock + Start/Stop go to USB and both DINs at once — drives Elektrons, MPC, VG-800, the MIDI pedals' tempo-sync, and the analog Clock Out feeds modular. The simplest "SL runs the room" setup.
- **SL as slave (follow an Elektron):** Rx On, feed clock from ONE source (e.g. Digitakt's DIN-out → SL DIN-In, OR USB — not both). Use when an Elektron owns the groove.
- **Caution:** decide ONE clock master per song. Don't have the SL Tx On while also Rx-ing an Elektron's clock — pick a direction.
