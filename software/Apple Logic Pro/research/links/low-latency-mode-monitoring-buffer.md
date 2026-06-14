https://support.apple.com/en-us/105040 · https://whylogicprorules.com/software-monitoring/ · https://www.charlescleyn.com/blog/how-to-use-buffer-size-logic-pro
apple.com + whylogicprorules + charlescleyn · current

# Low Latency Mode, software monitoring & buffer — for tracking the rig live

When recording the pedalboard/banjo/baritone through Logic's plugins live, this
is how to keep monitoring tight without disabling your chain.

## I/O Buffer Size (Settings > Audio > Devices)
- Range **32 to 1024 samples**. Lower = less latency, more CPU strain.
- **128 samples** = good starting point for tracking audio. Drop to 64/32 if
  your CPU allows; raise it for mixing big sessions.
- Going to **32 on a heavy project causes pops, glitches, and "System
  Overload"** — only use the smallest buffers on light tracking sessions.
- Workflow: **low buffer while recording, high buffer while mixing.**

## Low Latency Mode (Options menu, or assign a Key Command)
- Toggling it **temporarily bypasses any plugin contributing more than ~0.5 ms**
  of monitoring latency (lookahead limiters, linear-phase EQ, convolution
  reverb, etc.) so you can monitor through your chain with minimal delay.
- Turn it ON to track a part through a heavy drone chain, OFF to hear the full
  processed sound on playback. Great for playing banjo/baritone INTO a big
  Space Designer + ChromaVerb chain without lag.

## Software vs hardware monitoring
- **Software monitoring** (on) = you hear the signal THROUGH Logic's plugins —
  needed to monitor the live chain, but adds round-trip latency.
- For zero-latency tracking of the dry source, **monitor through the interface's
  own DSP** (Apollo Console / TotalMix on the Babyface) and keep Logic's
  software monitoring OFF for that track — then the recorded plugins are heard
  only on playback. Best of both: track dry+tight, hear effects after.

## Rig note
- The **Apollo x8 (UAD Console)** can monitor with near-zero latency and even
  print UAD effects — ideal for tracking the rig; let Console handle monitoring,
  Logic handle recording.
- The **RME Babyface Pro FS (TotalMix FX)** likewise gives DSP-mixer zero-latency
  monitoring. Use TotalMix for the cue mix, Logic for the multitrack.
- Reamping is the exception — there you WANT the round-trip (the signal must
  physically leave and return), so use the I/O plugin + ping (see
  io-plugin-reamp-ping-latency.md).
