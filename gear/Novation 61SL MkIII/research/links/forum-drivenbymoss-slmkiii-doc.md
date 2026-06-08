https://github.com/git-moss/DrivenByMoss-Documentation/blob/master/Novation/Novation-SLMkIII.md
github.com/git-moss · DrivenByMoss official SL MkIII documentation · maintained (current)

DrivenByMoss is the community-standard third-party control-surface script (Bitwig / Reaper, with the SL fully supported). Concrete setup + mapping:

## Enable
- Press the **InControl** button (top-left, between Global and Tempo) to hand the SL to DrivenByMoss. Toggling it returns the SL to its own hardware features. **Requires latest firmware via Components.**
- Setup gotcha: configure DrivenByMoss to use the **second MIDI/InControl port** as primary in/out for proper function.

## Mapping (concrete)
- **8 faders** → track volume for the 8 visible tracks; the LED above each fader shows track color and brightens with level.
- **8 knobs**, mode-colored:
  - **Track mode (green):** volume, pan, sends 1–6 for the selected track. **Shift = fine adjust.**
  - **Volume mode (blue) / Pan mode (amber) / Send modes (yellow):** knobs repurpose accordingly.
- **Transport:** Play = start/stop; **double-click Play = jump to song start**; **Shift+Play = toggle repeat**; Record = record, **Shift+Record = launcher overdub**; **<< / >>** = move play cursor left/right in the arranger (this is what fixes the stock-HUI dead FF/RW buttons).

## Why it matters here
Even with Logic/Ableton's native InControl scripts, DrivenByMoss exposes more (screen-aware device params, clip launching, deeper transport). It's the go-to when the stock integration feels shallow. Free.
