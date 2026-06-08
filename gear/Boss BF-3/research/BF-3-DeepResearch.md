# Boss BF-3 Flanger — Deep Research

A working dossier for the BF-3 as it actually lives in Board 1: 10th in line, the FIRST modulation pedal after the entire dirt stack (108 → Hizumitas → Brothers AM → Longsword → Oxford). Its job here is not flanging a clean Strat — it's flanging a dense, saturated, sustained fuzz-wall, which is a fundamentally different (and harsher) task than every demo video you'll find of this pedal. It's also stereo in/out sitting in a *mono* part of the chain (the stereo split doesn't happen until the CE-2W two pedals downstream), so half of what makes the BF-3 special — the Gate/Pan rotation — is dead weight where it currently sits. This document is mostly about those two facts.

## 1. Lineage: BF-1 → BF-2 → BF-3

Boss's flanger line runs BF-1 (1977, the large two-knob box), BF-2 (1980–2001), and BF-3 (February 2002–present). The BF-2 is the famous one: an **all-analog BBD (bucket-brigade delay) flanger** that ran for ~20 years with only a single notable op-amp change, prized for warm, lush, "liquid" sweeps ([MaxxMusic Boss flanger rundown](https://maxxmusicstore.com.au/blogs/news/boss-flangers), [CraveGuitars BF-2 feature](https://www.craveguitars.co.uk/home/features/effects/feature-1981-boss-bf-2-flanger/)).

