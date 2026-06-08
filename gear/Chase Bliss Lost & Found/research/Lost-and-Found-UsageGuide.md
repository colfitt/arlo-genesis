# Chase Bliss Lost + Found — Usage Guide

Despite the unassuming name, the Lost + Found is **not a utility** — it's a **two-channel,
12-algorithm multi-effect** (reverbs, pitch, warp, delay, synth, modulation) with a built-in
**GLUE** compressor/saturator, flexible routing, and full MIDI. Each channel's **MODIFY** knob
both *selects* the effect and sets its character — **MODIFY at noon = no effect (GLUE only)**,
which is the single biggest "is it broken?" trap. In this rig it's a texture/algorithm source
that feeds the Microcosm: **Sympathetic Resonator** turns banjo plinks into glassy pipe-drones,
**Grain Tumbler** makes clock-locked granular shuffles, and **Gen Lite** (≈ Generation Loss) adds
tape ruin. It shipped **Sept 2025 as a limited made-to-order run**, so community recipe/artist
coverage is genuinely thin — the canon is CB's Field Guide + a couple of deep teardown videos.

> Heads-up: this pedal is much deeper than the rig's prior "gate/feedback utility" shorthand
> suggested. Also note **demo videos ran beta firmware** (the Sympathetic Resonator behavior
> changed before release; an unfinished synth engine appeared) — distrust pre-release settings.
> A circulating "**L+F firmware 1.1.0**" claim is **unverified** (those version numbers trace to
> Generation Loss MkII) — check the Bliss Programmer for the real version. *(community-tips, bachelormachinestv-science-part2)*

---

## 1. Essential workflows

### Interface (from the BachelorMachinesTV teardown — exact maps)
- **MODIFY** = selects the channel's algorithm AND sets its character; **noon = effect OFF →
  the GLUE compressor/saturator runs alone.** **TIME** = the time component. **ALT** = hold BOTH
  footswitches + turn the upper knob. **EQ** = hold both + lower knob (LEFT of noon cuts highs,
  RIGHT cuts lows). **SWAP L / SWAP R** dips let either slot host any of the 12 algorithms —
  including **two of the same** (build-your-own dual reverb / shimmer). **SPREAD** dip = mono→stereo. *(bachelormachinestv-science-part1, community-tips)*
- **Routing/mixer:** middle = **parallel** (BLEND mixes the two outputs); point toward a side =
  **series** (that side becomes dry/wet for the second effect); **SPILL** (ALT on the top knob in
  series) feeds dry past the first effect so the second acts on dry + first's output. *(bachelormachinestv-science-part2)*
