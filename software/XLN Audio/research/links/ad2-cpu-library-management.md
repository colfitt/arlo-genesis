https://gearspace.com/board/music-computers/929684-anyone-else-getting-major-cpu-spikes-addictive-drums-2-a.html
gearspace.com thread "Anyone else getting major CPU spikes with AD2?" + jakeduffieaudio.com/articles/ad2-review + VDrums forum CPU thread · accessed 2026-06-11 (Gearspace 403s bots; points triangulated from search-indexed text + mirrors)

# AD2 CPU / RAM / library management

## CPU & RAM reality
- AD2 is **more RAM-intensive than CPU-intensive** (loads kit samples to RAM).
  Single instance is fine on modern machines; **multiple instances** get heavy fast —
  so for a multi-track kit, run **ONE AD2 instance multi-out**, not several.
- The **dual reverb engine (Delerb) is the biggest CPU variable** between presets.
  **Turning OFF the reverb** noticeably drops CPU. For this rig that's a double win:
  reverb off in AD2 → wash externally with VintageVerb/Room anyway.

## Beats-browser slowdown (the real-world gotcha)
- The **Beats/MIDI browser bogs down when you've loaded a lot of 3rd-party MIDI**
  (Groove Monkee, OddGrooves, etc.) into the library — searching/scrolling lags.
  **Playback/runtime is unaffected**; it's only the browser. Keep the user MIDI
  library lean, or fold heavy 3rd-party MIDI packs in only when needed.

## Library / disk management
- **Preset Browser filters**: All / User / per-ADpak — narrow before scrolling.
- **Beats grid-searcher** (top of Beats tab): set hits on the basic grid and it
  filters to only grooves containing those hits — fast way to find a pattern.
- Library lives where the XLN installer put it; large ADpak collections eat disk.
  The XLN Online Installer manages download/relocation of content.

## Workflow fix for CPU when arrangement is set
- **Freeze / bounce AD2 to audio** once the part is locked. Frees RAM+CPU and (handy
  in Ableton Lite) frees the device slot, and gives you the clean stems to degrade.
