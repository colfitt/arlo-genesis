Manual: Octatrack MkII User Manual, §17.5 (p.111), Appendix A.4 Neighbor (p.120)
Elektron manual

# OT as a deep effects processor — Thru → Neighbor chain (up to 8 FX on the pedalboard)

Each track has only **2 FX blocks**. To stack more processing on the incoming pedalboard signal, chain tracks with **Neighbor machines** — a Neighbor listens to the *output of the preceding track*. A Thru on track 1 feeding Neighbors on 2/3/4 gives up to 8 serial FX on the live wall.

## Setup
1. MIXER: **DIR AB = 0** (input only via Thru). Confirm `<REC>` LEDs show signal.
2. **Track 1 = Thru machine**, INAB = A B. Assign FX1 + FX2 (e.g. filter → Lo-Fi).
3. **Track 2 = Neighbor**, **Track 3 = Neighbor**, **Track 4 = Neighbor**. (Neighbor **cannot** be on track 1 or 5 — those are chain "heads".)
4. Assign two FX to each of tracks 2/3/4 (e.g. comb → chorus, then phaser → reverb, then EQ → Dark Reverb). An 8-deep serial FX rack is now formed.
5. **Track 1: place one trig** on step 1 to start the Thru passing audio. Press [PLAY]. The pedalboard signal, shaped by all chained FX, comes out the mains.

## Performance + mute behavior
- Use **scenes + crossfader** to ride multiple FX params across the chain at once; add p-locks for rhythmic FX bursts.
- **Muting:** with a Neighbor chain, the tracks *preceding* the last Neighbor can't be muted individually — **mute the last Neighbor** (track 4) to silence the whole chain.

## "Automated real-time sampling" variant (manual's strange-results tip)
Instead of a Thru on track 1, put a **Flex machine with recorder buffer 1** on track 1, drop **recorder trigs** that sample input A/B, and **sample trigs** that play buffer 1 back — p-locking pitch / FX / using LFOs per step. The OT continuously samples the incoming pedalboard and re-plays the just-captured audio, mangled. This is "capture-and-destroy" running on autopilot under the live guitar.

## Rig fit
Two stereo input pairs (A/B and C/D) + Neighbor chaining means you could process the **main pedalboard print on A/B (Thru → Neighbor rack)** while a **second feed (e.g. a VG-800 synth/COSM patch, or an Apollo monitor send) on C/D** runs its own Thru track — two independent live-FX racks in one box.
