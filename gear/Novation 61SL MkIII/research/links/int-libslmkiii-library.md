https://github.com/inno/slmkiii
GitHub · inno (community) · Python library "libslmkiii"

# libslmkiii — text/programmatic template authoring (alternative to Components UI)

A community **Python library** for building and editing SL MkIII templates without the point-and-click Components editor. Useful here for batch-authoring many similar CC maps (e.g. the seven Chase Bliss pedals, each a near-identical button/CC layout).

## What it does
- Templates exist in two forms:
  - **JSON** — human-editable intermediate format.
  - **SysEx (.syx)** — the format Components imports/sends to the hardware.
- The library converts **JSON ↔ .syx** and lets you author maps in code/text.

## Workflow
1. `slmkiii.Template()` → save as JSON (blank template).
2. Edit the JSON by hand or programmatically — set each control's message type, CC#, channel, min/max, behaviour.
3. `slmkiii.Template('file.json')` → save as `.syx`.
4. Import the `.syx` into Components → send to the SL.

## Status / caveats
- Repo is **source + examples + tests**; **no pre-built gear template pack** included.
- Under development; PyPI release pending; future plans for direct MIDI push/pull.
- Author's stated motivation: avoid the "tedium of the point-and-click interface."

## Rig use
Best for **bulk/repetitive** templates: generate one CB-pedal template programmatically, clone+offset CC numbers per pedal, batch-convert to .syx, import all at once. For one-off boutique maps the Components UI is fine.
