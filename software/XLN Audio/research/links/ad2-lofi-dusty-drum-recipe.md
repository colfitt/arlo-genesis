https://lofiweekly.com/2026/05/18/addictive-drums-2-presets-for-dusty-hip-hop-how-to-get-warm-knocky-drums-fast/
lofiweekly.com "AD2 Presets for Dusty Hip Hop" (2026) + reaper.blog/2018/11/lofi_ad2 (Jon, 2018-11-16, "Trashy & Lo-Fi Drums in AD2" — VIDEO, technique noted) · accessed 2026-06-11

# Lo-fi / dusty / "old sampler" drum recipe in AD2 (written-source values)

## The problem (LoFi Weekly framing)
- Stock AD2 is "**too clean**," highs too crisp, low end gets lost when you try to
  dirty it. Goal = make it **feel sampled** / dusty-old-sampler, low end intact,
  highs controlled for grit, saturation to glue.

## Concrete starting values (LoFi Weekly, dusty-hip-hop)
- **Cymbals / top end:** **low-pass ~12-14 kHz** to tame modern brightness (kills the
  "VST sparkle" — also the shoegaze move).
- **Drum-bus comp:** **slow attack 15-30 ms, release 80-150 ms, 1-3 dB GR** — glue,
  don't crush.
- **Ambience/reverb:** **decay < 1 s, pre-delay 0-20 ms, low-cut < 200 Hz** — short
  and dark, not a big wash.
- **Tone targets:** kick weight **50-90 Hz**; snare punch **180-250 Hz**.
- **Saturation:** **parallel** for subtle harmonics, "not harsh distortion."

## In-AD2 lo-fi chain (the REAPER Blog "trashy drums" method, in-plugin)
Jon's approach (do it all on AD2's own channels/Bus before going external):
1. **Per-channel Tape Saturation + Distortion** on snare/kick for grit.
2. **Transient Shaper** to claw back attack lost to saturation (knock).
3. **Bus channel** = send a submix, **distort the Bus hard**, blend back into Master
   for parallel destruction.
4. Use **Snapshots** to A/B clean vs trashed and to build the degrade in revertible
   stages.
   (Note: the REAPER Blog source is a video — the OTHER agent owns video detail; this
   captures only the documented workflow shape.)

## Rig version (degrade DOWNSTREAM — preferred for this setup)
Keep AD2 fairly clean as the source, then on the DAW track:
1. **RC-20 Retro Color** — Magnetic (tape wear) + small Distort + Digital rate-crush
   for the "old sampler" stamp; automate Magnitude up into a section.
2. **SketchCassette II** — wow/flutter for believable cassette pitch wobble (don't
   ALSO use RC-20 Wobble on the same layer — one wow/flutter source per layer).
3. **Soundtoys Decapitator** — low-medium drive for analog harmonics/body.
4. **Goodhertz Lossy** — codec crush last for the digital-degraded edge.
5. **DS-10 Drum Shaper** FIRST in the chain (or just after AD2) to set transient
   punch BEFORE you smear it with tape/codec.
- **Multi-out so you can degrade individual drums**: e.g. crush only the room/OH with
  Lossy + SketchCassette, keep the kick clean and punchy underneath.
