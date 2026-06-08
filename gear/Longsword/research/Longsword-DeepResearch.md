# Electronic Audio Experiments Longsword — Deep Research

A working dossier for the rig's heaviest gain stage. The Longsword sits 8th on Board 1 — after the Brothers AM drive platform and the 108→Hizumitas fuzz wall, before the Oxford Drive — tagged "Wall" / event, not always-on. This is the "stack a high-gain distortion on top of the fuzz wall for maximum destruction" pedal, and per the Hizumitas dossier it over-saturates when stacked, so most of this document is about restraint: treating a flagship op-amp distortion as a one-stomp tone-shaper and intensifier rather than as added gain.

**Identity confirmed.** The manual in this repo (`manuals/Longsword.pdf`, *Longsword V4 Manual, Version 2, 10-Jan-21, John Snyder*) confirms the rig sheet: this is the **Electronic Audio Experiments (EAE) Longsword**, specifically the **V4 / V4.5** generation, designed and built by John Snyder in Boston/Waltham, MA. The GearProfile.md had no brand field and GearList flagged "(brand?)" — that ⚠️ is now resolved. It is EAE's flagship and their first-ever pedal.

## 1. Lineage: EAE's First Pedal

The Longsword is where Electronic Audio Experiments began. Per the manual's own introduction, Snyder conceived it "in the margins of my grad school notebook" and breadboarded it during Boston's early-2015 "snowpocalypse" in a basement apartment — a doctorate-in-electrical-engineering origin story that the [WBUR profile](https://www.wbur.org/news/2024/05/07/boston-guitar-pedal-builder-electronic-audio-experiments-pile-rock-music) corroborates. It launched the company and remains the flagship.

Circuit type, from the manual directly: **"an op-amp drive with diode shunt clipping."** An op amp boosts amplitude, a pair of diodes shunts the peaks, the clipped peaks generate new harmonics. Snyder is refreshingly honest that this block "is found in hundreds of pedals (including the Distortion+, Rat, OCD, even the venerable Klon Centaur/KTR) and is, in itself, not special." What makes the Longsword special, per the manual, is "the way its clipping amplifier is placed between a series of other amplifiers and filters to precisely shape the sound" — i.e. the surrounding gain staging and the studio-grade EQ, not the clipper.

Where it sits in EAE's line (the brief's "Halberd/Sviatovid" comparison — note **Sviatovid is not an EAE product**; the real siblings are below), per [EAE's "Which EAE drive should you buy?"](https://www.electronicaudioexperiments.com/blog/2022/7/7/which-eae-drive-should-you-buy):

- **Longsword** — the big op-amp distortion. "An open, clear distortion character with lots of thickness," with "thicker low midrange content" that "fills out bright guitars." Hybrid active/passive EQ. The most versatile and the most gain on tap.
- **Dagger** — a "scaled-down Longsword," op-amp drive with germanium clipping. More compressed, "more chimey at low gain" but fuzzier as you push it, less low-mid punch, more "sizzly treble." Compact format.
- **Halberd** — *not* an op-amp pedal at all. A transistor mic-preamp-derived overdrive running 24V internally, "extremely soft transition into clipping," dynamics-first. Lighter gain, more touch-sensitive.

For this rig — banjo, baritone, doom — the Longsword is the correct EAE drive: it has the gain ceiling and the low-mid mass the others lack.

**Version history** (per [EAE's product page](https://www.electronicaudioexperiments.com/pedals/longsword)): V1 initial release → V2 added the diode-clipping switch and a "Gain 1/2" preset switch → V2.1 dropped the Range toggle → V3 added 9–18V bipolar supply and replaced Gain 1/2 with the Boost mode → **V4 introduced the current 6-knob layout, SMD PCB, relocated Boost knob, and soft-touch relay bypass** → **V4.5 changed the enclosure/jacks, added over-voltage + ESD protection, and shifted the Low/High crossover by ~500Hz.** The repo unit is V4/V4.5, so the manual in `manuals/` is the authoritative control reference below.

## 2. Controls

Six knobs, three toggles, two footswitches — a deliberately deep control set. From the manual:

- **Level.** Output volume. "Lots of volume on tap" — far past unity, which is the whole point for the intensifier role.
- **Drive.** Light grit → heavy overdrive. Per the manual, "the drive control introduces a natural high-end rolloff as it is increased, reducing harsh upper harmonics." That built-in top-end taming is exactly why it doesn't get ice-picky on a banjo at high gain.
- **Low / High.** A **James-Baxandall** pair — passive shelving filters cutting below/above a central crossover. V4.5 moved that crossover ~500Hz.
- **Mid.** A single active band of boost/cut. Crucially, it has a selectable center frequency via the **SHIFT** switch: **up = 1kHz (hi-mid), down = 300Hz (low-mid)**. This is the cut/punch control.
- **Boost knob + Boost footswitch.** A *separate front-end boost* placed **before** the distortion circuit: up to **+20dB** of gain with a **fixed 300Hz low cut**. The low cut is the tightening mechanism — it gives you "two distinct voicings for low and high gain" from one stomp.
- **DIODE toggle (clipping/compression).** The character switch:
  - **Up** — MOSFET clipping, *medium compression*, high headroom, smooth into clipping, "fairly aggressive at higher gain settings."
  - **Center** — *no diodes*, minimal compression, op-amp clipping only. "Recommended if you want high dynamic range or are using the pedal as a clean boost/EQ into an already driven amp."
  - **Down** — silicon-diode clipping, *high compression*. The tightest, most squared-off, most "wall" of the three.

(Note: older EAE marketing copy for earlier versions described the three modes as **LED / germanium / open**. The V4/V4.5 manual in this repo says **MOSFET / none / silicon** — trust the manual for this unit. Flagged as a version difference, not an error.)

EQ behavior, per the manual: "more like a studio EQ than a traditional stompbox control." Bands are fairly non-interacting, small moves are drastic — adjust gradually. Two tricks worth memorizing: **boost both Low and High = effective mid-scoop; cut both = effective mid-boost.** And "the Longsword has a great deal of low end available, so a tighter tone can be achieved by cutting the bass, particularly with an already overdriven amplifier" — directly relevant to stacking it after the Hizumitas.

## 3. Sonic Character vs Named Competitors

The Longsword is an op-amp/diode distortion, so the comparison set is RAT/OCD/Distortion+ territory, voiced bigger:

- **ProCo RAT** — the obvious ancestor. The Longsword is less midrange-honky, has dramatically more flexible EQ (the RAT has one Filter knob; the Longsword has a 3-band studio EQ plus a shift switch), and far more headroom and output. Where a RAT is one voice done well, the Longsword spans clean-boost to "massively clipped fuzz" ([Delicious Audio](https://delicious-audio.com/electronic-audio-experiments-longsword-drive/)).
- **Fulltone OCD** — similar "amp-like" ambition. The Longsword is cleaner-clipping in Center mode and bigger in the low mids; the OCD is more compressed and mid-honky by comparison.
- **MXR Distortion+** — same clipping block, vastly more refined. The Longsword is what a Distortion+ would be with a real EQ and 20dB of footswitchable boost bolted on.
- **EAE Dagger** — the in-house "lite" version. The Longsword has more low-mid punch and a fuller bottom; the Dagger is chimier and sizzlier. If you wanted the rig's wall pedal to be *smaller and brighter*, the Dagger; for *bigger and thicker*, the Longsword, which is what this rig has.

Its signature trait, in EAE's own words: "thicker low midrange content" that "fills out bright guitars." That is the single most relevant fact for a banjo/baritone rig — it adds the exact frequency band those bright sources lack.

## 4. Dynamic Behavior

The DIODE switch *is* the dynamic-response control, and it's the key to using this pedal well after a fuzz:

- **Center (no diodes)** is the high-dynamic-range, low-compression mode. Op-amp clipping only, most headroom, cleans up the most with guitar volume. This is the mode for using the Longsword as a clean-ish EQ/boost rather than a distortion.
- **Up (MOSFET)** is the middle ground — medium compression, smooth transition, gets aggressive as Drive climbs.
- **Down (silicon)** is maximum compression — squashed, squared, gated-feeling at the edges. The most "brick wall" of the three.

Note definition at high gain is helped by the Drive knob's built-in high-end rolloff and by the studio EQ — you can scoop mud (low-mid cut via Mid+SHIFT-up at 300Hz) and keep chords readable. Cleanup with the instrument volume is real but modest; this is a distortion, not a touch-overdrive (that's the Halberd's job). Threshold of clipping moves with pickup strength — the GK-5's medium-hot per-string output and the VG-800's line-level send both push it harder than a passive single-coil would, so expect to find clipping earlier on the Drive knob than the manual's clean-amp procedure implies.

## 5. Signal-Chain Placement (Board 1)

Order: `…MXR 108 → Hizumitas → Brothers AM → **Longsword** → Oxford → BF-3…`. The Longsword is the last and heaviest dirt stage before the Oxford.

- **Why it sits after Brothers AM and the fuzz wall:** this is the rig's gain ceiling. The Hizumitas already delivers a sustained Muff wall; the Brothers AM shapes/boosts it; the Longsword stacked on top is "maximum destruction." The Hizumitas dossier is explicit and **this document stays consistent with it**: *"stacking high-gain distortion after a Muff is destructive but in a good way. Expect the Longsword to over-saturate; back its gain off significantly (8–10 o'clock max) and use it as a tone-shaping stage rather than additional gain. The Hizumitas already has enough."*
- **The "back the gain off" rule, mechanically.** With a saturated Muff feeding it, the Longsword does not need its Drive. Run **Drive at 8–10 o'clock** and lean on the **EQ + Boost** instead. The pedal's real value when stacked is the studio EQ: use the Mid/SHIFT to carve a cut frequency, cut the Low to tighten the now-flubby fuzz bottom, and use the +20dB Boost (with its 300Hz low cut) as the actual "intensifier" stomp.
- **Use the DIODE switch to control stack chaos.** Into an already-saturated fuzz, **Center (no diodes)** keeps it an EQ-and-volume shove rather than piling compression on compression; **Down (silicon)** is the brick-wall maximum-destruction setting when you want the whole front end to fuse into one squared-off slab.
- **Tighten with the Low cut.** The manual's own advice — cut bass "particularly with an already overdriven amplifier" — is the antidote to the mud that a Muff + distortion stack creates. The Boost footswitch's fixed 300Hz cut does this in one stomp.
- **Standalone (fuzz off):** with the 108/Hizumitas bypassed, the Longsword is a full-range, very loud distortion in its own right — this is its native use, and where the full Drive range and all three clip modes earn their keep.
- **Oxford downstream:** per the Hizumitas dossier, by this point the Oxford is "a kill switch for nuance" — a one-button brick, not a tone shaper. The Longsword's EQ is the tone control for this whole dirt cluster; the Oxford just adds a final shove.
- **Time/mod downstream (BF-3 → Somersault → CE-2W → Deco)** all want the stable, hot, line-level wall the Longsword delivers — correct architecture.

## 6. Source-Specific Behavior

- **Banjo (Gold Tone EBM-5 + GK-5 → VG-800):** the Longsword's headline strength — "thicker low midrange content that fills out bright guitars" — is purpose-built for this. The Drive knob's natural high-end rolloff tames banjo's 2–4kHz pierce, and the Mid control (SHIFT down to 300Hz, boosted) adds the low-mid body a banjo physically lacks. This is arguably the most flattering dirt pedal in the rig for the banjo's deficiencies.
- **Baritone Jazzmaster:** home territory. EAE explicitly markets the Longsword as working "equally well with guitar, baritone, and bass" thanks to its broad frequency response ([product page](https://www.electronicaudioexperiments.com/pedals/longsword)). For baritone, watch the low end — the pedal has "a great deal of low end available," so the Low-cut/Boost-300Hz-cut tightening matters here.
- **Modeled VG-800 output:** the Longsword sees a hot, line-level summed signal, not a raw pickup. Expect it to clip earlier than the manual's passive-guitar procedure suggests; start Drive lower. Fuzzing/distorting an already-modeled cab IR is destructive in the rig's preferred "recorded-wrong" way — Center mode keeps it cleaner, Down mode obliterates it.
- **Bass (Fender Pro Jazz):** EAE and multiple [bass demos](https://www.youtube.com/watch?v=wggUREDvMUc) confirm it's genuinely bass-friendly — the broad response and 3-band EQ let you keep a clean low end under the dirt. The [TalkBass NPD thread](https://www.talkbass.com/threads/npd-electronic-audio-experiments-longsword.1271604/) is the relevant owner community for bass use.

## 7. Famous Users

EAE is boutique, and coverage reflects that — but the company is well-connected in the Boston/indie/post-hardcore scene. Per [WBUR](https://www.wbur.org/news/2024/05/07/boston-guitar-pedal-builder-electronic-audio-experiments-pile-rock-music): **Pile** (collaborated with EAE on the Mirror House), **Kal Marks**, and **Touché Amoré** (co-designed the Limelight, 2020) are documented EAE artists. These are noise-rock / post-hardcore acts, not doom or shoegaze. The Longsword specifically is EAE's flagship and widely owned, but it does **not** have a single signature artist the way the Hizumitas has Wata — there is no verified marquee-name "Longsword player." Treat any claim of a famous Longsword user with skepticism unless sourced.

## 8. Live / Power / I/O

- **Power:** 9V DC, center-negative, 2.1mm barrel. **75 mA** current draw — an order of magnitude more than the Hizumitas's 10 mA, so give it a real isolated supply slot (a low-current daisy chain slot won't do).
- **Voltage protection:** as of V4.5, an over-voltage + reverse-polarity protection circuit shuts the pedal down on reverse polarity or >9V. No batteries — cannot use them.
- **Do not exceed 9V** on V4/V4.5 (earlier V3 had a 9–18V bipolar supply; the current unit does not — the protection circuit will shut it down above 9V).
- **Bypass:** soft-touch relay, true bypass; defaults to bypass on power loss. Like the Hizumitas, **if power dies, signal still passes** (it defaults to bypass) — but the relay needs power to *engage* the effect.
- **Mono:** single in / single out. Stereo doesn't appear until the CE-2W later in the chain.
- **Input impedance ~500kΩ, output ~1kΩ** ([product page](https://www.electronicaudioexperiments.com/pedals/longsword)) — high input Z, buffer-friendly, completely happy with the CB Clean / Colour Box buffers upstream (unlike the fuzzes ahead of it).

## 9. Pairing Recommendations (This Rig)

- **After Hizumitas + Brothers AM:** the canonical wall stack. Drive low (8–10 o'clock), DIODE in **Center** for an EQ/volume shove or **Down** for the squared brick, Low cut to tame fuzz flub, Mid/SHIFT to carve a cut. Boost footswitch = the actual intensifier stomp.
- **Into the Oxford Drive:** the Longsword does the tone-shaping, the Oxford adds the final brute shove. Don't ask the Oxford to fix anything — fix it on the Longsword's EQ.
- **As a standalone wall event (fuzz off):** full Drive, MOSFET (Up) or silicon (Down) clipping, EQ to taste. This is its native, best-sounding use.
- **Banjo lead:** Drive moderate, Mid boosted at 300Hz (SHIFT down) for body, High eased back. The thick low-mid is what turns a banjo into a viable lead voice — exactly the rig's "banjo-as-lead" aesthetic.
- **Downstream into the texture/time boards:** the Longsword's stable, hot wall is ideal feed for the Microcosm, Dark Star, Generation Loss, MOOD, Blooper and H90 — same logic as the Hizumitas: a dense sustained source makes granular/tape/reverb processing sound intentional rather than choppy.

## 10. Reviews & Demos

- [EAE official Longsword product page](https://www.electronicaudioexperiments.com/pedals/longsword) — specs, version history, finishes. Start here.
- [EAE "Which EAE drive should you buy?"](https://www.electronicaudioexperiments.com/blog/2022/7/7/which-eae-drive-should-you-buy) — Longsword vs Halberd vs Dagger, in EAE's own words.
- [Pedal of the Day — Longsword Overdrive V2](https://www.pedal-of-the-day.com/2016/04/13/electronic-audio-experiments-longsword-overdrive-v2/) — early written review (V2-era).
- [Delicious Audio — Longsword Drive](https://delicious-audio.com/electronic-audio-experiments-longsword-drive/) — concise feature/character writeup.
- [Harsh Tones, Inc. — "EAE Longsword on bass & baritone guitar" (YouTube Short)](https://www.youtube.com/watch?v=xyNfbySI_ds) — baritone + bass. *(Verified via yt-dlp: channel is **Harsh Tones, Inc.**, NOT EAE's own channel — earlier draft mislabeled it "EAE.")*
- [Zachary Rizer — Model feT and Longsword bass demo (YouTube)](https://www.youtube.com/watch?v=3MNlUTg0A24) — bass stacking context (V3-era). *(Channel = **Zachary Rizer**, not EAE — verified via yt-dlp.)*
- [Andy Bassist — Longsword bass demo (YouTube)](https://www.youtube.com/watch?v=wggUREDvMUc) — third-party bass demo (V4).
- [Eirik Stordrange — Electronic Audio Experiments Longsword (demo) (YouTube)](https://www.youtube.com/watch?v=MMuV-dh53oc) — sponsored demo with EAE marketing copy. *(Channel = **Eirik Stordrange**, not EAE — verified via yt-dlp.)*
- [Demos In The Dark — Longsword full control walkthrough (YouTube)](https://www.youtube.com/watch?v=n1dBC5dpaNo) — best single control deep-dive (single-coil + humbucker).

> **V4.5 manual update:** EAE's current **Longsword V4.5 Technical Manual (Rev A, June 2025)** ships **8 named factory presets** with printed knob diagrams + descriptions (e.g. *Electrify Armament* = the no-diode/Drive-min/Boost-stomp stacking voice; *Great Weapon Fighting* = 300Hz-mid body; *Bastard Sword* = silicon-clip bass/doom wall). See `research/links/eae-manual-presets.md` and the UsageGuide §2. These supersede/expand the inferred §13 starting points below.
- [TalkBass NPD thread](https://www.talkbass.com/threads/npd-electronic-audio-experiments-longsword.1271604/) — owner discussion, bass-focused.
- [WBUR profile of EAE / John Snyder](https://www.wbur.org/news/2024/05/07/boston-guitar-pedal-builder-electronic-audio-experiments-pile-rock-music) — company background and artist roster.

## 11. Mods / Quirks / Known Issues

- **No mod target needed — it's already the modded version.** Where a stock RAT begs for a clipping/EQ mod, the Longsword ships with three clip modes and a 3-band studio EQ. The "mod" here is learning the SHIFT switch and the Boost-circuit low cut.
- **The EQ is a studio EQ, not a stompbox tone knob.** Small moves are drastic and bands are nearly non-interacting — the manual warns of this explicitly. People who dial it like a RAT Filter knob will overshoot.
- **Control-layout ergonomics.** Owner feedback (per general review consensus, e.g. [Equipboard](https://equipboard.com/items/electronic-audio-experiments-longsword)) notes the six-knob layout isn't a tidy single row; the EQ knobs aren't aligned the way some would prefer. Cosmetic, not functional.
- **Clip-mode labeling differs by version.** Earlier copy says LED/germanium/open; the V4/V4.5 manual says MOSFET/none/silicon. Don't trust a generic online spec for *your* unit's modes — trust the manual in this repo.
- **75 mA draw** is the one real gotcha — don't starve it on a shared supply.
- No widely reported reliability failures; EAE build quality is well-regarded and the V4.5 adds proper over-voltage/ESD protection.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Maker | Electronic Audio Experiments (John Snyder), Boston/Waltham MA |
| Type | Op-amp drive with diode shunt clipping (distortion) |
| Repo unit | Longsword V4 / V4.5 |
| Power | 9V DC, center-negative, 2.1mm barrel |
| Current draw | 75 mA |
| Max voltage | 9V (V4.5 protection shuts down above 9V or on reverse polarity) |
| Batteries | Not supported |
| Bypass | Soft-touch relay, true bypass; defaults to bypass on power loss |
| Input impedance | ~500 kΩ @ 1kHz |
| Output impedance | ~1 kΩ @ 1kHz |
| Controls (knobs) | Level, Drive, Low, High, Mid, Boost |
| Switches | DIODE (3-way clip/compression), SHIFT (mid 1kHz/300Hz), Boost footswitch |
| EQ | James-Baxandall Low/High shelves + active sweepable-center Mid |
| Boost circuit | Up to +20dB, front-end, fixed 300Hz low cut |
| Signal path | Analog |
| I/O | Mono in / mono out |
| Price (new) | from ~$249 |
| Warranty | EAE standard |

Source: [EAE Longsword product page](https://www.electronicaudioexperiments.com/pedals/longsword) + repo manual (`manuals/Longsword.pdf`).

## 13. Starting-Point Settings

Clock-face positions, viewed from above. Manual's day-one procedure: EQ at noon, Drive/Level at min, Boost off, all toggles up — then bring Drive/Level up to taste.

**(a) Standalone wall** — fuzz off, the rig's own distortion voice
- Drive: 1–2 · Level: 12+ · Low: 12 · High: 12 · Mid: 1 (SHIFT up, 1kHz, boosted to cut)
- DIODE: Down (silicon, max compression) · Boost: off
- The biggest, most squared-off self-contained distortion. Pull Low back to ~10 if it flubs.

**(b) Stacked-on-fuzz intensifier** — after Hizumitas + Brothers AM (the "Wall" event)
- Drive: 8–10 o'clock (backed way off — the Hizumitas has the gain) · Level: 1+
- DIODE: Center (no diodes — EQ/volume shove, not more compression) · Low: 10 (cut, tighten fuzz flub) · Mid: 1 (SHIFT up, carve a cut) · High: 12
- Boost footswitch = the actual intensifier stomp (its 300Hz cut also tightens). This is the Hizumitas dossier's "back the gain off, use as tone-shaper" setting made concrete.

**(c) Tightened doom rhythm** — palm-mute clarity at high gain
- Drive: 1 · Level: 12 · Low: 9–10 (cut) · High: 12–1 · Mid: 11 (SHIFT up, 1kHz)
- DIODE: Up (MOSFET) · Boost: on (its 300Hz cut keeps mutes defined)
- The Drive's built-in high rolloff plus the low cut keeps chugs readable instead of a mud-slab.

**(d) Banjo lead** — body and sustain for banjo-as-lead
- Drive: 11–12 · Level: 12 · Low: 12 · High: 11 (ease the pierce) · Mid: 2 (SHIFT down, 300Hz, boosted — add the body a banjo lacks)
- DIODE: Up (MOSFET, medium compression evens attack/decay) · Boost: off
- Feed a darker VG-800 amp model if still too bright. The low-mid boost is the whole trick.

## 14. Versus Alternatives — Why It Earns Its Slot

- **A second Muff / fuzz** — pointless here; the Hizumitas already owns the fuzz wall. The rig needs a *different* kind of dirt on top, and an op-amp distortion with a studio EQ is exactly the contrast that makes stacking productive rather than redundant.
- **ProCo RAT / MXR Distortion+** — same clipping family, a fraction of the control. They'd stack fine but give you one Filter knob to fight the fuzz mud; the Longsword gives you a 3-band sweepable EQ and a tightening boost. For a stack-on-fuzz tone-shaper, the EQ is the entire reason to pick this over a RAT.
- **EAE Dagger** — the in-house alternative. Smaller, brighter, less low-mid. Wrong direction for a banjo/baritone/doom rig that needs *more* low-mid mass and *more* gain ceiling, both of which the Longsword has.
- **EAE Halberd** — transistor OD, dynamics-first, soft clipping, lower gain. A beautiful pedal but the opposite job — it's a touch-sensitive boost, not a wall. Wrong tool for "maximum destruction."
- **JHS Kilt (on the bench)** — already benched in this rig precisely because "drive coverage [is] full — Brothers + Longsword + Oxford." The Longsword holds the heavy-distortion slot in that trio.

In this rig — bright banjo/baritone sources, a Muff fuzz wall immediately upstream, doom/drone/shoegaze aesthetic — the Longsword earns its slot on three counts: (1) the "thicker low midrange that fills out bright guitars" is the exact fix for banjo's missing body, (2) the studio-grade EQ + tightening boost is what turns a fuzz-plus-distortion stack from mud into a controlled brick, and (3) it has the gain ceiling and output to be the rig's definitive "wall" event when everything else is already saturated.

## Sources

- [Electronic Audio Experiments — Longsword product page](https://www.electronicaudioexperiments.com/pedals/longsword)
- [Electronic Audio Experiments — Which EAE drive should you buy?](https://www.electronicaudioexperiments.com/blog/2022/7/7/which-eae-drive-should-you-buy)
- Repo manual: `Gear/Longsword/manuals/Longsword.pdf` (*Longsword V4 Manual, Version 2, 10-Jan-21, John Snyder*)
- [WBUR — This Boston guitar pedal builder is shaping the sound of rock music](https://www.wbur.org/news/2024/05/07/boston-guitar-pedal-builder-electronic-audio-experiments-pile-rock-music)
- [Pedal of the Day — Longsword Overdrive V2](https://www.pedal-of-the-day.com/2016/04/13/electronic-audio-experiments-longsword-overdrive-v2/)
- [Delicious Audio — Electronic Audio Experiments Longsword Drive](https://delicious-audio.com/electronic-audio-experiments-longsword-drive/)
- [Equipboard — Electronic Audio Experiments Longsword](https://equipboard.com/items/electronic-audio-experiments-longsword)
- [Reverb — Electronic Audio Experiments Longsword](https://reverb.com/item/33682401-electronic-audio-experiments-longsword)
- [Perfect Circuit — Electronic Audio Experiments Longsword](https://www.perfectcircuit.com/electronic-audio-experiments-longsword.html)
- [TalkBass — NPD: Electronic Audio Experiments Longsword](https://www.talkbass.com/threads/npd-electronic-audio-experiments-longsword.1271604/)
- [EAE — Longsword on bass & baritone guitar (YouTube)](https://www.youtube.com/watch?v=xyNfbySI_ds)
- [EAE — Model feT and Longsword bass demo (YouTube)](https://www.youtube.com/watch?v=3MNlUTg0A24)
- [Longsword bass demo (YouTube)](https://www.youtube.com/watch?v=wggUREDvMUc)
- [Electronic Audio Experiments Longsword demo (YouTube)](https://www.youtube.com/watch?v=MMuV-dh53oc)
- [Guitar Pedal X — EAE Halberd V2 / Dagger V2 writeup](https://www.guitarpedalx.com/news/news/the-electronic-audio-experiments-halberd-v2-transistor-overdrive-and-dagger-v2-opamp-distortion-are-a-perfect-pair-of-versatile-fuzz-edged-pedalboard-weapons-from-the-john-snyder-armoury)
