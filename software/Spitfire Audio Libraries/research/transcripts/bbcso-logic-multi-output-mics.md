https://www.youtube.com/watch?v=O-F93wPe2oA
Tom Harrold Music · Logic Pro X / Spitfire BBC SO Pro Composer Tutorial: Using multi-outputs · 2023-02-20 (8:08)

[The Logic-specific mic workflow — exactly what this AU rig needs. Shows how to route each BBC SO mic (Close, Tree, Outrigger, Ambient) to its own Logic channel so each can be EQ'd/processed independently, then summed. This is how you'd split the close/dry mic off to send into Valhalla/Decapitator while keeping the room mics separate. Pro edition (needs the individual mic signals). Notes the RAM cost.]

## Setting up multi-output in Logic

1. New track → **Software Instrument** → instead of Stereo, choose **Multi-Output**. This lets you control routing of each microphone independently in the DAW.
2. Load the BBC SO instrument (he uses the Cello "leader"). In the plugin's mic menu you can now choose which **stereo channel** each microphone goes to.
3. In the Mixer, the instrument track has a **+ / –** button to create the associated aux channels. He uses **four mics: Close, Tree, Outrigger, Ambient** — so he adds three new aux tracks (the original track is the fourth). They appear as Stereo Channel 2 / 3 / 4 (mono 3-4, 5-6, 7-8) routed through separate auxes. Rename them Close / Tree / Outrigger / Ambient.

## Routing the mics

In the plugin's signals/mic menu: turn **off Mix 1** (don't need it), turn **on** the four mics you'll use and **turn them all up to full** — "we don't want to mix it at this stage; just give maximum signal to the DAW, it can do its thing later."
- Close mic → Stereo 1
- Tree mic → Stereo 2
- Outrigger mic → Stereo 3
- Ambient mic → Stereo 4

So each mic is heard only within one channel. Right-click each new track → **Create Track**, then select all four → **Create Track Stack → Summing Stack**, routed to a bus renamed (e.g. "Cello multi"). Now the cello is still one instrument visually, but each mic is independently processable.

## MIDI + articulations across the stack

You can put the MIDI on any of the four channels and it still plays — just set the **articulation set** on the channel that holds the MIDI (Strings → Cello leader), and all articulations work.

## What each mic sounds like (his descriptions)

- **Close** — "really close, intimate; sounds like the cello's playing right here." (← the dry, controllable signal for this rig.)
- **Tree** (Decca Tree) — "if you only had to use one microphone, use the Tree mic." The default balanced perspective.
- **Outrigger** — "adds a sense of space."
- **Ambient** — "puts it in a really interesting space" (the most distant/roomy).

## Why split them — independent processing

Each mic can now get its own EQ etc. that affects only that signal. His habit: on the **Close mic**, roll off "quite a bit of bass — the more you roll off the better," and shave harsher frequencies (the close mic "has real grit, which you might want, but normally you just want the warmth"). (For the degraded-wall rig: isolate the dry Close mic to feed Decapitator/EchoBoy, keep Tree/Ambient as the clean spatial bed, or build your own faked space entirely from Close → Valhalla.)

## RAM caveat

Multi-mic gets RAM-intensive — a big orchestral piece with four mics on every instrument hit ~30 GB RAM. For a small ensemble it's fine (8-16 GB easily achievable).
