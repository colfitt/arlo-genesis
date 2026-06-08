# Freeze, Flatten, Consolidate, and Bounce in Place

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Computer Audio Resources and Strategies, Bounce to Audio, Arrangement View; Ableton Help Center — Committing Audio in Live, Bounce Tracks to Audio FAQ; Ableton Blog — Live 12.2 release notes
**Tags:** `daw-ableton`, `live-12`, `workflow`, `freeze`, `flatten`, `bounce`, `cpu`, `recipe`

---

## The Four Commit Commands, Distinct

Live 12 has four commands for committing live processing into static audio: Freeze, Flatten, Consolidate, and Bounce (with its sub-variants Bounce Track in Place and Bounce to New Track). Each does something different and they are not interchangeable. Per the [Ableton Help Center "Committing Audio in Live" guide](https://help.ableton.com/hc/en-us/articles/22998838817820-Committing-Audio-in-Live), the conceptual split is: Freeze is reversible (offloads CPU but keeps source devices), Flatten is destructive (replaces frozen audio over the source devices), Consolidate is a merge operation (joins adjacent audio clips into one), and Bounce in Place is the modern commit (renders post-FX audio, replaces source, preserves mixer settings as track-level controls). Live 12.2 added Bounce to New Track, which keeps the source intact and writes a new audio track with the rendered output. The right command depends on whether you want reversibility, whether you need the source preserved, and whether the bounce includes mixer-level processing.

## Freeze Track — Reversible CPU Relief

Per the [Live 12 manual on Computer Audio Resources](https://www.ableton.com/en/manual/computer-audio-resources-and-strategies/), Freeze Track renders every clip on the track to a temporary "freeze file" and plays back those files instead of running the devices in real time. The devices stay on the track but are bypassed; the CPU cost of that track drops to near-zero. Freeze a track via `Edit → Freeze Track`, or right-click the track header → Freeze Track. A frozen track shows a snowflake icon and cannot be edited — clips don't move, MIDI doesn't edit, devices don't change parameters until you Unfreeze (`Edit → Unfreeze Track`). Freeze is the right reach when you have a CPU-heavy synth chain or convolution reverb but you're not done with the track yet. The frozen state is fully reversible: Unfreeze, edit, Freeze again. Freeze files live in the project's `Samples/Processed/Freeze` folder; deleting them from disk forces Live to re-render at next Freeze.

## What Freeze Includes (And What It Doesn't)

Per the [Sound on Sound article on Track Freezing](https://www.soundonsound.com/techniques/track-freezing-ableton-live), Freeze captures audio post-devices but pre-mixer — exactly like Bounce in Place. Track volume, pan, and Sends remain as live mixer controls, so you can still adjust the track's level in the mix after freezing. The freeze captures the track's automation, MIDI clips converted through the instrument, and all device effects. What Freeze does not include: Sends going out to Return tracks (those Returns still process the dry signal sent via the Send, so Reverb sends still work normally). Send levels are recorded with the frozen state; changing a Send level after freezing requires unfreezing. Frozen tracks cannot be the source of an Audio From routing into another track — the chain breaks until unfrozen.

## Flatten Track — The Destructive Commit

Flatten is the irreversible second step. Per the [Live 12 manual](https://www.ableton.com/en/manual/computer-audio-resources-and-strategies/), Flatten "takes any frozen track and replaces the elements in it with the equivalent bounced audio. Clips are replaced with new Clips that have any track effects and Warping printed as part of the audio." Devices are removed from the track. The MIDI clip is replaced with an audio clip on what is now an audio track. After Flatten, there is no going back to the original MIDI plus instrument plus chain — the only way to recover is Undo (which stays available in the current session) or to revert to a backup. Flatten is the commit-to-this-sound moment: lock in the decision, free the CPU permanently, free the device slot on the track. In Live 12 a combined `Freeze and Flatten Track` command runs both in one step (Edit menu and track context menu).

## Bounce Track in Place — The Modern Commit (Live 12.2+)

Live 12.2 introduced Bounce Track in Place, which per the [Ableton Live 12.2 release announcement](https://www.ableton.com/en/blog/live-12-2/) "supersedes the Freeze and Flatten Track command" for committing tracks. Per the [Live 12 Bounce to Audio manual](https://www.ableton.com/en/live-manual/12/bounce-to-audio/), Bounce in Place "commits a source track as a new audio track which replaces the source" — same end result as Freeze-then-Flatten, but in one operation without the temporary freeze state. It works on audio and MIDI tracks. The bounce captures post-FX, pre-mixer — meaning effects are rendered into the audio, but volume, pan, and Sends remain as live mixer controls on the new track. Bounced files live in `Samples/Processed/Bounce` in the project folder. New track names get `(Bounce)` appended and inherit the source track's color. There's no shortcut by default; use `Edit → Bounce Track in Place` or the track context menu.

## Bounce to New Track — Keep the Source (Live 12.2+)

Bounce to New Track (also Live 12.2) is the non-destructive variant. Select clips or a time selection across multiple clips, press `Cmd-B` on macOS, and Live writes the rendered audio to a new track while muting the source clips. The source track stays intact, devices and all, just with the bounced clips muted. This is the right reach when you want to commit to a particular take's sound but might come back to edit the source later — print a vocal-chain render of a verse so you can mix the rest of the song without bumping CPU, but keep the original vocal track with the chain in place. Per the [Live 12 Bounce manual](https://www.ableton.com/en/live-manual/12/bounce-to-audio/), Bounce to New Track is post-FX pre-mixer same as Bounce in Place — mixer settings live on the new track, devices are rendered into the audio.

## Group Track Bouncing — Post-Mixer Behavior

A non-obvious detail per the [Live 12 Bounce manual](https://www.ableton.com/en/live-manual/12/bounce-to-audio/): when you Bounce in Place a Group track, the bounce is post-mixer — it captures the audio "from the Main track's output, including all the effects and sends used inside the Group, but excluding any processing on the Main track." This means bouncing a Drums group printed everything inside that group as a single drum stem, with the bus comp baked in, sends rendered, and the inside-group fader levels printed. It's the right way to print stems for handoff to a mixer: bounce each Group, get a coherent stem per group. Live 12.3 expanded this with explicit Bounce Groups support per [Dubspot's coverage of the 12.3 update](https://blog.dubspot.com/ableton-live-12-3-update).

## Consolidate — Merging Adjacent Audio (Not a Bounce)

Consolidate is a different operation entirely. Per the [Live 12 Arrangement View manual](https://www.ableton.com/en/live-manual/12/arrangement-view/), Consolidate "combines selected material from several adjacent clips into one new clip." The shortcut is `Cmd-J` on macOS. Use case: you have three adjacent audio clips on one track (a comp result, a region you've trimmed, a chopped sample), and you want them treated as a single clip for subsequent dragging, looping, or warping. Select across them in Arrangement, hit `Cmd-J`, and the three clips become one audio clip with the combined waveform. Consolidate writes a new audio file in `Samples/Processed/Consolidate`, so it is destructive in the sense that the merged clip is now a new audio file — but it doesn't apply any device processing, doesn't change the sound, doesn't replace devices. It only joins regions. A consolidated clip with multiple original loops becomes a single audio file you can loop as a longer unit.

## When to Reach for Which

A practical decision chart for Live 12.2+. CPU is high mid-session and you might still tweak the sound? Freeze. Sure the sound is done but might come back later? Bounce to New Track (keeps source). Sure the sound is done forever and want the cleanest project? Bounce Track in Place. Have a comp or chopped-clips arrangement on one audio track and want it to play as a single clip? Consolidate (`Cmd-J`). Want to render a stem of a Group for handoff to a mixer? Bounce in Place on the Group track (post-mixer behavior). Want a freeze you can flatten later? Freeze, then Flatten when ready. The Freeze-then-Flatten path remains the only way to "decide later" — Bounce in Place is one-shot commit. Live 12.2 explicitly recommends Bounce in Place over Freeze-and-Flatten for new workflows because the rendered file is named, organized, and not a temporary file.

## Practical CPU Patterns

Per the [Live 12 Computer Audio Resources manual](https://www.ableton.com/en/manual/computer-audio-resources-and-strategies/), watch the CPU meter in the top-right of the Control Bar. When it crosses 70% sustained, freeze the most expensive tracks first — typically convolution-reverb returns, layered instrument racks, and CPU-heavy plugins like physical-modeling synths. The order matters: Return tracks with convolution should be frozen last (because they process from multiple sources), while instrument tracks with heavy chains can be frozen first without breaking other tracks' chains. After freezing, the CPU meter should drop. If it doesn't, identify the next-heaviest track. Bounce in Place is preferable to Freeze for tracks you're certain won't be revisited — the freed CPU is permanent and the project size on disk is smaller (no parallel device chain held in memory). Reduce CPU pressure further by closing the Device View for tracks you're not editing — visible device GUIs still consume some overhead.

## Naming, Files, and Project Hygiene

All committed-audio operations write files into the project folder. Per the [Live 12 Bounce manual](https://www.ableton.com/en/live-manual/12/bounce-to-audio/), bounce files go to `Samples/Processed/Bounce`, freeze files to `Samples/Processed/Freeze`, and consolidates to `Samples/Processed/Consolidate`. Saving the Set with `File → Collect All and Save` rolls these into the project's self-contained folder. Bounced and consolidated files persist after the operation; freeze files are deleted automatically when you Unfreeze (the device chain takes over again). When project size matters — handing off a Set to a collaborator, archiving a finished song — Bounce in Place beats Freeze for cleanliness because there's no parallel "render plus original" stored.

## Common Mistakes

A few worth naming. (1) Forgetting that Freeze captures Send levels — adjusting a Send after freezing has no effect on the frozen audio. Unfreeze first. (2) Bouncing a Group expecting per-track stems — Bounce in Place on a Group writes one mixed bounce of the group, not separate stems. To get stems, bounce each child track individually. (3) Confusing Bounce in Place (commits, replaces source) with Bounce to New Track (commits, keeps source muted) — read the menu name carefully. (4) Using Consolidate when you meant to bounce devices — Consolidate does not include devices, only the audio as it sat in the clip(s). For a "merge with devices baked in," use Bounce in Place. (5) Flattening a frozen MIDI track and then realizing you needed to edit the MIDI — the only recovery is Undo while the session is still open. Always Bounce to New Track if there's any chance you'll want the source back.

## Cited Retrieval Topics

- "what's the difference between freeze and bounce in ableton 12"
- "ableton bounce track in place new feature 12.2"
- "ableton freeze flatten track shortcut"
- "ableton consolidate clip shortcut cmd j"
- "ableton bounce to new track keeps source"
- "ableton bounce group track stems"
- "how do i free up cpu in ableton"
- "ableton freeze file location samples processed"
- "what does flatten do in ableton live"
- "ableton bounce in place post fx pre mixer"

## Sources

- [Computer Audio Resources and Strategies — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/computer-audio-resources-and-strategies/)
- [Bounce to Audio — Ableton Reference Manual Version 12](https://www.ableton.com/en/live-manual/12/bounce-to-audio/)
- [Arrangement View — Ableton Reference Manual Version 12](https://www.ableton.com/en/live-manual/12/arrangement-view/)
- [Live Keyboard Shortcuts — Ableton Reference Manual Version 12](https://www.ableton.com/en/manual/live-keyboard-shortcuts/)
- [Committing Audio in Live — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/22998838817820-Committing-Audio-in-Live)
- [Bounce Tracks to Audio FAQ — Ableton Help Center](https://help.ableton.com/hc/en-us/articles/22999165562396-Bounce-Tracks-to-Audio-FAQ)
- [Live 12.2 is Coming — Ableton Blog](https://www.ableton.com/en/blog/live-12-2/)
- [Ableton Live 12.3 Update — Dubspot](https://blog.dubspot.com/ableton-live-12-3-update)
- [Track Freezing In Ableton Live — Sound on Sound](https://www.soundonsound.com/techniques/track-freezing-ableton-live)

See also: `corpus/workflow/finishing-work-and-completion.md`, `corpus/workflow/preproduction-and-demo-handoff.md`
