https://userguides.novationmusic.com/hc/en-gb/articles/25626786833170-SL-MkIII-MIDI-ports-and-routing
userguides.novationmusic.com · official MIDI-ports-and-routing KB + MusicRadar SL+DAW+hardware how-to · current
(KB 403 WebFetch — distilled from search snippets quoting the official text)

MIDI routing rules + the double-clock warning.

## Ports
- 3× DIN: **In**, **Out**, **Out2/Thru** (Out2 switchable between a second clock-capable Out and pure Thru). USB-B class-compliant exposes MIDI + InControl + a **From-DIN-1** port to the host (so the Mac can see gear plugged into the SL's DIN In).

## CRITICAL: don't double up clock/MIDI on USB + DIN to the same path
- Novation's explicit warning: send MIDI to **USB OR DIN, not both** — doing both "might cause a **loss of synchronisation or erratic tempo**." This is the #1 self-inflicted clock problem.

## Per-template DIN disable (the Logic-MIDI-out workaround)
- On the **Templates** page you can **turn OFF the DIN setting** so MIDI is NOT transmitted from the physical MIDI Out — MIDI still goes down USB to the DAW. (Useful when you want a Part to reach the DAW only, not also blast a DIN-connected synth.)
- The "USB-to-Logic timeout, DIN avoids it" lore (dossier §11, anecdotal): the cleaner reading from the routing docs is that **timeouts/erratic behavior usually trace to double-pathed MIDI or control-surface mis-setup**, not a hard USB defect. Fix order: (1) ensure clock goes USB *or* DIN not both, (2) reset Logic's control-surface prefs + reinstall the Novation plugin (see brookes review file), (3) if Logic-over-USB still flakes, fall back to a DIN Out connection for the clocked/note path.

## Rig guidance
- Decide per device whether it lives on **USB or DIN** and don't clock it on both. With Digitakt/OT/MPC on DIN and soft synths on USB, that separation is natural — just don't also mirror the DIN Parts onto USB to the same boxes.
