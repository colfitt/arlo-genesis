https://www.youtube.com/watch?v=5y14LwN9oAk
Eventide Audio · Eventide H90 Tutorial - Part 1: The Essential Overview (Joe Cozzi) · 2023-08-16 · 58:37

This is the authoritative "video manual" for the H90 architecture and workflow, presented by Joe Cozzi for Eventide. Cleaned to prose below; parameter names and menu paths are quoted as stated.

## Back panel and basic connections
Four ¼" inputs and four ¼" outputs, each configurable in System Settings > I/O for instrument or line level. Instrument level suits guitars/basses/pedals (high-impedance); line level suits keyboards, synths, audio interfaces, DJ mixers. The LEDs on the LEFT side of the back panel light when any connector is set to line level. Two EXP inputs on the right accept an expression pedal, an aux switch with up to three buttons, or control voltage 0–5 V. USB-C connects to the H90 Control app (curate user lists, manage programs/presets, firmware updates) and can also carry MIDI. Power: supplied 12 V 1 A adapter, 2.5 mm CENTER-POSITIVE, no on/off switch.

Basic guitar rig: guitar to In 1, Out 1 to amp (default is instrument level, no adjustment needed). For stereo, add Out 2 to a second amp — the H90 automatically adjusts algorithms to run in stereo. Mono signal must come from Out 1; stereo from Outs 1 and 2.

## Hierarchy (memorize this)
- **Playlist** — the master user program list, up to 99 Programs.
- **Program** — two algorithms, one in slot A and one in slot B.
- **Preset** — each algorithm slot holds a saved preset (referred to as Preset A / Preset B).
- Algorithms route in **series or parallel** within one of two global routing modes: **Insert mode** (default) or **Dual mode**.

The Playlist is the active set on power-up. To change the Playlist: hold Programs + Routing together a few seconds to enter System Settings > Global > Playlist; turn the first quick knob to browse user lists (ships with four; create more in H90 Control). Only one list can be the Playlist at a time. Factory lists (Ambient, Bass, H9 Max, Lead) live in Programs mode, are ROM/un-deletable, and can be copied into a user list to become a Playlist.

## Play modes
**Select** — press the Select knob to scroll the Playlist (up/down footswitches or the Select knob). Display shows Program name, position, and the two algorithm names with a routing graphic top-right: an arrow = series, two vertical lines = parallel. Footswitch B increments, A decrements; the Active footswitch loads and toggles active/bypass. Quickest exit: press Perform then Select.

**Bank** — hold the Select knob from Select mode. Navigate in banks of three Programs (up to 33 banks of 3 = 99). A footswitch loads a Program; hold B/up or A/down to change banks; hold P to jump back to the first bank. Bank up/down can be mapped to an external 3-button aux switch for faster searching.

**Perform** — up to six configurable footswitches across two pages (toggle pages with consecutive Perform-knob presses, or turn Select). Top-right shows "HKP" = Program HotKnob (a hand-controlled expression knob). Three middle blocks map to P (whole Program), A (Preset A), B (Preset B), each tied to the LED button and footswitch below it. Options include tap tempo, active/bypass, momentary active (m), latching (L), the three HotSwitches, and algorithm-specific performance functions. LED color code: white = active/bypass, aqua = HotSwitch, blue = delay (repeat/feedback osc), red = pitch (e.g. Flex), green = modulation. Recommended practice: page 1 for common functions (active/bypass, tap tempo); page 2 for creative moves (HotSwitches, Freeze, Repeat). You cannot assign Preset B parameters to the P/A footswitches or vice versa — the H90 only offers parameters belonging to the slot in that block.

## Quick Knobs
Three quick knobs below the display in any play mode give instant access to mapped parameters (two pages of three; press a quick knob to view values, press again to toggle pages). Hold a quick knob to enter the assignment list — any parameter across the whole Program (categorized P / A / B) can be mapped. Save the Program before navigating away.

## Programs edit menu
Press Programs. Auditioned Programs auto-load on landing. Three quick-knob filters: List (factory/user/Playlist or "All"), Type (ten effect types as of this video), Algorithm (63 algorithms + two utilities, Mute and Thru). The Thru utility (controls: input gain, output gain, Tails on/off) is a placeholder/isolation tool — the H9 Max factory list represents single-algorithm H9 patches as "[algorithm] + Thru". An asterisk by the Program name = modified/unsaved. Quick save: hold Programs until the number flashes, press Perform twice (overwrites current position). Save to a new spot: hold Programs, turn Select for position (third quick knob switches user list), press Perform, edit name, press Perform to store. Programs can only be saved to user lists. The default Playlist (User 1) is a copy of Factory 1, so an accidental overwrite can be restored by re-saving from Factory 1 into the same User 1 slot.

