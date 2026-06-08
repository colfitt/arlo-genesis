# Chase Bliss Brothers AM — Usage Guide

How people *actually* use the Brothers AM, to complement the spec/reference dossier in `Brothers-AM-DeepResearch.md`. In this rig it's the always-on **drive platform** sitting 7th on Board 1 (after the Hizumitas, before the Longsword): the highest-value way to run it is the **2-IN-1 template** — Channel 2 as an always-on low-gain tightener/re-leveler, Channel 1 parked as a footswitchable clean push into the Longsword — with the **MASTER dip on** so the push doesn't throw your stage level, and the **Rangemaster treble booster** on hand to claw banjo cut back. Remember the AM is a King-of-Tone-grade *transparent* drive in **fixed series** (Boost → Ch1 → Ch2); there is no fuzz mode and no blend (those were the 2017 original).

> Captured this wave (Tier B, 2 agents): 5 video transcripts + 12 distilled links = 17 sources (see §8). MIDI/preset behavior leans on the reusable CB-stack files in the Blooper's `research/links/`. One dossier attribution fix folded in: the `3_ffkecEoFQ` demo is **AndyDemos**, not Chase Bliss's official channel — the genuine official demo is the Technical Demo (`YSv2JOXf26Y`), verified via yt-dlp.

---

## 1. Essential workflows

**The series stack is a *push*, not a blend.** Channel 1 (and the front booster) drive Channel 2's input — like cascading amp stages. The manual's stack modes (OVERLOADER / EXPANDER / COMBO) all come down to **cranking VOL 1 to push Channel 2 harder**. Small VOL 1 moves have a large effect on Ch2 saturation ([cb-technical-demo](transcripts/cb-technical-demo.md); [factory-preset-settings](links/factory-preset-settings.md)).

**Use the MASTER dip whenever you boost-stack.** It turns **VOL 2 into a global master**, so pushing VOL 1 adds *saturation* without a level spike — and it fixes the **VOL-1 level-snap trap** (turn Channel 2 off and output otherwise jumps to whatever VOL 1 is set to). This is Chase Bliss's own canonical boost-stacking recipe ([cb-technical-demo-settings](links/cb-technical-demo-settings.md)).

**The hidden Presence is worth finding.** Hold a channel's **footswitch + turn its TONE knob** to set that channel's Presence (ships fully down). Dan Steinhardt's reveal on That Pedal Show: bringing Presence **up** "changed the game," opening a closed/chewy tone — exactly the move for clawing banjo articulation back. Andy uses ~25% to smooth a spanky guitar ([tps-demo-settings](links/tps-demo-settings.md); [andy-demo-settings](links/andy-demo-settings.md)).

**Treble booster lives at the very front, linked to Channel 1.** Middle = OFF = pure classic KOT; up = brighter/strident (shaves lows); down = classic Rangemaster (upper-mid emphasis). It shines pushed *into* an already-overdriven channel for a "vocal" lead — and it's the tool to recover cut the Hizumitas darkened ([tps-vs-prince-duke-of-tone](transcripts/tps-vs-prince-duke-of-tone.md)).

**Sweet spot is below max gain.** Reviewers agree: "you don't need maximum gain," and the highest gain levels bring "heavily colored compression." The booster is "addictive, dynamite," best at low volume ([premier-guitar-review-tips](links/premier-guitar-review-tips.md)).

---

## 2. Signature settings & presets

Knob positions: the **manual prints panel diagrams and relative directions, not numeric clock values** — so factory-preset *modes/dips* are quoted, but exact knob numbers don't exist in any primary source. Dossier §13's clock positions are inferred; treat them as starting points.

**Factory presets** (modes/dips quoted; [factory-preset-settings](links/factory-preset-settings.md)):
| Preset | Config | Use |
|---|---|---|
| **THE ANALOG MAN** ("Mike's Sound", P1) | Mike Piera's KOT settings, **dip HI GAIN 1 ON**; stock KOT config = Ch1 OVERDRIVE, Ch2 BOOST | Solid always-on starter; "kick on Ch2 when you need a lift" |
| **SUNNY SKIES** (P2) | Treble-boost → Ch1 **DISTORTION** → Ch2 **OVERDRIVE** | Bright/focused full 3-circuit stack |
| **2-IN-1** (P3, alt bank) | Ch2 always-on OD, Ch1 a footswitchable boost "beyond its limits" | **The literal template for this rig's always-on tightener + push** |
| **BAD BROS** (P4, alt bank) | **HI GAIN 1 + 2 ON**, everything cranked | "As big and brash as it gets" — overflowing distortion |

**Player-shared starting points** (quoted):
- **Dan Steinhardt's decade-long KOT setting:** Ch1 **OVERDRIVE**, Ch2 **BOOST** — the boost adds harmonics + a small mid lift (his "overdrive boost"), not a big volume jump.
- **Joel Korte's go-to:** Rangemaster **ON** → Channel 1 in **BOOST**.
- **AndyDemos rhythm/lead base:** both channels OVERDRIVE, Ch1 lower gain / Ch2 higher, "gain ~halfway on both" stays detailed when stacked. ~25% Presence to smooth.
- **Dual-stack wall:** Ch1 **DISTORTION** + Ch2 **OVERDRIVE** adds saturation/compression without a volume jump.

