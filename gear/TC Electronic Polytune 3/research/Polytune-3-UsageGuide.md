# TC Electronic Polytune 3 — Usage Guide

How people *actually* use the Polytune 3, to complement the spec/reference dossier in `Polytune-3-DeepResearch.md`. The tuner half is "solved" — the real usage content is **mode choice (poly vs needle vs strobe), the BonaFide buffer on/off decision, and the banjo/open-tuning + modeler-tuning workflow**. In this rig it's 2nd in the chain (after the VG-800, before CB Clean + the fuzzes), so it tunes the VG-800's *summed* output, not a raw pickup — which shapes most of the advice below.

> Captured this wave (Tier C, 1 agent): 2 video transcripts + 5 distilled links = 7 sources (see §7). Both dossier video URLs verified correct via yt-dlp (Equipboard; ADDICTED TO GEAR) — no mis-credits. New field data on the buffer (a silicon-fuzz A/B) *reinforces* the dossier's leave-it-true-bypass call.

---

## 1. Essential workflows

**MonoPoly auto-detection is the core trick.** Strum all strings = **polyphonic** whole-guitar glance (fast, between songs); pick one string = single-note **needle/strobe**. You don't switch modes for this — it auto-detects ([polytune3-demo-review-equipboard](transcripts/polytune3-demo-review-equipboard.md)).

**Needle is the everyday mode; strobe is the precision tool.** Reviewers default to single-string **needle** because it's quicker and tracks better; **strobe** (slows as you approach, stops centered) is "more finicky" and reserved for **intonation and getting a string dead-on** — which is exactly the mode that matters for this rig's sustained-wall aesthetic, where any beating string in a held drone is punishing ([polytune3-modes-workflow-official](links/polytune3-modes-workflow-official.md)).

**The mode set** is just Display-Mode cycling: Guitar/Needle → Guitar/Strobe → Bass/Needle → Bass/Strobe. **Drop-D** = press-and-hold the footswitch; **flat tunings** (Eb/D/Db/C/B) and **capo 1–7** step via the Tuning button and persist across power cycles. Engaging the tuner mutes the output for silent tuning; the ambient-light sensor auto-dims the display.

**Tuning technique that holds (Chris Berrow):** tune **up from below** the note (wind up to it — holds better than overshooting and backing off); **mute** the other strings (sympathetic vibration reads you sharp); pluck **once, consistently** (harder = sharper read); let the note **ring** and nudge a hair sharp since pitch settles slightly flat on release; **recheck the bottom strings** after, since upper-string tension pulls them ([how-to-tune-properly-chris-berrow](transcripts/how-to-tune-properly-chris-berrow.md)).

---

## 2. The BonaFide buffer — on or off?

**Leave it True Bypass in this rig** (both rear DIP switches left). The dossier's reasoning holds, and the new field data strengthens it:
- The classic "never a buffer before fuzz" worry is mostly a **germanium** problem — Sound on Sound's exact caveat is "antique germanium fuzz boxes…rather picky about what's fed into them"; otherwise the BonaFide "made a significant difference to the high end" ([bonafide-buffer-sos-review](links/bonafide-buffer-sos-review.md)).
- **But even with a *silicon* Fuzz-Face-type**, a JustinGuitar A/B (Kamkor) found buffer-ON made the tone **"harsher" and broke guitar-volume cleanup** — his rule: "either disable the buffer or put it after the fuzz" ([bonafide-buffer-vs-fuzz-debate](links/bonafide-buffer-vs-fuzz-debate.md)). So even though this rig's fuzzes are silicon (MXR 108) + Muff (Hizumitas) and *tolerant*, true bypass is the cleaner call.
- **And it's redundant here anyway** — CB Clean immediately downstream already buffers the board, and the VG-800 source doesn't need impedance rescue.

