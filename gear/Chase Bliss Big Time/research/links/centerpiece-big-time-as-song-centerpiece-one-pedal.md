https://www.chasebliss.com/big-time + https://www.electronicaudioexperiments.com/blog/2026/4/29/big-time
chasebliss.com (product page) + EAE blog (John Snyder) + official Walkthrough (YT QY389WFTXgY) + Mark Johnston "Secret Weapons" deep-dive (YT 2kfrZbEbRY8) · accessed 2026-06-03

# Big Time AS A SONG CENTERPIECE — carrying a whole part on one pedal

Goal-driven distillation for the owner's plan: make the Big Time the centerpiece for a few
songs, minimal chain in, maximize the one pedal. This file is the **"carry a song on the one
box"** playbook. Concrete settings are mostly **first-principles reasoning from the verified
control behavior** in the manual/dossier + the three captured demos — clearly labeled. It's a
June-2026 pedal, so almost nothing here is "Artist X did this on Record Y"; it's
"the pedal verifiably does this, here's how to build a part out of it."

> Verified-vs-reasoned key: **[V]** = stated on the product page / EAE blog / in a captured
> official-or-demo transcript. **[R]** = first-principles reasoning from verified control
> behavior (sound, not sourced). Settings expressed low→high on the faders.

---

## 0. The thesis, in Big Time's own words

- **[V]** Chase Bliss/EAE pitch it as **"not just a delay pedal — a chorus, a flanger, a
  reverb, a dirt pedal, a compressor and limiter, and some crazy combination of those
  things"** that **"all centers around delay"** (Secret Weapons). That's the centerpiece
  license: one box already spans the texture palette you'd otherwise spread across a board.
- **[V]** Snyder's design thesis (EAE blog + Secret Weapons): *"old digital technology was bad
  at its job… it needed help, and when you help it out you get unintended consequences — and
  the most beautiful thing in sound design is unintended consequences that lead you to a new
  place."* The Big Time is **built to be played as an instrument** ("I'm excited to make some
  music with it"), not just patched in as utility.
- **[V]** Two interconnected analog stages bookend the digital delay: a **stereo preamp** at
  the input (COLOR) and a **stereo analog limiter** in the feedback loop (STATE). **COLOR sets
  how hot you hit those stages; FEEDBACK sets how hard you keep hitting them over time.** That
  COLOR↔FEEDBACK↔limiter loop is the engine you "play" to carry a part (Walkthrough).

---

## 1. The reset you build everything from

- **[V] Press-and-hold the center MODE button → instant clean, simple, straightforward
  delay.** This is the single most useful live hack on the pedal: from anywhere in the deepest
  chaos, hold MODE to snap back to a sane delay and re-find your bearings (Secret Weapons).
  Treat this as your "home base" before sculpting a part.
- **[V] Preset 0** is the other jumping-off point — "a nice normal delay," a great base for
  everything (Secret Weapons). The motorized faders fly to position on recall.

## 2. Self-oscillation / feedback walls as a SOUND SOURCE

- **[V]** STATE chooses how the limiter behaves as feedback climbs:
  - **Digital** = *no limiter* → "runaway oscillations, massive volume spikes," cleanest output
    (use for a controlled clean swell, mind the level).
  - **Compressed** = "subtle compression… limited headroom to prevent blowing up your amp and
    runaway oscillations" → the **safe** self-oscillation wall; it holds itself together. EAE
    studied the **Lexicon PCM42's** mis-calibrated limiter to get "hyper-compressed,
    disintegrating infinite delays" here — this is the Blue/Compressed state's whole reason for
    existing (EAE blog).
  - **Saturated** = clips harder as you drive in → "degradation and break-up in the delay line."
  - **#!&% (misbias)** = "massive degradation… broken drifting delay lines," "vintage fuzz on
    your delay / broken-speaker" textures; when the bias fully gates "it's like you're burning a
    hole in the loop" (Walkthrough, Secret Weapons).
- **[R] Centerpiece feedback-wall recipe:** MODE **Long** · STATE **Compressed** (safe) or
  **Saturated** (gnarlier) · FEEDBACK above COLOR so repeats *climb* into the limiter ·
  COLOR ~30% · DIFFUSE high · CLUSTER high · WET set conservatively (these get LOUD — the demos
  warn repeatedly). Play one chord/note and let the wall build itself; ride COLOR/FEEDBACK by
  hand or expression to swell and recede. The TEXTURE alt (under COLOR) tunes each STATE's
  character — on Compressed it goes gentle-sustain → full ducking; on misbias it sets how broken.
