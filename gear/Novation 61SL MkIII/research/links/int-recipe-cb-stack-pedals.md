Manual: SL MkIII V2 pp.13–14, 18 (Parts/Templates/Clock) + Components editor
Novation manual + Components

# RECIPE — Drive the Chase Bliss stack + Hologram + H90 from the SL

## Scope
The rig's MIDI-clocked pedals: **CB Brothers AM, Clean, MOOD MkII, Blooper, Big Time, Generation Loss, Onward**, plus **Hologram Microcosm & Chroma Console**, **Eventide H90**. All take **CC + PC** and **MIDI clock** for tempo sync. The SL sends CC/PC from Templates and clock from the master.

## Physical link & channels
- SL **DIN Out** → pedal MIDI In; daisy-chain via each pedal's MIDI Thru, OR split across **Out 1 / Out 2** (Out 2 = "Out") for two chains. (CB pedals use TRS-MIDI on the device — use the appropriate Chase Bliss/Empress-style TRS-MIDI cable/adapter from the DIN.)
- Give each pedal its **own MIDI channel** (set on each pedal). Match each SL Part's **Channel**.

## Template (Components) per pedal type
- Build a Template mapping the **8 encoders / 8 faders** to each pedal's documented CCs (each CB pedal's params map to specific CCs — pull from that pedal's own dossier/manual). Use **buttons** as **PC** (preset recall) or **CC toggles** (bypass / effect on-off, ramp/expression CCs). Set **Low/High** to scale ranges; use **toggle** for on/off, **momentary** for tap-style.
- The seven CB pedals share a near-identical control surface → author one, **clone & re-channel** per pedal (libslmkiii is fast for this — see `int-libslmkiii-library.md`).
- **Aftertouch → a CC** for expressive real-time mod (e.g. MOOD/Blooper modulation depth).

## Part setup
- One **Part per pedal** (8 Parts = up to 8 pedals), each Part = its Template + matching **Channel** + **Destination** (the DIN going to that chain).
- The SL's per-Part design means you can have the keybed/sequencer play notes to soft synths on some Parts while other Parts are pure CC/PC controllers for the pedals.

## Clock / tempo sync
- **Global → MIDI Clock Tx On** → 24 PPQN to both DINs. Pedals with MIDI-clock tempo sync (Blooper, MOOD, Microcosm, H90, etc.) lock their subdivisions to the SL's BPM.
- Set each pedal to **receive MIDI clock**; pick its sync subdivision on the pedal.

## Performance notes
- Use the SL's **sequencer automation lanes** to record CC sweeps (e.g. a slow Generation Loss wow/flutter ramp) and play them back in sync.
- PC from a Template button = jump pedal presets in time; combine with SL **Sessions** so a Session recalls a whole pedalboard state + sequence + clock.
- No factory Components templates exist for any of these — all build-your-own.
