# UAFX Del-Verb — Usage Guide

How to *actually* get the most out of the Del-Verb, to complement the spec/reference dossier in `Del-Verb-DeepResearch.md`. Be honest up front: in this rig the Del-Verb is **benched** — the Eventide H90 subsumes it and the OBNE Dark Star V3 / Walrus QI own the broken-ambient texture — so this guide is about the **two roles where it genuinely wins**: a one-box **travel/fly delay+reverb** that sounds like UA's flagships, and a coherent piece of the **all-UA Apollo x8 workflow**. Two practical truths shape everything: the pedal has **no onboard presets** (its depth lives in the app **"voicings,"** which are *stored in the pedal* so you can play phone-free), and the **UAFX 2.0 USB-MIDI** update is the only way to make it preset-like — but it's CC-only and fussy about message order.

> Captured this wave (second pass, Tier B, 2 agents): **7 video transcripts + 12 distilled links = 19 artifacts** (see §10). All video attributions verified via `yt-dlp --print channel`. **Two dossier corrections folded in** (§7/§10): the "official UA in-depth demo" (`8q2FBlLoGWI`) is actually **R.J. Ronquillo's** channel, and the "no-talking demo" (`ge_ORIwQyws`) is a **Bonedo Synthesizers OB-6 *synth* demo**, not a guitar demo — both patched. Coverage honesty: thin, exactly as expected for a 2023 convenience box with **no artist mythology** and **no deep settings video** (the deepest UA-sanctioned demo is 95% playing). The real depth is in the **manual** (now dated Dec 22 2025), the **app voicing list**, and the **Morningstar MIDI walkthrough** — which is where this research went.

---

## 1. Essential workflow — pick a world, pre-load voicings

**It's a travel box; treat it like one.** Strip the rig to a carry-on board and the Del-Verb is an entire ambient rig in one enclosure: a credible spring/plate/hall + tape/BBD/digital delay, stereo, ~400 mA, no laptop. The simplicity that makes it redundant at home is what makes it right on the road ([transcripts/matheus-barros-vs-collider.md](transcripts/matheus-barros-vs-collider.md) lands on exactly this verdict).

- **Footswitch modes** (set in the UAFX Control app): **Delay | Reverb** (default — each foot toggles one), **Effects | Tap** (left toggles both, right taps), **Delay | Tap** (reverb always-on, leveled by its knob). The documented gripe across three demos: you **can't have a dedicated tap *and* an independent reverb toggle at once** ([transcripts/doug-hanson-demo.md](transcripts/doug-hanson-demo.md), [transcripts/guitar-bonedo-sounddemo.md](transcripts/guitar-bonedo-sounddemo.md)).
- **Trails on/off** is app-selectable: Off kills tails instantly on bypass; On lets them ring. (Self-oscillation keeps running in the background even bypassed — see §5.)
- **The setup move:** pre-assign one voicing per Delay model + one per Reverb model in the app over Bluetooth, set your knobs, and you're done — the assignments **persist in the pedal**, so the phone comes off the board ([links/voicing-list-official.md](links/voicing-list-official.md)).

---

## 2. The app "voicings" — the hidden depth (no presets, but this)

There are **no user presets**, but ~**126 factory "voicings"** are the substitute: they reach the parameters the **hardware knobs can't** — reverb decay/tone/pre-delay/dwell, alternate tape machines, pitched-repeat and ping-pong delays, glide. You **assign** one per effect in the app (you **cannot edit** a voicing — assign-only, pick from the list); each type has a **"Default"** baseline; selecting a type over MIDI loads whatever voicing you assigned to it ([links/voicing-list-official.md](links/voicing-list-official.md), [transcripts/thomann-gear-check.md](transcripts/thomann-gear-check.md)).

**The picks that matter for a drone/doom/shoegaze player:**
- **Hall 224** (the ambient workhorse): **Dark N Dusty Trail** (Large Hall B, dark/distant, lots of pre-delay — the doom wall), **Cascade 224** (Large Hall B, bright + huge — shoegaze sparkle), **Fractal Forest** / **Swimmy and Shakey** (Small Hall A, max mid decay, 150 ms pre-delay — modulated bloom), **Shimmeron** (Chamber, shimmer-leaning), **Hallelujah Stack Verbs** (stacked Small Room + Large Hall — best for clean/fingerpicked).
- **Precision delay:** **Stereo Ping Pong Hi-Cut** (3.5 kHz LPF + 130 Hz HPF in the feedback loop — keeps an ambient wash from turning to mud), **Stereo Ping Pong Vibrato** (LFO movement on a static pad), **Delay Tempo Glide** (tape-style pitch drag — the only Precision mode where time changes bend pitch).
- **Tape EP-III:** **EP with octave / 5th Pitched Buckets** (free harmonized shimmer without a dedicated pedal), **Dark Tape n Preamp** (murky dub), **Broken Bottom** / **Dirty Heads** (thin/lo-fi).
- **Spring '65 wildcard:** **Symphonic Reverb** — a cavernous, *pitch-modulated* big-verb that's the surprise ambient option on the otherwise-surfy spring.

