# MXR M173 Classic 108 Fuzz — Usage Guide

How to *actually* get great results from the 108 in this rig, to complement the spec/reference dossier in `108-Fuzz-DeepResearch.md`. Unlike the recently-benched boxes, this one is **live on Board 1** — 5th in the chain, after the JHS Colour Box V2 (a buffer) and immediately before the EQD Hizumitas — as the **raw, splatty silicon Fuzz Face pre-stage that the Hizumitas smooths into the rig's signature doom wall**. Three truths govern it: **the Buffer switch is the whole game** (a silicon Fuzz Face hates a buffer in front, and there are two — the Colour Box and the VG-800's modeled line); **don't max the Fuzz** (the usable voicings live 12–3 o'clock); and **it has no tone control**, so the Hizumitas downstream does the EQ work — which matters enormously for taming the bright banjo.

> Captured this wave (second pass, Tier B, 2 agents): **6 video transcripts + 17 distilled links = 23 artifacts** (see §11) — a richer haul than the benched pedals, as befits an active fuzz. All video attributions verified via `yt-dlp --print channel`. **Dossier correction folded in (§7):** the Gilmour "BC109 on *Dark Side*" claim is softened — gilmourish (the authority) says **BC108**, so the M173's BC108 circuit is arguably *closer* to his DSOTM tone than the BC109 myth. Coverage honesty: strong on settings/buffer/voice/cleanup/stacking, but **nobody demos a 108 specifically into a Hizumitas, or fed by a VG-800/GK line, or on banjo** — those patches stay circuit-reasoned (verify by ear). Two cornerstone technical sources had access issues (ElectroSmash account-suspended → snapshot; freestompboxes 403) but the impedance mechanism is independently corroborated.

---

## 1. Essential settings & the FUZZ taper

Two knobs + a switch ([dossier §2](108-Fuzz-DeepResearch.md)): **OUTPUT/VOLUME** (left — lots of makeup gain, unity well below max), **FUZZ/INPUT** (right — the only voicing knob; **no tone control**), and the **BUFFER** switch (§2 below).

- **The FUZZ taper (two sources agree):** does little below noon; the **usable knee is 12→3 o'clock**, and the **big saturation jump is in the top quarter (3 o'clock→max)**. You do *not* need to max it — the manual's own factory presets all park FUZZ noon-to-2 ([transcripts/pedal-picassos-108-fuzz.md](transcripts/pedal-picassos-108-fuzz.md), [transcripts/middleagedgearjunkie-ff-silicon-vs-germanium.md](transcripts/middleagedgearjunkie-ff-silicon-vs-germanium.md)).
- **OUTPUT** has plenty of makeup gain; at high FUZZ you must push OUTPUT up to reach unity. **FUZZ minimum + OUTPUT high = a clean-ish amp-pusher / boost** (a real, demoed mode).
- **The manual's factory presets** — all doom/stoner-named, which tells you what Dunlop built it for ([links/settings-m173-manual-factory-presets.md](links/settings-m173-manual-factory-presets.md)):

| Preset | OUTPUT | FUZZ | Character |
|---|---|---|---|
| **Brown Acid** | ~1–2 o'c | ~1–2 o'c | balanced psych/stoner "brown" fuzz |
| **Black Iron** | ~10–11 o'c | ~11–12 o'c | lower-output, darker/heavier |
| **Kings of the Desert** | ~1 o'c | ~1–2 o'c | desert/stoner-rock, fuzz up |

The manual's baseline: "start with all controls at noon, flip BUFFER ON" — a sane starting patch for this board.

---

## 2. The Buffer switch — the rig-critical decision

The Buffer switch raises the pedal's input impedance from **10 kΩ (OFF) to 800 kΩ (ON)** — an 80× jump, and the whole story ([dossier §5](108-Fuzz-DeepResearch.md), [links/buffer-electrosmash-fuzzface-analysis.md](links/buffer-electrosmash-fuzzface-analysis.md)):

