https://www.chasebliss.com/s/Clean_Manual_Pedal_Chase-Bliss-th6p.pdf
chasebliss.com (Clean manual, pp. 8-9, 22-23, 30-37) · Chase Bliss · accessed 2026-06-03 (read from repo copy: manuals/Clean_Manual_Pedal_Chase+Bliss.pdf)

# Chase Bliss CLEAN — official published recipes (the authoritative recipe source)

CB's own "Compression Ideas" spread (manual pp. 22-23) gives THREE named starting-point recipes with stated ratios + the three center toggle positions. These are the closest thing to canonical "recipes" and where every other source ultimately points. Knob icons in the manual show approximate positions; ratios are quoted verbatim.

## The "safe space" starting point (Getting Started, pp. 8-9)
The manual's default reset point — "a good place to return to if you're feeling lost":
- DYNAMICS ~11 o'clock, SENSITIVITY ~11-12 (set by ear), WET ~1 (slight boost), ATTACK ~10-11, EQ noon (off), DRY off/low.
- Toggles: RELEASE middle (user, 650 ms) · MODE middle (Manual) · PHYSICS middle (stable). All dips OFF.
- Procedure (quoted): *"The most important step is to get your SENSITIVITY right… Keep your eye on the left LED and make some adjustments to the knob until you see it moving at a comfortable playing volume."* Then *"Turn up the DYNAMICS and mess with the PHYSICS to experience fluttering sag,"* *"Get the EQ moving to introduce some vibe,"* and *"hold down the AUX switch to turn it all into a swell."*

## Recipe 1 — TRANSPARENT ENHANCER (manual p. 22)
**~2:1, slow attack, slow release.** Verbatim: *"This setting will give you subtle compression (2:1) that thickens, focuses, and extends your sound. The slower ATTACK setting means your pick attack is uncompressed, preserving the energy of your instrument and preventing it from slipping into the background."*
- DYNAMICS: low/just into compression (~10-11, the 2:1 zone) · ATTACK: slow (toggle/icon shows slow) · RELEASE: RIGHT = Slow (1.5 s).
- **Suggested usage (quoted): "Lead lines or a versatile all-around starter."**

## Recipe 2 — TIGHT & LIVELY (manual p. 22)
**~4:1, fast attack, fast release.** Verbatim: *"Here we're applying a medium amount of compression (4:1), with a swift attack and release. The result is responsive and balanced smoothing. It absorbs everything except the first bit of your pick attack, but releases quickly to avoid an overly squished and static feeling."*
- DYNAMICS: ~noon-ish (the 4:1 zone — note p. 25 puts 4:1 just below noon) · ATTACK: fast (CCW) · RELEASE: LEFT = Fast (50 ms).
- **Suggested usage (quoted): "Chords or fast and dense playing (e.g. funk)."**

## Recipe 3 — PARALLEL POP (manual p. 23)
The parallel-compression / New-York recipe. Verbatim: *"Using the DRY knob is a good way to have it all. It lets you create extreme settings that bring out the details and heap on the sustain, and then blend the uncompressed sound back in to restore its character and dynamics. The result is a big, punchy sound that allows for plenty of experimentation."*
- DRY: UP (blended in) · WET: UP · SENSITIVITY: up · DYNAMICS: high/extreme · ATTACK: fast · RELEASE: middle/short.
- **Suggested usage (quoted): "Bass, drums, or thickening an instrument or mix."**

> CB caveat printed on the recipe page (p. 23): *"The ideal SENSITIVITY setting will be different for every instrument and set of hands. Keep an eye on the left LED as you explore these settings and adjust SENSITIVITY if you're seeing too much or too little action."* (Every recipe needs a per-instrument SENSITIVITY re-set against the left LED.)

## DUSTY recipe — official walkthrough (manual pp. 32-33)
Flip the **DUSTY** dip ON. CB: *"Clean's limiter typically hangs in the background, working as a final stage to smooth everything out, Dusty mode instead sets the limiter loose, turning it into a tactile overdrive with soft edges and a crumbly decay."* Signal flow: COMPRESSOR → EQ → MIXER → LIMITER (so EVERYTHING you change feeds the distortion).
- **The core recipe (quoted): "Crank DYNAMICS, boost WET to compensate, and then roll back SENSITIVITY. You will be greeted by blooming overdrive that sputters and breaks when you dig in."**
- SENSITIVITY = the Dusty "amount" control (sets the limiter/clip threshold).
- *"Your dry signal will be dusty as well; just turn up the DRY knob and the dust will begin to emerge."*
- Affects BOTH wet and dry signals.

## SWELL setups (manual pp. 30-31)
- **Dynamic Swell (default):** hold AUX footswitch (momentary). Signal swells in when playing passes the SENSITIVITY threshold, swells back out below it. Left LED green during swell.
- **Manual Swell:** turn on **SWELL AUX** dip → AUX triggers a single tempo-synced swell; hold AUX to mute, release to swell up; or tap for an instant swell.
- **Speed control:** in Hidden Options (hold both footswitches), **WET = SWELL IN time (100 ms–4 s), DRY = SWELL OUT time (100 ms–4 s).** Tinker with SENSITIVITY + speeds for "smooth and synthy textures."
- **BLIPS recipe (quoted):** *"Set both SWELL IN and SWELL OUT to their fastest speeds to turn your playing into short muted blips with a soft but percussive character."*

## STEREO MOVEMENT (SPREAD dip + EQ modes — pp. 29, 34)
Turn on **SPREAD** dip: EQ, compressor, and swells process L/R independently. Verbatim on EQ stereo behavior (p. 29): *"Manual mode creates bursts of flickering panning, Modulated mode auto-pans from side to side, and Shifty introduces smooth, dynamic panning."* (This is the synth-widener / mono-to-stereo move — pair with MISO dip to split a mono input to stereo first.) SPREAD ROUTING in Hidden Options can limit SPREAD to just EQ or just volume effects (PHYSICS toggle there: EQ / BOTH / VOLUME).

## MOTION (pseudo-tremolo, p. 35)
Turn on **MOTION** dip: modulates the amount of compression. **DYNAMICS = mod depth, ATTACK = mod rate.** Motion only occurs while playing and fades when you drop below the SENSITIVITY threshold.

## NOISE GATE (p. 35 + Hidden Options p. 17)
Turn on **NOISE GATE** dip. In Hidden Options: **SENSITIVITY = gate threshold, DYNAMICS = gate release time.** (Community use: single-coil hum/hiss mute — see Elektronauts/Gear Page captures.)

## Two-stage DYNAMICS sweep map (pp. 24-27) — for dialing the recipes by ear
One knob = two comps in series (Stage 1 shape-shifter → Stage 2 hard limiter). CCW→CW:
- **1:1 → 2:1 → 4:1 → 10:1 (compression, first half; subtle/transparent low, clamps harder toward noon).**
- **Noon = ∞:1 limiting**; SENSITIVITY now sets the absolute ceiling. Past noon it **blends feedback→feedforward** (*"Feedback – Natural, smooth, relaxed; Feedforward – Precise, snappy, aggressive"*).
- **Last quarter = SAG** (*"Your signal falls out, falters, and sputters as you play harder"*). Hold BYPASS footswitch = momentarily max the Sag.
- PHYSICS toggle (LEFT subtle wobble / MIDDLE stable / RIGHT twitchy) destabilizes the envelope for "organic wobbles and bursts of motion."
