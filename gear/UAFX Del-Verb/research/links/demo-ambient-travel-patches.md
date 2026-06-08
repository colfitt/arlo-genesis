# UAFX Del-Verb — Ambient / Travel Patch Sheet (for THIS rig)

Clock-face positions looking down at the pedal. Knob row = Delay **Time · Feedback · Mix · Color · Mod**, plus **Reverb** level + 3-way toggle. These extend the dossier's §13 starting points with the actual voicing names from `voicing-list-official.md` and the source-specific notes for banjo / baritone Jazzmaster / VG-800 pad. Honest framing: this is the **travel/fly board** role — Hall 224 + a controlled delay is the closest this box gets to the home rig's wall-of-sound aesthetic without an H90.

---

## 1. "Carry-on shimmer wash" — the signature travel patch
The reason to keep it. Big Hall, controlled pitched delay = instant ambient wall in one box.
- **Reverb:** Hall 224, level **1–2 o'clock**. Voicing: **Dark N Dusty Trail** (dark, distant, lots of pre-delay) for doom; or **Cascade 224** (bright, huge) for shoegaze sparkle.
- **Delay:** **Precision**, voicing **Stereo Ping Pong Hi-Cut** (the 3.5 kHz LPF/130 Hz HPF in the feedback loop keeps the wash from turning to mud).
- **Time:** dotted-eighth (tap/clock to song) · **Feedback ~1–2 o'clock** · **Mix noon** · **Color slightly left** (roll off treble) · **Mod off (noon)**.
- **Trails:** On. **FS mode:** Delay | Tap (reverb always on, left foot drops delay, right foot taps).
- *Baritone Jazzmaster neck pickup → let chords bloom. Watch feedback; on a baritone runaway goes subsonic fast — ride it down to kill.*

## 2. "Octave-shimmer drone" — closest to the home aesthetic
Uses a pitched-delay voicing for free shimmer without a dedicated shimmer pedal.
- **Reverb:** Hall 224, level **noon–1 o'clock**. Voicing: **Shimmeron** (224 Chamber, max mid decay) or **Fractal Forest** (Small Hall A, max mid decay, 150 ms pre-delay).
- **Delay:** **Tape EP-III**, voicing **EP with octave pitched buckets** (or **EP with 5th Pitched Buckets** for a fifth instead of an octave).
- **Time:** long, to taste · **Feedback ~12–1 o'clock** · **Mix ~11** · **Color past noon** (drive on the repeats for grit) · **Mod toward Worn tape (right)**.
- **Trails:** On. Long sustained source (baritone, or VG-800 pad model) → swells into a harmonized wall.

## 3. "VG-800 pad / synth ambience" — the source-agnostic line-level patch
Del-Verb is post-cab, end-of-chain, so it treats the VG-800's modeled amp/synth output like any line source (corroborated by the OB-6 no-talking demo, `transcripts/bonedo-synth-notalking-ob6.md`).
- **Reverb:** Hall 224, level **1 o'clock**. Voicing: **Default 224 Hall** (Room A, long ambient tails) or **Swimmy and Shakey** (modulated).
- **Delay:** **Precision**, voicing **Stereo Ping Pong Vibrato** (LFO vibrato on the repeats = movement on a static pad).
- **Time:** dotted-eighth · **Feedback noon** · **Mix ~10–11** (delay sits under the pad, not on top) · **Color noon (flat)** · **Mod off**.
- Analog dry-through preserves the synth's low end. Great for sustained VG-800 patches.

## 4. "Banjo-as-lead clean" — articulate, not smeared
Banjo (Gold Tone EBM-5 via GK-5 → VG-800) is bright + transient-dense; Plate flatters it, Precision keeps rolls articulate.
- **Reverb:** Plate 140, level **10–11 o'clock**. Voicing: **Studio standard Plate A** (warm, ~3 ms, rounds the attack without the spring ice-pick).
- **Delay:** **Precision**, voicing **Default Precision** (clean, pitch-stable).
- **Time:** ~120–180 ms (slap) · **Feedback minimum** · **Mix ~9** · **Color slight right** (a touch of treble for clarity) · **Mod off**.
- *Spring '65 can add 2–4 kHz splash/ice-pick to banjo — prefer Plate here. For a surfy lead, Spring **Symphonic Reverb** voicing (pitch-modulated) is the fun option.*

## 5. "Dub / tape feedback play" — performance patch
- **Reverb:** Spring '65, level **9 o'clock** (drip behind the repeats). Voicing: **Spring Tube Drive A** for extra sizzle.
- **Delay:** **Tape EP-III**, voicing **Default Tape EP-III** (or **Dark Tape n Preamp** for a murkier dub).
- **Time:** to taste · **Feedback 2–3 o'clock** (edge of self-oscillation) · **Mix ~11** · **Color noon** · **Mod toward Worn tape**.
- Ride feedback by hand; drop to minimum to stop runaway. **FS mode:** Effects | Tap so the right foot can re-tap on the fly.

---

### Quick-recall note (if a MIDI controller is on the travel board)
Pre-assign the 6 voicings above to the toggle positions in-app (they're **stored in the pedal**, so they persist phone-free). Then an MC-Pro-class controller can fire a CC "snapshot" — `[bypass] → CC14 delay-select → CC15 reverb-select → CC25 division / CC24 feedback / CC22 mix / CC27 mod / CC28 reverb`, ~50 ms apart — to jump between these patches with your feet. See `settings-midi-and-controls.md` for the full CC map and send-order caveat.
