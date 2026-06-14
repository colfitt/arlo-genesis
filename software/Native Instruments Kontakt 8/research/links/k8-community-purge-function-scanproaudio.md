https://www.scanproaudio.info/2017/11/16/tips-tricks-kontakt-optimization-the-purge-function/
scanproaudio.info · Scan Pro Audio · 2017-11-16 (still accurate for K8)

# The Purge function — the core RAM-saver

**What it does.** Unloads samples an instrument isn't actually using, freeing RAM. Most valuable with big multisampled libraries (orchestral, Spitfire) where a patch maps thousands of samples but a part only touches a fraction.

**The Purge menu (per-instrument, top-right of the instrument header) has four functions:**
- **Reset Markers** — removes the "used" markers but does NOT purge; samples stay loaded.
- **Update Sample Pool** — purges the samples that weren't used (the key one).
- **Purge All Samples** — unloads ALL samples (instrument goes silent until reloaded/triggered).
- **Reload All Samples** — loads every sample the instrument maps.

**The recommended workflow (purge AFTER playing):**
1. Start with all samples loaded.
2. Record/lay down your part.
3. **Reset Markers**, then play the part through once so Kontakt marks exactly which samples fire.
4. Run **Update Sample Pool** → only the unused samples are dropped. Big RAM win on a finished arrangement.

**Caveats:**
- Starting *purged* and loading on-the-fly from MIDI can cause clicks/pops/missing notes on the first pass — especially on HDD. SSD strongly recommended for purge-on-demand.
- Pair with DFD/preload buffer tuning for further memory savings.

**Rig note:** for a drone/ambient session where a Spitfire string patch is held on one or two sustained notes for minutes, "play the part → Update Sample Pool" can drop a multi-GB patch to a tiny resident footprint — exactly the use case where purge pays off most.
