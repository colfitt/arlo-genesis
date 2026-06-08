# Recovering a Crashed or Corrupted Live Project

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x — verify before treating as authoritative
**Canonical references:** Ableton Live 12 Reference Manual — Managing Files and Sets; Ableton Help Center — Backup Sets, Recovering a Set Manually After a Crash, Corrupt Sets, Plug-ins Tips and Troubleshooting, "Live cannot access the undo history file"
**Tags:** `daw-ableton`, `live-12`, `friction`, `recovery`, `crash`, `troubleshooting`

---

## The Two Recovery Paths

Live 12 has two recovery systems and they answer different questions. The **Backup folder inside each project** holds the ten most recent saved versions of the Live Set and is your fallback when a Set is corrupted on disk or when you saved-over something you wanted back. The **Crash folder in Live's preferences** holds the post-crash recovery package — the un-saved state of whatever Set was open when Live died, plus the undo history at the moment of death. Per the [Ableton Backup Sets article](https://help.ableton.com/hc/en-us/articles/360000377870-Backup-Sets), the Backup folder is automatic per project. Per the [Recovering a Set Manually article](https://help.ableton.com/hc/en-us/articles/115001878844-Recovering-a-Set-manually-after-a-crash), the Crash folder is automatic per Live installation. Knowing which to reach for is the first triage: if Live crashed and lost work, look in Crash; if the Set opens but is missing tracks or corrupted, look in Backup.

## The Backup Folder — Ten Versions per Project