## Routing menu (Insert mode)
Press Routing for the left-to-right signal-flow diagram. First quick knob sets series vs parallel; pressing it SWAPS preset order (expression mappings follow the presets). Two mono insert loops (or one stereo): quick knob 2 = Insert 1, quick knob 3 = Insert 2; turn right to place the insert and cycle positions. Series positions: Pre-A, parallel-to-both, between A and B (Mid), Post-B. Parallel positions add pre-A, pre-B, post-A, post-B, and in-series before/after both. If both inserts occupy the same position, Insert 1 routes into Insert 2. The last option on Insert 2 is **Stereo insert** (groups both mono inserts).

Insert connections: Insert 1 = Out 3 to device input, device output to In 3. Insert 2 = Out 4 / In 4. Stereo insert = Outs 3/4 to device L/R, device L/R to Ins 3/4. Make connections before activating an insert (avoid pops); mute an insert by pressing its quick knob (2 or 3).

Insert parameters (two pages, turn Select/Perform): Send/Return levels for gain-staging; **Mix** controls the return blend (at 0% the insert acts as a SPLITTER; default 100%); Tails On keeps a looped delay/reverb trailing when bypassed; **Latency (0–512 samples)** and **Polarity** correct comb-filtering when a DIGITAL pedal is inserted at a mix between 0 and 100%.

### Latency calibration procedure (for a digital insert)
1. Bypass the other presets so only the insert path is heard.
2. Invert the insert Polarity.
3. Set insert Mix to 50% (equal parts H90 and insert dry signal).
4. Set the external pedal's Mix so only its dry signal passes (or DSP-bypass it — true bypass won't work).
5. Increase Latency from 0 samples until the signal is silent / as quiet as possible.
6. Disengage Polarity invert. The insert is now time-aligned. (Analog pedals need 0 — they have no appreciable latency.)

## Levels / bypass
Watch input LEDs (dBFS): green = signal present, avoid red (clipping). Match I/O operating level to the connected device. Experiment with Relay vs DSP bypass — DSP bypass adds buffers that fix impedance-mismatch level jumps and restore top end after long cable runs. Program and per-Preset input/output gain range −60 dB to +12 dB (Parameters menu).

## Presets edit menu
Press Presets; consecutive presses switch A/B. Scroll presets with Select/Program (auto-loads on landing). Same three filters as Programs (Factory/User/All, Type, Algorithm) per slot. Save a user preset: hold Presets, rename (quick knob 1 = cursor, quick knob 2 = character + character-set toggle, quick knob 3 = delete), Perform to store; you'll be prompted to overwrite or rename if the name exists. Tip: select the correct A/B slot first.

## Parameters edit menu and HotKnobs
Press Parameters; consecutive presses cycle P / A / B (or use the LED buttons). Quick knobs adjust the three visible parameters; Select pages through parameter banks (varies by algorithm — e.g. H3000 MicroPitch has five pages of three). Program-level controls are consistent: Mix, Input Gain, Output Gain, Tails, Kill Dry. The Perform knob acts as a **HotKnob** per view (HKP/HKA/HKB) — an expression controller mapping one or more parameters at once. A diamond icon = parameter is mapped to a HotKnob or external controller.

To map: navigate to the parameter, hold its quick knob to enter the Parameter Mapping menu; quick knob 2 sets control source (HotKnob, MIDI CC, expression pedal, one of six aux switches, or **Learn** which auto-senses the mover). Next page sets the control range (min/max endpoints). Mapping rules: Program-level params → HotKnob P only; Preset A params → HotKnob A or P; Preset B params → HotKnob B or P; HotKnobs A and B can themselves be assigned to HotKnob P. Recommended workflow: map parameters to HotKnob P, then map HotKnob P to an expression pedal — so you can test with the onboard Perform knob without plugging anything in. HotKnobs A and B can also be assigned to quick knobs in any play mode (e.g. HKA → quick knob 2, HKB → quick knob 3; HKP is always the Perform knob).

## HotSwitches
Three per Program (latching or momentary). Each instantaneously jumps a range of parameters across the entire Program (Program-level + both Presets) to new values; disengaging returns them. Only one HotSwitch active at a time — activating a second is like bypassing the first (no layering unless you build it into one HotSwitch). Program a HotSwitch in the Parameters menu: hold the P LED button = HotSwitch 1, hold A = HotSwitch 2, hold B = HotSwitch 3. Inside, use P/A/B LED buttons to navigate categories, Select to page, and press a quick knob under an unmapped parameter to capture its current value (then turn to set the HotSwitch target value); press again to unmap. Exiting (Perform) auditions the change (parameters revert as if bypassing). Described as "a Program within a Program — three additional Programs for the price of one."

## Building a custom Program
Three approaches: (1) start from a factory Program and edit; (2) load Programs via filters (e.g. all Programs with delays) and customize; (3) use an INIT Program (Thru utility on both slots) and build from scratch. Three factory user lists ship full of INIT Programs; create more in H90 Control. Use Thru as a placeholder while working on the other slot; in parallel routing use the Mute utility on one side to avoid an unwanted dry path while building the other. Loading an algorithm always loads a preset; there are no true "default" presets even when one is named after the algorithm — pick a starting point, make it yours, store it in the preset library for reuse.
