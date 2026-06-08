https://forum.rme-audio.de/viewtopic.php?id=33616
RME User Forum · thread "Best settings for low latency in Win 10 (Babyface Pro FS)" · FireWire & USB series

Concrete low-latency advice from the RME forum, plus the "why" behind RME's small-buffer reputation.

THE METHOD (find your floor empirically):
- Start at the LOWEST buffer size and test. If you hear crackles, step up to the next-higher ASIO buffer size. Repeat until clean. There is no universal magic number — it depends on your CPU, drivers, DPC latency, DAW, and project complexity.

TARGET NUMBERS:
- For virtual-instrument / live-monitoring work you want round-trip latency (RTL) below ~10 ms. With RME you typically hit that with an ASIO buffer of AT MOST 128 samples at single speed (44.1/48 kHz).
- Real-world reports: users run 64 samples with "quite a few VST instruments" on both older i7 and newer i9 machines; latency is "still good at 128 samples." For recording-only work (no soft-synths to play live), you can just use a large buffer — latency doesn't matter when you're not monitoring through the computer.

SYSTEM TWEAKS THAT MATTER (Windows):
- Disable WiFi during live/critical work — it adds interrupt (DPC) load that causes dropouts at small buffers.
- Disable onboard audio in BIOS and any unnecessary onboard hardware (every active driver can inject poorly-optimized routines).
- In RME driver settings, enable Windows-compatible WDM devices but select only as many as you actually need (created instantly, no reboot).
- System optimization (clean drivers, low DPC latency) is what actually determines how small a buffer you can sustain.

WHY RME HOLDS UP AT TINY BUFFERS (the design philosophy):
- RME's stated approach is to run as many functions as possible NOT in the driver/CPU but within the audio hardware itself. The DSP mixer (TotalMix FX) and monitoring run on the interface, so the host CPU isn't doing the mixing.
- ASIO Direct Monitoring + the hardware mixer mean you can monitor inputs latency-free regardless of DAW buffer — so you can run a LARGE buffer for plugin headroom while still monitoring your live input with zero latency through TotalMix.
- This is the core reason the Babyface is a credible failover/portable box: every buffer size "works well and offers realistic latency figures," unlike interfaces that only behave at large buffers.
