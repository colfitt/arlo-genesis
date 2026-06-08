https://www.uaudio.com/blogs/ua/unlock-uafx-with-usb-midi-control
uaudio.com (UA official blog) · Universal Audio · 2025-11 (UAFX 2.0 launch)

# UA — "Unlock UAFX with USB MIDI Control" (the preset workaround, official)

The defining answer to "how do I make a no-preset Del-Verb behave like a preset machine":

- **The workaround is CC snapshots.** For pedals WITHOUT onboard preset saving — explicitly Del-Verb, Max, Galaxy '74 — quote: *"you can now use MIDI CC snapshots from your controller to create recallable sounds for the studio, stage or rehearsal room."* The snapshots capture **parameter states**, not named onboard presets; the recallable "sound" lives **in the MIDI controller**, not on the pedal. One footswitch on the controller fires a stack of CC messages that sets every Del-Verb parameter to the stored value.

- **Compatible USB MIDI host devices (named by UA):**
  - **Morningstar MC8 Pro** — direct USB-C connection, built-in USB host port.
  - **Disaster Area Designs DMC.micro Gen4.**
  - **Mortrix MIDI Switcher.**
  - A **computer** running a DAW / MIDI app.

- **Multiple pedals at once:** *"It is possible to use a USB hub to connect multiple UAFX pedals for simultaneous MIDI control. In many cases, four or more pedals can be controlled at once, depending on the USB MIDI host interface capabilities."*

- **5-pin DIN controllers:** the **CME H2MIDI Pro** bridges a traditional 5-pin DIN MIDI controller to the USB-enabled UAFX pedals (through a hub). So a legacy DIN board can still drive the Del-Verb.

- **Tempo sync:** *"sync time-based effects to your session tempo via MIDI beat clock."* Del-Verb delay time locks to incoming MIDI Beat Clock.

- **Expression over MIDI:** parameter automation over MIDI also enables expression-pedal-style control of parameters (noted as open beta launching Nov 11, 2025 alongside the 2.0 firmware).

## Host tiers (cheapest → most capable)
- **Cheapest / simplest single-pedal host:** **CME H2MIDI Pro** — a standalone USB-MIDI host box; UA notes it has "simpler electronics and the least chance of introducing noise." Pair it with any 5-pin-DIN foot controller you already own to drive ONE Del-Verb. Smallest, cheapest path to preset-like recall.
- **All-in-one foot controllers with built-in USB host:** Morningstar **MC8 Pro** / **MC6 Pro**, Disaster Area **DMC.micro Gen4**, **Mortrix MIDI Switcher** — these ARE the controller and the host, no separate box.
- **Multiple pedals:** a USB Host MIDI interface connects to one pedal directly, or "**up to eight devices with a standard USB hub**" (passive hub recommended — USB MIDI has no thru, per SoS). UAFX uses USB 2.0 for simplest compatibility.
- **Computer/tablet:** a Mac/PC (or iPad via camera-connection) can host MIDI too; the UAFX Control app programs the pedal over Bluetooth or USB.
- **Troubleshooting reference:** UA has a dedicated "UAFX 2.0 USB MIDI Troubleshooting" support article if a host doesn't enumerate the pedal.

REALITY for this rig: this is the ONLY way to gig the Del-Verb preset-like. A bare Del-Verb on a fly board has no preset recall at all — you change app voicings by hand. Add a USB-host foot controller (MC8 Pro etc.) or a cheap CME H2MIDI Pro + your existing board, and you can store/recall full Del-Verb states per song. But that controller + a passive USB hub (for >1 pedal) + the no-app-while-MIDI-connected friction (see SoS source) is real overhead for a "travel" box. For a pure-simplicity fly board, skip MIDI and pre-load one voicing per engine.
