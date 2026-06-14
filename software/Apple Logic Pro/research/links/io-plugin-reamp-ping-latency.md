https://forum.kemper-amps.com/forum/thread/66198-what-is-your-favorite-reamping-method-in-logic-pro-x/ · https://unity.neuraldsp.com/t/how-do-i-set-the-latency-compensation-in-logic-pro-for-re-amping-to-qc/15642 · https://www.soundonsound.com/sound-advice/q-how-do-compensate-latency-logic
kemper forum + neural dsp forum + soundonsound (Paul White) · community

# The I/O plugin reamp method in Logic — auto latency-compensated send to outboard

This is the "proper" reamp path (vs the record-to-a-new-track + nudge method in
lug-reamping-di-to-hardware.md). Use it when you want the reamped return to land
TIME-ALIGNED automatically, e.g. parallel outboard on a bus or a Kemper/board
return that must sit in the mix.

## Setup (step by step)
1. **Insert the I/O plugin** on the DI/source track (an insert slot, like a
   console insert point).
2. In the I/O plugin: **Output = the interface output** wired to your reamp box
   / pedalboard input; **Input = the interface input** receiving the
   amp/pedalboard/Kemper return.
3. **Create a new audio track**, record-enable it, and set its **input = the
   SAME input** the I/O plugin is listening on (the wet return).
4. Hit record — the dry track plays out through the rig and the processed return
   prints to the new track, latency-aligned.

## The Ping button (the key feature)
- Click **"ping"** — the I/O plugin sends a short test signal out through the
  amp/rig and back, **measures the exact round-trip latency**, and compensates
  for it automatically.
- If auto-comp isn't tight enough, you can dial an **additional manual offset**
  in the I/O plugin. Important: that extra offset is **applied ONLY when
  reamping through the I/O plugin** — "there's nothing that needs to be removed
  later when recording" normally.

## Why latency exists (Paul White / SoS)
- The signal goes through **AD→DA→AD conversion twice** (out to analog, back to
  digital). The I/O plugin hooks Logic's automatic plugin-delay-compensation,
  but it "won't compensate for any delay caused by the device itself" — ping
  closes that gap.
- Precision-align alternative (for critical phase): duplicate the track, flip
  phase with the **Gain plugin**, put the outboard on one copy, adjust **Track
  Delay** for max cancellation (null), then fine-tune with the **Sample Delay**
  plugin.

## Rig note
For this rig: I/O plugin Output → Apollo x8 line out → **Radial X-Amp**
(reamp box, converts line→hi-Z instrument) → pedalboard / VG-800 → back into
Apollo line in → I/O plugin Input. The X-Amp is the correct impedance bridge so
the pedals see a proper guitar-level signal. Ping after every repatch since the
round-trip changes with cable/buffer.
