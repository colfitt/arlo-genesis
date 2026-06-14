Mono/stereo behavior, CPU, and gotchas — VintageVerb
Compiled from: KVR/Gearspace/MOD WIGGLER search snippets + PluginDrop review (2026-04-24,
https://plugindrop.net/posts/valhalla-vintageverb-review/) + Cycling '74 review (Darwin Grosse,
2016-09-06, https://cycling74.com/articles/review-valhalla-vintageverb). Gearspace "No Mono"
thread (https://gearspace.com/board/.../1329902-valhalla-vintage-verb-no-mono.html) was 403 to
fetch but its key points surfaced in search.

## Mono / stereo (the real gotcha)
- **Sanctuary = mono-in / stereo-out.** All OTHER modes are stereo-in / stereo-out.
- Because each mode is modeled on different vintage hardware, mono-summing is inconsistent
  across modes: some sound fine with one channel used as mono, others need both channels summed.
  Reworking it would break backwards compatibility, so it's left as-is.
- Practical upshot for the rig: if collapsing to mono matters (or you're feeding a mono pedal
  chain), CHECK mono compatibility per mode — heavy modulation/wide modes can partially cancel.
  **Ambience mode in NOW** is a reliable way to add a stereo field to a mono source.

## CPU
- Very efficient on Apple Silicon (the user's Mac): PluginDrop ran **32 instances under ~30% load**
  on mid hardware; Apple Silicon native builds are "noticeably lower" CPU than Intel. Cycling '74's
  Grosse put it "in every patch and Live project." → You can run several instances (Tycho-style
  inserts, reverb-into-reverb) without sweating CPU. Long 70 s decays cost more than short ones.

## The two big "missing feature" gotchas
1. **No Freeze / no infinite button.** Unlike Big Sky / Microcosm / Supermassive, VintageVerb has
   NO freeze. Max **Decay = 70 s** is the ceiling. To FAKE infinite: set Decay near 70 s + big
   Size for a near-eternal tail, or automate Mix/Decay, or (best) use the hardware Big Sky's
   freeze / Supermassive's huge feedback when you need a true held drone.
2. **No post-reverb EQ on the tail.** The internal EQ/Damping shapes the wet, but for surgical
   tail-shaping you must **chain a separate EQ AFTER** VintageVerb (e.g. Logic Channel EQ on the
   return). Important for keeping low drones out of mud.

## Other gotchas
- 1970s/Dirty modes deliberately add artifacts (downsampling, quantization, 10 kHz ceiling) —
  that's the character, but it's NOT a clean reverb; don't reach for it when you need transparency.
- Mud: long decay + no LowCut = boom. Always LowCut the wet and predelay to keep pitch readable.
- The "reverb cliché" trap: ambient over-reliance on big verb "glosses over poor playing" (KVR).
  Signal over volume — carve with EQ/damping/predelay, don't just drown it.
