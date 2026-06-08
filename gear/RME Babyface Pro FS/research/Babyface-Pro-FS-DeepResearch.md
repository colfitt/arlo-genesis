# RME Babyface Pro FS — Deep Research

A working dossier for the studio's **portable/secondary** interface. The Babyface Pro FS is not the hub — the UA Apollo x8 is. It's the box that goes in the bag when the banjo or the pedalboard has to be recorded somewhere that isn't the room with the Apollo, the pristine clean front-end when a track needs RME converters and nothing else, the femtosecond clock master the digital rig can chase, and the failover that keeps a session alive if the Apollo drops. Most of what follows is concerned with *that* role — when you reach for the RME instead of the Apollo, and how the two coexist — rather than the spec-sheet bragging RME's marketing leads with.

## 1. Lineage: Babyface → Babyface Pro → Babyface Pro FS

The Babyface line is RME's "the whole interface fits in a coat pocket" answer to the question of how to get [Fireface](https://rme-audio.de)-grade conversion and drivers into a bus-powered desktop box. Three generations matter:

- **Babyface (2011)** — the original snail-shaped puck with a breakout cable for the analog I/O. Good converters, awkward ergonomics.
- **Babyface Pro (2015)** — the redesign that made the line serious: housing "machined from a block of aluminium," XLR mic inputs on the chassis, two independent headphone driver circuits, full TotalMix FX, and a proper rotary-encoder UI. This is the unit most people picture.
- **Babyface Pro FS (2018)** — the current model, and the one in this rig. The "FS" stands for **FemtoSecond**, and the headline change is the clock: RME dropped in the full **SteadyClock FS** circuit from the flagship [ADI-2 Pro FS](https://www.rme-usa.com/steadyclock-fs.html), the same femtosecond-grade clocking found in their reference converters. Per [RME USA](https://www.rme-usa.com/babyface-pro.html), the FS also inherited "the same headphone preamp technology output op-amps as ADI-2 Pro" — the 3.5mm headphone output's impedance dropped from 2Ω to **0.1Ω**, max power rose to **90mW**, and THD improved "up to 10 dB across both parallel outputs."

[Sound on Sound](https://www.soundonsound.com/reviews/rme-babyface-pro-fs) frames the FS honestly as "incremental rather than revolutionary" — the same winning formula with the clock and headphone stages upgraded. For this rig that's exactly right: you're not buying the FS for a sonic revolution over the Pro, you're buying it because it's the current, best-clocked, most-supported version of an already-proven travel interface.

## 2. Architecture & I/O

The Babyface Pro FS is a **24-channel** interface (12-in / 12-out when you count the optical port at single speed), built around four analog ins, four analog outs, an optical port, MIDI, and the TotalMix FX DSP mixer. Per the block diagram in the [manual](manuals/bface_pro_fs_e.pdf) (§29.1):

**Analog inputs (4):**
- **2 × XLR mic/line preamps** (channels 1–2), rear panel. Servo-balanced electronic input stage that "handles unbalanced and balanced signals correctly." **76 dB gain range in 1 dB steps** with a relay-driven PAD ([RME USA](https://www.rme-usa.com/babyface-pro.html)). These are the reference-quality preamps.
- **2 × TS instrument/line inputs** (channels 3–4), right side, ¼" hi-Z (1 MΩ), with 9 dB of fine digital gain and a +4 dBu / −10 dBV reference switch set from TotalMix.

**Analog outputs (4):**
- **2 × balanced XLR line outs** (channels 1–2), rear, with a recessed slide switch on the underside selecting **+19 dBu (default) or +4 dBu** max output level.
- **2 × headphone outs** (channels 3–4), right side: one **¼" TRS** (high-impedance optimized) and one **3.5mm TRS** (low-impedance optimized), each with its own independent driver circuit.

**Digital I/O:**
- **1 × optical TOSLINK in + 1 × out**, auto-detecting **ADAT or SPDIF**. ADAT carries 8 ch @ 48 kHz, 4 ch @ 96 kHz (S/MUX), 2 ch @ 192 kHz (S/MUX4). This is the channel-count multiplier and the clock link to the rest of the rig.
- **1 × MIDI I/O** via the included 6-pin mini-DIN breakout cable (2 × 5-pin DIN), optocoupler-isolated.

**The brain — TotalMix FX:** a **288-channel** DSP mixer with **46-bit internal resolution** running entirely on the interface (not the CPU), offering latency-free submixes, ASIO Direct Monitoring, and onboard FX: **3-band EQ, low cut, reverb, and echo** per channel. There is no onboard *plug-in* DSP — TotalMix FX is mixing/monitoring/EQ, not a UAD-style effects host. That distinction is the whole Apollo-vs-RME story (see §5).

## 3. Sonic Character

The RME house sound is the absence of a sound. Across reviews the descriptors are consistent: [Sound on Sound](https://www.soundonsound.com/reviews/rme-babyface-pro-fs) calls it "transparent, clear and pristine"; the brand's entire reputation is built on neutral, uncoloured conversion that gets out of the way. The numbers back it up — from the [manual](manuals/bface_pro_fs_e.pdf) §27.1:

- **Mic/Line 1–2 AD:** SNR **113.7 dB RMS unweighted (117 dBA)**, THD < −112 dB, THD+N < −108 dB.
- **Line/Instrument 3–4 AD:** SNR **116 dB RMS (120 dBA)** — the instrument inputs are actually the quietest converters in the box.
- **XLR Line Out 1–2 DA:** dynamic range **115 dB RMS (118 dBA)**, THD −106 dB.

Practically: the preamps are clean and quiet rather than characterful. There is no Neve-ish iron, no Unison-style tube/transformer modeling — what goes in comes out, amplified and converted with vanishingly low noise and distortion. For a banjo DI or a KM184 small-diaphragm condenser, that neutrality is the point: you want the source and the mic, not the interface's opinion of them. If you want *colour*, that's a job for the pedalboard upstream, a plugin downstream, or the Apollo's Unison preamps — not the RME.

## 4. Workflow & Behavioral Notes

This is where RME earns its cult reputation, and where the FS differs most from "cheaper interface that also has two preamps."

- **Drivers.** RME's drivers are the industry benchmark for stability and low latency. Measured round-trip latency is roughly **3.1 ms @ 44.1 kHz (48 samples), 2.9 ms @ 96 kHz, 2.8 ms @ 192 kHz** ([Sound on Sound](https://www.soundonsound.com/reviews/rme-babyface-pro-fs)), and — more importantly — *every* buffer size "works well and offers realistic latency figures," including tiny buffers that make other interfaces crackle. The conversion itself adds only ~5 samples AD / 7 samples DA ([manual](manuals/bface_pro_fs_e.pdf) §28.2). RME's philosophy, stated in the [manual](manuals/bface_pro_fs_e.pdf) §1, is to run "as many functions as possible not in the driver (i.e. the CPU), but within the audio hardware."
- **Bus power.** Fully bus-powered over USB with **no spec degradation** — idle 2.8 W, typical 3.7 W, max 5.4 W ([manual](manuals/bface_pro_fs_e.pdf) §27.6). An optional locking DC supply is available to unburden a marginal laptop port, but in practice the USB bus is enough.
- **Clocking.** **SteadyClock FS** actively rejects jitter from external clock sources. The [manual](manuals/bface_pro_fs_e.pdf) §28.7 shows it converting an extremely jittery ~50 ns SPDIF input into a clock with **< 2 ns jitter** — and the cleaned clock is used for the digital *output* too, so the Babyface can be a reference clock for the rest of the chain. **SyncCheck** and the Opt LED give instant visual confirmation of No-Lock / Lock / Sync state.
- **TotalMix FX learning curve.** The honest caveat. TotalMix is enormously powerful — three rows (hardware inputs / software playback / hardware outputs), arbitrary submixes, per-channel EQ and FX — but [Sound on Sound](https://www.soundonsound.com/reviews/rme-babyface-pro-fs) calls it "somewhat impenetrable" on first contact. Once the three-row model clicks it's the best monitor mixer in the class; until then it's the one thing about the box that frustrates newcomers. The iPad TotalMix control app is a paid add-on, which the same review calls "a bitter pill to swallow."

## 5. Role in the Studio / Integration with the Rig

This is the section that matters most. The studio has **two** interfaces and they are not redundant — they're a deliberate split.

**The UA Apollo x8 is the hub.** It's the print terminus the [rig-design](../../../rig-design.html) board explicitly routes to ("OUT → Apollo / FOH, printed to tape"). It has more analog I/O, **Unison preamps** that model classic mic-pre/amp front-ends, and — critically — **onboard UAD DSP** that hosts plugins (LA-2A, 1176, Neve, Pultec, amp sims) at tracking latency. The Apollo is where the rig lives when it's home: the pedalboard prints to it, full sessions track to it, and UAD processing happens on it.

**The Babyface Pro FS is the portable/secondary box.** Reach for it when:

1. **Mobile / location recording.** Bus-powered, aluminium, fits in a bag with a laptop. This is the interface that records the EBM-5 banjo or the whole pedalboard somewhere that isn't the studio — no power outlet required, no Apollo to haul.
2. **A pristine, uncoloured front-end.** When you specifically want RME conversion with *no* Unison colour — a clean banjo DI, a KM184 on an acoustic, a reference-clean print — the RME's neutrality is the feature, not a limitation.
3. **Clock master for the digital rig.** SteadyClock FS is arguably a *better* clock than the Apollo's. The Apollo and Babyface can be slaved either direction over optical ([RME forum](https://forum.rme-audio.de/viewtopic.php?id=30666)); if you want the femtosecond clock as the reference, the RME feeds it.
4. **Backup / failover.** If the Apollo goes down mid-session (driver hiccup, Thunderbolt drop, hardware fault), the Babyface gets you tracking again in the time it takes to swap a USB cable. RME drivers being what they are, it's the most reliable possible insurance.

**How they connect.** The optical port is the bridge. The most common topology: **Apollo as master, Babyface slaved via optical** (ADAT/SPDIF) — confirmed as a working config on RME's own forum ([thread](https://forum.rme-audio.de/viewtopic.php?id=30666)). That also gives you ADAT expansion: the Babyface's 8 ADAT channels can fold into a larger setup, or the two boxes can share a clock so prints stay sample-accurate. Note the Babyface has **no BNC word clock** connector — all clock sync is over the optical port, so the Apollo↔RME clock link *is* the optical cable.

## 6. Use-Specific Scenarios

- **Recording the pedalboard on the go.** The Board-3 stereo print (Deco → Apollo at home) instead lands on the Babyface's two TS line inputs (channels 3–4, set to +4 dBu) or the XLR ins via DI. SteadyClock FS keeps the stereo image rock-solid; the +19/+4 dBu output switch matches whatever monitors are on hand. This is the literal "record the wall-of-sound in a hotel room" use case.
- **Banjo / DI tracking.** The Gold Tone EBM-5 or a passive banjo pickup straight into a TS instrument input (1 MΩ) gives the cleanest possible DI — and the instrument inputs are the *quietest* converters in the box (120 dBA). Re-amp later through the Radial X-Amp + EHX Effects Interface back at the studio.
- **Mic tracking on location.** SM57/SM58 on a banjo head or cab, AT2020 or KM184 on an acoustic, into the two XLR preamps. 76 dB of gain handles even the SM7-class low-output dynamics; +48V phantom for the condensers. Two channels is the ceiling without an ADAT expander — fine for solo/overdub work, not for tracking a full kit.
- **Clocking the digital rig.** With the Octatrack, Digitakt, OP-1 Field, and MPC all in play, a stable master clock matters. SteadyClock FS as the reference (digital gear chasing the RME's optical out) is a legitimate reason to power the Babyface up even when the Apollo is doing the converting.

## 7. Famous Users

RME is an engineer's-choice brand, not a celebrity-endorsement brand — so this section is honestly thin and that's the point. The Babyface Pro / Pro FS shows up constantly on the rigs of mixing and mastering engineers, classical and location recordists, and laptop-based producers who prioritize driver stability and clock quality over name recognition. RME's reputation is strongest exactly where marketing is quietest: broadcast, post, classical, and any context where "it must work every single time" outranks "it has a vibe." The brand earns loyalty through its [driver track record and long-term firmware support](https://www.soundonsound.com/reviews/rme-babyface-pro-fs) rather than artist signatures — which is precisely why it's the right *secondary* box for a studio that already has the Apollo for character.

## 8. Connectivity / Power / I/O

- **Computer connection:** **USB 2.0**, Type-B socket on the unit. Ships with both a **USB-A→B** and a **USB-C→B** cable (1m, right-angle B) per [manual](manuals/bface_pro_fs_e.pdf) §2 — so it connects to legacy and modern hosts out of the box. When plugged into a USB 3 port it negotiates down to USB 2 protocol. *(Some retail listings loosely call this "USB-C"; the connector on the interface is Type-B — the C is on the cable's computer end.)*
- **Bus power or DC:** USB bus power is sufficient (700 mA @ 5 V). Optional locking DC supply (313 mA @ 12 V) for marginal ports.
- **Optical ADAT/SPDIF:** 1 in / 1 out, TOSLINK, auto-sensing. ADAT up to 8 ch (S/MUX scales channels down as sample rate goes up); SPDIF lock range 27 kHz–200 kHz.
- **MIDI:** 1 I/O via mini-DIN breakout (2 × 5-pin DIN), optocoupler-isolated, hi-speed mode jitter typically < 1 ms.
- **Word clock:** **None via BNC** — clock sync is optical-only. This is the one I/O limitation versus rack RME units (Fireface UFX, etc.).
- **Mounting:** 3/8" thread on the underside for mic-stand mounting.

## 9. Pairing Recommendations (by name)

- **vs UA Apollo x8 — the clear split.** Apollo = main hub: Unison preamps, onboard UAD plugin DSP, more I/O, the print terminus. RME = portable, pristine, best-clocked, lowest-latency, most-reliable secondary. Apollo for character + DSP at the desk; RME for clean capture on the road, clock duty, and failover. Link them over optical; clock either direction.
- **Mics (owned):** KM184 and AT2020 into the XLR preamps for clean acoustic/banjo capture; SM57/SM58 for dynamic sources. The 76 dB gain range covers all four with headroom.
- **Re-amp (owned):** Radial X-Amp + EHX Effects Interface — track a clean DI to the RME on location, re-amp through the pedalboard back at the studio into the Apollo.
- **DAWs (owned):** Logic Pro and Ableton Live 12 both see the RME as a rock-solid Core Audio device. RME's Core Audio + ASIO drivers are the reason you'd choose this over a class-compliant-only travel box — though the Babyface *also* runs class-compliant (and as a standalone unit / for iPad) when needed.
- **As clock master:** feed SteadyClock FS to the Octatrack / Digitakt / MPC / OP-1 digital rig via the optical out, or to the Apollo as the studio reference.
- **Monitors (owned):** JBL LSR305 off the XLR outs (set to +4 dBu to keep the TotalMix fader high and noise low); headphones off either the ¼" or 3.5mm jack — the 3.5mm now drives low-impedance phones cleanly at 0.1Ω / 90 mW.

## 10. Reviews & Demos

- [Sound on Sound — RME Babyface Pro FS review](https://www.soundonsound.com/reviews/rme-babyface-pro-fs) — the authoritative written review; best on the "incremental but transparent" verdict, latency figures, and the honest TotalMix learning-curve caveat.
- [RME USA — official Babyface Pro FS page](https://www.rme-usa.com/babyface-pro.html) — manufacturer feature list and FS-vs-Pro changes (headphone op-amps, SteadyClock FS).
- [RME USA — SteadyClock FS explainer](https://www.rme-usa.com/steadyclock-fs.html) — what femtosecond clocking actually does.
- [RME Audio (DE) — Babyface Pro FS product page](https://rme-audio.de/babyface-pro-fs.html) — full European spec sheet.
- [Mixonline — real-world review](https://www.mixonline.com/technology/reviews/others/rme-babyface-pro-fs-audio-interface-a-real-world-review) — practical tracking impressions.
- [RME User Forum — Apollo x8 + Babyface Pro FS clock mode](https://forum.rme-audio.de/viewtopic.php?id=30666) — confirms the exact Apollo↔RME master/slave optical topology this rig uses.

## 11. Quirks / Known Issues

There are no *major* known issues — that's the RME reputation, earned. The honest small print:

- **TotalMix FX is the steep part.** Powerful but "somewhat impenetrable" until the three-row mental model clicks. This is the single most common new-owner frustration; it is not a bug.
- **No BNC word clock.** Clock sync is optical-only. For most rigs (including this one) optical is fine; only matters if you needed a dedicated word-clock distribution chain.
- **Two preamps is the analog ceiling.** Without an ADAT expander you have two mic channels. Fine for overdubs and stereo capture, not for multitrack drum sessions.
- **iPad app costs extra.** The TotalMix iPad control app is a paid purchase, noted as an annoyance in reviews given the price of the hardware.
- **USB-B connector** (not native USB-C on the chassis) — a non-issue functionally since both cables ship, but worth knowing if you only carry USB-C cables.
- Build quality and reliability are class-leading; no widely reported failure patterns.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Bus-powered USB 2.0 audio/MIDI interface, 24-channel (12-in / 12-out) |
| Mic/line preamps | 2 × XLR, servo-balanced, **76 dB gain in 1 dB steps**, relay PAD, +48V |
| Instrument/line inputs | 2 × ¼" TS, 1 MΩ hi-Z, +4 dBu / −10 dBV switchable |
| Line outputs | 2 × balanced XLR, +19 dBu / +4 dBu switchable |
| Headphone outputs | 1 × ¼" TRS + 1 × 3.5mm TRS, independent drivers (3.5mm: 0.1Ω, 90 mW) |
| Digital I/O | 1 × optical ADAT/SPDIF in + out (TOSLINK); ADAT 8ch@48k / 4ch@96k / 2ch@192k |
| MIDI | 1 × I/O via mini-DIN breakout (2 × 5-pin DIN), optocoupler-isolated |
| Clock | **SteadyClock FS** (femtosecond), Internal / ADAT / SPDIF; **no BNC word clock** |
| Converters | AD SNR 113.7–116 dB RMS (up to 120 dBA); DA DR 115 dB RMS (118 dBA) |
| Sample rates | 28 kHz – 200 kHz (44.1 / 48 / 88.2 / 96 / 176.4 / 192 kHz), 24-bit |
| Round-trip latency | ~3.1 ms @44.1k / 2.9 ms @96k / 2.8 ms @192k (lowest buffers) |
| DSP mixer | TotalMix FX — 288 channels, 46-bit, 3-band EQ + low cut + reverb + echo |
| Power | USB bus power (700 mA @5V) or optional locking DC (313 mA @12V); 2.8–5.4 W |
| Connection | USB 2.0 Type-B (ships with USB-A→B and USB-C→B cables); class-compliant + native drivers |
| Standalone | Yes — works as standalone converter/mixer and class-compliant (iPad) |
| Dimensions | 108 × 35 × 181 mm (4.25 × 1.4 × 7.1 in); 680 g |

Sources: [manual](manuals/bface_pro_fs_e.pdf) §27, [RME USA](https://www.rme-usa.com/babyface-pro.html), [Sound on Sound](https://www.soundonsound.com/reviews/rme-babyface-pro-fs).

## 13. Starting-Point Setups

**(a) Mobile pedalboard record** — capture the Board-3 stereo print on the road
- Stereo print → TS inputs 3/4, reference **+4 dBu**; or XLR ins via DI.
- TotalMix: hardware inputs 3/4 → record + a monitor submix to headphones. SteadyClock Internal (Master).
- Output switch +4 dBu if feeding sensitive monitors/phones. No outlet needed — pure bus power.

**(b) Pristine DI / clean front-end** — banjo or acoustic, no colour
- EBM-5 / passive banjo pickup → TS instrument input (1 MΩ), gain to taste.
- Or KM184 → XLR preamp, +48V, gain ~mid; PAD off for a quiet source.
- Track flat to Logic/Ableton; re-amp later through Radial X-Amp into the pedalboard + Apollo.

**(c) Clock master for the digital rig** — SteadyClock FS as reference
- Clock Source = **Internal** (Master). Optical out → digital gear's optical/ADAT in.
- Slave the Octatrack / Digitakt / MPC / OP-1 (or the Apollo) to the RME's clock.
- Watch the Opt LED / SyncCheck for solid green = Sync before you commit a print.

**(d) Backup-interface failover** — Apollo goes down mid-session
- Swap USB cable to the Babyface; select it as the Core Audio device in Logic/Ableton.
- Mics to XLR preamps, instrument to TS in, monitors to XLR out.
- RME drivers mean you're tracking again in under a minute. The whole reason it's in the bag.

## 14. Versus Alternatives

- **vs UA Apollo x8 (in THIS studio).** Not a competition — a division of labor. Apollo wins on I/O count, Unison preamp colour, and onboard UAD plugin DSP at tracking latency; it's the hub and the print terminus. The RME wins on portability (bus power, aluminium, coat-pocket size), clock quality (SteadyClock FS arguably beats the Apollo's clock), driver stability, lowest-buffer latency, and being utterly platform-agnostic. Use the Apollo at the desk; take the RME everywhere else and let it clock the rig. They link over optical — keep both.
- **vs UA Apollo Twin X (the portable UA).** If the question were "one portable box," the Twin X gives you Unison + UAD DSP on the road but ties you to Thunderbolt, a wall wart, and UA's driver model. The RME gives you better clock, better drivers, true bus power, and cross-platform reliability — at the cost of onboard plugin DSP. For a studio that *already owns* the Apollo x8 for DSP, the RME is the smarter second box: it covers the gaps the Apollo can't (mobility, clock, failover) rather than duplicating what it already has.
- **vs Focusrite Scarlett / MOTU M-series / Audient iD (budget portables).** These are cheaper and have more analog ins for the money, but none match RME's driver stability, clock, or lowest-latency performance — the exact things that justify the RME as a *professional* secondary rather than a consumer travel toy.
- **vs RME Fireface UCX II (the rack-format step up).** The UCX II adds more analog I/O and a BNC word clock, but loses the Babyface's pocketability and pure bus-power convenience. If the secondary role ever grew into "small mobile rack," the UCX II is the upgrade path; for "fits in the laptop bag," the Babyface Pro FS is correct.

In this rig — Apollo x8 as the colour-and-DSP hub, a digital sampler ecosystem that wants a stable clock, and a banjo/pedalboard practice of recording wherever inspiration lands — the Babyface Pro FS earns its slot specifically because it is *not* a second Apollo. It's the clean, portable, perfectly-clocked, bulletproof complement: the box that handles mobility, clocking, and failover so the Apollo can stay home being the hub.

## Sources

- [RME USA — Babyface Pro FS product page](https://www.rme-usa.com/babyface-pro.html)
- [RME USA — SteadyClock FS](https://www.rme-usa.com/steadyclock-fs.html)
- [RME Audio (DE) — Babyface Pro FS](https://rme-audio.de/babyface-pro-fs.html)
- [Sound on Sound — RME Babyface Pro FS review](https://www.soundonsound.com/reviews/rme-babyface-pro-fs)
- [Mixonline — RME Babyface Pro FS real-world review](https://www.mixonline.com/technology/reviews/others/rme-babyface-pro-fs-audio-interface-a-real-world-review)
- [RME User Forum — Apollo x8 + Babyface Pro FS clock mode](https://forum.rme-audio.de/viewtopic.php?id=30666)
- [RME User Forum — Clock Source settings for Babyface Pro](https://forum.rme-audio.de/viewtopic.php?id=33142)
- Babyface Pro FS User's Guide (PDF, local): [manuals/bface_pro_fs_e.pdf](manuals/bface_pro_fs_e.pdf)
