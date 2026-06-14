https://www.youtube.com/watch?v=03j_SDkmDEc
YouTube · "how i record SHOEGAZE GUITAR & BASS in LOGIC PRO X" · (hardware-front guitar-tracking walkthrough)

Directly relevant to this rig: a hybrid analog-front-into-Logic workflow — amp + pedalboard recorded into Logic, with a parallel clean DI printed simultaneously for editing and reamping. This is exactly the "hardware-front chain INTO Logic" pattern the rig is built around.

## The dual-print (wet amp + clean DI) workflow
- Guitar → Tweed cable → DI box (an Altoids-box DI used as a splitter at the *front* of the pedalboard) → whole pedalboard → amp.
- The DI box also sends a **parallel clean DI** out via XLR — "just the guitar going straight into my DAW with zero effects."
- So every take prints TWO things at once: (1) the worked-out wet guitar tone, and (2) the totally unprocessed clean DI.
- He records a solid-state amp head (Marshall head; also a Roland JC-55) straight into the interface — no cab in the room. The cab is supplied by a cab-sim plugin in the **UAD Console app** (insert before Logic), using a Marshall 1960 cab IR with greenbacks ("JCM800-adjacent"). The amp section of the plugin is turned OFF — only the cab IR is used.

## Why print the clean DI (two reasons he gives)
1. **Editing**: a distorted guitar waveform is "very blocky, no transient," so editing/quantizing it is a nightmare. The clean DI has clear transients — quantize the DI and link the amp track to follow it.
2. **Reamping / re-tone**: the clean DI can be re-amped later through a different tone, doubled with a different tone, or — if he mixed himself "into a hole" with the initial tone — opened up and run through a Logic amp/`Rocker Verb`-style amp plugin instead. "It just gives you the option."

## Tone approach (minimal, committed)
- He rarely tweaks amp settings: keeps one good high-gain tone and one good clean tone, then **blends with pedals** to get where he wants (e.g. a Blues Driver pushed in front of a cranked gain stage). Single-coils give a "crunchy" sound that cuts/gets heavy in a mix.
- "A lot of times the tone itself is there when I record" — he does little guitar mixing, mostly just glue and de-harsh in the DAW.

## Logic editing chain (after printing)
- **Double-track hard L / hard R**: duplicate tracks with Command-D, record a second pass. The slight L/R differences "make it feel full."
- **Summing stack**: highlight the takes → create a **Summing Stack** so effects sit on the stack. Trim/loop, fade in / fade out.
- **Quantize via groups + Edit Group / Q-Reference**: in the Mixer, put each amp+DI pair in its own **Group** (Group 1, Group 2…). The key checkbox is **Editing (Q-Lock / "editing quantize lock")** — turn that on so quantizing follows for both. Click the DI track, run Flex/edit; it grabs transients from the DI and the (transient-less) distorted amp track follows. (He had to track at 1024 buffer for screen-recording, so notes the playing came in late — a good case for this.)
- He only quantizes "if something is off" or for surgically tight genres — not his usual riffing.

## Logic / plugin mix moves on the guitar bus
- **EQ (cut)**: go-to is FabFilter **Pro-Q3**; he hunts the exact resonant frequencies — guitar gets harsh around **4 kHz** — and notch them, watching the analyzer but trusting ears, not "mixing with eyes."
- **Soothe2**: catches the ~4 kHz harshness more specifically than a couple of EQ notches. He warns it's "very easy to overdo." Notes the default Soothe setting is "pretty geared towards guitar" because 4 kHz is a problem spot for most sounds.
- **Bus compression** on the all-guitars group: he uses the Waves **SSL bus compressor**, ~**4 dB gain reduction**, makeup-gain to match level, stock attack/release/ratio. He compresses **clean / transient-y guitars more** than distorted (a distorted square wave is already heavily compressed with little dynamics — so compression there is for tone, not transient control).
- Notes guitar is a "mid-range, contextual instrument" — saves the surgical guitar EQ until the full mix is in front of him; sometimes ends up removing the de-harsh plugins once bass/drums are added.

## Rig translation (DOUG note, not from the video)
- The video uses a UAD Console cab-sim; in this rig the equivalent is recording the pedalboard + VG-800/Iridium front-end into the **Apollo x8**, optionally printing a clean DI off the Radial X-Amp / EHX Effects Interface for later reamping through the board.
- The amp+DI Group + Edit-Group-Q-Lock trick is the stock-Logic answer to editing degraded/distorted-banjo or baritone takes that have no usable transients.
