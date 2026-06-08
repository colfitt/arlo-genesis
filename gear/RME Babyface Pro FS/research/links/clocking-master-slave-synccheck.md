https://forum.rme-audio.de/viewtopic.php?id=34401
RME User Forum · thread "Choosing Clock Master with SteadyClock" · FireWire & USB series

How to choose the clock master in a multi-device digital rig, and why SteadyClock FS makes the choice low-stakes sonically.

THE PRACTICAL RULE (workflow over dogma):
- Make the interface whose driver your DAW loads the clock MASTER. Then the host application sets the sample rate, the interface gets it automatically via the driver, and all slaved gear chases over ADAT/SPDIF — no manual DIP-switch or front-panel sample-rate fiddling on the external boxes.
- For the slave: set its Clock Source to the digital port carrying the signal (ADAT or SPDIF / "Optical In"). Only then does its input show a steady SYNC.

WHY SteadyClock MEANS MASTER vs SLAVE BARELY MATTERS SONICALLY:
- SteadyClock actively recovers a clean, low-jitter clock from a jittery incoming digital signal. Devices with strong clock recovery "perform (almost) identically as slave or master." So with the Babyface Pro FS, slaving it (or slaving the Apollo to it) does NOT degrade conversion — pick the master for WORKFLOW reasons, not sound. Expect negligible audible difference in blind tests.

SYNCCHECK — read the status, trust it:
- "Lock" = locked onto the incoming sample rate but still running on its own clock.
- "Sync" = the clock is genuinely detected on a digital input and the device is synchronous. For a correctly slaved device you want SYNC, not just Lock.
- The Opt LED / SyncCheck display gives instant No-Lock / Lock / Sync feedback. Confirm solid SYNC before committing a print so prints stay sample-accurate.

GOTCHAS:
- Only ONE master allowed in a digital setup. Two masters fighting = clicks/pops or no-lock.
- Clock quality also depends on cable/signal integrity, not just master/slave designation.
- The Babyface has NO BNC word clock — the clock link is the optical (ADAT/SPDIF) cable. Plan the topology around that single optical bridge.

RIG APPLICATION: with the Octatrack/Digitakt/MPC/OP-1 + Apollo all in play, the simplest stable config is to make the box driving the DAW the master and slave the rest over optical. If you specifically want the femtosecond SteadyClock FS as the studio reference, set the Babyface to Internal/Master and slave the others to its optical out — but know that, thanks to SteadyClock's jitter rejection, you're choosing this for tidiness, not a sonic upgrade.
