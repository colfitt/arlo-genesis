https://www.youtube.com/watch?v=qAVqNbC_wso
RhythmLoopa (looping/streaming channel) · Ableton Live Looping Tutorial — How To Set Up Instruments To Loop (My Setup) · ~2022

> **LITE NOTE (facet-agent added):** This is the cleanest LITE-SAFE live-looping
> template captured — it uses NO Looper device (Lite has none). Instead it loops by
> routing each instrument track into a dedicated "loop" audio track (input = the
> source track, **post-mixer** so FX print into the loop) and MIDI-mapping clip
> launch buttons. Every step works in Live 12 Lite: audio tracks, ExtIn input
> config, Monitor=In, internal track-to-track routing, Session-view clip record,
> MIDI map. The ONLY non-stock element is the **Valhalla VintageVerb** send — and
> the user OWNS Valhalla, so that's fine; swap to the stock **Reverb** for a pure-Lite
> build. Track budget: each instrument + its loop-track pair eats 2 of Lite's 8
> tracks, so this scales to ~3 instrument/loop pairs + returns in Lite (use rack
> chains or resample to stretch further).

## Cleaned transcript

Quick tutorial on how to set up instruments for live looping in Ableton Live — this
is the setup I use for my Twitch stream.

**The finished project.** I have several instrument tracks (blue): acoustic guitar,
electric guitar, electric and acoustic violins, a bass, and a vocal mic. I monitor
all of them so I can always hear what I'm playing without arming record. Then I have
a set of separate "loop" tracks that capture each instrument.

**Step 1 — make an instrument track.** Ctrl-T (Cmd-T on Mac) for a new audio track.
Ctrl/Cmd-R to rename it ("Guitar"). Set **Audio From** to **Ext In**, pick your
interface input. If your inputs aren't listed: Options → Preferences → Audio → Input
Config, enable the mono/stereo inputs you use (do the same for outputs). Set
**Monitor = In** — this lets you hear yourself WITHOUT clicking the record-arm
button. Leave **Audio To = Master**.

**Step 2 — add FX on the instrument track.** Double-click the track and add whatever
you want (EQ, compressor, etc.). Put **reverb and delay on Sends/Returns** — here I
use Valhalla VintageVerb on Send A so I can dial reverb in per track; same for delay.
[LITE: use stock Reverb + Delay on the 2 return tracks instead.]

**Step 3 — make the loop track.** Ctrl-T again for another audio track — this is your
"Guitar Loop." Set its **Audio From** to the **Guitar** track you just made, and the
sub-dropdown to **Post Mixer** — this prints all the FX you added on the instrument
track into the loop recording. Set **Monitor = Off** (you're already hearing the live
guitar, don't double it). **Audio To = Master** so the recorded loop plays straight
out.

**Step 4 — multiply the loops.** Duplicate the loop track as many times as you want
parts. I keep three guitar-loop tracks so I can layer a rhythm part, a riff, and a
percussion part (all played on guitar). Same idea for bass, violins, vocals.

**Step 5 — perform.** **MIDI-map** the Session-view clip-launch / record buttons on
each loop track to a controller (or foot pedal). Hit record on a loop slot, play a
pass, it loops; trigger the next slot for the next layer. Build up: rhythm →
percussion → riff → full loop. Then get creative — add more instruments and vocal
loops.

**Takeaway.** Looping in Lite = instrument track (Monitor In) → loop track (input =
instrument track, Post Mixer, Monitor Off) → Session clip record, MIDI-mapped. No
Looper device required. Maps directly onto a pedalboard/banjo/baritone front end:
each hardware feed is an instrument track, each loop track captures it with the
chain's FX baked in.
