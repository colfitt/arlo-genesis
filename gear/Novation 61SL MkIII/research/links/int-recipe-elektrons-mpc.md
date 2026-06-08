Manual: SL MkIII V2 pp.13–14 (Parts/Channel/Destination), 18 (Clock Tx), 8–12 (sequencer) + Components factory templates (Octatrack, Digitakt)
Novation manual + Components factory template library

# RECIPE — Sequence the Elektron rig + MPC as clock master

## Goal
SL = standalone clock master + 8-track poly sequencer driving **Digitakt 2**, **Octatrack MkII**, **Akai MPC Sample** at once, each on its own Part / channel / destination.

## Cabling options
- **All-DIN:** SL DIN Out → Digitakt MIDI In → (Digitakt MIDI Thru) → Octatrack MIDI In → … daisy-chain, OR use SL **Out 2 = "Out"** for a second independent chain (see `int-din-routing-destinations.md`). MPC via USB or the second DIN.
- **Mixed:** Digitakt/Octatrack on DIN, MPC on USB. Each Part just picks USB vs DIN1/DIN2.

## Part setup (Shift + Sessions = Part Settings)
- **Part 1 → Digitakt 2**: Destination **DIN 1**, **Channel = Ch1** (match Digitakt's AUTO/track MIDI-in channel).
- **Part 2 → Octatrack MkII**: Destination **DIN 1** (or **DIN 2**), **Channel = Ch2** (match an OT track's MIDI channel).
- **Part 3 → MPC Sample**: Destination **USB** (or **DIN 2**), **Channel = Ch3**.
- Each Part can also use a factory **Components template**: Components ships **Elektron Octatrack** and **Elektron Digitakt** templates — load them so the encoders/buttons map to those boxes' known CCs out of the box (then tweak).

## Clock / transport (SL as master)
- **Global → MIDI Clock Tx = On.** 24 PPQN goes to **USB + both DINs** simultaneously.
- On each Elektron/MPC: set **Clock Receive = On** and **Transport Receive = On** (follow external). SL **Play/Stop/Continue** then start/stop the whole rig.
- Set tempo on the SL (**Tempo** button, 40–240 BPM).

## Performing
- Build 16-step patterns with **micro-steps** (6 per step) for triplet/glitch runs; **gate to 32 steps** for held drones.
- One Part on **Random direction + ~60–80% Chance** = generative motion; pattern-chain the others for structure.
- **Mute/Solo per Part** (top yellow / bottom blue soft buttons) to arrange live.
- 8 automation lanes/track to ride params over time.

## The "who sequences whom" decision (important)
The Octatrack, Digitakt, and MPC all have their **own sequencers**. Decide per song:
- **SL sequences them** (above) → set the boxes to play sounds from incoming MIDI notes; don't run their internal patterns on the same tracks (double-sequencing chaos).
- **OR an Elektron is master sequencer** → SL **MIDI Clock Rx = On**, feed clock from ONE source (e.g. Digitakt DIN-out → SL DIN-In), SL follows; SL then just adds keybed/CV parts. Don't have SL Tx On and Rx-ing simultaneously.

## Alt: MPC as clock master
- Set MPC to send clock; SL **Clock Rx On**, fed from MPC (one source only). SL plays melodic/keys parts into the MPC's pads-can't-easily-play range.