---

## 3. Signature patches & settings (copyable)

Clock-face positions; full sheet in [links/demo-ambient-travel-patches.md](links/demo-ambient-travel-patches.md) (extends the dossier §13 with voicing names + per-source notes).

| Patch | Reverb | Delay | Key knobs |
|---|---|---|---|
| **(a) Carry-on shimmer wash** — the reason to own it | Hall 224 @ **1–2 o'c**, *Dark N Dusty Trail* (doom) / *Cascade 224* (shoegaze) | **Precision**, *Stereo Ping Pong Hi-Cut*, dotted-⅛ | FB 1–2 o'c · Mix noon · Color slightly left · Mod off · Trails On |
| **(b) Octave-shimmer drone** — closest to home | Hall 224 @ **noon–1**, *Shimmeron* / *Fractal Forest* | **Tape EP-III**, *EP with octave pitched buckets* | Time long · FB 12–1 · Mix 11 · Color past noon (grit) · Mod → Worn |
| **(c) VG-800 pad / synth ambience** | Hall 224 @ **1 o'c**, *Default 224 Hall* / *Swimmy and Shakey* | **Precision**, *Stereo Ping Pong Vibrato* | Time dotted-⅛ · FB noon · Mix 10–11 (under the pad) · flat Color |
| **(d) Banjo-as-lead clean** — articulate, not smeared | Plate 140 @ **10–11**, *Studio standard Plate A* | **Precision**, *Default Precision* | Time ~120–180 ms slap · FB min · Mix 9 · Color slight right |
| **(e) Dub / tape feedback** — performance | Spring '65 @ **9**, *Spring Tube Drive A* | **Tape EP-III**, *Default* / *Dark Tape n Preamp* | FB 2–3 o'c (edge of self-osc) · Mix 11 · Mod → Worn · ride FB to kill runaway |

