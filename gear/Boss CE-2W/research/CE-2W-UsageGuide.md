# Boss CE-2W (Waza Craft) Chorus — Usage Guide

How people *actually* use the CE-2W, to complement the spec/reference dossier in `CE-2W-DeepResearch.md`. In this rig it does two jobs: a world-class all-analog chorus **and** the **mono→stereo split point of the whole signal path** (12th on Board 1, after the Somersault, before the Deco). The load-bearing facts: the "stereo" is a **wet/dry hard split** (not two L/R voices), and the **buffered bypass keeps both legs fed when the chorus is off** — which is *why* it's the right split point. Most of the time it lives in **Standard, subtle, "on for the split,"** while the Somersault upstream does the broken character.

> Captured this wave (Tier B, 2 agents): 5 video transcripts + 10 distilled links = 15 sources (see §8). No video mis-credits this wave (agents verified all channels via yt-dlp). Best find: **Frusciante used his CE-1 primarily as a signal *splitter* between two amps** (his own words) — the canonical CE player used it exactly the way this rig uses the CE-2W; added to the dossier §7.

---

## 1. Essential workflows

**The three modes:**
- **Standard ("S," left)** = the CE-2 voicing — subtle, clear, classic Boss chorus ("will not impair the crispness of your guitar"); a slight mid-boost. The everyday split setting.
- **CE-1 Chorus (middle)** = deeper, darker, "queasier," more spatial/dramatic — the Frusciante lush wash.
- **CE-1 Vibrato (right)** = true pitch-vibrato with the **dry removed** — i.e. it's inherently the "wet-only" sound (no patching trick needed); rotary-ish at noon.

**The stereo is a wet/dry HARD split, not L/R.** From **OUTPUT A alone** = chorus + dry mixed (normal mono chorus). Plug **OUTPUT B too** and it changes: **A = chorus (wet) only, B = direct (dry) only**. The width comes from one pure-wet + one pure-dry leg — "a very three-dimensional modulation," not two modulated channels ([sos-stereo-buffered-bypass](links/sos-stereo-buffered-bypass.md); [wet-dry-stereo-splitter-trick](links/wet-dry-stereo-splitter-trick.md)).

**Buffered bypass keeps both outputs fed when off** — so the downstream stereo chain never collapses to mono whether the chorus is engaged or not. This is *the* reason the CE-2W is the right split point (a true-bypass stereo pedal could drop a leg). It also presents a low 1 kΩ output to drive the long run into the Deco/Board 2.

**No MIX knob** — to get *less* effect, lower DEPTH (or use the split), not a blend control.

---

## 2. Signature settings

Clock positions where sources give them (Guitar Chalk uses a 0–10 scale — relative, not clock). Attributed below.

| Sound | Settings | Source |
|---|---|---|
| **Subtle stereo widener** (everyday "on for the split") | Standard · RATE ~9 ("a crawl") · DEPTH just shy of noon | quoted, [boss-studio-applications](links/boss-studio-applications.md); DEPTH in the lowest third = "subliminal in a mix" ([premier-guitar-review](links/premier-guitar-review.md)) |
| **CE-1 lush / two-amp wall** (the canonical stereo recipe) | **CE-1 Chorus · RATE ~10 · DEPTH ~2:00** · into two amps, hard-pan the wet/dry legs, leave a dry track up the middle | quoted, [boss-studio-applications](links/boss-studio-applications.md) |
| **Deep vibrato / rotary** | CE-1 Vibrato · mid RATE/DEPTH = "metallically tinged rotary"; low/low = "space-drunk, nitrous" | quoted, [premier-guitar-review](links/premier-guitar-review.md) |
| **Slow oceanic / ambient** | CE-1 Chorus · very slow RATE · deep DEPTH — built to sit under delay/reverb | [guitarchalk-settings](links/guitarchalk-settings.md) |
| **Vintage CE-2 match** | Standard · RATE ~11 · DEPTH 1–2 (dial DEPTH a hair higher than an original CE-2 to match) | [legendarytones-modes-vs-ce2](links/legendarytones-modes-vs-ce2.md) |
| **Baseline reference** | both RATE + DEPTH at noon, Standard = "rich, chiming, sparkling" | quoted, [sweetwater-mitch-don](transcripts/sweetwater-mitch-don.md) |

See dossier §13 for four rig-tuned starting points (subtle widener / CE-1 lush / deep vibrato / slow oceanic two-amp).

---

## 3. Power-user tips, tricks & hidden features

