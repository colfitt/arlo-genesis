https://www.kvraudio.com/forum/viewtopic.php?t=377834 + https://www.kvraudio.com/forum/viewtopic.php?t=430977 + general Valhalla forum reports
KVR Valhalla DSP Forum — "Valhallas stereo image — do I lose much in mono?" + "Valhalla Room Bug v1.1.1 AU in Studio One" + Costello replies · ~2013–2017

# ValhallaRoom — mono, AU, and CPU gotchas (community-reported)

Practical traps, several straight from Sean Costello's own forum replies. The AU one
matters for **this rig specifically — Logic Pro is an AU-only host.**

## Mono compatibility (Costello's own guidance)
- Room is **true stereo, mono-in → duplicated → stereo-out.** "Most of the algorithms
  should work well being mixed to mono," **but "a few of the reverb modes may have strange
  artifacts"** — if a collapsed mix sounds metallic/hollow, **switch modes.**
- **Sum L+R to mono — do NOT just take one channel:** "You'll lose a lot of echo density
  if you use just the left or right channel." (Some modes build density across the stereo
  field.)
- **Phase-cancellation fix:** if summing to mono thins/cancels the tail, **micro-delay one
  output channel by ~12 ms before summing** — Room (like many reverbs) uses phase
  inversions for stereo width, and that 12 ms shift de-correlates them. Costello's caveat:
  "if there aren't phasing issues, this might *introduce* some" — so only reach for it when
  you actually hear cancellation.
- Lighter alternative some users prefer: **reduce stereo width to ~30–50%** instead of full
  mono for better control while keeping the reverb's quality. (Relevant before feeding a
  Room tail into a mono pedal/chain or a mono Octatrack input.)

## ★ AU pan-vs-depth bug (Logic / AU hosts — flag for this rig)
- Reported on the **AU build**: send a **mono** track to an FX bus running ValhallaRoom and
  **panning scales the reverb** — at **100% R the signal goes ~dry, 100% L it's full wet** —
  "almost as if panning is scaling Depth." The **VST version is unaffected.**
- This is the AU mono-in/stereo-out handling biting. **Workaround: use a STEREO track / send
  to the Room bus, not a mono one.** For a Logic AU rig, make the reverb send/aux **stereo**
  and the feeding track stereo (or hard-center a mono source on a stereo track) to avoid the
  pan-eats-the-reverb surprise. (Same family of issue bites Studio One: "Valhalla plugins
  are mono/stereo-in, stereo-out and Studio One is picky with mono-in/stereo-out — use
  stereo tracks.")

## CPU
- A **non-issue** — Room is famously light (the "28 instances in one track" reports). On
  Apple Silicon you can multi-instance freely; no need to bus everything to one Room for
  CPU reasons (do it for cohesion, not load).

## Quick checklist for the rig
1. Feeding a mono pedal/Octatrack input from a Room tail → **sum L+R**, don't pick a side;
   add ~12 ms micro-delay only if it cancels.
2. Logic AU send → **make the aux and the source track stereo** (avoids the pan-vs-Depth
   bug).
3. Collapsed mix sounds metallic → **change mode**, don't fight it.
