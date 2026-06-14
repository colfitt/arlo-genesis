https://vi-control.net/community/threads/reverb-for-spitfire-based-orchestra.68342/
vi-control.net (forum thread) + kvraudio.com/forum/viewtopic.php?t=596658 · accessed 2026-06-11 · 403 to fetcher → triangulated from search snippets + KVR fetch

# VI-Control / KVR — the dry-mics-then-add-your-own-space workflow

VI-Control 403s automated fetch; content below is from search-result snippets of the
"Reverb for Spitfire-based orchestra" thread + a full fetch of the KVR "Orchestral
Reverb" thread. LABEL: triangulated, not full-thread reads.

## The core community consensus (directly relevant to the degrade angle)
- **Valhalla Room is "typically fine if working with bone-dry samples, or if just
  using the late reflections (tails)."** The caveat the forum repeats: **"trying to use
  something with any baked-in room information just generates too much metallic
  ringing."** → i.e. **feed Valhalla the DRY/CLOSE mics, not the ambient/hall mics.**
  This is the technical reason the dry Maida Vale source is the right one to degrade:
  reverb-on-reverb rings.
- The "purist" counter-view (also useful): "you'll probably not get as good [realistic]
  results putting Spitfire material through a lot of plugin reverb as by simply mixing
  the wide selection of mics within the library." → For *realism* mix the mics; **for
  YOUR degraded space, kill the mics and use the plugin.** Both camps agree: the choice
  is mic-blend OR external reverb, not both stacked.
- **Two-stage spatialisation** (noiseboyuk, KVR): "Spatialising comes in two parts.
  First the **early reflections**, second the **tail**." Practical recipe for a dry lib:
  a short **ER** (~0.5 s) to place it in a small space, then a **longer tail** from a
  second reverb. Maps cleanly onto Valhalla Room (ER/short) → into a long VintageVerb
  or Supermassive tail.
- Reverb picks named for orchestral/dry libs: **Valhalla Room** (for dry/tails),
  **Seventh Heaven** (IR, "set-and-forget" — but one user: "not realistic, quite
  effected sounding" — which for the doom/lo-fi aesthetic is a *feature*),
  LiquidSonics Cinematic Rooms, Berlin Studio, Acon Verberate.

## Translation to the owner's chain
Owner already runs **Valhalla Room + VintageVerb**. The forum's "dry samples → Valhalla
tails, no baked room" rule is exactly the BBC SO recipe: load the **Close/dry mics
only** (or the single Discover mix), CC1 way down, and let **Valhalla Room do the small
ER, VintageVerb do the long degraded tail**. Then EchoBoy/Decapitator for the
"recorded-wrong" colour. The metallic-ringing warning is the reason NOT to also raise
the Ambient/Tree/Balcony mics first.
