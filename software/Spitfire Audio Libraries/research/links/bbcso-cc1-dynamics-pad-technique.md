https://vi-control.net/community/threads/the-difference-between-dynamics-cc-1-and-expression-cc-11.58127/
vi-control.net (CC1 vs CC11 thread) + michaelmusco.com BBCSO Discover review + BBCSO manuals · accessed 2026-06-11 · CC mechanics triangulated from search snippets (VI-C 403s) + full fetch of Musco review

# CC1 dynamics crossfade — the actual ambient-pad mechanic in BBC SO

This is the single most important *technique* fact for making a ghost-bed out of BBC SO,
and it's mechanical, not opinion.

## How the long/sustain patches work
- Spitfire long patches map **CC1 (mod wheel) = "Dynamics"** → it **crossfades between
  separately-recorded dynamic LAYERS** (pp → ff). Each note is sampled at multiple
  volumes because "an instrument played softly has a very different TIMBRE than the same
  instrument played loudly." So CC1 down isn't just quieter — it's a **breathier, darker,
  less-bow-noise timbre.**
- **CC11 (Expression) = simple volume on top.** Different job: trim level without
  changing timbre.
- **Practical for the ghost layer:** ride **CC1 way down and KEEP it down** to lock the
  softest, most ghostly timbre, then use **CC11 to set how far back in the mix** the bed
  sits. This is how you get the "real orchestra playing as soft as possible" — it's the
  pp *sample layer*, not just a turned-down loud sample.
- **Evolving/alive bed trick:** slowly automate CC1 in a gentle wave (e.g. drift between
  ~15 and ~45) under a held cluster — the timbre breathes pp↔mp without the note
  re-attacking. Cheap, convincing "evolving orchestral pad" from a static chord. Pair
  with overlapping note lengths across sections so attacks never line up.

## Confirmed: Discover is genuinely usable as an ambient bed
Musco review (full fetch): Discover "excels at sustained, pad-like textures… strings
are smooth and cohesive… the entire orchestra blends naturally" with little processing.
Explicitly endorsed "as the orchestral layer beneath electronic textures" / for
"understated scoring and hybrid compositions" — i.e. the ghost-under-other-material job.
So even the free tier's plain **Long (vib)** sustain + CC1 ride does the core bed task;
you just don't get the breathy super-sul-tasto/flautando colours (Core/Pro).

## Honesty flag
CC1/CC11 mechanics are well-documented Spitfire behavior (multiple VI-C threads +
manuals); the specific "drift CC1 15–45 wave" is an *inferred* recipe applying that
documented crossfade to the drone use case, not a quoted forum post.
