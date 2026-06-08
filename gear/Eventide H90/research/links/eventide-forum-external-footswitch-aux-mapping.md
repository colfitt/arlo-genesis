https://www.eventideaudio.com/forums/topic/h90-and-footswitch-external/
Eventide official forum · SKYDRIVE98 (Q) / tbskoglund (Eventide staff, A) · June–July 2024

# External aux switches on the H90 — wiring + the #1 gotcha (double-assignment)

The H90 has only THREE on-board footswitches (P/A/B), but the two EXP/CTL TRS jacks accept up to **six aux switches** total (or expression pedals / CV). This is THE way past the two/three-footswitch limit. Key concrete notes from this thread:

## Cable / wiring
Eventide staff (tbskoglund, June 10 2024):
> "A TRS cable would be best, but with a single button aux switch a TS cable can work."

- A **TRS** cable into one EXP/CTL jack carries TWO aux switches (tip + ring).
- A single-button momentary switch on a **TS** cable works for one function.

## How to assign
- Tap tempo (and any performance/global function) can be mapped to an aux switch either on the pedal (System menu) or in **H90 Control → External Control**.
- Global Mappings can pin the three HotSwitches to aux switches across all Programs (System > External Control).

## THE GOTCHA: don't double-assign one aux switch
User's symptom: the preset toggled on/off every time he hit tap tempo. Root cause (staff):
> "both Tap Tempo and Load are assigned to Aux Switch 1. You will need to assign these functions to different Aux Switches to avoid the problem you are experiencing."

Fix: in H90 Control → External Control, remove the duplicate "Load" assignment from that aux switch (or move it to a different one). **One function per aux switch** unless you truly intend a combo.

## Rig relevance
For the End board (one player, hands on the baritone/banjo), this is how you get instant scene control without bending down to the encoders: wire a 2- or 3-button aux switch into one EXP/CTL jack via TRS, and globally map the buttons to HotSwitch 1/2/3 (or tap tempo + program load). That effectively turns the H90 into a 5–6-switch performance box.
