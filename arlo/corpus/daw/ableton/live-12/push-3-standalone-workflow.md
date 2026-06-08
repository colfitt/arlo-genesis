# Push 3 Standalone Workflow

**Scope:** daw
**Source:** Deep-research synthesis (2026-05) — Ableton Live 12.x + Push 3 standalone firmware (current) — verify before treating as authoritative
**Canonical references:** [Ableton Push 3 Manual](https://www.ableton.com/en/push/manual/); [Push 3 Technical FAQ](https://help.ableton.com/hc/en-us/articles/8483166334748-Push-3-Technical-FAQ); [Push with Live 12 — Release Notes](https://www.ableton.com/en/release-notes/push-12/); [Max for Live Devices on Push 3 standalone](https://help.ableton.com/hc/en-us/articles/8506527153308-Push-standalone-Max-for-Live-Device-compatibility); [Ableton Drummer — Push 3 review](https://blog.abletondrummer.com/ableton-push-3-review/)
**Tags:** `daw-ableton`, `live-12`, `live-12-feature`, `push-3`, `standalone`, `hardware`

---

## What "standalone" means for Push 3

Push 3 ships in two SKUs: Push 3 (controller-only, requires a computer running Live) and Push 3 Standalone (with an internal computer running its own copy of Live). The hardware is identical between the two — pads, encoders, screen, jog wheel, transport, MPE-capable pad surface — but the Standalone unit adds an Intel 11th-gen Core i3-1115G4, 8 GB of RAM, and a 256 GB user-replaceable NVMe SSD inside the chassis. The controller-only unit can be upgraded to Standalone via Ableton's Upgrade Kit. In Standalone mode, Push runs Live as a hosted application against its internal storage — projects live on the SSD, audio renders on the internal CPU, and no computer is needed. In Control mode (tethered to a Mac via USB-C with Live 11.3+ running), Push behaves as a control surface for the desktop Live instance — the computer is the brain, Push is the interface.

## Bundled Live edition and licensing

Push 3 Standalone ships with a Live Intro license per the [Push 3 Technical FAQ](https://help.ableton.com/hc/en-us/articles/8483166334748-Push-3-Technical-FAQ), with bundles available that include Live Standard or Live Suite for additional cost. Critically, the Live edition you're licensed for determines which features are available on Push Standalone — owning Live Suite on your desktop means Push runs in Suite mode with all bundled instruments, effects, and Max for Live; owning Live Intro means Push runs in Intro mode with a much smaller stock device set. You authorize Push for a higher Live edition by signing into your Ableton account from Push's settings menu. The license unlock applies on Push the same way it does on the desktop.

## Hardware specs that shape the workflow

The Push 3 Standalone CPU is a low-power mobile-class Intel — capable but not desktop-grade. Working rules from the [Push 3 Technical FAQ](https://help.ableton.com/hc/en-us/articles/8483166334748-Push-3-Technical-FAQ) and [Ableton Drummer's review](https://blog.abletondrummer.com/ableton-push-3-review/): expect to manage CPU pressure aggressively (freeze tracks frequently, keep Wavetable voice counts modest, avoid Hybrid Reverb stacks). The audio interface is a 2-in / 2-out at up to 96 kHz with buffer sizes from 128 to 2048 samples. Battery life is approximately 2.5 hours of typical use — practical for cafe sessions but plan to plug in for longer work. The SSD is user-replaceable (per [Ableton's Push 3 Upgradability guide](https://help.ableton.com/hc/en-us/articles/9204692908188-Push-3-Upgradability-with-Third-Party-Parts)) and the unit accepts standard NVMe M.2 drives, which makes storage expansion straightforward.

## What's available in Standalone mode

In Standalone, you have access to: all stock Ableton instruments and effects available in your authorized Live edition (Operator, Wavetable, Drift, Meld, Drum Rack, Sampler, Simpler, Granulator III, Drum Sampler, the EQ/compression/reverb/delay families, etc.); most bundled Max for Live devices; Session view recording, editing, and clip-launching; full MIDI editing of clips; the Browser with Packs you've installed to the internal SSD; Drum Rack and Melodic Step Sequencer modes for pad-based composition; the four-stem Push step sequencer; Note mode for melodic playing with MPE; Live's tuning systems and scale-aware MIDI features (Push 12.x firmware respects the project Scale and lights up in-scale pads). The [Push with Live 12 Release Notes](https://www.ableton.com/en/release-notes/push-12/) is the canonical reference for which Live 12 features have made it to Push firmware — Live 12.2 added Push Follow Actions, for example.

## What is NOT available in Standalone — the hard limits

This is the single most-asked Push 3 question, and the limits matter for workflow planning:

- **Third-party VST/AU/VST3 plugins are not supported in Standalone mode.** The [Push 3 Technical FAQ](https://help.ableton.com/hc/en-us/articles/8483166334748-Push-3-Technical-FAQ) is explicit: "Push 3 in standalone mode only supports Ableton's built-in devices and supported Max for Live devices." If your project uses Serum, Pigments, Diva, or any third-party plugin, those tracks won't play on Push. The workaround is to freeze affected tracks on the desktop before transferring — frozen tracks play their rendered audio on Push without needing the source plugin.
- **Arrangement View editing is not supported in Standalone.** Per Ableton's documentation, "Live Sets can be loaded and played back, but the Arrangement timeline can't be edited on Push in Standalone Mode." Recording into Session view works; arrangement editing requires the desktop. Push 3 is a Session-view-first instrument by design.
- **Some Max for Live devices have limited functionality or don't work at all on Push.** Per [Ableton's M4L on Push 3 standalone compatibility article](https://help.ableton.com/hc/en-us/articles/8506527153308-Push-standalone-Max-for-Live-Device-compatibility), specific devices may exhibit limited control (parameters un-mappable), disabled sample import (can't load new samples while certain M4L devices are active), playback-only behavior, or full incompatibility.
- **Cloud Sets from Note/Move require Control mode** for full Ableton Cloud integration in some cases.

## The sketch-on-Push, finish-on-desktop workflow

The most common Push 3 Standalone workflow is **sketch on Push, finish on desktop**. Push captures musical ideas — chord progressions on the pads, melodic improvisations in Note mode, drum programming via the step sequencer, recorded vocals or guitar via the audio inputs — while away from the studio. Back at the desktop, the Set transfers over WiFi (or via USB drag-and-drop of the .als project folder), opens in desktop Live 12, and gets finished with third-party plugins, Arrangement view editing, and the full mixing toolkit. This split respects what each tool is good at: Push is a tactile musical input device with constrained focus; desktop Live is the finishing room. The reverse direction — finishing on Push — works for simple projects but hits the third-party-plugin and Arrangement-editing walls fast.

## Project transfer between Push and desktop Live

WiFi pairing is the canonical transfer method. Both Push and desktop Live must be on the same network, the Push is paired in desktop Live's preferences, and Sets transfer in both directions — Push → desktop (with all clips, devices, samples), desktop → Push (with the caveats about plugins and arrangement). Per [Ableton's Push 3 Manual](https://www.ableton.com/en/push/manual/), the transfer includes all referenced samples and Pack content. USB-C cable transfer is the alternative for large projects or when no WiFi is available — connect, Push appears as a storage device, drag the project folder. Frozen tracks transfer their audio; plugin tracks transfer their MIDI and device chains but won't play on Push without the plugins being substituted or the tracks being pre-frozen on desktop.

## Recording audio into Standalone Push

Push 3's hardware audio inputs let you record guitar, vocals, line-level synths, and other sources directly into Session view audio clips without a computer. Set up: connect via the 1/4" balanced inputs on the back, arm an audio track, monitor through Push's outputs (1/4" balanced) or headphone jack, hit record on the track. The 96 kHz capability gives sample-rate parity with most studio interfaces. Latency is acceptable for tracking — buffer down to 128 samples for live monitoring with effects. Live 12.1's Drum Sampler is especially good for Push-recorded one-shots: tap the pad to capture, the Drum Sampler treats the recording as a one-shot ready for further processing. Auto Shift (Live 12.1+) runs on Push for pitch correction and harmony generation on recorded vocals.

## Push 3 and MPE — the expressive playing layer

Push 3's pads are MPE-capable per the [Ableton Push 3 Manual](https://www.ableton.com/en/push/manual/) — each pad transmits three independent dimensions per note: **pressure** (continuous after-touch), **slide** (vertical movement on the pad), and **per-note pitch bend** (horizontal movement). This makes Push 3 a serious MPE controller alongside ROLI Seaboard and Linnstrument. Pair MPE-aware instruments (Meld, Wavetable, Drift, Granulator III, MPE-enabled third-party plugins) with Push and the pads become expressive instruments — vibrato via horizontal wiggle, filter sweep via vertical slide, dynamics via pressure. The instrument's MPE response is configured per-device; Push respects whatever the target instrument is expecting.

## CPU and latency realities on Standalone

Working with Push as a producer means thinking about its CPU envelope. The mobile-class i3 handles Suite-default projects comfortably but can be pushed past its limits faster than a desktop Mac. Practical patterns: freeze drum buses (Drum Rack chains with multiple effects per pad eat CPU), commit synth tracks once the patch is locked, avoid running Wavetable at high voice counts (Live 12.4 raised the max to 16 voices, which can still be too many on Push), use the older Reverb device rather than Hybrid Reverb on multiple tracks. Buffer size up to 512 or 1024 samples is reasonable for playback; track at 128–256. The [Ableton Drummer Push 3 review](https://blog.abletondrummer.com/ableton-push-3-review/) notes CPU management as the most consistent friction in working entirely on the unit.

## Standalone vs tethered — when each fits

The decision tree: **Standalone alone** when you want a screen-free, focused composition tool — café sessions, sketching, performing, working with someone over the shoulder on a kitchen table. **Tethered (Push 3 controller mode against desktop Live)** when you want Push's hands-on control with the full desktop toolkit — third-party plugins, Arrangement view, larger projects, all the CPU your Mac provides. **Both** when the workflow is sketch-on-Push, finish-on-desktop, with project transfer in between. Many Push 3 owners use it primarily tethered with occasional standalone sessions; some use it primarily standalone with occasional desktop finishing. Live 12's project portability means you don't have to choose a single workflow.

## Cited Retrieval Topics

- "can i use third party plugins on push 3 standalone"
- "does push 3 work without a computer"
- "what's the difference between push 3 standalone and controller"
- "how do i transfer projects between push 3 and ableton live on my mac"
- "how long does push 3 battery last"
- "can i edit arrangement view on push 3 standalone"
- "what live edition comes with push 3"
- "does push 3 have an audio interface"
- "what max for live devices don't work on push 3 standalone"
- "is push 3 mpe"

## Sources

- [Ableton Push 3 Manual](https://www.ableton.com/en/push/manual/)
- [Ableton — Push 3 Technical FAQ](https://help.ableton.com/hc/en-us/articles/8483166334748-Push-3-Technical-FAQ)
- [Ableton — Push with Live 12 Release Notes](https://www.ableton.com/en/release-notes/push-12/)
- [Ableton — Max for Live Devices on Push 3 standalone](https://help.ableton.com/hc/en-us/articles/8506527153308-Push-standalone-Max-for-Live-Device-compatibility)
- [Ableton — Push 3 Upgradability with Third-Party Parts](https://help.ableton.com/hc/en-us/articles/9204692908188-Push-3-Upgradability-with-Third-Party-Parts)
- [Ableton Drummer — Push 3 review](https://blog.abletondrummer.com/ableton-push-3-review/)
- [PushPatterns — Live vs Push 3](https://www.pushpatterns.com/blog/ableton-live-vs-push-3)

## See also

- `corpus/daw/ableton/workflows/session-vs-arrangement-view.md` (A1 — Session view, where Push lives)
- `corpus/daw/ableton/workflows/instrument-racks-effect-racks-macros.md` (A7 — racks and macros, key to Push performance)
- `corpus/daw/ableton/workflows/clip-launching-and-follow-actions.md` (A5 — clip launching from Push)
- `corpus/daw/ableton/live-12/live-12-point-releases-changelog.md` (C7 — Push firmware tracks Live point releases)
- `corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md` (I12 — Live as a performer's tool)
