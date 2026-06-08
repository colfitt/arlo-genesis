# Groove Construction and Pocket

**Scope:** rhythm
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** Dennis DeSantis, *Making Music* (in seed); Attack Magazine *Secrets of Dance Music Production*; Ableton Live Reference Manual
**Tags:** `rhythm`, `groove`, `pocket`, `swing`, `humanization`, `drums`, `recipe`

---

## What "groove" and "pocket" actually mean

"Groove" is the felt repetition of a rhythmic pattern — the sensation that the music wants to move you. "Pocket" is the slightly narrower idea that all the rhythm-section players are agreeing on the same micro-timing reference, so the music sounds locked rather than aligned-but-stiff. As [Bobby Owsinski writes](https://bobbyowsinskiblog.com/groove-pocket/), the pocket is what happens when the drummer and bassist are "locked in together jamming a groove while the rest of the band is doing their own thing." [Sweetwater's "Playing in the Pocket" feature](https://www.sweetwater.com/insync/playing-in-the-pocket/) emphasizes that the effect is enhanced by **interlocking parts, not unison parts** — the kick and bass that share rhythmic DNA but stay off each other's exact hits feel deeper than the kick and bass that double every note. The practical implication for programmers: the goal is never "every part on the grid" — it is "every part referenced to the same pulse, with intentional displacement against that pulse."

## The kick/snare/hi-hat backbone tells you the genre

Almost every contemporary genre's identity is announced by where the kick sits relative to the snare and what subdivision the hi-hat reinforces. Four-on-the-floor (kick on every quarter, hat on the off-eighth) reads as house and most modern dance pop. Kick on 1 and 3, snare on 2 and 4, with straight-eighth hats reads as rock. Kick on 1 and the "and-of-3" with snare on 2 and 4 and 16th-note hats reads as boom-bap hip-hop. Trap inverts the kick pattern entirely — sparse, syncopated kicks plus a snare or clap on 3, with hi-hats running 16th-note (and 32nd-note rolls) trills. Per [DrumLoopAI's funk-groove guide](https://www.drumloopai.com/blog/funk-drum-pattern/) and [DRUM! Magazine's ghost-note lesson](https://drummagazine.com/lesson-ghost-note-style-and-placement/), funk specifically lives in the snare's *quiet* events between the backbeats — ghost-note 16ths that hint at the underlying pulse without competing with 2 and 4. The skeleton you choose for those three voices is the loudest signal your beat sends about what kind of song it is.

## Ghost notes: the snare drum's pocket builder

A ghost note is a quiet snare stroke played between the accented backbeats — typically at velocities **15–35 (on the 0–127 MIDI scale)** vs. the **100–115** of the main backbeat. [DRUM! Magazine](https://drummagazine.com/lesson-ghost-note-style-and-placement/) describes them as "subtle, quiet strokes that fill in the spaces between the louder, primary beats," and [the Percussive Arts Society's ghost-note funk lesson](https://pas.org/pas-blog/groove-of-the-month-ghost-note-funk/) notes that they sit "1.5 inches above the drumhead" in real performance — the programmer's analog is dramatically lower velocity. In a 16th-note funk groove with kick on 1 and 3 and snare on 2 and 4, ghosts commonly fall on the **"e" and "a" of every beat** — the 16ths between the accented hits — at varying low velocities so that no two consecutive ghosts are identical. The job of a ghost is to make the listener feel the 16th-note pulse without explicitly hearing it; the rule [Connor McCorkindale](https://connormccorkindaledrums.co.uk/blog/beginners-guide-to-developing-ghost-notes) gives drummers applies equally to MIDI programming: "treat ghost notes like glue rather than decoration."

## Micro-timing: pushing and pulling specific elements

Pushing a part means landing it a few milliseconds *ahead* of the grid; pulling means landing it a few milliseconds *behind*. Per [MusicRadar's push/pull tutorial](https://www.musicradar.com/tuition/tech/how-to-push-or-pull-drum-tracks-to-increase-or-reduce-urgency-639436), **5 ms and 10 ms are the two most effective offset amounts; beyond ~20 ms the part starts to sound out of time rather than expressive**. Common professional moves: snare pulled 5–10 ms late for laid-back R&B and neo-soul; hats pushed 3–7 ms early for urgent indie and rock; bass pulled slightly behind the kick to "fall onto" each downbeat in classic-soul productions. The reference timing — what you measure all the offsets against — is whatever element you decide is the song's metronome. In most programmed productions the kick is the reference because it's the most felt; everything else gets nudged relative to it. The cardinal rule from [Sweetwater](https://www.sweetwater.com/insync/playing-in-the-pocket/): differences as short as 5 ms are perceptible, so commit to which element is "on" and which is displaced, and be consistent.

## Swing percentages: the Roger Linn framework

Roger Linn's MPC swing — the most influential groove-encoding ever shipped — describes the delay applied to even-numbered 16th notes as a ratio. Per Linn's own explanation in [Attack Magazine](https://www.attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/): **50% is straight time; 66% is perfect triplet swing (the second 16th lands on the 8th-note triplet); 75% is the maximum, a hard shuffle**. Between those endpoints sit the magic numbers: Linn specifically calls out **54% as the "loosens straight 16ths without sounding like swing"** setting and **62% as looser-than-perfect at 90 BPM**. For classic boom-bap hip-hop on a real MPC, [the MPC Forums consensus](https://www.mpc-forums.com/viewtopic.php?f=4&t=192879) clusters around **54–58%**. The triplet/shuffle territory (62–68%) is more associated with neo-soul and the broader "Dilla feel" tradition. As [Melodiefabriek's MPC-Swing-in-Reason guide](https://melodiefabriek.com/blog/mpc-swing-reason/) catalogs, modern DAWs implement the same math but expose it through different UIs — Ableton's groove pool, Logic's swing, Reason's shuffle.

## The "Dilla feel": handle with care

The microtiming of J Dilla's MPC programming is widely studied but hard to pin to a single swing-percentage value, and the literature should be read cautiously. [Brian Powell's brltheory analysis](https://www.brltheory.com/analysis/dilla-part-ii-theory-quintuplet-swing-septuplet-swing-playing-off-the-grid/) argues that Dilla's signature feel is not a uniform shuffle setting but a *deliberate inconsistency* — hi-hats referenced to one subdivision (quintuplet swing), kicks referenced to another (septuplet swing), snares slightly early, kicks slightly delayed. The qualitative summary is reliable: **Dilla blends straight and swung notes within the same bar, often plays kicks loose enough that no preset swing-% reproduces them, and resists quantization deliberately**. The qualitative summary is what to internalize. The specific numbers — "Dilla's hats were at 58%, his kicks at 62%" — are not measurements you can find in primary literature, and you should not program them as facts. The reliable production move inspired by Dilla is to **leave the kick un-quantized** while keeping snare and hats locked, which produces the looseness without requiring a measurement.

## Groove templates: extracting feel from a reference

Every modern DAW supports importing the timing/velocity profile of one performance and applying it to another. In [Ableton Live](https://www.ableton.com/en/manual/using-grooves/), this is the Groove Pool: drag any audio or MIDI clip into the pool to extract its groove, then apply it to other clips via the Groove dropdown in clip view. The four Groove parameters that matter: **Timing (how strongly notes are pulled to the groove's positions, 0–130%); Random (humanization, normally kept low — 1–10%); Velocity (how strongly the groove's velocity profile is imposed, ±100%); Base (the grid resolution against which positions are compared — 1/4, 1/8, 1/16, with triplet variants)**. The workflow that works in practice: extract a groove from a commercial reference (a loop in the same genre), apply it to your programmed drums at **50–70% Timing strength**, leave Random at **0–5%**, and adjust Velocity to taste. This is the modern equivalent of an MPC user dialing in 56% swing by ear.

## DAW groove implementations side by side

The same idea lives in every DAW under different names. **Ableton Live**: Groove Pool with Timing, Random, Velocity, Base — covered in the [Ableton Live Reference Manual](https://www.ableton.com/en/manual/using-grooves/). **Logic Pro**: per the [MacProVideo Logic humanize guide](https://www.macprovideo.com/article/audio-software/7-ways-to-humanize-beats-and-midi-regions-in-logic-pro-x), the Q-Swing slider in the inspector plus the MIDI Transform > Humanize function (randomizes position, velocity, length). **FL Studio**: per-channel Shift and the Swing knob in the step sequencer. **Cubase**: the Iterative Quantize and Groove Quantize functions. **Pro Tools**: Groove Quantize with templates. The lesson is that **groove is mostly a question of timing-offset values and velocity profiles**, and every DAW exposes those two surfaces; the UI differences matter less than understanding which knob does which job.

## The "humanize" knob and what it actually does

The humanize function in most DAWs applies a **small random offset to note start time, velocity, and (in some implementations) note length**. The risk is that *random* is the opposite of *grooved* — a robotic 16th-note hi-hat humanized by ±15 ticks doesn't sound human, it sounds drunk. [Splice's humanize-your-drums guide](https://splice.com/blog/humanize-your-drums/) recommends extremely small values — **±5–10 ticks of timing (where 480 ticks = quarter note in Logic, or about 1–2 ms at 120 BPM), and ±10 velocity** for natural-sounding variation. The better workflow is to randomize *velocity only* and leave timing alone — then if timing variation is needed, apply a Groove Template (which adds *consistent* timing offsets) rather than random ones. As [Black Ghost Audio](https://www.blackghostaudio.com/blog/5-ways-to-humanize-your-productions) notes, the goal is "anti-robotization," not "anti-precision." Random alone never sounds human; structured displacement plus light random velocity does.

## Velocity programming for natural-feel hats and snares

A continuously hit 16th-note hi-hat at velocity 100 sounds like a machine. Real drummers can't physically play every hit the same; the natural alternating-stick pattern produces an accent pattern. The professional move is to **place accents on the downbeats (velocity 100–115), underscored beats at velocity 80–90, off-beats at velocity 60–75, and the "in-between" 16ths at velocity 45–60**. For snare, the accented backbeats sit at 100–120 while the ghost notes drop to 15–35. As [Splice's humanize guide](https://splice.com/blog/humanize-your-drums/) notes, this velocity programming alone — with no timing variation at all — gets a programmed beat 80% of the way to feeling live. Use the DAW's velocity randomization on top of (not instead of) a designed accent pattern.

## The kick-bass interlock as a separate skill

The pocket isn't just about drums — it's specifically about how the bass and kick relate. As [Sweetwater](https://www.sweetwater.com/insync/playing-in-the-pocket/) and [Owsinski](https://bobbyowsinskiblog.com/groove-pocket/) both emphasize, the pocket lives in the bass-and-kick relationship, with the drummer's job to "stay out of the bassist's way." Common interlock patterns: **bass plays on every kick hit and one or two off-beats** (locks the low end tightly); **bass plays the kick rhythm offset by one 16th** ("bass on the and" — creates motion); **bass holds long notes that span multiple kicks** (the dub and reggae approach, lets the kick punch through silence). The kick-and-bass-relationship file covers the frequency-domain side of this; from a rhythm-construction standpoint, the rule is to **decide which element is the metronome and which one references it**, the same as with snare-vs.-kick micro-timing.

## Quantize less, design more

The most common failure mode in beat programming is to record sloppy MIDI, hit "quantize 100%," and call it done — which kills any micro-timing nuance that survived the recording. The opposite failure is to leave the recording at 0% quantize and call the resulting drift "groove." The professional middle path: **quantize hard-on-the-grid for elements that should be metronomic (kick on a four-on-the-floor, the downbeat-snare backbone), then leave or partially-quantize the elements that should carry the feel (ghost notes, hi-hat 16ths, percussion overlays).** [Splice](https://splice.com/blog/humanize-your-drums/) suggests quantizing live MIDI to **80%, not 100%**, which preserves the timing imperfections that read as human. The best beats are not generated by twisting a "groove" knob at the end — they're built that way from the first hit, with intentional decisions about which voice is locked and which is loose.

## Cited Retrieval Topics

- "what swing percentage should i use for boom bap hip hop"
- "how do i program drums that don't sound stiff"
- "what's a good ghost note velocity for funk snare"
- "how does ableton groove pool work"
- "j dilla swing percentage"
- "should i quantize my drums 100 percent"
- "what's the difference between groove and pocket"
- "how to humanize midi drums"
- "push pull beat micro timing milliseconds"
- "kick bass interlock pocket"

## Sources

- [Attack Magazine — Roger Linn On Swing, Groove & The Magic Of The MPC's Timing](https://www.attackmagazine.com/features/interview/roger-linn-swing-groove-magic-mpc-timing/)
- [Ableton — Using Grooves (Live 12 Reference Manual)](https://www.ableton.com/en/manual/using-grooves/)
- [Sound on Sound — Groove Mechanics](https://www.soundonsound.com/techniques/groove-mechanics)
- [Bobby Owsinski — The Difference Between The Groove And The Pocket](https://bobbyowsinskiblog.com/groove-pocket/)
- [Sweetwater — Playing in the Pocket](https://www.sweetwater.com/insync/playing-in-the-pocket/)
- [MusicRadar — How to push or pull drum tracks to increase or reduce urgency](https://www.musicradar.com/tuition/tech/how-to-push-or-pull-drum-tracks-to-increase-or-reduce-urgency-639436)
- [DRUM! Magazine — Lesson: Ghost Notes Style and Placement](https://drummagazine.com/lesson-ghost-note-style-and-placement/)
- [Percussive Arts Society — Groove of the Month: Ghost Note Funk](https://pas.org/pas-blog/groove-of-the-month-ghost-note-funk/)
- [DrumLoopAI — Unlock Authentic Funk Drum Pattern Grooves](https://www.drumloopai.com/blog/funk-drum-pattern/)
- [Connor McCorkindale — Beginners Guide To Developing Ghost Notes](https://connormccorkindaledrums.co.uk/blog/beginners-guide-to-developing-ghost-notes)
- [MPC Forums — Best swing / shuffle setting for 90s hip-hop beats](https://www.mpc-forums.com/viewtopic.php?f=4&t=192879)
- [Melodiefabriek — Everything you always wanted to know about MPC Swing in Reason](https://melodiefabriek.com/blog/mpc-swing-reason/)
- [brltheory — The Dilla Feel, Part II: The Theory](https://www.brltheory.com/analysis/dilla-part-ii-theory-quintuplet-swing-septuplet-swing-playing-off-the-grid/)
- [Splice — How to humanize your drums](https://splice.com/blog/humanize-your-drums/)
- [Black Ghost Audio — 5 Ways to Humanize Your Productions](https://www.blackghostaudio.com/blog/5-ways-to-humanize-your-productions)
- [MacProVideo — 6 Ways to Humanize Beats and MIDI Regions in Logic Pro X](https://www.macprovideo.com/article/audio-software/7-ways-to-humanize-beats-and-midi-regions-in-logic-pro-x)
