https://www.youtube.com/watch?v=bc3HahDH-_w
Native Instruments · How to use everything in Guitar Rig 7 Pro · 2023-10-24 · 1:16:42

[Presenter: Sam Loose / Sam Luce, NI. The single deepest official walkthrough — the authoritative source for what every part of GR7 does.]

## What Guitar Rig 7 is
Guitar Rig 7 Pro is "a creative effect playground where you can mix and match modules to create the ultimate processing chain." Building on GR6, version 7 adds new ICM amplifiers, new stompboxes, new lo-fi effects, and new ways of working (Loop Machine Pro). "It's not just a processing suite for guitars; you can use this on any instrument you like." Repeated throughout: presets are filtered by input source (guitar, drums, keys, vocals, **mix bus**) but you are explicitly told not to feel limited — "you can click on a mix bus preset and use something there."

## Interface layout
- **Left column** = presets + components. Presets are pre-built rigs (double-click to load). Components = the raw module palette, browsable by category (amplifiers, cabs, reverb, delay, distortion, dynamics, modulation, etc.). Drag a component into the rack; a yellow bar shows insert-between, a yellow box-around shows replace.
- **Center** = the rack: anything that affects the sound lives here, top-to-bottom signal flow.
- **Right** = the new **Signal Flow** panel: a condensed top-to-bottom map of the whole rig. Click any module to jump to it in the rack; drag modules to reorder ("hot swap" — seamless, no audio stop). Especially valuable for **A/B split** patches: on the preset "Arctic" the Signal Flow clearly shows a clean A path and a B path (Vintage Verb + Solid EQ) rejoining at a **Split Mix** — much easier to read than the center rack alone.
- **Info pane** (bottom right): hover any parameter/module for an explanation. Click a Split Mix and it explains exactly what's happening.
- **Resizable plugin window.**

## Rack tools (top row, 7 utilities)
- **Tape Deck Pre** — load/drag/record a piece of audio *before* the rack, so you can tune your rig without a guitar in hand. Ships with demo files named to suit amp types. Loops between locators; can transpose/tune the loop slightly.
- **Tape Deck Post** — sits at the end of the rack; records the processed output. Lets you capture an idea in standalone mode (no DAW), save anywhere.
- **Tuner** — reads the input; settable reference pitch / concert A.
- **Metronome** — full time signatures incl. odd meters (5/4, 7/8) with selectable accent groupings; muted by default.
- **Preset Volume + Mix** — per-preset saved volume, plus a global **wet/dry Mix** control with a **Pre-mix / Post-mix** toggle. *Post-mix* = standard wet/dry (no level change). *Pre-mix* = splits before the rack and intelligently matches dry/wet levels (matters for level-dependent effects like distortion — it accounts for the input level). This is the key control for "using GR purely as an FX processor (just reverb / just delay) and blending in a bit."
- **Global Effects** (the paperclip/strip on the right) — a module that stays loaded regardless of which preset you switch to (e.g. always-on RC48 reverb across all presets).

## ICM (Intelligent Circuit Modeling)
Modules tagged "ICM" model "the journey of the signal from input to output" — every stage affects the next, like a car taking a different route LA→NY ending in a different state. Reinforces that **order matters**: distortion-before-reverb ≠ reverb-before-distortion. Applies to the new amps and some new stomps.

## Amps demonstrated
- **Super-Fast 100** (new ICM) — usable wide gain range, keeps note definition + attack even dimed. Overdrive channel = modern rock; "normal" channel cleaner = classic rock. Bright switch. Matched Cabinet Pro loads with it.
- **AC Box XV / AC Box 15** (new ICM) — bluesy, lower-drive, laid-back amp; takes pedals into it well.
- **Reverb Delight** (new ICM) — used in a "Lo-fi chords" patch.
- **Bass Rage** (new ICM, 300W bass) — warm bottom + familiar "clank"; an **ultra-high button** adds top-end clank to cut the mix.
- **Plex** (older) — barely-driven warm clean.
Input control = treat it like a guitar's volume knob: it sets how hard you hit the amp / how much overdrive. "Before reaching for other stuff, start with this input control." Matched Cabinet Pro = blend mic'd cab + room; you can swap to any other cab.

