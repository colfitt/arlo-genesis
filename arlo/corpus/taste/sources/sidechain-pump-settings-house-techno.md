https://www.gearnews.com/sidechain-compression-in-techno-workshop/  ·  https://www.musicradar.com/tuition/tech/how-to-create-classic-pumping-sidechain-compression-624915  ·  https://www.waves.com/sidechain-compression-explained-fundamental-techniques

gearnews.com + MusicRadar + Waves · sidechain-compression "pump" technique guides · (concrete settings)

# Sidechain pump — the four-on-the-floor "breathing" settings

The defining motion of filter-house / French-house / LCD-style dance (the kick "ducks" everything else so the track breathes with the beat). Concrete starting numbers, triangulated across three guides:

- **Trigger:** a **quarter-note kick** (4-on-the-floor) feeds the sidechain input of a compressor on the synth/bass/pad/loop bus. When the kick hits, the bus volume drops, then recovers before the next kick — that recovery sweep IS the pump.
- **Attack:** **1–10 ms** (a popular start = **1 ms**) — fast enough to duck instantly on the kick; if you hear a click, ease attack up slightly.
- **Release:** **30–300 ms**, set so the bus is **fully back up just before the next kick**. At house tempo (~120–125 BPM) **150–250 ms** gives the obvious pump. At 120 BPM a quarter note = 500 ms, so release well under that.
- **Ratio:** **4:1 to 10:1** for a classic pump (2:1 = subtle, 10:1 = aggressive).
- **Threshold / gain reduction:** set low enough that the kick triggers it; aim for **6–12 dB of gain reduction** on each hit.

**Rig honesty (no DAW compressor in the chain — fake the pump on hardware):**
- **Octatrack MkII:** it has **2 compressors** (one per stereo input pair) and a documented "sidechain pumping on every pattern (default 4-on-the-floor)" template; OR fake it with an **LFO → AMP volume** (ramp/saw wave, synced to 1/4) on the loop track — the ramp's shape IS the duck-and-recover.
- **Digitakt 2:** **LFO → track LEVEL/AMP volume**, `WAVE = RAMP` (or inverse saw), `MULT` tempo-synced so one cycle = one beat, `DEP` high; trigs the duck without a real sidechain.
- **MPC Sample:** the **Compressor FX** (Attack 0.100–150 ms, Release 3.0–300 ms, Amount 0–100%) on a bus — but the AC50 has no sidechain key input, so the closest is an LFO/automation-style volume duck or a transient/tremolo trick on the loop pad.
- The pump is an **emulation** on this rig — there is no true sidechain key routing on the Elektrons/MPC the way a DAW has; the LFO-ramp-on-volume reproduces the *result*.
