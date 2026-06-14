# Jonny Greenwood's randomized stutter/glitch (Go To Sleep) + Feral Glitch pedal

URLs:
- https://www.musicradar.com/news/recreate-jonny-greenwoods-randomised-stutter-effect-with-new-feral-glitch-pedal
- https://reverb.com/item/19364501-the-feral-glitch-effect-pedal-randomizer-stutter-looper-delay-radiohead-max-msp
- (mechanics from) WebSearch summary of thekingofgear.com "Go To Sleep" Max/MSP coverage
MusicRadar · news desk · 2021 — plus King of Gear (Feral Glitch is by the KoG founder)

## Distilled

- Jonny's "randomised stutter Max/MSP patch" — **as heard on "Go To Sleep"** (also the family
  of glitch/stutter heard live on There There etc.) — is the most-documented Max/MSP use.
- **How it works (mechanics, from King of Gear):** the patch is always active once open; a
  **random generator runs**, and "when it hits a certain value the patch loops some audio for
  'x' amount of time." Whether you hear the glitch vs the dry signal is decided *randomly by
  the patch.*
- **Routing:** Jonny's laptop sits in an effects loop controlled by a **Boss LS-2** — the very
  FIRST pedal in his chain. He stomps the LS-2 to fold the patch in, then "plays a lot of
  notes to ensure the patch always has information to loop."
- **Feral Glitch pedal** (built by the King of Gear founder) recreates it: a left toggle picks
  **random vs fixed** stutter mode; a second toggle **kills or passes the dry signal**; two
  knobs set **effect time/length** (= max possible length in random mode) and **effect
  volume**; plus bypass + engage footswitches. (Kickstarter, ~$260.)

## Translation note
This is the **glitch/stutter** half of the art-rock lens, and it maps almost 1:1 onto the
**Blooper Scrambler (B5)** — jump points lock to a 16-slice grid; CW = repeating sequence,
CCW = **random** (= Jonny's random generator); "lowest random setting" = Skip Protection
(occasional disturbance). The "play a lot of notes so it has something to loop" approach is
exactly how you feed Blooper a dense source then let Scrambler chop it. DRY KILL dip = the
Feral's "kill dry" toggle. Honest: Blooper's randomness is per-toggle regen, not a free-running
generator, but the audible result is the same family.
