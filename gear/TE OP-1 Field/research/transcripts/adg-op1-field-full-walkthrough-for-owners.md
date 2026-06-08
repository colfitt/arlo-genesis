https://www.youtube.com/watch?v=AYXjDsDSyK8
ADG · OP-1 Field (Walkthrough For OP-1 Owners) · 2022-05-29

A ~71-minute exhaustive overview aimed at people who knew the original OP-1, on firmware 1.1.2. Strongest on tape styles, the "baked-in" tape behavior, the album/loopback bounce, the input/recording menu, the Hold sequencer, and connectivity. Distilled to workflows and settings below (skipping the lengthy hardware/key-alignment intro).

## Power-off safety
[Shift]+metronome → settings → System settings → Power off. Default is INSTANT; set to DELAYED to get a ~6-second on-screen reprieve when you flip the switch (press [Com] for instant-off even when delayed is on).

## Tape styles & tapes/reels (4 styles, 8 projects total)
[Shift]+[Tape] opens tape settings. Four styles, each a 6-minute, 4-track, STEREO tape:
- STUDIO 4-track — cleanest (equivalent to the original OP-1's tape).
- VINTAGE 4-track — vintage-colored (tag: gold reels).
- PORTA 4-track — cassette emulation, audible hiss + tape WOBBLE (tag: chrome).
- DISC MINI — minidisc/digital, subtle artifacts (tag: disc).
Projects are called "reels" (studio/vintage), "tapes" (porta), or "discs" (disc mini). There are EIGHT TOTAL across the whole machine (not 8 per style). Press [New] to create one (takes a couple seconds); when 8 exist, [New] is grayed out. Loading any tape when full only offers to ERASE it (there's always at least one tape on the machine). Erase/delete is instant (like the OG's 1-2-3-4 wipe). Name tapes: BLUE knob moves the cursor, GOLD knob cycles characters (# - 0-9 space a-z), up to 12 chars — you MUST press OK to save the name.

## CRITICAL: tape character is baked in at RECORD time only
Demonstrated directly: a sound recorded to the Porta tape carries its wobble/hiss; if you LIFT that audio and DROP it onto the Studio tape, it STILL has the wobble — lifting/dropping carries whatever the SOURCE emulation was. Conversely, audio recorded clean on Studio, lifted and dropped onto Porta, stays CLEAN (no wobble). The tape style only affects audio AT THE MOMENT IT IS RECORDED to that tape. So: to get Porta warmth, you must RECORD to the Porta tape; you can then lift it to a Studio reel to keep working.
- Tapes save the audio content only, NOT synth/sound state — switching reels swaps only the tape content (confirmed by loading a new sound on one reel and finding it unchanged on another).

## Tape transport quirks per style
All styles keep tape-stop, reverse, stutter, loop in/out. PORTA has a much QUICKER tape-stop; DISC MINI is nearly instant. Reverse near a loop region behaves oddly (it loops back if you're within a certain range of the start point, but not always beyond it).

## Loop points (same as OG)
Press [1] (which is the "in"), hold [Shift] + arrows to jump across, hit "out" → you're in a loop; toggle it on/off. Hold [Shift] + arrow to jump between sections.

## Synth UI changes
Turning any knob now NAMES the parameter on screen (e.g., FM amount / frequency / topology / detune). This can't be turned off. Click an encoder IN to show the parameter without changing its value. [Shift]+[Synth] (or [Shift]+the relevant mode button) RESETS the current preset to default.

## DIMENSION synth (the new engine)
- Left knob = WAVEFORM blend: noise → pulse (variable pulse width) → square → saw (up) → sub-saw → back to noise.
- Gold knob = STEREO WIDTH (shown as a blue outline).
- Then frequency FILTER (cutoff) and RESONANCE.
- Affected by all the usual LFOs (Element, MIDI, Random, Tremolo, Value, Velocity).

## Sampler waveform editing (Field improvement)
Pressing the BLUE encoder IN now ZOOMS the waveform (no more holding shift + cranking). Works for all the point knobs (start/end/loop start/loop end), speeding the workflow. [Shift] still gives play direction (forward/reverse), detune, the loop-end fade, and overall sample gain.

## Drum sampler (stereo + mix)
Per-chop: pitch, start point (zooms; based on the next sample's end point), end point, play mode (one-shot / gated-forward / loop). [Shift]: MIX knob blends the left-channel vs right-channel content of a stereo chop, OR push it in to switch to PANNING (far-left/far-right, played as mono otherwise); attack (less/more clicky → pad-like); per-chop gain; play direction. Shows the note you're editing.

## Mixer & global effects
[Mixer]: per-track volume/pan, mute tracks from here. [2] = EQ (low/mid/high with a visual of how much you're affecting "cleanliness"). [3] = GLOBAL tape effects: CWO, Delay (shows ms; speed, feedback, input), Grid (z/x/y), MOTHER (new reverb: DISTANCE = tail length, MIX dry/wet, GATE = only passes reverb above a volume threshold, COLOR), Nitro, Phone, Punch (compressor), Spring. [4] = MASTER COMPRESSOR (release, drive, peak L and R; [Shift] = shift-lock both faders together).

## Metronome
Tap to set tempo; beat-match options (MIDI sync, Pocket Operator sync), link BPM to tape speed, free BPM. Volume up = pitch up (as on the OG). Tape speed shown in "cm/s."

## Input / recording menu (hold [Shift]+[Input])
- OP-1 MIC (change source with BLUE): threshold + input gain (can't attenuate below 0, boost only). The old "scratch the mic" trick still works.
- RADIO: press the green/encoder IN to auto-seek to the next station; can attenuate volume below 0, boost to +16, threshold control.
- USB: sample audio coming IN over USB-C from a computer or another device (e.g., the TX-6); gain/trim.
- OUT-IN: a LOOPBACK — whatever the OP-1 is hearing/outputting is recorded back in. This is one way to BOUNCE multiple tracks down to a single track.
- ALBUM: A-side / B-side, STEREO mixdown only (no mono option). BLUE knob toggles between recording to album and FM TRANSMITTING; press Live to start transmission (broadcasts the OP-1's name as the station). Record/stop/flip the tape from here.

## Hold sequencer (new)
[Shift]+[Sequencer] → Hold. BLUE knob sets the RANGE/break point of notes it will hold; press/hold a note below it to LATCH it (great for low-octave DRONES) while you play freely above. GRAY knob TRANSPOSES the held note(s)/chord and stays in key (e.g., shift a C-major shape around). GOLD = poly/mono (in mono, a new note toggles the held one; same note again turns it off). Press the orange/red button to CLEAR held notes; rotate it to turn Hold off/on. (Polyphony is limited — ~10 voices — so you can't truly hold every key at once.)

## Connectivity / computer ([Shift]+[Com])
- MIDI: set channel; clock (none / in / out / both); notes (none / in / out / both); "other" = CC + SysEx.
- Control mode: OP-1 as a pure MIDI controller (knobs absolute or relative; choose whether octave keys send octave messages).
- List: shows connected devices (BLE and USB MIDI). "Advertise" broadcasts the OP-1's Bluetooth for pairing as a controller.
- Charging: press the orange/red button IN on the com page to DISABLE charging (fixes ground-loop/noise interference for some users).
- Mount as drive: [Shift]+[4] mounts as a FAT16 USB drive (267 MB capacity shown) — slow to mount. MTP mounts faster (for Android).
- OLD OP-1 patches load and work on the Field, sounding slightly better due to the 32-bit path. If you want the OG's lo-fi character, use a different tape emulation.

## Verdict
A "really nice update" — flawless in use over a few days, NO pops/clicks on tape lift/drop/overdub/recording or running to outboard gear like the TX-6 (a notable fix vs the original OP-1's tape clicks). One bug noted on this firmware: [Shift]+[1] to show only user presets crashed when scrolling.
