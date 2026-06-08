https://components.novationmusic.com  +  https://support.novationmusic.com/hc/en-gb/articles/360012446819-SL-MkIII-Components-Template-Editor-Guide  +  Manual: SL MkIII User Guide V2, pp.13–14, 28
support.novationmusic.com / userguides.novationmusic.com · Novation · Components Template Editor Guide (firmware-current)

# Building a Template in Novation Components (the only place templates are made)

## What a Template controls (mapping data, per Template)
A Template defines what MIDI each control sends, on which **MIDI channel** (per-control, no global channel), to which **destination** (set on the SL itself in Part Settings, not in the template). One Template holds maps for:
- **16 Rotary knobs** (8 physical encoders across **two pages/banks** → 16 addressable)
- **16 Pads** — both **hit** (note/velocity) and **pressure** (aftertouch/CC) mappable separately
- **8 Faders**
- **16 Buttons** (the 8×2 soft-button area, two banks)
- **Modulation wheel**, **Pitch wheel**
- **Footswitch, Expression pedal, Sustain pedal**
- (Keybed velocity/aftertouch behaviour is set on-hardware + Global, not in the template.)

The SL holds **64 Templates** on board. Parts reference a Template by name/number.

## How to get Components
- Web app at **components.novationmusic.com** — needs a Web-MIDI browser (**Chrome / Edge / Opera**; not Safari/Firefox).
- **Standalone** desktop app — download after registering the SL; works offline. Same editor.
- You can build/edit a template **with or without the SL connected**; you only need it connected to **send** the template to the unit (over SysEx) and to update firmware.

## Per-control parameters you set in the editor
For each control, choose a **message type** and its sub-settings:
- **CC (Control Change)** — pick **CC number 0–127**, **MIDI channel 1–16**, **Low Value** and **High Value** (default 0 / 127; set them to scale or invert a control's range — Low>High inverts), and **behaviour**:
  - Rotaries: **absolute** or **relative** (endless-encoder relative modes for DAW-style param nudging).
  - Buttons/pads: **toggle** vs **momentary** (and value sent on press/release).
- **NRPN** (firmware 1.2+) — for high-resolution / extended params on synths that use it.
- **Program Change** (+ optional **Bank Select MSB/LSB**) — for patch/memory switching on external boxes.
- **Note** — pads (and buttons) can fire notes with a chosen note number + velocity; pads also send velocity from the hit.
- **Channel pressure / aftertouch** routing for pad pressure.
- **MMC / transport**-type messages where applicable.
- **Off** — disable a control: its LED/screen goes blank to show it's unmapped.

CC is "a MIDI message capable of transmitting 0–127"; Low/High let one physical control sweep only part of a parameter's range (e.g. fader 30→100 only).

## Workflow (concrete)
1. Open Components (web/standalone), pick **SL MkIII**, **New Template** (or duplicate a factory one).
2. Click a control on the on-screen surface to highlight it; set **type / CC# / channel / low / high / behaviour** in the side panel.
3. Repeat across knobs (both pages), faders, buttons (both banks), pads (hit + pressure), wheels, pedals.
4. **Name** the template (else it shows as "Template X" on the SL).
5. **Send to SL** — connect via USB, push the template into one of the 64 slots (SysEx transfer; SL enters "Content Transfer Mode," transport stops, screen shows progress).
6. On the SL: **Shift + Sessions** = Templates view → assign that Template to a Part (left-most rotary), set the Part's **Channel** (rotary 6) and **Destination** (USB / DIN1 / DIN2 / Both / CV-Gate).

## Notes for this rig
- The template only carries *message + channel + range*. **Which physical port** it goes out (USB vs DIN1 vs DIN2 vs CV) is a **Part Setting on the SL**, stored in the Session — so one template can drive a DIN pedal in one Session and USB soft-synth in another.
- Because editing is point-and-click and computer-bound, batch your CC maps in one sitting; see `int-libslmkiii-library.md` for a text/programmatic alternative.
- Glossary reference (message types, value ranges, behaviour modes): support article 360005133340 (Components SL MKIII Template Editor Glossary) — same parameter set as above; 403s to automated fetch, viewable in a browser.
