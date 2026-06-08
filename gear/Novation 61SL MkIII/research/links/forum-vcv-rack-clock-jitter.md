https://community.vcvrack.com/t/stable-external-midi-clock-with-novation-sl-mk3/11564
community.vcvrack.com · "Stable external MIDI clock with Novation SL Mk3" · posters: juozasgaigalas, Soxsa

The clearest first-hand jitter report — relevant because the SL is this rig's clock master and CV bridge.

## Symptom
- **juozasgaigalas:** syncing VCV Rack to the SL Mk3 was "**jittery, drifty and laggy**. Sometimes hardware and VCV Rack sequences would be in sync and other times not."

## What was tested
- **External hardware as clock master → VCV:** drift/jitter once clock passed through VCV modules.
- **VCV as master → hardware:** solid software side, but "hardware sequence gates dropping out of sync."
- **Hardware Start/Stop control:** the **most stable** approach — using transport resets to re-align phase.

## Fixes / mitigations
- Don't average/modify the incoming clock; instead **preserve clock integrity** (used Holonic Systems "Gaps" module in "Mus" mode) and **re-trigger transport (Start/Stop) to resync.**
- **Soxsa:** residual jitter "**of a few ms whatever method I try**" — accepted as inherent USB/MIDI timing slop, not an SL-specific defect.
- One user: try the **3.5 mm analog Clock Out** instead of MIDI clock for tighter sync to gear that accepts it.

## Rig takeaway
- Expect a **few ms of MIDI-clock jitter** — fine for most material, but for tightly phase-locked layers prefer the **analog Clock Out** (at 1 or 2 PPQN — see the clock-drift file) and use **transport Start/Stop to re-align** if things wander. For the Elektron chain, the Digitakt/Octatrack's own clocking is tighter; consider letting an Elektron be master and slaving the SL (it locks at 24 PPQN) for the most rhythmically critical pieces.
