---
type: scene
name: Ambient Wash
sceneId: ambient-wash
plugin: Prophet-5 V
engine: VST3
controller: Novation 61SL MkIII
sessionProgram: 12
date: 2026-06-29
---

# Ambient Wash — scene

Recalls **Prophet-5 V** (VST3) + Chase Bliss MOOD MkII + Novation 61SL MkIII session 12.

The VST patch is recalled from its opaque state chunk (`stateRef` → the host
sidecar's `spike/data/scenes/ambient-wash.<format>.dawstate`); pedals fire
PC/CC from `midi-maps/`; the controller loads a Session via PC on channel 16.

```json
{
  "type": "scene",
  "name": "Ambient Wash",
  "sceneId": "ambient-wash",
  "vst": {
    "plugin": "Prophet-5 V",
    "engine": "VST3"
  },
  "perPedal": [
    {
      "device": "Chase Bliss MOOD MkII",
      "programChange": 7,
      "cc": {
        "Time": 80,
        "Mix": 64,
        "Length": 100
      }
    }
  ],
  "knob": {
    "controller": "Novation 61SL MkIII",
    "sessionProgram": 12
  }
}
```

## Sources
- spike/scene-engine.js (deterministic firing order + invariants)
- research/vst-control/REPORT.md §4.2 (SCENE schema), §4.3 (firing order)
