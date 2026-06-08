https://www.mpc-forums.com/viewtopic.php?f=50&t=220432
mpc-forums.com (MPC Sample subforum) · multiple users (SpaceTraffic, Die DIngen, NearTao, MPC2K500, Elijah, Lampdog, amaury, DJ AMBUSH, J.O.BEATS) · thread started Mar 27, 2026

AC50-SPECIFIC. The dedicated "MPC Sample: Bugs and fixes" thread on the official-adjacent MPC-Forums. Early-firmware (1.2.1 era, before the 1.3 beta) bug reports from actual owners. This is the single best source for AC50 gotchas. Distilled and quoted:

## Confirmed / corroborated bugs (multiple owners)

1. **Resample produces silence on the first attempt — you must resample TWICE.**
   - SpaceTraffic (OP): "Every time I resample, I have to do it twice. The first attempt always results in a silent clip, while the second one works as expected."
   - amaury: "I experience that as well! The first attempt is silent..."
   - Lampdog: "Just now exploring resampling, and yep, it's as you described, first was silence."
   - WORKAROUND: always discard the first resample pass and keep the second. Relevant to the rig's resample-bed-then-remangle loop — budget an extra pass.

2. **MIDI Slave mode distorts drums (esp. kicks) — distortion appears only when slaved to external MIDI clock.**
   - MPC2K500 (firmware 1.2.1): "As soon as it's triggered externally via MIDI, all the kick drums have a distorted noise. The kick drum sounds overdriven. This only happens when it's running in Slave mode. As soon as it's running independently, the noise disappears. It only affects the kick drums. The issue occurs with both USB and MIDI cables."
   - Elijah confirms: "when receiving MIDI Clock, the sample playback becomes distorted... there may be a bug in the MIDI input processing."
   - RIG-CRITICAL: in this studio the MPC would typically slave to the existing MIDI-clock master (Elektrons / Novation 61SL). On early firmware that introduces audible distortion on bass/kick sounds. WORKAROUND on affected firmware: run the MPC as clock MASTER, or verify whether 1.3.x fixes it before slaving. Flag = early-firmware bug, may be patched.

3. **Loose / untight pad-to-sound trigger timing.**
   - Die DIngen: "triggering of samples feels not super tight."
   - Lampdog: "It's a loose trigger or minuscule delay from pad bang to audio being triggered. Really noticeable when hitting pads fast and doing manual rolls."
   - For a finger-drumming-first box this matters; flagged by more than one owner on early firmware.

4. **Static / digital noise on pad-bang playback even below clipping.**
   - Lampdog: "there IS a static problem when pad banging internal and external samples (micro sd). All samples are green, they aren't touching yellow and I still hear static."
   - DJ AMBUSH: static when sampling over USB from an Android ("Droid") phone.
   - NearTao's triage question: "Is your distortion a ground loop noise issue? Do you have it from USB sources... are you connected to USB for power?" — i.e. first suspect USB-power ground loop. WORKAROUND to test: run on battery, unplug USB, try a different source.

## Other single-report bugs / weirdness
- **Audio spike after restart (HEARING-SAFETY).** SpaceTraffic: after a restart a long sample "had developed a bunch of brutal peaks—straight into the ears... take your headphones off immediately." He asked Akai to add a "built-in, non-disableable limiter." Treat with caution: pull headphones if a waveform looks corrupted after reboot.
- **Samples can go MISSING when a project is saved internally then moved to external (microSD) storage.** SpaceTraffic: "I had three samples go missing after working on a project that was first saved internally and then moved to external storage." WORKAROUND: decide internal-vs-SD up front; verify samples survive the move before deleting originals.
- **Sample "skipbacks" (slice retriggers) carry distortion** even with FX off (Die DIngen).
- **FX-monitor leak:** "if u set the fx monitor to on and the pads to fx off it still resamples with fx" (Die DIngen) — i.e. monitored FX can bake into a resample unexpectedly.
- **Resample / skipback can produce EMPTY MIDI sequences** (Die DIngen): "resampling or skipack the midi appears to give empty midi sequences."

## Notes
- NearTao (Expert Member, owns Force/MPC Live/SP404 mk2/OP-1 Field) updated firmware early and did NOT hit the resample/sample-loss bugs — suggests some are firmware- or workflow-dependent, not universal.
- Community read: several users feel Akai "rushed this thing out before 404 day" (J.O.BEATS) and expect software fixes. Treat all of the above as EARLY-FIRMWARE issues likely to be partially addressed by ongoing updates (1.3.x and later).
