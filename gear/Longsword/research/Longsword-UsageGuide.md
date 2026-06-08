# Electronic Audio Experiments Longsword — Usage Guide

How people *actually* use the Longsword, to complement the spec/reference dossier in `Longsword-DeepResearch.md`. In this rig it's the heaviest gain stage / "Wall" event (8th on Board 1, after the Brothers AM + the 108→Hizumitas fuzz wall): the way to get the most out of it is to **stop treating it as added gain and start treating it as a studio EQ with a footswitchable second distortion channel** — back Drive off (8–10:00), run the **no-diode Center mode**, sculpt with the 3-band EQ, and use the **+20 dB Boost** (with its fixed 300 Hz low cut) as the actual intensifier stomp. EAE literally ships a factory preset (*Electrify Armament*) that *is* this approach.

> Captured this wave (Tier B, 2 agents): 6 video transcripts + 10 distilled links = 16 sources (see §8). Biggest find: EAE's **V4.5 Technical Manual (June 2025) ships 8 named factory presets** — the authoritative settings source, which didn't exist in the dossier's §13. Folded a dossier fix in too: several §10 demos were mislabeled "EAE" but are actually Harsh Tones / Zachary Rizer / Eirik Stordrange (third parties) — verified via yt-dlp.

---

## 1. Essential workflows

**Dial the EQ like a console, not a RAT.** Low/High are James-Baxandall shelves; Mid is active with a SHIFT-selectable center (**up = 1 kHz, down = 300 Hz**). It's "more studio EQ than stompbox" — **small moves are drastic, the bands barely interact, adjust gradually.** People who twist it like a one-knob RAT Filter overshoot ([eae-studio-eq-baxandall-mid-shift](links/eae-studio-eq-baxandall-mid-shift.md)).

**Two console moves to memorize** (verbatim from the manual): **boost BOTH Low + High = an effective mid-scoop; cut BOTH = an effective mid-boost.** The scoop also "overloads the output stage for a more aggressive sound."

**Clip-mode = your dynamics control** (V4/V4.5 labeling — MOSFET / none / silicon):
- **Center (no diodes)** — op-amp clipping only, minimal compression, **most dynamic range**. *The mode for stacking into an already-driven signal* (EQ + volume shove without piling compression on compression). Caveat: at high Drive it gets very loud and "the tone controls are more effective cutting than boosting" — rebalance Level when you switch modes.
- **Up (MOSFET)** — medium compression, smooth all-rounder.
- **Down (silicon)** — high compression, the squared-off "brick wall."

**The Boost is a second channel, not a volume bump.** It's +20 dB *with a fixed 300 Hz front-end low cut* — "more gain and a different, slightly tighter EQ and feel." That low cut is the tightening mechanism, giving you "two distinct voicings for low and high gain" from one stomp. Treat the Boost footswitch as a voicing change / performance intensifier ([delicious-audio-longsword-clipmodes-eq](links/delicious-audio-longsword-clipmodes-eq.md); [eae-eq-recipes-clipmodes](links/eae-eq-recipes-clipmodes.md)).

**Tighten with the Low cut.** EAE's own line: the Longsword has "a great deal of low frequency content, so a tighter tone can be achieved by reducing the Low control — particularly useful with an already overdriven [source]." Cut Low to kill fuzz flub; the Boost's 300 Hz cut does it in one stomp. And **scoop the low-mid (SHIFT down) to clarify mud** on neck-pickup/down-tuned sources.

---

## 2. Signature settings & presets

