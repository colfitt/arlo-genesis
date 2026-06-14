# DS-10 Drum Shaper — Usage Guide

DS-10 is XLN's simple, very-low-CPU **transient shaper** — Attack / Sustain plus a
frequency-focused **Mojo** punch control. In this rig its job is **punch**: set knock on a
drum *before* the lo-fi degraders eat it (it's the **first** box after AD2 in the drum
bus), recover attack on degraded/sampled hits, and shape your MPC/Digitakt breaks. It's
strong at *adding* attack, weak at *removing* sustain — reach elsewhere to gate a tail.
*(Tier-C unit: community depth is genuinely thin — see QC note. Controls are relative
knobs; XLN publishes no numeric defaults, so values below are directional.)*

---

## 1. Essential workflows & settings

**Pick the ALGORITHM first, then the mode** — algorithm choice matters more than the
Kick/Snare/Bus mode tab (which is just a starting point; any mode runs on any source).
[links/ds10-musicradar-review.md]
- **Natural** (default) — transparent, cleaner/punchier/louder transients, artifact-free
  even pushed hard; the most-improved on kicks. Use for nearly everything.
- **Smooth** — extra-long release, "parallel-compression-like"; best on full kits, loops,
  drum bus.
- **Classic** — the AD2 algorithm; raw, aggressive, **pumping**; weak on kicks but its
  positive-Sustain settings flatter **snare tails**. Reach for vibe/pump.

**The controls:**
- **Attack** raises/lowers the transient spike; **Sustain** raises/lowers the post-hit tail.
- **Mojo = frequency-focused punch** (a separate processor): Kick = **Tightness**
  (boomy↔tight low end), Snare = **Body** (low-mid), Bus = **Presence** (high-freq, called
  "Snap" in some third-party copy — same control). [links/ds10-official-manual-controls.md]
- **Soft Clipping** toggle — gentle saturation when you drive Attack hard into the
  non-linear zone; drum sound-designers use it for density. [links/ds10-musicradar-review.md]

**The killer combo (MusicRadar):** push **Sustain UP** for body/fatness, then use **Mojo
Tightness** to clamp the low-end mud that long Sustain creates on kicks — body without the
boom. [links/ds10-musicradar-review.md]

**Tighten / "de-verb" move (Morsy):** **Sustain all the way DOWN** to dry out busy
hats/tambourines/room, then a touch of **Attack** to poke the transient back through.
[transcripts/ds10-tighten-drums-morsy.md]

---

## 2. Rig-specific recipes (owner's gear named)

**1) Place in the AD2 lo-fi drum bus — set punch FIRST.** AD2 (clean, multi-out) →
**DS-10** → RC-20 → SketchCassette II → Decapitator → Goodhertz Lossy. DS-10's community
sweet spot is "boosting drums in a compressed/busy mix," so establishing attack/knock
*before* the degraders means there's punch left to survive the crush. Natural algo for
clean punch, or Smooth across the whole bus. [transcripts/ds10-5-great-ways-thomann-sensho.md; links/ds10-kvr-gearspace-community-verdict.md]

**2) Recover knock from squashed/lo-fi drums (parallel).** DS-10 adds attack well but
reduces sustain poorly — so to restore lost knock *after* RC-20/Lossy crush, blend a
**parallel** DS-10 (Kick mode, Attack up, Mojo Tightness) rather than gating in series.
Note: **no internal Mix/dry-wet knob** in the reviewed builds — do parallel via a **Logic
aux send / Ableton return**, not a plugin wet knob. [links/ds10-kvr-gearspace-community-verdict.md; links/ds10-musicradar-review.md]

**3) MPC / Digitakt / sampled breaks (directly on-point).** Put DS-10 on the whole Drum
Rack / sampler: pull **Sustain** to dry out an old break's room/imperfections, push
**Attack** to recover knock on individual chopped hits — exactly the chop-an-Amen-break
workflow on the MPC Sample / Digitakt. [transcripts/ds10-5-great-ways-thomann-sensho.md]

**4) Fix draggy/late hits.** Add **Attack** to pull transients *earlier* and tighten a
loose or sidechained part — useful on bounced one-shots or hardware-sampled loops.
[transcripts/ds10-tighten-drums-morsy.md]

**5) Reverb-send shaping (shoegaze wash trick).** Put DS-10 **before** a reverb return and
raise **Attack** to feed more of the hit into the tail — "spark" a bigger wash without
raising the send level. [transcripts/ds10-5-great-ways-thomann-sensho.md]

