https://www.chasebliss.com/s/Big-Time_Manual_Chase-Bliss.pdf
chasebliss.com · Chase Bliss / EAE (official manual, "Factory Presets" pp.22–23) · accessed 2026-06-03

# Big Time factory presets — the 10 official recipe starting points

The closest thing to "published settings recipes" for the Big Time. There are **10 factory presets (slots 0–9)**, each described first-party as a *starter* for a use case. Recall via the preset menu (HOLD LEFT). You can always restore a factory preset by **holding MOTION + VOICING in the Preset Menu** — works even after you've saved over a slot. (Recall/save mechanics are covered separately in `cb-stack-preset-scene-recall.md`; this file = the actual sounds.) The manual gives *characters + intent*, not numeric fader positions — but because the Automatone faders fly to the saved positions, loading a preset and reading the sliders IS the recipe. Descriptions quoted verbatim.

| # | Name | Description (quoted) | "Use this as a starter for…" |
|---|------|----------------------|------------------------------|
| 0 | **NICE DELAY** | "A good ol' echo with a bit of modulation, long trails, and the preamp set on the edge of breakup." | "making simple delays." |
| 1 | **COMPRESSED CHORUS** | "Smooth modulation with a dreamy character, compressed to bring out the details." | "making classic modulation." |
| 2 | **SLAP/DOUBLE** | "A big, burly expander with two stages of clipping and room-like ambience." | "doubling and almost-real-time textures." |
| 3 | **SAGGING ECHOES** | "Immersive echoes with long, compressed trails that react to your playing." | "dynamic delays." |
| 4 | **BOUNCY THERMAE** | "An upbeat echo sequencer reminiscent of an old friend." | "exploring sequencing." |
| 5 | **BROKEN DYNAFLANGE** | "A starved flanger that fills the gaps between your notes with dynamic oscillations that react to your instrument's loudness." | "making unorthodox modulation." |
| 6 | **CLUSTER$%&!** | "A misbiased wash of swirling clusters – start with sparse playing and see where it takes you." | "exploring strange ambience." |
| 7 | **CRUSHED ANALOG** | "A murky, modulated, and saturated delay." | "making vintage echoes." |
| 8 | **NOSTALGIC REPEATER** | "A cozy looping delay that crumbles and quivers, with no dry signal." | "malfunctioning echoes and Frippertronics looping." |
| 9 | **LOOP DIFFUSER** | "A slowly dissolving delay with infinite feedback – play a few notes, sit back, and see what happens." | "musical drones and slow-building atmosphere." |

## Which presets map to THIS rig's aesthetic (drone/doom/shoegaze, degraded)
- **#7 CRUSHED ANALOG** — the bread-and-butter End-Board voice. Murky + modulated + saturated = exactly the "recorded-wrong" tape echo to feed after Generation Loss. Start here.
- **#9 LOOP DIFFUSER** — the oceanic single-chord-forever drone (infinite feedback, slowly dissolving). The "play a few notes, sit back" doom wall; feed into H90 hall.
- **#8 NOSTALGIC REPEATER** — crumbling/quivering loop, **dry killed** already → pure degraded repeats, "Frippertronics" looping. On-aesthetic and pre-configured with no dry.
- **#6 CLUSTER$%&!** — misbiased (#!&% STATE) swirling-cluster wash for "strange ambience"; the chaotic banjo-cascade fuel.
- **#4 BOUNCY THERMAE** — the pitched/sequenced echo (Snyder's "reminiscent of an old friend" = Chase Bliss Thermae); the banjo-as-lead arpeggiated-cascade starting point. Pair with SCALE = Octave / Oct+4+5.
- **#3 SAGGING ECHOES** — dynamic, playing-reactive compressed trails (Compressed STATE); good ducking-delay under vocals/lead.

## First-party dial-in mechanics (manual, "State and Limiter" pp.34–35) — how to build your own recipe
The **STATE button** sets the limiter role; the **TEXTURE** alt-fader tunes each state. This is the core of any recipe:
- **DIGITAL** — "No limiter… completely digital feedback path, useful when you want cleaner textures and stable, steady feedback (when looping, for example)." TEXTURE "introduces aliasing and lowers the bit depth."
- **COMPRESSED** — "Clean compression and sag… snappy repeats with extra punch, or glitchy modulation that sags and falters, or endless trails that duck out of the way when you play." TEXTURE "sets the amount of compression, from a subtle squeeze to ducking sag."
- **SATURATED** (the default state) — "echoes that slowly disintegrate and expand into a big harmonic mass. Use it for colorful degradation, churning oscillation, and cutting ambience." TEXTURE "controls the symmetry of the clipping, becoming more ragged as it's turned up."
- **#!&%** (misbias) — "sabotages and misbiases the limiter… a raw, electric character… broken and obliterated sounds, lively soundscapes, and textural sound design." TEXTURE "sets the sensitivity of the misbiasing."

**Gain-structure recipe rule (manual pp.24–25, quoted):** "COLOR sets the loudness of the signal before it enters the delay line, FEEDBACK sets the loudness of the signal within the delay line." High COLOR → "echoes bonk into the limiter immediately." Low COLOR + high FEEDBACK → echoes "gradually climb… until eventually the echoes encounter the limiter and begin to transform and settle into a 'maximum loudness'" — "where you find the most change over time… also real loud and scary if you're not expecting it." Set WET conservatively for the climb.

**MODE "try this" tips (manual pp.26–27):**
- LONG mode: "Turn up DIFFUSION and CLUSTER to explore some long-form ambient haze (changing STATE to Saturated won't hurt either)."
- SHORT mode: "Max out TIME to underclock Big Time and introduce just a touch of crispy aliasing."
- HOLD RIGHT (Short/Long): freezes/loops current sound infinitely, play overtop.
- OVERLOAD (HOLD RIGHT, also): "Ramps both COLOR and FEEDBACK up to the max (beware volume levels!)."
- CLUSTER note: "Because CLUSTER is creating additional echoes, it will also increase the gain in the delay line. As you turn CLUSTER up you may wish to decrease FEEDBACK to compensate."

**VOICING + TILT EQ (manual pp.38–39):** HiFi "clear and pure"; Focus "subtle filtering… focused floating repeats"; Warm "emulates… primitive digital rack delays… signature elliptical ripple"; Analog "dark and rich… BBD-based analog delay." Manual's own combo tips: "set VOICING to Analog and push up the TILT EQ to create narrow but characterful echoes that slice right through the middle"; "Maybe you want to cut the mud from your bass" (push TILT EQ up); "have echoes that float overtop of the vocals" (push TILT EQ up + CROSSOVER up).
