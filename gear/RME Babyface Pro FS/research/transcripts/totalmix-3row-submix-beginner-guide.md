https://www.youtube.com/watch?v=CW_IPQ4IeP0
Creative Sauce · RME TotalMix FX Made Easy: The Beginner's Guide You Need · 2025-05-29

Whether you're considering buying an RME interface, you've just bought one, or you've had one a while and you're confused about the TotalMix software, you're in the right place. It's incredibly powerful and versatile but also quite easy once you know how.

PRE-FLIGHT SETTINGS. Before starting, three things. (1) Routing mode — options are Submix or Free. This tutorial uses Submix mode; arguably the easier of the two, but no less powerful. (2) Set the layout to three rows (not two-row) so you can follow along. (3) If you've already messed things up, go to Options → Reset Mix → Total Reset to get back to a clean default.

THE THREE ROWS (the single most important thing to learn). If you push faders up and get unpredictable results, it's because you didn't understand the three rows.
- TOP ROW = your hardware INPUTS — mic and line inputs on the interface, plus digital inputs like ADAT and MADI.
- MIDDLE ROW = your software PLAYBACK destinations — places you can send signal TO from your DAW or other audio software. Normally your DAW's master/main bus defaults its output to the first channel here (Analog 1/2). These are NOT your hardware outputs despite some of the default naming; think of them as an intermediary.
- BOTTOM ROW = your hardware OUTPUTS — monitor speaker outs, headphone outs, all the line outs on the back, and digital outs like ADAT/MADI. This is the most important row because it's your STARTING POINT. Every output can have a separate mix.

THE CORE WORKFLOW (per-output submix). To build a mix for any output: FIRST click that output in the bottom row to select it, THEN use the top two rows of faders to build its mix. If you don't select the output first, you'll be adjusting the faders for a different output and get confused. Example session: recording a guitarist and a vocalist at once, each wanting a different headphone mix.
- Guitar player's mix: click his headphone output (Phones 1) first. He's on mic channel 10 — push that input fader up to hear him. If too quiet, click the wrench/spanner on his channel to open the gain control and bring INPUT gain up (the channel meter shows input gain, not output). He wants the backing track too — that comes from the DAW master bus to software playback Analog 1/2, so push that fader up. He wants a click track — route the DAW's click to a SEPARATE software playback channel (channel 2) and push that fader up. He wants a little of the singer — singer is on mic 9, bring that fader up a touch.
- Vocalist's mix (Phones 2): rather than rebuild from scratch, reuse the guitarist's mix as a starting point. Right-click Phones 1 → "Copy / Mirror Output Phones 1", then right-click Phones 2 → "Paste Submix from Phones 1". All faders snap into position. Now adapt: she wants the click quieter, herself louder, the guitar quieter. Flick between Phones 1 and Phones 2 to see the two independent mixes.

DSP EFFECTS (reverb/echo) work like aux sends, not inserts. First: DSP reverb/echo isn't on every RME interface — check specs. These are NOT plugins inserted on a channel; they behave like an outboard reverb/echo you SEND signal to and get a RETURN from. To put reverb on the vocalist: open the FX panel (FX button up top), enable reverb, then push up the little FX-send fader on the vocalist's channel — you'll see signal appear in the FX metering. You still hear nothing until you decide WHERE the return goes: turn up the reverb return on the destination output (e.g. Phones 2 for the singer, leaving the guitarist's Phones 1 dry). NOTE: this is "comfort reverb" for the performer's monitoring — it is NOT recorded to the DAW. For recorded reverb you'll realistically use DAW plugins or hardware. (Echo can also be enabled the same way.)

EQ + DYNAMICS are per-channel and CAN be recorded. Unlike the aux FX, EQ and Dynamics are channel-by-channel. Click the EQ button on a channel, switch it on, dial it. Click the D button for dynamics, switch on, adjust. To decide whether these print to the DAW, you DON'T do it in TotalMix — open the interface's Settings application and toggle the "EQ + D for Record" checkbox.

HOUSEKEEPING THAT MAKES TOTALMIX BEARABLE.
- Rename channels: double-click the label above a channel, type a name (e.g. "Guitar"), Enter. Works on inputs, software playback, and outputs.
- Hide unused channels: right-click a channel → Change Channel Layout. Select a range (click first, Shift-click last) → "Hide Channel in Mixer Matrix". Hidden channels are still ACTIVE, just out of view. (Great for hiding MADI/ADAT rows you aren't using.)
- Snapshots (right-hand panel): store/recall mix settings only — fader/pan/mute/solo positions and EQ/dynamics settings. Click Store, then a snapshot slot; double-click to rename. Does NOT include layout.
- Layout presets: store/recall which channels are hidden/revealed and the visual layout.
- Workspaces (File menu, or "Workspace Quick Select"): the master recall — includes layouts AND mixes AND window size — essentially everything set up at that moment. The fastest way to recall an entire configuration.
