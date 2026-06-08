https://www.elektronauts.com/t/digitakt-ii-bug-reports/216060
elektronauts.com · community bug-report thread (+ OG-migration threads below) · 2024–2025

# Digitakt II — Bugs, Firmware Lore & OG→DT2 Migration Gotchas

Pulled from the main DT2 bug-reports thread plus the OG-migration threads. This is the "what bites people" facet.

## Firmware / OS gotchas
- **Pitch-bend range bug** (OS 1.01A → fixed in OS 1.02). Pitch-bend range was wrong (not −128…+127), causing off-pitch sounds. Fixed in 1.02. [Confirmed fixed.]
- **+Drive folder delete error** (seen on OS 1.02). Creating/deleting folders via Elektron Transfer could throw "Device failed with operation"; on-device deletion showed "Error (Not Empty)!" One user's fix was a full **+Drive format** (back up first). Status: not confirmed by Elektron support as of the report.
- **Pattern corruption after an OS update** (reported on 1.02). One user: "Some patterns have been changed to the point in which they are no longer recognizable" after updating. Cause unclear. Reported to occur even with the unit connected to a DAW via USB. [Unverified / isolated — but a real backup warning.]
- **USB / Logic auto-connect quirk** carried over unresolved from an earlier thread.
- **+Drive corruption near capacity** (fixed in OS 1.02). Filling the +Drive with many GB of imported samples could crash and produce faulty samples before the 1.02 fix.

**Community rule of thumb (verbatim):** "Avoid upgrading before a gig!" — and back up every project + the +Drive before any OS update.

## OG (Digitakt 1) → Digitakt II migration
Source: https://www.elektronauts.com/t/transferring-og-digitakt-projects-to-digitakt-ii/227198 and https://www.elektronauts.com/t/digitakt-1-to-digitakt-2-data-transfer/212486

- **The bottom-8-tracks gotcha** (Sam1, verbatim): "once the digitakt 1 project is in the digitakt 2, the bottom 8 tracks are now only midi like they were in the og digitakt." Because the OG had a fixed 8 audio + 8 MIDI split, an imported OG project lands with tracks 9–16 still configured as MIDI. NOT a data-loss bug — you just have to convert them.
  - **Fix** (Re5et, verbatim): "It's just a few button presses to change the machine … seconds per track." Change each of tracks 9–16 from a MIDI machine to an audio machine.
- **Kits don't travel with the project** (community): kits are not carried across on save, and Transfer currently has no kit-management/export option. Plan to rebuild kits, or save sounds as presets first.
- The mono OG samples import fine but stay mono — you'd re-sample in stereo or swap in stereo source material to actually exploit the DT2's stereo engine.

## Other confirmed DT2 behavior worth knowing (not bugs, but gotchas)
- **Audio tracks are monophonic** — no chording on one track; layer tracks (see CTRL-SEL trick in the tips file). Catches MPC/Maschine pad-poly users.
- **Chorus collapses to mono when sent into the Reverb** (see the send-FX capture file) — a real limitation when chasing wide ambient sends.
- **Resampling feedback**: with input monitoring ON, the signal you're sampling is also sent to the Main Outs, so re-amping through external FX and back in creates a feedback loop unless you disable TO MAIN monitoring (see resampling capture file).

NOTE: post-number specifics vary; bug statuses above reflect what was reported/confirmed in-thread as of mid-2025. Anything tagged Unverified is a single-user report.
