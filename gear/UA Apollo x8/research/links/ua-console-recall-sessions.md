https://help.uaudio.com/hc/en-us/articles/26489269396116-Console-Recall-Plug-In
Universal Audio Support · "Console Recall Plug-In" (+ "Console Sessions")

(Distilled from UA Support text surfaced via search; help.uaudio.com blocks direct fetch. The per-session save/recall that makes the Apollo's print setup repeatable.)

WHAT CONSOLE RECALL IS:
- A plugin (VST/AU/AAX) you insert into a DAW track. Its SYNC switch stores the current UAD Console state INSIDE the DAW project file. When you reopen the project, Console is automatically restored to that state, regardless of any changes made to Console/Apollo in the interim.

WHAT GETS SAVED (with SYNC on):
- All inserted UAD plugins and their settings; all knob/slider/menu values; Monitor Gain and Line Input Gain; Line Output Reference Levels; Monitor Outputs Digital Mirror; Cue Outputs; Clock Source; and Sample Rate. Mix balances, input gains, and 48V Phantom Power status all recall too.
- You get a WARNING before phantom power is re-enabled on recall (in case you've connected fragile mics in the meantime).

HOW IT WORKS (and the common gotcha):
- SYNC stores the Console settings in the DAW FILE, not in the Console app — so you MUST save the DAW project to disk to retain them. Enabling SYNC alone does nothing until the project is saved and later reloaded.
- Enabling SYNC does not change current Console settings; it only captures them on save.

CONSOLE SESSIONS (the disk-based alternative):
- Independently, Console configurations save/load to disk as Session presets (Steve Kinney calls them "scenes") for unlimited reusable setups — e.g. a stereo-board-print session, a vocal-tracking session, a reamp-loop session.

FOR THE RIG: drop Console Recall on the print/master track and SYNC so each song recalls its exact capture chain (preamp-bypass-to-A/D state, input gains, +4/+24 reference, sample rate, monitor/cue routing). Pair with a saved Console Session for the recurring board-print and reamp-loop setups.
