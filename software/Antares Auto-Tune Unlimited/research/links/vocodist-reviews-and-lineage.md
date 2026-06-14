https://www.mixonline.com/technology/antares-auto-tune-vocodist-a-real-world-review
Mix (Mixonline) "Antares Auto-Tune Vocodist – A Real-World Review" + Synth&Software (2021-09) + Sound On Sound review · vocoder lineage + notable users
[SOS review 403'd to the fetcher; SOS specifics taken from the pre-existing antares-vocodist-review.md capture — LABELED]

# Vocodist — reviews, vocoder lineage, and notable users

## Real-world review takeaways (Mixonline)
- **Default carrier = the internal dual 8-voice oscillator**, voices independently transposable;
  alternatively route a **side-chain signal from another track** as the carrier.
- The vocal is the **modulator**; three pitch-control methods: **Voice** (source-track pitch, default),
  **MIDI** (controller or MIDI track), and **Key** — *"a one-octave keyboard… click a key and it
  transposes the output to **drone** at that pitch."* (← the rig's drone mode, confirmed.)
- **20 vocoder choices**, most digital models of classic hardware; audition by switching live;
  band count is editable per model.
- **Output+FX**: a tube-distortion **Warmth**, a "rich-sounding **Chorus**."
- Verdict: interface is **"easier to adjust than other vocoding plug-ins"** despite many params;
  "an exceptionally powerful plug-in." Subscription-only is the one knock.

## Vocoder lineage (cite as technique, not as Vocodist artist credits)
- Manual + reviews trace the modeled units to **Homer Dudley's 1937/1939 Voder/Vocoder** →
  hardware used by **Wendy Carlos, Stevie Wonder, Herbie Hancock, Kraftwerk, Daft Punk, ELO**.
- This is the **"Kraftwerk → Burial" vocal-texture lineage** the rig brief invokes: robotic,
  formant-shaped synthetic vocal walls. These are *genre lineage / technique*, not documented uses
  of **Vocodist specifically**.

## Notable users / preset designers (the genre-adjacent thread)
- Bundled **artist presets** by **Chromeo / P-Thugg, Buddy Ross, Damien Lewis, J. Chris Griffin,
  Rachel K Collier.**
- **Buddy Ross** = a **Frank Ocean** collaborator (Synth&Software). This is the same experimental-
  pop / smeared-vocal-texture orbit as the Harmony-Engine **Prismizer** (Bon Iver / Frank Ocean /
  Francis & the Lights) — the rig's one real genre-adjacent artist anchor. **No documented
  drone/doom/shoegaze/post-rock credit for Vocodist exists** — recipes are by capability + technique.

## Logic-specific note (Sound On Sound, via prior capture)
SOS: *"Logic users will have to play the now-familiar MIDI Controlled Effect game via an Instrument
track and side-chain input if using the MIDI input facility, but otherwise Vocodist can be
instantiated on an audio track."* → confirms: **audio-track insert is fine** for the default
voice-tracked internal carrier; the **AU-MIDI-effect + side-chain** dance is only needed when you
want MIDI to play the carrier (or an external side-chain carrier). See
`vocodist-logic-carrier-routing.md` for the step-by-step.

## QC
Mixonline + Synth&Software fetched directly. SOS review 403'd this pass; its specifics reuse the
already-captured `antares-vocodist-review.md` (which cited SOS/Mixonline/Synth&Software). Lineage
artists = the modeled *hardware* vocoders' users, not Vocodist credits — flagged as technique.
