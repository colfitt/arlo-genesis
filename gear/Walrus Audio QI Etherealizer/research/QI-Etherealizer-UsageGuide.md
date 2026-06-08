# Walrus Audio Qi Etherealizer — Usage Guide

How people *actually* use the Qi, to complement the spec/reference dossier in `QI-Etherealizer-DeepResearch.md`. In this rig it's slot 4 of Board 2 (after the Microcosm, before the Dark Star V3): the way to get the most out of it is the **grain-Freeze pad workflow** — capture a banjo/baritone chord into a frozen loop and play a lead over it — fed into the Dark Star for the actual "space." Two things must be internalized first: run it in **Parallel** and keep **Space modest** (the reverb dominates and is always the last block), and **watch input level** (no level switch — it clips on hot sources like the VG-800).

> Captured this wave: 8 video transcripts + 13 distilled link files (see §8). Forum-grade chatter was largely paywalled/blocked (Reddit, TGP, Gearspace, ModWiggler all 403), so community findings are review- and owner-grade; Elektronauts was the one accessible real thread. Dossier corrections folded in: the **Andrew Huang attribution was wrong** (the "Ambient Adventure" video is **Nobes Music / Yvette Young & Walrus**; no verified Huang Qi demo exists — see §4), and the **Space reverb is always the last block even in Parallel** ([guitarcom-big-review-freeze-routing](links/guitarcom-big-review-freeze-routing.md), [pedal-collaborative](transcripts/pedal-collaborative-understanding-the-qi.md)).

---

## 1. Essential workflows

