https://www.youtube.com/watch?v=FwxTZfshTDs
Richard DeHove · Strymon Timeline tutorial: Looping in perfect sync · 2022-03-18 (15 min)

> How to drive the 30-second looper entirely from MIDI notes off a clocked sequencer so loops record and play in perfect sync — the only kind of looping DeHove considers useful in a clocked rig. Directly applicable to a Digitakt-clock-master setup. Cleaned from the channel's manual English captions; light punctuation added for readability.

---

For me the only looper that's useful is one that can do **perfect sync**. If your loop is going to play along with clocked machines and sequencers, then your loop must also be clocked — no human can precisely hit a perfect loop point. Happily, the looper in the TimeLine is clockable and can easily be set up to record and play in perfect sync.

## What you need
A device that can send **MIDI note + clock** to the TimeLine. He uses an Arturia KeyStep 37 (a normal KeyStep is fine; just about any decent sequencer works). One critical proviso: the looper transport commands live at the very bottom of the MIDI note range, so your sequencer must reach **MIDI note 0 (C-1)**. (His Dreadbox DB-01 only goes down to C0 / note 12, so it couldn't do it.) From the TimeLine manual graphic:
- **Note 0 = Record**
- **Note 2 = Play**
- **Note 4 = Stop**
- **Note 14 = Toggle Reverse**
- **Note 16 = Toggle Half-Speed**

## Prerequisites
The sequencer, the TimeLine, and your music source all need to be on a **common clock and in sync** (true already in any synced synth/drum setup). Ideally have a system-wide **Start** command to fire everything together (he uses an E-RM Multiclock). The sequencer should be set to **play each pattern fully through before switching** (don't jump the instant you select the next pattern) — the Arturia default, and the default in most machines.

## Looper global settings (press-and-hold VALUE → globals)
- **Loop Location (LP LOC):** **Pre** = records the raw signal; **Post** = bakes in whatever delay you've got going. He starts on **Post**.
- **Looper Level:** playback level of the loop — set to maximum.
- **Loop Exit:** what happens when you leave the looper — set to **Stop** here (it can also be Play, to keep the loop running in the background).

## Entering looper mode
Press and **hold TAP** → "looper" appears. Manual controls: **A = record, B = play, TAP = stop.** But here everything will be driven by MIDI notes from the sequencer instead.

## Building the sync sequences (his method)
He programs separate one-command sequencer patterns, each the same length, so the loop boundaries line up with the clock:
1. **Seq 1 (Record):** while programming, he temporarily uses **MIDI channel 2** so hitting notes doesn't trigger the TimeLine (everything actually communicates on channel 1). Spam the octave-down key to reach **Note 0** (Record). Record it as an **8-step** sequence.
2. **Seq 2 (Play):** **Note 2** (Play), also **8 steps**, matching the record sequence length.
3. Shift back to **MIDI channel 1** (where the TimeLine listens), select Seq 1, put the pedal in looper mode, and hit **Start** on the master clock.

Result: it records the 8-step loop, and *before recording even finishes* he switches the sequencer to Seq 2 (Play) — because the record pattern plays to its very end and then the play pattern takes over, so the loop drops straight into playback "seamlessly, as if nothing had ever happened," in perfect sync (verified by running an arpeggiator over the top).

## Pre vs Post in practice
Switching LP LOC to **Pre** records the loop dry (no baked-in effect). He notes Post can be better for ambient material: if you start recording right at the top of the sequence, Pre won't capture the *tail* of effects, whereas Post bakes the wet tail into the loop.

## Reverse and Half-Speed sequences
- **Seq 3:** Note **14** = Toggle Reverse (record on channel 2, 8 steps; play back on channel 1).
- **Seq 4:** Note **16** = Toggle Half-Speed.
- **Seq 8:** he stacks Toggle Half-Speed + Toggle Reverse on alternating steps for deliberately strange, glitchy, perfectly-synced mangling.

Switching between these sequences live (play → reverse → half-speed → back) turns the TimeLine into "not really just a looper now, but a pretty sophisticated audio recorder and mangler," all in perfect sync. You don't even need to be *in* looper mode for the sequencer to drive it — you can exit looper mode and the MIDI note commands still work; he just stays in looper mode to keep track of what's happening.