- **[V] Performative one-stomp swell:** in a long-delay/feedback patch, **hold the RIGHT
  footswitch to ramp COLOR + FEEDBACK toward max** as a momentary effect ("beware volume").
  Stomp it to detonate a part's climax, release to fall back (Secret Weapons / manual).
- **[V] The "expensive boost"** edge case: pull **WET fully down** and the box is *just* the
  stereo analog preamp — a clean(ish) saturator/dirt with no delay at all. So one pedal also
  covers "the dirt before the part" if you want it.

## 3. Infinite HOLD / freeze — a pad you solo over

- **[V] Press-and-hold the RIGHT footswitch (Short/Long)** → freezes the buffer: nothing new
  gets in, the captured sound **revolves infinitely and stops degrading** (it switches to DSP
  feedback and "holds it forever"). With long times this works as a **phrase-freeze / quasi-
  looper** mid-song (Walkthrough, Secret Weapons).
- **[R] Centerpiece move:** play a chord or texture, freeze it into an infinite bed, then play
  a melody/lead over the held pad — the one pedal is simultaneously the drone and the delay on
  your live playing. Combine with DIFFUSE + CLUSTER for an ambient cloud to solo over.

## 4. Ramping / pitch dives & rises (motion + scale + time)

- **[V] MOTION** = modulation type: **Sine** (smooth chorus/vibrato of repeats), **Square**
  ("classic Thermae pitch jumps"), **Env** (envelope-following time bends from your dynamics).
  RATE/DEPTH live in the alt menu (under TIME/CLUSTER). DEPTH gets extreme fast — small moves
  go a long way (Secret Weapons).
- **[V] SCALE** quantizes both TIME moves and MOTION pitch to musical intervals: **Off**
  (smooth glides/detune), **Chromatic**, **Oct+4+5**, **Octave**. Because TIME is a *clock*
  control, dragging the TIME fader = **audible pitch dives/rises**; with SCALE on they snap to
  octaves/fifths instead of swooping (Walkthrough, Secret Weapons).
- **[V] Step / Thermae mode** (Options → under MOTION): turns the pedal into a **stepped
  pitch sequencer** — each TEMPO stomp steps through your scale; TIME sets how fast the steps
  move (legato vs snappy). With SCALE = Octave this is the "more mature Thermae" cascade Emily
  Hopkins and Mark Johnston both single out (Harp Lady, Secret Weapons).
- **[V] SCALE IGNORE** (Options): lets MOTION keep a smooth sine while TIME does the scaled
  transposition — "big octave steps with a nice sine modulation and none of the chaos." This is
  how you get *musical* pitch ramps without the whole pedal going feral (Secret Weapons).
- **[R] Centerpiece pitch-dive part:** sparse melodic source (banjo/OP-1 pluck/synth stab) →
  SCALE Octave + MOTION Square + moderate FEEDBACK → each note cascades into an arpeggiated
  octave ladder. The repeats do the melodic work; you just feed it single notes.

## 5. Multi-tap / rhythmic / stereo with CLUSTER (the "free arrangement" fader)

- **[V] CLUSTER has zones:** first it adds **one extra head**, then **a few more heads**, then
  it **modulates and diffuses them into something washy** (Walkthrough). In Short modes the
  extra taps read as **multi-tap rhythms**; in Long mode they become **separate delay lines
  drifting in/out of sync across the stereo field** (Secret Weapons).
- **[V]** Top of CLUSTER adds **ping-pong** to the *added* taps even while your core delay
  stays put — so you get wide bouncing rhythms layered over a centered main echo (Secret
  Weapons). **CLUSTER is also a stereo-image generator** ("bump it up if your field is narrow").
- **[V] Big Time as a reverb:** crank **CLUSTER + DIFFUSE** (alt, under FEEDBACK; DIFFUSE TYPE
  under VOICING) and the taps smear into a **diffuse reverb-like cloud** off a single delay
  line (Secret Weapons). One pedal = delay + reverb for the part.
- **[R] Rhythmic-centerpiece recipe:** MODE Short · SCALE off · TIME tapped/MIDI to the song ·
  CLUSTER ~⅓–⅔ for a multi-tap pattern · STATE Compressed for punchy articulate repeats ·
  SPREAD = blue (gentle widening) or ping-pong. Let the multi-tap pattern *be* the groove.

## 6. Lo-fi / generation-loss character on the one pedal