- **Why it matters here:** a silicon Fuzz Face has a deliberately *low* input impedance that loads the guitar pickup — that loading *is* the sound. Feed it from a buffer (the Colour Box) or a modeled line (the VG-800) instead and the circuit "runs at **max gain with oscillations and mayhem**" — the thin/gated/crackly misbehavior. **So in this rig, Buffer ON is the correct default** (it gives the fuzz a defined high-Z input that tolerates buffers in front, brightens, and stabilizes).
- **The Buffer is also the brightness lever:** ON = brighter, behaves predictably; OFF = darker, fuller, rawer/less stable. Emergent rule from the demos: **dark source → ON; bright source → consider OFF; high FUZZ → OFF (else brittle); low FUZZ → ON (else lifeless)** ([transcripts/superfunawesome-classic-108.md](transcripts/superfunawesome-classic-108.md)).
- **Honest nuance — buffered-into-FF is a *legitimate* voice, not just damage control.** Players run Fuzz Faces off active pickups (a low-Z source) "all the time and don't mind it," and an FF **sandwiched between two buffers** "sounds great" — which is effectively this board's Colour-Box-buffer + 108-input-buffer topology. **Judge by ear; don't assume it's compromised** ([links/forum-pedalpcb-fuzzface-buffers.md](links/forum-pedalpcb-fuzzface-buffers.md)).

---

## 3. The silicon Fuzz Face voice

- **vs germanium FF:** silicon = brighter, edgier, "ruder," **higher-gain and more stable**; germanium = mid-range growl, warmer, softer. Crucially the silicon voice **survives buffering better** — the right side of the FF axis for a buffered chain ([transcripts/middleagedgearjunkie-ff-silicon-vs-germanium.md](transcripts/middleagedgearjunkie-ff-silicon-vs-germanium.md), [links/tips-silicon-vs-germanium-quirks.md](links/tips-silicon-vs-germanium-quirks.md)).
- **BC108 specifically** = the more temperature-stable, smoother-leaning silicon (matches Premier Guitar's "darker/fuller than expected"); it won't drift muddy/over-gated when warm the way germanium can.
- **vs the Big Muff (Hizumitas):** the 108 is the **raw, gated, spitty, touch-reactive two-transistor splat**; the Muff is the dense sustaining wall. Complementary, not redundant — that's exactly why they're stacked.

---

## 4. The volume-cleanup trick & the rig caveat

The Fuzz Face party trick: roll the guitar volume back and the fuzz decongests to edge-of-breakup, then dirties as you turn up — no pedal touch needed. The mechanism is the **passive volume pot loading the fuzz's low input-Z** (an "exaggerated log-pot" taper).

- **The rig caveat (important):** through the **GK-5 → VG-800 → Colour Box** path there is *no passive pot* in the loop, and **a buffer decouples the trick** (the pot reverts to a normal volume control). So the magic taper is **unavailable from the GK instruments** — and engaging the 108's own Buffer decouples it further ([links/buffer-electrosmash-fuzzface-analysis.md](links/buffer-electrosmash-fuzzface-analysis.md)).
- **To get it back:** plug a **passive guitar (SG, MIJ Jazzmaster) straight into the front of Board 1, ahead of all buffers** — that restores both the real Fuzz Face response and the volume cleanup. (A passive-pickup simulator pedal in front does the same.)
- **Honest nuance:** silicon doesn't clean *all the way* to clean like germanium, but per Analog Man it "cleans up quite a bit and is sensitive to your dynamics" — slightly more available than a worst-case reading suggests ([links/artist-analogman-fuzzface-silicon.md](links/artist-analogman-fuzzface-silicon.md)).

---

## 5. Stacking — the 108→Hizumitas doom wall

The signature move, and the reason the 108 earns its slot ([links/stack-gilmourish-bigmuff-stacking.md](links/stack-gilmourish-bigmuff-stacking.md), [links/stack-sixstringsensei-108-chain.md](links/stack-sixstringsensei-108-chain.md), [links/stack-musicradar-gain-stacking.md](links/stack-musicradar-gain-stacking.md)):

- **108 → Hizumitas** is the *unconventional* order (a Muff usually goes first). Here the 108 is the splatty grind/level pre-stage and the Hizumitas smooths it into a sustained wall — **and the Hizumitas supplies the tone-shaping the tone-control-less 108 lacks** (its 3n3 HPF Tone is your only EQ on this stage).
- **Insert a low-gain drive between them** — the canonical 108 chain is literally "fuzz → light drive → Muff." A **Brothers AM** (or a TS/SD-1-style drive) between the 108 and Hizumitas pushes the fuzz, **masks its gate, and makes it sustain longer** (drive-into-a-gated-fuzz = longer sustain).
- **The order-swap fix:** if the 108 sounds thin/unstable even with Buffer ON, **swap to Hizumitas → 108** — the Muff's low *output* impedance drives the Fuzz Face cleanly. Worth A/Bing once on the board.
- **Shape after, don't pile gain:** a clean boost or mid-pushed EQ *after* the dirt reclaims the mids a Muff scoops and tightens woofy lows (the Brothers AM in its "drive-after-Muff" role).
- **Shoegaze A/B (not its hardwired slot):** fuzz *after* a reverb = the chaotic "distorted-reverb" texture — worth trying via the H90/Board 3 if you route a fuzz into the time wall.

---

## 6. Signature patches & settings

| Patch | 108 | Stack |
|---|---|---|
| **Full splatty fuzz** | OUTPUT ~12 (to unity) · FUZZ 3 o'c · Buffer per source | 108 alone, Hizumitas bypassed; accept the gate |
| **108 → Hizumitas DOOM WALL** (rig signature) | OUTPUT 12 · FUZZ 12–2 o'c · **Buffer ON** | Hizumitas: Volume max · Sustain max · Tone full CW (bass). Long verb/delay downstream. *Live move: park Hizumitas Sustain at noon and sweep its Tone through the decay.* |
| **Banjo lead through the wall** (EBM-5) | OUTPUT 12 · FUZZ ~3 o'c · **Buffer ON** (stability with the buffered source) | Hizumitas Tone 1–2 o'c (bass side) + a **darker VG-800 cab model** to kill the banjo's ice-pick — the 108 has no tone knob, so the EQ lives downstream. *(A/B Buffer OFF for a darker fuzz if it doesn't get crackly.)* |

