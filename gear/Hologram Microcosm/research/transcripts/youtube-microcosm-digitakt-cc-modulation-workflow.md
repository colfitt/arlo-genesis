https://www.youtube.com/watch?v=dKsp6xwjLXc
YouTube · "Microcosm + Digitakt is a DREAM — MIDI Mapping, Modulation, & Routing Tutorial" · auto-caption transcript, distilled to prose

# Microcosm + Digitakt: modulating Microcosm knobs from Digitakt LFOs (concrete CC workflow)

The single most rig-relevant demo — exactly the Digitakt-drives-Microcosm pairing in the rig. The creator uses **Digitakt MIDI tracks + LFOs to modulate Microcosm parameters via CC**, treating the pedal as the Digitakt's missing effects/granular engine: "the Digitakt lacks a bit of effect potential, this thing fills that void; the Microcosm lacks a little modulation, [the Digitakt] can cover all of that."

## The exact mapping workflow (per Digitakt MIDI track)
1. On a Digitakt **MIDI track**, set the **output MIDI channel to 1** (Microcosm listens on Ch 1; he uses Ch 1 for all of them).
2. Set the track's **CC value number** to the Microcosm parameter you want (this is the key step). CCs he uses, read off the manual's CC list:
   - **Time = CC 10**
   - **Activity = CC 6**
   - **Repeats = CC 11**
   - (also mentions liking to send to **Filter** and **reverb/Space** level)
3. **Important re-trigger quirk:** "for some reason you always have to hit play again just to make sure it gets started" — after arming, stop/start transport so the CC stream begins. (Consistent with the pedal needing a transport kick.)
4. Assign the track's **LFO to "CC 1" (the CC-value destination)** and shape it: randomize for organic granulation, or a slow triangle/sine for a "gentle sway." "It's like my third or fourth hand."

## CLOCK-vs-CC gotcha (critical)
- To **modulate the Time knob via CC** rather than slave to clock, he goes into the Digitakt's **SYNC menu and turns OFF "Clock Send."** Reason: if the Digitakt is sending MIDI clock, the Microcosm slaves to it and **CC 10 (Time) no longer does anything** — clock overrides Time. So it's **either** clock-sync the subdivision **or** hand-modulate Time via CC, not both. Choose per use-case.

## Audio routing trick (mono-in → stereo-out widening)
- He routes only the granular-bound sounds to the **RIGHT side**, feeding a **mono signal into the Microcosm's mono input** — the Microcosm's effect/reverb "adds a lot of stereo imaging really nicely," so a mono source comes out wide. (In the rig we feed it true stereo, but this confirms the engines generate genuine stereo width even from mono.)
- The other tracks (beat + bass) go to the LEFT/other path entirely — keeping rhythm dry and only granulating the textural voices.

## Reverse love
- "I love the Microcosm in reverse setting — sounds beautiful." He flips the effect to reverse over the modulated granular bed for the payoff.

## Rig takeaways
- Use Digitakt MIDI tracks + LFOs on **CC 6 (Activity)** and **CC 11 (Repeats)** for hands-free evolving texture; a randomized LFO on Activity makes granulation feel organic.
- **Decide: clock-sync (subdivision locks) OR CC-modulate Time — not both.** If you want the Digitakt to *both* clock the rig *and* hand-modulate Time, you can't; clock wins.
