https://support.native-instruments.com/hc/en-us/articles/360014454117 · https://discussions.apple.com/thread/7340179 · https://www.audeobox.com/learn/logic-pro/how-to-install-plugins-in-logic-pro/
native-instruments support + apple community + audeobox · current

# AU-only host: what it means in practice + fixing "plugin missing / failed validation"

## The hard rule
Logic loads **Audio Units ONLY** — VST/VST3/AAX are ignored entirely. Every
plugin this user runs in Logic MUST have an AU build. (Most do: Komplete,
Kontakt 8, Arturia V Collection, Soundtoys, Spitfire, Antares, Valhalla,
Neural DSP, Goodhertz, Melodyne all ship AU. The only real casualties are
VST-only tools — none in the current inventory, but worth checking before
buying.) Ableton Live 12 Lite is the fallback host if something is VST-only.

## Where AU components live
- System: `/Library/Audio/Plug-Ins/Components/`
- User:   `~/Library/Audio/Plug-Ins/Components/`
A valid AU is a `.component` bundle in one of those.

## When a new plugin doesn't show / fails validation — fix in order
1. **Relaunch Logic.** If it was open during install, the scan missed it.
2. **Reboot the Mac.** macOS's AudioComponentRegistrar frequently needs a reboot
   to see newly installed AUs (a long-standing OS bug — see
   kvr-au-validation-reality.md). This fixes most "missing plugin" cases.
3. **Plug-in Manager:** Logic Pro > Settings > Plug-in Manager >
   **Reset & Rescan Selection** on the offending plugin.
4. **Delete the AU cache, then relaunch** (forces a full rescan):
   `~/Library/Caches/com.apple.audiounits.cache`
5. **Privacy & Security:** System Settings > Privacy & Security — if macOS
   blocked the plugin (unsigned/notarization), click **"Open Anyway,"** then
   rescan.
6. **"Use anyway" override:** if it fails validation but Plug-in Manager lets
   you enable it manually, do so — devs confirm Logic's run-anyway override is
   usually reliable; a failed validation is often a Logic/OS edge case, not a
   broken plugin.

## Apple Silicon vs Rosetta gotcha
- A few AUs validate/run differently **native (Apple Silicon) vs under Rosetta**.
  If a legacy/Intel-only AU won't validate, relaunch **Logic in Rosetta** (Finder
  > Logic Pro > Get Info > Open using Rosetta). Keep a consistent mode so you're
  not re-validating constantly.

## Practical AU-only hygiene for a big collection
- Use **Plug-in Manager colon-naming** (`Synth:Analog`) to fold the huge AU menu
  into sub-folders (see sos-logic-hidden-features.md).
- After any macOS or Logic update, expect a re-validation pass; a plugin that
  "vanished" usually just needs a rescan, not a reinstall.
