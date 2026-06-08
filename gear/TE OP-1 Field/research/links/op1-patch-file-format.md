https://github.com/blattm/op1tools  (plus https://schollz.com/posts/op1/ and https://github.com/padenot/libop1)
github / blattm, padenot, schollz (teoperator) · reverse-engineering docs/code · 2016–2021 (accessed 2026-06-03)

# OP-1 / OP-1 Field patch file format (the .aif-with-embedded-JSON "patch")

An OP-1 "patch" — whether a **synth preset** or a **drum kit** — is a single **AIFF (.aif) audio file** with a proprietary JSON blob stuffed into an `APPL` metadata chunk. The audio inside the file *is* the sound (the sample for sampler/drum patches; an 8-second preview render for synth-engine patches), and the JSON carries the engine type, knob positions, ADSR, FX, LFO, and (for drums) the 24 slice start/end markers. Same container for OP-1 and OP-1 Field.

## Container layout (AIFF chunks)
Standard AIFF: `FORM` → `AIFF` → `COMM` (channels/bit-depth/rate) → `APPL` (the OP-1 JSON) → `SSND` (the PCM audio). The OP-1 data lives in the **`APPL` chunk, tagged `op-1`**, inserted **right before the `SSND` tag**.

Byte structure of the OP-1 chunk (from schollz / op1tools reverse-engineering):
- `APPL` (4 bytes, the chunk ID)
- 4 bytes = big-endian size of the chunk, counting from `op-1` up to (but not including) `SSND`
- `op-1` (4 bytes, the application signature)
- the JSON string (UTF-8)
- padding: after the closing `}` you pad with `0a` (newline) and/or `20` (space) bytes until the whole file size is a multiple of 4; the `FORM` size field at the top must then be updated. (Observed pads were "`0a20`" or just "`0a`".)

> Honest flag: those exact pad bytes and the "size up to SSND" rule are community reverse-engineering, not TE docs. They're consistent across three independent implementations (schollz/teoperator, blattm/op1tools, padenot/libop1), so they're reliable, but TE has never published the spec.

## Synth patch JSON (verified — teoperator `synth.go` `SynthPatch` struct + real examples)
```json
{"adsr":[64,64,0,64,14336,64,4000,4000],
 "fx_active":true,
 "fx_params":[64,-14337,4515,7232,0,0,0,0],
 "fx_type":"nitro",
 "knobs":[3072,0,512,3,0,0,0,0],
 "lfo_active":false,
 "lfo_params":[4608,32767,8448,15360,0,0,0,0],
 "lfo_type":"value",
 "name":"default",
 "octave":0,
 "synth_version":2,
 "type":"cluster"}
```
Field meaning:
- `type` — the synth **engine** name (e.g. `cluster`, `sampler`, `dimension`, `string`, `fm`, `phase`, `pulse`, `digital`, `dna`, `dsynth`, `dr_wave`, `voltage`). This is the engine the patch loads into.
- `knobs` — the 8 values behind the four colored encoders (engine params). Range roughly 0–32767.
- `adsr` — 8 ints; the first four are Attack, Decay, Sustain, Release (the teoperator `iota` order is Attack, Decay, Sustain, Release, Playmode, Portamento), then envelope extras.
- `fx_type` / `fx_params` / `fx_active` — the one master FX slot. `fx_type` is one of the OP-1 effects (e.g. `cwo`, `delay`, `grid`, `nitro`, `phone`, `punch`, `spring`; the Field adds `mother`). 8 params.
- `lfo_type` / `lfo_params` / `lfo_active` — the single mod source: `value`, `tremolo`, `random`, `element`, `midi`, `bend`, `crank`.
- `octave` — int, allowed range **-2 … +2**.
- `synth_version` — `1` or `2` (format/engine revision; sampler-based examples seen with `1`, engine patches with `2`).
- `base_freq` — optional float (e.g. `440.0`) present on **sampler** patches (root pitch of the recorded sample).

Sampler-engine example (a recorded sample turned into a playable synth patch):
```json
{"adsr":[64,10746,32767,10000,4000,64,4000,4000],"base_freq":440.0,
 "fx_active":false,"fx_params":[8000,8000,8000,8000,8000,8000,8000,8000],"fx_type":"delay",
 "knobs":[0,19361,27626,32767,12000,0,0,8192],"lfo_active":false,
 "lfo_params":[16000,0,0,16000,0,0,0,0],"lfo_type":"tremolo",
 "name":"20911115_1948","octave":0,"synth_version":1,"type":"sampler"}
```