Per the [Backup Sets article](https://help.ableton.com/hc/en-us/articles/360000377870-Backup-Sets), every time you Save a Live Set, Live writes a copy of the prior version into a `Backup` subfolder inside the project. The folder retains the ten most recently saved versions — when an eleventh save happens, Live moves the oldest backup to the macOS Trash and the new one takes its place. Files in `Backup` are named with a timestamp suffix (`MySet [2026-05-28 144530].als` or similar). To recover, navigate into the project folder, open `Backup`, and double-click the version you want; Live opens it as a standalone Set. To make a recovered version the current Set, Save As over the original (or save with a new name to keep both). The Backup mechanism is local to each project and does not back up across projects — so a project folder you delete takes its backups with it. On macOS the project folder lives wherever you saved the Set originally; there is no central Backup vault.

## The Crash Folder — Post-Crash Recovery State

Per the [Recovering a Set Manually article](https://help.ableton.com/hc/en-us/articles/115001878844-Recovering-a-Set-manually-after-a-crash), Live writes a recovery package to a Crash folder inside its Preferences directory whenever the audio engine or the host process terminates unexpectedly. On macOS the path is `~/Library/Preferences/Ableton/Live 12/Crash/`. The folder is hidden under Library by default — reveal hidden files in Finder with `Cmd-Shift-.` or use `Go → Go to Folder...` (`Cmd-Shift-G`) to type the path directly. Inside Crash you'll find three files per crash event: a Base file, a Crash Recovery Info file, and an Undo file. Each is timestamped if multiple crashes occurred. Per Ableton's procedure, rename the three files to strip the timestamp, move them up to the parent `Live 12` Preferences folder (replacing any existing copies), then relaunch Live — Live detects the recovery package on startup and offers to restore the Set. The recovery must be done with the same Live version that crashed; opening crash data in a different Live point release can silently fail.

## The "Restore Document" Dialog on Relaunch

Per [LiveAspects' Ableton recovery walkthrough](https://liveaspects.com/recover-an-ableton-project/), the simpler path most users follow: when Live launches after a crash, it shows a "Restore document?" dialog automatically. Click Yes. Live restores the Set in the state it was when the crash happened, including unsaved changes. Click No only if you don't want the recovery — Live then moves the recovery files into the Crash folder for later manual access, but offers no further auto-restore prompt. The "Yes" path is straightforward and rarely fails when the crash was clean (plug-in died, OS killed the process). The manual-from-Crash-folder path is for users who clicked No, who didn't see the dialog, or whose crash recovery files weren't auto-loaded.

## Auto-Save — There Is No Interval

A point of friction that confuses Logic and Pro Tools converts: Live 12 has **no auto-save with a user-settable interval**. Per the [Ableton forum thread on auto-save](https://forum.ableton.com/viewtopic.php?t=247691) and the Live 12 manual, the recovery story is the Crash folder for unexpected exits and the Backup folder for save history, not a periodic auto-snapshot. If you want interval-based auto-save, third-party tools exist — [LiveSaver](https://bugbytz.gumroad.com/l/livesaver) is a Max for Live device that triggers Save on a configurable interval. Otherwise the discipline is manual: hit `Cmd-S` before any big change, use `File → Save As` (`Cmd-Shift-S`) when starting a new arrangement variation, and rely on the ten-version Backup folder to catch your prior states. The Backup folder is fed by manual saves only — if you go four hours without hitting Save, the Backup folder has nothing from those four hours.

## Versioning by Save As — The Safe Discipline

A working producer convention to layer on top of Live's Backup mechanism. Before any structurally large move (deleting tracks, freezing everything, removing a section, changing the song form), use `File → Save As` with an incremented version suffix: `Song_v3.als`, `Song_v4.als`. This is more robust than relying on the ten-version Backup folder because (a) the Backup folder rotates out the oldest, and a long-running session can blow past ten saves; (b) the Save As versions live alongside the current Set in the project folder and don't disappear with macOS Trash actions; (c) version-named files are easier to triage at a glance. Per common Ableton-Certified Trainer workflow guidance, naming versions `v1`, `v2`, `v3` is enough — date stamps in the filename get noisy fast.

## Third-Party Plugin Crash Recovery

Per the [Plug-ins Tips and Troubleshooting article](https://help.ableton.com/hc/en-us/articles/5232428442002-Plug-ins-Tips-and-Troubleshooting), the single most common cause of Live crashes is a third-party plug-in. After a recovery, the first move is to identify and isolate the plug-in. Hold `Opt` while launching Live — this boots without scanning plug-ins, so the recovered Set loads with all third-party plug-ins as placeholders. If Live now opens the Set without crashing, the failure is in a specific plug-in. Update the plug-in to the current version (most crashes track to plug-ins out of date for the current Live release). Use only one format of each plug-in (AU or VST3, not both) — per Ableton, multiple formats of the same plug-in in one Set can cause conflicts. If a plug-in is still crashing after update, replace its instance with a different format (AU → VST3 or vice versa) or stub it out with a placeholder track and reload it after stabilizing the Set.

## Corrupted .als Behavior in Live 12

Per the [Corrupt Sets article](https://help.ableton.com/hc/en-us/articles/209773445-Corrupt-Sets), Live 12 attempts a partial load when it encounters a corrupted .als file — opening what it can parse and flagging the rest with errors. The split is usually plug-in instantiation versus document structure: a corrupted plug-in chain may produce empty device slots while the rest of the Set loads cleanly. If Live refuses to open the Set entirely, the .als XML structure itself is damaged. The fallback is the Backup folder — open the most-recent backup that is not corrupted. As last resort, the Ableton support team accepts corrupted .als files for repair via their support request form per the [Corrupt Sets article](https://help.ableton.com/hc/en-us/articles/209773445-Corrupt-Sets); the .als file alone is required (not the project samples) because the file format is XML-based and repair is structural.

## The Undo History Across Sessions

Per the [Live "cannot access undo history" article](https://help.ableton.com/hc/en-us/articles/209769125--Live-cannot-access-the-undo-history-file-and-is-switching-to-a-memory-based-undo), Live writes an undo history file to disk to allow undo across the full session. Undo persists within a single Live session — closing and reopening Live discards the undo stack and starts fresh. So if you save a broken state and close, you cannot Undo back to the working state on next open. The recovery is to open a Backup folder version, not Undo. The undo history file itself lives in the Preferences folder; if a corrupted undo file is causing Live to fail, the article documents moving `Undo.lock` to the Trash to force Live to start with a clean undo state.

## Prevention Discipline

A few habits that prevent most recovery situations. (1) **Save often** with `Cmd-S` — Live has no auto-save, so the Backup folder fills only when you hit Save. (2) **Save As with version suffix** before any large structural change (`Song_v3`, `Song_v4`). (3) **Collect All and Save** before archiving or sending to a collaborator — bundles external samples into the project folder so the Set can be reopened on another machine without missing-sample errors. (4) **Keep plug-ins current** — out-of-date plug-ins are the leading cause of crashes per Ableton. (5) **Use one plug-in format per Set** (AU or VST3) — mixing formats invites instantiation conflicts. (6) **Back up the whole project folder externally** — Time Machine or a manual copy to external drive catches the case where macOS Trash silently empties or the project folder is moved. (7) **Don't store sessions on the boot drive's space-critical partition** — a full disk during Save can corrupt the .als mid-write.

## When the Recovery Doesn't Work

If the Crash folder route doesn't restore the Set and the most recent Backup is also corrupted, walk the Backup folder backwards from the most recent. Per the [Backup Sets article](https://help.ableton.com/hc/en-us/articles/360000377870-Backup-Sets), the ten files are timestamped; pick the second-most-recent and open it. You'll lose the work done since that save, but you'll have a working Set to start from. If all ten Backup versions are corrupted (rare, usually only happens when the project folder was on a failing drive), check macOS Time Machine for an older copy of the project folder. If you have no external backup and no working Backup version, the last resort is the [Ableton support request form](https://help.ableton.com/hc/en-us/articles/209773445-Corrupt-Sets) for support's manual XML repair attempt. Attaching the .als file is sufficient; samples and presets are not part of the structural corruption.

## What ARLO Should Tell a User Mid-Crash

When a user reports a Live crash, the response order: (1) **Did the "Restore document?" dialog appear on relaunch?** If yes, click Yes; you're done. (2) **If no dialog**, walk the Crash folder steps — `~/Library/Preferences/Ableton/Live 12/Crash/`, rename and move the three files, relaunch. (3) **If recovery fails**, open the project folder, find the `Backup` subfolder, open the most-recent timestamped .als inside. (4) **If a specific plug-in is suspected**, relaunch Live with `Opt` held to skip plug-in scan, confirm the Set opens, then update/replace the offending plug-in. (5) **Prevention going forward**: save more often, version-name sessions, and back up project folders externally. Walking these in order resolves the vast majority of "Live just crashed and I lost my work" reports.

## Cited Retrieval Topics

- "ableton live crashed recover unsaved work"
- "ableton live 12 backup folder location"
- "ableton crash folder mac path"
- "ableton restore document dialog"
- "how often does ableton auto save"
- "ableton live 12 corrupted als file"
- "ableton plugin crash on load skip scan"
- "ableton live save as version naming"
- "ableton time machine project recovery"
- "ableton collect all and save before share"

## Sources

- [Ableton Live 12 Reference Manual — Managing Files and Sets](https://www.ableton.com/en/manual/managing-files-and-sets/)
- [Ableton Help Center — Backup Sets](https://help.ableton.com/hc/en-us/articles/360000377870-Backup-Sets)
- [Ableton Help Center — Recovering a Set Manually After a Crash](https://help.ableton.com/hc/en-us/articles/115001878844-Recovering-a-Set-manually-after-a-crash)
- [Ableton Help Center — Corrupt Sets](https://help.ableton.com/hc/en-us/articles/209773445-Corrupt-Sets)
- [Ableton Help Center — Plug-ins Tips and Troubleshooting](https://help.ableton.com/hc/en-us/articles/5232428442002-Plug-ins-Tips-and-Troubleshooting)
- [Ableton Help Center — Live Cannot Access the Undo History File](https://help.ableton.com/hc/en-us/articles/209769125--Live-cannot-access-the-undo-history-file-and-is-switching-to-a-memory-based-undo)
- [Ableton Help Center — Collect All and Save](https://help.ableton.com/hc/en-us/articles/209775645-Collect-All-and-Save)
- [LiveAspects — How to Recover an Ableton Project](https://liveaspects.com/recover-an-ableton-project/)
- [Ableton Forum — Why is There No Built-In Autosave](https://forum.ableton.com/viewtopic.php?t=247691)
- [LiveSaver Max for Live Device](https://bugbytz.gumroad.com/l/livesaver)

See also: `corpus/daw/ableton/workflows/freeze-flatten-consolidate-bounce.md`, `corpus/daw/ableton/friction/cpu-optimization.md`, `corpus/workflow/finishing-work-and-completion.md`, `corpus/workflow/session-methodology.md`