- **Frusciante's move = use it as the splitter** — the chorus is a bonus on top of the routing. In this rig that's literally the slot: OUTPUT A → Deco L (wet), OUTPUT B → Deco R (dry).
- **Dummy-plug trick:** in an otherwise-mono rig, plugging *anything* into OUTPUT B (a dead/George-L's plug, an 1/8"→1/4" adapter) activates the split and forces OUTPUT A to **100% wet** ([wet-dry-stereo-splitter-trick](links/wet-dry-stereo-splitter-trick.md)). *(In this rig both outputs are already used, so OUTPUT A is already pure-wet — but the trick is worth knowing for a wet-only patch.)*
- **CE-1 Vibrato is already "wet-only"** (dry removed) — no patching needed for the dramatic, dry-free pitch wobble.
- **Double-tracking trick:** record dry L + dry R takes, then a middle take with CE-1 Vibrato on → a thick 3-D studio layer.
- **It already bakes in the two most-requested classic-CE-2 mods** (variable depth + a vibrato mode) — but still no blend/mix mod.

---

## 4. The wet/dry split into the Deco (rig routing craft)

- **Wire OUTPUT A → Deco L, OUTPUT B → Deco R.** Because A is pure chorus and B is pure dry, the two legs into the Deco are **not a matched pair** — they diverge *before* the Deco's tape sim touches them, which the degraded/tape aesthetic exploits for free (the two channels evolve differently under the Deco's wobble/saturation).
- **If you want a more symmetrical image**, run the CE-2W in mono (OUTPUT A only — chorus+dry mixed) and let the Deco/downstream make width — but then you lose the split. Conscious trade-off.
- **The split survives bypass** — both legs stay fed (dry) when the chorus is off, so you can disengage the chorus without collapsing Board 2/3 to mono.
- **Order is correct:** chorus *before* the Deco's tape doubling/saturation — modulate first, then smear/saturate. Push the Deco's wobble and the chorus pitch-mod + tape wow compound into genuine seasick motion.

---

## 5. CE-1/CE-2 history & verified users (be precise)

- **Lineage:** Roland JC-120 (1975) → **CE-1 (1976** — the first chorus pedal *and* the first Boss product; MN3002 BBD; chorus + vibrato; stereo) → **CE-2 (1979** — compact, MN3007 BBD, mono, chorus-only) → **CE-2W (2016** — MIJ Waza, folds both in; adds stereo to the CE-2 mode + variable depth to the CE-1 modes) ([frusciante-ce1-history](links/frusciante-ce1-history.md); [legendarytones-modes-vs-ce2](links/legendarytones-modes-vs-ce2.md)).
- **VERIFIED users:** **John Frusciante (RHCP) = CE-1** (~1990–2010, again 2022) — and notably used it as a **signal splitter** between two amps (his own words); **James Honeyman-Scott (Pretenders) = CE-2**; David Gilmour, Johnny Marr, Robert Fripp, Rory Gallagher, John Mayer, Keith Urban named as CE-2 users (cite as users, not specific tracks).
- **Myth corrections (verified, keep honest):** **Andy Summers "Walking on the Moon" was NOT a Boss CE** — it was an **EHX Electric Mistress** flanger (and/or an AMS/SCAMP rack on the record); Summers himself muddies it ("Who calls it a flanger? I would have called it a chorus"). And **Kurt Cobain's *Nevermind* chorus was an EHX Small Clone**, not a CE-1/CE-2 ([chorus-misattributions](links/chorus-misattributions.md)).

---

## 6. Rig-specific recipes (banjo/baritone drone)

Slot: `… Somersault → CE-2W (stereo split) → Deco V2 → (stereo to Board 2)`.

