https://help.uaudio.com/hc/en-us/articles/360030068452-Managing-DSP-Resources
Universal Audio Support · "Managing DSP Resources" (+ companion blog "Channel DSP Pairing with your Apollo Interface", uaudio.com)

(Help page content distilled from UA Support text surfaced via search; the help.uaudio.com domain blocks direct fetch.)

THE CORE REALITY:
- Realtime UAD processing on a Console INPUT is allocated per channel. A single UAD plugin must fit on one DSP core; it cannot span cores.
- Tracking-side (Console) DSP and mix-side (DAW UAD plugins) draw from the SAME six SHARC chips (HEXA Core). They compete.

CHANNEL DSP PAIRING (the main per-input headroom feature):
- Enable path: Console → Settings → Hardware panel → Options column. ON by default.
- What it does: lets multiple UAD plugins inserted on a SINGLE Console input channel strip span across two paired DSP cores — effectively DOUBLING the realtime DSP available to one input. UA: it "automatically distributes plug-in processing loads across paired DSP cores on a single input," letting you "run larger plug-in chains on individual channels with the lowest possible latency."
- Limits: requires UAD v9.10+; a single plugin still can't span paired cores; it does NOT increase TOTAL system DSP — it only redistributes per-input.

MITIGATIONS FOR OVERLOAD (from "Managing DSP Resources" + "Getting the Most Out of Your DSP"):
1. COMMIT while tracking: set INSERT EFFECTS to "UAD REC" rather than "UAD MON" to print the processing into the recording, then disable the UAD plugins in Console afterward to FREE that DSP for mixing.
2. Reduce CUE BUS COUNT: Console → Settings → Hardware. If you don't need all 4 independent cue sends, lowering the count conserves DSP.
3. Use Legacy / SE plugin versions — similar sound, much smaller DSP footprint.
4. Bus routing: to use a DSP-heavy plugin on several tracks, route them to one bus/aux and use a single instance.
5. In the UAD Meter & Control Panel, enable "Release all UAD DSP resources on AU bypass" so bypassing a plugin in Logic/AU hosts actually frees its DSP.

For this rig: four Unison preamps + channel inserts + a couple monitor-bus reverbs fit comfortably; the contention point is a giant tracking chain on one input or heavy mix-side UAD use. Print/commit (UAD REC) the board capture, then free the DSP for the mix.
