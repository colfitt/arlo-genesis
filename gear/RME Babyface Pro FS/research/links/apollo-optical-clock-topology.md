https://forum.rme-audio.de/viewtopic.php?id=30666
RME User Forum · thread "Apollo x8 and Babyface Pro FS clock mode" · FireWire & USB series

The exact topology this rig uses — confirmed working by RME forum users connecting a UA Apollo x8 to a Babyface Pro FS over the optical port.

TOPOLOGY (Apollo as master, Babyface slaved):
- Connect Apollo x8 ↔ Babyface Pro FS via TOSLINK optical (ADAT or SPDIF).
- Apollo x8 = clock MASTER. Babyface Pro FS = clock SLAVE.
- On the Babyface, set Clock Source = "Optical In" (NOT Internal). Set the sample rate to match the Apollo (e.g. 48000 Hz).
- When locked correctly, the Babyface driver/TotalMix status reads: "ADAT: Sync (48 kHz)".

LOCK vs SYNC (read the status line, don't guess):
- "Lock" = the interface has locked onto the sample rate of the incoming digital signal, but is still running on its own clock.
- "Sync" = the interface has detected its clock ON a digital input and is genuinely synchronous. For a properly slaved device, you want to see SYNC, not just Lock. Seeing "ADAT: Sync (48 kHz)" on the Babyface confirms it is correctly chasing the Apollo's clock.

ADAT vs SPDIF over the same optical port (the sample-rate gotcha):
- ADAT always runs at 44.1 or 48 kHz. It has no native 96 kHz — at higher rates it uses S/MUX (two 48 k ADAT channels carry one 96 k channel; channel count halves as rate doubles).
- If you only need 2 channels of clock+audio between the boxes, the forum's recommendation is to use SPDIF optical instead of ADAT. Set BOTH devices to send/receive SPDIF-optical mode (not ADAT). SPDIF allows the sample-rate change to propagate cleanly between the two devices, giving better sample-rate flexibility (e.g. switching to 96 k) than ADAT's S/MUX behavior.

CABLING:
- A SINGLE optical cable from master → slave is enough to carry the clock. A second cable (slave → master) is only needed if you also want to send the slave's input audio back to the master.

RIG NOTE: the Babyface has NO BNC word clock — this optical link IS the clock connection between the Apollo and the RME. If you instead want the femtosecond SteadyClock FS as the studio reference, reverse the roles: Babyface = Internal/Master, optical out → Apollo's ADAT/optical in, set the Apollo to slave to its optical input.