**Grain-Freeze pad → play over it (the headline trick, and this rig's bread-and-butter).** Short-press **Freeze** to capture the grain buffer into an indefinite loop (LED **blue**); play a lead over it. **Long-press** Freeze ramps **Space reverb to 100%** under the frozen loop (LED **green**); long-press again releases the reverb ramp while the grain keeps looping; a short press releases both ([Yvette Young](transcripts/yvette-young-explore-my-signature-pedal.md); [Mad Steex](transcripts/mad-steex-full-explanation-step-by-step.md)). In **Parallel**, your live dry playing stays unaffected on top of the frozen wall — the most powerful version of the move.

**Three distinct freeze gestures** (people conflate them — they're separate):
- **Grain Freeze** — short-press center → loops the grain buffer.
- **Reverb Freeze** — long-press center → ramps Space to 100% over the grain loop.
- **Delay Freeze / oscillation** — hold **Tap/Osc** → drives delay feedback to max for a saturated snowball ([elektronauts](links/elektronauts-synth-community-thread.md); [guitarcom](links/guitarcom-big-review-freeze-routing.md)).
- *Housekeeping:* long-press **Bypass** clears the grain buffer if a frozen grain has gone stale.

**Choose routing deliberately.** Series ("Forward") lets the always-last Space reverb swallow everything; **Parallel keeps chorus/delay/grain discrete and lets you blend dry at unity**, which is the better default into the Dark Star. Remember the reverb is the final block in *both* modes — Parallel doesn't make the reverb parallel, it just feeds it less wet material ([pedal-collaborative](transcripts/pedal-collaborative-understanding-the-qi.md); [guitarworld](links/guitarworld-review-no-exp-verdict.md)).

**Grain modes + the X knob (two different functions).** *Grain Cloud* triggers grains randomly; X = grain length (min ≈ first-transient-only, near delay-like; max = longer phrase chunks). *Phrase Sample* triggers rhythmically off attack peaks; X = spacing, and **X fully min syncs Phrase Sample to the Delay time** (MIDI-clock the Qi to lock grains to the rig). Playback rotary: x1 / x2 (+oct) / x.5 (−oct) / REV / RNDM — and you can change Playback *while frozen* ([mad-steex](transcripts/mad-steex-full-explanation-step-by-step.md)).

**Don't solo the grain.** Reviewers and owners agree granular alone "sounds a bit weird" but blooms when blended into delay/reverb ([synth-anatomy](transcripts/synth-anatomy-with-synths.md)).

---

## 2. Signature patches & settings

The three factory presets are **Yvette Young's own voicings** (manual p.5, "Yvette's Default Factory Presets"; all ship in **Parallel**). Descriptions directly quoted; knob positions read off the printed diagram, so approximate.

| Preset | Voicing | Settings (approx.) |
|---|---|---|
| **RED** (PC 1) | "Great for freezing & making granular pads" — the rig's freeze-pad anchor | Grain Cloud, Grain Mix ~1:00, X ~1:00, Playback x1; Chorus subtle (Tri); Tone low; Space low. Chord → short-press Freeze → solo over the loop |
| **GREEN** (PC 2) | "THE chorus tone" (Yvette's favorite; target = Roland JC-40/JC-120) | Chorus high ~2:00; Grain off; light Delay; Tone ~10:00; Space low |
| **BLUE** (PC 3) | "Great for randomized moments to freeze and play over" | Grain ~1:00 with randomized Playback; freeze + reverb-pad armed; freeze an unpredictable grain moment, improvise over it |

Source: [yvette-factory-presets-rgb](links/yvette-factory-presets-rgb.md).

**Third-party suggested recipes** (Guitar Chalk, 0–10 scale — *suggested, not hardware-verified*): Dreamy Granular Wash · Warped Tape Echo · Watery Chorus Drift · Glitch Pulse Delay · Freeze Pad Texture — full values in [guitarchalk-settings-suggestions](links/guitarchalk-settings-suggestions.md).

**Owner quick-start:** everything at noon, Grain Playback **x2**, then tap-tempo to your BPM and dial from there ([dkdivedude](links/dkdivedude-hands-on-blog.md)).

**Hidden building blocks** (official): Stereo chorus Mix fully CW = **vibrato**; Phrase-Sample X-min syncs grains to Delay; Freeze long-press ramps reverb 100%; Tap/Osc hold oscillates delay ([walrus-marketing](links/walrus-marketing-patch-descriptions.md)).

See dossier §13 for four fuller rig-tuned starting points (frozen pad / lush chorus / glitch cloud / galaxy wash).

---

## 3. Power-user tips, tricks & hidden features

- **Tone is your hands-free expression substitute.** With no EXP jack, sweep **Tone** on a frozen pad for movement — start open, roll down for motion ([elektronauts](links/elektronauts-synth-community-thread.md)).
- **The Space knob is mix *and* decay on one control** — which is *why* it dominates: you can't get a long decay quietly. Keep Space well below noon into the Dark Star regardless of Flow ([elektronauts](links/elektronauts-synth-community-thread.md); [guitarcom](links/guitarcom-big-review-freeze-routing.md)).
- **The Space reverb morphs** small-room → huge-diffuse as you sweep — it's a character control, not just a decay-amount knob ([walrus-yvette-reverb-demo](transcripts/walrus-yvette-reverb-demo.md)).
- **Tap tempo doesn't affect chorus rate** (intentional) — chorus has its own Rate.
- **Change Playback mode live under a frozen grain** — swap x1 → REV → x.5 while the loop holds for evolving motion.
- **The grain attack is immediate** vs. the Microcosm's noticeable onset delay — useful when you want a reactive (not laggy) granular response ([pedal-collaborative-qi-vs-microcosm](transcripts/pedal-collaborative-qi-vs-microcosm.md)).

---

## 4. Notable users & techniques

- **VERIFIED — Yvette Young (Covet)**, designer. Direct intent: *"an instant vibe and mood machine that would take the control away from you, abstract everything you are doing, and generate pads and things you could jam over by yourself"* — which *is* the Red/Blue workflow. Her technique: math-rock tapping/fingerstyle lead over a self-sustaining frozen grain bed; "painterly," film-scoring-informed. Green = *"give ppl access to my fav chorus sounds"* ([yvette-young-design-intent](links/yvette-young-design-intent.md)).
- **VERIFIED — Jeremy Galindo (This Will Destroy You), Chavez Soliz, Alex Akins** — credited players in the official Walrus Qi Tech Demo (Jan 16 2025). Galindo (post-rock/drone) is the most rig-relevant lane match. No published settings ([verified-artists-demos](links/verified-artists-demos.md)).
- **Non-guitar use:** SYNTH ANATOMY runs hardware synths through it (the rig-relevant clipping warning); also documented with electric harp and a Sequential OB-6 — reinforcing the "any instrument or voice" framing.
- **Attribution correction (don't repeat the error):** the "Ambient Adventure" video (`r0FiTzG9YfQ`) is **Nobes Music**, content credited to **Yvette Young & Walrus** — it is **NOT an Andrew Huang demo**, and there is **no verified Andrew Huang Qi demo** (the candidate `xcKdQAicxq8` is SYNTH ANATOMY). Confirmed via yt-dlp channel metadata ([verified-artists-demos](links/verified-artists-demos.md)).

It's a 2025 pedal — beyond the above, user mythology is genuinely thin.

---

## 5. Rig-specific recipes (this banjo/baritone drone rig)

Slot: `… Microcosm → Qi → Dark Star V3 → (stereo to Board 3)`. Source = a hot, line-leaning VG-800 modeled signal through Board 1.

- **Frozen banjo/baritone pad → Dark Star.** Parallel; Grain Cloud, Grain Mix ~1:00, X ~11, Playback x1; Chorus light (Tri); **Space 10–11** (let the Dark Star own the space); Tone ~1:00. Hit a chord, **short-press Freeze**, play a banjo lead over the loop. Banjo's fast bright transients are ideal **Phrase Sample** peak-fodder — use the **Tone LPF** to tame the 2–4 kHz banjo spike before it grains.
- **Division of labor with the Microcosm (upstream).** Let the **Microcosm own rhythmic/melodic granular motion**; let the **Qi own freeze + texture + smear**. Running both engines hot = mud. Overlap is specifically Qi's Phrase-Sample + REV/RNDM vs the Microcosm's phrase modes — don't double the glitch ([gearnews-vs-microcosm](links/gearnews-vs-hologram-microcosm.md); [pedal-collaborative-vs-microcosm-verdict](links/pedal-collaborative-vs-microcosm-verdict.md)).
- **Don't double the reverb into the Dark Star.** Two big reverbs in series = featureless cloud. Either keep Qi's Space low and let the Dark Star be the board's reverb, or freeze a Qi pad (Space modest) and feed that *sustained source* into the Dark Star's pitch-shimmer — source vs space, complementary not competing.
- **Glitch-cloud over the Microcosm's rhythm.** Parallel; Grain Cloud, Playback **RNDM**, X ~1:00 (sparse, surprising); Delay Mix ~11; Space noon; Tone noon. Let the Microcosm drive the rhythm; the Qi sprinkles reverse/octave grains.
- **Feed the Blooper (Board 3).** Freeze a Qi grain pad → capture in the Blooper → layer. The Qi is a strong sustained source for the loop/tape stage.

---

## 6. Best learning resources

**Video — channels/clips worth following:**
- **Mad Steex** — [the deepest narrated step-by-step tutorial](transcripts/mad-steex-full-explanation-step-by-step.md): every control, the X-knob dual function, the freeze modes, Series/Parallel, reverb-always-last.
- **The Pedal Collaborative** — [control deep-dive](transcripts/pedal-collaborative-understanding-the-qi.md) (with the on-camera routing/reverb-last correction) + [Qi-vs-Microcosm shootout](transcripts/pedal-collaborative-qi-vs-microcosm.md).
- **Yvette Young (official)** — [designer walkthrough](transcripts/yvette-young-explore-my-signature-pedal.md): JC-40 chorus target, freeze-latch-to-DAW workflow, design philosophy.
- **Walrus + Yvette Reverb demo** — [engine-by-engine + morphing reverb + Prophet-6](transcripts/walrus-yvette-reverb-demo.md). **Walrus official Tech Demo** — [canonical control reference](transcripts/walrus-official-tech-demo.md) *(no captions — notes)*.

**Text — reviews/community (forum-grade is thin; these are the best accessible):**
- [guitar.com Big Review](links/guitarcom-big-review-freeze-routing.md) — three freeze types, "mushes delay even at halfway," the Parallel fix.
- [Guitar World review](links/guitarworld-review-no-exp-verdict.md) — confirms no EXP input; reverb is final stage in both modes.
- [SYNTH ANATOMY clipping/reamp fix](links/synthanatomy-clipping-reamp-fix.md) — the rig-critical hot-source clipping issue + Walrus's own reamp fix.
- [Elektronauts thread](links/elektronauts-synth-community-thread.md) — best real community thread (synth use, the mix+decay-on-one-knob insight, Microcosm/Chroma overlap).

---

## 7. Common pitfalls / gotchas

- **Clipping on hot sources is the #1 issue (rig-critical).** The Qi has **no line/instrument level switch** — "clips like crazy with a hot synth signal." Walrus's own recommended fix is to **reamp/attenuate the input** (no onboard pad). For the VG-800 line-level source feeding Board 2: pad it down (inline attenuator / reamp box / the bench EHX Effects Interface) or pull upstream gain until the clip stops ([synthanatomy-clipping-reamp-fix](links/synthanatomy-clipping-reamp-fix.md)).
- **The Space reverb dominates by design** — mix and decay are on one knob, so you can't get a long quiet tail. Keep Space low into the Dark Star; run **Parallel**; don't expect it to sit politely at noon ([elektronauts](links/elektronauts-synth-community-thread.md)).
- **No expression input at all** — continuous sweeps are MIDI-CC only. Use Tone-by-hand or a MIDI controller.
- **The delay is a clean MONO line, not stereo/ping-pong** — and deliberately undegraded; don't expect tape/BBD character from it.
- **300 mA isolated supply required** — won't run off a low-current daisy-chain tap.
- **Firmware: still thin/unverified.** No public post-launch changelog beyond v1.0 / a beta v0.12; the Qi isn't yet on Walrus's main troubleshooting page (it uses the separate MDSP/WebUSB updater). One owner needed to **manually install a driver via Windows Device Manager** before the updater saw the pedal. Check the updater for the current build ([dkdivedude](links/dkdivedude-hands-on-blog.md)).
- **Don't ask both the Qi and the Microcosm to be the main glitch** — split roles or it muds.

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `mad-steex-full-explanation-step-by-step.md` — best tutorial; every control, X-knob dual function, freeze modes, reverb-always-last.
- `yvette-young-explore-my-signature-pedal.md` — designer walkthrough; JC-40 target, freeze-to-DAW, routing philosophy.
- `pedal-collaborative-understanding-the-qi.md` — control deep-dive + on-camera Parallel/reverb-last correction.
- `pedal-collaborative-qi-vs-microcosm.md` — Qi-vs-Microcosm shootout; immediacy difference.
- `walrus-yvette-reverb-demo.md` — engine-by-engine demo; morphing reverb; Prophet-6.
- `synth-anatomy-with-synths.md` — synth use + clipping warning *(notes only — music audio)*.
- `walrus-official-tech-demo.md` — official control walkthrough *(notes only — no captions)*.
- `nobes-music-ambient-adventure.md` — "Ambient Adventure" performance demo (Nobes Music / Yvette Young & Walrus content; *notes only — no captions*; corrects the old Andrew Huang attribution).

**Links** (`research/links/`):
- `yvette-factory-presets-rgb.md` — the three Yvette Red/Green/Blue factory voicings (manual p.5).
- `yvette-young-design-intent.md` — Yvette's direct design-intent + technique quotes.
- `verified-artists-demos.md` — Galindo/Soliz/Akins tech demo + the Andrew Huang mis-attribution correction.
- `guitarchalk-settings-suggestions.md` — 5 named third-party patch recipes with full knob values (suggested, not verified).
- `walrus-marketing-patch-descriptions.md` — official patch-framing + hidden-move building blocks.
- `guitarcom-big-review-freeze-routing.md` — three freeze types, dominant-reverb quantified, Parallel fix.
- `guitarworld-review-no-exp-verdict.md` — confirms no EXP input; reverb final-stage in both modes.
- `synthanatomy-clipping-reamp-fix.md` — clipping on hot signals + Walrus's reamp fix.
- `elektronauts-synth-community-thread.md` — best real community thread (synth use, mix+decay-on-one-knob, Microcosm/Chroma overlap).
- `gearnews-vs-hologram-microcosm.md` — "more ambient than Hologram?"; Phrase-Sample = Microcosm overlap.
- `pedal-collaborative-vs-microcosm-verdict.md` — "closest we've come yet" to the Microcosm.
- `russo-music-routing-midi-clock.md` — Series vs Parallel "no wrong answers"; MIDI-clock sync value.
- `dkdivedude-hands-on-blog.md` — owner blog: Windows firmware-driver gotcha, "noon + 2x" recipe.

## Sources

All claims above cite a captured `transcripts/` or `links/` file. Original URLs are on the first line of each captured file. Authoritative spec/reference lives in [`QI-Etherealizer-DeepResearch.md`](QI-Etherealizer-DeepResearch.md); the manual is at [`manuals/Walrus Audio Etherializer QI.pdf`](../manuals/Walrus%20Audio%20Etherializer%20QI.pdf).