---

## 7. Rig-specific recipes & pairings

- **Buffer fixes, ranked** for the Colour-Box + VG-800 source: (1) **Buffer ON** — the default; (2) accept buffered-into-FF as a voice and tune by ear; (3) **order-swap** to Hizumitas → 108; (4) **plug a passive SG/Jazzmaster into the front of Board 1** (best tone + restores the volume cleanup) or use a pickup-simulator.
- **Into the texture/time boards:** the 108→Hizumitas wall is ideal food for the Microcosm / Dark Star V3 / H90 downstream — a dense, gapless sustained source the granular/smear engines love.
- **Don't expect the volume-cleanup from the GK path** — it's a buffered/modeled line; that trick needs a passive guitar in front (§4).

---

## 8. Notable users (honest)

No signature mythology around the **M173** itself (a modern reissue) — attribute to the **silicon BC108 Fuzz Face circuit**, not the pedal ([links/artist-mitchakes-silicon-users.md](links/artist-mitchakes-silicon-users.md), [links/artist-analogman-fuzzface-silicon.md](links/artist-analogman-fuzzface-silicon.md)):
- **Jimi Hendrix** — **likely a BC108 silicon Fuzz Face** for the Band of Gypsys / Fillmore East (NYE 1969–Jan 1970) period (his earlier, more famous tones were germanium).
- **David Gilmour** — a **silicon Fuzz Face on *The Dark Side of the Moon*** ("Time," "Money"). The popular "BC109" claim is **contested** — gilmourish (the authority) says **BC108**, which makes the M173 *more* accurate to his DSOTM tone than the BC109 myth ([links/artist-gilmour-bc108-vs-bc109-flag.md](links/artist-gilmour-bc108-vs-bc109-flag.md)).
- **Eric Johnson** (BC183L silicon, "Cliffs of Dover" — likely), **Gary Clark Jr** (mentioned, low confidence). *Treat specific transistor/song attributions as the hedge-flagged lore they are.*

---

## 9. Best learning resources