## Drum kit JSON (verified — teoperator `drum.go` `DrumPatch` struct + real "boombap1" example)
A drum patch is one .aif containing a long concatenated audio file plus **24 slices** mapped across the keys.
```json
{"drum_version":2,"type":"drum","name":"boombap1","octave":0,
 "start":[0,97647201,165167950, …24 values… ],
 "end":[97643143,165163892, …24 values… ],
 "pitch":[0,0, …24 zeros… ],
 "playmode":[8192,8192, …24× 8192… ],
 "reverse":[8192,8192, …24× 8192… ],
 "volume":[8192,8192, …24× 8192… ],
 "dyna_env":[0,8192,0,8192,0,0,0,0],
 "fx_active":false,"fx_params":[8000,8000,8000,8000,8000,8000,8000,8000],"fx_type":"delay",
 "lfo_active":false,"lfo_params":[16000,16000,16000,16000,0,0,0,0],"lfo_type":"tremolo"}
```
- `start` / `end` — 24 sample-offset markers (one slice per key) into the concatenated audio. **Only ~13 bits of precision are honored** by the OP-1; the values are scaled — teoperator uses `MAXENDPOINT = 2147483646` mapped over `44100*12` samples (`SAMPLECONVERSION ≈ 4058`), i.e. these are *not* raw sample counts, they're a fixed-point scaling of position within a ~12-second buffer.
- `pitch` / `playmode` / `reverse` / `volume` — 24-element arrays, one per slice. `8192` is the neutral/center value.
- `dyna_env` — 8-int amp envelope shared by the kit.
- everything ends ~12 s; samples are normalized/truncated when built.

## How patches get *built* programmatically (tools)
- **padenot/libop1** — `op1-drum` CLI: `op1-drum [-fxon] [-lfoon] -fx <cwo|delay|grid|nitro|phone|punch|spring> -lfo <bend|crank|element|midi|random|tremolo|value> -o out.aif sample1 sample2 …` — builds a drum kit .aif with start/end markers. `op1-dump file.aif` prints the proprietary JSON of any drum or synth patch.
- **schollz/teoperator** (Go) — powers op1z.com; splits a long audio file into 24 slices on silence, writes the start/end JSON. This is the engine behind the op1.fun Drum Patch Builder lineage.
- **blattm/op1tools** (bash/Linux) — `label` adds the sound-preview render to bare "OP-1 PATCH" synth files by round-tripping them through the device's 8 user-synth slots; also `count`, `backup-user-synth`, `restore-user-synth`. Key fact it documents: **the 8 user-synth slots store the preview-render flavor; every other synth patch on the device is the bare "OP-1 PATCH" flavor.**

## Two flavors of synth .aif (important when sharing/downloading)
1. **"OP-1 PATCH"** — bare patch, no preview audio. This is how almost all stored synth patches live on the device.
2. **Preview-render** — contains a short rendered audio preview of the sound. Only the **8 user-synth slots** hold this. op1.fun/blattm generate previews by round-tripping through those slots.

## Loading onto the device (USB content/disk mode)
The OP-1 Field mounts as a USB disk ("content"/MTP mode) exposing **`synth/`** and **`drum/`** folders. You drag .aif patch files into the matching folder. (Step-by-step in the official + op1.fun captures.) No SD card — internal storage only.

## QC / unverified flags
- Exact `knobs`/`adsr`/`fx_params` numeric *meaning per engine* is not documented by TE; the ranges (≈0–32767, 8192=center) are inferred from dumped real patches and are reliable in aggregate but not per-parameter-labeled.
- The OP-1 **Field** added engines (`dimension`, `vocoder`) and the `mother` reverb FX; teoperator predates the Field so its allowed-lists don't include them, but the JSON `type`/`fx_type` strings are just engine names and Field engines use the same mechanism. Field patches are reported as backward-compatible to read but original-OP-1 patches using removed/changed engines can fail to load on Field (see RMR pack capture: ~7 synth patches "not compatible with the OP-1 field").