- **GLUE** is the cohesion tool for multi-effect stacks ("stacked modulation always has something
  missing: compression"). **WET VOLUME unity = MIX at noon** (hold right footswitch, turn MIX). *(community-tips)*

### Per-algorithm control maps (the useful ones for this rig)
- **Slow-verb / Useful Ambience** — MODIFY = feedback, TIME = delay/size, ALT = diffusion.
- **Orchestral Swell** — MODIFY = pitch interval (oct/4th/5th), ALT = feedback, TIME = swell/attack.
- **Sympathetic Resonator** (Knobs's favorite) — "12 pipes tuned to the chromatic scale";
  MODIFY = feedback (max = resonates forever), TIME = onset (near-inaudible), ALT = octave.
  Note-gated: it self-selects pitched content. *(bachelormachinestv-science-part2, walkthrough-knobs)*
- **Grain Tumbler** — TIME governs loop length + playhead rate + grain count *simultaneously*;
  MODIFY = feedback-into-buffer probability; ALT = grain fade (glitch↔ambient); **LATCH dip + HOLD
  = a frozen, repeatable grain pattern**. *(bachelormachinestv-science-part2)*
- **Tape Echo** — TIME = time, MODIFY = feedback (→ infinite, **never self-oscillates**), ALT =
  "stability"/tape age (HPF + warble).
- **Gen Lite** (≈ Generation Loss) — TIME = wow↔flutter (pick one), MODIFY = depth, ALT = "failure"
  crinkles. **Go full-wet for real tape — any dry blend = a random chorus artifact.**
- **Ensemble Expander** — ALT = 2–8 voices, TIME = LFO speed, MODIFY = depth (fewer voices = deeper);
  Juno chorus ≈ **TIME ~10:00 / MODIFY ~8:00 / ALT ~noon (≈4 voices)**.
- **Impulse Synth** — register-sensitive; **strike block chords together**; MODIFY = brightness,
  TIME = portamento, ALT = attack/release tradeoff. *(bachelormachinestv-science-part2, community-tips)*

---

## 2. Signature combos & settings

**CB's 8 named factory Combos** (Field Guide — exact, copyable; `*` = best with MIX maxed): *(cb-manual-combos-official-recipes)*

| Combo | Modes | Routing |
|---|---|---|
| **SHOEGAZE SPECIAL** | Slow-verb **>** Ensemble Expander | `L>R` series |
| **END CREDITS** * | Useful Ambience **<** Impulse Synth | `L<R` series |
| **LIGHT SLEEPER** * | Orchestral Swell **>** Gen Lite | `L>R` series |
| **SYNTH TOWER** * | Impulse Synth **+** Sympathetic Resonator | `L+R`, L SWAP on |
| **ORCHESTRAL RESONANCE** * | Orchestral Swell **+** Sympathetic Resonator | `L+R` |
| **TAPE SHIFTER** | Pitch Repeater **<** Tape Echo | `L<R` series |
| **GRAIN DOUBLER** | Grain Tumbler **+** Grain Tumbler | `L+R`, L SWAP on |
| **MYSTERY MOVEMENT** | Spectral Modulator **+** Pinging Phaser | `L+R`, R SWAP on |

**Recipe-building patterns:** **MEGA EFFECTS** (same mode twice, different settings — try Pitch
Repeater), **FRESH VS. FROZEN** (one instance live, one frozen — try Grain Tumbler), **GLUE-alone**
(a channel on with MODIFY at noon). **A full shareable recipe = modes + MODIFY + ROUTING + BLEND +
MIX + dips (SWAP/SPREAD/UNSYNC/TRAILS) + GLUE**, and **dip settings save with presets** (122 slots,
PC recall via the cb-stack file). *(cb-manual-combos-official-recipes, community-tips)*

---

## 3. Power-user tips, tricks & hidden features

- **MODIFY at noon = effect off / GLUE only** — the #1 trap; also the way to use the comp standalone. *(community-tips, bachelormachinestv-science-part1)*
- **SWAP dips = run any two engines, incl. two of the same** (DIY dual-reverb/shimmer). *(community-tips)*
- **Phaser HOLD freezes the LFO** so you set the poles (2–64) by hand; **Grain Tumbler LATCH+HOLD
  freezes a repeatable grain pattern.** *(bachelormachinestv-science-part1/2)*
- **MIDI randomization** (CC112 / 113 / 114 = Random L / R / Both Mode) → constantly-shifting mode
  combos; drive it from the Digitakt's CC automation. *(baymud-randomizing-midi, bachelormachinestv)*
- **SonicFreaks Max-for-Live + standalone editor** (Dec 2025) exposes all hidden params without
  dip-diving — the only dedicated L+F software tool. *(maxforlive-sonicfreaks-editor)*
- **Tap tempo:** double-tap both footswitches; hold one side + turn TIME for that engine's subdivision. *(community-tips)*

---

## 4. Notable users & techniques

- **Honest:** no touring artist claims it as a signature and no rig rundown features it — too new/
  limited. The de-facto references are **Chase Bliss + Knobs** (Joel Korte's collaborator):
  flagship **Slow-verb shoegaze swell pushed with chunky GLUE**, and **Sympathetic Resonator as a
  forgiving note-gated drone source** (Knobs's stated favorite). *(walkthrough-knobs, artists-and-techniques)*
- **Mark Johnston** ("Secret Weapons," 70 min) — the best routing/workflow tutorial (beta firmware). *(secret-weapons)*
- **Transferable lineage:** Gen Lite ≈ Generation Loss MkII — borrow GenLoss drone technique
  (set-and-drone, freeze, heavy degradation) for that mode. *(artists-and-techniques)*

---

## 5. Rig-specific recipes & CB-stack MIDI

- **Banjo → doom drone:** **Sympathetic Resonator, MODIFY (feedback) maxed** = banjo plinks resonate
  forever into glassy/vibraphone pipes; sweep ALT (octave) during the resonance for expression. *(bachelormachinestv-science-part2)*
- **Clock-locked granular shuffle into the Microcosm:** **Grain Tumbler** — incoming Digitakt clock
  auto-overrides UNSYNC, so it locks; **LATCH + HOLD** freezes a repeatable pattern, then nudge TIME
  for new clock-quantized patterns. *(bachelormachinestv-science-part2)*
- **"Recorded-wrong" wall:** **Gen Lite full-wet** (real tape) → **series into Slow-verb / Useful
  Ambience** for a degraded halo; use **GLUE** lightly to tame spikes before the Microcosm.
  *(bachelormachinestv-science-part1)*
- **Shifting-texture performance event:** draw **MIDI random (CC112/113/114)** from the Digitakt for
  constantly-evolving mode combos feeding the Microcosm. *(baymud-randomizing-midi)*
- **Avoid:** **Useful Ambience does NOT beat-sync** and loses its short room reverb under clock —
  use **Slow-verb** for synced reverb; and don't stack its reverbs against the Microcosm / Dark Star /
  Etherealizer (mud). *(bachelormachinestv-science-part1)*

**CB-stack MIDI/clock** *(reuse the shared `cb-stack-*` files in the Blooper folder):* L+F **syncs
the TIME subdivision of the loaded delay/LFO algorithm** per channel — **CC51** = clock-ignore
(0=ignore), **CC53 (L) / CC54 (R)** = tap subdivision (0–12 = 1/32…double-whole); **MIDI clock
overrides the UNSYNC dip**; tap tempo disabled while synced. Default channel 2; **122 presets** via
PC; one-PC whole-stack scene recall per the shared file. *(cb-stack-clock-sync-per-pedal, cb-stack-preset-scene-recall)*

---

## 6. Best learning resources

- **BachelorMachinesTV "Let's Do Some Science" Pt 1 & 2** (~2 hr) — the essential teardown; the only
  source that maps every knob per algorithm and tests clock sync. Documents the resonator firmware change.
- **Chase Bliss (official)** — the Walkthrough (mode-character tour) + "The Story of Lost + Found."
- **Mark Johnston "Secret Weapons"** (70 min) — routing/workflow deep dive (beta firmware).
- **Bay Mud** — the live **MIDI-randomization** demo (the rig's "Random" use case).
- **Sources:** CB Field Guide "Combos" page (the authoritative recipe doc); the SonicFreaks editor.
  Text forums (TheGearPage 29-page megathread, The Gear Forum, TalkBass, MOD WIGGLER) exist but are
  paywalled/403 to scrapers — browse manually for owner shares. *(bachelormachinestv, walkthrough-knobs, secret-weapons, baymud, cb-manual-combos, community-tips)*

---

## 7. Common pitfalls / gotchas

- **MODIFY at noon = no effect** (GLUE only) — not a fault. *(community-tips)*
- **Gen Lite needs full wet** — any dry blend choruses against the wet (random-chorus artifact); and
  **Gen Lite + SPREAD = per-side flutter** (wide pseudo-random chorus, not realistic tape — SPREAD off
  for believable tape). *(community-tips)*
- **Impulse Synth is register-dependent and wants block chords struck together** (rolling = only the
  last note); not for fast leads. *(community-tips)*
- **Useful Ambience doesn't beat-sync** and its reverb lengthens under clock — pick Slow-verb for
  synced reverb. **Phaser syncs uselessly** (fastest sync = once/beat). *(bachelormachinestv-science-part1)*
- **Beta-firmware demos** misrepresent the shipping Sympathetic Resonator — distrust pre-release
  settings; the "1.1.0" version claim is unverified. *(community-tips, bachelormachinestv-science-part2)*
- **Dual-mono TRS jacks** (may need TRS→dual-TS); **~200 mA** draw — high-current isolated outlet. *(community-tips)*
- **No community recipe culture / no signature artist yet** — too new/limited; lean on CB's Combos + the teardown. *(cb-lost-found-coverage-state)*

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`)
- `bachelormachinestv-science-part1.md` — deepest teardown Pt 1: interface + Reverb/Pitch/Warp maps + clock-sync tests
- `bachelormachinestv-science-part2.md` — Pt 2: Delay/Synth/Bend maps, UNSYNC/LATCH, resonator firmware flag, routing/SPILL
- `cb-lost-found-walkthrough-knobs.md` — official Knobs-studio walkthrough (mode characters, chunky-GLUE Slow-verb, Resonator drone)
- `secret-weapons-mark-johnston-walkthrough.md` — 70-min routing/workflow tutorial (beta firmware)
- `baymud-randomizing-midi-deluge.md` — live MIDI randomization (notes-only); the "Random" reference
- `pedal-of-the-day-stereo-demo.md` — wordless stereo A/B demo (notes-only)

**Links** (`research/links/`)
- `cb-manual-combos-official-recipes.md` — CB's 8 named factory Combos + Swap/Blend/Glue recipe mechanics
- `community-tips-gotchas-firmware.md` — power-user tips / hidden behaviors / gotchas / firmware lore + forum list
- `maxforlive-sonicfreaks-editor.md` — the third-party Max-for-Live/standalone editor
- `cb-lost-found-coverage-state.md` — recipe-source map + honest artist/coverage assessment
- *(MIDI/clock: reuse `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`)*

## Sources

Video (YouTube): BachelorMachinesTV `-GOoani8ZZ4`, `51vhEOrD6es` · CB Knobs walkthrough `Gv7EntFhSLU`
· Mark Johnston `7ebOPVUX8Ew` · Bay Mud `g34eqyKSh6g` · Pedal of the Day `SPQL8wiT19Q`.
Official: chasebliss.com/lost-and-found + Field Guide PDF (Combos) · Bliss Programmer (firmware).
Community: thegearpage.net (megathread), thegearforum / talkbass / modwiggler (fetch-blocked) ·
maxforlive.com (SonicFreaks editor). CB-stack MIDI: `Gear/Chase Bliss Blooper/research/links/cb-stack-*.md`.