---

## 3. Power-user tips, tricks & hidden features

- **PRES LINK dip** makes TONE control Tone **and** Presence together — more open/transparent; CB recommends it for full-range/synth sources (good for the modeled VG-800 output).
- **Three internal treble-booster trim pots** (CB-blessed, not a mod — confirmed in CB's own post): **(1) Input Impedance** (default fully CW; back it off CCW so the booster "behaves much better after a buffer" — the load-bearing trim here, since CB Clean + Colour Box buffer the front end); **(2) Output** (noon; CW hits the KOT harder); **(3) Bias** (noon; headroom / Rangemaster symmetry). Tiny movements, small flathead ([treble-booster-internal-trims](links/treble-booster-internal-trims.md)).
- **HI GAIN 1/2** dips add ~25% gain (LED turns red). **MOTOBYP** makes a footswitch momentary (hold-to-engage). **Tap both footswitches** to swap channels.
- **The MIDI jack doubles as a TS external-footswitch input** to bypass Channel 2 — useful if you're not running MIDI.
- **External-control ramp:** assign EXP or CV to **GAIN 1 or VOL 1** via the CONTROL dip bank; with MASTER on, you ramp *saturation/intensity* into Channel 2 without a level spike — a drone-build tool.

---

## 4. MIDI / preset integration (into the CB stack)

The AM folds into the rest of the rig's Chase Bliss MIDI ecosystem (Clean, Generation Loss, Big Time, MOOD MkII, Blooper, Onward). It's another **ring-active TRS** pedal that needs a powered **Chase Bliss MIDIbox** (not native 5-pin/USB). PC recalls presets; a uniform CC map covers knobs/dips. **Save the AM's preset to the same number as the rest of the board so one Digitakt PC recalls a whole-stack scene** ([midi-preset-integration-cb-stack](links/midi-preset-integration-cb-stack.md)). Full MIDIbox/TRS wiring and preset/scene-recall detail live in the reusable references: `Gear/Chase Bliss Blooper/research/links/cb-stack-midi-trs-and-midibox.md` and `…/cb-stack-preset-scene-recall.md`.

---

## 5. Notable users & lineage (honest)

The AM is a **2025 pedal with no developed artist mythology yet** — don't claim AM-specific touring users. The real story is the **King of Tone lineage**, inherited by association:
- **Mike Piera (Analog Man)** is the effective marquee "user" — his settings ship as the **THE ANALOG MAN / "Mike's Sound"** preset. The collab: Joel Korte reached out **early 2020**; ~5 years to market; the Beano Boost uses **Akihabara-sourced TO-18 silicon transistors** ([guitarworld-collab-story](links/guitarworld-collab-story.md); [analogman-bethel-profile](links/analogman-bethel-profile.md)).
- **KOT lineage:** a heavily-reworked Marshall **Bluesbreaker** (~2003, originally built for Jim Weider of The Band) → Prince of Tone → MXR Duke of Tone (2022) → **Brothers AM (2025)**. KOT is one of the most waitlisted ODs ever (4–6 yr wait) ([king-of-tone-lineage](links/king-of-tone-lineage.md)).
- **Verified *KOT*-ecosystem users** (NOT AM endorsements — flag as lineage only): Ed O'Brien, Brad Whitford, Tom Bukovac, Noel Gallagher, John Mayer, Jason Isbell, Gary Clark Jr., John Petrucci, Kenny Wayne Shepherd.

---

## 6. Rig-specific recipes (banjo/baritone drone)

Chain: `… MXR 108 → Hizumitas → Brothers AM → Longsword → Oxford → BF-3 → …`

- **Clean tightener after the Muff (the always-on default).** Channel 2 only, mode **BOOST** or low **OVERDRIVE**, GAIN low, **MASTER dip on**, Presence up slightly to recover cut the Hizumitas darkened. Goal = tighten + re-level + add cut, *not* more gain. (The 2-IN-1 factory preset is this, with Ch1 ready as the push.)
- **Clean push into the Longsword.** Use Channel 1 **BOOST** as a clean lift — more cut and level, not more fuzz — and keep the Longsword's own gain low. The KOT principle "a clean boost *after* a dirt pedal increases volume without adding much distortion" is exactly this move.
- **Recover banjo articulation.** Rangemaster (booster down) into Channel 1 lifts the upper-mids the Hizumitas rolled off; or bring Presence up. Banjo doesn't need more saturation here — it needs articulation and level.
- **Baritone:** OVERDRIVE mode's tightness keeps the low strings from going flabby after the Muff; use HI GAIN sparingly (baritone + Muff + AM distortion compounds fast).
- **Modeled VG-800 source:** lean on **BOOST + PRES LINK** for the most open, full-range response (CB's own recommendation for full-frequency/synth sources).
- **Ramped drone build:** EXP/CV → GAIN 1 (MASTER on), sweep heel→toe to swell the push into Channel 2 under a sustained chord before the Longsword and the End Board's granular/reverb stages chew on it.

---

## 7. Best learning resources

- **Chase Bliss (official) — Technical Demo** — [the authoritative deep-dive](transcripts/cb-technical-demo.md): modes, hidden Presence, dips, MASTER, stock config.
- **That Pedal Show** — [best A/B vs the KOT family](transcripts/tps-vs-prince-duke-of-tone.md) (King/Prince/Duke of Tone + Bluesbreaker) with real player settings and the Presence reveal.
- **AndyDemos** — [clearest practical two-channel/stacking walkthrough](transcripts/andy-brothers-am-demo.md).
- **Rhett Shull + Josh Scott (JHS)** — [KOT lore/FOMO + "the dips just externalize KOT internals" framing](transcripts/rhett-shull-review.md). **Doug Hanson** — [concise accurate feature recap](transcripts/doug-hanson-demo.md).
- **Text:** [Premier Guitar](links/premier-guitar-review-tips.md) (treble booster "dynamite," high-gain compression caveat), [Guitar.com Big Review](links/guitar-com-big-review-tips.md) (usability + dip/Presence/trim tips), [Guitar World collab story](links/guitarworld-collab-story.md).

---

## 8. Common pitfalls / gotchas

- **VOL-1 level-snap trap** — turn Channel 2 off and output jumps to VOL 1's setting; **MASTER dip is the fix**. Know this before going live.
- **Mode-to-mode volume jumps are inherent** (a clipping side-effect — more distortion = more compression = different perceived level). Rebalance with VOL or use presets.
- **Distortion + HI GAIN compounds compression** on top of the already-squished Muff signal — gets squishy fast. The rig-correct move is the opposite of max gain.
- **Presence defaults fully down and is hidden** — easy to forget it exists.
- **~200 mA draw** — give it a healthy isolated 9V slot, not a daisy chain. **Do not exceed 9V.**
- **MIDI needs the powered MIDIbox** — not native DIN/USB; don't forget to power the box.
- **Internal trims are fragile** — tiny movements with a small flathead.

---

## 9. Captured sources

**Transcripts** (`research/transcripts/`):
- `cb-technical-demo.md` — Chase Bliss (official) — modes, Presence, dips, MASTER, stock config.
- `tps-vs-prince-duke-of-tone.md` — That Pedal Show — A/B vs the KOT family + player settings + Presence reveal.
- `andy-brothers-am-demo.md` — AndyDemos — practical two-channel/stacking walkthrough.
- `rhett-shull-review.md` — Rhett Shull + Josh Scott (JHS) — KOT lore/FOMO; "least Chase-Blissy CB pedal."
- `doug-hanson-demo.md` — Doug Hanson — concise feature recap.

**Links** (`research/links/`):
- `factory-preset-settings.md` — Brothers AM manual — the 4 factory presets (quoted) + "Finding Your Sound" + Presence/TB quotes.
- `cb-technical-demo-settings.md` — Joel Korte's stock config + personal go-to + dip behaviors.
- `tps-demo-settings.md` — Dan's "overdrive boost," the Presence reveal, boost-stacking, exp/MIDI footswitch.
- `andy-demo-settings.md` — rhythm/lead, organic vs saturation stacks, 25% Presence, exp on Gain 1.
- `preset-stacking-recipes.md` — CB official — 4 presets + boost-stacking + MASTER-dip recipe.
- `treble-booster-internal-trims.md` — CB official post — the 3 booster trims (impedance/output/bias) + "after a buffer" advice.
- `premier-guitar-review-tips.md` — treble booster "dynamite," high-gain compression caveat, touch response.
- `guitar-com-big-review-tips.md` — usability verdict + dip/Presence/internal-trim tips.
- `guitarworld-collab-story.md` — Korte×Piera dev story, TO-18 transistor, verified KOT genre/artist mentions.
- `king-of-tone-lineage.md` — KOT Bluesbreaker lineage, scarcity, verified famous-user list.
- `analogman-bethel-profile.md` — Mike Piera human-interest profile; 6-yr waitlist.
- `midi-preset-integration-cb-stack.md` — the AM's MIDI/CV/preset hooks, citing the two reusable cb-stack refs.

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Brothers-AM-DeepResearch.md`](Brothers-AM-DeepResearch.md); reusable CB-stack MIDI/preset research lives in `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`.

> **Honest coverage notes:** Reddit, The Gear Forum, TalkBass, and several review sites were blocked to the fetcher (403/paywall), so community findings lean on Chase Bliss's own docs, Analog Man's site, and named reviewers rather than raw forum threads. It's a 2025 pedal — there's little user-generated power-user lore yet, and **no exact numeric knob settings exist in any primary source** (the manual prints diagrams/directions). There is no AM-specific artist data; the famous names are KOT-lineage only.
