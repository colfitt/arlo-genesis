https://www.soundonsound.com/techniques/making-impulse-responses-logics-ir-utility
soundonsound.com · Sound On Sound · (technique article — Logic's IR Utility / Space Designer)
(also draws on: https://support.apple.com/guide/logicpro/use-impulse-responses-lgcef2af4d05/mac and the MusicRadar Space Designer guide https://www.musicradar.com/news/logic-pro-space-designer-guide)

Reference for custom-IR sourcing and the drone-friendly Space Designer parameters — the bridge between "record a weird space / object" and "use it as a reverb in the rig."

## Making your own IRs (IR Utility workflow)
- Logic ships an **IR Utility** and a sine-**sweep** track. Play the sweep through a loudspeaker in a real room while re-recording with one/two ambient mics; deconvolve the recording against the sweep to get a custom IR.
- Best capture mics: **condensers**, **omni** pattern → most natural ambience and HF detail. (Rig: KM184 / AT2020 are the condensers on hand.)
- Beyond rooms: you can convolve against **any** sample — percussion hits, sustained tones, metallic objects — to get "impossible" resonant spaces. Load via the **Sample IR → Load IR** menu (works identically to factory IRs).

## Drone / sound-design parameters in Space Designer
- **Quality**: **Lo-Fi** = grainy reverb (good for degraded aesthetic); **High** = smooth/clean.
- **Length** + **Size**: stretch the IR length and widen/narrow the room to push small captures into "enormous, other-worldly" tails.
- **Reverse**: turns Space Designer into drone-like resonators and ghostly tempo-synced echo effects.
- Factory IRs span tiny/intimate → enormous; "Big Cave," cathedral, and reverse-instrument IRs are the long-wash favorites.

## Rig fit
Custom IRs are the obvious way to get the *rig's own gear* into Logic's reverb engine: convolve a single banjo pluck, a VG-800 drone, or a feedback swell into an IR and you have a reverb that resonates at the rig's own harmonics. Lo-Fi quality + reverse = the degraded/"recorded-wrong" reverb.
