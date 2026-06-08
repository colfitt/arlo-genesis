# Groove Pool and Extracted Grooves

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Grooves; Ableton Learn Live Groove Pool video; Slynk groove tutorials
**Tags:** `daw-ableton`, `live-12`, `daw-ableton-timeless`, `groove-pool`, `swing`, `humanization`, `rhythm`

---

## What the Groove Pool is

The Groove Pool is Live's project-level repository of timing templates — small files (extension `.agr`) that store **timing nudges, velocity scaling, and randomization** that can be applied to any audio or MIDI clip in the project. It opened as a dedicated panel in Live 8 ([documented historically in the Live 8 release materials](https://www.ableton.com/en/blog/)) and the implementation in Live 12 is materially the same. Open the Groove Pool from the bottom-left **Show/Hide Groove Pool** button in the Browser pane, or by pressing the small grid icon. The [Live 12 Reference Manual's Grooves chapter](https://www.ableton.com/en/live-manual/12/grooves/) documents the panel and its controls. The pool holds whatever grooves you've loaded into the current set — either from Live's bundled groove library (the Browser's **Groove Library** section, which ships with Live and includes MPC-style swing files, 16th-note shuffles, dotted-note feels, and named templates like "Logic 8C 67%") or grooves you've extracted from your own clips. Each clip in the project has a **Groove** chooser in its Clip View that points to one of the grooves in the pool — set it and the clip plays back with that timing template applied non-destructively.

## Extracting a groove from a clip

The signature workflow: take a clip whose timing you love (a sampled drum loop with a specific shuffle, a vocal phrase with idiosyncratic phrasing, a MIDI part you tapped in by hand), right-click it, choose **Extract Groove(s)**, and Live writes a new `.agr` file into the Groove Pool capturing that clip's timing and velocity pattern. The [Live 12 Reference Manual's Grooves chapter](https://www.ableton.com/en/live-manual/12/grooves/) documents this as the canonical extraction path. Slynk's [groove tutorials filmed in Live 10](https://www.youtube.com/@Slynkable) demonstrate the extraction on a sampled break: he drops in a vintage funk loop, extracts the groove, then applies that groove to a programmed MIDI drum part and the programmed part suddenly inherits the breath of the sampled break. Live 12 verification: the extraction workflow and right-click menu item still exist and behave identically. The extracted groove can then be applied to any other clip in the project. The original clip remains unchanged — extraction is read-only on the source.

## Applying a groove to other clips

Once a groove is in the pool, applying it to a clip is one click: open the clip in Clip View, find the **Groove** chooser in the Clip box, and select the groove from the dropdown. The clip will now play back with timing and velocity nudges from the groove file applied non-destructively. The Live 12 Reference Manual's [Grooves chapter](https://www.ableton.com/en/live-manual/12/grooves/) documents the parameters that control how the groove is applied per-clip: **Base** (the rhythmic grid the groove maps to — 1/16, 1/8, etc.), **Quantize** (how much the groove pulls notes toward its template), **Timing** (how much of the groove's timing variation applies — 0% means no effect, 100% means full effect, values above 100% exaggerate), **Random** (adds random timing variation), and **Velocity** (how much of the groove's velocity pattern applies). These parameters mean a single groove file can be applied subtly (Timing at 30%) or aggressively (Timing at 130%) to taste. Ableton's [Learn Live Groove Pool video](https://www.ableton.com/en/learn-live/) walks through each parameter.

## Committing a groove to a clip

Live 12 retains the classic distinction between **applied** grooves (non-destructive, the clip can revert) and **committed** grooves (destructive, the groove's timing is baked into the MIDI notes or the clip's warp markers). Commit by clicking the **Commit Groove** button in the Clip View (or right-click the clip → **Commit Groove**). The Live 12 Reference Manual notes that committing is a one-way operation in the sense that after commit, the groove chooser resets to "None" and the timing variation is now part of the clip itself. Slynk's Live 10 tutorials make this distinction explicit: commit a groove when you're done iterating and want the timing baked in for further editing in the piano roll; leave the groove non-committed when you want the freedom to swap grooves later or A/B against the straight version. A common workflow: extract a groove, apply it to a programmed MIDI part, listen for a week, decide it's right, then commit so you can manually nudge individual notes from the committed positions without the groove fighting you.

## Building a personal groove library

Veteran Live users treat the Groove Pool as a long-term resource. The discipline: every time you find a sampled loop or human-performed clip whose timing feels great, extract the groove and save the `.agr` file into the User Library. The [Live 12 Reference Manual's Library chapter](https://www.ableton.com/en/live-manual/12/library/) documents the User Library structure; the **Grooves** subfolder is where personal `.agr` files live. Right-click the groove in the Groove Pool → **Save** sends it to the User Library. Name the file descriptively: `funk-break-92bpm-heavy-shuffle.agr`, `tatum-pushed-snare.agr`, `jdilla-vibe-around-90bpm.agr`. Over a few years this library becomes one of the most personal things a Live user owns — your library of timing feels, ready to apply to any new project. Ill Gates teaches this practice as part of his Producer DJ courses; the [Live 12 Library](https://www.ableton.com/en/live-manual/12/library/) makes the persistence automatic across projects once the `.agr` files are in the User Library.

## Groove Pool vs. straight quantization

The reason Groove Pool exists: rigid quantization to a grid kills feel. Programmed drums quantized to a straight 16th grid sound like programmed drums. A groove file lets you keep MIDI's edit-ability (you can still edit individual notes in the piano roll) while inheriting **micro-timing variation from a sampled break or a humanly-performed clip**. The Live 12 Reference Manual's [MIDI Editing chapter](https://www.ableton.com/en/live-manual/12/midi-arrangements/) lets you Quantize-to-Groove via the Quantize dialog (right-click a clip → **Quantize** → enable **Groove Quantization**). The choice: hard-quantize (notes snap to the grid), groove-quantize (notes nudge toward the groove's template), or apply-groove (notes stay where they are, the Groove parameters adjust playback). Each has its uses. Hard quantization for EDM kicks. Apply-groove for everything else. Slynk's [groove tutorials](https://www.youtube.com/@Slynkable) demonstrate the A/B side-by-side: same MIDI, hard-quantized vs. groove-applied — the difference is obvious in seconds.

## How the Timing parameter actually works

The **Timing** parameter on a groove is the most-tweaked knob in the Groove Pool. At 0% the groove has no effect. At 100% the groove's timing is fully applied. At 130% the timing variation is **exaggerated** — notes that were nudged forward 20 ticks in the groove file get nudged forward 26 ticks. Values above 100% produce dramatic micro-timing differences that don't exist in the source groove. The Live 12 Reference Manual documents this in the [Grooves chapter](https://www.ableton.com/en/live-manual/12/grooves/). The discipline: start at 100% and listen, then dial down to 50% or up to 130% based on whether you want the groove subtler or more pronounced. The Velocity and Random parameters work similarly. Mr. Bill has demonstrated the Timing parameter as a creative tool in [his Live 11 streams](https://www.mrbill.com.au/) — applying a heavy shuffle groove at 30% Timing to a four-on-the-floor kick adds just enough drag to feel human without obviously shuffling.

## The classic MPC-feel use case

The bundled Groove Library ships with MPC-style swing files (`MPC-16-Swing-50.agr` through `MPC-16-Swing-75.agr`) that recreate the legendary feel of Akai MPC hardware swing percentages. These are the most-applied grooves in the bundled library because they map a familiar concept (MPC swing 58% = light hip-hop shuffle, MPC swing 62–67% = heavy boom-bap feel) onto Live MIDI clips. The [Live 12 Reference Manual's Grooves chapter](https://www.ableton.com/en/live-manual/12/grooves/) confirms the bundled MPC files persist in Live 12. The workflow: program straight 16th-note hats, apply MPC-16-Swing-58 at 100% Timing, the hats now shuffle to taste. Slynk's beat-making tutorials in Live 10 use this exact move repeatedly. Live 12 verification comes from any current Live 12 hip-hop tutorial — the MPC files are still bundled and still applied this way.

## Groove for non-drum elements

The Groove Pool isn't drum-only. Apply a swing groove to a hi-hat pattern, fine — but apply the same groove to the bass line and the kick stays straight while the bass shuffles, producing the classic interlocking funk-groove pattern. Apply a groove to a pad line and the chord changes nudge slightly off-grid, adding human feel to programmed harmony. Mad Zach's [Live 10 tutorials](https://www.youtube.com/@madzach) walk through grooving non-drum elements. The Live 12 Reference Manual's [Grooves chapter](https://www.ableton.com/en/live-manual/12/grooves/) doesn't restrict grooves to specific track types — any clip with a Groove chooser (which is every audio and MIDI clip in Live) can have a groove applied. The practical discipline: apply different grooves to different elements deliberately. The kick and snare on the strict grid for stability, the hats with MPC swing 58% for pocket, the bass with a half-applied snare-pushed groove for drag, the pads with extracted-from-clip groove for breath. The result feels human without being sloppy.

## Common Groove Pool mistakes

The mistakes that show up in forum-triangulation searches for "groove pool not working": (1) The Groove parameter on the clip is set to None — the groove file in the pool isn't applied to the clip until the clip's Groove chooser is set. (2) The Base parameter is set to the wrong grid — apply a 1/16-based groove to a 1/8-based clip and the timing nudges land in the wrong places. (3) The clip is hard-quantized after applying a groove, snapping notes back to the grid and erasing the groove's effect. (4) Hot Swap is loading a groove from outside the User Library and the file moves break the link in the project file. (5) The Timing parameter is at 0%, applying the groove with zero effect. The [Live 12 Reference Manual's Grooves chapter](https://www.ableton.com/en/live-manual/12/grooves/) covers each of these as part of its parameter documentation. Walk through them when a groove isn't audibly applying.

## Workflow recipe — give a programmed beat human feel

A complete recipe for adding feel to a programmed beat: (1) Program your kick/snare/hat pattern on a straight 16th grid in a MIDI clip. (2) Drag a reference loop with the feel you love into a second track (a Dilla beat, a Questlove break, a Madlib loop — any sampled loop with strong timing character). (3) Right-click the reference clip → **Extract Groove**. The groove appears in the Groove Pool. (4) Open the programmed MIDI clip, set the Groove chooser to the extracted groove. (5) Set Timing to 100%, Velocity to 50%, Random to 0%, Base to 1/16. (6) Listen. Adjust Timing down to 60–80% if the effect is too dramatic, or up to 120% if you want exaggeration. (7) When you've got the right amount, click **Commit Groove** on the clip if you want to bake it in, or leave non-committed if you want the freedom to A/B. The programmed beat now has the reference's pocket. The [Live 12 Reference Manual's Grooves chapter](https://www.ableton.com/en/live-manual/12/grooves/) and Slynk's [Live 10 groove tutorial](https://www.youtube.com/@Slynkable) both document this recipe.

## Cited Retrieval Topics

- "how do i use the groove pool in ableton"
- "how do i extract a groove from a sample"
- "what's the difference between groove and quantize in ableton"
- "how do i make my programmed beat feel more human"
- "ableton groove pool timing parameter"
- "how do i apply mpc swing in ableton"
- "ableton commit groove"
- "where is the groove pool in live 12"
- "how do i save a groove to my library"

## Sources

- [Ableton Live 12 Reference Manual — Grooves](https://www.ableton.com/en/live-manual/12/grooves/)
- [Ableton Live 12 Reference Manual — MIDI Arrangements / Editing](https://www.ableton.com/en/live-manual/12/midi-arrangements/)
- [Ableton Live 12 Reference Manual — Library](https://www.ableton.com/en/live-manual/12/library/)
- [Ableton Learn Live — Groove Pool video tutorials](https://www.ableton.com/en/learn-live/)
- [Ableton Blog — Live 8 launch (Groove Pool original introduction)](https://www.ableton.com/en/blog/)
- [Slynk — YouTube channel (groove tutorials, Live 10 era)](https://www.youtube.com/@Slynkable)
- [Mad Zach — YouTube channel (groove-applied-to-non-drum tutorials, Live 10 era)](https://www.youtube.com/@madzach)
- [Mr. Bill — official site (groove streams, Live 11 era)](https://www.mrbill.com.au/)
- [Ill Gates — Producer DJ courses (groove library discipline)](https://illgates.com)

## See also

- `corpus/rhythm/groove-construction-and-pocket.md`
- `corpus/rhythm/drum-programming-by-genre.md`
- `corpus/daw/ableton/timeless/velocity-randomization-and-humanization.md`
- `corpus/daw/ableton/live-12/midi-generators-and-transformations.md`
- `corpus/daw/ableton/editing/warp-modes-by-ear.md`