- **Default "on for the split":** Standard, RATE ~9–10, DEPTH just shy of noon — quiet, classic, three-dimensional; the baseline Board-1 stereo state. The Somersault is the one you stomp for character.
- **Baritone (home turf):** Standard adds shimmer without thinning the low end (the gentle BBD top-roll flatters the baritone's darker voice); keep DEPTH modest so the lows don't pitch-warble.
- **CE-1 lush on sustained chords:** CE-1 Chorus, RATE ~10, DEPTH 1–2:00 — darker/thicker into the Deco for drone passages.
- **Deep vibrato (drone/psych only):** CE-1 Vibrato, RATE 11–1, DEPTH 1–2 — too dramatic for rhythm; pairs with sustained VG-800 pads or Hizumitas walls upstream.
- **VG-800 pad patches:** CE-1 Chorus or Vibrato turns a static modeled pad into a moving 3-D drone — exactly the wall-of-sound aesthetic.
- **Bass:** the wet/dry split is *better* for bass than a fully-wet chorus — OUTPUT B keeps a dry low-end anchor while A carries the modulation; keep DEPTH low to protect the fundamental.
- **Don't double-stack wet:** pick a lane — Somersault for broken wobble *or* CE-2W's CE-1 Vibrato for the dramatic modulation; both wet at depth = mush. Most of the time CE-2W = Standard (subtle) for the split.

---

## 7. Best learning resources

- **Sweetwater (Mitch Gallagher & Don Carr)** — [the best official-grade full mode walkthrough](transcripts/sweetwater-mitch-don.md) + vs original CE-2; the "both at noon" baseline.
- **Leon Todd** — [CE-1-vs-CE-2W reamp](transcripts/leon-todd-ce1-vs-ce2w.md): audibly confirms the wet/dry split + CE-1-mode accuracy.
- **TheSuperFunAwesomeHappyTimePedalShow** — [old CE-2 vs CE-2W shootout](transcripts/ce2-vs-ce2w-superfun.md) (waveform/mode notes). **Pedal Science** — [the dummy-jack 100%-wet trick](transcripts/pedal-science-secret-mode.md) *(no captions)*. **David VDH** — [CE-1 Frusciante stereo target](transcripts/david-vdh-frusciante-stereo.md) *(no captions)*.
- **Text:** [Boss "A Chorus of Tones" two-amp studio technique](links/boss-studio-applications.md), [Sound on Sound](links/sos-stereo-buffered-bypass.md) (the authoritative wet/dry + buffered-bypass routing), [Premier Guitar](links/premier-guitar-review.md) (mode-by-mode), [Legendary Tones](links/legendarytones-modes-vs-ce2.md) (vs vintage CE-2).

---

## 8. Common pitfalls / gotchas

- **Wet/dry, not L/R stereo** — people expect two modulated channels; it's one wet, one dry. Patch accordingly.
- **No MIX knob, no MIDI/tap/expression** — set-and-forget; rate changes are manual only.
- **INPUT jack doubles as the power switch** — a dead-signal head-scratcher if the input cable isn't fully seated.
- **Buffered bypass** (always colors slightly, always needs power) — desirable here (it keeps both legs alive), but there's no true-bypass option.
- **Vintage-vs-reissue:** a minority of owners find the original CE-2 has "thicker swirl / more midrange" and the CE-2W a touch brighter on top — A/B reviews call the match near-perfect; dial DEPTH a hair higher to match an original.
- **CE-2W-specific internal mods/trimmers are undocumented** — the mod ecosystem is for the classic CE-2/clones (flagged, not invented).

---

## 9. Captured sources

**Transcripts** (`research/transcripts/`):
- `sweetwater-mitch-don.md` — Sweetwater — official-grade full mode walkthrough + vs original CE-2; "both at noon" baseline.
- `leon-todd-ce1-vs-ce2w.md` — Leon Todd — CE-1-vs-CE-2W reamp; confirms the wet/dry split + CE-1 accuracy.
- `ce2-vs-ce2w-superfun.md` — TheSuperFunAwesomeHappyTimePedalShow — old CE-2 vs CE-2W shootout; waveform/mode notes.
- `pedal-science-secret-mode.md` — Pedal Science — the dummy-jack 100%-wet trick *(no captions)*.
- `david-vdh-frusciante-stereo.md` — David VDH — CE-1 Frusciante stereo target tone *(no captions)*.

**Links** (`research/links/`):
- `boss-studio-applications.md` — Boss (Fletcher Stewart) — the two-amp technique + quoted RATE/DEPTH.
- `sos-stereo-buffered-bypass.md` — Sound on Sound — authoritative wet/dry split + buffered-bypass-feeds-both-outs.
- `premier-guitar-review.md` — Premier Guitar — DEPTH-thirds map + rotary/vibrato descriptions.
- `legendarytones-modes-vs-ce2.md` — Legendary Tones — A/B vs vintage CE-2, concrete dials, mode-by-mode.
- `guitarchalk-settings.md` — Guitar Chalk — five mode-paired named presets (0–10 scale).
- `wet-dry-stereo-splitter-trick.md` — theFretBoard — dummy-plug trick + CE-1 Vibrato = wet-only.
- `power-user-tips-settings-quirks.md` — Gigs & Guitars — mode layout, sweet spots, no-mix limitation, double-tracking.
- `ce2-mod-community-context.md` — PedalPCB/ElectroSmash — CE-2 mod ecosystem; CE-2W already includes depth+vibrato mods.
- `frusciante-ce1-history.md` — Ground Guitar — Frusciante = CE-1 used as a splitter; CE-1 lineage.
- `chorus-misattributions.md` — MusicRadar — Summers = Electric Mistress, Cobain = Small Clone (both NOT a Boss CE).

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`CE-2W-DeepResearch.md`](CE-2W-DeepResearch.md); the manual is at [`manuals/CE-2W_eng02_W.pdf`](manuals/CE-2W_eng02_W.pdf).

> **Honest coverage notes:** strong — Boss's own two-amp settings + the wet/dry/buffered-bypass routing are nailed down and quoted, and the CE-1/CE-2 history is well-verified. Reddit/TalkBass/Reverb were blocked, so community tips lean on accessible sources (SoS, Legendary Tones, Gigs & Guitars, theFretBoard, Ground Guitar). No dedicated numeric bass-settings source surfaced (keep DEPTH low). CE-2W-specific internal mods remain undocumented. Guitar Chalk's numbers are a 0–10 scale (relative, not clock).
