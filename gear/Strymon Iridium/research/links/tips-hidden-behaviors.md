https://www.strymon.net/support/iridium/ + https://www.strymon.net/faq/how-do-you-connect-to-iridium/ + product page + community
strymon.net official + community reports · undated (current 2026)

# Power-user tips & hidden behaviors (consolidated)

**LEVEL TRIM (global volume that doesn't touch your preset).** A global output-level adjustment for both 1/4" out and headphone out that does NOT alter the level saved into a Favorite/preset. Use it to match room/interface gain without re-saving every preset. (Made persistent through power cycles in firmware 1.32.)

**Input Level: Instrument vs Line (the clipping trap).** Default = Instrument (-10 dB, guitars & basses). A hot/line source — loud pedalboard, JHS Colour Box V2, or the VG-800 line out — will clip the front end unless you switch to **LINE (+4 dB / +10 dB headroom)**. Set via power-up mode. Max input +8 dBu either way. Single easiest mistake to make when feeding it anything but a raw guitar.

**Buffered bypass needs power.** Bypass is buffered, not true — Iridium must be powered to pass ANY signal. If it loses power mid-set, signal stops. Relevant for failover/live; on the bench it's moot.

**Power is thirsty — don't daisy-chain.** 9 VDC center-negative, **500 mA minimum**. Underpowering causes glitches/dropouts. Needs a dedicated high-current isolated supply slot. Supply not included.

**Room IR is fixed.** You can change room SIZE (small/med/large, via hold-ON + ROOM) and LEVEL, but the ~256 ms room IR itself is NOT user-replaceable (unlike the 9 cab slots). For long ambient tails, keep ROOM modest and let downstream reverbs do the work — the room can sound boxy if pushed.

**AMP DISABLE as a general convolution box (firmware 1.32+).** Run cab + room on ANY source — synth, drum bus, bass, line input. IDLES' Mark Bowen literally cabs his drummer's signal through Iridiums (see artist file). Combined with loading ANY 24/96 WAV (bass cabs, acoustic-body resonance, even music samples per manual p.5) as an "IR," the Iridium becomes a small standalone convolution processor, not just a guitar-cab loader.

**Stereo-IR widening trick.** Load a DIFFERENT IR into LEFT vs RIGHT of one cab slot (Impulse Manager) — "huge effect on the tone… warm and punchy to bright and cutting" and a wider stereo image. Per-channel LEVEL/TREBLE/BASS via the slot Info button (un-check "Match left channel"). Ideal for a wide drone/wall pad: dark cab L + bright cab R.

**EXP jack is one jack, many jobs.** Volume pedal (pre/post amp) | knob-morph between two settings | MultiSwitch Plus = 3-preset footswitching (no MIDI) | MIDI EXP cable / TRS-MIDI adapter = full 300-preset MIDI. Pick ONE function per power-up. MIDI output mode can be set to THROUGH to daisy-chain Iridium in a MIDI string.

**Headphone out = latency-free monitor.** Front 1/8" stereo, voiced for 25–70 Ω phones, shares main signal, LEVEL controls it. Monitor yourself on phones while OUT L/R feeds FOH/interface.

**Firmware via Nixie 2.x.** Current = Rev 1.33 (Nov 2024); updating now uses the Nixie 2.x app (needs Nixie 2.2.0+). Must-have baseline is 1.32 (AMP DISABLE + persistent LEVEL TRIM).
