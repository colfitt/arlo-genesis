https://www.maxforlive.com/library/device/14227/lost-found-editor-for-chase-bliss-pedal
maxforlive.com · SonicFreaks · added 2025-12-28 · v1.0 (commercial)

# Third-party Lost + Found editor (SonicFreaks)

The one notable community/third-party software tool found for the Lost + Found: a **Max for Live device + standalone macOS app** that gives a full graphical editor over MIDI. Relevant to this rig because the pedal hides ALT, EQ, SPILL, GLUE, ramp/bounce arming, swaps and routing behind footswitch-holds and two dip banks — an editor removes the "no dip switches, no manual diving, no guesswork" friction.

## What it does (per the listing)
- "Unlocks all hidden features, no dip switches, no manual diving, no guesswork." Design patches, explore routing, automate parameters via MIDI/DAW.
- **Preset management:** save patches to disk, recall them, or store them directly into the pedal.
- **Smart UI:** "When you change FX algorithms, the editor automatically updates all relevant dial names" — so the knobs relabel per the active mode (e.g. ALT becomes "diffusion" / "grain shape" / "failure" depending on engine).
- Resizable interface with onboard help docs; auto-recalls its own settings on reopen.
- Parameter automation through MIDI / the DAW timeline (so ramp/bounce-style motion can be sequenced from Ableton instead of armed via dips).

## Two delivery formats
- **Standalone macOS app** (no Ableton needed), and
- **Max for Live device** (macOS + Windows). Tested against Live 12.0.5 / Max 8.6.2.

## Rig relevance / honest caveats
- For a Digitakt-clocked, MIDI-heavy rig, a DAW/M4L editor is the cleanest way to dial and store the dense L+F scenes, then recall them as presets on the pedal — complements (does not replace) the MIDI scene/clock workflow already documented in `Gear/Chase Bliss Blooper/research/links/cb-stack-preset-scene-recall.md`.
- **Commercial** (paid), **third-party** (not Chase Bliss), and **v1.0 / Dec-2025** — i.e. brand-new and unverified for stability/coverage. CB's own MIDI implementation is the source of truth; treat the editor's parameter mapping as convenient but unaudited.
- This is the only dedicated L+F software tool surfaced — no free community editor or web tool was found. Flag: thin tooling ecosystem, consistent with the niche/new install base.
