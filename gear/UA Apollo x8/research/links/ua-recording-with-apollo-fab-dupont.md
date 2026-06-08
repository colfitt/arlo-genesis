https://www.uaudio.com/blogs/ua/apollo-interfaces-setup
Universal Audio (official) · blog · "How to Record with your Apollo Setup" (Fab Dupont)

UA's official getting-started recording guide. The canonical near-zero-latency tracking workflow:

CONSOLE SETUP & INPUT:
1. Power up the Apollo and open the Console app.
2. Plug in mic/instrument and set input gain.
3. Open the INSERTS tab in Console's Input view.

LOADING PLUGINS FOR MONITORING (before you record, for inspiration):
- Click the INSERTS tab, select an available plugin, load a matching preset (examples given: EP-34 Tape Echo, Capitol Chambers reverb).

UNISON PREAMP SETUP (the "sound of the hardware" front end):
1. Click the dedicated UNISON insert tab in Console (or LUNA).
2. Choose a Unison plugin from the "PREAMP & CHANNEL STRIP" category.
3. Browse presets to match your source (SM57 on a cab, condenser on a room, DI, etc.).

UAD MON vs UAD REC — the critical distinction (quoted):
"In Monitor mode you hear the plug-ins through your headphones or monitors, but the audio that is sent to your DAW is unaffected. In Record mode, your DAW captures whatever plug-ins you have loaded onto the track."
Tip: use Monitor mode for "vibey" inspiration with a CLEAN DAW recording; switch to Record mode only when you are "100% confident" in the sound (it commits/prints the processing).

LOW-LATENCY BEST PRACTICES:
- In non-LUNA DAWs (Logic, Pro Tools, Ableton), enable "Low Latency Monitoring."
- LUNA users get Accelerated Realtime Monitoring (ARM) for zero-latency plugin tracking, and LUNA automatically integrates Console settings into new tracks.

For this rig: the stereo board print uses UAD MON with the preamp BYPASSED to A/D (cleanest capture of an already-processed chain); Unison + UAD MON is for mic'ing amps/room/banjo where you WANT the modeled front end and "sounds-like-a-record" monitoring while the clean signal goes to wave (or commit with UAD REC when confident).
