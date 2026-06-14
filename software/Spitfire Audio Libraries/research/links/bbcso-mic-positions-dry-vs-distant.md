https://skippystudio.nl/2023/07/spitfire-bbc-symphony-orchestra-professional-microphone-positions/
skippystudio.nl + Spitfire product page + spitfireaudio.zendesk.com · accessed 2026-06-11 · descriptions via search-snippet triangulation (full pages truncated/closed)

# BBC SO mic positions — which to pull for DRY-to-degrade vs which give built-in space

The mic mixer is Core/Pro only (Discover = 1 fixed mix). For THIS rig the decision is:
**use the dry/close mics, then add your OWN space** (Valhalla/VintageVerb/EchoBoy) —
because the ambient/hall mics carry baked-in room that rings when re-reverbed (see
`bbcso-vicontrol-dry-reverb-workflow.md`).

## The 20 signals (11 positions + stereo mixes + 5 spill)
**DRY / CLOSE / INTIMATE — use THESE as the degrade source:**
- **Close** — tight, upfront, the driest spot mic.
- **Close Wide Pan** — close but spread across the stereo field.
- **Leader** — placed above the section leader; "a more intimate sound." Great for a
  small, human, dry-ish bed.
- **Mono** — the BBC's 1930s-style single mic; **vintage, narrow, lo-fi-leaning** — on
  aesthetic for the "recorded-wrong" sound BEFORE you even add Decapitator.
- **Decca Tree / Outriggers** — the classic neutral orchestral picture; moderate room.

**DISTANT / AMBIENT — generally AVOID as the reverb source (they ring), but usable as
a standalone "already-degraded space" if you DON'T add more reverb:**
- **Ambient** — "up in the gods," high at the back; most reverberant room sound.
- **Balcony** — two omnis at the very rear/high; "about as much ambience as you can get."
- **Sides** — omnis at the orchestra's edge; extreme width (Atmos/5.1).
- **Atmos front / Atmos rear** — immersive/height.
- **Mids** — mid-distance fill.

**SPILL (5)** — mics left open on *other* sections (strings bleeding into brass mics,
etc.). "A subtle but telling ambience… the sense of being in the room." → a free,
**dry-ish** room layer that does NOT ring like the hall mics — a good middle ground.

## Rig recipe
Ghost-under-banjo: **Close + Leader (+ a touch of spill or Mono for character)**, kill
Ambient/Balcony/Sides → CC1 low on Super Sul Tasto → Valhalla Room (short ER) →
VintageVerb (long degraded tail) → EchoBoy/Decapitator. For an instant "distant
unprocessed orchestra in a real hall," instead just push **Balcony/Ambient** alone and
add NO plugin reverb (avoids the metallic double-verb).
