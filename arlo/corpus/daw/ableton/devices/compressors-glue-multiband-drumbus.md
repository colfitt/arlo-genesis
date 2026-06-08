# Ableton's Compressors — Compressor, Glue, Multiband, Drum Buss

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Compressor, Glue Compressor, Multiband Dynamics, Drum Buss
**Tags:** `daw-ableton`, `live-12`, `device`, `compression`, `glue-compressor`, `drum-buss`, `mixing`

---

## The four-compressor lineup in Live 12

Live 12 ships four core dynamics processors that cover almost every routine compression job: **Compressor** (the general-purpose workhorse), **Glue Compressor** (SSL G-style bus comp, co-developed with Cytomic), **Multiband Dynamics** (three-band upward/downward compression and expansion, mastering-oriented), and **Drum Buss** (one-knob drum-bus processor introduced in Live 10 with combined transient shaping, saturation, and resonant low-end). They sit alongside the **Gate** device (covered in B5) and the newer **Roar** for distortion-heavy dynamic shaping (B6). The choice between them is a question of source-and-position, per the [Ableton Live 12 Reference Manual — Audio Effect Reference](https://www.ableton.com/en/manual/live-audio-effect-reference/): individual tracks usually get Compressor; the drum bus gets Glue or Drum Buss; the mix bus gets Glue; mastering gets Multiband for surgical band-by-band work. Knowing which to reach for first is the highest-leverage decision when building a chain.

## Compressor: detection modes and the three model curves

The stock **Compressor** offers two detection modes — **Peak** and **RMS** — selected at the right side of the device. Peak detection responds to short transient peaks and is the right choice when you need transient control (snare smacks, plosives, percussive bass). RMS detection averages level over a short window and is closer to perceived loudness; it sounds more musical on sustained sources (vocals, pads, bass body). Compressor also exposes three internal model curves selected as **FF1**, **FF2**, and **FB** in the device chooser. FF1 is the original Live-9-era feed-forward model; FF2 is a refined feed-forward design with cleaner transient response; FB is a feedback-style topology that emulates older analog units and tends to sound smoother and rounder at high gain reduction, per discussion on the [Ableton Forum FF/FB thread](https://forum.ableton.com/viewtopic.php?t=58887). The working rule: FF2 for transparent control, FB for color and "glue" on individual tracks.

## Compressor: knee, lookahead, and envelope follower

The **Knee** control sets how gradually compression engages as input level approaches threshold. At 0 dB it is a hard knee (compression engages abruptly at threshold), and with higher (or "soft") knee values the compressor begins compressing gradually as the threshold is approached — per the [Ableton Live 12 Reference Manual — Compressor](https://www.ableton.com/en/manual/live-audio-effect-reference/), "with a 10 dB knee and a -20 dB threshold, subtle compression will begin at -30 dB and increase so that signals at -10 dB will be fully compressed." Soft knees sound more natural on sustained material; hard knees catch transients more precisely. **Lookahead** offers three settings — **0 ms**, **1 ms**, and **10 ms** — which let the compressor "see" peaks slightly before they arrive at the gain-reduction stage. 10 ms lookahead is the choice for peak limiting where missed transients are unacceptable; 0 ms is the choice when you need zero added latency. The envelope-follower shape can be set to **Linear** (Lin) or **Logarithmic** (Log), affecting how release curves taper.

## Compressor: sidechain and Expand mode

The Compressor's **Sidechain** panel (toggled with the unfold button) provides external sidechain routing — pick any track as the trigger source — plus a built-in sidechain EQ with selectable filter types so you can have the compressor key on, say, only the kick's fundamental without the cymbal bleed triggering ducks. This is the canonical ducking architecture, and is the older classical approach that the Envelope Follower modulator (Live 12+) now offers an alternative to (covered in D2). The compressor also has an **Expand** mode, accessed via the ratio chooser, that flips the compression curve into an upward expander — useful for restoring snare crack or adding life back to over-compressed material, though most users never reach for it.

## Glue Compressor: the SSL-style bus workhorse

**Glue Compressor** is an emulation of the SSL G-series bus compressor, co-developed with Cytomic, per practitioner references at [Black Ghost Audio](https://www.blackghostaudio.com/blog/how-to-use-sidechain-compression-in-ableton). It is the routine reach for drum-bus and mix-bus glue compression. Glue exposes a deliberately small parameter set: **Threshold**, **Ratio** (three discrete steps: **2:1**, **4:1**, **10:1**), **Attack** (six discrete steps: **0.01**, **0.1**, **0.3**, **1**, **3**, **10 ms**), **Release** (five discrete steps plus **Auto**: **0.1**, **0.2**, **0.4**, **0.6**, **1.2 s**, and **Auto**), **Makeup** gain, **Soft** clipper, and **Dry/Wet**. The discrete steps are not a bug — they mirror the original SSL unit, which made dialing in "the right setting" a matter of choosing between a handful of musical options rather than micromanaging a continuous knob. Auto release is the safest default on a busy mix bus, per the [Music Guy Mixing Glue Compression article](https://www.musicguymixing.com/glue-compression/), because it adapts the release time to incoming program material.

## Glue Compressor: the Soft clipper and Range

The **Soft** switch enables a soft-clipping limiter at the output stage — when on, peaks above 0 dBFS are gently shaped rather than hard-clipped, which is the routine choice for letting Glue do mild peak control without an additional limiter. The **Range** parameter sets the maximum amount of gain reduction Glue will apply, in dB — useful for parallel-bus situations where you want the comp to engage clearly but cap its squash, and for sidechain ducking depth control. The sidechain section offers external input with sidechain EQ identical in concept to Compressor's. Glue's character is most apparent at 2:1 with slow attack and Auto release on the drum bus: 1–3 dB of gain reduction adds cohesion and a subtle "snap" to the transients that producers describe as the SSL "glue" — the cumulative reason the device is on so many shipped records.

## Multiband Dynamics: three bands, bi-directional thresholds

**Multiband Dynamics** is Live's per-band dynamics processor — three bands (Low, Mid, High) with adjustable crossover frequencies, each capable of both compression and expansion simultaneously. Per the [Ableton Live 12 Reference Manual — Multiband Dynamics](https://www.ableton.com/en/manual/live-audio-effect-reference/), each band has **upper (T Above)** and **lower (T Below)** thresholds. Signal above the upper threshold is compressed downward; signal below the lower threshold is processed independently — you can either expand it downward (gating-like) or upward (expansion to add life). This gives six independent dynamic processes per device. Crossover frequencies are dragged in the display or set with the **L-M** and **M-H** knobs. The routine setup for full-mix work: L-M crossover around 200–250 Hz to isolate bass from mids, M-H crossover around 2.5–4 kHz to isolate presence from body, per [PCAudioLabs' Multiband Dynamics tutorial](https://pcaudiolabs.com/how-to-use-the-ableton-live-multiband-dynamics-audio-effect/).

## Multiband Dynamics: typical mastering uses

Three classic Multiband Dynamics moves recur on shipped records. **First**, a gentle downward compression on the low band only (T Above active, ratio ~2:1) tames bass-bus bloat without affecting the rest of the spectrum. **Second**, downward expansion (T Below active in expand mode) on the mid band acts as a dynamic de-cluttering tool — quiet midrange detail is pulled down further while loud midrange stays present, opening space. **Third**, upward compression on the high band (T Below in upward mode) adds presence to quiet top-end content without slamming the loud parts. Multiband Dynamics is not as visually friendly as iZotope Ozone or FabFilter Pro-MB, but it is fully featured for routine mastering work and integrates with Live's automation and Modulators.

## Drum Buss: the one-knob drum bus

**Drum Buss** is Live's one-stop drum-bus processor, introduced in Live 10. Per the [Ableton Live 12 Reference Manual — Drum Buss](https://www.ableton.com/en/manual/live-audio-effect-reference/) and Liveschool's [Drum Buss tutorial](https://blog.liveschool.net/ableton-live-tutorial-enhancing-loops-drum-buss/), its sections are: **Trim** (input gain), **Comp** (a fixed-character compressor toggle), **Drive** (saturation amount), **Drive mode** (three distortion characters: **Soft** for waveshaping, **Medium** for limiting-style distortion, **Hard** for clipping with bass boost), **Crunch** (sine-shaped distortion that adds mid-high presence to claps and snares), **Damp** (a low-pass filter at the output to tame top-end harshness from the saturation), **Transients** (a transient shaper from -1 to +1 emphasizing attack at one extreme and sustain at the other), **Boom** (a resonant low-end enhancer with frequency from **30 Hz to 90 Hz** and a separate Decay), and **Dry/Wet**. The Comp toggle adds a non-adjustable compressor that just engages or bypasses.

## Drum Buss: the working recipe

The routine Drum Buss starting point is well-documented: Drive 10–25% on Soft mode for cohesion without obvious distortion; Crunch 5–15% for added snare/clap crack; Transients slightly negative for compression-like glue or slightly positive for snappier hits; Boom 15–30% with frequency tuned by ear to a fundamental of the kick (often 50–70 Hz); Damp to control any added top-end harshness. The [MusicTech Drum Buss tutorial](https://musictech.com/tutorials/using-the-new-drum-buss-in-ableton-live/) describes Boom as "a resonant filter tuned to a low frequency" — its character is sub-add rather than EQ-style boost, so it benefits drums lacking weight more than it benefits drums with already-dense low end. Drum Buss is bus-only — its character compounds badly on full mixes — and is not a substitute for a serious mix-bus compressor like Glue.

## Which compressor on which source

The working defaults distilled from shipping records and Ableton-Certified-Trainer content:

- **Individual vocals, bass, synths, guitars** → **Compressor** (FF2 or FB, Peak or RMS by source character)
- **Drum bus** → **Drum Buss** for character-forward processing, **Glue** for transparent SSL-style glue, or both in series with Drum Buss first
- **Instrument-group busses (vocal stack, synth stack)** → **Glue** at 2:1, slow attack, Auto release, 1–3 dB GR
- **Mix bus** → **Glue** at 2:1 or 4:1, similar settings — the classic mix-bus comp move
- **Mastering** → **Multiband Dynamics** for band-by-band control; Glue at the end for final glue
- **Sidechain ducking** → **Compressor** with external sidechain (the classic way) or the **Envelope Follower** modulator (the Live-12 way — see D2)

## Common compressor mistakes in Live

Three recurring failure modes. **First**, leaving Compressor on FF1 model out of habit when FF2 sounds cleaner on most modern material — old presets default to FF1 and many users never change it. **Second**, treating Glue Compressor like a continuous parametric (trying to dial in a "perfect" attack between 0.1 and 0.3) — the discrete steps are deliberate; pick the step that sounds right and adjust threshold and ratio to taste. **Third**, putting Drum Buss on a full mix or a single drum (kick, snare): it is bus-only by design, and on a single source it sounds heavy-handed compared to source-specific processing. Drum Buss wants two or more drum elements summing into it.

## Cited Retrieval Topics

- "what compressor should i use on the drum bus in ableton"
- "ableton glue compressor settings for mix bus"
- "what's the difference between ff1 ff2 and fb on ableton compressor"
- "how to set up drum buss for kick and snare"
- "ableton multiband dynamics for mastering"
- "ableton compressor peak vs rms detection"
- "how to use sidechain compression in ableton"
- "drum buss boom frequency how to tune"
- "glue compressor auto release when to use"
- "ableton compressor knee setting explained"

## Sources

- [Ableton Live 12 Reference Manual — Live Audio Effect Reference](https://www.ableton.com/en/manual/live-audio-effect-reference/)
- [Ableton Forum — Peak Detecting & RMS Feedback & Feedforward Compressor](https://forum.ableton.com/viewtopic.php?t=58887)
- [Music Guy Mixing — Glue Compression: What is It and How to Use It](https://www.musicguymixing.com/glue-compression/)
- [PCAudioLabs — How to Use the Ableton Live Multiband Dynamics Audio Effect](https://pcaudiolabs.com/how-to-use-the-ableton-live-multiband-dynamics-audio-effect/)
- [Liveschool — Processing Drum Loops with Live's Drum Buss](https://blog.liveschool.net/ableton-live-tutorial-enhancing-loops-drum-buss/)
- [MusicTech — Crunch and Punch: Using the New Drum Buss in Ableton Live](https://musictech.com/tutorials/using-the-new-drum-buss-in-ableton-live/)
- [Black Ghost Audio — How to Use Sidechain Compression in Ableton](https://www.blackghostaudio.com/blog/how-to-use-sidechain-compression-in-ableton)
- [Seed to Stage — Ableton Live Glue Compressor Advanced Techniques](https://seedtostage.com/advanced-techniques-with-ableton-glue-compressor/)

See also: [`corpus/mixing/compression-fundamentals.md`](../../../mixing/compression-fundamentals.md), [`corpus/mixing/low-end-management.md`](../../../mixing/low-end-management.md), [`corpus/rhythm/kick-bass-relationship.md`](../../../rhythm/kick-bass-relationship.md)
