https://www.youtube.com/watch?v=BUd8WwiLVEo
Morningstar Engineering · UAFX 2.0 - A MIDI Dream Come True · 2025-11-11 (10:38, ~49k views)

**Best for:** THE definitive UAFX 2.0 USB-MIDI walkthrough, and the only video that demos Del-Verb MIDI specifically. Published the day the 2.0 firmware dropped. Settles every "what's actually recallable / what drives it" question for this rig.

## The MIDI reality (Del-Verb specifically)
- **Del-Verb is a "no-preset" pedal** (no preset footswitch). Therefore: **it does NOT accept Program Change. It accepts Control Change (CC) only.** You cannot recall a stored preset by PC the way the preset-capable pedals (e.g. Lion, Dream '65, etc.) can. The video draws this exact line: preset pedals = PC for presets + CC for params; no-preset pedals (Del-Verb, Max, Galaxy '74) = CC only.
- **A "snapshot" on Del-Verb = a bundle of CC messages sent from your controller**, not a pedal-side memory. To recall a "sound," the controller fires the CCs that set delay type, reverb type, the assigned voicings, division, feedback, mix, reverb level, bypass states, etc. The pedal has no slot to store this — the recall lives entirely in the MIDI controller.
- **MIDI clock tempo sync works.** "The Del-Verb also accepts MIDI clock now, which is amazing. This allows me to use a switch to send MIDI clock tap tempo." So delay time can be slaved to a host clock or a tap-tempo switch on the controller.

## How it physically connects (the key clarification)
- **The pedal is a USB *device*, not a host.** It does NOT connect to a 5-pin DIN. MIDI arrives over the pedal's USB-C port.
- **You need a MIDI controller that has a USB *host* port.** Morningstar **PRO** controllers (MC6 Pro / MC8 Pro) have USB-C host ports that connect *directly* to the UAFX pedal — **no computer required.** A USB-C cable host-port → pedal is the whole connection.
- **For multiple UAFX pedals:** plug a USB hub into the MC Pro host port to fan out to several pedals at once.
- Per the companion support docs: DIN-only controllers (GigRig G3S, Jet Pedals Unity6) must go through a USB-MIDI host converter (e.g. CME H2MIDI Pro). A computer/DAW also works as the host. (For THIS rig the clean answer is: an MC-Pro-class controller with a USB host port, direct, laptop-free.)

## Del-Verb control flow shown on the MC8 Pro
- One bank/page selects **delay type and reverb type** (each via CC), plus **engage/bypass delay** and **engage/bypass reverb**. Choosing a type also recalls whichever **voicing** you assigned to that type in the app.
- A second page (held footswitch) holds **delay settings: time division, feedback, delay mix.**
- A third page holds **reverb length** controls.
- **EXP-select switches** re-target a connected **expression pedal** to sweep any chosen Del-Verb parameter (mix, feedback, reverb level, etc.) live with the foot.
- Morningstar added all 14 UAFX pedals to the **MIDI Dictionary** — pick a function by name, the app tells you the CC and value mapping, no manual lookup. Pedal lights an orange LED when receiving MIDI.
- **Downloadable resource:** Morningstar publishes a ready-made **MC8 Pro Del-Verb bank** (link in the video description) that reproduces this exact layout.

## Honest limitation restated
"This makes the Del-Verb less flexible than the pedals with presets" — because there is no stored preset, the MIDI controller has to send the full state each time. With a capable controller this is a non-issue; without one, MIDI buys you nothing extra over the front panel.
