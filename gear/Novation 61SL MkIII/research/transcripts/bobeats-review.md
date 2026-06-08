https://www.youtube.com/watch?v=bh1xtuUgifw
BoBeats · Novation SL MkIII REVIEW — Almost Perfect MIDI Keyboard & Sequencer · 2018-10-10

A 34-minute hands-on review from a heavy Circuit user, framing the SL MkIII as "Circuit sequencer + KeyStep + screens/encoders/faders + DAW integration." Strong on the Circuit-lineage workflow and honest limitations. (Cubase used for the DAW section, so DAW notes are Cubase-specific.) Includes a "future Bo" correction confirming the see-notes-while-playing feature shipped in release firmware.

## His multi-device setup
- 8 parts: Part 1 = Novation Peak, Part 2 = Matrixbrute (through an Erica Black Hole DSP), Parts 3–6 = Digitone (4 parts for its 4 tracks), Part 7 = Digitakt, Part 8 = (Make Noise) Erica/Eurorack via CV.
- For Digitakt/Eurorack he uses **one part** and drops octaves to reach individual tracks/sounds, rather than a part per sound. Part color shows on the keybed LEDs.
- CV: **2× CV/Gate + 2× Mod** outputs (two voices). Per part you choose USB / MIDI out 1 / 2 / both, MIDI channel, and whether it sends to CV/Gate.

## Screens / encoders
- Screens show the template name per part; 8 encoders × 2 (up/down arrow) = 16 params per synth. Blank rows = nothing mapped on that template page (easily added in Components). Faders show values on-screen when moved.
- **Factory templates ship onboard** (TR-8S, Octatrack, Sub 37, OB-6, Big Sky, Digitone, Blofeld, Digitakt, etc.) — he praises having mappings ready out of the box; empty slots for your own. Load via **Shift + Sessions**.
- Bottom buttons: mute states (mutes the sequence) + solos; arrow-down for additional programmable CC buttons.

## Sequencer (Circuit DNA)
- **Sessions** = collections of patterns for song sections (no session-chaining mode yet — on his wishlist). Each saves all part + pattern data.
- **Patterns view**: 8 patterns per part like the Circuit, but you can only see two parts at once (normal) or, with **Shift + Pattern**, two patterns per part across all parts (expand). His main dislike is this limited overview vs the Circuit showing all 8 patterns × all channels.
- **Build**: pick a part (transpose down for Digitakt sounds), hold a step + place a trigger; **live record** like a Circuit. Pressing a step shows the notes on it (easier than Circuit thanks to the big keybed) — good for chords.
- **Per-pattern options**: pattern length (start/end position), play mode (forward/backward/ping-pong/random), and **sync rate** (1/16 → 1/32 etc.).
- **Gate/velocity per step**: Options → Velocity / Gate; you set values via the encoders, top row = steps 1–8, scroll down for 9–16. For an arp chord he set step 1's gate to 16 steps so the chord rings the whole pattern. (He'd prefer hold-step-and-tweak-gate directly rather than a menu.)
- **Automation**: 8 lanes per part; live-record encoder moves (frequency/resonance) or step-automate by pressing a step + changing value. NOTE: automation is a **curve**, not Elektron-style p-locks — setting a value on one step changes other steps that have no automation.

## Arpeggiator
- **Arp** button → grid + options; turn on, set part (Peak). Edit the arp rhythm via the grid, plus type (up/down/random/played/chord), gate, sync, octaves, latch. **Only one arp** — can't run different arps on different parts.

## Scales + Zones
- **Scales**: root note, scale type, sequence transpose, mode. **Shift + Scale** = Snap (forces to scale) or Filter (mutes off-scale greys).
- **Zones**: up to 5 (he demos) / 8 total; **Shift + Zone** to enable; combine with scales to record a loop over the drums across split instruments (Peak / Matrixbrute / Digitone).

## CV setup specifics
- Templates menu: USB on/off, MIDI out 1/2/off/both, and which CV/Gate this part sends to. **"Both" setting** sends the same pitch+gate out both pitch/gate outs — AND is **required to use both Mod outputs from one part**.
- **Global menu → CV Mod outputs**: assign each mod output a CC number (he used 21 + 22 to match his first two template encoders). Set **CV Mod range** independently per output: **0 to +5V or −5 to +5V**.

## Cubase InControl
- Press **InControl** → screens show track names; navigate with prev/next part buttons; **updates in real time** — reorder a track in the DAW and it reorders on the keyboard (two-way). Transport, arm (hold for multiple), solo, mute, volume faders. Encoders default to pan; Options → pan + send levels — but limited. Caveat: muting a MIDI track doesn't mute the corresponding VST audio track in Cubase. He hopes Novation builds out Cubase support (Ableton/Reason are better supported).

## Components
- Get-from / send-to SL; rename + color sessions; save to cloud/PC. **Template editor** to build custom templates (he makes a Matrixbrute one): per control choose CC / NRPN / note / Program Change; covers faders, buttons, pads (the Grid pads), wheels, pedals (sustain/footswitch/expression).

## Likes / dislikes / wishlist
- **Likes**: hands-on workflow, the sequencer, factory templates make it a great studio centerpiece, tight DAW integration.
- **Main dislike**: can't see all patterns/parts at once — easy to lose track of the arrangement; hard to do uneven pattern counts across tracks.
- **Wishlist**: longer patterns (≥64 steps via arrow-key pattern pages), session chaining, note-tie, micro-steps + step shift (Circuit features — important because grid-quantized notes feel rigid; micro-steps add human/fluid groove), faster gate-length editing, and loadable **MIDI effects** (MIDI LFO modules beyond just the arp). NOTE: a "future Bo" insert confirms see-notes-while-playing shipped in release firmware.
- Alternatives: Circuit (built-in synths/samples), KeyStep / BeatStep Pro (cheaper standalone sequencing), Komplete Kontrol S-series Mk2 (if you don't need the sequencer).
