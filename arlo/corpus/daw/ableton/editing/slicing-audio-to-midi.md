# Slicing Audio to MIDI in Live

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Converting Audio to MIDI, Simpler; Ableton Help — *Slice to MIDI preset changes in Live 12.1*; Sound on Sound — *Re-Slicing Audio in Ableton Live*; MusicRadar Simpler tutorials
**Tags:** `daw-ableton`, `live-12`, `editing`, `slicing`, `drum-rack`, `simpler`, `sampling`, `recipe`

---

## Two Slicing Paths — Slice to MIDI Track and Simpler Slice Mode

Live offers two distinct workflows for turning a continuous audio clip into a MIDI-triggered sliced instrument: **Slice to New MIDI Track** (a one-shot command that creates a new track with a Drum Rack and a MIDI clip) and **Simpler's Slice mode** (an editable in-place slice on a single Simpler instrument). The first is the right move for re-flipping a loop into a drum-rack pattern; the second is the right move for fast slice-and-trigger work where you want the slice points to remain editable. Both are built on the same transient-detection engine and offer similar slicing options, but the resulting workflow and CPU footprint differ ([Ableton Reference Manual — Converting Audio to MIDI](https://www.ableton.com/en/live-manual/12/converting-audio-to-midi/)). This file covers both paths, the slicing modes they share, the sensitivity tuning that determines slice count, and the cross-link to the general `chopping-resampling-and-warping.md` corpus file that already covers the conceptual basics in Ableton-flavored language.

## Slice to New MIDI Track — The Command

