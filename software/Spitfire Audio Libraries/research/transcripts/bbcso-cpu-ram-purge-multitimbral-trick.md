https://www.youtube.com/watch?v=Rax8IDPiGVw
Stephen O'Connell - Cmd Shift New · If You Own Spitfire Audio's BBC Orchestra, You Are Going To Want To Know This Trick! · 2022-11-21 (14:56)

[The definitive CPU/RAM/disk-optimization video for BBC SO. Three tricks: (1) "Optimize" in the Spitfire app, (2) purging unused articulations to slash RAM, (3) one-instance multitimbral routing in Logic to put each articulation on its own track without loading multiple plugin instances. Directly answers the "BBC SO is CPU-hungry" problem on a laptop/AU rig. Pro version cited (~660 GB).]

## Trick 1 — "Optimize" (the boring-but-necessary disk step)

In the **Spitfire Audio app**, open BBC Symphony Orchestra → each product → the **cog** → **Optimize**. What it does: renames/reorganizes file metadata and "moves the metadata to the head of the file," so content is found and read much faster off disk. With thousands of samples per Pro library, every load has to scan them all; optimizing speeds up load times — significant when a session has ~20 plugin instances open. You must do it per product (no "already optimized" checkbox, so track which you've done); takes a while but worthwhile.

## Trick 2 — Purge unused articulations (RAM)

Loading a default patch (e.g. Violins 1) loads **every articulation + all its samples** — in Pro that's a lot. Example: Violins 1 alone = ~873 MB of RAM at default. If you only need, say, Longs + Staccato, the rest is wasted RAM/CPU.
- Open the **techniques editor** (the little button by the articulation list) and **remove** the articulations you don't want. They can be re-added anytime. Three pages of articulations dropped to two; RAM "so much better."
- **Save your own preset** (Save icon at top of the app) with just those articulations so you can recall the trimmed version. (For this rig: a "ghost-strings" preset = just Long + Sul Tasto + Flautando + Harmonics + Con Sordino, everything else purged = a tiny, fast patch.)

## Trick 3 — One-instance multitimbral in Logic (the big one)

The problem with the usual fixes: key-switching is fiddly to program and dumps weird low ledger-line notes into the score; loading a separate plugin instance per articulation eats RAM fast (five instances ≈ five GB). The happy medium = **Logic's multitimbral parts on a single BBC SO instance**:

1. New Software Instrument track → load BBC Symphony Orchestra → choose **Multitimbral parts** (he picks 4; can go up to 16. Hot tip: create all 16 up front — you can delete extras later but **can't add more** after).
2. This makes N tracks all named the same instrument but on **MIDI channels 1, 2, 3, 4…**. In the mixer it's still **one track / one plugin instance**.
3. In BBC SO's **Trigger** section, change the trigger from key-switch to **MIDI Channel**, then assign each articulation to a channel: e.g. Legato→ch1, Long→ch2, Spiccato→ch3, Pizzicato→ch4.
4. Now each articulation plays from its own track, but all mic channels / instrument settings / expression are controlled in **one** instance = far less CPU/RAM than multiple instances, and no key-switching.

He saves these as user patches (e.g. a "BBC Orchestra > Violins" multitimbral summing track) for instant recall.

## Key-switch octave gotcha

In his default Logic setup the BBC SO key switches read an octave off — selecting "C-1" actually triggers what's labelled "C-2" (the C1–C8 vs C0–C7 / zero-counting mismatch). Worth knowing if you program key switches in Logic's piano roll.
