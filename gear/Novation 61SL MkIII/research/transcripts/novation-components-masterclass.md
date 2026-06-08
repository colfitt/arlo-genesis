https://www.youtube.com/watch?v=fGXcvTnXHRM
Novation · SL MKIII - Making the most of Components to master your hardware // Novation Live · 2020-09-09

The definitive Components walkthrough (presented by Calc, Novation). Covers Components as both a **librarian** (backup/organize Sessions + templates) and a **template editor**, then builds a full template for a Novation Summit from scratch — demonstrating every control type (CC, high-res CC pairs, NRPN, increment/decrement buttons, Program Change, poly-aftertouch faders). This is the practical "how do I map the VG-800 / a Chase Bliss pedal" reference.

## Components basics
- Two free formats: **standalone app** (novationmusic.com) and **cloud** (Chrome/Opera browser — log in, access all your backups/templates anywhere).
- For the SL MkIII it does two jobs: a **librarian** (back up + organize the 64 Sessions and the templates) and a **template editor** (create/edit hardware mappings). It is **NOT a session editor** — you can't move/correct MIDI notes or automation in Components; all that editing is done on the hardware. Components only backs up/archives.

## Librarian workflow
- **Get pack from SL MkIII** pulls all 64 sessions (takes a moment). Sessions show their hardware labels (e.g. "Chris", "user two", "starting point").
- **Rename** a session in software (you can't rename on hardware), then **send** back: either "Send SL MkIII to SL MkIII" (whole pack) or send a **single session** to a chosen slot. Tip: you must know the target slot number — use the hardware to scroll to the right session first (e.g. send to slot 63).
- **Color-code** sessions; note the computer view only updates after you re-retrieve. Drag sessions to **reorder/swap** slots. Group four sessions as green + name them "part 1–4" for a live set so co-joined sessions are obvious on hardware.
- **Save as** a named pack ("stream pack"); filter the list by deselecting the Novation factory pack or user packs; **pack settings** to recolor; delete + **restore from trash**.
- Templates can also be reordered, edited, sent, replaced, or downloaded from the librarian; clicking **Edit** on a template (e.g. Octatrack) jumps into the template editor (faders show track-1 volume, track-2 volume, etc.).

## Template editor — building a Summit template from scratch
Workflow pattern repeated for each control: edit in Components → **Send to SL MkIII** → choose **Part** (not template-name) → send to **Part 1**, which overwrites a known empty "default" template. Calc's strong tip: **send to a PART, not a template slot** — the template list shows no slot numbers, so saving over the empty default loaded on Part 1 is the reliable way to know where it lands.

Setup: load an empty **default** template on the hardware (Shift + Sessions → scroll to "default"), USB off, MIDI on **DIN 2**, **MIDI ch.15** (Summit), initialize the Summit to a single sawtooth.

**Rotary encoders** (two banks: top row = Bank 1 = CC21–28-ish; Bank 2 = CC31+; 16 total):
- **Simple CC**: Encoder 1 = "amp attack" → look up Summit manual CC list → **CC 86**, 128 values (0–127), 7-bit, default channel. Name it "amp attack."
- **High-resolution CC pair**: Encoder 2 = "filter cut" → Summit filter frequency uses a CC pair (CC 29 + CC 61). In Components set CC **29**, change resolution to **8-bit scaled**, max value **255** (256 values). The SL automatically pairs CC 29 with CC 29+32 = CC 61 for the extra resolution. (14-bit also available for even higher resolution.)
- **Bipolar CC pair**: Encoder 3 = "LFO1 → filter" CC **28**, 8-bit, 255, pivot at center (0 = no LFO).
- Encoder 4 = "LFO1 speed" CC **30**, 8-bit scaled (LFO1 rate pair 30/62).
- **NRPN** (for params beyond the 128 CCs): saw density uses NRPN — set assignment type **NRPN**, two fields **MSB 0 / LSB 17**, 7-bit (only 128 values needed). Saw detune = NRPN 0/18.

**Buttons** (right-side 16 buttons): behaviors = momentary / toggle / **increment** / **decrement** / trigger.
- "Wave" up/down: set one button to increment, **Pair** it with another set to decrement, so two buttons step a value up/down like cursor keys. Map to oscillator-1 wave (NRPN 0/14) with value range **0–4** (5 wave shapes: sine, triangle, saw, square, wavetable) — not 0–127.
- **Program Change** via paired increment/decrement buttons steps through Summit patches. Crucially this also works **in the sequencer**: hit record, press a step, and step in a Program-Change automation value — so patch changes can be sequenced per step. Also triggerable by pressing the pad.

**Faders**: can send CC, NRPN, **Channel Pressure**, or **Program Change** (a fader instantly gives 128 PC values for jumping around patches). Clever trick — set 8 faders to **Poly Aftertouch** on notes 41–48; with 8 notes latched, route the Summit's aftertouch → osc-1 pitch in the mod matrix, and the faders become a per-voice "swarm oscillator" detune control.

**Pads** (Grid mode): two stages — **hit** (CC / NRPN / note / Program Change / Song Position) and **pressure/aftertouch** (CC / Program Change / Channel Pressure / Poly Aftertouch). The grid comes pre-set with poly-aftertouch.

**Wheels / Pedals / Keys**: mod wheel = assignable CC. Three pedal inputs (**Sustain, Footswitch, Expression**) each assignable. Key **aftertouch** assignable to CC / NRPN / Channel Pressure / Poly Aftertouch — note the keybed is NOT a poly-aftertouch keyboard, but you can route its channel aftertouch to a poly-AT message on a specific note.

## Practical takeaway for this rig
This is exactly the process to map the **VG-800** or a **Chase Bliss pedal**: find the device's CC/NRPN list in its manual, build encoder/fader/button mappings in Components, name them, and **send to a Part** to overwrite a known empty template. Use CC pairs/14-bit for smooth filter/param sweeps, NRPN for params past 128, increment/decrement button pairs for waveform/preset stepping, and Program-Change-in-sequencer to automate patch changes per step.
