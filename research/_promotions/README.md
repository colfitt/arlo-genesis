# Staged promotions

Files in this directory are **staged findings** from bloop research passes, held here
until they can be **manually appended** into v2's suggestion index (`v2/.../chunks.jsonl`)
from the main tree.

The `v2/` app is **not present in this worktree**, so promotion cannot happen here.
When working in the main tree:

1. Review each `*-index-chunks.jsonl` file below.
2. Append its lines into v2's `chunks.jsonl`.
3. Re-run the index build / refresh as usual.
4. Remove the staged file once it has been promoted (or leave it as an audit trail).

Each `.jsonl` line is a single chunk object with fields:
`{"text", "device", "content_type", "source"}` — matching the v2 chunk schema.

## Contents

- `2026-06-19-big-time-index-chunks.jsonl` — 15 gear-fact chunks for **Chase Bliss Big Time**,
  extracted from the bloop digest `research/bloops/2026-06-19-chase-bliss-big-time.md`
  ("Candidate index chunks" section).
- `2026-06-19-big-time-l2-index-chunks.jsonl` — 14 gear-fact chunks for **Chase Bliss Big Time**,
  extracted from the layer-2 digest `research/bloops/2026-06-19-chase-bliss-big-time-l2.md`
  ("Candidate index chunks" section).
