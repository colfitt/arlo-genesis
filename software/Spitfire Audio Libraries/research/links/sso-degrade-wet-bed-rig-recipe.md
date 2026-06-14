https://www.musicradar.com/how-to/lo-fi-processing-tps
MusicRadar · "9 ways to add lo-fi processing" + EPICOMPOSER tape-on-strings · accessed 2026-06-12
(also: https://epicomposer.com/adding-analog-warmth-sampled-strings-tape-simulation/)

# Degrading a PRE-REVERBED (wet) orchestral source — the SSO rig recipe

The hard part of SSO vs BBC SO: you're degrading something that **already has a big hall on it**.
You can't dry it first (close mic is still roomy — see `sso-apg-relaunch-close-mic-room.md`), and
the forum rule is **don't stack a second hall on the front** ("feather reverb, don't paint over"
— see `sso-vicontrol-reverb-for-spitfire-orchestra.md`). So the chain is *recolour and degrade
the existing space*, not *add a new one*.

**General lo-fi-on-orchestra technique (grounded):**
- **Tape saturation's mid-dip** is "more organic and musical" on orchestral material than
  hacking mids with EQ; low tape speed adds grit + rolls highs.
- **Roll off the highs** (LPF / tilt) → instantly less "refined," more degraded.
- **Compression for 'messiness'/pump** — forceful GR turns clean into "vibe and dirt."
- The article names **RC-20** specifically (owner owns it) as the all-in-one for noise / wobble
  & flutter / saturation / bitcrush / volume drops layered together.

**The SSO degrade chain (adapted to the wet bed — owner's plugins):**
1. **Source:** SSO Super Sul Tasto / Flautando / Harmonics / CS-Blend long, OR a Curated
   Ensembles sustain. Play soft (auto-swell), long release. **Pick ONE mic** — Tree or
   Outriggers for the lush wall, Close only if you want a touch more focus (still roomy).
2. **Bounce the held chord to audio** first (frees the 368 GB streaming/RAM; gives you a
   stable file to abuse). Optionally **PaulStretch 8–20×** → an endlessly-looping evolving wall.
3. **Degrade — DON'T pre-reverb:** the Lyndhurst hall is already your space. Go straight to
   **EchoBoy / Decapitator** (tape wow-flutter, saturation, mid-dip, drive) and/or **RC-20**
   (wobble + noise + bitcrush). Roll off the highs; let saturation eat the polish.
4. **Recolour the space, sparingly:** if you want a DIFFERENT/smeared room, the move is to
   degrade the wet bed and then **a touch of Valhalla** as a *feather* tail or a totally
   different character (e.g. Supermassive for a smeared cloud) — NOT a realistic second hall on
   top of Lyndhurst (= mush). Smaller is safer here than with the dry BBC SO chain.
5. **Bus parallel:** keep one clean (just-the-hall) layer under the degraded one for body.

**Why this differs from the BBC SO chain:** BBC SO is dry → you BUILD the space (Valhalla Room
→ VintageVerb → tape). SSO already HAS the space → you BREAK/recolour it (tape/sat/RC-20 first;
reverb only as a feather or a deliberately wrong second colour). SSO is the move when you want
the gorgeous real hall *in* the degraded result; BBC SO when you want to invent the space.
