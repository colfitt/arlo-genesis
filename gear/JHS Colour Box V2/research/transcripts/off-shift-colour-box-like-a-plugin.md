https://www.youtube.com/watch?v=ApiWeqaIjCo
Off Shift Productions · How to Use the JHS Colour Box like a Plugin | Complete Guide · 2025-08-11

(The unique "hardware-plugin / re-amp" recording workflow — using the Colour Box as an outboard insert on every track in a DAW, then A/B'ing it against a 1073-style plugin. Most useful for the rig's console-print philosophy and for the exact line-level interfacing details.)

PREMISE: The Colour Box is probably the cheapest, most flexible 1073-style preamp you can buy. I can't afford eight of them for all my drum mics — but I can use ONE as a "hardware plugin" to affect every track in a project. A hardware plugin is when you wire any piece of outboard (a pedal, a rack EQ/comp) into your interface so you can use it like a plugin during the MIX phase, not just at record time.

CRITICAL LINE-LEVEL INTERFACING (the key practical detail):
- The Colour Box has the INSTRUMENT/XLR side switch. Most interface ins/outs are LINE level. Because of that switch you can use the Colour Box with a line-level interface WITHOUT a re-amp box.
- BUT: "the only way to use line level with the Colour Box is to use the XLR input." The combo jack's quarter-inch path is instrument level; to take a line-level signal you must use the XLR input.
- Needed cables: a male-XLR-to-male-TRS to go from the interface line OUTPUT into the Colour Box XLR INPUT, and a female-XLR-to-male-TRS to go from the Colour Box XLR OUTPUT back into a line INPUT on the interface. (In his example: interface output 4 → Colour Box; Colour Box → interface input 4.)
- In the DAW (Studio One) he uses the "Pipeline" insert plugin (Ableton = "External Audio Effect," Logic = "I/O plugin") to route a track out to the hardware and back, with auto latency/phase compensation (it measured a 72-sample / ~1.6 ms offset, in phase).

FIVE GAIN STAGES (his summary): "There are essentially five different places where you can adjust gain": (1) the 20 dB PAD on the side, (2) the HIGH/LOW switch (HIGH drives the preamp more, LOW = more headroom), (3) the STEP gain (steps up gain by some dB per step, five steps), (4) the PRE-VOLUME (volume going into the preamp after the step gain), and (5) the MASTER (output volume back to the interface).
- HIS RECIPE: "I keep the MASTER volume cranked all the way up to the top, and then I adjust my STEP gain and my PRE-VOLUME just to make sure I'm getting a decent signal. Then I start messing with EQ after that."
- He ENABLES the 20 dB PAD: "because if I don't have that enabled, my signal is way too hot going into the Colour Box." (Line-level sources hit it hard — the pad is essential when inserting it on already-recorded tracks.)

WORKFLOW REALITIES:
- Because it's hardware, the insert affects EVERYTHING routed to it at once — so to use it per-track you must dial in a sound, then BOUNCE/print that track in real time (it physically plays through the hardware), un-route, and move to the next track. Tedious but that's the cost.
- RECALL: hardware has no saved state, so he photographs the knob settings and drags the picture into the Pipeline plugin window as a visual reference, saving named presets ("color box kick", etc.) for a starting point.
- For bass and guitar tracks he did NOT EQ — just ran them through "to get that preamp effect" (saturation/color only), same as he did with the plugin.

VERDICT: It comes down to taste and workflow. A plugin is much faster. But the Colour Box "makes me use my ears and it does bring something sonically to the tracks that I haven't really found in a plugin."
