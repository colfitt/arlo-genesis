---
type: chain
title: "Hizumitas → Big Time Crushed Rhythmic Echo"
date: 2026-06-15
artists: [Boris, Trent Reznor]
instrument: "guitar / down-tuned guitar"
gear:
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
  - Elektron Digitakt 2
---

# Hizumitas → Big Time Crushed Rhythmic Echo ⭐

A three-box centerpiece where one hot fuzz feeds one clock-locked delay over a borrowed groove: bit-crushed multitap fuzz repeats that **duck under the riff and punch back the instant you stop**, all snapped to a dotted-8th grid. The Compressed STATE on Big Time is doing two jobs at once — it keeps the hot, sustaining Hizumitas from running away, and its VCA acts as a per-repeat ducker so the echoes stay out from under your attack and only bloom in the gaps. Early-'80s lo-fi grit on a clock.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

Guitar / down-tuned guitar → **EQD Hizumitas — "Baritone Drop-G# Tight Low"** → **CB Big Time — "Lo-Fi Rhythmic Groove"** (Short, Compressed, 0.5X ON, CLUSTER ~½, TIME slaved · CC54 dotted-8th) ← MIDI clock from **Elektron Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template"** → amp / tape. Mono fuzz → Big Time **IN-L** auto-engages **MISO** (mono-in/stereo-out); stereo from Big Time onward.

## Per-unit

- **EQD Hizumitas — "Baritone Drop-G# Tight Low":** the hot, defined down-tuned fuzz. Volume ~10:00 (near unity), Sustain ~75% (≈2:00–3:00), Tone toward the bass side for a round but **tight, defined low end** so the crush in the delay has clean transients to chop. The standout here is the treble-bleed-friendly volume-knob cleanup — roll the guitar volume down for the verse riff, push it back up to slam the repeats — which is what makes the "duck under the riff / punch back" dynamic land off the fingers as well as off the delay. *(Sustain ~75% and unity Volume are framed in Andy's Reverb Tone Report baritone demo; the exact Tone position is swept on camera, not published — dial Tone from the recipe.)*
- **CB Big Time — "Lo-Fi Rhythmic Groove":** MODE **Short**, STATE **Compressed** (VCA comp → the ducking-echo behavior, and the runaway-control under a hot fuzz), VOICING **Focus** (shaves highs+lows so the muff stays defined in the repeats), **0.5X ON** (the first-party **12-bit** sample-rate crush = the lo-fi grit), CLUSTER **~½** (the multitap pattern becomes the rhythm), **COLOR ~40%** kept modest because the fuzz already supplies the saturation, TILT EQ slightly up to cut muff mud, FEEDBACK **~35%** (articulate, not washy), WET **~40%**. **TIME is slaved** to the DT2 clock; **CC54** sets the subdivision to **dotted-8th**. *(The numeric fader positions are a designed interpretation of this patch's recipe — Chase Bliss publishes character, not numbers; on PC recall the motorized faders fly to the real saved values. STATE/0.5X/CC54 mechanics are sourced.)*
- **Elektron Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template":** the tempo engine. `SETTINGS → MIDI CONFIG > SYNC` → CLOCK SEND + TRANSPORT SEND ON; Big Time follows on shared ch.2. Sequence a groove (or just run the clock); use a MIDI track's CCs to p-lock COLOR/CLUSTER per section if you want the delay to thicken into the chorus.

## Routing

**DT2 = clock master, Big Time follows** (CC111 ignore off, CC54 sets the dotted-8th subdivision) — native 5-pin DIN, no MIDIBox needed. Pick ONE master; never loop clock. **Gain-staging is the whole point:** the Hizumitas is hot and sustaining, so keep Big Time **COLOR modest (~40%)** — too much COLOR plus a hot fuzz clamps the limiter "to porridge." Compressed STATE is the safe state under a sustaining fuzz and *is* the ducker, so you get the punch-back-when-you-stop motion for free; the dotted-8th CC54 lock is what turns CLUSTER's multitaps into rhythm against the riff. Mono fuzz → IN-L auto-MISO for stereo spread out. If the repeats ever run away, **hold MODE on the Big Time** for an instant clean reset.

## Sound

Bit-crushed, clock-locked multitap fuzz repeats that duck out of the way of the riff and bloom into a rhythmic, 12-bit-gritty cloud the moment you stop — early-'80s lo-fi grit on a dotted-8th grid, with a tight down-tuned low end that stays defined even crushed.

**Taste-ref:** down-tuned lo-fi grit / rhythmic-delay-as-hook (Boris/Wata sustaining fuzz weight + Reznor-era crushed, clock-locked repeats). ⚠️ The ducking is real (Compressed VCA), not a true sidechain key; the rhythmic lock is real (CC54 dotted-8th).

## Play

Set the DT2 tempo, start the clock. Play the riff with the guitar volume backed off so the repeats stay tucked under it; **stop, and the dotted-8th multitaps punch back** crushed and rhythmic in the gap. Push the guitar volume up to slam the delay for a fill. Ride **CLUSTER** live as the "more/less taps" fader, and **CC54** to flip the subdivision (dotted-8th ↔ 16th) for a double-time section. Hold MODE on the Big Time is your panic reset back to a clean delay.

## Sources

- **Basis:** designed integration; chains **Hizumitas "Baritone Drop-G# Tight Low"**, **Big Time "Lo-Fi Rhythmic Groove"**, and **DT2 "MIDI / Clock-Master Rig Template."** Compressed = ducking echoes that stay out from under your attack + the runaway-control under a sustaining fuzz, COLOR-modest fuzz→delay gain-staging, MISO auto-engage, 0.5X = first-party 12-bit crush, and DT2-master / CC111-ignore / CC54-subdivision (dotted-8th) are documented in `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` §3/§5 and `research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A/§C.
- `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md`
- `Patches/Chase Bliss Big Time/lo-fi-rhythmic-groove.md`
- `Patches/EarthQuaker Devices Hizumitas/baritone-drop-gsharp-tight-low.md`
- `Patches/Elektron Digitakt 2/dt2-midi-clock-master-rig-template.md`
