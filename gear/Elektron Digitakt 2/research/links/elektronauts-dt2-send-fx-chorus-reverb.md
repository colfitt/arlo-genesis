https://www.elektronauts.com/t/digitakt-ii-examples-of-reverb-with-chorus-applied-to-send/217570
elektronauts.com · community thread · 2024

# Digitakt II — Send FX: Chorus into Reverb (and the mono-collapse gotcha)

How people route the new stereo send FX (Supervoid Reverb, Panoramic Chorus, Saturator Delay) — and the key limitation when chasing lush/wide ambient sends.

## The routing trick
You can feed the Panoramic Chorus *into* the Supervoid Reverb so reverb tails get chorused. Community method (verbatim):

> "Instead of [using] Reverb Send, use Chorus Send instead, and within the Chorus's settings, turn up the Reverb Send (turn down the Chorus volume if you don't want to hear its effect)."

So: send a track to the CHORUS, then inside the CHORUS page raise its REV (reverb-send) amount; pull the chorus's own output/volume down if you only want the chorused reverb tail. This is the path to shimmery, modulated reverb beds.

## The gotcha (DT2-specific, confirmed in-thread)
The chorus is **collapsed to mono before it hits the reverb**, so the stereo width of the Panoramic Chorus is lost on the chorus→reverb path:

> "the Chorus has been collapsed to mono, creating a flange-y phase-y effect" (with apparent high-end rolloff).

Practical upshot for wide ambient work: if you want a *stereo* chorused reverb, you generally can't get it purely via the chorus→reverb send — you may prefer chorus and reverb in parallel (both sends up on the track) rather than chorus-into-reverb, or resample the wet chorus and reverb that. Users in-thread were specifically hunting for lush settings and ran into this limit.

## Related FX-page notes
- CHORUS / DELAY / REVERB parameters can be set **global or per-pattern** (see "GLOBAL FX/MIX" / "settings on the DELAY, REVERB, and MASTER pages" threads) — decide whether your ambient send config is fixed for the whole project or morphs per pattern.

NOTE: the thread documents the *capability and the limitation* but did not post numeric knob settings for an ideal ambient patch — those remain to-be-dialed by ear. Flagged: thin on exact values.
