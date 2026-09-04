---
type: scene
name: AL Pad
sceneId: al-pad
plugin: Analog Lab V
engine: VST3
controller: Novation 61SL MkIII
sessionProgram: 13
date: 2026-07-01
---

# AL Pad — scene

Recalls **Analog Lab V** (VST3) + Hologram Microcosm + Novation 61SL MkIII session 13.

The VST patch is recalled from its opaque state chunk (`stateRef` → the host
sidecar's `spike/data/scenes/al-pad.<format>.dawstate`); pedals fire
PC/CC from `midi-maps/`; the controller loads a Session via PC on channel 16.

```json
{
  "type": "scene",
  "name": "AL Pad",
  "sceneId": "al-pad",
  "vst": {
    "plugin": "Analog Lab V",
    "engine": "VST3"
  },
  "perPedal": [
    {
      "device": "Hologram Microcosm",
      "programChange": 10,
      "cc": {
        "Mix": 80,
        "Time": 64
      }
    }
  ],
  "knob": {
    "controller": "Novation 61SL MkIII",
    "sessionProgram": 13
  }
}
```

## Sources
- spike/scene-engine.js (deterministic firing order + invariants)
- research/vst-control/REPORT.md §4.2 (SCENE schema), §4.3 (firing order)
