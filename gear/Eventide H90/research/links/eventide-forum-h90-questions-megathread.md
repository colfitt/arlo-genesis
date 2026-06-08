https://www.eventideaudio.com/forums/topic/h90-questions/
Eventide official forum · multiple (Brock, tbskoglund/Tim Skoglund staff, coirbidh_99, dongothard, rosensta, LBraniff, apalazzolo, MPOhNooo) · Nov 2022 – June 2023

# H90 launch-era megathread — power-user tips, gotchas, H9-vs-H90 (distilled)

The single densest early thread. Highlights, grouped:

## Dry-signal architecture (the "why is there latency / why kill-dry" answer)
- Eventide keeps the **same dry-path architecture as the H9**: the dry signal passes through the ADC/DAC (it is NOT analog-bypassed) "to avoid comb filtering from phase cancellation." Skoglund: *"After extensive testing… we chose the latter due to the fact that it ultimately sounds better"* (June 2 2023).
- Main-path latency is small but real: **Series ~4.5 ms, Parallel ~3.8 ms**, each Insert adds ~3.8 ms.
- If you want a truly analog dry path / parallel wet-only, use an external analog pan/blend pedal and enable the **"Kill Dry"** system setting so the H90 outputs wet only.

## MIDI / program management
- A MIDI **Program Change loads BOTH Presets at once** — you cannot address Preset A and Preset B on independent MIDI channels (Brock, Mar 30 2023). The Program is the unit MIDI sees.
- **Bank Mode** gives 6 algorithms across a 3-Program bank using the two footswitches (workaround for the limited switch count).
- **LEARN is a Performance Parameter locked to specific algorithms** (e.g. Diatonic), NOT a HotSwitch function (rosensta, Mar 30 2023).
- Live gripe (LBraniff, May 23 2023): the old H9 app gave single-tap access to 9+ algorithms; the H90 needs Bank Mode (2–3 interactions per change). Eventide said an app is "in the works," no date. Workarounds offered: **MIDI Designer iPad app** or **external 3-button aux switches**.

## Tempo
- Tempo is saved **per-Program** (not independently per-Preset in H90 Control). On the pedal in Perform mode, Tap Tempo can give different BPM per Preset, but **H90 Control has no numeric tempo entry** (open feature request).

## Spillover / bypass tails
- "Bypass tails" let a delay/reverb keep ringing after you bypass the Preset; spillover loads a new Program while the previous tail decays (Skoglund, Nov 13 2022). Confirmed working as designed.
- Effect bypass can be mapped to an **expression-pedal range** via H90 Control's General tab.

## Aux switch / expression CRITICAL setup note
- **Calibrate the aux switch** if an external switch is non-responsive: System > I/O > Exp & Aux (dongothard, Nov 12 2022). This fixes most "my external switch doesn't work" reports.
- H90 accepts **both TS and TRS** expression pedals; calibration is much improved over the H9 (you can set 8-Step Depth 1–9 with accurate calibration).

## Power
- Skoglund confirmed a **12 V / 500 mA** outlet on a CIOKS supply suffices (NOTE: this is the 12 V figure — the dossier's "600 mA @ 12 V" is the spec; CIOKS 500 mA ports reportedly run it. At 9 V you need 800 mA. Center-POSITIVE either way).

## Routing tricks
- **Mono-in → split A to outs 1/2, B to outs 3/4**: use a stereo insert as a tap point — "Preset A will be output on 1-2 and Preset B will be on outputs 3-4" (Skoglund, Feb 20 2023). A true two-amp / wet-dry-wet trick.
- Brock's experimental idea: **two Loopers in parallel with a third stereo looper inserted between them**, MIDI-clock-synced, for Riley/Reich phase-music.

## Parameter naming gotchas (carried over from Factor pedals)
- Chorus **"Intensity" = dry/wet mix** (not pure vibrato at 100%).
- Flanger **"Intensity" = feedback level**, not effect level (manual is misleading here).

## H9 → H90 migration
- ~200 H9 presets imported successfully, BUT the user had to **manually reassign expression-pedal ranges** (ribbon/expression mappings don't carry cleanly) (apalazzolo, June 2023).
- H90 subjectively "sounds cleaner, clearer," more headroom; legacy algorithms got parameter additions and audible re-voicing.

## Rig relevance
- For the MIDI-linked End board: remember a PC changes the whole Program (both effects) — design Programs as scene units, not single effects.
- The dry-through-ADC/DAC fact matters end-of-chain: if you ever want a pure-wet parallel feed into the tape stage, use Kill Dry + external blend, or use Dual routing.