The BF-3 broke from that. The headline technical shift is that the BF-3 is **digital** — it abandons the BBD chip for DSP ([MaxxMusic](https://maxxmusicstore.com.au/blogs/news/boss-flangers), [TalkBass BF-2 vs BF-3 thread](https://www.talkbass.com/threads/boss-bf-2-bf-3-what-the-hell-is-the-difference.292129/)). That swap is *the* point of contention among BF-2 loyalists: the BF-3 is more versatile and arguably "thicker," but it trades the BBD's analog grain for digital cleanliness. For this rig that trade is largely moot — you're feeding it a fuzz wall, not a pristine clean tone, so the BF-3's relative sterility is buried under saturation before the flanger ever touches it. The DSP also enabled the features the BF-2 couldn't do: two new modes (Ultra, Gate/Pan), a Momentary mode, tap-tempo via the pedal, and independent guitar/bass inputs with stereo outs ([Boss US BF-3 page](https://www.boss.info/us/products/bf-3/)).

## 2. Controls & the Four Modes

Four knobs — **MANUAL, RES, DEPTH, RATE** — plus a **MODE** selector and the footswitch ([BF-3 owner's manual](manuals/BF-3_M_eng03_W.pdf)).

- **MANUAL** — sets the center frequency where the flange sweep is applied; range rises clockwise. Note: the MANUAL knob **does nothing when DEPTH is fully clockwise** (max depth overrides it). Its range also shifts when you use the BASS IN jack.
- **RES (Resonance)** — feedback/regeneration. The metallic, hollow, "jet" intensity. Clockwise = stronger, more emphasized, more characteristic flange. This is the knob that turns the effect from subtle to ridiculous.
- **DEPTH** — sweep depth. How far the comb-filter notch travels.
- **RATE** — sweep speed.

**MODE** selects four behaviors ([owner's manual](manuals/BF-3_M_eng03_W.pdf), [Boss US](https://www.boss.info/us/products/bf-3/)):

- **STANDARD** — normal flanger.
- **ULTRA** — a stronger, "ultra-fat" flange with more edge than Standard. This is the BF-3's signature trick — a more aggressive, hollow, scooped voicing the BF-2 couldn't produce.
- **GATE/PAN** — *in mono*, it creates radical output-volume changes (a slicer/tremolo-with-swirl). *In stereo*, it alternately pans L/R for a rotary/Leslie-like spin. The gate switches on/off 32 times over one full flanger rise-and-fall cycle.
- **MOMENTARY** — flange applies **only while the footswitch is held**, using the Standard voicing, with flanging starting in the low end. You cannot tap-tempo in this mode.

**Tap-tempo ("Momentum"):** Hold the footswitch for ≥2 seconds and the CHECK indicator blinks red/green; tap the beat and the RATE syncs to tempo (sync range 0.1–18 sec per cycle). Touching the RATE knob afterward returns control to the knob. **Caveat to flag:** the term *"Momentum"* does not appear anywhere in Boss's official copy or the manual — Boss calls it "Tap tempo adjustable via pedal" and treats *Momentary* as a separate mode ([Boss US](https://www.boss.info/us/products/bf-3/)). "Momentum" looks like community/marketing shorthand; I could not verify it as an official BF-3 term.

**Guitar vs Bass inputs:** Two physically separate input jacks. BASS IN is disabled when GUITAR IN is plugged. Both jacks double as the power switch (plugging in turns the unit on — unplug when not in use or you'll drain the battery). The BASS IN path shifts the MANUAL frequency range and is voiced to preserve low end ([owner's manual](manuals/BF-3_M_eng03_W.pdf)).

## 3. Sonic Character vs Other Flangers

The BF-3's defining trait versus the boutique/vintage flanger world is **range plus digital headroom**, not warmth.

- **vs MXR M117 / EVH Flanger** — The MXR is the "Unchained" jet-sweep gold standard: analog, lush, one perfect sound. The BF-3 in Standard gets in the ballpark but sounds slightly cleaner/glassier; where it pulls ahead is Ultra (more extreme than the MXR can go) and the slicer/pan modes the MXR doesn't have.
- **vs EHX Electric Mistress / Deluxe Electric Mistress** — The Mistress is the Andy Summers "watery, barely-there chorus-flange" voice and the filter-matrix freeze trick. The BF-3 is more clinical and more aggressive; it does not do the Mistress's gauzy shimmer as convincingly, but it's far more flexible and quieter.
- **The "Ultra" extreme** — This is the reason to own a BF-3 over a one-trick analog flanger. Ultra is hollow, metallic, scooped, and borderline ring-mod at high RES. For drone/doom it's the useful setting: it doesn't sound "classic rock," it sounds *broken*.
- **Metallic vs subtle** — RES is the whole story. Low RES + slow RATE = subtle movement, almost a slow phaser. High RES = the screaming-comb-filter jet. The BF-3 covers that entire arc on one pedal, which is rare.

It is a *digital* flanger and reviewers consistently note that, while versatile, it has a "warm enough" but ultimately cleaner timbre than the BF-2 ([Tonepedia BF-3 review](https://www.tonepedia.com/catalog/effects-and-pedals/flanger/bf-3-flanger/), [Rex and the Bass review](http://www.rexbass.com/2014/09/boss-bf-3-flanger-effect-pedal-review.html)).

## 4. Behavioral Notes — Flanging a Saturated, Sustained Signal

This is the crux for this rig, and it's the opposite of how the pedal is usually demoed.

- **Flanging a fuzz wall is louder and more violent than flanging a clean signal.** A flanger is a comb filter: it sweeps notches through the spectrum. On a clean note you hear a gentle whoosh. On a *sustained, harmonically dense fuzz wall* (Hizumitas + Longsword + Oxford), those notches are cutting through a continuous spectrum packed with harmonics, so the sweep becomes a dramatic, vocal, almost *talking* movement across the whole wall. This is the single best argument for the BF-3 in this slot — a sustained fuzz drone is the ideal source for flanging because there's always signal present for the notches to chew on.
- **RES runaway / self-oscillation** — High RES on a hot, sustained input pushes the regeneration loop hard. Expect the resonant peak to scream and, at extreme settings, to approach self-oscillation against the fuzz's own feedback. With the doom aesthetic this is a feature, but it's *additive* gain — watch your output into the Somersault/CE-2W, because a flanged fuzz wall at high RES is a level spike.
- **Notch interaction with fuzz harmonics** — Because fuzz generates strong odd harmonics, the comb notches sometimes land on and cancel fundamental energy, producing a hollow, gated "ULTRA"-style scoop even in Standard mode. Embrace it for "recorded-wrong" textures; back off DEPTH if the wall thins out too much.
- **Slow + shallow = the safe, musical setting on a wall.** For a sustained drone you usually want RATE low, DEPTH moderate, RES low-to-medium — slow movement that keeps the wall intact. Fast/deep/high-RES is the chaos setting.

## 5. Signal-Chain Placement — Flanging the Fuzz Wall Here

Current order: `… Oxford Drive → **BF-3** → Caroline Somersault → Boss CE-2W (stereo split) → Deco V2`.

- **After all the dirt is the correct, conventional placement.** Flanger-after-distortion makes the sweep "richer and more pronounced because the flanger is modulating an already-distorted signal" ([PedalPlayers: flanger before/after distortion](https://pedalplayers.com/flanger-before-or-after-distortion/)). For a fat, obvious jet on the wall, leave it where it is.
- **The "before the dirt" alternative is worth a real experiment.** Putting a flanger *in front of* distortion yields the classic thick, chewy, "jet-like phasing" that's more integrated and less surgical ([Traveling Guitarist](https://travelingguitarist.com/flanger-signal-chain-placement/), [PedalPlayers](https://pedalplayers.com/flanger-before-or-after-distortion/)). Because the BF-3 is buffered with a 1MΩ input, it's electrically *fine* in front of the fuzzes — but the MXR 108 is a Fuzz Face derivative that wants to see a guitar/high impedance, and a buffered flanger in front of it can make it spit and thin out. If you try BF-3-before-108, expect gated splatter (which may be exactly your aesthetic). Practically: keep it after the dirt for predictability, move it pre-fuzz only as a deliberate "broken" patch.
- **The mono-vs-stereo reality — this is the big one.** Board 1 is **mono** until the CE-2W performs the stereo split *two pedals downstream*. The BF-3's stereo outputs and, critically, its **Gate/Pan rotary mode are wasted here** — in mono, Gate/Pan collapses to a volume-slicer tremolo, not the L/R Leslie swirl that's the mode's whole appeal. You're paying for a stereo flanger and using it in mono.
  - **Should it move?** Two honest options: (1) **Leave it.** Its real job here is mono Standard/Ultra flange on the wall, and that works fine. (2) **Relocate the BF-3 downstream of the CE-2W split** (e.g., onto Board 2 or in a stereo loop) if you want Gate/Pan's rotation — but that strands it among the deep texture/granular pedals where its flange will fight the Microcosm/Dark Star, and you'd lose the "flange the dirt directly" benefit. My read: keep it on Board 1 in mono and accept that Gate/Pan is a bonus you won't use much. If stereo rotary flange genuinely matters to a part, that's a re-patch decision, not a permanent move.
- **Into the Somersault** — feeding a flanged signal into the Somersault's lo-fi vibrato/chorus stacks two modulations. Slow, shallow BF-3 + Somersault can get gorgeously seasick; fast BF-3 + Somersault is mush. Pick one to be the "lead" modulation.

## 6. Source-Specific Notes

- **Baritone Jazzmaster wall (magnetic + VG-800):** Home turf. The baritone's low fundamental plus a sustained fuzz wall gives the BF-3's notches enormous spectral content to sweep. Standard or Ultra, slow RATE, moderate DEPTH. Watch the low-end notch cancellation — on a baritone, a deep notch can briefly gut the fundamental.
- **Banjo lead (Gold Tone EBM-5 + GK-5 → VG-800):** Banjo is bright, transient, and fast-decaying. By the time it's a Hizumitas-sustained wall, it behaves like guitar and flanges well; but a *clean-ish* banjo lead into the BF-3 will sound thin and metallic (the notches accentuate the banjo's already-piercing 2–4 kHz). Use low RES and shallow DEPTH on exposed banjo, or only engage the flanger once the part is sitting in the saturated wall.
- **Modeled VG-800 signal:** The BF-3 is digital and sits after the VG-800's summed (non-divided) output, so it flanges whatever model the VG-800 sends — modeled cab IR, synth pad, GR-style patch. Flanging a VG-800 synth pad is one of the better drone tricks available here: a continuous pad gives the comb filter unlimited material and the result is a slow, evolving, rotor-like wash. Polyphonic guitar-synth patches will artifact under high RES — on aesthetic, that's a feature.
- **Jazz bass via the BASS IN jack:** This is the under-used asset. The dedicated BASS IN re-ranges MANUAL and is voiced to **retain low end**, which a guitar-input flanger famously eats ([TalkBass BF-3 thread](https://www.talkbass.com/threads/boss-bf-3-flanger.47492/), [BassChat BF-3](https://www.basschat.co.uk/topic/173795-boss-bf-3-flanger/)). If the Jazz bass ever runs through Board 1, plug into BASS IN specifically — you'll keep the bottom that GUITAR IN thins out. Note BASS IN is disabled whenever GUITAR IN is occupied, so this is an either/or repatch, not simultaneous.

## 7. Famous Users (honest)

Flangers have a strong signature-sound mythology, but most of it predates and bypasses the BF-3 specifically:

- **Eddie Van Halen — "Unchained"** used an **MXR Flanger** (commonly cited as the M117), not a BF-3 — the sweep-up/sweep-down riff trick ([GuitarPlayer: Unchained isolated](https://www.guitarplayer.com/players/eddie-van-halen-unchained-guitar-isolated)).
- **Heart — "Barracuda"** used a kit-built Phoenix Systems flanger, not a Boss ([Stompbox Book: Forever Flanged](https://stompboxbook.com/forever-flanged-10-great-flanger-powered-tracks-pedal-playlist/)).
- **Andy Summers (The Police)** used an **EHX Electric Mistress**, set subtle/chorus-like ([Guitar World: Andy Summers tone](https://www.guitarworld.com/gear/tonal-recall-the-police-andy-summers)).

The honest verdict: the **BF-3 itself has no single iconic record** the way those analog units do — it's a workhorse on countless boards (it's one of the best-selling flangers ever) but it isn't a signature-tone pedal. Don't buy it for someone else's sound; buy it for its mode flexibility. I could not verify any marquee artist whose defining flange is specifically a BF-3.

> Note (lineage): the one Boss flanger with a famous record is the **analog BF-2** — **Robert Smith / The Cure, "A Forest."** Other canonical flanges are non-Boss: MXR M117 (Van Halen "Unchained"; McGeoch/Siouxsie "Permafrost"), Phoenix Systems kit (Heart "Barracuda"), EHX Electric Mistress (Andy Summers, Gilmour, Lifeson), Tycobrahe (Geezer Butler "E5150"). The BF-3 is conspicuously absent from that canon — which is exactly why its case is *flexibility + placement*, not a borrowed tone.

## 8. Live / Power / I/O Notes

- **Power:** 9V DC center-negative, 2.1mm barrel (Boss PSA series) or internal 9V battery. **Current draw 60 mA** per the [official Boss spec page](https://www.boss.info/global/products/bf-3/specifications/) and the [owner's manual](manuals/BF-3_M_eng03_W.pdf). Several third-party sites list 40 mA — that figure is **wrong**; trust Boss's 60 mA. Battery life ~4 hrs continuous (digital pedals are thirsty — run it off the isolated supply, not a battery).
- **The input jacks are the power switch.** Plugging into GUITAR IN or BASS IN powers the unit; unplug to power down. On a permanently patched board this is irrelevant, but it means a half-inserted patch cable = no power.
- **I/O:** GUITAR IN, BASS IN, OUTPUT A (MONO), OUTPUT B. 1MΩ input impedance, 1kΩ output impedance, ≥10kΩ recommended load. Stereo out via A+B; mono via A only — which is how it's wired in this rig.
- **Expression/external:** The GearProfile lists "expression: true," but the BF-3 has **no expression jack and no external footswitch jack** — tap-tempo is done on the unit's own footswitch ([owner's manual](manuals/BF-3_M_eng03_W.pdf)). That profile field appears to be a metadata error; I could not find any BF-3 expression-pedal support to verify it.
- **Bypass:** **Buffered bypass** (standard Boss FET switching), confirmed on the [official spec page](https://www.boss.info/global/products/bf-3/specifications/). Not true bypass. See §11 for the tone-suck debate.

## 9. Pairing Recommendations (this rig, by name)

- **Before it — the dirt stack (108 / Hizumitas / Brothers AM / Longsword / Oxford):** This is the BF-3's reason to exist here. A sustained Hizumitas/Longsword wall is the *ideal* flanger source. Keep the BF-3 last in the dirt chain; let the wall feed it.
- **Caroline Somersault (immediately after):** Stack carefully. BF-3 slow/shallow → Somersault chorus = lush, drifting, oceanic. BF-3 fast → Somersault = soup. Use one as the dominant motion.
- **Boss CE-2W (the stereo split):** The CE-2W is where mono becomes stereo. A mono BF-3 flange into a stereo CE-2W chorus is a classic doubled-modulation wash. If you ever want stereo *flange*, this is the boundary you'd need to cross by re-patching the BF-3 after the CE-2W.
- **Redundancy with the End Board — be honest:** Board 3 has the **Chroma Console** (which includes flanger/vibrato-class modulation), the **H90** (every modulation algorithm Eventide makes, including flangers and ModFactor-derived sweeps), and the **MOOD MkII**. The H90 and Chroma Console can both produce flange *better and in stereo* than the BF-3. So the BF-3 is **partially redundant** — its unique value is (a) flanging the dirt *directly at the source*, pre-everything, which the End Board can't do, and (b) the immediacy of a footswitchable analog-feeling Ultra flange you don't have to menu-dive for. If you only ever wanted occasional stereo flange on the final wash, the H90 already covers it and the BF-3 is justified mainly by the pre-fuzz, in-the-wall placement. That's the real argument for its slot.

## 10. Reviews & Demos (real links)

- [Boss US — BF-3 product page](https://www.boss.info/us/products/bf-3/) — official mode descriptions.
- [Boss Global — BF-3 specifications](https://www.boss.info/global/products/bf-3/specifications/) — authoritative spec sheet (60 mA, buffered bypass).
- [Tonepedia — BF-3 sound review](https://www.tonepedia.com/catalog/effects-and-pedals/flanger/bf-3-flanger/) — detailed mode-by-mode breakdown.
- [Guitar Chalk — BF-3 review](https://www.guitarchalk.com/boss-bf-3-review/) and [BF-3 settings cookbook](https://www.guitarchalk.com/boss-bf-3-flanger-settings/) — practical starting settings.
- [Rex and the Bass — BF-3 review](http://www.rexbass.com/2014/09/boss-bf-3-flanger-effect-pedal-review.html) — best on the bass input and low-end retention.
- [TalkBass — BF-3 thread](https://www.talkbass.com/threads/boss-bf-3-flanger.47492/) and [BassChat — BF-3](https://www.basschat.co.uk/topic/173795-boss-bf-3-flanger/) — bass-input real-world use.
- [TalkBass — BF-2 vs BF-3, "what's the difference"](https://www.talkbass.com/threads/boss-bf-2-bf-3-what-the-hell-is-the-difference.292129/) — the analog-vs-digital debate.
- [MaxxMusic — Boss flangers rundown](https://maxxmusicstore.com.au/blogs/news/boss-flangers) — concise BF-1/BF-2/BF-3 lineage.

## 11. Mods / Quirks / Known Issues

- **Buffered-bypass tone-suck debate:** Like all standard Boss pedals, the BF-3 keeps a JFET buffer in the path even when bypassed. The internet's perennial "Boss buffers suck tone" argument applies — but here it's a non-issue: the BF-3 sits late in a long buffered chain (CB Clean and the Colour Box are already buffering upstream), and any high-end loss is irrelevant under a fuzz wall. The buffer is arguably *helpful* driving the mono run into the Somersault/CE-2W.
- **No true-bypass mod is clean on a digital Boss** — unlike the analog BF-2, you can't simply true-bypass the BF-3 without losing the buffer Boss intends; not worth it.
- **MANUAL-knob dead zone:** With DEPTH maxed, MANUAL does nothing. People think the knob is broken — it isn't.
- **Digital sheen on clean tones:** The recurring BF-2-loyalist complaint. Genuinely audible on a clean guitar; inaudible under saturation, so irrelevant in this rig.
- **Gate/Pan in mono is not the "real" mode** — if you select Gate/Pan expecting rotation and only get volume-slicing, that's because Board 1 is mono. Not a fault.
- No widespread reliability failures; it's a Boss compact, which is to say nearly indestructible.

## 12. Spec Sheet

| Spec | Value |
|---|---|
| Type | Digital (DSP) stereo flanger |
| Released | February 2002 (replaced analog BF-2) |
| Controls | MANUAL, RES, DEPTH, RATE, MODE knob, pedal switch |
| Modes | Standard, Ultra, Gate/Pan, Momentary |
| Tap tempo | Yes — via pedal switch (hold ≥2 s); sync range 0.1–18 s/cycle |
| Inputs | GUITAR IN, BASS IN (1/4"; BASS IN disabled when GUITAR IN used) |
| Outputs | OUTPUT A (MONO), OUTPUT B (1/4") — stereo capable |
| Nominal input level | −20 dBu |
| Input impedance | 1 MΩ |
| Nominal output level | −20 dBu |
| Output impedance | 1 kΩ |
| Recommended load | 10 kΩ or greater |
| Bypass | Buffered bypass |
| Power | 9V battery (6LR61) or PSA-series adaptor, center-negative |
| Current draw | 60 mA (official; ignore third-party "40 mA") |
| Dimensions | 73 (W) × 129 (D) × 59 (H) mm |
| Weight | 425 g (15 oz, incl. battery) |
| MIDI / Expression | None |

Source: [Boss Global BF-3 specifications](https://www.boss.info/global/products/bf-3/specifications/) + [owner's manual](manuals/BF-3_M_eng03_W.pdf).

## 13. Starting-Point Settings

Knob positions clock-face, viewed from above. RES/MANUAL is one knob position; treat MANUAL as the labeled function.

**(a) Subtle movement on the wall** — slow drift that keeps the fuzz intact
- MODE: Standard · RATE: 8 o'clock (slow) · DEPTH: 11 · RES: 9 · MANUAL: 11
- Engage once the dirt stack is already a sustained wall. The flange should breathe, not announce itself.

**(b) Jet-flange swell** — the classic sweeping rush, on a doom wall
- MODE: Standard (or Ultra for more edge) · RATE: 9–10 · DEPTH: 2 o'clock · RES: 1 o'clock · MANUAL: 12
- Or use tap-tempo to sync the sweep to the song. Watch output level into the Somersault.

**(c) Ultra chaos** — broken, metallic, ring-mod-adjacent
- MODE: Ultra · RATE: 1–2 o'clock · DEPTH: max · RES: maxed · MANUAL: irrelevant (DEPTH max overrides it)
- Self-oscillating against the fuzz feedback. This is the "recorded-wrong" setting. Pair with granular downstream.

**(d) Bass flange (Jazz bass via BASS IN)** — movement without losing the bottom
- Plug into BASS IN · MODE: Standard · RATE: 8 · DEPTH: 11 · RES: 9–10 · MANUAL: 10
- The BASS IN path preserves low end; keep RES modest so the notches don't thin the fundamental.

## 14. Versus Alternatives — Does It Earn Its Slot?

In a modulation-rich rig (Somersault, CE-2W, Chroma Console, H90, MOOD), the BF-3 has to justify a board space against pedals that can also flange. Honest comparison:

- **vs MXR M117 / EVH Flanger** — The MXR is warmer and more "iconic," but one-trick and analog-only. The BF-3 wins on *flexibility* (four modes, Ultra, slicer, bass input) which matters more here than vintage authenticity, since the flange is buried in saturation anyway.
- **vs EHX Electric Mistress** — Better at the watery, subtle, Summers-style flange and the filter-matrix freeze. If you wanted *that specific* gauzy sound, the Mistress beats the BF-3. The BF-3 is more versatile and quieter.
- **vs the Hologram Chroma Console / Eventide H90 (already in the rig)** — These can flange in stereo, with more depth and recall. The BF-3 **cannot out-flange them on the final wash.** Its one irreplaceable trick is **placement**: it flanges the dirt *directly, in the front of the chain, in the wall,* before any of the texture/time pedals — and it does so on a dedicated footswitch you don't have to menu-dive for. That, plus the Ultra mode's aggressive scooped voicing and the dedicated bass input, is the entire case for keeping it.

**Verdict for this rig:** The BF-3 earns its Board 1 slot specifically as a **front-of-chain, in-the-wall mono flanger** with an immediate Ultra-chaos option — not as a stereo-rotary or as a "better flange than the H90," because it's neither. If you find you only ever want flange on the final stereo wash, the H90 already covers that and the BF-3 becomes optional. Its defensible value is doing the one job nothing downstream can: flanging the saturated source itself. The wasted stereo Gate/Pan mode is the one real inefficiency — accept it, or re-patch post-CE-2W when a part demands rotation.

## Sources

- [Boss US — BF-3 Flanger product page](https://www.boss.info/us/products/bf-3/)
- [Boss Global — BF-3 Specifications](https://www.boss.info/global/products/bf-3/specifications/)
- [Boss BF-3 Owner's Manual (local PDF)](manuals/BF-3_M_eng03_W.pdf)
- [MaxxMusic — Boss Flangers: A Quick Rundown (BF-1/BF-2/BF-3 lineage)](https://maxxmusicstore.com.au/blogs/news/boss-flangers)
- [CraveGuitars — 1981 Boss BF-2 Flanger feature](https://www.craveguitars.co.uk/home/features/effects/feature-1981-boss-bf-2-flanger/)
- [TalkBass — Boss BF-2 vs BF-3, what's the difference](https://www.talkbass.com/threads/boss-bf-2-bf-3-what-the-hell-is-the-difference.292129/)
- [Tonepedia — Boss BF-3 sound review](https://www.tonepedia.com/catalog/effects-and-pedals/flanger/bf-3-flanger/)
- [Guitar Chalk — Boss BF-3 review](https://www.guitarchalk.com/boss-bf-3-review/)
- [Guitar Chalk — Boss BF-3 settings cookbook](https://www.guitarchalk.com/boss-bf-3-flanger-settings/)
- [Rex and the Bass — Boss BF-3 review (bass input)](http://www.rexbass.com/2014/09/boss-bf-3-flanger-effect-pedal-review.html)
- [TalkBass — Boss BF-3 thread](https://www.talkbass.com/threads/boss-bf-3-flanger.47492/)
- [BassChat — Boss BF-3 thread](https://www.basschat.co.uk/topic/173795-boss-bf-3-flanger/)
- [PedalPlayers — Flanger Before or After Distortion](https://pedalplayers.com/flanger-before-or-after-distortion/)
- [Traveling Guitarist — Where to put the flanger in your signal chain](https://travelingguitarist.com/flanger-signal-chain-placement/)
- [Stompbox Book — Forever Flanged: 10 Great Flanger Tracks](https://stompboxbook.com/forever-flanged-10-great-flanger-powered-tracks-pedal-playlist/)
- [GuitarPlayer — Eddie Van Halen "Unchained" isolated guitar (MXR Flanger)](https://www.guitarplayer.com/players/eddie-van-halen-unchained-guitar-isolated)
- [Guitar World — Andy Summers tone (Electric Mistress)](https://www.guitarworld.com/gear/tonal-recall-the-police-andy-summers)
