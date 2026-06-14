https://www.cableguys.com/  •  /Applications/Arturia/Pure LoFi.app  •  /Library/Audio/Plug-Ins/Components/Pure LoFi.component/Contents/Info.plist
local-verification + cableguys.com product list · DOUG research facet-agent · 2026-06-08

# CRITICAL FINDING — "Pure LoFi" is an ARTURIA product, NOT Cableguys

The task brief and `Software/Cableguys/SoftwareProfile.md` both attribute a plugin
called **"Pure LoFi"** to **Cableguys**. This is wrong. Three independent,
verifiable facts:

1. **Cableguys' own product list** (fetched from cableguys.com) contains NO
   product named "Pure LoFi." Cableguys makes: PitchShaper, ShaperBox 3, Snapback,
   Kickstart 2, CrushShaper, Curve, DriveShaper, FilterShaper Core, FilterShaper XL,
   HalfTime, Kickstart, LiquidShaper, MidiShaper, NoiseShaper, PanCake, PanShaper,
   ReverbShaper, TimeShaper, VolumeShaper, WidthShaper. (Their lo-fi-relevant
   *effects* = the Shaper family + HalfTime — none installed here.)

2. **The on-disk install is Arturia.** From the AU component's Info.plist:
   - CFBundleIdentifier = `com.arturia.component.Pure-LoFi`
   - AudioComponents: manufacturer = `Artu`, name = "**Arturia: Pure LoFi**",
     subtype = `PrLF`, **type = `aumu`** (= a music *instrument* / synth, NOT an
     effect `aufx`).
   - The standalone app lives at `/Applications/Arturia/Pure LoFi.app` — i.e. in
     the Arturia folder, not a Cableguys folder.

3. **How the mislabel happened:** the repo's `Software/_inventory.json` lists the
   four Pure LoFi files (.component/.vst3/.vst/.app) under a `"Cableguys"` brand
   key — but the very same entries record `"path": "/Applications/Arturia/Pure
   LoFi.app"`. The `scripts/scan_plugins.py` brand-grouping heuristic bucketed an
   Arturia plugin into the Cableguys group. `Software/Cableguys/CONTENTS.md` and
   `SoftwareProfile.md` then inherited the error.

## What Pure LoFi actually IS

Arturia **Pure LoFi** = a lo-fi *synthesizer / sampler instrument* (Arturia's
2025 V-Collection-11-era release). It is a SOUND SOURCE you play, NOT a character
effect you put on a banjo stem or a drone bus. It bakes degradation in at the
source via three engines (Realistic multisample / Creative Sampler / LoFi
Oscillator) plus a tape "LoFi processor," noise layer, filters, and an FX rack.

## Consequence for this task

The brief's framing — "lo-fi character plugin," compare vs RC-20 / SketchCassette
/ Decapitator / Lossy, put it on stems/bus, where does it fit in a degraded-tape
*effect* chain — does NOT apply. Those are all effects; Pure LoFi is an instrument
from a different vendor. No honest "Cableguys Pure LoFi usage guide" can be
written. The accurate digest treats it as **Arturia Pure LoFi, the instrument**,
and flags the repo bug to fix (move it from the Cableguys folder/profile to
Arturia, re-run the scan, correct CONTENTS.md + SoftwareProfile.md).
