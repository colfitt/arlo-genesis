# TKOG Oxford Drive — Deep Research

A working dossier for the **Oxford Drive** as it sits 9th on Board 1 — the *last dirt stage* before modulation, after the CB Brothers AM and EAE Longsword, before the Boss BF-3 flanger. Rig art tags it just "Drive" (an event, not always-on), and that's the right instinct: this is a British-voiced, mid-humped Shredmaster-in-a-box dropped on top of an already-saturated fuzz stack. Most of this document is about whether it earns that slot or just acts as a one-button intensifier — and, critically, **who actually makes it**, because our metadata had that wrong.

> **QC FLAG — MAKER CORRECTED.** The repo's `rig-design.html` color-codes "Oxford Drive" as a **JHS** pedal (`b-jhs` class, JHS-red left border), and the master `GearList.md` flagged the brand as ⚠️ uncertain. **It is not JHS.** The manual and the maker's own site confirm it is built by **TKOG — "The King of Gear"** (contact `thekingofgear@gmail.com`), a small New York builder that specializes in recreating Radiohead tones. The rig-art brand tag and color should be fixed (TKOG has no house color in the current CSS; it's currently borrowing JHS red). This is exactly the kind of error the deep-research pass is meant to catch.

## 1. Lineage: What It Actually Is

The Oxford Drive is **TKOG's recreation of the Marshall ShredMaster** — the 1991 high-gain British distortion most famously used by **Jonny Greenwood of Radiohead** (audible on *Pablo Honey*, including "Creep's" crunchy choruses, per [Premier Guitar's ShredMaster review](https://www.premierguitar.com/gear/reviews/marshall-shredmaster)). TKOG's [own product page](https://thekingofgear.com/oxforddrive) states it "replicates the circuit of a certain shred-tastic high-gain distortion pedal from the 1990s," and the brand exists to "re-create the sounds of famous UK rock band Radiohead." That is the whole point of the **"Oxford"** name: Radiohead formed in **Oxford, England**. This is not a Vox/AC30 reference and not a generic "UK flavor" — it's a literal Radiohead/ShredMaster homage. (Our records guessing "British-voiced because Oxford" was directionally right but for a more specific reason.)

The ShredMaster was one of a 1991 Marshall trio — Bluesbreaker, Drivemaster, ShredMaster — that superseded the late-'80s **Guv'nor** ([Marshall ShredMaster, Wikipedia](https://en.wikipedia.org/wiki/Marshall_ShredMaster)). The Oxford Drive folds the Guv'nor's DNA back in via switching:

- **'91 Voice = ShredMaster** (a "Shred-tastic distortion pedal from 1991," per the manual). The darkest, most mid-punchy voicing.
- **'88 Voice = Guv'nor** (a "Gubenatorial drive pedal from 1988" — the manual's coy spelling of *Guv'nor / Gubernatorial*). Brighter, with TKOG also re-filtering the input to tame the Guv'nor's harshness, unlike the cheap "bright switch" mods on other ShredMaster clones.
- **LED clipping mode** is itself "inspired by the LED-clipping found on Guv'nor and Drivemaster pedals," so the pedal spans the whole 1988–1991 Marshall-dirt family from one box.

**Version meaning:** The "Manual 3.09" filename is **not** a circuit version — it's the *manual revision date*, **March 9, 2024** (printed on every page footer: "Manual revision: March 9, 2024"). That's a tell about the maker: TKOG dates its manuals like a tiny one-person shop iterating on a PDF, not like a big brand with a marketing version system. The *pedal* version is **V2** (released late-2021): redesigned low-noise PCB, C0G caps (kills the earlier microphonic issue), soft-touch flexible bypass, and the added voice switch. Original Oxford Drives shipped early-2019 at $170 with only Si/LED clipping; a 2020 running change added the asym mode. The current shelf price is **~$235** ([Stomp Box Steals review](http://stompboxsteals.blogspot.com/2022/12/overdrive-tkog-oxford-drive-impressive.html)). Note: TKOG has since added a **third '01 voice** (a 2000s NYC garage-rock ShredMaster variant) to later V2 units — the owner's manual revision documents **only two voices ('91/'88)**, so this rig's unit is most likely a **two-voice V2**. Verify against the physical pedal's voice toggle (2-position = two-voice; 3-position = the later '01-equipped build).

## 2. Controls (from the manual)

Five knobs, two toggles, one soft-touch footswitch — the ShredMaster control set exactly (Gain, Bass, Contour, Treble, Volume).

- **Gain.** Distortion amount. Stock max is ~4 o'clock; the Oxford's pot has *extended range* past an original '90s ShredMaster, so there's more gain than a vintage unit on tap.
- **Bass.** Logarithmic taper. To get the bass *cut* of a normal (non-transparent) overdrive you have to run it **low, 7–9 o'clock** — counterintuitive, and the #1 thing people set wrong.
- **Contour.** **NOT a mid knob.** It's a combined treble+mid tilt. *Counter-clockwise = mid-focused, less treble*; *clockwise = mid-scooped, more treble.* Whenever you move Contour you'll need to re-trim Treble. This is the heart of the pedal's voicing.
- **Treble.** Top end, but its range is heavily dependent on where Contour sits.
- **Volume.** Unity ~noon (depends on gain + clipping mode). A **large boost** is available — be careful, especially in LED mode where output is highest.
- **Clipping toggle (3-position):** **Si** (silicon — stock, compressed, tightest), **LED** (red LEDs, higher clipping voltage → more open, louder, less compression), **asym** (one Si + one LED — asymmetric warmth with wide dynamic range; differences vs LED are clearest at medium gain).
- **Voice toggle:** **'91** (ShredMaster) / **'88** (Guv'nor) — adjusts both input and output filters.
- **Footswitch:** soft-touch relay true bypass. **Tap = latching, hold = momentary** (great for stab-style dirt bursts on noisy high-gain settings). Default on/off state is selectable by holding the switch at power-up.

## 3. Sonic Character vs Named Competitors

Which archetype? **British mid-hump distortion**, firmly *not* transparent and *not* a Tube Screamer, though it shares one trait with the TS. From the manual itself: "this pedal is not a true Marshall-In-A-Box... it is certainly Marshall-ish... it definitely can't be described as 'transparent.'" Crucially: "Just like on a popular green overdrive pedal, both the treble and bass frequencies are heavily filtered, regardless of knob positions" — i.e. it has **TS-style band-limiting** that carves a fixed mid window so it cuts a loud mix.

Placed on the usual drive axes:

- **vs Tube Screamer (TS9/808):** Both are mid-forward and band-limited, but the Oxford has **far more gain ceiling**, a darker/heavier ShredMaster grind, and a real EQ section (Bass/Contour/Treble) where the TS has one tone knob. Reach for the Oxford when you want *distortion that bites*, not a transparent push.
- **vs ShredMaster (the real thing):** The [Stomp Box Steals review](http://stompboxsteals.blogspot.com/2022/12/overdrive-tkog-oxford-drive-impressive.html) calls it "basically the old Marshall ShredMaster but with more volume and gain," praising it as "an improvement on its weaknesses without f-ing with its sound." The original ShredMaster is "naturally dark, compressed" ([Premier Guitar](https://www.premierguitar.com/gear/reviews/marshall-shredmaster)); the Oxford keeps that and adds headroom + clipping options.
- **vs Guv'nor:** The '88 voice covers this — brighter, slightly looser, classic amp-in-a-box crunch, but with TKOG's input re-filtering removing the harsh top the original Guv'nor was known for.
- **vs Marshall-in-a-box pedals (Wampler Plexi-Drive, Lovepedal Eternity, JHS Charlie Brown):** Those chase *plexi/JTM amp* character. The Oxford chases a *ShredMaster pedal*, which is a more compressed, more scooped-or-humped, more "'90s alt-rock" voice — closer to the records the owner's aesthetic references than a vintage-amp clone.

The standout claim for THIS rig: the manual notes the heavy filtering "makes the pedal sound good with synthesizers and other instruments with rich harmonic overtones, since it prevents the distortion from becoming harsh and buzzy even with complex inputs." That is directly relevant to a VG-800 / hex-divided front end (see §6).

## 4. Dynamic Behavior (cleanup, stacking)

- **Compression:** Si mode is the most compressed/tightest; LED is the most open and dynamic with the most output; asym sits between with the widest dynamic range. For cleanup-by-guitar-volume, **LED or asym** track your picking hand best.
- **Cleanup:** Reasonable for a high-gain box but not Fuzz-Face-grade. Rolling guitar volume back thins it toward edge-of-breakup, especially in LED mode. It's more a "set the character" pedal than a "ride the volume knob" pedal.
- **Stacking — the key question for this rig:** The manual is blunt that this circuit was *designed for a clean Fender-style amp* (ideally solid-state) for "extremely focused tone with a lot of definition," and warns: "you'll probably want to lower both the gain and the bass if you're pushing dirty amps or **other dirt pedals** into heavier distortion." That is the operative instruction here — see §5. Stacked into existing saturation, its TS-like fixed-mid filter dominates and it stops behaving like an EQ and starts behaving like a brick.

## 5. Signal-Chain Placement — Its Role This Late in THIS Rig

Board 1 dirt order: `… MXR 108 → Hizumitas → Brothers AM → Longsword → **Oxford Drive** → BF-3 → Somersault → CE-2W → Deco`. The Oxford is the **fifth dirt stage**, sitting *after* a silicon Fuzz Face, a Big-Muff-derivative fuzz, a drive platform, and a high-gain wall — with *no amp to push*, just the BF-3 flanger downstream.

Stay consistent with the **Hizumitas dossier's** read, which I'll refine rather than overturn: that dossier says "the Oxford's mid character will be doing nothing useful at this point in the chain; consider it a 'kill switch for nuance' that turns the whole front-end into a single brick. Useful as a one-button intensifier, not as a tone shaper here." **That is correct, and the Oxford's own manual explains *why*:** its band-limiting filter sets a fixed mid window regardless of knob position. When everything upstream is already saturated and broadband, dropping a fixed-mid, heavily-filtered distortion on top collapses all that texture into the Oxford's one voice. You lose the Hizumitas Tone sweep, the Longsword's wall detail, the Brothers' blend — it all gets re-filtered into a ShredMaster honk.

So its honest role here is a **momentary intensifier / "section" switch**, not a tone-sculpting stage:

- **Use the momentary footswitch.** Hold-for-burst is the right mode for this slot — kick the whole front end into a single denser brick for a chorus or a peak, release back to the nuanced stack. The manual literally recommends momentary "for short bursts of distortion... with a high gain sound with a lot of noise."
- **Run it LOW-gain.** Per the manual's stacking warning, **gain 8–10 o'clock and bass 7–9 o'clock**. At this position you don't need more saturation — you need a bit of mid-focus and a volume bump to shove the stack into the BF-3 harder. Treating it as a clean-ish mid+level boost is the only way it adds rather than erases.
- **Into the BF-3:** a hotter, more mid-focused signal makes the flanger's sweep more dramatic and metallic — the jet-whoosh reads better over a focused brick than over a broadband fuzz mush. That's a genuine reason to have *a* level/mid stage right before the BF-3.
- **Better placement?** If you want the Oxford to actually *shape* tone, it belongs **earlier** — before the Hizumitas/Longsword, used as a ShredMaster *base distortion* that the fuzzes pile onto (the manual: "place it prior to any dedicated distortion pedals"). As wired, accept it as an event switch, not a voice.

## 6. Source-Specific Notes (banjo, baritone, VG-800, bass)

- **VG-800 / modeled + hex-divided source:** This is the Oxford's most defensible reason to exist in this rig. Its fixed input/output filtering specifically "prevents the distortion from becoming harsh and buzzy even with complex inputs" (manual) — exactly the failure mode of distorting a synthetic, harmonically-dense VG-800 patch. Where a Muff or Fuzz Face turns a modeled pad/COSM patch into fizz, the Oxford's band-limiting keeps it musical. The **'88 (Guv'nor) brighter voice + LED clipping** is the cleanest, most articulate combo for modeled signal.
- **Gold Tone EBM-5 banjo (GK-5 → VG-800):** The banjo's piercing 2–4 kHz transient spray is the enemy. Run **'88 voice, Contour low (mid-focused / less treble), Treble well down, Bass low** — let the inherent filtering eat the ice-pick. Low gain; you want focus, not more fizz on an already-bright source.
- **Baritone Jazzmaster:** Home territory for a ShredMaster. The '91 voice and its low-mid punch suit the baritone's range. Mind the **logarithmic Bass knob** — keep it low or the baritone's bottom turns to mud, especially stacked.
- **Bass (Fender Jazz Bass):** Not a bass-specific circuit; the heavy bass filtering thins low end. Usable for a gnarly distorted bass *texture*, not for clean low-end retention. If you need bass dirt with body, the Brothers AM or Colour Box is the better tool — keep the Oxford for grind/texture.

## 7. Famous Users (honest)

The Oxford Drive itself is a small-batch boutique pedal with **no documented marquee artist users** — TKOG sells it largely on the *tone it replicates*, not a roster. The relevant fame is the **circuit it clones**: the Marshall ShredMaster, used by **Jonny Greenwood (Radiohead)** on '90s records ([Wikipedia](https://en.wikipedia.org/wiki/Marshall_ShredMaster), [Premier Guitar](https://www.premierguitar.com/gear/reviews/marshall-shredmaster)). The broader (frequently-repeated) ShredMaster-family list includes Thom Yorke and Ed O'Brien (Radiohead), Kevin Shields (My Bloody Valentine), and Alex James (Blur) — though some of those attributions are loose and only Greenwood is consistently confirmed by primary review sources. Treat "famous Oxford Drive users" as **a ShredMaster legacy, not an Oxford Drive discography**.

## 8. Live / Power / I/O Notes

- **Power:** 9V DC, 2.1mm **center-negative** (Boss-style), **~8 mA** draw. No battery option. Works on a daisy-chain but TKOG recommends isolated supply for noise. Trivial load for any isolated slot.
- **Bypass:** Soft-touch **mechanical-relay true bypass** (tap = latch, hold = momentary). Relay-based, so behavior on total power loss is the usual relay caveat — don't assume signal passes if power dies mid-set.
- **I/O:** Mono in / mono out, **top-mounted jacks** (pedalboard-friendly). Matches the rig's mono Board-1 dirt section (stereo only begins at the CE-2W).
- **Enclosure:** 1590B-style. **60mm W × 115mm D × 53mm H** with knobs. Compact — small footprint for five knobs + two toggles.

## 9. Pairing Recommendations (using THIS rig's gear by name)

- **After Brothers AM / Longsword (as wired):** Accept the intensifier role. Best partner setting: Oxford at low gain, '91 voice, Si clipping, as a momentary mid+level shove. Let the **Brothers AM** do the actual EQ shaping (its blendable channels reach mids the Oxford's fixed filter can't), and use the Oxford only to *commit* the stack to a denser state on cue.
- **Into the BF-3 (immediately downstream):** This is the one pairing that genuinely benefits. A focused, hotter, mid-present feed makes the BF-3's flange more vocal and metallic. Keep Oxford **bass low** so the flanger isn't sweeping mud.
- **Reconsidered placement — before the fuzzes:** If you'd rather it earn a tonal role, move it ahead of the **Hizumitas** to act as a ShredMaster foundation that the MXR 108 and Hizumitas stack onto. The manual explicitly endorses placing it "prior to any dedicated distortion pedals." This is the single most impactful change available if the current slot feels redundant.
- **Downstream texture (End Board):** Like the Hizumitas, a sustained, focused Oxford brick gives the **Microcosm / Chroma Console / Blooper / MOOD MkII** a stable, dense source to granulate and loop — its lack of broadband fizz actually makes it a *cleaner* granular input than the fuzzes.
- **Avoid:** stacking it for *more gain* on top of the Longsword. You have enough saturation; adding the Oxford's gain just gates and squares everything off. Use it for focus/level only.

## 10. Reviews & Demos (real links)

- [TKOG Oxford Drive — official product page](https://thekingofgear.com/oxforddrive) — maker's full feature/voicing breakdown; the authority on what it clones.
- [Stomp Box Steals — TKOG Oxford Drive review](http://stompboxsteals.blogspot.com/2022/12/overdrive-tkog-oxford-drive-impressive.html) — "basically the old Marshall ShredMaster but with more volume and gain"; lists $235; best plain-language tone writeup.
- [Joe Edelmann — "Shreddy or Not, Here It Comes: TKOG Oxford Drive v2"](https://www.youtube.com/watch?v=wPHLQfGufps) — the V2-specific demo with the new voice/bypass features.
- [Mike Hermans — TKOG Oxford Drive](https://www.youtube.com/watch?v=UkPeC4_sL9U) — clean high-production playthrough. *(Verified via yt-dlp: channel is **Mike Hermans**, NOT collector//emitter — earlier draft mis-credited it.)*
- [Joe Edelmann — "The ShredMaster Shootout!" original 90s Marshall vs reissue vs TKOG Oxford Drive](https://www.youtube.com/watch?v=nlx69O9y-zY) — the most useful A/B; includes Greenwood's quoted setting (channel = **Joe Edelmann**, verified).
- [collector//emitter — TKOG Oxford Drive + Filter prototype, Stompbox Exhibit 2019](https://www.youtube.com/watch?v=MkZDi-7vg5A) — historical, shows the original 2019 unit (this is the genuine **collector//emitter** video).
- [Marshall ShredMaster review — Premier Guitar](https://www.premierguitar.com/gear/reviews/marshall-shredmaster) — context on the cloned circuit and the Greenwood/"Creep" association.

## 11. Mods / Quirks / Known Issues

- **Early-unit oscillation:** The *first* 2019 Oxford Drives could oscillate at high gain+volume due to bypass-switch wiring; re-wiring fixed it. The **V2 in this rig is past that** (redesigned PCB).
- **Microphonics:** Some early units were microphonic; **V2's C0G caps eliminate this.** Non-issue here.
- **Counterintuitive Bass knob:** Logarithmic — you must run it *low* (7–9 o'clock) for normal-overdrive bass cut. People leave it too high and get mud, especially stacked.
- **Contour is not a mid knob** — the most common dial-in mistake. Moving Contour forces a Treble re-trim every time.
- **Output is hot in LED mode** — large available boost; easy to slam the BF-3 (or Apollo, if ever run direct) too hard.
- **Serviceability:** V2 footswitches use a **JST connector — replaceable by hand, no soldering.** Good for a touring board.
- **No known reliability problems** on V2; standard small-shop boutique build.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Maker | **TKOG — The King of Gear** (NOT JHS; metadata corrected) |
| Circuit | Marshall ShredMaster ('91) + Guv'nor ('88) recreation |
| Pedal version | V2 (late-2021); manual rev. March 9, 2024 |
| Controls | Gain, Bass, Contour, Treble, Volume |
| Switches | Clipping (Si / LED / asym) · Voice ('91 / '88; later units add '01) |
| Power | 9V DC, center-negative, 2.1mm (Boss-style) |
| Current draw | ~8 mA |
| Battery | None |
| Bypass | Soft-touch relay true bypass (tap = latch, hold = momentary) |
| I/O | Mono in / mono out, top-mounted jacks |
| Enclosure | 1590B-style |
| Dimensions | 60 × 115 × 53 mm (W×D×H, with knobs) |
| MIDI / Expression | None |
| Price (V2) | ~$235 USD |

Sources: [TKOG product page](https://thekingofgear.com/oxforddrive); Oxford Drive Manual rev. March 9, 2024 (in repo).

## 13. Starting-Point Settings (clock-face)

Adapted from the manual's recommended settings, biased toward THIS rig's stacked, modeled-source, doom/shoegaze use.

**(a) Stack Intensifier** — the honest job in the current slot; momentary burst into the BF-3
- Voice: '91 · Clipping: Si · Gain: **9** · Bass: **8** · Contour: **10** (mid-focused) · Treble: **11** · Volume: **1–2**
- Hold the footswitch for the burst; low gain so it focuses + boosts rather than re-saturates.

**(b) Low-Gain Ambient / Shoegaze** (manual's own shoegaze patch) — for the rare "Oxford as base drive" experiment ahead of the fuzzes
- Voice: '91 · Clipping: Si · Gain: 3 o'clock · Bass: 11 · Contour: 12 · Treble: 2 o'clock
- Best with dynamic arpeggios/chords into delay/reverb. Move it *before* the Hizumitas to use this.

**(c) Modeled-Source Tamer** — for VG-800 / banjo, where filtering earns its keep
- Voice: **'88** (brighter, input-refiltered) · Clipping: LED · Gain: **10** · Bass: **8** · Contour: **9** (mid-focus, treble pulled) · Treble: **10**
- Kills VG-800/banjo fizz; keeps complex patches musical. Lowest-gain, most-articulate setting.

**(d) Classic Green/Yellow OD** (manual's "Classic Green Overdrive") — if you ever want it as a transparent-ish TS-style push
- Voice: '88 · Clipping: Si (or asym for "yellow") · Gain: 12 · Bass: 9 · Contour: 9 · Treble: 3 o'clock

## 14. Versus Alternatives — Does It Earn Its Slot?

**Honest verdict, consistent with the Hizumitas dossier's skepticism: in its *current* position it is largely redundant as a tone-shaper.** As the fifth dirt stage with no amp to push, its defining feature — a fixed-mid ShredMaster filter — fights the nuanced fuzz wall it sits on top of, collapsing texture into one honk. The Hizumitas dossier's "kill switch for nuance / one-button intensifier" framing is accurate, and the Oxford's own manual ("lower gain and bass when pushing other dirt pedals") confirms it was never designed to be stacked fifth.

It earns its place only under one of two conditions:

1. **As an event/intensifier**, used momentary at low gain to commit the stack to a denser state before the BF-3 — a *function*, not a tone. Defensible, and the soft-touch momentary switch makes it ergonomically ideal for it.
2. **Relocated before the fuzzes**, where it becomes a genuine ShredMaster *base distortion* — the one move that turns it from redundant to foundational, and the one the manual explicitly blesses.

Against alternatives the owner already has or could bench: the **Brothers AM** is the better tone-shaper at this point in the chain (real blendable EQ vs the Oxford's fixed filter); the benched **JHS Kilt** would be more redundant still (rig art literally notes "Drive coverage full — Brothers + Longsword + Oxford"). What the Oxford uniquely offers no other pedal in this rig does is the **specific Radiohead/ShredMaster voice** — and for an owner whose aesthetic leans Radiohead-adjacent doom/shoegaze, *that voice* is the reason to keep it, even if the current slot underuses it. **Recommendation: keep it, but move it ahead of the Hizumitas, or commit to using it strictly as a momentary section-switch.** Standing pat as an always-available fifth tone-stage is the worst of the three options.

## Sources

- [The King of Gear — Oxford Drive (official product page)](https://thekingofgear.com/oxforddrive)
- TKOG Oxford Drive User's Manual, revision March 9, 2024 (PDF in repo: `Gear/Oxford Drive/manuals/Oxford Drive Manual 3.09.pdf`)
- [Stomp Box Steals — TKOG Oxford Drive review ($235, "old Marshall ShredMaster with more volume and gain")](http://stompboxsteals.blogspot.com/2022/12/overdrive-tkog-oxford-drive-impressive.html)
- [Premier Guitar — Marshall ShredMaster review (Greenwood / "Creep" / dark-compressed voicing)](https://www.premierguitar.com/gear/reviews/marshall-shredmaster)
- [Wikipedia — Marshall ShredMaster (1991, controls, Guv'nor/Drivemaster trio, Greenwood)](https://en.wikipedia.org/wiki/Marshall_ShredMaster)
- [Guitar Player — Marshall reissues the Guv'nor / Bluesbreaker / Drivemaster / ShredMaster](https://www.guitarplayer.com/news/we-copied-them-exactly-marshalls-steve-smith-introduces-the-new-guvnor-bluesbreaker-drivemaster-and-shredmaster-reissues)
- [Joe Edelmann — TKOG Oxford Drive v2 demo (YouTube)](https://www.youtube.com/watch?v=wPHLQfGufps)
- [collector//emitter — TKOG Oxford Drive demo (YouTube)](https://www.youtube.com/watch?v=UkPeC4_sL9U)
- [The ShredMaster Shootout — 90s Marshall vs reissue vs TKOG Oxford Drive (YouTube)](https://www.youtube.com/watch?v=nlx69O9y-zY)
- [TKOG Oxford Drive + Filter prototype, Stompbox Exhibit 2019 (YouTube)](https://www.youtube.com/watch?v=MkZDi-7vg5A)
- [Reverb — The King of Gear (TKOG) Oxford Drive listings](https://reverb.com/item/28347721-the-king-of-gear-tkog-oxford-drive-pedal-fast-free-shipping-in-u-s)
- [Equipboard — TKOG Oxford Drive](https://equipboard.com/items/the-king-of-gear-oxford-drive)
