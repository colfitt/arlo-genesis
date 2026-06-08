# Chase Bliss Brothers AM — Deep Research

A working dossier for the Brothers AM as it lives 7th on Board 1, immediately downstream of the EQD Hizumitas Muff and upstream of the EAE Longsword. In this rig the Brothers AM is the **drive platform** — the box that takes the dense fuzz wall coming out of the MXR 108 → Hizumitas pair, tightens and re-gains it, and hands a clean, line-level, sculpted signal to the Longsword to stack on top of. Rig art marks it "Channel B-into-A always-on" (the front board's always-on overdrive stage), and crucially it is **MIDI-capable** — this is the 2025 Analog Man collaboration, not the 2017 original. That last point reshapes a lot of this document, so read Section 1 first.

## 1. Lineage: original Brothers → Brothers AM (and why the difference matters here)

There are **two completely different pedals** both called "Brothers," and the rig owner has the second one. Getting this straight is the whole game:

- **Original Brothers (2017, ~$349).** Chase Bliss's first dirt pedal. Two dissimilar channels — one **JFET**, one **TL072 op-amp** (the same IC family as a Klon) — each with a 3-way **boost / overdrive / fuzz** toggle, giving nine mode combinations. It had a real **routing toggle** (Channel A pushes B, B pushes A, or **parallel with a blend knob**), plus ramping, expression, and a MIDI-in jack. Per [Premier Guitar's original Brothers review](https://www.premierguitar.com/gear/chase-bliss-audio-brothers-review), it carried six knobs, four jacks, and 22 switches. It was a polarizing pedal — some loved it, some never connected with the circuits.
- **Brothers AM (2025, $399).** A five-years-in-the-making collaboration with **Mike Piera of Analog Man**, built from the ground up around the legendary, scarce **King of Tone** (KOT) overdrive — itself a modified Marshall **Bluesbreaker** circuit — plus a bonus **Beano Boost**-style Rangemaster treble booster. Per [Guitar World's interview](https://www.guitarworld.com/gear/guitar-pedals/analogman-chase-bliss-brothers-am-interview), Joel Korte reached out to Piera in early 2020; the germanium-flavored treble booster ended up using silicon transistors in vintage TO-18 packages sourced partly from Tokyo's Akihabara district.

The single most important structural fact, **straight from the AM manual**: the AM is **three circuits in series** — `BOOST → CHANNEL 1 → CHANNEL 2` — in a **fixed order, series only**. Each channel's modes are now **BOOST / OVERDRIVE / DISTORTION** (manual, "Controls – Modes"). **There is no "fuzz" mode and no parallel/blend knob on the AM.**

> ⚠️ Reconcile with the brief and the Hizumitas dossier. The task brief described "boost / drive / **fuzz**," "series **or parallel**, in either order, with **blend**" — that accurately describes the **original 2017 Brothers**, not the AM the owner actually owns. The Hizumitas dossier likewise says to "run Brothers Channel A clean-ish, Channel B with a small amount of breakup, **blend**." On the AM there is no blend control to do that with — the channels stack in series. The *spirit* of that advice (one channel clean-ish as a tightener, the other adding a touch of grit, the pair used as a drive platform) is still exactly right; the *mechanism* is series stacking, not a parallel blend. This dossier corrects the mechanics and keeps the intent.

So in this rig: KOT-grade transparent overdrive, two stages of it, with a Rangemaster on the front, full preset/MIDI/CV/expression control, and a fixed series topology.

## 2. Controls & dip switches (from the manual)

Six knobs, three mode toggles, two footswitches, and two banks of dip switches. All of the following is sourced from the **Brothers AM manual** (CBA + AM ref 2025 – BAM01) unless noted.

**Knobs** (manual, "Controls – Knobs"):
- **GAIN 1 / GAIN 2** — saturation amount per channel; also nudges overall level.
- **VOL 1 / VOL 2** — output loudness per channel. With both channels on, **VOL 2 sets the final output** and VOL 1 becomes a tool to *push Channel 2 harder*. Manual warning: once Channel 2 turns off, output jumps to whatever VOL 1 is set to — hence the **MASTER** dip (below).
- **TONE 1 / TONE 2** — brighten/darken each channel's voicing.
- Each channel also has a **hidden PRESENCE** control: hold that channel's footswitch and turn its TONE knob to set it. Default/recommended is **PRESENCE fully down**.

**Mode toggles** (manual, "Controls – Modes"), per channel:
- **BOOST** — clean boost capable of low-gain overdrive; clearest, loudest. For clean lifts, stacking, or pushing an amp/another drive.
- **OD / OVERDRIVE** — the classic King of Tone voice; soft-clipping, natural, open, preserves the instrument's character. The edge-of-breakup sound.
- **DIST / DISTORTION** — hard-clipping; more compression and saturation but retains clarity. The "full-on, blown-out" voice.
- Manual caveat: each mode is a different volume (a clipping side effect — more distortion = more compression = different perceived level). Expect level jumps when switching modes; rebalance with VOL.

**Treble Booster toggle** (center, 3-position; manual, "Controls – Modes" / "Treble Booster"). **Linked to and engaged by Channel 1, sitting at the very front of the circuit.** Up = the brighter/cutting "more forward and bright" option; **middle = OFF** (gives you the pure classic KOT with no Rangemaster, which the original KOT didn't have); down = the classic **Rangemaster** voice with heavy upper-mid emphasis.

**Footswitches** — tap each to toggle its channel; **tap both at once to swap between channels** (manual, "Two-Channel Ideas"). Hold a footswitch to set that channel's PRESENCE.

**Presets** (manual, "Presets") — left and right toggle positions store a preset; middle is the live state. Save by holding the right footswitch 3 sec, then the left 3 sec (reverse for the left slot). Factory default bank: **THE ANALOG MAN** (Mike Piera's preferred KOT settings, HI GAIN 1 on — a solid always-on starter) and **SUNNY SKIES**. Flipping the **BANK** dip exposes two more (**2-IN-1**, **BAD BROS**), for **4 onboard presets**, plus up to **122/128 more via MIDI**.

**CUSTOMIZE dip bank** (pink, manual "Customize"), per-channel where noted:
- **HI GAIN 1 / HI GAIN 2** — adds ~**25%** gain to all modes on that channel; bypass LED turns red.
- **MOTOBYP 1 / 2** — "momentary to bypass": footswitch only engages while held (momentary boost/kill).
- **PRES LINK 1 / 2** — Presence-link: the TONE knob then controls TONE *and* PRESENCE together (more open/transparent; good for full-range/synth sources).
- **MASTER** — turns **VOL 2 into a global master volume**; VOL 1 then only acts when both channels are on. This is the recommended fix for volume jumps when boost-stacking.
- **BANK** — switches to the alternate preset bank (Presets 3 & 4). Dip settings are saved with presets.

**CONTROL dip bank** (for **CV / Expression**, manual "External Control"): choose which knob(s) to control, set polarity (response direction), and set the **range** — the knob's current position divides the sweep into a **(T)op** or **(B)ottom** half via the SWEEP dip.

## 3. Sonic character of each mode and the stack

**BOOST.** The cleanest, loudest circuit. As a transparent clean boost it just makes the signal bigger and a touch more present; pushed, it tips into low-gain overdrive. In this rig its most valuable job is **clean make-up gain and a level lever** — re-establishing line level and headroom after the Hizumitas, or pushing the *other* channel/the Longsword harder.

**OVERDRIVE (the KOT voice).** This is the heart of the pedal and the reason it's here. [Guitar.com's review](https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-brothers-am/) says it "perfectly nails that edge-of-breakup sound" and keeps "that King Of Tone DNA." Soft-clipping, open, dynamic, **not** mid-honky like a Tube Screamer — [Premier Guitar](https://www.premierguitar.com/gear/reviews/chase-bliss-brothers-am-review) explicitly notes it's "less midrange-heavy than vintage TS9 overdrives." It preserves the instrument's character rather than stamping its own on top, which is exactly what you want from a *shaper* sitting after a Muff.

**DISTORTION.** Hard-clipping, more compression and saturation, but it "retains clarity" (manual). PG flags "heavily colored compression at the highest gain levels" — true, and useful: that compression is what tames the ragged, gated Hizumitas tail into something more sustained and even.

**The treble booster** is the secret weapon for this rig (see Sections 5–6). [PG calls it "addictive, dynamite."](https://www.premierguitar.com/gear/reviews/chase-bliss-brothers-am-review) Because it sits at the very front and feeds Channel 1, it shapes everything after it — and its Rangemaster mode emphasizes upper-mids exactly where banjo and baritone need cut.

**The stack.** Run both channels and Channel 1 overloads Channel 2; the manual's "Stacking Ideas" (OVERLOADER, EXPANDER, COMBO) all describe progressively cranking VOL 1 to push Channel 2 past where it goes alone. This is genuinely a "crackling stream of overflowing gain" (manual, Overview) when you want it — but it's a **series** push, not a parallel blend.

## 4. Dynamic behavior (cleanup, stacking, compression, series feel)

The KOT's reputation is built on **touch sensitivity** and clean-up, and the AM keeps it. PG calls the pedal "touch responsive" and praises that it "avoids muddiness at low volumes." In **BOOST** and **OVERDRIVE** it cleans up beautifully with guitar-volume rolls and lighter picking — far more than the Hizumitas does. In **DISTORTION**, and especially with **HI GAIN** on, the "heavily colored compression" PG flagged sets in and the cleanup window narrows; that's the trade for saturation and sustain.

**Series feel.** Because the topology is fixed series, stacking on the AM is *additive and directional* — Channel 1's output (and the booster's) genuinely drives Channel 2's input, so the interaction is more like cascading amp stages than two parallel voices summed. The practical upshot: small VOL 1 moves have a large effect on Channel 2's saturation. Use the **MASTER** dip so those pushes don't also throw your stage level around (manual's explicit recommendation while boost-stacking).

Where this matters most in the rig: the Hizumitas hands the AM a **already-compressed, dense** signal. Stacking a lot of AM distortion on top of that compounds compression and can get squishy. The rig-correct move is the *opposite* of maximum gain — use the AM mostly as a **clean/low-gain tightener** (Section 5).

## 5. Signal-chain placement — why it sits AFTER the Hizumitas

The chain is `VG-800 → Polytune → CB Clean → Colour Box V2 → MXR 108 → Hizumitas → **Brothers AM** → Longsword → Oxford → BF-3 → …`. Placing a KOT-style platform *after* the Muff (rather than before) is the deliberate, correct architecture for this rig:

- **It tightens and re-gains the Muff wall.** The Hizumitas is a mid-forward, sometimes-loose, gated-tail Muff. Running the AM in **BOOST or low-gain OVERDRIVE** after it acts as a post-fuzz EQ-and-level stage: TONE 2 / PRESENCE sculpt the upper mids the Hizumitas Tone knob can't reach, and the soft-clipping rounds off the Hizumitas's ragged decay into something more sustained. This is precisely the "Brothers as a clean-ish boost/EQ shaper after the Hizumitas will tighten the low end" role the Hizumitas dossier calls for — just executed via series staging, not a blend knob.
- **It re-establishes line level for everything downstream.** The Muff's output is hot and uneven; the AM's VOL (with MASTER on) gives you a clean, predictable level handed to the Longsword and the whole modulation/time chain after it. The Hizumitas dossier is right that "time/modulation downstream wants a stable, line-level source" — the AM is what *makes* it stable.
- **It feeds the Longsword deliberately.** The EAE Longsword is a high-gain "wall." Stacking it on top of an already-saturated Muff is destructive-in-a-good-way, but it over-saturates fast. Use the AM's BOOST as a **clean push into the Longsword** (more cut, not more mush), and keep the Longsword's own gain low. The AM is the tool that lets you drive the Longsword *cleanly* instead of just piling fuzz on fuzz.
- **Treble booster placement is automatic and useful here.** Because the AM's booster is at the very front of the AM (not the chain), it lifts upper-mids *into* the AM's own stages — handy when the Hizumitas has darkened the banjo too far and you need the chord to read again before the Longsword.

Order note: the rig runs `108 → Hizumitas → AM`. If you ever want the AM to shape the *raw* fuzz wall before the Muff smooths it, the AM could go before the Hizumitas — but its current slot (cleaning up *after* the densest dirt) is the higher-value position and should stay.

## 6. Source-specific (banjo, baritone, VG-800, bass)

Everything the AM sees has already passed through the **VG-800** (modeled/divided source) and two fuzzes, so it never sees a raw pickup — it sees a hot, modeled, already-distorted signal.

- **Gold Tone EBM-5 banjo (GK-5 → VG-800).** Banjo is piercing and transient-heavy; the Hizumitas darkens it, sometimes too far. The AM's **treble booster (Rangemaster mode)** and **PRESENCE/TONE** are the recovery tools — dial cut *back in* at the upper-mids so the banjo-as-lead survives the downstream chain. Keep AM gain low here; banjo doesn't need more saturation, it needs **articulation and level**.
- **Baritone Jazzmaster (GK-5 → VG-800).** Closer to home for a KOT-style drive. The OVERDRIVE mode's tightness keeps the low strings from going flabby after the Muff. Use **HI GAIN** sparingly — the baritone's low end plus Muff plus AM distortion compounds fast.
- **Modeled VG-800 output.** Because the AM is fed a modeled cab/amp signal, OVERDRIVE/DISTORTION re-clip an already-saturated source. For the owner's "recorded-wrong" aesthetic that's a feature; for clarity, lean on **BOOST + PRES LINK** (TONE controls TONE+PRESENCE together) for the most open, full-range response — the manual specifically recommends PRES LINK "when using full frequency instruments like a synth."
- **Bass (Jazz Bass, or low VG-800 patches).** KOT-style drives are bass-friendly; the BOOST/OD modes add grit without collapsing low end. DISTORTION + HI GAIN will compress the bottom — use the MASTER dip to keep level sane.

## 7. Famous users (honest)

The AM landed in **2025**, so it has no developed artist mythology yet. The honest lineage is **the King of Tone's** user base, inherited by association: the KOT is one of the most waitlisted overdrives ever, famously used by countless session and touring players (its scarcity is the whole reason the AM exists). The AM's marquee "user" is effectively **Mike Piera himself** — his preferred settings ship as the **THE ANALOG MAN / "Mike's Sound"** factory preset ([Guitar World](https://www.guitarworld.com/gear/guitar-pedals/analogman-chase-bliss-brothers-am-interview)). Don't claim specific touring artists on the AM specifically; that data doesn't exist yet honestly.

## 8. Live / power / I/O notes

- **Power (manual):** 9V DC center-negative, **at least ~200 mA**. This is a high-draw Chase Bliss digital-control pedal — give it a healthy isolated 9V slot, not a daisy chain. **Do not exceed 9V** (manual: higher voltage risks damage).
- **Bypass:** **True bypass** (Chase Bliss spec), with **momentary (MOTOBYP) or latching** options per channel via dip.
- **I/O:** **Mono in / mono out**, 100% analog audio path (the digital side is control only).
- **External control (manual, "External Control"):** **CV** (floating-ring TRS, 0–5V — negative/over-voltage can damage it), **Expression** (TRS), **External footswitch** (TS, normally-open), and **MIDI**.
- **MIDI — verified, and it corrects the GearProfile.** The AM **does support MIDI** (Program Change + Control Change over every parameter) **via a Chase Bliss MIDIbox** to convert MIDI to the 1/4" TRS jack (manual, "External Control"; [chasebliss.com/brothers-am](https://www.chasebliss.com/brothers-am)). The rig-design.html correctly tags it **MIDI**. ⚠️ The current `GearProfile.md` front-matter says `midi: false` and `expression: true` — the `midi` flag is **wrong for this pedal** (it should be true, with the MIDIbox caveat); expression is correct. The brief's hypothesis that "the original Brothers AM is NOT MIDI" is **incorrect for the 2025 AM** (it likely conflated the older original Brothers' more limited MIDI-in). I did not modify the GearProfile per instructions, but flag it for correction.
- **Dimensions:** Not stated in the AM manual or current spec page; the original Brothers used a standard **125B** (~4.8 × 2.6 × 1.56 in / 122 × 66 × 40 mm) and the AM appears to use the same form factor, but I could **not verify exact AM dimensions** from a primary source — treat 125B as likely-but-unconfirmed.

## 9. Pairing recommendations (this rig, by name)

- **After Hizumitas (the core job):** AM in **BOOST** or **low-gain OVERDRIVE**, GAIN low, as a post-Muff tightener/EQ. PRESENCE up slightly to recover cut lost to the Muff's darkening. MASTER dip on so level stays put.
- **Into the Longsword:** AM **BOOST** as a clean push; keep Longsword gain low and let the AM provide cut and level, not more fuzz.
- **With the Oxford Drive:** redundant if the AM is already overdriving — treat Oxford as a one-button "brick everything" intensifier rather than a tone shaper this far down the chain (consistent with the Hizumitas dossier's read).
- **Treble booster + banjo:** Rangemaster mode to claw banjo articulation back before the Longsword.
- **External control / ramping:** No raw signal here is wasted — assign **EXP or CV to GAIN 1 or VOL 1** (via the CONTROL dip bank) for swelling the *push into Channel 2* during a sustained drone; with the MASTER dip on, you can ramp saturation without a level spike. The owner's deep Chase Bliss MIDI ecosystem (Clean, Generation Loss, Big Time, MOOD MkII, Blooper, Onward) means a **MIDIbox** can fold the AM into the same preset/automation scheme as the rest of the boards — verify MIDIbox is on hand.
- **Upstream CB Clean:** its buffer is fine in front of the AM (the AM is not a finicky fuzz front-end); no impedance issue.

## 10. Reviews & demos (real links)

- [Premier Guitar — Brothers AM review](https://www.premierguitar.com/gear/reviews/chase-bliss-brothers-am-review) — best on the "subtle to vicious" range, the treble booster, and the high-gain compression caveat.
- [Guitar.com — "The Big Review" Brothers AM](https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-brothers-am/) — best on the KOT-DNA / edge-of-breakup verdict and the price discussion ("half of what a King Of Tone will cost").
- [Guitar World — How Analog Man and Chase Bliss joined forces on Brothers AM](https://www.guitarworld.com/gear/guitar-pedals/analogman-chase-bliss-brothers-am-interview) — the development story, Beano Boost/TO-18 transistor sourcing, Bluesbreaker lineage.
- [Guitar.com news — KOT "expanded counterpart" announcement](https://guitar.com/news/gear-news/chase-bliss-analog-man-brothers-am-king-of-tone/) — the official framing.
- [Guitar Pedal X — Brothers AM / KOT / Beano Boost blog](https://www.guitarpedalx.com/news/gpx-blog/the-much-anticipated-chase-bliss-x-analogman-collaboration-is-with-us-an-updated-brothers-variant-covering-the-analogman-kot-and-beano-boost) — feature breakdown vs the original.
- [AndyDemos — Chase Bliss Brothers AM (Analog Man Collab) (YouTube)](https://www.youtube.com/watch?v=3_ffkecEoFQ) — practical two-channel/stacking walkthrough. *(Verified via yt-dlp: this is **AndyDemos**, not Chase Bliss's official channel — earlier draft mislabeled it as the official walkthrough.)*
- [Chase Bliss (official) — Brothers AM – Technical Demo (YouTube)](https://www.youtube.com/watch?v=YSv2JOXf26Y) — the genuine official deep-dive: modes, hidden Presence, dips, MASTER, external control.
- [That Pedal Show — "The New King Of Tone?" Brothers AM vs Prince of Tone & MXR Duke of Tone (YouTube)](https://www.youtube.com/watch?v=9B-1QH8nqi4) — A/B against the KOT family.
- [Premier Guitar — original Brothers (2017) review](https://www.premierguitar.com/gear/chase-bliss-audio-brothers-review) — for the JFET/op-amp, fuzz-mode, parallel-blend original (lineage reference only).

## 11. Mods / quirks / firmware / known issues

- **Three internal trim pots** (manual, "Internal Trimmers"), all for the **treble booster**: **(1) Input Impedance** (default fully CW / max; lower it counter-clockwise so the booster "behaves much better after a buffer" — relevant since CB Clean/Colour Box buffers are upstream), **(2) Output level** (default noon; CW hits the KOT circuits harder, CCW for a more "unity" feel), **(3) Bias** (default noon; squeezes more headroom or a more symmetrical Rangemaster break-up). Use a *very* small flathead and tiny movements — easy to damage.
- **Mode-to-mode volume jumps** are inherent (clipping side effect) — rebalance VOL or use presets.
- **VOL 1 level-jump trap:** turn Channel 2 off and output snaps to VOL 1's setting; the **MASTER** dip is the fix. Know this before going live.
- **PRESENCE defaults fully down** and is "hidden" (hold-footswitch-+-TONE) — easy to forget it exists.
- **High current draw (~200 mA):** a real power-budget consideration on a crowded board.
- **MIDI needs the MIDIbox** — not native 5-pin/USB; you must own the converter to get MIDI in.
- No widely reported reliability problems as of writing; build quality is standard Chase Bliss (excellent). The pedal is new (2025) so long-term field data is thin.

## 12. Spec sheet

| Spec | Value |
|---|---|
| Model | Brothers AM (CBA + AM ref 2025 – BAM01) |
| Type | Dual-channel analog overdrive/distortion/boost + treble booster |
| Channels | 2 identical, multi-mode, **series** (Boost → Ch1 → Ch2, fixed order) |
| Modes per channel | Boost / Overdrive / Distortion |
| Treble booster | Rangemaster-style (Beano Boost-inspired), 3-pos: bright / OFF / classic Rangemaster; front of circuit, linked to Ch1 |
| Knobs | Gain 1/2, Vol 1/2, Tone 1/2 (+ hidden Presence per channel) |
| Presets | 4 onboard (2 banks); up to ~122/128 more via MIDI |
| Power | 9V DC center-negative, **≥ ~200 mA** (do not exceed 9V) — *manual* |
| Bypass | True bypass; momentary (MOTOBYP) or latching per channel |
| I/O | Mono in / mono out; 100% analog audio path |
| External control | MIDI (PC+CC, via Chase Bliss **MIDIbox**), CV (0–5V, floating-ring TRS), Expression (TRS), ext footswitch (TS, N.O.) |
| Internal trims | Treble-booster Input Impedance / Output / Bias |
| Dimensions | **Not verified** (original Brothers = 125B, ~122 × 66 × 40 mm; AM presumed similar) |
| Price | $399 USD |

Sources: Brothers AM manual; [chasebliss.com/brothers-am](https://www.chasebliss.com/brothers-am); [Premier Guitar](https://www.premierguitar.com/gear/reviews/chase-bliss-brothers-am-review).

## 13. Starting-point settings

Clock-face positions, looking down at the pedal. Channel 1 = right-side knobs (GAIN 1/VOL 1/TONE 1), Channel 2 = left side, per the manual's layout.

**(a) Clean tightener after the Muff** — the rig's default always-on job
- Channel 2 only ON, mode **BOOST** (or low **OVERDRIVE**); Channel 1 off.
- GAIN 2: 9 · VOL 2: noon (level-match the Hizumitas bypassed/engaged) · TONE 2: noon, then taste.
- Treble booster: **OFF** (middle) unless banjo needs cut, then Rangemaster.
- **MASTER** dip ON. PRESENCE down. Goal: tighten, re-level, add cut — *not* more gain.

**(b) Dual-stacked wall** — both stages, into the Longsword
- Channel 1 **BOOST**, Channel 2 **OVERDRIVE** (or DIST). Channel 1 pushes Channel 2.
- GAIN 1: 9 · VOL 1: 1–2 (this is your push amount) · GAIN 2: 11 · VOL 2 (=MASTER): to taste.
- Treble booster: bright/up for cut. HI GAIN as needed. Keep the Longsword's own gain low downstream.

**(c) "Parallel blend" intent, done in series** — clean-and-dirty character (the Hizumitas dossier's idea, AM-correct)
- Channel 1 **BOOST** clean-ish (GAIN 1 ~8, VOL 1 modest), Channel 2 **OVERDRIVE** with light breakup (GAIN 2 ~10).
- You can't literally blend, but low Channel-1 push + moderate Channel-2 OD gives the *clean-foundation-plus-grit* result. Add **PRES LINK** on Ch2 for openness. MASTER on.

**(d) Ramped swell** — drone build via external control
- Channel 2 **OVERDRIVE/DIST** as the bed; assign **EXP (or CV) to GAIN 1 or VOL 1** via the CONTROL dip bank, polarity so heel = no push, toe = full push.
- MASTER dip ON so the ramp adds *saturation/intensity* without a level spike. Sweep up into a sustained chord/banjo drone before the Longsword and the End Board's granular/reverb stages chew on it.

## 14. Versus alternatives (why it earns its slot)

- **Original Chase Bliss Brothers (2017).** The "blend + fuzz mode" pedal the brief half-described. Reach for it if you genuinely want **parallel blending** and a **fuzz** mode in the dual box. The AM trades those for KOT-grade transparent overdrive, the treble booster, full MIDI/CV, and (per Guitar.com) far easier usability. For *this* rig — where fuzz is already covered by the 108 + Hizumitas and the job is a clean, transparent **tightener/platform** — the AM is the better tool, not the original.
- **Analog Man King of Tone (the source).** The AM is "half the price of a KOT" and available now, with on-the-fly mode access, presets, and external control the KOT can't offer. The KOT is the holy grail of transparency; the AM gets ~95% there with vastly more flexibility. No contest for a routing-heavy, MIDI-integrated board like this.
- **Generic dual-drive platforms (e.g. JHS stacked drives, the owner's benched JHS Kilt).** None match the AM's KOT voicing *plus* preset/MIDI integration into the existing Chase Bliss ecosystem (Clean, Generation Loss, Big Time, MOOD MkII, Blooper). That ecosystem fit is a real, rig-specific reason the AM earns the slot over a cheaper two-in-one.
- **A single transparent OD (Timmy, OD-ish boxes).** One stage, no second channel, no treble booster, no external control. The AM's whole value here is being a **two-stage platform** that can be a clean tightener *and* a wall *and* a ramp target — a single OD can't cover that range after a Muff.

In this rig — banjo/baritone through a modeled VG-800, Muff wall upstream, Longsword wall downstream, deep Chase Bliss MIDI ecosystem all around it — the Brothers AM earns its always-on slot because it's the one box that can (1) tighten and re-level the Hizumitas, (2) cleanly push the Longsword, (3) restore banjo cut via the treble booster, and (4) fold into the rig's preset/automation scheme via MIDI/CV. It's the platform, not just a drive.

## Sources

- Chase Bliss — *Brothers AM* manual (CBA + AM ref 2025 – BAM01), local copy: `manuals/Brothers+AM_Manual_Pedal_Chase+Bliss.pdf` — **authoritative for routing, modes, dips, controls, external control, power.**
- [Chase Bliss — Brothers AM product page](https://www.chasebliss.com/brothers-am)
- [Premier Guitar — Chase Bliss Brothers AM Dual Overdrive Review](https://www.premierguitar.com/gear/reviews/chase-bliss-brothers-am-review)
- [Guitar.com — The Big Review: Chase Bliss Brothers AM](https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-brothers-am/)
- [Guitar.com — Chase Bliss & Analog Man unveil Brothers AM (KOT)](https://guitar.com/news/gear-news/chase-bliss-analog-man-brothers-am-king-of-tone/)
- [Guitar World — How Analog Man and Chase Bliss joined forces on Brothers AM](https://www.guitarworld.com/gear/guitar-pedals/analogman-chase-bliss-brothers-am-interview)
- [Guitar Pedal X — Brothers AM / KOT / Beano Boost blog](https://www.guitarpedalx.com/news/gpx-blog/the-much-anticipated-chase-bliss-x-analogman-collaboration-is-with-us-an-updated-brothers-variant-covering-the-analogman-kot-and-beano-boost)
- [Premier Guitar — original Chase Bliss Brothers (2017) review](https://www.premierguitar.com/gear/chase-bliss-audio-brothers-review) (lineage reference)
- [Chase Bliss — Brothers AM (Analog Man Collab) demo (YouTube)](https://www.youtube.com/watch?v=3_ffkecEoFQ)
- [Brothers AM – Technical Demo (YouTube)](https://www.youtube.com/watch?v=YSv2JOXf26Y)
- [Brothers AM vs Prince/Duke of Tone (YouTube)](https://www.youtube.com/watch?v=9B-1QH8nqi4)
- Internal rig docs: `rig-design.html` (Board 1 signal flow, MIDI tag), `Gear/Chase Bliss Brothers AM/GearProfile.md`, `Gear/EarthQuaker Devices Hizumitas/research/Hizumitas-DeepResearch.md`