> Plate flatters the bright/transient banjo (Spring's 2–4 kHz splash ice-picks it); the baritone loves Hall 224 + worn Tape, but watch feedback — runaway goes subsonic fast.

---

## 4. The UAFX 2.0 USB-MIDI workflow — the "preset" workaround

Since there are no onboard presets, external MIDI (Nov 2025 firmware) is the only way to recall sounds with your feet — but understand its shape ([links/midi-official-manual-cc-chart.md](links/midi-official-manual-cc-chart.md), [transcripts/morningstar-uafx2-midi.md](transcripts/morningstar-uafx2-midi.md), [links/midi-morningstar-forum-delverb-implementation.md](links/midi-morningstar-forum-delverb-implementation.md)):

- **CC-only, no Program Change** → a "snapshot" is a **stack of CCs stored on the *controller*,** not a preset on the pedal.
- **The WYSIWYG gotcha (official):** the manual's required send order is **(1) bypass/unbypass → (2) effect select → (3) all other params** — because selecting an effect type **snaps every knob back to its physical panel position**, wiping any params you sent first. Owners report needing **~50 ms gaps** between messages.
- **CC map:** `12` FS-Left · `13` FS-Right · `14` Delay Select (0=Tape,1=DMM,2=Precision) · `15` Reverb Select · `20` Reverb Bypass *(independent of footswitch mode — toggle reverb even in Delay|Tap mode)* · `22` Mix · `24` Feedback · `25` **Division** · `27` Mod · `28` Reverb level.
- **Hidden gold — CC-25 Division** unlocks subdivisions the hardware tap can't reach: dotted-⅛, ⅛, ⅛-triplet, and **two dual-rhythm modes** (Dual ¼+dotted-⅛, Dual ¼+⅛) — multi-tap rhythmic echoes, the most useful "hidden" delay feature for ambient/dub.
- **What hosts it:** the pedal is a USB *device* over USB-C (no DIN), so it needs a controller with a **USB host port** wired directly (e.g. **Morningstar MC6/MC8 Pro — no computer needed**), or a **CME H2MIDI Pro** + any DIN controller; up to 8 pedals via a **passive USB hub** (USB-MIDI has no thru). MIDI Beat Clock sync works.
- **The single-port caveat (Sound on Sound):** one USB-C port means you **can't run the MIDI host and the UAFX Control app at the same time** — set voicings over Bluetooth first, *then* plug into the host for the gig ([links/midi-soundonsound-uafx20-review.md](links/midi-soundonsound-uafx20-review.md)).

---

## 5. Power-user tips & hidden features

- **Kill-dry at max:** both Mix and Reverb knobs mute the dry signal fully clockwise (100% wet) — useful for a parallel/aux send, a trap on a series board ([links/tips-power-user-hidden-behaviors.md](links/tips-power-user-hidden-behaviors.md)).
- **Runaway survives bypass:** Tape/DMM self-oscillate past ~3 o'clock (Precision repeats forever at max but never oscillates); turning the pedal **off doesn't stop it** — only dropping **Feedback to minimum** does. Know this before a quiet section.
- **Color is an overdrive on Analog DMM** (input gain; past noon adds OD + harmonics), a tape record-level on EP-III, and a treble-tilt tone on Precision.
- **Bipolar Mod knob, noon = off:** Tape = New↔Worn crossfade; DMM = Vibrato/Chorus; Precision = Flanger/Chorus.
- **Fixed internal order = delay → reverb** (not reorderable); each engine is a separate stereo instance.
- **Engine-switch auto-rescales** an over-long delay time to the new model's range; Tape/DMM pitch-shift with the Time knob, Precision is pitch-stable (except glide voicings).

---

## 6. Rig-specific recipes & pairings

- **The travel/fly board (the endorsed home):** tuner → one drive/fuzz (**JHS Kilt v10** or **Brothers AM**, both bench-able for travel) → Del-Verb → amp/PA/Apollo. Stereo out via the two TS jacks. A complete walls-of-sound rig in a backpack ([links/stack-placement-recipes.md](links/stack-placement-recipes.md)).
- **Apollo x8 / all-UA synergy (the real edge):** nearly every engine has a UAD plug-in twin — **Hall 224 → UAD Lexicon 224**, **Plate 140 → UAD EMT 140** (modeled from the *same* Plant/Sausalito units the pedal's plate was sourced from — the tightest match), **Spring '65 → AKG BX 20 / amp-spring**, **Tape EP-III → UAD EP-34 / Galaxy Tape Echo**. Track dry into the x8, monitor wet through the pedal, then **extend/automate in the box** with the plug-in — which *has* the decay/tone/pre-delay the pedal lacks (the plug-in is effectively the Del-Verb's missing deep-edit page). Caveat: UA "recoded for guitar," so they're voiced cousins, not byte-identical ([links/apollo-uad-in-the-box-synergy.md](links/apollo-uad-in-the-box-synergy.md)).
- **Source notes:** Plate 140 flatters the bright banjo; Hall 224 + worn Tape suits the baritone drone; the Del-Verb is post-cab/end-of-chain so it treats a **VG-800** modeled patch like any line source (analog dry-through preserves low end — also why it's bass-friendly).
- **Why it's benched at home (don't fight it):** on a full board the **H90** does everything it does *with* decay/tone controls and presets; **Dark Star V3 / QI** own the broken-granular ambient this player actually chases. The Del-Verb's seat is the road, not the wall of sound.

---

## 7. Notable users (honest)

**No signature-artist mythology — none to invent.** It's a 2023 curated convenience box. UA's named endorsers (Pete Thorn, Blues Saraceno, James Santiago) attach to the **AMP** pedals (Lion), not the Del-Verb; in-the-wild "users" are anonymous small-board/HX-Stomp/home-producer players. The credible heritage belongs to the **hardware it models** — the Lexicon 224, EMT 140, and Echoplex EP-III — and to the **Golden Reverberator / Starlight Echo Station** engines it's built from (the Golden won a 2022 TEC Award). Anyone citing "the Golden's plate" or "the Starlight's EP-III" is, sonically, citing the Del-Verb ([links/artist-uses-honest.md](links/artist-uses-honest.md)). *(Unverified: any specific Del-Verb artist — none found.)*

---

## 8. Best learning resources

- **Morningstar Engineering** — [the definitive UAFX 2.0 MIDI walkthrough](transcripts/morningstar-uafx2-midi.md) (demos the Del-Verb specifically; the single best source for the MIDI reality).
- **Thomann's Guitars & Basses** — [the best voicings walkthrough](transcripts/thomann-gear-check.md) (the ~126 count + stored-in-pedal fact). **Doug Hanson** — [the cleanest spoken controls reference](transcripts/doug-hanson-demo.md).
- **R.J. Ronquillo** — [the UA-sanctioned tone playthrough](transcripts/rj-ronquillo-indepth.md) (great sounds, light on spoken settings). **Guitar Bonedo** — [voicings are assign-only + the footswitch gripe](transcripts/guitar-bonedo-sounddemo.md). **Matheus Barros** — [ambient head-to-head that endorses the travel role](transcripts/matheus-barros-vs-collider.md).
- **The manual** (now dated Dec 22 2025) is the real settings/CC reference; the **[UAFX Preset & Voicing Lists](https://help.uaudio.com/hc/en-us/articles/8272165765012-UAFX-Preset-and-Voicing-Lists)** support page has the full voicing names ([links/midi-ua-unlock-usb-midi.md](links/midi-ua-unlock-usb-midi.md), [links/tips-anatomyoftone-gig-workflow.md](links/tips-anatomyoftone-gig-workflow.md) for the "pick a world and stick to it" gig advice).

---

## 9. Common pitfalls / gotchas

- **No reverb decay/tone/pre-delay on the hardware** — if a tail's wrong you must change the **app voicing**, so plan voicings before a gig.
- **Runaway survives bypass** — drop Feedback to min to stop self-oscillation; off doesn't.
- **Kill-dry at max Mix/Reverb** — surprising on a series board.
- **MIDI send order matters** — bypass → effect-select → params, ~50 ms apart, or the pedal snaps to panel positions and ignores your changes.
- **Can't run the MIDI host and the app at once** (single USB-C) — configure over Bluetooth first.
- **No DIN MIDI / no Program Change** — needs a USB-host controller; snapshots live on the controller, not the pedal.
- **400 mA, LPS-compliant supply** — heavy draw, give it a dedicated high-current isolated slot.
- **Footswitch modes are mutually exclusive** — no dedicated tap + independent reverb toggle simultaneously.

---

## 10. Captured sources

**Transcripts** (`research/transcripts/`, 7):
- `morningstar-uafx2-midi.md` — Morningstar Engineering — the definitive UAFX 2.0 MIDI walkthrough.
- `thomann-gear-check.md` — Thomann's Guitars & Basses — best voicings walkthrough (~126, stored-in-pedal).
- `doug-hanson-demo.md` — Doug Hanson — cleanest spoken controls reference.
- `rj-ronquillo-indepth.md` — R.J. Ronquillo — UA-sanctioned tone playthrough *(the demo the dossier mis-credited to "UA official")*.
- `guitar-bonedo-sounddemo.md` — Guitar Bonedo — voicings assign-only + footswitch gripe.
- `matheus-barros-vs-collider.md` — Matheus Barros — ambient head-to-head; endorses the travel role.
- `bonedo-synth-notalking-ob6.md` — Bonedo Synthesizers — no-talking OB-6 *synth*-source demo *(the clip the dossier mis-labeled a "no-talking guitar demo")*.

**Links** (`research/links/`, 12):
- `voicing-list-official.md` — the app voicing names per model + drone/doom picks.
- `demo-ambient-travel-patches.md` — 5 copyable ambient/travel patches for this rig.
- `settings-midi-and-controls.md` — per-model control tables (CC cross-referenced).
- `midi-official-manual-cc-chart.md` — authoritative CC map + the send-order rule + dual-rhythm divisions.
- `midi-ua-unlock-usb-midi.md` — UA's USB-MIDI overview. `midi-soundonsound-uafx20-review.md` — the single-USB-port caveat.
- `midi-morningstar-forum-delverb-implementation.md` — the WYSIWYG gotcha + host options.
- `apollo-uad-in-the-box-synergy.md` — the UAD plug-in twin map + tracking workflow.
- `stack-placement-recipes.md` — drive-first / Del-Verb-last + the travel-board build.
- `tips-power-user-hidden-behaviors.md` — kill-dry, runaway, Color-as-OD, bipolar Mod.
- `tips-anatomyoftone-gig-workflow.md` — the "pick a world / no-app-on-the-fly" gig advice.
- `artist-uses-honest.md` — the honest no-mythology finding + the modeled-hardware heritage.

## Sources

All claims above cite a captured file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Del-Verb-DeepResearch.md`](Del-Verb-DeepResearch.md); the manual is in `manuals/`.

> **Honest coverage notes:** thin by nature — a 2023 convenience box with **no artist mythology** and **no deep settings video** (the deepest UA-sanctioned demo is 95% playing). The substance came from the **official manual** (now Dec 22 2025, with a dedicated MIDI-CC section), the **app voicing list**, the **Morningstar MIDI walkthrough**, and **Sound on Sound**. Community-forum depth was limited by blocks — **TheGearPage (402), Gearspace / TalkBass / UAD Forum (403)** all refused fetches; their substance was pulled from snippets + the dossier. **Two dossier corrections folded in:** `8q2FBlLoGWI` is **R.J. Ronquillo's** channel (not UA's official upload), and `ge_ORIwQyws` is a **Bonedo Synthesizers OB-6 synth demo** (not a no-talking guitar demo) — §7/§10 patched; the dossier's bench-it-for-travel verdict is fully corroborated.
