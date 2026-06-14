https://www.logicprohelp.com/forums/topic/147505-how-to-set-up-midi-to-control-antares-vocodist/
LogicProHelp forum thread "How to Set Up MIDI to control Antares Vocodist - Logic Pro" + Antares Help Desk article (canonical AT-in-Logic procedure)
[Forum + Antares help page both 403 to the fetcher; steps triangulated from search-engine extracts — LABELED triangulated]

# Vocodist CARRIER ROUTING IN LOGIC — the explicit answer (most important deliverable)

## The core fact about Logic + AU MIDI/side-chain (verified, well-established mechanism)
In Logic, **audio-track inserts do not receive MIDI**. Only **software-instrument tracks** receive
MIDI. Antares solves this the standard AU way: the plug-in is loaded as the **Instrument** of a
software-instrument track via Logic's **"AU MIDI-controlled Effects"** category, and the audio you
want to process comes in through the plug-in's **Side Chain** menu. This is the same mechanism for
Auto-Tune Pro/Artist, Harmony Engine, and **Vocodist** (they share the AT MIDI-effect framework).
**This is a long-established, working Logic path — NOT the broken-AU-sidechain situation that hit
Arturia MS-20 V.** (The Antares tools are explicitly designed for and documented in this workflow.)

## ⚠️ Key clarification: two different "carrier" questions in Logic
Vocodist's carrier is chosen by its **Synth → Source** menu, independent of how MIDI gets in:

### A. Internal synth carrier — pitch-tracked from the voice (NO routing needed)
Drop Vocodist on the **audio track** carrying your modulator (banjo / voice / baritone). Synth
Source = **Oscillator**, Pitch Track = **Voice** (or **Key** for a drone). The internal 8-voice
osc IS the carrier and follows the input. **Zero MIDI, zero side-chain.** This is the simplest and
the recommended starting point — and it covers the rig's "Key drone → talking-pad" mode entirely.

### B. Internal synth carrier — played by MIDI (need the AU-MIDI-effect track in Logic)
To play the carrier as chords from the 61SL MkIII while the voice/banjo supplies the words:
1. Create a **software-instrument track**. As its **Instrument**, choose
   **AU MIDI-controlled Effects > Antares > Auto-Tune Vocodist**. (This is how the plug-in receives
   the MIDI on that track.)
2. Put your modulator audio (banjo/voice) on a separate **audio track**; set that audio track's
   **output to "No Output"** (so you don't double-hear it).
3. In the Vocodist window, open the **Side Chain** menu (top-right) and select that audio track —
   that feeds the **modulator** into Vocodist's analysis bank.
4. In Vocodist set Synth Source = **Oscillator**, Pitch Track = **MIDI**.
5. **Record-enable (R) the software-instrument track** and play the 61SL → the carrier follows your
   chords while the side-chained audio supplies the vocoded articulation.
   *(Steps mirror Antares' official "MIDI control of Auto-Tune Pro/Artist in Logic Pro" article,
   which uses the identical AU-MIDI-effect + Side-Chain pattern — triangulated.)*

### C. External side-chain carrier — your own synth/drone/VG-800 as the carrier
This is the rig's headline use (sustained drone = carrier, banjo/voice = modulator):
1. Put the **modulator** (banjo/voice) on the **audio track where Vocodist is inserted** (a normal
   audio-track insert — no instrument track needed unless you also want MIDI pitch).
2. Route your **carrier** source (a synth track, drone, VG-800, Mellotron, hardware-synth track)
   to a **bus**, and select that bus as Vocodist's **Side Chain** input.
3. In Vocodist set Synth Source = **Side Chain**. The Oscillator controls gray out; you now have
   **Comp / Gain** to condition the side-chain carrier level.
4. Vocode: the drone's harmonics are shaped by the played modulator's formant/envelope.
   (Official Antares video confirms this "instrument track output → side-chain bus → Source = Side
   Chain" flow; it demos in Pro Tools but the side-chain concept is identical in Logic.)

## Honest flags on the Logic answer
- The **A** path (internal osc, Voice/Key pitch) is fully verified by the manual + both videos and
  needs no special routing — **highest confidence**, and it already delivers machine-choir / drone
  walls.
- The **B/C** paths use Logic's standard **AU MIDI-controlled Effects + Side-Chain** mechanism. That
  mechanism is verified for Antares' Auto-Tune family in Logic (official help article + forum); the
  Vocodist-specific click-path is **triangulated** from the Auto-Tune-Pro Logic article (same
  framework) + the official Vocodist video (which demos in Pro Tools). The manual itself defers the
  exact side-chain setup to a JS-walled help page (p.25). **Confirm the exact menu labels on the
  user's install** — but there is no known Vocodist-in-Logic side-chain/MIDI blocker comparable to
  the MS-20 V issue.
- Whether the **external side-chain carrier** requires the instrument-track variant or works from a
  plain audio-track insert depends on whether you ALSO want MIDI pitch. For C (no MIDI), a plain
  audio insert + side-chain bus is enough.