To **Slice to New MIDI Track**: right-click an audio clip in Session or Arrangement view and select **Slice to New MIDI Track** from the context menu, or use the Create menu equivalent ([Ableton Reference Manual — Converting Audio to MIDI](https://www.ableton.com/en/live-manual/12/converting-audio-to-midi/)). A dialog appears with two choosers: the **Slicing Preset** chooser (which determines what kind of sliced instrument is created and what its macro controls do) and the **Create one slice per** chooser (which determines where the slice points are placed). When you click Create, Live builds a new MIDI track containing a **Drum Rack** with one chain per slice — each chain holds a Simpler with the corresponding audio slice loaded — plus a MIDI clip whose notes trigger each chain in the order the slices appear in the source audio. The clip plays back the original loop verbatim out of the new MIDI track; from there you can rearrange the notes, swap chains, or add processing per slice.

## The 128-Slice Limit

A Drum Rack can hold at most **128 chains**, which is the hard upper limit on slice count when using Slice to New MIDI Track. If your chosen slicing division would produce more than 128 slices, Live refuses to proceed and tells you to pick a coarser division ([Ableton Reference Manual — Converting Audio to MIDI](https://www.ableton.com/en/live-manual/12/converting-audio-to-midi/)). This matters for long source files — a 4-minute drum-loop break sliced at 1/16 produces far more than 128 slices and the command will fail. The fix is to either slice a shorter section, choose a coarser division (1/4 or 1/8 instead of 1/16), or slice at Transients (which usually produces fewer slices than a fine grid). The MIDI clip created by the command maps slice 1 to C1, slice 2 to C#1, slice 3 to D1, and so on chromatically upward — predictable and easy to re-pattern.

## The Four Slicing Modes — Warp, Transients, Beat, Region

The **Create one slice per** chooser in the Slice to MIDI dialog offers four modes ([Ableton Reference Manual — Converting Audio to MIDI](https://www.ableton.com/en/live-manual/12/converting-audio-to-midi/)). **Warp Markers** — slices land on every warp marker currently set in the source clip; useful when you've already manually placed markers at specific musical events. **Transients** — slices land on every detected transient in the source audio; this is the right default for percussive material. **Beat** — slices land on every grid division you specify (1/4, 1/8, 1/16, 1/32, plus triplet variants), regardless of what's actually in the audio; this is the J Dilla / chop-and-shuffle workflow. **Region** — slices the entire clip into a fixed number of equal-length regions you specify; useful for tonal samples where you want predictable boundaries. Beat-grid slicing is the most predictable; Transients is the most musical; Warp Markers is the most precise; Region is the most utility-oriented. Pick by source: drums get Transients or Beat, melodic stabs get Warp Markers or Region.

## Slicing Presets and Macro Mappings

The **Slicing Preset** chooser in the dialog determines what factory configuration the resulting Drum Rack uses — which macros are mapped to which Simpler parameters, and what envelopes and crossfades are pre-loaded. Live ships with a set of factory slicing presets covering common use cases (basic envelope, loop-and-crossfade, FX-applied, etc.); user presets saved into the User Library's default presets folder also appear in the chooser. Live 12.1 redesigned the entire slicing-preset set: every preset now offers **Macro Variations** and **Info Texts** for each macro, so you can recall variant macro states and read inline explanations of what each macro does without leaving the Drum Rack ([Ableton Help — Slice to MIDI preset changes in Live 12.1](https://help.ableton.com/hc/en-us/articles/17130785137820-Slice-to-MIDI-preset-changes-in-Live-12-1)). Legacy presets from before Live 12.1 are no longer in the chooser by default but can be requested from Ableton support if needed.

## Simpler's Slice Mode — In-Place Slicing

The alternative workflow uses **Simpler** directly. Drop an audio file into Simpler (drag onto an empty MIDI track, or onto an existing Simpler instance) and click the **Slice** tab in Simpler's main view ([MusicRadar — How to Chop Beats with Ableton Simpler's Slice Mode](https://www.musicradar.com/tuition/tech/how-to-chop-beats-with-ableton-simplers-new-slice-mode-632939); [FaderPro Blog — Ableton Simpler: Classic vs One-Shot vs Slice mode](https://blog.faderpro.com/instruments/ableton-simpler-modes/)). Simpler analyzes the audio for transients and presents the slices as orange vertical markers across the waveform. Each slice is playable from a chromatic MIDI note (starting at C1 by default). The advantage over Slice to New MIDI Track is that the slice points stay editable in place — you can adjust them without re-running the slicing command, and you can play the result immediately without committing to a Drum Rack. Convert to a Drum Rack later by right-clicking the Simpler title bar and selecting **Slice to Drum Rack**, which moves each slice into its own chain with independent processing.

## The Slice By Chooser in Simpler

Simpler's Slice mode has its own **Slice By** chooser with the same four options as the Slice to MIDI dialog: **Transient**, **Beat**, **Region**, and **Manual** ([MusicRadar — Simpler Slice Mode](https://www.musicradar.com/tuition/tech/how-to-chop-beats-with-ableton-simplers-new-slice-mode-632939)). Manual mode is unique to Simpler — slice points are placed only where you double-click the waveform. Double-click an existing slice marker to delete it; double-click an empty area to add one. This is the right mode when transient detection is wrong (because the source has soft onsets, swells, or no clear transients) and you want to place slice points precisely by hand. For Beat mode, set the **Division** parameter to choose grid resolution. For Region, set the **Regions** parameter to choose how many equal pieces. The slice points themselves are visible as colored markers — orange for active transient-detected slices, gray for inactive ones, white for user-added manual slices.

## Sensitivity — How It Actually Works

In Simpler's Transient slicing mode, the **Sensitivity** slider controls how many of the detected transients become active slice points ([Sound on Sound — Re-Slicing Audio in Ableton Live](https://www.soundonsound.com/techniques/re-slicing-audio-ableton-live)). At 100% Sensitivity, every detected transient is an active slice. As you lower Sensitivity, transients with progressively higher amplitude thresholds become inactive (turn gray) and adjacent slices merge into longer chunks. The discipline: start at 100%, listen to which slices are useful, then dial Sensitivity down until only the structurally important transients remain active. For drum loops with lots of ghost notes, lower sensitivity (40–60%) usually gives the cleanest playable instrument. For melodic source material, higher sensitivity is usually wrong — manual placement gets better results because the algorithm is unreliable on soft onsets. Live's Sensitivity slider is non-destructive: at any time you can drag it back up to re-activate slice points that were merged.

## Manual Marker Placement for Melodic Material

Transient detection is reliable on percussive material and progressively less reliable as the source becomes more legato. For **chord stabs, sustained vocal phrases, melodic loops, and instrumental lines** with soft attacks, manual marker placement gives the cleanest slice points because you can park each marker exactly on the note attack ([Sound on Sound — Re-Slicing Audio in Ableton Live](https://www.soundonsound.com/techniques/re-slicing-audio-ableton-live)). In Simpler's Slice mode, switch the Slice By chooser to Manual and double-click the waveform where each note begins. In the Slice to MIDI dialog, first place warp markers manually on the source clip at each note attack, then choose **Warp Markers** as the slice mode. Both paths produce a sliced instrument with musical, not algorithmic, boundaries. The same Sound on Sound article notes a useful refinement: "drag the transient a little to its left" to avoid a glitch at the end of the preceding slice — the slice point should be just *before* the attack, not on top of it.

## Playback Modes — Mono, Poly, Thru

Simpler in Slice mode offers three **playback modes** ([Studio Brootle — Ableton Simpler](https://www.studiobrootle.com/ableton-simpler/); [FaderPro Blog — Simpler Modes](https://blog.faderpro.com/instruments/ableton-simpler-modes/)). **Mono** — triggering a new slice terminates the currently playing one; useful for tight, gated drum patterns. **Poly** — slices can play simultaneously; useful when overlapping slices is musical (long-tail percussion, atmospheric sources). **Thru** — slices play through to their natural end regardless of subsequent triggers; a hybrid useful for percussion where you want the tail to ring out. There's also a **Trigger vs. Gate** toggle: Trigger plays each slice to its natural end (or until terminated by Mono mode); Gate plays a slice only while the MIDI note is held. For most drum-loop chopping, Mono + Trigger is the right default. For melodic chops where you want sustained playback, switch to Poly + Gate.

## The Convert Button — From Simpler to Drum Rack

Once a Simpler is set up in Slice mode and the slice points are right, click **Convert** (the right-click context option **Slice to Drum Rack**, or the Convert button in Simpler) to replace the Simpler with a Drum Rack where each pad holds one slice on its own chain ([Ableton Reference Manual — Converting Audio to MIDI](https://www.ableton.com/en/live-manual/12/converting-audio-to-midi/)). The conversion preserves the slice-to-note mapping (slice 1 stays on C1, etc.) so any MIDI clip playing the Simpler keeps working with the new Drum Rack. The advantage of converting: each slice now lives on its own chain with its own envelope, filter, sends, and effects rack. The trade-off: you've committed; the source-audio Simpler is replaced. Convert when you're sure the slice points are right and you want per-pad processing. Don't convert if you might want to re-edit the slice points later — Simpler is editable in place; the Drum Rack version isn't.

## Re-Flipping a Loop With the Sliced MIDI Clip

The musical payoff of slicing is **re-flipping the loop**: once the source audio is decomposed into one slice per MIDI note, the MIDI clip is editable like any other pattern. Drag notes to reorder slices; copy a slice's note to multiple positions to repeat a hit; delete notes to create gaps; duplicate the clip and pattern variations on top of the original sequence. This is the workflow that turns a sampled drum break into a new beat — the source slices stay sonically identical, but the pattern is yours. For chord-stab samples, re-flipping means triggering each chord on a different beat to build a new progression. For vocal chops, re-flipping means re-arranging vowel sounds into new phrases. The cross-link to the general corpus file `corpus/sampling/chopping-resampling-and-warping.md` covers the chop-and-flip workflow conceptually; this file is about the Ableton-specific mechanism that gets you there.

## Drum Rack vs. Simpler — Which Endpoint for Which Job

For **quick patterns where you just want playability**, Simpler in Slice mode is the lighter, faster path — no Drum Rack overhead, slice points stay editable, the workflow is one device. For **layered processing per slice**, the Drum Rack endpoint (either via Slice to New MIDI Track or via Simpler's Convert button) is the right tool — each slice gets its own chain, its own send levels, its own effects rack, and its own macro controls. For **performance use with a controller like Push 3**, the Drum Rack is the canonical choice because Push's pad grid maps cleanly to Drum Rack pads. As a working heuristic: if you only need to play the slices back as they came, stay in Simpler; if you need to process slices independently, convert to a Drum Rack. The decision is reversible until you start adding per-chain processing, at which point the Drum Rack is locked in.

## Cited Retrieval Topics

- "how do i slice a drum loop in ableton"
- "ableton slice to new midi track shortcut"
- "what's the difference between slice to drum rack and slice to simpler"
- "how do i chop a sample manually in ableton"
- "ableton simpler slice sensitivity what does it do"
- "ableton how to flip a sample loop"
- "ableton slice by transient vs beat vs region"
- "ableton drum rack 128 slice limit"
- "how do i convert a simpler slice to a drum rack"
- "ableton slice to midi presets live 12.1"

## Sources

- [Ableton Reference Manual — Converting Audio to MIDI (Live 12)](https://www.ableton.com/en/live-manual/12/converting-audio-to-midi/)
- [Ableton Help — Slice to MIDI preset changes in Live 12.1](https://help.ableton.com/hc/en-us/articles/17130785137820-Slice-to-MIDI-preset-changes-in-Live-12-1)
- [Sound on Sound — Re-Slicing Audio in Ableton Live](https://www.soundonsound.com/techniques/re-slicing-audio-ableton-live)
- [MusicRadar — How to Chop Beats With Ableton Simpler's Slice Mode](https://www.musicradar.com/tuition/tech/how-to-chop-beats-with-ableton-simplers-new-slice-mode-632939)
- [FaderPro Blog — Ableton Simpler: Classic vs One-Shot vs Slice mode](https://blog.faderpro.com/instruments/ableton-simpler-modes/)
- [Studio Brootle — Ableton Simpler](https://www.studiobrootle.com/ableton-simpler/)
- [Modul8 Online — How to use Ableton Live's Simpler Slice Mode](https://modul8online.com/how-to-use-ableton-lives-simpler-slice-mode/)

See also: `corpus/sampling/chopping-resampling-and-warping.md`, `corpus/daw/ableton/editing/warp-modes-by-ear.md`, `corpus/daw/ableton/editing/warping-discipline.md`
