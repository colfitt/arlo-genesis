# JHS 424 Gain Stage — Usage Guide

How people *actually* use the 424 Gain Stage, to complement the spec/reference dossier in `424-DeepResearch.md`. It's the **last always-on box in the whole three-board rig** — the "cassette print" that finishes the console-to-tape arc (Colour Box V2 = the Neve front-end at the start). The two things to internalize: it's a **three-gain-stage cascade you *build* (Gain 1 trim → Gain 2 channel → Volume master)**, and the **Mk.gee "elastic" sound is a dynamic-clipping technique + pairings**, not just a knob setting. Take the **XLR out into the Apollo**, set it once, leave it on.

> Captured this wave (Tier B, 2 agents): 6 video transcripts + 11 distilled links = 17 sources (see §8). Dossier patched this wave: the demo credited as "JHS official" (`LXhkhDbGEUw`) is actually **Happy Mag** — JHS's own upload is private, and the public "official" content is the **John Mayer guest demo**; also sharpened the *Nebraska* note (cut on a **TEAC 144**, not a 424). Verified via yt-dlp.

---

## 1. Essential workflows

**Build the tone from Gain 1 into Gain 2, set level with Volume.** **Gain 1** (= the 424's TRIM) is where the dirt is born — input saturation ("this gain is no joke"). **Gain 2** (= the CHANNEL fader) either cools it or "blows it out totally"; **past ~3 o'clock it becomes a gated fuzz monster.** **Volume** (= MASTER) sets output independent of grit — Andertons proved cranking Volume alone adds *no* distortion ([gain-staging-tips](links/gain-staging-tips.md); [andertons-424-deep-dive](transcripts/andertons-424-deep-dive.md)).

**Same loudness, different grit** (the key trick): because the two gains balance against the master, you can hit the same level either clean or filthy. More Gain 1 + lower Volume = more grit at equal output. "This sucker gets loud" — mind the master into the converter.

**The Mk.gee move is dynamic, not static.** Set the gains near the clipping threshold, then **let pick attack trigger the blow-out** — dig in and it falls apart, ease off and it cleans. Fingerstyle and lower-output pickups give control. John Mayer's framing: it's "not a paint color, but a whole different brush" — and "all the good ones are really, really *down* here" (best tones at low settings) ([john-mayer-424-demo](transcripts/john-mayer-424-demo.md)).

**Treble = a de-haze / clarity dial.** The pedal trends dark/gooey by default; the Treble knob is your articulation recovery when the always-on print buries detail. Bass "bottoms out" the low end but **flubs at high gain** (especially baritone) — pull it back before the print.

---

## 2. Signature settings

No clock-face settings exist in any primary source (it's an Aug-2025 pedal — JHS/MusicRadar/Guitar World all give relative guidance only). Below are attributed; Mk.gee clock values are inferred (the *technique* is the load-bearing finding). See dossier §13 for four fuller rig-tuned starting points.

| Sound | Settings | Source |
|---|---|---|
| **Subtle tape warmth** (always-on glue) | Gain 1 **low**, Gain 2 moderate, Volume to taste — "warm, harmonically rich preamp" | quoted, [bass-musician-magazine-settings](links/bass-musician-magazine-settings.md) |
| **Saturated grit** | grit lives on **Gain 1 higher** = "vintage overdrive/fuzz" | quoted, Bass Musician |
| **Blown-out gated fuzz** | **Gain 2 past 3 o'clock** = "gated fuzz monster" (below that, no gating) | quoted, Bass Musician |
| **John Mayer "rubbery"** | **Gain 1 ~12, Gain 2 up** — "every note falls off the cliff" | quoted, [john-mayer-424-demo](transcripts/john-mayer-424-demo.md) |
| **"Grunge"** | both gains **maxed** (Pearl Jam vibe) | quoted, JM demo |
| **Clean DI** | low–moderate Gain 1, higher Gain 2, Treble cut a touch — stays clean | directional, [guitarguitar-mkgee-tone-in-a-box](transcripts/guitarguitar-mkgee-tone-in-a-box.md) |

**The full Mk.gee "elastic" recipe is the 424 *plus* pairings** ([mkgee-tone-explained](links/mkgee-tone-explained.md)): subtle **chorus** (the rig's CE-2W, ~Rate 9–10 / Depth 11–12), a short **dark reverb** (decay 2–3 s, ~20–25% mix), a short **delay** (300–400 ms, low feedback), and a **fast-attack compressor** (1176-style). Baritone + heavy strings + finger attack is what makes the preamp bloom.

---

## 3. Power-user tips, tricks & hidden features

- **XLR terminus into the Apollo.** The balanced XLR out (with ground-lift dip switch) runs *simultaneously* with the ¼" out — the clean path into the interface, and the 424's standout advantage over the PORTA424 (which has no XLR). Engage ground-lift if the rack hums; set Volume so peaks don't clip the converter ([gain-staging-tips](links/gain-staging-tips.md)).
- **Its compression acts as a gentle program-dependent limiter** on the way into A/D — useful for a terminus.
- **Buffered bypass** conditions the signal even at modest settings and drives the cable run to the rack cleanly (no relay click).
- **For a wall-of-sound print, keep Gain 2 below ~3 o'clock** and add the grit with Gain 1 — past that, the gate chokes sustained drones.

---

## 4. Placement & the mono question (terminus craft)

- **PORTA424 → JHS 424 is two cassette channels in series** (the period-correct "bounce one track to another"), not redundant: the **MXNHLT PORTA424** is the fuller, faithful channel-strip *tone* (with a real slider fader, but **no XLR**); the **JHS 424** is the gain-stage *commit/print* with the XLR + ground-lift + buffered-bypass terminus behavior. Keep the PORTA424 cleaner and let the 424 do the gain (or vice-versa) — **don't max both** or the bus turns to mush ([porta424-vs-jhs424](links/porta424-vs-jhs424.md)).
- **The stereo image must collapse to mono here** — the rig is stereo from the CE-2W on, but both Portastudio boxes are mono. The dossier's call (and the period-correct one) is to **commit to mono at the print** — a real Portastudio bounce is mono-per-track anyway, and it suits the ruined-cassette aesthetic. Nothing in the sources contradicts this.
- **vs Generation Loss (Board 3 opener):** complementary — Gen Loss is *transport* degradation (wow/flutter/dropouts) applied *first* so the time effects degrade with it; the 424 is *channel* degradation applied *last* to glue the bus. Gen Loss breaks the source; the 424 prints the result.
- **De-perfecting the VG-800:** running a clean modeled amp/cab through the worn cassette channel is exactly what makes COSM tones believable — but the VG-800 is near line level, so back **Gain 1** off if it clips unintentionally.

---

## 5. Notable users & history (honest — the fame is borrowed)

- **Mk.gee** is the **inspiration, not a pedal user.** His tone (a modified Jaguar/Jazzmaster into a real Tascam Portastudio 424's overdriven preamp) is the entire reason the pedal exists — but he uses the **hardware**, and there's no evidence he plays the JHS box. An entire micro-market (the Audio Hertz "Mk.pre" plugin, boutique pedals) now chases that one preamp tone ([mkgee-phenomenon-breadth](links/mkgee-phenomenon-breadth.md)).
- **John Mayer DEMOED it ≠ uses it.** He filmed one JHS video while Josh Scott recovered from a mountain-bike accident; his point was about *dynamics*, not an endorsement ([john-mayer-demo](links/john-mayer-demo.md)).
- **Portastudio history:** the 1979 **TEAC 144** ($899) launched the home-recording revolution; Springsteen's *Nebraska* (1982) was cut on a **144** (not a 424 — same family). The lineage runs through DIY/lo-fi/bedroom recording, Sting, Mac DeMarco, and '90s lo-fi ([tascam-portastudio-history](links/tascam-portastudio-history.md)).
- The pedal is too new (Aug 2025) for a real user roster — its fame is borrowed from Mk.gee + the Tascam, and that's the honest framing.

---

## 6. Rig-specific recipes (terminus on Board 3)

Order: `… → H90 → MXNHLT PORTA424 → JHS 424 → Apollo / FOH` — always-on.

- **Subtle always-on print (the default).** Volume noon · Gain 1 ~9 · Gain 2 ~10 · Bass noon · Treble ~1:00 — rubbery compression + a little channel grain under everything; hit the Apollo near unity via XLR. Keep the PORTA424 as the tone, let this finish it.
- **Lo-fi degraded "ruined cassette" print.** Push the gains for blown-out gated fuzz — but keep the **PORTA424 clean so only one stage destroys**; watch Bass (pull back if it flubs); Treble up to keep some articulation. The drone/doom "recorded-wrong" wall.
- **Banjo/baritone at the terminus:** by here the banjo's pierce is long gone, so the 424 mostly adds rubbery compression to a sustained bed — Treble is the clarity dial if it goes murky; keep Gain 2 modest so transients don't get spitty/gated against the wall.
- **Bass/DI commit:** the 424 is a documented bass favorite ("tape-like saturation," pairs well with octavers/synths) and a one-box bass DI via the XLR.
- **Mono-commit the stereo bus here** (sum L+R in) — the natural place to glue the rig's abundant upstream stereo width down for the cassette print.

---

## 7. Best learning resources

- **guitarguitar (Kieran)** — [the richest settings demo](transcripts/guitarguitar-mkgee-tone-in-a-box.md): baritone, per-song Mk.gee recipes, Boss SY-1, XLR-to-desk.
- **Andertons** — [23-min deep dive](transcripts/andertons-424-deep-dive.md): runs the rig's exact XLR→Apollo path, proves Volume≠drive, the dynamic-clip trigger.
- **John Mayer** — [the public "official" demo](transcripts/john-mayer-424-demo.md): spoken settings, the dynamics framing. **Eirik Stordrange** — [XLR-DI-into-interface, C-standard](transcripts/eirik-stordrange-424-demo.md). **Riley Thornton** — [control walkthrough + Mk.gee recipe](transcripts/riley-thornton-424-demo.md). **Happy Mag** — [A/B vs a real Tascam 414](transcripts/happy-mag-424-vs-real-414.md) (busts the preamp-not-tape myth).
- **Text:** [Russo gain-staging how-to](links/gain-staging-tips.md), [Bass Musician settings](links/bass-musician-magazine-settings.md), [Mk.gee tone-pairings guide](links/mkgee-tone-explained.md), [GPX 4-preamps comparison](links/guitar-pedal-x-4-preamps-compared.md), [JHS official tone copy](links/jhs-official-tone-copy.md).

---

## 8. Common pitfalls / gotchas

- **Gain 2 past ~3 o'clock = gated fuzz monster** — chokes sustained drones; for wall-of-sound keep it below that and drive with Gain 1.
- **Bass flubs at high gain** (esp. baritone) — pull it back before the print.
- **Dark/gooey by default** — Treble is the clarity recovery.
- **No true bypass** (buffered only) and **mono** — the stereo bus must collapse here; on dead power it behaves like a buffer dropout. As the last box before FOH, give it a reliable supply.
- **Niche/harsh clipping by design** — it's not a transparent drive and won't pretend to be one; "won't suit all players."
- **It gets loud** — set Volume so peaks don't clip the Apollo; the pedal can put out a hot signal.
- **9 V only** (don't exceed; 50 mA draw is trivial otherwise).

---

## 9. Captured sources

**Transcripts** (`research/transcripts/`):
- `guitarguitar-mkgee-tone-in-a-box.md` — guitarguitar (Kieran) — baritone, per-song Mk.gee recipes, SY-1, XLR-to-desk (richest).
- `andertons-424-deep-dive.md` — Andertons — XLR→Apollo, Volume≠drive, the dynamic clip trigger.
- `john-mayer-424-demo.md` — (re-up of JM's JHS demo) — spoken settings: 12/up "rubbery," both-maxed "grunge."
- `eirik-stordrange-424-demo.md` — Eirik Stordrange — XLR-DI into interface, clean vs blown-out.
- `riley-thornton-424-demo.md` — Riley Thornton — control walkthrough, Mk.gee recipe (tape breakup before + gated verb after).
- `happy-mag-424-vs-real-414.md` — Happy Mag — A/B vs a real Tascam 414; preamp-not-tape myth-bust *(the dossier had mis-credited this as JHS official)*.

**Links** (`research/links/`):
- `jhs-official-tone-copy.md` — JHS — control mapping, XLR/ground-lift, verbatim tone copy.
- `gain-staging-tips.md` — Russo Music — best how-to on the Gain1/Gain2/Volume interaction + XLR.
- `bass-musician-magazine-settings.md` — Bass Musician — the only quoted named-sound guidance.
- `bass-and-gated-fuzz.md` — Bass Musician — bass/low-end use, the Gain-2 gated-fuzz threshold, Treble-as-clarity.
- `424-mkgee-tone-settings.md` — synthesized copyable Mk.gee recipes (A–D) + method.
- `mkgee-tone-explained.md` — guitareffect.fr — what to pair the 424 with (chorus/reverb/comp) for "elastic."
- `mkgee-phenomenon-breadth.md` — MusicRadar — the borrowed-fame / crowded-recreate-market context.
- `john-mayer-demo.md` — Guitar World — demoed-not-uses, the dynamics framing.
- `tascam-portastudio-history.md` — MusicRadar — 144/*Nebraska*/lo-fi lineage (144≠424 note).
- `porta424-vs-jhs424.md` — Guitar Pedal X — JHS vs MXNHLT vs Benson vs Neutrino; why two boxes.
- `guitar-pedal-x-4-preamps-compared.md` — Guitar Pedal X — the four-Tascam-preamp comparison.

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`424-DeepResearch.md`](424-DeepResearch.md); the manual is at [`manuals/jhs424.pdf`](../manuals/jhs424.pdf).

> **Honest coverage notes:** brand-new (Aug 2025) — **no clock-face settings exist anywhere**; all sources give relative guidance, so the numbered settings above are quoted-directional or inferred (flagged). Reddit/TalkBass/Reverb-history blocked the fetcher (403), so this leans on accessible trade press + the demo transcripts. Mk.gee uses the **hardware, not the pedal**; John Mayer **demoed, doesn't use** — both kept honest.
