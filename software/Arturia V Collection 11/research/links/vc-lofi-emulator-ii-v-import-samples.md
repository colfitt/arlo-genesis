https://legacy-forum.arturia.com/index.php?topic=111165.0
legacy-forum.arturia.com · "How to import my own recorded sample into Emulator II V?" · accessed 2026-06-11
(+ corroborated by Arturia Emulator II V overview & CatSynth/DeMarzo demos)

The core "sample your own gear → run it through 8-bit EMU II" workflow.

## Two ways to get audio in
1. **Browser buttons** — in the sample browser, click **"Add Folder"** or
   **"Add Sample"** to load a WAV. Once imported, your sounds live under the
   **"User"** button in the sample browser.
2. **Manual folder placement** — drop WAV files into a subfolder inside the
   Emulator's **User** sample directory (in Arturia's resource folder); the new
   folder then shows up in the browser. WAV is the recommended format.

## Per-voice editing (advanced/screen page)
EMU II V holds **up to 8 samples/voices** at once. For each voice you can:
- **Transpose / fine-tune** (double-click a knob to reset to 0).
- Set the **root note** — important when importing your own samples, or pitch
  tracking will be off (factory samples are auto-named e.g. "C#3" so they map
  correctly; your own recordings need the root set manually).
- Move **sample start / end** and **loop points** (loop a small section + fade
  to make weird sustaining textures).
- Per-voice **low-pass filter** (with key-tracking so the filter opens up the
  keyboard), **ADSR**, **LFO** (→ filter or volume).
- **Chain-link** icon on each control = the parameter is linked across all
  voices; **unlink** to give a voice its own filter/envelope (e.g. long slow
  attack on strings vs instant attack on a guitar layer → one layer fades in
  behind the other).

## The DAC mode = the 8-bit grit
- A **DAC Mode** switch: **Vintage** vs **Modern**. Vintage = the classic 8-bit
  "Super-Nintendo," lo-fi crunch (the reason to use it over a clean sampler);
  Modern = slightly brighter/cleaner. **Leave it on Vintage** for the lo-fi
  aesthetic.

## Assign / keyboard mapping
- The **Assign** panel maps each of the 8 voices to keyboard zones (splits) or
  layers; set per-voice key range, reference/root key, tapers to **crossfade
  samples across the keyboard**, and velocity/keytrack/aftertouch/wheel mod
  routing per voice.

## Effects
- **3 global effect slots** (chorus, delay, reverb by default; also a
  **bit-crusher** + downsampler for even more lo-fi). Routing switchable
  **parallel** (3 independent mixes) or **series** (chained).

## Offset trick (phasing pads)
- Load the **same sample into multiple voices**, set their filter params as
  **relative offsets** (red rings) from the global controls with slightly
  different amounts → complex phasing/filtering motion (a precursor to EMU's
  Z-plane morphing).
