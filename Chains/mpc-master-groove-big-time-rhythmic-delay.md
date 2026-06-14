---
type: chain
title: MPC-Master Groove → Big Time Rhythmic Delay
date: 2026-06-14
artists: [Daft Punk, LCD Soundsystem]
instrument: drums/sampler
gear:
  - Akai MPC Sample
  - Elektron Digitakt 2
  - Elektron Octatrack MkII
  - Roland VG-800
  - Chase Bliss Clean
  - Chase Bliss Big Time
---

# MPC-Master Groove → Big Time Rhythmic Delay ⭐

A groove-led song where the **MPC is clock master** (the fw-safe arrangement), its four-on-the-floor kit drives the tempo, and Big Time's multi-taps lock to the groove as the rhythmic centerpiece delay — with the kick ducking the delay bus for the house "breathe." A pumping four-on-the-floor groove where the delay taps lock dotted-8th against the kick; the acid bass's filter opens over the build.

🟣 DOUG-designed integration. No artist used this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

**MPC Sample** (clock MASTER) → MIDI → Big Time (follows) + DT2/Octatrack; MPC audio + VG-800 acid bass → Board 1 → Clean → **Big Time #2 Lo-Fi Rhythmic Groove** → CB stack → tape. (MPC drum bus optionally → **Clean #13 Pseudo-Sidechain Bus Limiter** for the pump.)

## Per-unit

- **MPC #29 4-on-the-Floor 909/808 Kit + Cowbell** — tuned to song key (kick=root), Swing 54–58%, Transient FX on the kick. The tempo engine.
- **MPC #31 Glitchy Beep-Beat** (optional B-section) — the un-pumped Postal Service counterpoint when you want the groove to drop out.
- **Big Time #2 Lo-Fi Rhythmic Groove (clock-locked)** — MODE Short, STATE Compressed, MOTION Off, 0.5X ON, CLUSTER ~⅓–½ (the multi-tap groove), FEEDBACK ~35% (articulate not washy), WET ~40%, subdivision via **CC54** (dotted-8th/16th). p-lock COLOR/TIME via CC14–19 from a sequencer for grid-quantized moves.
- **VG-800 #VG-E2 Around-the-World Acid Filter-Bass** — baritone as the bouncing acid bass under the kit.

## Routing

**MPC = clock master** (its MIDI-slave distortion bug means it should NOT be slaved). Big Time CC111=0 follows the MPC; CC54 sets the subdivision against the kit. **The pump is faked, not true sidechain** — either route the MPC drum bus through **Clean #13** (hot kick ducks the bus) for a hardware pump, or fake the duck on the loop with the Elektron **LFO-ramp** (DT2-E2 / OT-E2). Big Time itself is *not* in the sidechain — it just locks its taps to the grid.

## Sound

A pumping four-on-the-floor groove where the delay taps lock dotted-8th against the kick; the acid bass's filter opens over the build.

**Taste-ref:** electronic / groove-first (Daft Punk filter-house + LCD four-on-the-floor pump). ⚠️ **Approximation:** the rig has no true DAW sidechain key — the pump is an LFO-ramp / bus-limiter fake (flagged in DT2-E2/OT-E2 and Clean #13). The delay locking to the groove is real (CC54).

## Play

Start the MPC; ride Big Time **WET/CLUSTER** to swell the delay in for the chorus; switch to MPC #31 (drop the pump) for a breakdown, then slam the kit back in.

## Sources

- **Basis:** designed integration; chains **MPC #29 (+ #31)**, **Big Time #2 Lo-Fi Rhythmic Groove**, **Clean #13 / DT2-E2 / OT-E2**, **VG-E2**. MPC-as-master (fw 1.2.1 slave-distortion) + CC54 rhythmic-lock from the centerpiece source file §C [V] and Big Time sheet #2's MPC warning; the pump-is-faked flag from electronic.md honesty ledger.
- `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md`
- `Research/Chains/centerpiece-live.md` (C4)
- `Research/Taste-Profile/electronic.md`
- `Research/Taste-Profile/taste-profile.md`
