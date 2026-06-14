https://vi-control.net/community/threads/yt-tutorial-how-to-properly-loop-drones-and-pads-in-kontakt.75146/
VI-CONTROL forum thread · "how to properly loop drones and pads in Kontakt?" · composer community (Pianobook/VI-C crowd)

# Looping drones & pads seamlessly in Kontakt — the two main recipes

The single most rig-relevant technique (sustained walls, evolving pads). Two
schools, both used by working sample-library devs:

## Recipe A — "record 4× a cycle, grab the middle two bars" (destructive, in the DAW)
The cleanest seamless loop, done **before** Kontakt:
1. Record the sustained source (pedalboard tail, synth pad, bowed note) at least
   **4× longer than one intended loop cycle**.
2. **Grab the middle two bars** of that recording. The point: the *beginning* of
   your selection already contains the ring-out content from the end of a cycle,
   and the *end* of your selection contains the fade-into-the-beginning content —
   so the join naturally matches.
3. Add a **teeny-tiny fade in and fade out** on the selection.
4. **Test** it by pasting the clip after itself and listening at the join for
   pops/weirdness; nudge until clean.
5. In Kontakt, set the loop **start-to-finish with NO crossfade** (the match is
   already baked in).

## Recipe B — "offset + heavy crossfade" (in Kontakt's loop editor, the fast way)
For polyphonic pads where a tiny imperfection won't be heard:
- In the Wave Editor loop editor, **offset the beginning and end** of the loop
  region and **add a lot of crossfade**.
- This often produces a **slight volume dip at the crossfade**. Workaround: for
  **polyphonic** instruments it's inaudible *as long as you add variation to the
  loop length* (so multiple held notes don't dip in unison) — i.e. give each
  zone a slightly different loop length so the dips don't line up.

## Practical settings cross-ref (from 344 Audio's pad example)
A concrete starting point for a pad/sustained sound in Kontakt's Wave Editor:
loop region roughly **0.25 s → 0.75 s** into the sample with a **fairly short
crossfade of ~500 samples** — then stretch the loop region wider for more
internal variation. (NI FIRST STEPS Ch.2 Ep.4 instead reaches for a *large*
crossfade — ~**50,000 samples** ≈ ~1 s at 48 kHz — when looping a longer,
slowly-evolving pad. The right number scales with how long/evolving the loop is.)

## Key cross-cutting warnings (community consensus)
- **Zero-crossing snapping is not enough** — "don't trust it, trust your ears."
  Kontakt's snap-to-zero-crossing helps but won't guarantee a click-free loop on
  complex material.
- **Longer loops sound more natural** than short ones — a short loop of a complex
  source (violin, choir) machine-guns the ear; a long loop the ear can't
  "remember" reads as continuous.
- For **plucked/decaying** acoustic sources, looping kills the character — only
  loop genuinely **sustained** content (synth pads, bowed notes, drones, held
  pedalboard tails). Decaying sources should use the natural tail instead.

## Rig relevance
This is THE technique for turning a **sustained Chase Bliss / Big Sky / Microcosm
pedalboard wall**, a **VG-800 pad**, or an **OP-1 drone** into an infinitely
playable Kontakt drone instrument: print the long sustained tail, use Recipe A in
Logic, map one zone per few semitones, give each zone a slightly different loop
length (Recipe B variation trick) so a held chord evolves instead of dipping in
lockstep.

> Source: VI-CONTROL thread + 344 Audio "Complete Guide Part 3" loop values +
> NI FIRST STEPS Ch.2 Ep.4 (captured transcript). Distilled, not raw HTML.
