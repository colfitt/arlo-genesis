https://support.apple.com/guide/logicpro/bounce-in-place-overview-lgcpe2a9f868/mac · https://whylogicprorules.com/bounce-freeze-poweroff/
apple.com + whylogicprorules.com · Logic Pro User Guide / community · current

# Freeze vs Bounce in Place vs Disable ("Power Off") — CPU management

All three free up CPU by printing a track's plugin chain. Pick by how
reversible you need it.

## Freeze (the in-progress workhorse)
- Renders the track + its plugin chain to a temp file; **track still looks the
  same** and is fully restorable (un-freeze to edit, re-freeze).
- **32-bit float** render — safe against clipping.
- Enable the Freeze button column: **Track menu / right side of track header**;
  freeze runs on next playback.
- **Freeze Mode (per track, in track inspector)** matters a lot for drone:
  - **Source Only** = freezes the instrument/region but LEAVES the insert FX
    live and editable (lighter CPU win but keeps your reverb tweakable).
  - **Pre Fader** (a.k.a. full / "Pre Fader") = freezes the whole chain
    INCLUDING inserts — maximum CPU relief; use for finished texture beds.
  - Choose Source Only while still sculpting the wall, Pre Fader once locked.
- Freeze captures **reverb/delay tails** within the frozen region length —
  for very long ambient tails extend the region/add empty bars before freezing
  so the tail isn't cut off.

## Bounce in Place (commit)
- Renders to a **new 24-bit audio file at project sample rate** on a NEW track;
  mutes the original (kept, not deleted). Permanent, portable stems.
- Best for "finished" tracks, sharing stems, or printing a hardware/External
  Instrument return to audio.
- Options dialog: include/exclude volume+pan automation, normalize, bypass
  effect plug-ins, and add a tail.

## Disable track ("Power Off")
- Right-click track > Disable (or the on/off in some layouts) — unloads the
  plugins from RAM/CPU entirely. Heaviest CPU relief, but the track is silent
  and inert until re-enabled. Good for parked alternate takes / unused
  instrument tracks in a big drone session.

## Decision
In progress → **Freeze (Source Only)**. Locked texture bed → **Freeze (Pre
Fader)**. Done / need a stem / printing hardware → **Bounce in Place**. Parked
/ not using → **Disable**.
