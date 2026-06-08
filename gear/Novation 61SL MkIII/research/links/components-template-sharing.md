https://support.novationmusic.com/hc/en-gb/articles/360005133320-SL-MKIII-Factory-Templates  +  https://www.kvraudio.com/forum/viewtopic.php?t=533895
Novation support + KVR Audio "Novation SL MK3 Controller Templates" thread · community · ongoing

# State of community / shared Components templates (honest: thin)

## Factory templates (ship in Components, ready to use)
Components includes a "Novation Templates" library. Confirmed factory templates relevant to this rig and beyond:
- **Elektron Octatrack**, **Elektron Digitakt** ← directly useful here
- **Elektron Analog Rytm**
- Roland **TR-8S**
- Novation **Circuit**, **Peak**
- Moog **Sub 37**
- **OB-6**, **Prophet 6**, **Prophet R2 (Rev2)**
- Strymon **BigSky**
- Waldorf **Blofeld**, **Microkorg**, **Minilogue**, **Mininova**, **Nord Lead 2**
These are starting points — load, then tweak CC maps in the editor.
**No factory template for the Boss VG-800, Chase Bliss pedals, Hologram, Eventide H90, MPC** — those you build yourself (see VG-800 recipe + `components-template-editor.md`).

## Community sharing (limited)
- **Facebook "Novation SL MK3" group** — the main place users swap custom templates. Active but social-media-gated.
- **piedpipers.club/sl/templates/** — a curator mirrored the FB group's shared templates to a web archive for non-FB users. **WARNING: as of 2026-06 this host is DOWN (connection refused / dead).** Treat as historical; don't rely on it.
- **GitHub `inno/slmkiii` (libslmkiii)** — a Python library to build/convert templates as JSON↔SysEx; not a template *pack*, a tooling repo (see `int-libslmkiii-library.md`).
- Coverage requests seen: Arturia **Analog Lab / V Collection**, **Korg Collection**, u-he (**Diva/Sylenth**), KORG **wavestate/modwave/opsix**.

## Sentiment / takeaway
Community consensus: making templates in Components is "really difficult" / tedious point-and-click; sharing exists but is **modest and scattered** (FB + one now-dead archive). For this rig, plan to **build your own** templates for the VG-800, CB stack, Hologram, H90; lean on **factory Octatrack/Digitakt** templates as-is or lightly edited. The libslmkiii route is the fastest bulk-authoring path if you're comfortable editing JSON.