---

## 3. Aesthetic-fit (doom vs shoegaze)

- **Punchy doom / cut through the wall:** Kick mode, **Natural**, Attack up, **Mojo
  Tightness** up to clamp boom → a tight thump that pokes through a dense guitar wall. On
  the bus, Attack + Bus Presence up to surface buried drums; Soft-clip on for glue.
- **Washed shoegaze / ambient:** pull **Attack DOWN** to soften spiky hits into the mix;
  **Sustain UP + Smooth** to swell room/tail into a wash. Thomann's inverse trick (Attack
  down, Presence up) keeps softened hits from going dull.
- **Slowcore / drone:** Sustain-up + Smooth turns sparse hits into long breathing swells;
  Mojo to stop them muddying.
[transcripts/ds10-5-great-ways-thomann-sensho.md; links/ds10-musicradar-review.md]

---

## 4. Power-user tips & common pitfalls

- **Very low CPU** — ~10 instances "barely touching" CPU; safe one-per-drum even in busy
  sessions. [transcripts/ds10-5-great-ways-thomann-sensho.md]
- **Weak at sustain REDUCTION** (the one real community criticism) — great at adding
  attack, but to fully gate/kill a long tail, NI Transient Master / Logic stock Transient
  Shaper / SPL go further. "Dry it out a bit" = fine; "kill the tail" = wrong tool.
  [links/ds10-kvr-gearspace-community-verdict.md; transcripts/ds10-vs-spl-vs-logic-amen-808.md]
- **No input-gain control** (no gain-staging) and **no multiband** (Mojo is the only
  frequency-aware element). [links/ds10-musicradar-review.md]
- **No internal dry/wet** → parallel must be host-side (see recipe 2).
- **Over-shaping artifacts** — pushing Attack hard gets *harsh* (Morsy backed off); the
  meter is "perceived"/visual — trust ears, not the waveform display.
- **Logic = AU-only** (`.component` in CONTENTS.md — fine). In **Ableton Live 12 Lite**,
  cheap CPU-wise but watch the track/return ceiling if you also explode an AD2 multi-out
  kit; do heavy per-drum DS-10 work in Logic, or limit to 2–3 returns in Lite.
- **Context:** frequently bundled / on deep sale (~$20–58); same XLN installer/folder as
  AD2 + RC-20. No documented signature-artist uses (it's a utility, not a sound).

---

## 5. Captured sources

**Transcripts** (`research/transcripts/`):
- `ds10-5-great-ways-thomann-sensho.md` — Thomann/Sensho, the deepest creative-use video (breaks, inverse Attack/Mojo, reverb-send, plucky bass, taming perc)
- `ds10-tighten-drums-morsy.md` — Morsy Music, real session: Sustain-down to tighten, Attack to fix draggy hits
- `ds10-vs-spl-vs-logic-amen-808.md` — Marc Renton A/B vs SPL & Logic stock on Amen/808 *(captions 429-blocked → distilled notes)*

**Links** (`research/links/`):
- `ds10-official-manual-controls.md` — control reference (Attack/Sustain/Mojo/modes/algos/soft-clip) *(manual 403'd → triangulated)*
- `ds10-musicradar-review.md` — most authoritative review; algorithm verdicts, Sustain+Tightness combo, limitations
- `ds10-kvr-gearspace-community-verdict.md` — community consensus, the sustain-reduction weakness, alternatives, value *(Gearspace 403'd → folded from snippets)*

**QC note:** 6 sources (3 transcripts + 3 links) — DS-10 has **no deep tutorial ecosystem**
(no dedicated Reddit threads surfaced); this is the realistic ceiling, not a search
shortfall. The XLN manual, Gearspace, and web.archive.org **403'd/blocked the bot** — the
manual control reference and Gearspace verdict are **triangulated** from XLN's product
page + MusicRadar + ProducerSpot/ADSR + search snippets (control names/modes/algorithm
behaviors corroborated across 3+ sources = reliable; exact numeric ranges aren't published
anywhere — DS-10 uses relative knobs). DS-10's place in this rig's drum bus and the
parallel-knock-recovery recipe are **reasoned from** the documented AD2 chain + the
community "best for boosting drums in a busy mix" consensus, not a single first-party source.

## Sources

See §5 for the local capture index. Originals: youtube.com (Thomann Bedroom Producers,
Morsy Music, Marc Renton), support.xlnaudio.com, musicradar.com, kvraudio.com,
gearspace.com. URLs on line 1 of each captured file.