**DIP modes** (set once at the bench — it's internal-only): both-left = True Bypass; top-right = Buffered; both-right = **Buffered + Display-Always-On**. Flip to Buffered + Display-Always-On *only* if CB Clean is ever removed/moved or you hear high-end loss into the dirt — and **A/B it** (opinion genuinely cuts both ways).

---

## 3. Banjo, open tunings & tuning the VG-800

- **Banjo = chromatic/strobe single-string, NOT polyphonic.** Polyphonic mode expects a low→high 6-string guitar order; the EBM-5's **re-entrant high-g 5th string** (an octave above the 3rd, starting at the 5th fret) breaks that order. A **chromatic** display just names whatever pitch it hears, so it handles open-G (gDGBD) and the drone string fine ([banjo-open-tuning-chromatic-technique](links/banjo-open-tuning-chromatic-technique.md)). Tune the 5th string one at a time; banjo's fast attack/decay favors **strobe** for a stable read.
- **Tune off a CLEAN VG-800 patch.** The tuner sees the VG-800's summed output — if the patch has heavy modeled distortion/modulation/synth (COSM/GR), pitch detection struggles. Momentarily select a clean amp/guitar model, tune, switch back. (The manual itself says place the tuner before drive/modulation — it already is.)
- **The VG-800's own tuner is complementary** — it reads the **pre-modeling divided GK signal** (arguably the more "correct" tap for fine intonation), but it's menu-driven and GK-instruments-only. Use the VG-800 tuner for fine GK intonation; use the Polytune for fast, universal, foot-stomp tuning of *everything* (including the magnetic guitars and bass).
- **Baritone (B standard):** in range — use Bass mode or chromatic on the lowest strings if the guitar-mode read gets jittery; low strings read best in strobe. **Jazz bass:** switch Display Mode to **Bass**.

---

## 4. Notable users

It's the **industry-standard tuner** — "almost everyone with a pedalboard since 2010." There's no signature-tone mythology to a tuner; a famous-user list is just a list of people who needed to tune. Skip it.

---

## 5. Common pitfalls / gotchas

- **It needs an instrument plugged in to do anything** — the footswitch does nothing with no input signal (a common "it won't turn on" confusion).
- **Polyphonic mode dislikes anything non-clean upstream** — distorted/modulated/synth patches confuse poly pitch-detection. Tune off a clean source.
- **The buffer is internal DIP-switch only** — you must unscrew the backplate; you can't toggle it live. Set it once.
- **>100 mA draw** — the heaviest Board-1 pedal except the digital modelers; give it a real 100 mA+ isolated slot.
- **Spec confusion:** TC's older bundled PDF still carries "±0.1 cent" strobe; the **3's** current/correct figure is **±0.02 cent** strobe / 0.5 cent chromatic. Both are "absurdly accurate."
- **Don't intonate off the poly display** — poly is for speed (coarser by nature); use strobe for intonation and drone precision.

---

## 6. Versus alternatives

- **Boss TU-3:** ±1 cent (50× coarser than the Polytune's strobe), no poly, no strobe, **buffered-only** (its buffer is *always* in your path — the worst fit for a fuzz front end). The Polytune wins on accuracy + the true-bypass *choice*.
- **Peterson StroboStomp HD:** the real **banjo upgrade** — sweetened/banjo presets and a clearer strobe (some find the Polytune's strobe "drifting spaghetti"), at ±0.1 cent. Bigger, pricier, buffered, no poly strum-and-go. Worth it *only if* banjo intonation becomes a recurring studio bottleneck; otherwise the Polytune's poly speed wins day-to-day ([polytune3-vs-tu3-vs-strobostomp](links/polytune3-vs-tu3-vs-strobostomp.md)).
- **The VG-800's own tuner:** free, pre-modeling, GK-only, menu-driven — complementary, not a replacement.

**Why it stays:** fastest universal tuner on the board (poly strum-and-go), most accurate in its class (±0.02 strobe for the sustained-wall stuff), the *only* one of these that lets you choose **true bypass** in front of a fuzz section, and the BonaFide buffer is free insurance if the board's buffering ever changes.

---

## 7. Captured sources

**Transcripts** (`research/transcripts/`):
- `how-to-tune-properly-chris-berrow.md` — How To Play Guitar with Chris Berrow — technique lesson: tune-up-from-below, mute, pluck-consistency, let-it-ring.
- `polytune3-demo-review-equipboard.md` — Equipboard — mode walkthrough; runs buffered + display-always-on.

**Links** (`research/links/`):
- `polytune3-modes-workflow-official.md` — TC official Quick Start — authoritative controls + verbatim DIP buffer table + spec-confusion note.
- `bonafide-buffer-sos-review.md` — Sound on Sound — impedance specs, audible high-end gain, the germanium-fuzz caveat (verbatim).
- `bonafide-buffer-vs-fuzz-debate.md` — JustinGuitar community — the buffer-vs-silicon-fuzz A/B; "tuner goes first / A/B it" consensus.
- `banjo-open-tuning-chromatic-technique.md` — banjo tuning guide — re-entrant 5th string, chromatic-not-poly, creep-up-from-below.
- `polytune3-vs-tu3-vs-strobostomp.md` — aggregated forums — accuracy figures, poly/true-bypass edge, Peterson's banjo-preset edge (partly search-derived, flagged).

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Polytune-3-DeepResearch.md`](Polytune-3-DeepResearch.md); the manual is at [`manuals/polytune3.pdf`](manuals/polytune3.pdf).

> **Honest coverage notes:** a tuner is a "solved" utility, so coverage is intentionally thin and centered on the buffer + banjo/open-tuning + modeler-tuning angles (where the real decisions are). TalkBass, TDPRI, Sweetwater, and OffsetGuitars 403'd the fetcher, so the tuner-comparison file is partly search-summary-derived (flagged in-file); all other files are from cleanly-fetched primary sources. The buffer-in-front-of-fuzz question genuinely cuts both ways — the consensus is "A/B it," and this rig lands on true bypass for redundancy + cleanliness reasons.
