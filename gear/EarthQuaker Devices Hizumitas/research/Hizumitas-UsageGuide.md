# EarthQuaker Devices Hizumitas — Usage Guide

How people *actually* use the Hizumitas, to complement the gold-standard spec/reference dossier in `Hizumitas-DeepResearch.md`. In this rig it's the Board-1 sustain engine behind the banjo and baritone: the single highest-leverage skill is treating the **Tone knob as a filter you sweep through a note's decay** (not a set-and-forget EQ), and the second is **stacking** — Wata's own move is a fuzz-plus-distortion wall, which maps directly onto the 108 in front and the Brothers AM behind it here.

> Captured this wave (Tier B, 2 agents): 4 video transcripts (one is a multi-video notes file) + 11 distilled links — 15 sources total (see §8). Two dossier attribution fixes folded in: the "Tone Report demo" is on **Reverb's** channel, and the "vs Triangle" video is a **We As A Company** "sound like Boris" shootout that also stacks a **Boss DS-1** — both verified via yt-dlp.

---

## 1. Essential workflows

**The Tone-as-filter sweep (THE signature technique).** Hold a sustained note or chord and *sweep Tone through the decay* — the wall "burns and changes shape as it decays" ([premier-guitar-synth-filter-tone](links/premier-guitar-synth-filter-tone.md)). The knob is **inverted**: CW = bass-forward/dark/scooped (the 3n3 HPF cap), CCW = treble-forward/"near-RAT," noon ≈ flattest. Reviewers describe three zones ([mixdown-bass-and-recording](links/mixdown-bass-and-recording.md)): **CCW = "Iommi treble-booster," center = mid-boosted cut-through voice, CW = "stupidly fat" low end.** The center/mid voice is the one that survives a dense downstream chain — keep that in mind on a busy board.

**Guitar-volume cleanup.** There's no clean floor (minimum Sustain is already crunchy), but it cleans up unusually well for a Muff — roll the instrument volume to 6–8 for controlled crunch even with Sustain up, especially on treble-bleed guitars/baritone ([tone-report-and-bass-settings](links/tone-report-and-bass-settings.md)).

**It's voiced for loud amps.** Wata's own framing: "I want people to try it in an environment where they can set amps very loud" — the feedback-sustain bloom only really arrives at volume ([stillman-wata-musicradar-making-of](links/stillman-wata-musicradar-making-of.md)). Feedback is controllable (low runaway even at high gain).

---

## 2. Signature settings

Knob positions are clock-face (Volume / Sustain / Tone). EQD's own "Hizumitas for Noodlers" post is the cornerstone and the only source with reliably quoted positions; everything else is attributed inline ([eqd-noodlers-settings](links/eqd-noodlers-settings.md)).

| Sound | Volume / Sustain / Tone | Source |
|---|---|---|
| **Doom wall** (max heavy) | max / max / **CW** (full bass) | EQD Noodlers (quoted) |
| **Balanced mid-forward** lead/rhythm | ~10–12 / **noon** / ~10 (treble side) | EQD Noodlers (quoted) |
| **Controlled crunch / low-gain** | noon / **min** / **CCW** (treble) — roll guitar vol to clean | EQD Noodlers (quoted) |
| **Wata-adjacent everyman** | 9–10 (unity) / noon / noon | The Distortion Principle (quoted summary) |
| **Bass** (Cliff Burton vibes) | noon / ~3:00 / ~10 (treble side); low feedback | Andy Bassist (quoted) |
| **Starter** | noon / noon / noon | EQD |

*The "synth-filter" move isn't a static setting — park Sustain at noon and sweep Tone CW↔CCW live.* A Guitar Chalk 1–10 settings table exists but is flagged low-confidence/likely-inferred with suspect inverted-Tone numbering — defer to EQD's quoted positions ([guitarchalk-settings-table](links/guitarchalk-settings-table.md)). See dossier §14 for four fuller rig-tuned starting points.

---

## 3. Power-user tips, tricks & hidden features

- **Source-agnostic & buffer-tolerant.** "Doesn't give a crap if you hit it with active or passive pickups, a six/seven/eight-string, or a bass" ([mixdown](links/mixdown-bass-and-recording.md)) — the ~150 kΩ input handles the banjo / VG-800 / Colour Box buffer in front fine (unlike a vintage Fuzz Face).
- **Sustain min ≠ off** — it's a fuzzy overdrive at minimum, more low end as you raise it.
- **Touch-sensitive Tone** — small moves = large tonal shifts; dial it watching the knob, not by feel.
- **No noise gate** — it doesn't gate between notes; add the BF-3's suppression or a gate if you need silence.
- **Bass / Bass VI use is genuinely good** — documented as a recording-preamp-ish fuzz with the center Tone zone cutting through ([mixdown](links/mixdown-bass-and-recording.md)).

