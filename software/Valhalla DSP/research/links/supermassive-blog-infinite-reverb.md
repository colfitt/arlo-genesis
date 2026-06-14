https://valhalladsp.com/2021/05/19/tips-and-tricks-infinite-supermassive/
valhalladsp.com · Sean Costello · 2021-05-19

# Tips and Tricks: Infinite Supermassive (authoritative)

The official "how to make it drone forever" post. THE infinite-drone recipe.

## The infinite-reverb recipe
- **MODE** — use one of the *reverb-leaning* algorithms: **Gemini, Hydra, Great
  Annihilator, Lyra, or Capricorn.** (These sustain cleanly at max feedback.)
- **FEEDBACK = 100% (1.0)** — the essential requirement. At 0 dB feedback gain the
  reverb theoretically sustains **indefinitely** → a true infinite/freeze.
- **WARP = non-zero** — so you don't get an obvious repeating echo loop; smears the
  infinite tail into reverb.
- **DENSITY = non-zero** — smooths the held sound into a reverb texture (vs discrete).
- **MOD DEPTH = 0%** — *"This helps preserve the pitch of the freeze reverb"* (mod on a
  held infinite tail detunes/beats audibly).
- **MIX = 0.5** in the worked preset example (set 100% on a send).

## Why it works (the key design fact)
*"It uses modulation with no filtering, and most of the algorithms have their low cut
and high cut filters OUTSIDE the feedback path."* → the held tail does **not** lose
highs over time the way most reverbs do. The infinite drone stays full and bright.

## Motion & layering
The infinite reverbs generate their own internal "motion"/beat patterns from the
algorithm + delay settings. You can layer **additional modulation (e.g. a phaser)
AFTER** Supermassive for more movement without disrupting the infinite decay (keep the
internal Mod Depth at 0 to hold pitch; add motion downstream).

## Caveat
Not every algorithm holds a clean infinite without degradation — stick to the five
listed modes for true infinite behaviour. (To "freeze" a moment: ride Feedback up to
100% once the tail you want is in, then stop playing — it holds.)
