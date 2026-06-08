https://www.elektronauts.com/t/octatrack-neighbor-tracks-series-or-parallel/134331
elektronauts.com · Octatrack subforum (see also "Why neighbor and not route-able?" /2225, "neighbour as post-fader fx" /28833, "FX chain order" /95783)

# Neighbor machines — multi-stage FX racks across tracks

A Neighbor machine listens to the **OUTPUT of the immediately preceding track**, letting you chain a track's 2 FX slots into the next track's 2 FX slots for **4+ effects in series** on one source.

## Track restriction
- **Neighbor CANNOT be assigned to track 1 or track 5.** (The OT's internal routing is grouped in fours — 1–4 and 5–8 — and the first track of each group has nothing "above" it to listen to.) So track 2 listens to 1, track 3 to 2, track 4 to 3; and track 6 to 5, 7 to 6, 8 to 7.
- Practical rack: put your source (Flex/Thru) on track 1, Neighbors on 2→3→4. That's the source + up to 3 extra FX stages = a 8-effect serial chain (2 FX per track × 4 tracks).

## Series vs parallel — the routing rule that bites people
- **Both source and neighbor routed to MAIN outs → they work in SERIES** (signal flows source → neighbor chain). This is the normal/intended behavior.
- **Both routed to CUE outs → they work in PARALLEL** (you'll hear the source AND the neighbor summed → phasing/doubling).
- Gotcha: if you route ALL tracks in a neighbor chain to cue (instead of just the final track) you create unintended parallel mixing and phasing. Route the intermediate stages to MAIN and only the final stage where you want it; or deliberately use cue routing for parallel/wet-dry FX.

## Cue / volume behavior
- The CUE system can monitor source tracks **independently of mutes and the neighbor chain** — useful for auditioning "pre and post neighbor" via the independent CUE LVL controls without affecting the main output chain.

## Why it exists (the "why not just routable?" answer)
- The OT has no free patch matrix; Neighbor IS the routing mechanism. It costs you whole tracks to build a deep FX rack — that's the tradeoff (2 FX slots/track is the hard limit, Neighbor chaining is the only workaround for more).

## Rig note
For processing the pedalboard wall: Thru on track 1 → Neighbor on 2 → Neighbor on 3 stacks Lo-Fi → filter → freeze-delay → reverb across the chain, all routed to main, all morphable by scenes.
