https://www.ehx.com/wp-content/uploads/2025/11/EIHP_manual_Web_v1.pdf
EHX · EIHP Manual v1.0 (official) — "Tips and DAW Notes" pp. 9-14 · 2025-11

The authoritative DAW setup + gotchas, quoted from the manual. THE single most important workflow reference.

THE CONNECT STEP (both plugin modes, marked "VERY IMPORTANT"): "You must connect the software plugin to the Effects Interface unit for the audio to reach the hardware." Open the plugin GUI → Settings (upper-right) → Select Device (greyed out if the unit isn't connected to the computer) → under FXI-[serial] choose Audio / Control / Pedalboard. For Hardware Plugin Mode pick Audio > Stereo (or Mono); USB light goes green on both plugin and unit. First time on a computer, a calibration screen appears — click "Calibrate" then "Done." No green = no audio.

HARDWARE PLUGIN MODE (pedals-in-DAW) setup:
1. Pedals' output → INPUT jacks; OUTPUT jacks → pedals' input.
2. In the DAW, keep your USUAL interface as the DAW's input/output device — "The Effects Interface should not be used for DAW input/output in this mode."
3. Insert the Electro-Harmonix → Effects Interface plugin on the track; connect (Audio > Stereo).
4. Press play; the track's audio passes through your pedals. Footswitch (hardware or plugin) bypasses.

PEDALBOARD MODE (plugins-as-pedals) setup — TWO instances:
1. Instrument → INPUT jacks; OUTPUT jacks → amp.
2. Insert one Effects Interface plugin; connect Pedalboard > IN (Stereo/Mono).
3. Add the plugin(s) you want on the board AFTER that instance.
4. Add a SECOND Effects Interface instance after all the plugins; connect Pedalboard > OUT.
5. Signal routes instrument → DAW plugins → out to amp. ("Routes audio onto a single track… lets you use other channels independently and another audio interface at the same time.")

AUDIO INTERFACE MODE: select "Electro Harmonix USB Audio / FXI-[serial]" as the DAW I/O device; INPUT L/R in, OUTPUT L/R or headphones out. "Do not use the Effects Interface software plugin while using the hardware as an audio interface." Lowest latency, "but won't allow use of your DAW for anything else."

GOTCHAS — quoted from "Tips for Successful Operation":
- SAMPLE RATE: "Your DAW's sample rate must be set to 44.1, 48, 88.1, or 96 kHz. Other sample rates are not supported." (Silence is often a wrong sample rate.)
- OFFLINE RENDER OFF: "Any rendering, bouncing, or freezing of tracks with the Effects Interface must be done in real-time, since the signal is converted to analog and sent through outboard pedals in real-time." (No offline bounce — print live.)
- MIDI GRAB: "In some DAWs, the Effects Interface will be detected as a MIDI input/output and the DAW will automatically connect to it with MIDI. This prevents the hardware from connecting to the plugin. Check the MIDI settings of your DAW and disable MIDI input/output/sync for the Effects Interface in order to connect."
- DEVICE OPTIONS / SPEED CONTROL (Settings > About Hardware): set buffer/block "for the best combination of stability and low latency. Slower or older computers may need larger buffer and block sizes." Speed Control "synchronizes audio streaming between the DAW and the Effects Interface… should typically be kept on… but can create occasional 'phasing' sounds on some systems. Turn off when absolute short-term agreement is necessary between wet and dry signals." (Turn Speed Control OFF for tight wet/dry phase agreement.)

PEDALBOARD MODE TIPS — quoted:
- GETTING STREAMING AUDIO: "In some DAWs, you must populate the track with an audio or MIDI region in order to process audio… some DAWs require that you press play and see a moving playhead in order to send audio to plugins. Getting pedalboard mode to work may require some experimentation with your system."
- LATENCY: "lowest possible latency that still allows for smooth audio streaming… the lowest possible buffer (sometimes called 'block') sizes in both the Effects Interface hardware and the DAW." (Also: "Some plugins will also have their own latency that adds to the total delay.")

DAW-SPECIFIC — quoted:
- REAPER: "Reaper's Anticipative Processing must be disabled for the Effects Interface to stay in sync with other audio. This is found in Reaper's preferences menu, under Audio > Buffering."
- LOGIC PRO: "enabling Low Latency Mode will bypass the Effects Interface. The Effects Interface will be re-activated when recording is completed… To avoid this, disable Low Latency Mode." Pedalboard-mode latency trick: Logic "will still often pass buffer of 1024 samples to plugins. To circumvent this, you can set up a MIDI or Software Instrument track, populate this track with a blank MIDI region, and then set up the Effects Interface in the Pedalboard Mode configuration. On a MIDI track the buffers passed to the plugin match Logic's settings."
- PRO TOOLS (Windows only): an "ExcludedMIDIPorts.txt" file "must be created to prevent Pro Tools from taking control of the Effects Interface as a MIDI port." First connection prompts you to create it; otherwise Settings → "Setup Pro-Tools…" walks you through it; restart Pro Tools.

POWER (Tech Specs): current draw 125 mA; USB/5V or 9 VDC-200 mA center-negative. (Elsewhere the manual warns supplies under ~150 mA may be unreliable.)
