https://op1.fun/users/dominusregnavit/packs/bass-sounds-17878
op1.fun · DominusRegnavit (pack curator) · uploaders wavi, tlorach, nate437 · accessed 2026-06-14

# op1.fun "Bass Sounds" pack — bass/baritone patches with concrete settings

A 28-patch bass collection. Most pages don't expose engine details, but three do — and all three are **sub-octave** (octave -1 / -2), which is exactly the baritone-weight / doom-low-fundamental target.

| Patch | Author | Engine | Octave | FX | LFO | Notes |
|---|---|---|---|---|---|---|
| **wonky_bass** | wavi | iter | **-2** | filter | element | iter engine + filter FX + element (tilt) LFO — modulated sub bass |
| **Bass** | tlorach | cluster | **-2** | nitro | — | cluster supersaw dropped two octaves + nitro distortion = thick saturated sub |
| **bass face** | nate437 | voltage | **-1** | nitro | value | voltage (AM/biting) + nitro + value LFO — aggressive moving bass |

Other patches in the pack (engine not exposed on listing): cuckoomusic/bassmonster, Op1kenobi/Acoustic_Bass, snugsworth/synthy_bass, coreys_w/Juno_Synth_Bass, maxCarter/Dx7Bass, brendanciccone/Moog_Bass_{Aggro,Fat,Punch,Soft}, Macaw/{nt 70s bass, nt p bass, nt upright bass}, Miro/{Bass_21, Kick_bass}, VanillaSun/Cassette Bass, 9jef9/Warm Bass.

## Rig takeaway
For a **baritone / doom sub-octave bed**, the documented recipe pattern is: **cluster or voltage engine at octave -1/-2 + nitro FX** (saturation), optionally a value or element LFO for slow movement. `tlorach/Bass` (cluster -2 + nitro) is the closest single-patch match to "baritone weight + saturated drone." Pairs with the pattisoni drwave-at-(-2) drone set in `op1fun-drone-ambient-patches-concrete.md`.

> Honesty flag: engine/octave/FX/LFO read off op1.fun listing; per-knob numeric arrays not exposed (use `op1-dump`). Most patches in the pack don't surface engine data on the listing page.
