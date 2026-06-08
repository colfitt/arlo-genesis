https://www.elektronauts.com/t/octatrack-project-templates/3751
elektronauts.com · community thread (multiple authors) · 2015–ongoing

# Octatrack Project Templates — the canonical Elektronauts thread

The long-running "where are the shared OT project templates" thread. Honest finding: the OT community talks about sharing project templates far more than it actually ships them — this thread is largely a request thread, but it surfaces two concrete shares plus the standard DIY template advice.

## Concrete shared template
**Crossfader Transition Project** (author: virtual_flannel)
- A starter Set/Project built to demonstrate **scene-to-scene crossfader transitions**.
- Author's key note: it required "fine-tuning," and that **Scene parameter-locks are the whole point** of the setup — the transition lives in the difference between Scene A and Scene B values.
- Download posted in-thread (post #12): `http://www.elektronauts.com/files/download/63` (old forum file host — may be dead now; flag as possibly-broken link).
- Reported use: people loaded "64-hit sample chains and crossfaded" with it (i.e. drop a 64-slice chain on a track, scene A = one slice region/clean, scene B = mangled, ride the fader).

## DIY template pattern repeatedly recommended in-thread (subq and others)
A reusable "house" Project the OT community keeps re-describing — build this yourself as your blank-canvas starting Project:
- **Track 8 = master bus**: a Neighbor or master-style track running a **compressor + reverb** for the whole mix.
- **Thru machines** pre-placed on dedicated tracks for external gear (so external audio is always one trig away from being processed).
- **8 MIDI tracks pre-assigned** to the channels of your external drum machines / synths, so a new pattern can immediately sequence the rest of the rig.
- Saved as the project you copy/duplicate for every new song.

## How to load any shared OT Project
A shared template is a **Set/Project folder** (contains `project.work`, `project.strd`, bank/markers files, and an `AUDIO` pool). Copy the folder onto the CompactFlash card, then on the OT: **PROJECT → LOAD PROJECT** (or load the SET it lives in). Save before swapping the card.

## Honest note
Only the Crossfader Transition project is a real downloadable artifact here, and its old-forum download URL may be dead. The bigger value is the recurring DIY master-track + Thru + MIDI template recipe.