**The 8 V4.5 factory presets** (descriptions verbatim; knob positions read off the manual's diagrams, approximate). Source: [eae-manual-presets](links/eae-manual-presets.md). Knob layout: top row = Level/Drive/Low, bottom = High/Mid/Boost; toggles = DIODE + SHIFT.

| Preset | Description (verbatim, abridged) | Config |
|---|---|---|
| **Quest Hook** | "great starting point for a wide variety of instrument and amp combinations" | all ≈ noon, MOSFET, SHIFT 1k, Boost off |
| **Anduril** | "classy, refined gain… push your amp with the Level knob" | Level high, Drive noon, Boost up, MOSFET |
| **Stormbringer** | "Drive + Boost, push Mids at 1kHz… old distortion into a practice amp. Very Cvlt" | Drive+Boost up, Mid 1k boosted, silicon |
| **Bastard Sword** | "heavy, raw… swinging a big chunk of steel. Very potent on bass" | Drive near-max, Low up/High cut, **silicon, SHIFT 300Hz** |
| **Electrify Armament** | "Disengage the clipping diodes, Drive to minimum, lets the EQ shine… kick on Boost for grit" | **DIODE center, Drive min, Boost = stomp** |
| **Great Weapon Fighting** | "max dynamics (Diode center), crank Mids at 300Hz… sturdy sustain, desert/stoner" | DIODE center, **Mid 300Hz boosted** |
| **Berserker** | "pull out the midrange entirely, go big or go home. Might kick a fuzz off your board" | **full mid-scoop**, high gain |
| **Finesse Weapon** | "full bore mid boost… for pushing amps and other pedals" | **full mid-boost**, try both SHIFT |

**The two rig-load-bearing presets:** *Electrify Armament* is EAE's own endorsement of the stacked-on-fuzz approach (no-diode + Drive min + Boost stomp), and *Great Weapon Fighting* is essentially the banjo-body move (300 Hz mid boosted).

**Owner-shared named sounds** (attributed): *full-bore doom* = "gain high + Boost engaged" + silicon + SHIFT-up mid maxed for "brutal, in-your-face" cut ([owner-doom-heavy-settings](links/owner-doom-heavy-settings.md)); *articulate rhythm* = "gain at noon"; *RAT-like snarl / bass* = silicon + SHIFT-down (300 Hz) ([zachary-rizer-feT-bass](transcripts/zachary-rizer-feT-bass.md)); *live bass* = "Boost and Mid-shift very usable live, holds the low end" ([andy-bassist-bass](transcripts/andy-bassist-bass.md)).

---

## 3. Power-user tips, tricks & hidden features

- **The Mid is a mix weapon** — EAE's phrase is cutting through with a "blade of midrange." SHIFT-up (1 kHz) boosted to cut through density; SHIFT-down (300 Hz) boosted to add body a bright source lacks ([eae-which-drive-should-you-buy](links/eae-which-drive-should-you-buy.md)).
- **Drive has a built-in high-end rolloff** as it increases — reduces harsh upper harmonics, which is why it doesn't get ice-picky on a banjo at high gain.
- **Rebalance Level whenever you change clip mode** — center mode especially "can get extremely loud at higher Drive settings."
- **Center mode at high gain favors cutting over boosting** on the tone controls — sculpt by subtraction there.
- **Buffer-friendly** (~500 kΩ input Z) — completely happy after the CB Clean / Colour Box buffers upstream, unlike the fuzzes ahead of it.

---

## 4. Notable users & maker story (honest)

**There is no single signature artist** for the Longsword (unlike Wata/Hizumitas) — the real story is the maker:
- **John Snyder / EAE.** Longtime guitarist, BU CAS '14 + **EE doctorate '20** (photonics/quantum optics); plays in noise-rock band **Weird Machine**; influences are **Radiohead *Kid A*, Sigur Rós, Godspeed You! Black Emperor** + screamo — the same drone/post-rock world as this rig. EAE founded 2015 in a Brighton basement apartment; **the Longsword V1 was the company's first pedal**, now a 4-person Waltham shop in perpetual backorder. Ethos, verbatim: *"We don't really need more clones of the Tubescreamer or Rat or Big Muff"* — the Longsword is that family done bigger, with a real EQ ([eae-john-snyder-wbur](links/eae-john-snyder-wbur.md); [eae-snyder-origin-pedal-of-the-day-interview](links/eae-snyder-origin-pedal-of-the-day-interview.md)).
- **Documented EAE artists** — **Pile** (→ Mirror House), **Kal Marks**, **Touché Amoré** (→ Limelight, 2020) — are noise-rock/post-hardcore *company collaborators*, **NOT doom/shoegaze and NOT Longsword endorsers.** Do not present them as Longsword users.
- *Minor sourcing flag:* the "2015 snowpocalypse / first-pedal" origin comes from EAE's manual + Snyder's 2016 interview; BU's profile corroborates the basement/side-project spirit but doesn't independently confirm the snowpocalypse detail.

---

## 5. Rig-specific recipes (banjo/baritone drone)

Chain: `… MXR 108 → Hizumitas → Brothers AM → Longsword → Oxford → BF-3 → …`

- **Stacked intensifier (the "Wall" event) = the *Electrify Armament* preset.** DIODE **center**, Drive **8–10:00** (the Hizumitas already has the gain), cut **Low ~10:00** to tame fuzz flub, carve a cut with **Mid/SHIFT-up**, High ~noon — then the **Boost footswitch is the actual intensifier stomp** (its 300 Hz cut also tightens). Use **silicon (down)** instead when you want the whole front end fused into one squared-off slab.
- **Banjo lead (body for banjo-as-lead) = the *Great Weapon Fighting* move.** DIODE center or MOSFET, **Mid SHIFT-down (300 Hz) boosted** to add the low-mid body a banjo physically lacks, High eased back ~11:00 to soften the pierce, Drive moderate. This is the single most flattering dirt move in the rig for the banjo's deficiencies.
- **Standalone doom wall (fuzz off) = *Bastard Sword* territory.** Near-max Drive, **silicon**, Low boosted + High cut, SHIFT-down — "very potent on bass/baritone." Pull Low back if it flubs.
- **Tightened doom rhythm.** Drive low, **Boost on** (300 Hz cut keeps palm-mutes defined), MOSFET, Low cut, Mid SHIFT-up ~11:00. Drive's high rolloff + the Low cut keeps chugs readable instead of a mud-slab.
- **Into the Oxford:** the Longsword's EQ is the tone control for the whole dirt cluster; the Oxford just adds a final shove — don't ask it to fix anything.
- **Modeled VG-800 source** clips earlier than the manual's passive-guitar procedure implies (hot line-level) — start Drive lower; Center mode keeps it cleaner, silicon obliterates it (on-aesthetic).

---

## 6. Best learning resources

- **Demos In The Dark** — [the best single control walkthrough](transcripts/demos-in-the-dark.md) (single-coil + humbucker, captions).
- **Zachary Rizer** — [best bass + stacking demo](transcripts/zachary-rizer-feT-bass.md) (RAT-snarl & sub-bass recipes; V3-era).
- **Brendan Sloan** — [V2-era demo + live band-fuzz setting](transcripts/brendan-sloan-v2.md). **Andy Bassist** — [V4 bass demo](transcripts/andy-bassist-bass.md). **Harsh Tones / Eirik Stordrange** — [baritone+bass Short](transcripts/harsh-tones-bass-baritone.md) / [marketing-copy demo](transcripts/eirik-stordrange-demo.md).
- **Text:** [EAE V4.5 manual presets](links/eae-manual-presets.md) (THE settings source), [EAE "Which drive should you buy?"](links/eae-which-drive-should-you-buy.md), [Delicious Audio](links/delicious-audio-longsword-clipmodes-eq.md) (clearest clip-mode/EQ writeup), [WBUR maker profile](links/eae-john-snyder-wbur.md), [TalkBass owner thread](links/talkbass-longsword-npd-owner-tips.md) (the key owner community — bass-leaning).

---

## 7. Common pitfalls / gotchas

- **⚠️ 18V is a V3-only trick — DANGER on this unit.** Owners say it "slays at 18V," but that's the older V3 (bipolar 9–18 V). **The repo V4/V4.5 is 9 V-only and its protection circuit shuts the pedal down above 9 V** (or on reverse polarity). Do not feed it 18 V.
- **Studio-EQ overshoot** — small moves are drastic, bands nearly non-interacting; dial gradually or you'll fly past the sweet spot.
- **Clip-mode labels differ by version** — old copy says LED/germanium/open; the V4/V4.5 manual says **MOSFET/none/silicon**. Trust the manual for this unit.
- **It over-saturates when stacked on the fuzz** — the whole rig discipline is to back Drive off and use it as EQ + Boost, not added gain.
- **75 mA draw** — give it a real isolated supply slot; a low-current daisy-chain tap won't do.
- **Center (no-diode) mode gets very loud at high Drive** and its dynamic range can "run out" — rebalance Level.
- **Six-knob layout isn't a tidy single row** — cosmetic, not functional.

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `demos-in-the-dark.md` — Demos In The Dark — full control walkthrough (single-coil + humbucker).
- `zachary-rizer-feT-bass.md` — Zachary Rizer — bass + stacking demo; RAT-snarl & sub-bass recipes (V3).
- `brendan-sloan-v2.md` — Brendan Sloan — V2-era demo + live band-fuzz setting.
- `andy-bassist-bass.md` — Andy Bassist — V4 bass demo *(no captions)*.
- `eirik-stordrange-demo.md` — Eirik Stordrange — sponsored demo w/ EAE marketing copy *(no captions)*.
- `harsh-tones-bass-baritone.md` — Harsh Tones, Inc. — 60-sec bass+baritone Short *(no captions)*.

**Links** (`research/links/`):
- `eae-manual-presets.md` — EAE V4.5 Technical Manual — the 8 named factory presets + EQ tricks (THE settings source).
- `eae-eq-recipes-clipmodes.md` — EAE blog/product — maker EQ recipes, clip-mode & Boost intent.
- `eae-studio-eq-baxandall-mid-shift.md` — EAE — studio-EQ behavior, Baxandall topology, the boost-both/cut-both tricks.
- `delicious-audio-longsword-clipmodes-eq.md` — Delicious Audio — clearest plain-language clip-mode + EQ + Boost writeup.
- `eae-which-drive-should-you-buy.md` — EAE — Longsword vs Dagger vs Halberd; "blade of midrange."
- `owner-doom-heavy-settings.md` — The Fretboard NPD + Pedalboards of Doom — concrete doom/heavy settings.
- `talkbass-longsword-npd-owner-tips.md` — TalkBass — owner community (Boost-as-2nd-channel, 18V-is-V3-only) *(blocked — snippet-sourced)*.
- `eae-john-snyder-wbur.md` — WBUR — maker story + honest EAE artist roster.
- `eae-snyder-origin-pedal-of-the-day-interview.md` — Pedal of the Day — Snyder verbatim: V1 = first pedal, anti-clone ethos, drone influences.
- `eae-snyder-bu-bostonia-profile.md` — BU Bostonia — independent corroboration (PhD timeline, Weird Machine).

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Longsword-DeepResearch.md`](Longsword-DeepResearch.md); the manual is at [`manuals/Longsword.pdf`](../manuals/Longsword.pdf).

> **Honest coverage notes:** boutique pedal — only 3 of 6 demos had captions (rest are notes), and there's no single official EAE-channel Longsword demo. TalkBass, The Gear Page, Reddit, and Equipboard all blocked the fetcher (402/403), so owner-community tips were recovered from snippets and accessible sources rather than full forum reads. No Longsword signature artist exists — the famous names are EAE *company* collaborators, not Longsword endorsers.
