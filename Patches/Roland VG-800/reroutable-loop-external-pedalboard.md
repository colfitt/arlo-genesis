---
type: patch
title: "Re-Routable S/R Loop — external pedalboard inserted anywhere"
device: Roland VG-800
date: 2026-06-15
description: "A routing/template patch — exploit the VG-800's stereo SEND/RETURN loop, re-routable to ANY point in the chain, to drop an entire external pedalboard (or second unit) into the model's signal path. Elantric's post-NAMM \"my demand\" feature on VGuitarForums; Gear Sounds ran a VG-800 + RT-2 through it in full stereo as a worked example."
tags: [performance, loop, stereo, community, template]
dips:
  SEND/RETURN: "stereo TRS (standard SEND/RETURN)"
  WARNING: "a stereo-collapsing block downstream kills upstream per-string PAN"
controls:
  - { name: "S/R loop block placement", type: switch, value: "in EFFECTS view, drag the S/R loop block to the chain position where you want the external gear inserted (freely placeable, unlike CHO/DLY/REV)" }
  - { name: "Loop MODE", type: switch, value: "NORMAL (send/return), stereo" }
  - { name: "External patch point", type: switch, value: "connect external pedals/board to the stereo TRS SEND/RETURN" }
---

# Re-Routable S/R Loop — external pedalboard inserted anywhere

## Concept

Exploit the VG-800's stereo SEND/RETURN loop — re-routable to ANY point in the chain — to insert an entire external pedalboard (or another unit) at a chosen spot in the model's signal path. This is Elantric's post-NAMM "my demand" feature: place dirt/time effects before or after the modeled amp at will. It's a routing block, not a sound — no tonal values, just where the loop lives.

## How to play it

1. In the EFFECTS view, move the S/R loop block to where you want the external gear inserted — it's freely placeable, unlike CHO/DLY/REV.
2. Patch your external pedalboard / second unit into the stereo SEND/RETURN (standard TRS).
3. Place it pre-amp to color the model's input, or post-amp for time/space — your choice.
4. Worked example: Gear Sounds ran the VG-800 + an RT-2 in full stereo through this loop.

## Notes

- Confirmed real and re-routable: "The VG-800 Stereo FX Send… re-routable to any part of the signal chain" (Elantric, VGuitarForums) — a post-NAMM addition. Gear Sounds confirms it's a full stereo loop you can patch a whole board into.
- Caveat from Gear Sounds: it's "not a true loop" in the amp/cab sense (no movable virtual cab), so you can't insert between virtual amp and speaker.
- ⚠ A routing/template patch — **no published knob values** exist for this feature; the placement/MODE entries above are a dialable recipe, not sourced parameter settings. Treat as architecture, not a sound.
- ⚠ Watch the stereo path: a stereo-collapsing block placed downstream silently kills upstream per-string PAN.

## Sources

- 🔵 `research/links/vguitarforums-vg800-main-thread.md` (stereo FX send re-routable to any point — Elantric)
- 🔵 `research/transcripts/gear-sounds-full-tutorial.md` (full stereo S/R loop; ran VG-800 + RT-2 through it)
- Transformed from Pedalxly VG-800-Patches.md (community)