## New stompboxes
- **Screamer Deluxe** (ICM) — Tube-Screamer-style; three modes: **Classic**, **LED** (different clip), **EQ** (bass/treble *before* the gain = EQ-into-the-gain). Adds bite/grit/top before the amp.
- **IVP Stomp** — preamp w/ bass+treble set before the drive circuit (push frequencies into the gain).
- Also referenced: Chainsaw (Swedish-death-metal buzz distortion), Seattle Fuzz (grunge fuzz + diode clipping).

## Cabinet IR Loader (new)
Up to **4 IRs** loaded at once, each with independent **level + pan**, plus per-IR **EQ** (low cut, high cut, bass/mid/treble). **Auto-align** button time-aligns the impulse pulses so blended IRs aren't phase-cancelling (shown clearly: out-of-phase IRs lose low end; auto-align "solidifies" without cutting frequencies). Ships with IRs from 3 Sigma Audio, Bogren Digital, cabIR, Eminence, Lancaster. Load your own custom IRs. Per-IR EQ lets you notch e.g. just the bright IR's top end without touching the amp. Jens Bogren artist presets ship with custom IRs.

## Lo-fi effects (the v7 theme)
- **Color** — 10 distortion algorithms, several borrowed from iZotope **Trash 2**. Has wet/dry, gain, drive, and a **Bass Saver** (limits how hard distortion hits the low end — "saves the low end," a real consideration when distorting bass). Demonstrated *before* the amp as a "character control," not a fuzz; algorithms range subdued→sweeter→clippy. Movable anywhere in the chain.
- **Tape Wobble** — wow/flutter + saturation + **Age**. Age rolls off top end and adds hiss; wow/flutter bends pitch (emulating a misaligned tape machine). "You can be as destructive or as subtle as you like." Great on drums.
- **Vintage Vibrato** — vibrato/chorus from a classic vintage organ; 6 modes of increasing intensity; mostly used on a chorus-flavored sound.
- **Noise Machine** — adds hiss/crackle/hum: 50 Hz hum, 60 Hz hum, transformer hum, power hum, amp hum, vinyl noise — "as if recorded to a really bad, misaligned cassette tape." Blend in at varying degrees. (Used in a "too hot to handle" drum patch with the looping wow.)
- **Kolor** (mentioned elsewhere) — additional lo-fi color.

## Non-guitar uses demonstrated
- **Drums** — processed with Solid EQ + a compressor (VC 160, described as "knocky," chops the transient = percussive knock) + **iZotope Ozone Maximizer** module (tames peaks without pumping, adds transient control/sweetening). Tape Wobble + Noise Machine + Color for lo-fi destruction.
- **Bass** — two contrasting patches off the Bass Rage: a clean rock tone (Screamer Deluxe for edge) and a wild melodic one with **Psych Delay + Vintage Vibrato + Tape Wobble** ("breaking the rules — delay/reverb on bass — but why not, it stops sounding like a bass anymore"). Different cab swapped in.
- Closing: "use it on drums, vocals... all kinds of compressors (VC 76, VC 160, VC 2A), EQs, reverbs — the toolset to mix anything. Works on vocals with the Ozone Maximizer. Works great on a master bus."

## Macros (advanced control)
16 macros (two layers of 8). Auto-assigned by preset, remappable. Right-click a macro → **Learn MIDI control**, turn a knob = tactile control. Drag the 4-arrows to assign one macro to multiple parameters at once (e.g. Screamer Deluxe overdrive + Super-Fast 100 gain together). **Expert view** sets per-target min/max range and scaling (e.g. Screamer overdrive maxes at 50% while the amp gain goes full). Nearly every control (incl. transport) is MIDI-assignable.

## Loop Machine Pro
Two buffers A/B (MIDI/footswitch assignable to be hands-free). Record/play/stop; record length in bar multiples; record start = count-in / direct / auto-start (>-60 dB). **Auto-grow** records as long as you play. **Reverse**: record backward then play forward = reverse-guitar effect; or play whole thing backward. Drag drum loops into a buffer to jam over. **Record Pan** can be modulated by an **LFO component** (assign LFO → record-pan via the 4-arrows, sine wave) = auto-panning takes as you record. Keep Loop Machine *last* in the chain (so loops don't re-run through the amps; signal runs strictly top→bottom, letting you switch presets seamlessly mid-loop).