- **The Pedal Picassos** — [the #1 concrete-settings demo](transcripts/pedal-picassos-108-fuzz.md) (FUZZ taper, buffer A/B, cleanup, fuzz-as-boost, the shoegaze "stack delay+reverb in front" move).
- **TheSuperFunAwesome…PedalShow** — [the deepest buffer A/B](transcripts/superfunawesome-classic-108.md) across guitars/gain. **gearmanndude** — [humbucker/SG into the 108](transcripts/gearmanndude-classic-108.md) (the owner's SG source). **Middle Aged Gear Junkie** — [silicon-vs-germanium voice](transcripts/middleagedgearjunkie-ff-silicon-vs-germanium.md).
- **ProGuitarShop** (713k views, *no captions*) and **Eirik Stordrange** (*no captions*) — the canonical sound references, content covered in prose by the captioned demos above.
- **ElectroSmash Fuzz Face analysis** ([links/buffer-electrosmash-fuzzface-analysis.md](links/buffer-electrosmash-fuzzface-analysis.md)) — the impedance/cleanup mechanism; **gilmourish** ([links/stack-gilmourish-bigmuff-stacking.md](links/stack-gilmourish-bigmuff-stacking.md)) for Muff-stacking.

---

## 10. Common pitfalls / gotchas

- **Don't max the FUZZ** — the usable range is 12–3 o'clock; the top quarter is the only big jump.
- **Buffer ON is the default here** (buffered source in front); but A/B it — OFF can be a better voice if it doesn't crackle.
- **No tone control** — all EQ comes from the Hizumitas downstream + the VG-800 cab model; this is how you tame the bright banjo.
- **The volume-cleanup trick is unavailable from the GK path** — needs a passive guitar in front of all buffers.
- **The gated "splat"** at low FUZZ / bright sources is inherent — fix by feeding more level (a drive in front) or embrace it.
- **If it sounds thin even with Buffer ON,** swap the order to Hizumitas → 108.
- **No user bias trim** — it's a sealed production unit; "mods" = none (unlike a clone).

---

## 11. Captured sources

**Transcripts** (`research/transcripts/`, 6):
- `pedal-picassos-108-fuzz.md` — the #1 settings demo (taper, buffer A/B, cleanup, shoegaze stacking).
- `superfunawesome-classic-108.md` — the deepest buffer A/B across guitars/gain.
- `gearmanndude-classic-108.md` — humbucker/SG into the 108.
- `middleagedgearjunkie-ff-silicon-vs-germanium.md` — silicon-vs-germanium voice + taper/buffer confirmation.
- `proguitarshop-m173-108.md` — canonical full-size M173 reference *(no captions — notes)*.
- `eirik-stordrange-ff-silicon-vs-germanium.md` — best-known FF silicon/germanium A/B *(no captions — notes)*.

**Links** (`research/links/`, 17):
- **Settings:** settings-guitarchalk-108-tones · settings-m173-manual-factory-presets.
- **Buffer:** buffer-electrosmash-fuzzface-analysis · buffer-jhs-understanding-buffers · buffer-texasbluesalley-pickup-simulator · forum-pedalpcb-fuzzface-buffers.
- **Stacking:** stack-gilmourish-bigmuff-stacking · stack-sixstringsensei-108-chain · stack-musicradar-gain-stacking · stack-wampler-gain-stacking-101 · stack-shoegaze-fuzz-reverb-order.
- **Tips/voice:** tips-screaminfx-fuzz-tips-tricks · tips-silicon-vs-germanium-quirks.
- **Artists:** artist-analogman-fuzzface-silicon · artist-hendrix-silicon-customboards · artist-mitchakes-silicon-users · artist-gilmour-bc108-vs-bc109-flag.

## Sources

All claims above cite a captured file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`108-Fuzz-DeepResearch.md`](108-Fuzz-DeepResearch.md); the manual is in `manuals/`.

> **Honest coverage notes:** good depth for a production fuzz — settings, the buffer verdict, the FUZZ taper, silicon-vs-germanium voice, the cleanup mechanism, and stacking are all corroborated across multiple verified sources, and the manual's own presets confirm the doom/stoner intent. **Gaps:** nobody demos a 108 *specifically* into an EQD Hizumitas, fed by a VG-800/GK line, or on banjo — those rig patches are circuit-reasoned (verify by ear), consistent with the dossier's §6 flag; the two highest-view demos have no captions (covered in prose by the captioned ones). ElectroSmash (account-suspended) was captured from snapshot but its impedance mechanism is independently corroborated (PedalPCB, screaminfx, Analog Man). **Dossier correction:** §7's Gilmour "BC109 on *Dark Side*" softened to "silicon FF, likely BC108 (BC109 contested)." All video attributions yt-dlp-verified — no mis-credits.
