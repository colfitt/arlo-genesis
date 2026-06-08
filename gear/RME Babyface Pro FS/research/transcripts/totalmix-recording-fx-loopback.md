https://www.youtube.com/watch?v=GY4pjSJFeUA
RME Audio · TotalMix FX for Beginners - Recording FX with Loopback · 2019-01-18

Hello and welcome back to the TotalMix FX beginner's guide. This week we talk about recording the internal effects.

There are two types of effects in TotalMix FX. There are the channel insert effects, namely the EQ and dynamics, and there are the auxiliary effects, i.e. the reverb and the echo. Depending on the effects type the recording process is different.

To record the channel insert effects all we have to do is go to the Fireface USB settings and activate the "EQ + Dynamics for Record" option. (That single checkbox prints the per-channel EQ/dynamics into your recorded signal instead of leaving them monitor-only.)

To record the auxiliary effects we need a little bit of TotalMix FX routing magic — this is the Loopback trick.

What Loopback does is send the signal of a hardware output back to the respective hardware input channel. So the signal flow is: we take the input signal from AS-1 and send it to one of the channels that I don't use for normal recording — in this case ADAT 1 & 2. I select ADAT 1 & 2, and by turning up the input channel fader in the submix mode, ADAT 1 & 2 is getting the dry signal from AS-1.

To add the wet signal we go to the effect send, turn up the right amount of effects send, and the effects unit detects an input signal. I activate the reverb, and now we have a wet signal that can be dialed in by going to the effects return. So ADAT channels 1 and 2 now have the processed sound from AS-1.

When we now activate loopback, this processed signal is sent back to the input channel ADAT 1 & 2. That shows up in my Ableton session as channels 15 and 16. So if I click record, I record the wet signal.

This method is also applicable to software playback channels — so I can process sounds that have been recorded before. In my Ableton session I have a pattern recorded; when I click play, software playback channel 1 (which I called "Ableton") receives a signal from the DAW. As before, I select ADAT 1 & 2, turn up the software playback channel to send the dry signal to ADAT 1 & 2, and turn up the effects send to send the software playback channel to the effects unit. The wet signal is sent to ADAT 1 & 2, and loopback is already activated. I go to another track in Ableton and select 15 and 16, and I can now record not only the dry signal back into the session, but also the wet signal.

So we can process sounds within TotalMix FX very easily.

KEY TAKEAWAY (loopback recipe): pick an unused output pair (e.g. ADAT 1/2) → in Submix view select that output → raise the source fader (a hardware input or software playback channel) to feed it the dry signal → raise the FX send to add reverb/echo → enable Loopback on that output → the mixed/processed result reappears as a hardware INPUT your DAW can record. This is how you bounce a TotalMix-processed stem or capture a mix of inputs + playback as a single stereo recording.
