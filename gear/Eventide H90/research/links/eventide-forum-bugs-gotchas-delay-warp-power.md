https://www.eventideaudio.com/forums/topic/delay-glitches-with-midi-pc-changes/
Eventide official forum · njdelyster (Q) / tbskoglund (Eventide staff) · Jan 2024
Also: https://www.eventideaudio.com/forums/topic/h90-bugs-and-issues/ (rck, damnjeeves, apalazzolo, jimheath87 · Aug–Nov 2023)

# Known bugs / gotchas — delay-warp on Program change, power under-current, H90 Control crashes

## #1 live gotcha: "delay warp" pitch warble on Program/PC change
- Symptom: loading a Program (even reloading the SAME delay algorithm) via MIDI PC produces a **pitch/delay "warp" sound on the delay trails.** Reported with an RJM PBC6X: *"pitch warbles occur whenever the PBC sends a PC message for this H90 program."*
- **Turning tails/spillover off does NOT fix it**; user set Spillover to 0 with no change.
- Eventide staff acknowledged: *"when certain delay algorithms are loaded there is a pitch/delay 'warp' sound. We're looking into improving this."* Initially framed as expected: *"Any time the delay time or heads change, there will be a delay warp sound. That noise is a byproduct of the effect."*
- **WORKAROUND (staff):** *"use a Hotswitch instead of loading another preset"* to change subdivisions/head levels — i.e. morph within ONE Program instead of triggering a full reload. (This user ultimately went back to a TimeLine, calling the artifacts "not workable in a live environment" — an honest negative data point.)
- Takeaway for live ambient: prefer **HotSwitches/Performance moves within a Program** over PC-loading new Programs when delay trails are ringing; reserve PC changes for clean section breaks.

## Program load latency
- Some Programs take **~0.5 s to load** when switching. Plan changes on a downbeat/gap, or use HotSwitches for instantaneous moves.

## Power under-current (real-world failure)
- A 12 V outlet supplying only **375 mA severely under-powers** the H90 (needs ~600 mA @ 12 V, or 800 mA @ 9 V, center-POSITIVE). Fix reported: **current-doubler cable combining two outlets**, or use a true high-current port. Under-powering causes flaky behavior. (Reinforces the dossier's power flag.)

## H90 Control software bugs (logged by rck, Aug–Nov 2023)
- **Windows app crashes "multiple times daily," with data loss**; crashes also reported after importing from PatchStorage. SAVE OFTEN.
- The **"Control" (fine-adjust) key doesn't slow parameter range adjustment**, making exact range values hard to set.
- **Typed-in numeric values sometimes don't "stick"** across several algorithms.
- Expression-pedal **range endpoints land inconsistently** even after repeated calibration.

## Misc firmware lore
- A **firmware 1.8.5** issue caused output only on **Output 2, not Output 1** for some users (fixed in later builds) — keep firmware current.
- **Tape Delay tap-tempo warble** reported on H90 that wasn't present on the H9 (related to the delay-warp issue above).
- Footswitches feel "crunchy" to some (build-feel complaint, not a fault).

## Rig relevance
For this MIDI-heavy ambient End board: the delay-warp-on-PC behavior is the most important live caveat. Build scenes so that PC changes happen at natural breaks, and do mid-song moves with **HotSwitches/HotKnobs/Freeze** (no reload). Make sure the H90 gets a dedicated high-current (>=600 mA @ 12 V) center-positive outlet — a shared/low-current port will cause intermittent faults. Keep firmware + H90 Control updated and save work often (Windows-app crashes).