---

## 4. Stacking recipes (Muff-stacking is the point here)

- **Wata's canonical move: Hizumitas + Boss DS-1** stacked together "to create more chaotic feel" — her own words, confirmed across multiple sources ([wata-boris-guitar-world-interview](links/wata-boris-guitar-world-interview.md); [sixstringsensei-muff-stacking](links/sixstringsensei-muff-stacking.md)).
- **Drives IN FRONT push it to brutal/savage high-gain.** Tested-good front-stackers: JHS PackRat, Boss SD-1 Waza, **EQD Plumes** ("go-to metal" per The Distortion Principle), EQD Special Cranker, Empress Para EQ MkII. Logic: a low-gain OD/boost in front tightens and slams the Sustain stage; a RAT-voiced drive adds grind; a para-EQ pre-shapes what the fuzz saturates ([sixstringsensei-muff-stacking](links/sixstringsensei-muff-stacking.md)).
- **An EQ / mid pedal AFTER is the documented fix for its one weakness** ("needs some EQ or mid-hump pedal to expand versatility"). **This maps exactly onto the rig's Brothers AM placed after the Hizumitas** — run Brothers clean-ish to restore/sculpt the upper mids the wall masks.
- **Rig-specific (from the dossier's chain):** the MXR 108 silicon Fuzz Face sits *in front* here, acting as a gated/splatty pre-stage the Hizumitas smooths into a wall; the Longsword downstream should have its gain backed well off (8–10:00) since the Hizumitas already supplies the saturation.

---

## 5. Notable users & techniques

**Wata of Boris (the signature artist — the Hizumitas's discography is essentially hers).**
- **A/B verdict:** *"The Hizumitas is not inferior to my ELK when I A/B them"* — she tours it as her main fuzz, keeping the original Elk as reference/backup ([wata-boris-guitar-world-interview](links/wata-boris-guitar-world-interview.md); [wata-boris-musicradar-pedalboard-tour](links/wata-boris-musicradar-pedalboard-tour.md)).
- **Discography line:** "Feedbacker" (from *Boris at Last - Feedbacker*) used the original **Elk**; anything from **2022 onward** with her audible fuzz wall is likely the **Hizumitas**.
- **Stacking philosophy:** layers fuzz "with a distortion" (DS-1) for chaos, plus wah, reverb, and echo. She carries *multiple* fuzzes (Hizumitas, MASF Watafuzz, Dwarfcraft Shiva, Mattoverse AirTrash) and swaps per song.
- **Core rig:** '86 Les Paul Custom → fuzz → Roland Space Echo = "the core of my expression." The Boris *band* wall is Wata's Muff (Elk/Hizumitas) summed with Takeshi's **modified Pro Co RAT** bass dirt — which is why the Hizumitas's CCW "near-RAT" Tone zone matters ([boris-rig-tour-musicradar](links/boris-rig-tour-musicradar.md)).
- **Dev lore:** Jamie Stillman did ~7 revisions over a year; part of the Elk's magic turned out to be "wildly drifted" component tolerances, not just the schematic ([stillman-wata-musicradar-making-of](links/stillman-wata-musicradar-making-of.md)).

**Other users:** it's a doom/shoegaze board staple, but **Wata is the only signature/claimed user** — no others invented.

---

## 6. Rig-specific recipes (banjo/baritone drone)

- **Banjo "sustain manufacturer."** Banjo decays in ~1.5 s; the Hizumitas completes the note. Start **Tone 1–2:00** (bass side, to roll off banjo's piercing 2–4 kHz via the 3n3 cap), **Sustain noon, Volume 11**. If still too bright, feed it a darker VG-800 amp model (Tweed/AC, treble pulled back). The gentle compression also evens out banjo's fast attack/fast decay so notes behave more like guitar notes.
- **Baritone Jazzmaster = home territory.** Less Tone compensation needed — noon to 1:00 works.
- **Sweep the wall live.** On a sustained baritone drone, sweep Tone through the decay (§1) so the wall morphs from fat/dark to mid-forward as it rings — the most expressive single gesture, and ideal feed for the granular/reverb End Board (the sustain makes Microcosm/Chroma/H90 sound intentional, not choppy).
- **VG-800 synth/pad patches** turn into massive distorted drones (good); poly guitar-synth patches artifact heavily under the Muff topology — on-aesthetic for "broken/recorded-wrong."

---

## 7. Best learning resources

- **EarthQuaker Devices (official)** — the demo + the ["Hizumitas for Noodlers"](links/eqd-noodlers-settings.md) settings post (the cornerstone settings reference).
- **The Distortion Principle** — [best talking deep-dive with concrete settings](transcripts/distortion-principle-most-aggressive-big-muff.md) (Wata-adjacent setting, Plumes stack, amp A/B).
- **Reverb / Tone Report (Andy)** — [unity-gain, the Tone sweep, baritone cleanup](transcripts/tone-report-reverb-hizumitas.md).
- **We As A Company** — best A/B shootout (vs Triangle Big Muff + Boss DS-1, "sound like Boris") *(no captions — see [no-caption-demos](transcripts/no-caption-demos.md))*.
- **Andy Bassist** — [the bass demo](transcripts/andy-bassist-hizumitas-bass-demo.md). **Premier Guitar / Oscillator Devices** — synth-filter technique / pure-doom textures *(notes in [no-caption-demos](transcripts/no-caption-demos.md))*.
- **Text:** [Premier Guitar review](links/premier-guitar-synth-filter-tone.md), [Mixdown](links/mixdown-bass-and-recording.md) (bass/recording, three Tone zones), [SixStringSensei](links/sixstringsensei-muff-stacking.md) (stacking), the Wata interviews above.

---

## 8. Common pitfalls / gotchas

- **CCW (treble) extremes can be harsh / noisy** — back off, and avoid maxing **Sustain + Tone simultaneously** (clarity loss, possible oscillation/hiss) ([premier-guitar-synth-filter-tone](links/premier-guitar-synth-filter-tone.md)).
- **Touch-sensitive Tone knob** — large effect from small moves.
- **No noise gate** — quiet for a high-gain Muff, but it won't silence between notes.
- **Relay true-bypass needs power to pass signal** — if the supply dies on stage, the signal dies. (10 mA draw otherwise — any isolated slot handles it.)
- **Don't exceed 9V** — EQD explicitly warns against it; no 18V trick.
- **Feedback blooms only at volume** — bedroom levels won't show the sustain character.
- **Mod note:** the **3n3 tone cap** is the single-cap mod target (→330pF for Elk-faithful, ~1nF for less low-end swing); no new community mod chatter surfaced this pass.

---

## 9. Captured sources

**Transcripts** (`research/transcripts/`):
- `tone-report-reverb-hizumitas.md` — Reverb (Andy), 2021-11-04 — unity gain, Tone sweep, baritone cleanup.
- `distortion-principle-most-aggressive-big-muff.md` — The Distortion Principle, 2021-11-28 — Wata-adjacent setting + Plumes stack + amp A/B.
- `andy-bassist-hizumitas-bass-demo.md` — Andy Bassist, 2023-03-03 — bass settings, low feedback.
- `no-caption-demos.md` — notes file for the caption-less demos: EQD official, Premier Guitar First Look, We As A Company (vs Triangle + DS-1), Oscillator Devices doom, Pedal of the Day, Cloud Factory.

**Links** (`research/links/`):
- `eqd-noodlers-settings.md` — EQD (Malcolm X Abram) — the cornerstone; all clock positions quoted.
- `distortion-principle-wata-setting.md` — copyable Wata-adjacent setting.
- `tone-report-and-bass-settings.md` — guitar + bass settings.
- `guitarchalk-settings-table.md` — 5-tone table, flagged low-confidence/inferred.
- `premier-guitar-synth-filter-tone.md` — the synth-filter sweep-on-decay technique; CCW-harshness gotcha.
- `mixdown-bass-and-recording.md` — bass/Bass VI use; three Tone zones; recording context.
- `sixstringsensei-muff-stacking.md` — concrete stacking recipes; Wata+DS-1; the "needs EQ after" weakness.
- `wata-boris-guitar-world-interview.md` — Wata's A/B verdict + "use it with a distortion for chaos" + Feedbacker.
- `wata-boris-musicradar-pedalboard-tour.md` — full verified board; DS-1 + Watafuzz; multiple fuzzes.
- `stillman-wata-musicradar-making-of.md` — 7 revisions/year; "set amps very loud"; drifted tolerances.
- `boris-rig-tour-musicradar.md` — 2017 fuzz-wall architecture; Takeshi's modified RAT; Muff+RAT palette.

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Hizumitas-DeepResearch.md`](Hizumitas-DeepResearch.md).

> **Honest coverage notes:** Reddit and Sweetwater user reviews were fully blocked to the fetcher (403/unfetchable), so forum-tier community chatter is sourced via blogs/reviews rather than raw threads; the EQD official demo and the best A/B shootout lack captions (logged as notes). Third-party *quoted* settings beyond EQD's own Noodlers post are scarce — community settings talk mostly points back to that post.
