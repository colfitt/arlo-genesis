https://www.hologramelectronics.com/pages/chroma-console-manual
hologramelectronics.com · Hologram Electronics (official manual, Firmware v1.04) · accessed 2026-06-03
(cross-checked against on-disk `manuals/ChromaConsole.pdf`, COPY/SAVE PRESETS pg. 31–33 and BROWSING PRESETS pg. 34)

# How Chroma Console presets / banks / saving / sharing work

**Headline finding: Hologram presets are RECIPE-ONLY. There is NO official preset file format, no
official import/export, no first-party companion app, and the pedal CANNOT dump or report its own
state.** Like the Microcosm, an on-device "preset" lives only as state you dial by hand and save to
a slot; official sharing = sharing knob positions (a recipe), not a file. (Verified across the
official manual, the product page, and the only commercial pack — even that paid pack ships as a PDF
of knob positions, not a file. No source found describing any official sysex/USB preset dump.)

**Caveat (unofficial workaround):** a community Web-MIDI editor — **Chroma Controller**
(chromacontroller.co.uk, by Edward Denholm) — CAN save/load a settings snapshot file (knob
positions, module selections, bypass states) and "share the preset with your friend." So
file-based sharing IS possible *through that third-party tool*, sent to the pedal over MIDI CC.
Big limitation per the developer: it's **one-way (editor → pedal)** — the pedal does not report
state back, so after you touch a hardware knob the editor's display silently desyncs. See the
sibling capture file `chroma-console-community-editors-web-and-m4l.md` for the editor details.

## Preset structure
- **80 user presets** = **4 banks (A/B/C/D) × 20 slots**. Slots 1–20 per bank; the four buttons
  pick the bank, the 4 LED bars pick the slot.
- **Ship state: all 80 slots are EMPTY (blank).** There are NO pre-loaded factory/artist presets
  out of the box. (The "preset browser" is the 80 user slots; empty slots flash white.) So "factory
  presets" as a downloadable concept does not exist for this pedal.

## What a saved preset stores (verbatim, manual pg. 31)
- Effects & Module Routing
- All primary control settings
- All secondary control settings
- **All Gesture recordings** ← GESTURE knob-motion automations ARE saved per preset
- Filter Style
- Dual Bypass Settings
- Capture Routing
- Expression control mapping
- Tapped tempo

> **NOTE for the dossier:** GESTURE recordings save with the preset; **CAPTURE (looper/sustainer)
> recordings do NOT** (manual: "CAPTURE recordings are not saved within user presets"). The dossier
> currently says only "Captures are not saved in presets" — worth adding that *gestures are*, so a
> scene-recalled preset brings its automated knob motion back with it.

## Saving / overwriting (COPY/SAVE menu)
1. **Press B + C simultaneously** — copies the active (live) preset and arms it for saving.
2. Scroll to the target bank/slot with the **AMOUNT knobs or the footswitches**. Empty slot = buttons
   flash white; occupied slot = buttons light in the saved effects' colors AND that preset becomes
   active so you can audition before overwriting.
3. **Press B + C again** to save/overwrite — a teal animation confirms.
4. To cancel: press & hold BYPASS (red animation; copied settings restored).

## Loading / browsing presets (PRESET BROWSER)
- **Press & hold the BYPASS footswitch** to enter the browser (wiping animation).
- Buttons show the bank; the 4 LED bars show the slot. Controls are disabled while browsing.
- **To load:** press & hold BYPASS or TAP while the desired preset is selected.
- By default presets auto-audition as you scroll; **disable "Preset Browser Audition" in Global
  Settings** for live use so the current sound persists while scrolling (good live tip — pairs with
  the dossier's "preset switching is clunky live, drive via MIDI PC" note).

## MIDI recall (the practical live path)
- Highly configurable MIDI over **5-pin DIN + USB-C**: clock sync, full CC, and **instant preset
  recall via Program Change**. MIDI listen channel set in Global Settings (TILT knob; default Ch 1).
- This is the supported way to scene-recall a Chroma preset alongside the rest of a MIDI rig —
  there is no other "transfer." (Confirmed by Morningstar MC6 Pro / MC8 user-forum threads that
  drive Chroma preset changes via PC.)
- Firmware v1.04 added **MIDI CCs for module bypass/engage**.

## Reset
- Factory reset (hold A+B+C+D until pulsing orange) **clears all user preset banks** and resets
  globals. There is no "restore factory presets" because there were none — reset just empties slots.