- **[V] 0.5X** (alt, under MODE): halves the clock → **2× the delay time, half the bandwidth,
  reduced bit depth** → "those nice artifacts," stereo Memory-Man-ish lo-fi. On Long + ping-pong
  you reach ~24 s of delay (Secret Weapons). **VOICING** sets the base filter: HiFi pristine →
  Focus (shaves highs+lows over time, "focused floating repeats") → Warm (primitive-rack
  elliptical ripple) → Analog (dark BBD). **TILT EQ** + its **CROSSOVER** alt sculpt the repeats
  independently; pushing TILT down boosts lows → *louder/longer* feedback tails (the low-end
  feeds the loop harder) (Secret Weapons).
- **[R]** For a whole degraded ambient piece: STATE Saturated + VOICING Warm/Analog + 0.5X on +
  DIFFUSE up + slow Sine MOTION → murky crumbling wash you can build a song bed from, no other
  pedal required.

## 7. The on-board looper as a composition layer (3.2 min)

- **[V]** MODE **Loop**. **In overdub the whole pedal is live** (saturation/modulation/feedback
  all apply, repeats fade like Blooper if FEEDBACK is low); **on playback it locks to DSP
  feedback and holds without degrading** (Walkthrough).
- **[V] Two looper voices:** **HiFi + TIME at noon** = clean ~45 s perfect loops; drop to
  **Focus/Warm/Analog** = a **sound-on-sound / tape-style looper that morphs and fades older
  layers away over time** (Secret Weapons). Push TIME to the top for **>3 min** of (very lo-fi)
  loop time; higher TIME = more fidelity but less time. **Hold STOP** returns TIME to center so
  you can speed up *and* slow down a recorded loop equally.
- **[V]** You can also **jump into Loop from Short/Long to freeze what you're already playing**
  into the buffer. Apply SCALE/MOTION/CLUSTER/DIFFUSE to loops too — "what if the Thermae was a
  stereo looper."
- **[R] Rig note:** with Blooper/MOOD/OP-1/Octatrack in the room, use Big Time's looper as a
  **performative phrase-freeze**, not the main song looper (dossier §5).

## 8. Stereo as a centerpiece tool (SPREAD)

- **[V] SPREAD** (alt, under MOTION): **off** = true stereo / dual-mono (L stays L, R stays R —
  feed it a stereo source and it preserves the image); **blue/on** = gentle stereo widening of
  the core delay (the demo's default + favorite); **ping-pong** = hard bouncing. Combine MOTION
  + CLUSTER for "incredibly wide delays without resorting to pure ping-pong" (Secret Weapons).

---

## 9. Four ready-to-go centerpiece patches (build, then save to a preset slot)

1. **Oceanic drone bed** *(carry an ambient intro/outro)* — Long · #!&% or Saturated · Analog ·
   slow Sine MOTION · FEEDBACK > COLOR · DIFFUSE + CLUSTER high · WET careful → hold RIGHT to
   freeze, play over the top. **[R]**
2. **Thermae cascade lead** *(the melodic hook)* — Short/Mod · SCALE Octave · MOTION Square ·
   SCALE IGNORE on for clean steps · moderate FEEDBACK → feed single notes, repeats arpeggiate.
   **[V on behavior / R on exact knobs]**
3. **Lo-fi rhythmic groove** *(the body of a song)* — Short · STATE Compressed · 0.5X on ·
   CLUSTER ~½ for multi-tap · TIME to the song tempo (tap/MIDI) · SPREAD blue. **[R]**
4. **One-stomp climax** *(the build/drop)* — Long · Saturated · TILT down (more lows → longer
   tails) → hold RIGHT footswitch to ramp COLOR+FEEDBACK into a wall, release to collapse.
   **[V]**

Save each as a numbered preset (10 onboard, 127 via MIDI) so a footswitch — or a MIDI Program
Change from the Digitakt/MPC — recalls a whole song section in one move (see the integration
file). **[V]**

## Sources
- https://www.chasebliss.com/big-time (centerpiece framing, modes, looper, Cluster, presets, MIDI)
- https://www.electronicaudioexperiments.com/blog/2026/4/29/big-time (Snyder: PCM42 "disintegrating infinite delays," limiter/preamp design, instrument intent)
- https://www.gearnews.com/chase-bliss-big-time/ ("perfect centerpiece for a synth setup," 3.2-min loop, balanced I/O)
- Captured transcripts (this folder): centerpiece-chasebliss-big-time-official-walkthrough.md · centerpiece-mark-johnston-big-time-secret-weapons-deep-dive.md · centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md
- Big Time dossier: Gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md (control reference, starting-point settings §13)
