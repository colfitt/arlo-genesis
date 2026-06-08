# Clip Launching and Follow Actions

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Launching Clips, Session View; Ableton Help Center — Updates to Follow Actions in Live 11
**Tags:** `daw-ableton`, `live-12`, `workflow`, `clip-launching`, `follow-actions`, `generative`, `performance`

---

## Clips Are Triggers, Not Files

In Session view, every clip on screen is a launchable trigger. Click the triangular launch button at the clip's left edge, or pre-select the clip and press `Enter`, and the clip starts playing in time with the project's launch quantization. Per the [Ableton Live 12 Launching Clips manual](https://www.ableton.com/en/manual/launching-clips/), launching a clip on a track stops whatever else that track was playing — both Session and Arrangement playback on that track is overridden by the launched clip until you stop it or trigger another. A scene's launch button (the triangle on the Master/Main track row) fires every clip in that row at once. Clips can also be launched from a hardware MIDI controller (right-click a clip launch button → Edit MIDI Map, or `Cmd-M`), from a computer keyboard key (Edit Key Map, `Cmd-K`), from a Push 3, or from follow-action chains. The architecture treats clip launching as the foundational performance gesture; everything else in Session view builds on it.

## Launch Quantization

Per the [Live 12 manual](https://www.ableton.com/en/manual/launching-clips/), each clip has its own launch quantization setting in the clip's Launch panel (open the clip with `Shift-Tab` to show Clip View, then choose the Launch tab). The default is `Global`, which uses the Control Bar's Global Quantization menu. Specific overrides per clip: `None`, `8 Bars`, `4 Bars`, `2 Bars`, `1 Bar`, `1/2`, `1/4`, `1/8`, `1/16`, `1/32`. Global Quantization is changed quickly with `Cmd-6` through `Cmd-0` on macOS — `Cmd-6` is 1 Bar, `Cmd-7` is 1/2, etc. A working default is 1 Bar for song-form launching; for fine-grained performance manipulation `1/16` lets you stutter clips on near-real-time triggers. `None` is the right choice when triggering one-shots or sample-pads where the trigger time defines the moment. Launch quantization also affects when Follow Actions fire, since they're treated as launches.

## The Four Launch Modes

Per the [Live 12 Launching Clips manual](https://www.ableton.com/en/manual/launching-clips/), every clip has one of four Launch Mode settings, configured in the Launch panel:

- **Trigger**: "down starts the clip; up is ignored." This is the default — a tap fires the clip.
- **Gate**: "down starts the clip; up stops the clip." Useful for sample-pad-style behavior where you only want the clip while the key is held.
- **Toggle**: "down starts the clip; up is ignored. The clip will stop on the next down." A tap fires, a second tap stops — useful for toggling loops on and off without holding the key.
- **Repeat**: "As long as the mouse switch/key is held, the clip is triggered repeatedly at the clip quantization rate." This is how stutter-roll effects are performed live — set quantization to 1/16, repeat-launch the same clip, and you get a 16th-note retrigger as long as the key is held.

Each clip has its own launch mode independent of its neighbors, so you can mix Trigger clips with Gate one-shots and a Repeat-mode roll clip in the same scene.

## Legato Mode

Per the [Live 12 manual](https://www.ableton.com/en/manual/launching-clips/), enabling Legato in the clip's Launch panel makes the next clip pick up the previous clip's play position rather than starting from clip-beginning. With Legato on across a group of identical-length clips, launching between them feels like switching between variations of the same loop — the underlying play position is continuous. The canonical use: build five variations of a melody as five Session clips, set Legato on all of them, and switch between them at any launch boundary — the melody keeps moving forward through its bar, but the variation changes. Combined with Follow Actions in Other or Any mode, Legato gives an evolving melodic line that never restarts, which is the standard live-performance generative trick in Live going back to Live 4 and still the right tool in Live 12.

## Follow Actions — The Concept

Per the [Live 12 Launching Clips manual](https://www.ableton.com/en/manual/launching-clips/), every clip can have a Follow Action: when the clip finishes playing (or after a set Follow Action Time), Live automatically launches a different clip according to the rule you set. This is Live's built-in generative-arrangement engine. The Follow Action settings live in the same Launch panel: Action A, Action B, Chance A, Chance B, Follow Action Time, and the Linked/Unlinked toggle (Live 11+). The ten possible actions per [Live 12's Follow Action set](https://www.ableton.com/en/manual/launching-clips/): No Action, Stop, Play Again, Previous, Next, First, Last, Any, Other, Jump. Each clip's two Action slots can hold any two of these. The Chance fields are weighted probabilities — Chance A is the weight for Action A, Chance B is the weight for Action B, and Live rolls every time the Follow Action triggers.

## Linked vs Unlinked Follow Actions (Live 11+)

A 2021 Live 11 update added the [Linked/Unlinked toggle](https://help.ableton.com/hc/en-us/articles/360019101360-Updates-to-Follow-Actions-in-Live-11). In Linked mode (the default), the Follow Action fires when the clip finishes — or after N loops if you set the Follow Action Multiplier. In Unlinked mode, the Follow Action fires after a fixed Follow Action Time that you set independently of the clip's length. Per the [Live 12 manual](https://www.ableton.com/en/manual/launching-clips/), the Time field "defines when the Follow Action takes place in bars-beats-sixteenths from the point in the clip or scene where play starts. The default for this setting is one bar." Unlinked is useful when you want a 4-bar clip to trigger its Follow Action after only 1 bar (creating a chopped-loop pattern), or when you want a 1-bar clip to play through 4 times before the Action fires. A sample-editor marker visualizes the Follow Action Time and can be dragged.

## The Ten Action Behaviors

Per the [Live 12 Launching Clips manual](https://www.ableton.com/en/manual/launching-clips/), the action set is:

- **No Action**: chain ends; nothing else fires
- **Stop**: clip stops at the action time
- **Play Again**: relaunches the same clip from its start (or from the Linked position if Legato is on)
- **Previous**: launches the clip immediately above in the track
- **Next**: launches the clip immediately below; wraps to the top of the group if at the bottom
- **First**: launches the topmost clip in the contiguous group
- **Last**: launches the bottommost clip in the contiguous group
- **Any**: random launch of any clip in the contiguous group
- **Other**: random launch of any clip *except* the one that just played (no immediate repeats)
- **Jump**: launches a specific clip slot by index (Live 11+, set via a target slider)

"Contiguous group" means clips next to each other in the same track column with no empty slots between them. Empty slots break the group — useful for limiting Follow Actions to subsets of clips on the same track.

## Scene-Level Follow Actions (Live 11+)

Live 11 added native Follow Actions for scenes. Per the [Live 12 Session View manual](https://www.ableton.com/en/manual/session-view/), open Scene View by double-clicking a Scene Header in Session view (under the Main/Master header). The Scene View panel exposes the same Follow Action grid — Action A, Action B, Chance A/B, Follow Action Time, Linked/Unlinked. A scene with `Next` Follow Action and a 4-bar Time will fire the next scene every 4 bars, walking the song through scenes automatically — this is how a full song arrangement plays back from Session view without manual scene firing. Combine with per-scene tempo and time-signature changes (Live 12, also in Scene View) and you have a complete linear-song playback from Session, no Arrangement view required. The pre-Live-11 IAC-bus workaround documented in older [Sound on Sound articles](https://www.soundonsound.com/techniques/follow-actions) is now obsolete.

## Generative Patterns — Chance-Based Variation

A practical generative drum-loop setup: four 1-bar drum clips on one track, named `Beat A`, `Beat B`, `Beat C`, `Beat D`. Each clip has Follow Action A = `Next` with Chance A = 70, Action B = `Any` with Chance B = 30, Linked mode. Hit `Beat A` and the chain walks A → B → C → D → A 70% of the time, with a 30% jump to any clip every loop. The result is a continuously evolving beat that never settles. Drop in a fifth clip with a sparse "breakdown" variation, give it Action A = `First` Chance 100 (so the breakdown always returns to A), and now the beat occasionally takes a breakdown and recovers. Stack additional tracks with their own per-track chains — a melodic line on a Wavetable track with its own Follow Actions in Other-mode for non-repeating variation — and you have a song that writes itself while you mix.

## Performance Patterns — Repeat Mode and Stutter Rolls

For live performance, the Repeat launch mode plus a high quantization rate is the stutter-roll workflow. Set a one-shot vocal sample to Launch Mode = `Repeat`, Launch Quantization = `1/16`. Map the clip to a Push 3 pad or a MIDI controller key. Holding the pad triggers the sample at 1/16-note intervals; releasing the pad lets the last triggered instance play out. Vary the quantization in real time (Cmd-6 through Cmd-0) to shift from 1/4-note hits to 1/32-note rolls without changing the clip. Combine with Gate-mode clips on the same scene for a hybrid hold-to-play / tap-to-stutter performance surface. This is the foundation pattern for finger-drumming on Push, for live remixing of vocal stems, and for performing breakdowns from a backing-track set.

## The Generative-with-Legato Combo

The canonical "evolving melody" patch in Live: write a 4-bar melodic clip with a Wavetable patch on a MIDI track. Duplicate it four times as variations — slightly different velocities, swapped notes, an octave drop in one. Set all five clips to Legato on, with Follow Action A = `Other` Chance 100, Linked mode. Launch the first clip. Every 4 bars, Live picks a different clip at random (never immediate repeats), and Legato makes the new clip pick up where the old one left off in the bar. The audible result: a melody that continuously plays without restarting, but with subtle variation every 4 bars. Per the [Live 12 manual](https://www.ableton.com/en/manual/launching-clips/), this combination "provides a powerful way of gradually changing a melody or beat" — it's the technique behind many ambient and generative-electronic Live performances.

## Common Failure Modes

A few common Follow-Action mistakes worth naming: (1) Empty slots between clips break the contiguous group — a Follow Action set to Any/Other/Next/Previous won't see clips across an empty slot. Use Stop buttons or right-click → Add/Remove Stop Button to manage which slots respond. (2) Chance A + Chance B don't have to total 100 — they're weighted, and Live normalizes them. Chance A=50, Chance B=50 is identical to A=10, B=10. (3) Follow Actions fire only when launch quantization is set to something other than `None`; per the [Live 12 manual](https://www.ableton.com/en/manual/launching-clips/), "any setting besides 'None' will quantize Follow Actions when they're triggered." A clip with quantization None can play but its Follow Action won't fire. (4) Scene Follow Actions and clip Follow Actions on the same scene fire independently — you can have both running, which can create timing surprises.

## Practical Defaults

For sketching with Follow Actions: build a track of 4–8 variations of a loop, set Legato on across them, set each clip's Follow Action A = `Other` Chance 100 with Linked mode, hit play, and let Live generate variation. For performance: keep Launch Mode at Trigger for most clips, use Gate for one-shots, Repeat for stutter pads, Legato on for tonal variations. For song playback from Session: set the top scene's Follow Action to `Next` with a Time matching the section length (8 bars, 16 bars), set the same on every scene, and the song plays through scenes top-to-bottom automatically. Always double-check launch quantization on per-clip overrides before performing — a clip with `None` won't quantize itself or fire its Follow Action.

## Cited Retrieval Topics

- "how do follow actions work in ableton live 12"
- "ableton scene follow actions live 11"
- "ableton clip launch modes trigger gate toggle repeat"
- "what does legato do in ableton clip launch"
- "ableton generative chance follow action"
- "ableton live 12 launch quantization shortcut"
- "ableton follow action time linked unlinked"
- "how do i make a generative drum loop in ableton"
- "ableton clip stutter repeat launch mode"
- "ableton other vs any follow action"

## Sources

- [Launching Clips — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/launching-clips/)
- [Session View — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/session-view/)
- [Updates to Follow Actions in Live 11 — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/360019101360-Updates-to-Follow-Actions-in-Live-11)
- [Follow Actions — Sound on Sound (Live 9 era; cited for historical workaround context only)](https://www.soundonsound.com/techniques/follow-actions)

See also: `corpus/sampling/loop-based-arrangement.md`, `corpus/structure/arrangement-arcs-and-transitions.md`
