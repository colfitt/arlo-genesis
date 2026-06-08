https://www.thegearpage.net/board/index.php?threads/chase-bliss-onward-pedal.2559936/
Forum-landscape map + firmware status · accessed 2026-06-03

# Where the Onward community actually lives (+ firmware status + access flags)

A map of the high-signal community sources for the Onward, with honest access notes — useful so a human knows where to dig and what I could/couldn't reach.

## Forum landscape (annotated)
- **TheGearPage — "CHASE BLISS ONWARD PEDAL" megathread** (`threads/chase-bliss-onward-pedal.2559936/`, 20+ pages) — the largest dedicated thread. **PAYWALLED** (Tollbit redirect → HTTP 402 to non-browser clients). Highest-value target for a human with a login. See `tgp-onward-megathread.md`.
- **Reddit r/chasebliss + r/guitarpedals** — almost certainly the densest tip pool, but **NOT ACCESSIBLE to this research agent**: reddit.com is blocked to the crawler (WebSearch refuses the domain) and direct fetch hits the login/JSON wall. *This is a real coverage gap in this facet — flag for manual follow-up.* Suggested manual searches: r/chasebliss "Onward sensitivity", "Onward dip", "Onward Microcosm".
- **Morningstar Engineering forum** — Onward + ML10X integration gotcha (captured in `morningstar-onward-ml10x-gotcha.md`). Good for MIDI-loop-switcher users.
- **Facebook "Chase Bliss" group** (`groups/1203044129709305`) — has an Onward troubleshooting post; auth-walled, not capturable here.
- **KVR / TheFretboard** — glitch-pedal comparison threads (mostly pre-Onward MOOD-vs-Microcosm; context only).
- **Reviews with real usage detail:** guitar.com (best), delaydude.de, pedal-of-the-day, gearnews — all captured.
- **Video, owner-perspective:** Aaron Rusch "Why Buy This?" (captured to transcripts) is the best long-term-owner workflow source.

## Firmware status (honest)
- The Onward is **user-updatable** via the web Bliss Programmer (`firmware.chasebliss.com`) + the open-source CBA Firmware Interface Program (github.com/chasebliss/cba-firmware-interface-program).
- **No public Onward firmware changelog / version history could be found.** The Bliss Programmer page is JS-rendered with no visible Onward version list; the GitHub repo is a generic DFU flasher with **no releases/tags** and no per-pedal version notes. Unlike the Blooper (which has a dedicated `blip.chasebliss.com` "v3.2" update page), the Onward has no equivalent public update page as of 2026-06.
- **Practical takeaway:** check the Bliss Programmer in a browser before deploying for any newer build, but there's no documented old-vs-new behavior split to worry about — no "firmware lore" exists yet for this pedal (it's only ~2 years old and niche).

## Net assessment of this facet's coverage
Community coverage for the Onward is **genuinely thin** vs older CB pedals — it's a new, polarizing, niche box. The strongest signal came from reviews + one long-term-owner video, not from forum megathreads (which are either paywalled (TGP) or uncrawlable (Reddit)). Tips below are well-supported; firmware lore is effectively nonexistent; the Reddit gap is the main thing a human should close manually.
