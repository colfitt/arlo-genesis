https://www.youtube.com/watch?v=iruCtkliNUI
Novation · Novation // SL MKIII - Deep Dive · 2018-10-10

The official 48-minute deep dive, presented by Chris (Novation, Brighton studio). The most complete single walkthrough of standalone sequencing, templates, gate/velocity/pattern editing, CV calibration, zones, scales, arp, and Ableton InControl — all demoed against real gear (Novation Peak, Roland SP-404, Octatrack, Make Noise 0-Coast, SH-101, ARP 2600).

## Connections (back panel)
- USB → computer; works with all major DAWs (Ableton, Pro Tools, Logic, Cubase, Reason).
- **DIN Out 1** + a **second MIDI out** that the Global menu can set to **Through OR a dedicated Out**. He uses DIN 1 → Peak → (MIDI thru) → Prophet/FM → SP-404 sampler as one chain; second out → other side of room (Juno, Korg Poly-61, etc.). Keeping two channel-1 devices on separate DIN outs lets them stay independent.
- **2× CV + 2× Gate** (addressed independently) plus **2× "Mod CV"** = CC messages out as voltage to modular.
- **Analog Clock** out, set 1 PPQN up to 24 PPQN (great for modular sync).

## Setting up a sequence + a template
- **Sessions page** = projects (save notes, automation, all parts); color-code; up to **64 slots**.
- **Steps page** = main working view. Hit play → 16 pads under the screens = steps; white "playhead" pad moves across. Records **up to 8 notes per step** (big chords).
- Load a template: **Shift + Sessions** → templates page → 64 slots, with onboard factory mappings + Components-made ones. He loads "Peak":
  - Turn **USB off** (not needed), set **MIDI Out = DIN 1**, set **MIDI channel = 1** (Peak listens on ch.1), pick a part color (blue).
  - Note: CV/Gate controls grey out because they're off for this part — keeps it exclusive to MIDI.
- Back on Steps, the screens now label Peak params (cutoff, reverb, etc.) on the encoders — control the synth without reaching for it.

## Automation (per part, 8 lanes)
- Hit **record**, move an encoder → that movement is captured to an automation lane. **Clear** + wiggle the pot removes it.

## Building a beat (SP-404 example)
- Next part → **Shift + Templates** → choose a generic basic MIDI mapping → USB off, DIN 1 on, **MIDI ch.4** (SP-404), orange color.
- Tap a step + a note to place a kick; or hit **record** and live-play snare/hats in.
- To erase: press the step (red LEDs show which notes are on it), tap the note to remove it.

## Multiple devices + mute/solo arranging (Octatrack example)
- Next part → Octatrack template → **MIDI DIN 2**, **MIDI ch.1**. Powerful point: Peak on DIN1-ch1 and Octatrack on DIN2-ch1 stay completely separate because they're on different physical DIN outs.
- The **16 top buttons** have layers navigated by the arrows; on the Octatrack mapping the top row are **mute switches** — unmute parts one at a time to build an arrangement live. Mute/solo also exists globally (top button layer says "mute/solo").
- He also maps two buttons in the Octatrack template to move the **focused device** on the Octatrack (via **Grid** mode — toggle with the Grid button to swap pad function between steps and the assigned mappings).

## Per-step gate length, velocity, and pattern controls (Options page)
- **Options → Gate**: screens show steps 1–4 (arrow down for 5–8, 9–16). Set a step to e.g. 6 steps long to draw a chord out; another to 2 steps. Press a step to see all its notes and set **individual note gate lengths** (one note in a chord short, others long).
- **Options → Velocity**: per-note velocity values per step.
- **Options → Pattern**: length (1–16), start point, **direction** (forward / backward / ping-pong / random).
- **The "secret weapon" — sync rate, set PER PATTERN not per part**: default 1/16 = 16 steps = one bar. Set 1/32 → half a bar; 8th, quarter-note triplets, 8th-triplets, 16th-triplets; or quarter notes → each step = 1 quarter note → 16 steps = **4 bars** in one pattern. Demonstrated that Peak pattern 1 can be at quarter-note sync while Peak pattern 2 is at 1/16 — **8 independent patterns per part, each with its own sync rate, length, direction, start/end.**

## CV + tuning (Make Noise 0-Coast example)
- New part → Components-made "0-Coast" template → USB off, MIDI off, **CV/Gate set to CV Gate 1**. (Channel irrelevant when MIDI is off.)
- The 0-Coast plays out of tune vs the Peak. Fix via **Global → Analog settings → Calibrate**: enter tuning page, the SL outputs reference note **A2** then a high reference; he opens Ableton's Tuner, plays low A2, dials the calibration until it reads A, repeats for the high octave, hits **Apply** to save CV1 calibration. (Playing with the scaling deliberately yields microtonal scales.)
- Also maps **CV1 Mod output → 0-Coast decay** and records that as automation.

## Zones
- **Zones button** → management page; **Shift + Zones** turns them on (key LEDs match part colors). Per zone: destination part (or "off" or "follow selected part"), low key, high key — up to **8 zones**. Demo: Zone 1 = top half → Peak; Zone 2 = bottom → 0-Coast. Doubles as a sound-design split (Peak full range + 0-Coast on bottom half = layered).

## Scales
- **Scales button** → **Shift + (on)** to enable. **Snap** (wrong notes snap to nearest right note — can't play wrong), **Filter** (wrong notes don't trigger), **Display-only** (all notes play, LEDs only guide). Choose scale type + root. Also **transposes sequences**, settable for one or all tracks (careful: applying a scale to a drum part on different MIDI notes changes which samples fire).

## Arpeggiator
- **Shift + Arp** on; **Arp** button = menu. Route to a specific part or follow-selected. Types: up / down / up-down / up-down (repeat top+bottom) / random / played / chord. Gate control + **sync rate** (triplets, 8ths up to 32nd triplets, or down to 1/1 = each step a full bar). The arp rhythm grid lets you turn individual steps on/off and set odd lengths for strange rhythms. **Latch** frees your hands to tweak the synth engine.

## Ableton InControl
- Hit **InControl** → full device access. He makes a Components "Ableton" template on **MIDI ch.6, USB only** so Ableton listens to that specific channel rather than all sequencer data. Record-enable the track, play the instrument; switch parts to play a drum rack on the same ch.6.
- **Grid** mode → 16 velocity- + aftertouch-sensitive pads trigger/control the drum rack. Exit grid → pads become **clip launchers**; **Shift + clip** stops a clip; grab multiple clips to layer. Faders = track volume.
- **Device control**: press-and-hold **Options** to see a track's devices (he adds Auto Filter + Ping Pong Delay); encoders control the focused device's params; the down arrows page through additional param pages.
- Duplicate / Clear / Save section duplicates and clears clips. **Shift** reveals click on/off, undo, redo, and **Capture** — plays an idea freely, hits Capture, and it materializes the just-played part as a MIDI clip.
- Closing thesis: with Ableton + the SL as centerpiece, "pretty much anything in this room can be just directly connected" — a full 8-part sequencer with a keyboard attached is the headline.
