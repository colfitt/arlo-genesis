---
type: guide
title: "Load Blackhole into Preset B on the Eventide H90"
device: Eventide H90
date: 2026-06-11
---

# Load Blackhole into Preset B on the Eventide H90

This guide walks you through loading the Blackhole reverb algorithm into slot B of your current Program, dialing in a starting sound, and hearing it. Every step is one physical action on the pedal.

**Before you start:** plug your guitar into In 1, run Out 1 to your amp (or Out 1 + Out 2 for stereo), and power up with the supplied 12 V center-positive adapter. The pedal boots into Select mode — you will see a Program name and number on the OLED screen.

---

## Step 1 — Open the Presets menu

Press the **Presets** button (the right-hand button in the top row of four, labeled on the panel). The screen changes to show the Preset browser for slot A — you will see the Preset A name and the three filter knobs below it (List, Type, Algorithm).

```controls
- { name: "Presets", type: button, value: "Preset A browser visible on screen" }
```

## Step 2 — Switch to Preset B

Press the **Presets** button again. The screen switches to the Preset B browser — the display now shows the B slot name. Consecutive presses of Presets toggle between A and B.

```controls
- { name: "Presets", type: button, value: "Preset B browser visible on screen" }
```

## Step 3 — Filter by algorithm type

Turn **Quick Knob 2** (the middle knob in the bottom row of three) until the Type filter reads **Reverb**. This narrows the list to reverb presets only.

```controls
- { name: "Quick Knob 2", type: knob, value: "Reverb" }
```

## Step 4 — Filter to the Blackhole algorithm

Turn **Quick Knob 3** (the right-hand knob in the bottom row) until the Algorithm filter reads **Blackhole**. The list now shows only presets built on the Blackhole algorithm.

```controls
- { name: "Quick Knob 3", type: knob, value: "Blackhole" }
```

## Step 5 — Scroll to a Blackhole preset and load it

Turn the **Select** knob (the large left encoder on the top panel) to scroll through the available Blackhole presets. Each preset auto-loads as you land on it — you will hear the reverb change in real time as you scroll. Pick the one named "Blackhole" (or whichever factory preset you like as a starting point).

```controls
- { name: "Select", type: knob, value: "Scroll until 'Blackhole' preset name appears" }
```

## Step 6 — Open the Parameters menu for Preset B

Press the **Parameters** button (the far-right button in the top row). Then press the **B LED button** (the small lit button above the right footswitch) so the screen shows Preset B's parameters. You should see the first page of Blackhole controls — typically Mix, Decay, and Size.

```controls
- { name: "Parameters", type: button, value: "Parameters menu open" }
- { name: "B LED button", type: button, value: "Preset B parameters shown on screen" }
```

## Step 7 — Set the Mix

Turn **Quick Knob 1** (the left knob in the bottom row) to set Mix. Start around **65%** — this blends the Blackhole reverb with your dry signal. (If your Program's Kill Dry is ON, Mix controls the reverb level alone.)

```controls
- { name: "Quick Knob 1", type: knob, value: "65%" }
```

## Step 8 — Set the Size

Turn **Quick Knob 3** (the right knob) to set Size. Start at **90** — this gives Blackhole its signature enormous, cosmic space.

```controls
- { name: "Quick Knob 3", type: knob, value: "90" }
```

## Step 9 — Page to the Gravity and Feedback controls

Turn the **Select** knob to page through Blackhole's parameter banks until you see **Gravity** (the decay control) and **Feedback**.

```controls
- { name: "Select", type: knob, value: "Page until Gravity and Feedback are visible" }
```

## Step 10 — Set Gravity

Turn the Quick Knob under **Gravity** to about **3:00**. Gravity controls decay length — turning it right gives longer, denser tails. "Inverse" values (turning left past noon) reverse the envelope for swells.

```controls
- { name: "Gravity Quick Knob", type: knob, value: "3:00" }
```

## Step 11 — Set Feedback

Turn the Quick Knob under **Feedback** to about **2:00**. This recirculates the reverb tail. Turning fully clockwise reaches **Infinite** (tail sustains forever but still accepts new input), and the last fraction of travel past Infinite is **Freeze** (tail locks, no new input enters). For now, keep it below Infinite — you can explore Freeze later.

```controls
- { name: "Feedback Quick Knob", type: knob, value: "2:00" }
```

## Step 12 — Play and listen

Strum a chord or play a note. You should hear a massive, long-tailed reverb bloom behind your dry signal. The Blackhole algorithm produces a soft attack with a lingering, harmonic tail — the space should sound "cosmically epic," not like a normal room.

## Step 13 — Save the Program

Hold the **Programs** button until the Program number on screen begins to flash. Then press the **Perform** knob twice to quick-save in place. The flash stops — your Program is saved with Blackhole in slot B.

```controls
- { name: "Programs", type: button, value: "Hold until number flashes" }
- { name: "Perform", type: button, value: "Press twice to confirm save" }
```

## Step 14 — Return to play mode

Press the **Perform** knob once, then press the **Select** knob once. You are back in Select mode, ready to perform. The B footswitch toggles Preset B (Blackhole) active or bypassed.

```controls
- { name: "Perform", type: button, value: "Press once" }
- { name: "Select", type: button, value: "Press once — back in Select mode" }
```

---

## Where to go next

- **Freeze a drone:** In Perform mode, turn Feedback fully clockwise past Infinite to Freeze — the reverb tail locks and you can solo over it. Map this to a footswitch for hands-free control.
- **Stack two effects:** Slot A is still available. Load a delay or pitch algorithm there and route A into B (series) for a delay-into-Blackhole or shimmer-into-Blackhole wall.
- **Adjust low end:** Page through Blackhole's parameters to find Low Level — turn it down slightly to keep the bass from clouding the tail.

---

## Sources

- `gear/Eventide H90/GearProfile.md` — device metadata, power specs, summary
- `gear/Eventide H90/research/H90-UsageGuide.md` — workflows, Blackhole settings, Freeze/HotSwitch mapping, hierarchy
- `gear/Eventide H90/research/H90-DeepResearch.md` — Blackhole algorithm description (Size, Gravity, Feedback/Infinite/Freeze behavior), controls and architecture, play modes
- `gear/Eventide H90/research/transcripts/eventide-official-h90-tutorial-part1-essential-overview.md` — Presets menu navigation, Parameters menu, quick-knob mapping, save procedure, play modes
- `gear/Eventide H90/research/links/h90-ambient-pad-settings-recipes.md` — Blackhole starting values (Size 90, Feedback ranges, Mix ranges)
- `gear/Eventide H90/research/links/eventide-forum-freeze-drone-holds.md` — Blackhole Freeze via Feedback fully clockwise, mapping to footswitch
