Manual: Octatrack MkII User Manual, §9.3 (p.49–50), §17.1.4 (p.105), §17.1.5 (p.106), Appendix A.5 (p.121)
Elektron manual

# PICKUP MACHINE — live-loop the rig (banjo / fuzz wall) as a sync-locked looper

Pickup machines are the OT's **looper**: capture a loop, overdub, repeat, re-pitch/reverse, and **conform the project BPM to the captured loop**. A Pickup machine is **hard-linked** to its track's recorder and recorder buffer — no buffer assignment needed. The track must be **active** to sample. Pickup machines **cannot be sequenced or p-locked** (unlike Flex/Static).

## Key behavior — master vs slave
- The **first Pickup machine to record a loop = master**. The **OT BPM auto-changes to that loop's calculated BPM.** Everything downstream (synced gear, FX times) follows.
- Pickup machines on other tracks record **slave loops**. **LEN** sets slave length vs master: **X1** = same length + phase-locked to master, **X2** = double length, etc.
- Stop all Pickups → next one to record becomes the new master.

## On-panel control (per track, with a Pickup machine)
The [REC1]/[REC2] keys change meaning for Pickup tracks: **[REC1] = record/overdub toggle, [REC2] = play/stop toggle.** Behavior depends on the **TRIG** mode (RECORDING SETUP 1):
- **ONE** — [REC1] starts recording (length = RLEN); press again = restart. After RLEN it auto-enters overdub. [REC2] = stop/play loop.
- **ONE2** — like ONE, but you define loop length on the fly: press [REC1] = begin overdub, [REC2] = begin playback. (Best for free-form looping.)
- **HOLD** — hold [REC1] to record, release to play. Hold [REC1] again to overdub. (Momentary/loop-pedal feel.)

## Concrete setup — loop the banjo (EBM-5 → GK-5 → VG-800) on input A/B
1. **Track 1 = Pickup machine** (double-tap [TRACK 1] → Pickup).
2. **RECORDING SETUP 1** ([FUNC]+[REC1]): **INAB = A B**, INCD = −, **RLEN = MAX**, **TRIG = ONE2**, SRC3 = −, **LOOP = ON**. (Eliminating C/D + internal sources prevents accidental wrong-source capture.)
3. **RECORDING SETUP 2** ([FUNC]+[REC2]): **FIN = 0.063, FOUT = 0.063** (tiny fades kill loop-point clicks), **AB = 127** (direct-monitor the input through this track while the Pickup is active — so you hear the banjo without touching MIXER DIR), **QREC = OFF, QPL = OFF**.
4. **SRC MAIN** ([SRC]): **PITCH = 0** (must be 0 for overdub/replace to work), **DIR = FWD**, **GAIN = 0**, **OP = DUB**. LEN is irrelevant for the master loop (set OFF).
5. Play the banjo. **[REC1]** to start the loop, **[REC2]** to close it — it immediately loops and OT BPM snaps to it. **[REC1]** again = overdub another pass; **[REC2]** = stop overdub (loop keeps playing).
6. For a **slave layer** (e.g. a baritone drone twice as long): Track 2 = Pickup, same RECORDING SETUP, but **SRC MAIN LEN = X2**. Record after the master exists; it auto-locks to 2× master length and phase.

## Re-pitch / reverse / fade the loop
- **PITCH** (SRC MAIN): ±1 octave; integers = semitones. (Re-pitching disables overdub until back to 0.)
- **DIR = REV** = reverse loop; **DIR = PIPO** = ping-pong.
- **GAIN** + **OP = GAIN** = no new recording, only volume rides → gradual loop fade-outs / swells.
- **TSTR** can't be turned off on Pickups — loops always timestretch to BPM. Tune **TSNS** higher to track banjo picking transients.

## Sync the OT sequencer to the loop
**[TRACK] + [TEMPO]** locks the sequencer tempo to a chosen Pickup loop (BPM readout is replaced by which Pickup is driving). With sequencer stopped + Pickup playing, [PLAY] starts the sequencer at the loop's next downbeat. Use this to mix programmed Flex/MIDI tracks against the live loop without drift.

## Gotcha (from Elektronauts)
**Overdub misbehaves when the OT is a MIDI clock SLAVE** — even slaved to other Elektrons. For reliable Pickup-machine overdubbing, run the **OT as clock master** (see clock-topology-ot-61sl-digitakt.md).
