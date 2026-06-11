---
type: guide
title: "Load VocalShiftMIDI as Preset A"
device: Eventide H90
date: 2026-06-11
---

## Step 1 — Confirm your firmware is v1.10 or later

VocalShiftMIDI was added in firmware v1.10 (April 2025) and will not appear on older firmware. Hold the **Programs** button and the **Routing** button together for a few seconds. The display enters **System Settings**. Turn the **Select** knob (the large left encoder) until you see the firmware version number. If it reads v1.10 or higher, you are good — press **Perform** (the large right encoder) to exit. If it is lower, connect the H90 to a computer via USB-C and update through the free H90 Control app before continuing.

```controls
- { name: "Programs + Routing (hold)", type: button, value: "System Settings screen" }
- { name: "Perform", type: button, value: "press to exit System Settings" }
```

## Step 2 — Get to a Program you want to edit

From the main screen (the display shows a Program name, number, and two algorithm names), turn the **Select** knob left or right to scroll through your Playlist. Land on the Program where you want to load VocalShiftMIDI into slot A. The Program loads automatically as you scroll — you will see the name change on the display.

```controls
- { name: "Select", type: knob, value: "turn to scroll Programs" }
```

## Step 3 — Open the Presets browser

Press the **Presets** button (the third button from the left in the row of four above the quick knobs). The display switches to the Presets browser and shows a list of presets with filter labels above the three quick knobs.

```controls
- { name: "Presets", type: button, value: "Presets browser opens" }
```

## Step 4 — Make sure you are editing slot A

Look at the top of the display. It will say **A** or **B** to indicate which slot you are browsing presets for. If it says **B**, press **Presets** one more time — consecutive presses toggle between slot A and slot B. Stop when the display shows **A**.

```controls
- { name: "Presets", type: button, value: "display shows A at top" }
```

## Step 5 — Filter by Algorithm to find VocalShiftMIDI

Turn the **third quick knob** (the rightmost knob below the display — it is labeled **Algorithm**). Scroll until the display reads **VocalShiftMIDI**. The preset list on screen narrows to show only presets that use the VocalShiftMIDI algorithm.

```controls
- { name: "Algorithm filter (Quick Knob 3)", type: knob, value: "VocalShiftMIDI" }
```

## Step 6 — Pick a preset and let it load

Turn the **Select** knob to scroll through the available VocalShiftMIDI presets. Each one auto-loads as you land on it — the preset name appears on the display and the algorithm is now live in slot A. Pick whichever sounds like a useful starting point.

```controls
- { name: "Select", type: knob, value: "turn to browse presets — each loads on landing" }
```

## Step 7 — Verify the load on the main screen

Press **Perform** to exit the Presets browser and return to the main play screen. The display now shows the Program name with **VocalShiftMIDI** listed as the algorithm in the **A** slot. If you see a different algorithm name under A, repeat from Step 3.

```controls
- { name: "Perform", type: button, value: "main screen shows VocalShiftMIDI under slot A" }
```

## Step 8 — Save the Program

Hold the **Programs** button until the Program number on the display starts flashing. Press **Perform** twice to overwrite the current Program slot. The display stops flashing — your Program now has VocalShiftMIDI saved in Preset A. Programs can only be saved to user lists, not Factory lists.

```controls
- { name: "Programs (hold)", type: button, value: "Program number flashes" }
- { name: "Perform (press twice)", type: button, value: "display stops flashing — saved" }
```

## Sources

- `gear/Eventide H90/GearProfile.md` — device summary, power spec (12 V center-positive)
- `gear/Eventide H90/research/links/eventide-h90-harmonizer-plus-vocal-algorithms.md` — VocalShiftMIDI parameter list, firmware v1.10 requirement
- `gear/Eventide H90/research/H90-UsageGuide.md` — hierarchy (List > Program > Preset > Algorithm), Harmonizer+ algorithm overview
- `gear/Eventide H90/research/H90-DeepResearch.md` — controls layout (Select/Perform encoders, quick knobs, mode buttons), play modes, firmware history
- `gear/Eventide H90/research/transcripts/eventide-official-h90-tutorial-part1-essential-overview.md` — Presets browser navigation, Algorithm filter on Quick Knob 3, auto-load on scroll, A/B slot toggle, save procedure
