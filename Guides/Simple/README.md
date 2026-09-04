# Simple Sheets — the ADHD-friendly looping guides

HTML sheets in plain English. Short steps. No theory.
Open the `.html` files in a browser, or use the published artifact links below.

**For a new Claude session:** this folder + this README is the context. The full
detailed versions live in `Guides/Ableton Live 12 Lite/`, `Guides/Rig Map/`,
and `Guides/Wall of Sound/`. Current pedalboard truth = the owner's
"Board, Shelf & Cables" artifact (12 pedals + MC6 Pro, Deco splits to stereo
at position 04). Bass board (settled 2026-08-09, see boards.html): Polytune 3 →
108 Fuzz (buffer switch ON) → Oxford → Longsword → BF-3 (bass input) → CE-2W →
TimeLine → Big Sky → PORTA424 → Colour Box → Iridium (maybe) → Apollo in 2.
All mono TS, all 9V centre-negative. Big Sky won over Dark Star because Dark
Star is wired into guitar board slot 11 + MC6 OMNI 1 — don't move it.

## Start Here (table of contents)

**start-here.html** — hub page linking every sheet.
Artifact: https://claude.ai/code/artifact/ebd5c4d8-ee10-459d-ab7d-afc3de10ef55

## Boards (gear reference)

**boards.html** — every sound source on one page: guitar board, bass board
(pedal-by-pedal build), Yamaha S08 + 61SL keys, VST options (Parallax X =
bass amp in the box), instruments, beat/loop boxes, and the bench.
Artifact: https://claude.ai/code/artifact/453a01d6-9a09-48ca-bb49-c79b67f2dfb3

## The four sheets

1. **make-a-beat.html** — start a beat on the Digitakt 2 or the MPC Sample.
   Artifact: https://claude.ai/code/artifact/ab8254ac-67c3-4e45-9d02-7de6eed3fe96
2. **loop-with-op1.html** — walk-the-room mode. Cue mix from the Apollo feeds
   the OP-1 Field tape; overdubs stack (OS 1.7 undo = Tape+◀, 7 deep); the wall
   returns on Apollo ins 7–8; Ableton tapes the whole session on one track.
   Never send inputs 7–8 back into the OP-1's cue (feedback).
   Includes both boards + the instrument list (banjo, baritone, Asher Electro
   Slide Jr → guitar board; violin/uke/mandolin/voice → SM57; bass → bass
   board; S08 → ins 5–6).
   Artifact: https://claude.ai/code/artifact/2320067a-dee6-4362-95fb-d3b6209db6c8
3. **loop-in-ableton.html** — granular mode. One track per source (mic 1 vox,
   mic 2 instrument 57, 3–4 guitar board, 5 bass, 6 S08, 7–8 Digitakt),
   Monitor Off everywhere, arm all, live monitoring in UA Console. Click a
   slot = record, click again = loop; new takes go to the next row; rows are
   song sections. Live is clock master; Digitakt follows over direct USB.
   Artifact: https://claude.ai/code/artifact/3ca34cb3-00a5-4463-b7ec-a4e8e1cdf51b
4. **loop-on-the-ipad.html** — Loopy Pro on the iPad, wired as a third loop box.
   **CONFIRMED WORKING 2026-08-09**, exporting to Ableton. The flow: everything
   through the Behringer ADA8200 where it can go (→ ADAT → Babyface, discrete
   channels so Loopy can put each source on its own colour), Apollo cue mix into
   Babyface analog ins 3/4, return on **Apollo ins 7–8**.
   Artifact: https://claude.ai/code/artifact/fd505702-8f74-47b4-a444-590ecc7693fb

## Mode rule

- Quick session / true overdub / wandering the room → **OP-1 sheet**
- Separate, editable, muteable loops → **Ableton sheet**
- Hands-on colour looping with a screen → **iPad sheet**
- Either way, drums start on the **Make a Beat** sheet.
- The OP-1 and the iPad both return on **Apollo 7–8**. One per session.

## iPad / Loopy Pro — the routing facts (don't re-derive these)

The obvious plan (one USB-C cable, laptop ↔ iPad, iPad picks up Apollo inputs)
is impossible. Verified, not assumed:

- Apple's IDAM is **iPad → Mac only**. Nothing comes back over that cable.
- IDAM is **stereo, locked to 44.1 kHz**.
- iPadOS allows **one audio device at a time** — with IDAM active the iPad
  cannot use a USB audio interface at all.
- The box that solved this (iConnectivity AUDIO4c, dual USB-C host) is
  **discontinued** with no equivalent replacement.

What works: analog round-trip, the same topology as the OP-1.
Console CUE 1 (sends from ins 1–6) → Apollo line outs 3/4 → the **RME Babyface
Pro FS** hosted by the iPad → Loopy Pro. Return: Babyface main outs →
**Apollo ins 7–8** → monitors + one armed Ableton track. Headphone feed for
walking comes off the Babyface, built in TotalMix FX. Tempo via **Ableton Link**
over Wi-Fi. Cue sends from 7–8 stay **off forever** (feedback), same rule as
the OP-1.

Interface choice is settled — don't re-litigate it. Owned interfaces are the
Apollo x8 (Thunderbolt, UAD drivers, iPadOS can't host it), a Focusrite
Scarlett 18i8 3rd gen, an M-Audio, and the Babyface Pro FS. **The Babyface
wins on one point:** 3rd gen Scarletts do their routing in Focusrite Control,
which is Mac/Windows only, so routing can't be changed from the iPad. The
Babyface carries TotalMix in hardware and has an iPad app. Two Babyface
gotchas: Class Compliant mode is a manual toggle (hold Select + Recall while
powering up), and it needs real power — an iPad supplies ~20 mA, it wants 500.

Also owned: a Behringer ADA8200. Treated as **overflow only**, not the primary
path — the 8 analog Apollo inputs stay primary, so the 7–8 shared-slot warnings
in the sheets remain true. Wire it Apollo ADAT OUT → ADA8200 ADAT IN (clock),
ADA8200 ADAT OUT → Apollo ADAT IN (audio), ADA8200 sync switch to ADAT IN so
the Apollo stays clock master.

Ruled out: the **Eventide H90 cannot do USB audio.** Its USB-C is control and
MIDI only — confirmed by Eventide staff, not inferred. The guitar board stays
analog into Apollo ins 3–4, which is load-bearing anyway: it's what puts the
board in the Console cue mix that feeds both the OP-1 and the iPad.
