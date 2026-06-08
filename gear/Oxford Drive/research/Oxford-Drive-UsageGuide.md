# TKOG Oxford Drive — Usage Guide

How people *actually* use the Oxford Drive, to complement the spec/reference dossier in `Oxford-Drive-DeepResearch.md`. This is **TKOG's recreation of the Marshall ShredMaster** — the Jonny Greenwood/Radiohead distortion — so the single most useful thing to know is that **Greenwood's documented ShredMaster settings transfer to it 1:1** (TKOG's own advice: "set the Oxford identically to how you'd set the ShredMaster, then back the gain off a little"). In this rig it's the last dirt stage before the BF-3, where the honest move is a **low-gain momentary intensifier**, or relocating it **ahead of the fuzzes** as a ShredMaster base distortion.

> Captured this wave (Tier B, 2 agents): 4 video transcripts + 10 distilled links = 14 sources (see §8). Folded in a dossier fix: three §10 demos were mis-credited — `UkPeC4_sL9U` is **Mike Hermans** (not collector//emitter), the real collector//emitter video is the 2019 prototype `MkZDi-7vg5A`, and the shootout `nlx69O9y-zY` is **Joe Edelmann** — all verified via yt-dlp.

---

## 1. Essential workflows

**Dial it like a ShredMaster, then back off gain.** TKOG's own Q&A answer (verbatim): *"Set the Oxford Drive identically to how you'd set the ShredMaster, then back off the gain knob a little… and make sure to use silicone clipping if you want the 'stock' sound"* ([tkog-recommended-settings](links/tkog-recommended-settings.md)).

**Contour is a treble+mid TILT, not a mid knob** (the #1 dial-in mistake). CCW (toward 7:00) = mids boosted / treble slightly cut (mid-focused); CW (toward 3:00) = mids scooped *and* treble added. **Re-trim Treble every time you move Contour** — Treble's range shifts with it. Premier Guitar's method: park the EQ, set Contour first, then trim ([premierguitar-shredmaster-dialing-tips](links/premierguitar-shredmaster-dialing-tips.md)).

**Bass is logarithmic — run it LOW (7–9:00).** It "becomes much more noticeable past a certain point"; leaving it high = mud/fogginess. This is why TKOG's own "Classic Overdrive" sits at Bass 8:00.

**Pick the clipping for the job:** **Si** = stock/compressed/tightest, the authentic ShredMaster (most overtones); **LED** = open, louder, higher clipping threshold, good for rhythm (output is *hottest* here — easy to slam the BF-3); **asym** = Si/LED hybrid, widest dynamic range, warm/fat (differences clearest at medium gain).

**Voice:** **'91** = ShredMaster (darkest, mid-punch, lead); **'88** = Guv'nor (brighter, input-refiltered, rhythm). (Later V2.2 units add a brighter **'01**; this rig's two-voice unit may not have it — confirm on the physical toggle.)

**Momentary footswitch.** Hold = momentary burst, tap = latch. Ideal for stab-style dirt events ("à la Pixies") or to avoid hum on noisy high-gain settings.

---

## 2. Signature settings

**TKOG's own example settings** (quoted; '91 voice + Si unless noted) ([tkog-recommended-settings](links/tkog-recommended-settings.md)):

| Name | Gain / Bass / Contour / Treble | Notes |
|---|---|---|
| **Classic Overdrive** | ~12 / **8** / 9 / 3:00 | Lowest-gain pushed-amp; note the low Bass |
| **Shoegaze / Low-Gain Ambient** | 10 / 11 / 12 / 4:00 | TKOG's literal shoegaze patch — "best with dynamic arpeggios + delay/reverb" |
| **Scooped** | 3:00 / 11 / **3:00** / ~2:00 | Mid-scoop (Contour CW scoops mids + adds treble) |
| **Traditional 90s Lead** | 3:00 / ~2:00 / **7:00** / ~2:00 | The straight ShredMaster lead (Contour min = max mids) |
| **Blues Lead** | ~2:00 / 12 / 7:00 / ~8:00 | **LED clipping**; darker, mid-rich, dynamic |

**Jonny Greenwood tone-match** — TKOG documents his actual ShredMaster knobs; they transfer 1:1 (use '91 + Si, then back gain off) ([jonny-greenwood-tone-match](links/jonny-greenwood-tone-match.md)):
- **"Normal" (In Rainbows era):** Gain 3:00 · Bass 2:00 · Contour 7:00 · Treble 2:00 · Vol 5:00 (often lower).
- **AC30-live (2010):** Gain 3:00 · Bass 2:45 · Contour 7:00 · Treble 2:45 · Vol 1:30.
- **Shootout "Jonny's preferred" on the Oxford:** Gain 3:00 · Bass 1:00 · Treble 1:00 · Contour 7:00 (min) · Vol maxed — verdict: with a Fender 85 + Lace Sensors it "nails the Greenwood sound" vs the real ShredMaster ([shredmaster-shootout](transcripts/shredmaster-shootout.md)).
- **"Creep" choruses** (inferred, ShredMaster lore): nearly flat-out — Gain high, Treble high, Bass lower (log taper), Contour low, Si, '91; then back gain off slightly.

> ⚠️ In *this* rig Greenwood's high Bass (2:00) is for a single pedal into a clean amp — **stacked fifth here, run Bass much lower** or it turns to mud.

---

## 3. Power-user tips, tricks & hidden features

- **It's a set-the-character box, not a ride-the-volume box** — cleanup with guitar volume is modest (best in LED/asym). Pick the voice/clipping, don't expect Fuzz-Face dynamics.
- **The fixed band-limiting is a feature for complex inputs** — TKOG's framing: the heavy filtering "prevents the distortion from becoming harsh and buzzy even with complex inputs," so it stays musical on synth/modeled/hex sources where a Muff or Fuzz Face turns to fizz.
- **LED output is hot** — a large boost is available; easy to overdrive the BF-3 downstream.
- **Default on/off state is selectable at power-up** (hold the footswitch).
- **V2 fixed the early issues** — C0G caps killed the V1 microphonics, and the redesigned PCB killed the early-2019 high-gain oscillation. Footswitches are a solderless JST swap (touring-friendly).

---

## 4. Notable users & lineage (honest)

The Oxford Drive itself has **no marquee artist roster** — TKOG sells it on the tone it clones. The fame is the **circuit + the builder's mission**:
- **CONFIRMED: Jonny Greenwood (Radiohead)** — the **Marshall ShredMaster** was his first pedal and primary distortion (most of *Pablo Honey* incl. "Creep" choruses, plus *The Bends*, "Paranoid Android," etc.). His method: ShredMaster → clean Fender Eighty-Five (Boss LS2 toggling a clean path) — the crunch is the pedal, not the amp ([shredmaster-greenwood-radiohead](links/shredmaster-greenwood-radiohead.md)).
- **LOOSELY attributed** (dealer/blog folklore, secondary sources only — flag, don't assert): Thom Yorke, Ed O'Brien, Kevin Shields & Bilinda Butcher (MBV), Alex James (Blur). Kevin Shields has the strongest consensus but no primary confirmation ([shredmaster-circuit-history-users](links/shredmaster-circuit-history-users.md)).
- **TKOG "The King of Gear"** — a NY boutique whose website is literally a Radiohead-gear archive ("how Radiohead make all those funny noises") that grew into a pedal shop. Nice real link: **Greenwood actually uses TKOG's Mini Glitch.** Their line: Oxford Drive, Mini Glitch, Pitch Magpie, EQ-201 ([tkog-builder-profile](links/tkog-builder-profile.md)).
- **Demo reference:** Joe Edelmann (self-described "Radiohead obsessive") runs the Oxford on nearly all his Radiohead covers into a Fender 85 + Lace Sensors.

---

## 5. Rig-specific recipes (banjo/baritone drone)

Chain: `… Hizumitas → Brothers AM → Longsword → Oxford Drive → BF-3 → …` — the Oxford is the 5th/last dirt stage with no amp to push.

- **The honest placement read (consistent with the Hizumitas dossier):** stacked fifth, the Oxford's fixed-mid ShredMaster filter collapses the upstream fuzz texture into "one honk." No community A/B contradicted this. So use it one of two ways:
  1. **Low-gain momentary intensifier into the BF-3.** '91 voice, Si, **Gain 9, Bass 8, Contour 10, Treble 11, Volume 1–2**; *hold* the footswitch to commit the whole front end to a denser brick for a chorus/peak, release back to the nuanced stack. A focused, hotter, mid-present feed makes the BF-3's flange more vocal and metallic — keep Bass low so the flanger isn't sweeping mud.
  2. **Relocate it ahead of the fuzzes** (the manual's own blessing: "place it prior to any dedicated distortion pedals") to act as a genuine ShredMaster *base distortion* the MXR 108 + Hizumitas pile onto — the single highest-impact change if the current slot feels redundant.
- **Modeled-source tamer (the Oxford's most defensible reason to exist here).** For VG-800 / banjo fizz: **'88 voice + LED, Gain 10, Bass 8, Contour 9 (mid-focus, treble pulled), Treble 10** — the band-limiting eats the ice-pick and keeps complex patches musical where the fuzzes turn them to fizz.
- **Banjo:** '88 voice, Contour low (mid-focused), Treble well down, Bass low, low gain — focus over fizz on an already-bright 2–4 kHz source.
- **Baritone:** home territory for a ShredMaster — '91 voice suits the range; mind the log Bass knob (keep it low stacked).
- **Don't stack it for more gain** on the Longsword — you have enough saturation; the Oxford's job here is focus/level, not more dirt.

---

## 6. Best learning resources

- **Joe Edelmann** — the definitive source (a self-described Radiohead obsessive): [the V2 control walkthrough](transcripts/joe-edelmann-v2.md) and [the ShredMaster shootout](transcripts/shredmaster-shootout.md) (Oxford A/B vs a real '90 ShredMaster + reissue, with Greenwood's quoted setting).
- **collector//emitter** — [the 2019 prototype floor demo](transcripts/collector-emitter-2019-prototype.md) (historical). **Mike Hermans** — [clean high-production playthrough](transcripts/mike-hermans-demo.md) *(no captions — ear reference)*.
- **Text:** [TKOG official + example settings](links/tkog-recommended-settings.md), [TKOG Greenwood tone-match](links/jonny-greenwood-tone-match.md), [Stomp Box Steals review](links/stompboxsteals-oxford-drive-review.md) ("old ShredMaster with more volume + gain"), [Premier Guitar ShredMaster dialing tips](links/premierguitar-shredmaster-dialing-tips.md), [V2-vs-V1 improvements](links/oxford-drive-v2-improvements.md).

---

## 7. Common pitfalls / gotchas

- **Contour is not a mid knob** — it's a tilt; re-trim Treble after every move. The most common dial-in mistake.
- **Bass is logarithmic — run it low** (7–9:00) or it fogs, especially stacked. Greenwood's published 2:00 Bass is for a single pedal into a clean amp, not for fifth-in-a-fuzz-stack.
- **Stacked fifth it erases nuance** — it re-filters the whole front end into one ShredMaster honk; use it momentary/low-gain or relocate it. Don't run it always-on as a fifth tone-stage.
- **LED output is hot** — large available boost can slam the BF-3.
- **Version check:** the repo unit is a two-voice ('91/'88) V2 per its manual; later V2.2 units add a third '01 voice. Confirm on the physical toggle (2-position vs 3-position).
- **9V only, ~8 mA** — trivial load, but it's a Boss-style center-negative supply; relay bypass means don't assume signal passes on total power loss.

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `joe-edelmann-v2.md` — Joe Edelmann — full V2 control walkthrough (best single demo; settings + workflows).
- `shredmaster-shootout.md` — Joe Edelmann — Oxford A/B vs real '90 ShredMaster + reissue, with Greenwood's quoted setting.
- `collector-emitter-2019-prototype.md` — collector//emitter — 2019 prototype floor demo (historical).
- `mike-hermans-demo.md` — Mike Hermans — sponsored playthrough *(no captions — notes)*.

**Links** (`research/links/`):
- `tkog-oxford-drive-official.md` — TKOG official — controls/voices/clipping; Contour-tilt + log-Bass gotchas; '01-voice flag.
- `tkog-recommended-settings.md` — TKOG — the 5 named example settings + the Si-stock dial-in Q&A.
- `jonny-greenwood-tone-match.md` — TKOG — Greenwood's documented ShredMaster settings (transfer to Oxford) + shootout setting.
- `shredmaster-greenwood-radiohead.md` — TKOG Radiohead archive — confirmed Greenwood lineage; clean-amp + LS2 method; songs.
- `shredmaster-circuit-history-users.md` — Wikipedia — 1991 trio / Guv'nor lineage; verified-vs-loose artist roster.
- `tkog-builder-profile.md` — TKOG — the Radiohead-archive-turned-builder story; Greenwood uses their Mini Glitch.
- `premierguitar-shredmaster-dialing-tips.md` — Premier Guitar — the Contour-first dial-in method; "dark, compressed"; Creep.
- `stompboxsteals-oxford-drive-review.md` — Stomp Box Steals — "old ShredMaster with more volume + gain," $235, two-voice unit.
- `oxford-drive-v2-improvements.md` — AME Audio — V2-vs-V1: C0G caps fix microphonics, soft-touch momentary bypass.
- `harryandaguitar-creep-2021.md` — real-world Oxford "Creep" cover (inferred settings; QC disambiguation of his later non-Oxford re-records).

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Oxford-Drive-DeepResearch.md`](Oxford-Drive-DeepResearch.md); the manual is at [`manuals/Oxford Drive Manual 3.09.pdf`](../manuals/Oxford%20Drive%20Manual%203.09.pdf).

> **Honest coverage notes:** boutique pedal — Reverb (403), YouTube descriptions, and r/guitarpedals/TGP threads were largely inaccessible, so tips lean on TKOG official + Premier Guitar + Stomp Box Steals + the Joe Edelmann demos. No Oxford-Drive-specific artist roster exists; the famous names are ShredMaster lineage (Greenwood confirmed, the rest loosely attributed). No maker-published Oxford patches exist for the stacked-intensifier / Creep uses — those settings are inferred and flagged.
