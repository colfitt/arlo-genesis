https://www.youtube.com/watch?v=eO28ct5_T50
SPITFIRE AUDIO CLIPS · How to use DYNAMICS in BBC Symphony Orchestra · 2020-09-18 (3:29)

[Official short, demonstrated IN LOGIC, on the single most important gesture for evolving string beds: riding Dynamics (the mod wheel = CC1) to create crescendos/diminuendos. Three ways to write the data, plus the cleanup + automation-mode workflow. This is the "how to make a held note breathe" mechanic.]

## The core gesture

"The most common way of changing dynamics when using our libraries is to use the **mod wheel** on the MIDI keyboard — simply move it up and down as you play in the notes." The mod wheel drives the **Dynamics** fader (the soft→loud dynamic-layer crossfade), so riding it = the note swells and recedes. (In Logic this is the workhorse for a sustained bed: hold a Long/sul tasto chord and ride the wheel for slow crescendo/diminuendo movement.)

## Editing the recorded dynamics data (Logic)

To edit what you played: switch the track to **Automation mode** (Automation Lane button). To see the data as a line, switch the track to **Region mode** and select **Modulation** from the dropdown — now you see the MIDI CC data you wrote with the mod wheel.
- Edit individual points by moving the dots, or highlight + delete to rewrite manually.
- Double-click to bring up the automation line; click on the line to add automation points.
- Raise the line's height = **crescendo** (gets louder); lower it = **diminuendo** (gets quieter).

## Third option — touch mode (record fader moves)

If you don't own a controller / don't like writing data manually: switch to **Touch mode** and record the movements of the on-screen **fader**. To see the data, switch automation from Region to **Track**, then on the BBC SO instrument select the relevant fader from the dropdown.
- Caveat: touch mode produces "inconsistencies in the MIDI CC data" — too many dots. Thin them by deleting individual dots: "this will save you CPU" and makes the transition smoother on playback.
- When done, switch the track mode from **Touch to Read** so you don't overwrite the data if you touch a plugin parameter afterward.
