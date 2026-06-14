https://vi-control.net/community/threads/valhalla-reverbs-as-send-or-separate.73549/ + https://www.sageaudio.com/articles/how-to-make-a-vocal-chain + general producer practice (search-snippet distilled; VI-Control 403'd on direct fetch)
VI-Control + Sage Audio + community practice · ~2019–2023

# ValhallaRoom — chain placement, sends, saturation & delay (community practice)

Distilled from search snippets + the VI-Control "send or separate" thread (403 on direct
fetch — flagged) + general mix-chain consensus. Tailored to the drone/doom/shoegaze rig.

## Send vs insert — the community default
- **Room belongs on a send/aux** when you want space + the ability to **process the wet
  only** (EQ, compression, saturation on the return) — the standard reason given:
  "producers put the reverb on a send to control the sound more — add EQ, compression,
  saturation — to get it sounding how they want." Mix = 100% on the send.
- **Insert at low Mix (~10–15%)** is the move for *placement/glue* — making one track sit
  in a believable room (Depth low, short Early Size). The draft already has this; the
  community frames it as "two different jobs, two different routings."
- **Multiple sends:** a classic vocal/instrument trick is **two sends — one short room +
  one longer ambient** — so the source reads as "in a space" (close room) *and* big
  (long wall) at once. Maps directly onto **a short Room (placement) send + a long
  Room/VintageVerb (wall) send**, both fed from the same banjo/baritone.

## Where saturation goes (two valid placements)
- **Saturate the RETURN (after Room):** Decapitator / RC-20 / SketchCassette on the wet
  output, **Lo Cut first** → the grit lives only in the tail = the saturated doom/shoegaze
  wall. (The draft's move.)
- **Saturate BEFORE the reverb:** standard vocal-chain order puts saturation/excitement
  *ahead* of the reverb send. On a drone source this means the reverb is fed an
  already-dirty signal, so the *space itself* inherits the harmonics rather than the tail
  being re-saturated. Subtler, more "baked-in." Worth trying both ways on a sustained
  banjo/baritone bed.

## Reverb ↔ delay order (the ambient-wall decision)
- **Delay → Reverb** = the "natural"/clean order: discrete repeats, then space around them.
  Keeps rhythm legible.
- **★ Reverb → Delay** = the **ambient/shoegaze wall** order: the big reverb washes the
  source out, then the delay **chops and re-throws that wash**, building "swelling,
  cinematic, synth-like walls of sound." It "destroys clarity and rhythmic punch" — which
  is exactly the point for drone/doom. This is the in-the-box version of the classic
  ambient-pedalboard "reverb before delay" trick, and it maps onto
  **Room (or Room→VVV) → EchoBoy** on a send.
- Either way the consensus: **"there are no hard rules — personal preference."** For this
  rig, reverb-into-delay is the default for walls; delay-into-reverb for legible ambience.

## Self-stacking inside the plugin
- Room has an **internal reverb-stack**: **Early Send feeds the Early engine into the Late
  engine** (0 = parallel, 1.0 = max). Big Early Size + Early Send 1.0 = a dense/blooming
  Late tail without adding a second plugin — "reverb into reverb" you don't have to route.

## Sound-design scale note
- Electronic producers report **up to ~28 instances of Room in a single project** for
  layered spatial sound design (low CPU makes this trivial) — i.e. Room is cheap enough to
  treat as a *per-element* placement tool, not just one shared bus. Relevant for a
  multi-layer drone arrangement where every part wants its own depth.
