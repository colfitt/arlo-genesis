Sources: https://discussions.apple.com/thread/1715283 · https://vi-control.net/community/threads/logic-kontakt-guru-help-needed-cpu-overload-in-a-good-system-environment-solved.84373/ · https://vi-control.net/community/threads/logic-pro-freezing-multitimbral-tracks.42187/ · https://support.apple.com/en-us/108295
Apple Community / VI-Control / Apple Support · distilled · current

# Kontakt in Logic — CPU, crackling, freezing (the load-management playbook)

## Crackling / CPU overload fixes
- **Raise Logic's I/O buffer** to **1024** (Settings → Audio) for mixing/playback — biggest single CPU relief; drop it back for low-latency recording.
- Logic audio settings that help: **Multithreading ON**, **Processing Threads = Automatic**, **Buffer = Large**, **32-bit rendering**, **ReWire OFF**.
- In Kontakt, push **DFD/preload higher (~60 MB)** or switch a heavy instrument to **Sampler mode** so samples sit in physical RAM rather than streaming — trades RAM for fewer disk-stream dropouts.
- Crackling specifically *when you tweak a plugin* is often a momentary overload, not a steady-state problem — bigger buffer absorbs it.

## Freezing vs bouncing (Logic + Kontakt gotcha)
- **Logic disables track Freeze for MULTITIMBRAL / multi-output AU instances** (incl. multi-out Kontakt). Single (stereo, one-instrument) Kontakt instances CAN be frozen normally.
- Workaround for multitimbral/multi-out: **Bounce In Place** (or bounce each aux output to audio) instead of Freeze. Both render to audio and slash CPU.
- General rule: once a Kontakt part is written, **freeze or bounce it to audio** to kill CPU spikes, pops, and latency — essential on bigger ambient sessions with several heavy instances.

## CPU-saving routing (pairs with multi-out)
- **One shared reverb on a Kontakt aux output**, with each instrument *sent* to it, instead of a reverb instance per instrument — big CPU save and a more cohesive space (ideal for a drone bus where everything shares one long tail).
- For per-track reverb prefer Logic's lighter **SilverVerb / PlatinumVerb** over heavy convolution when CPU is tight.

## Rig takeaways
- Drone/ambient sessions are usually **low-polyphony but heavy-patch** → the wins are: purge after playing, freeze/bounce finished layers, one shared reverb aux, and a 1024 buffer. Keep automation-heavy instruments on their OWN single instance (freezable + clean CC).
