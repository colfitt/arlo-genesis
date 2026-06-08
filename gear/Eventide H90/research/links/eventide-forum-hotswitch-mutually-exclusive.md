https://www.eventideaudio.com/forums/topic/h90-hotswitch-question-2/
Eventide official forum · tonyshred (Q) / Brock (Eventide staff, A) · Aug 4, 2023

# HotSwitches are MUTUALLY EXCLUSIVE — the gotcha + the Performance-Parameter workaround

## The surprise that trips people up
Engaging HotSwitch 1 and then HotSwitch 2 does NOT stack — the second cancels the first.
Brock (staff): *"The hotswitches are mutually-exclusive. Selecting one toggles the other off."*

A HotSwitch is a Program-level snapshot that *can* combine parameters from BOTH Presets:
> "...a combination of parameters from both Presets. It doesn't 'have' to be, but it is a Program-level command."

So you cannot layer HS1 + HS2 + HS3 simultaneously. Each Program effectively has one "active HotSwitch state" at a time (or none). This behavior is identical via the panel, MIDI, and external aux switches, across firmware versions.

## The workaround: Performance Parameters DO persist independently
> "Performance Parameters persist. That is, you can latch them on & off, independently of hotswitch actions."

Example: a FREEZE Performance Parameter stays active even as you toggle HotSwitches. So if you need stacked/independent latched states, put SOME of them on Performance Parameters (Freeze, Warp, momentary moves) rather than cramming everything into mutually-exclusive HotSwitches.

## Rig relevance
Design Programs with this in mind: the three HotSwitches are three ALTERNATIVE snapshots, not three independent layers. For the drone use, put the big snapshot moves on HotSwitches (e.g. HS1 = Blackhole→Infinite, HS2 = scale change) but keep a latching FREEZE on a Performance Parameter footswitch so you can freeze a wall AND still flip a HotSwitch underneath it. That combination gives you a frozen pad you can re-voice live.
