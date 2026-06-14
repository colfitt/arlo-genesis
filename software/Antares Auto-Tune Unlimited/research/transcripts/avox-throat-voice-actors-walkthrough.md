https://www.youtube.com/watch?v=UcpBJxr1ZV4
YouTube · "How To Use Antares Avox Throat (Great for Voice Actors)" · control-by-control THROAT Evo walkthrough (auto-captions, paraphrased)

# THROAT Evo — control-by-control walkthrough (NEW capture)

A spoken control tour of the **current THROAT Evo** UI on a male (self-described baritone)
voice. Confirms the modern control layout (the older AVOX 2 Throat lacked some of this —
notably the built-in Pitch control). Captions auto-generated; distilled to prose below.

## What it does (presenter's framing)
"Helps sculpt the throat to make it sound different to your liking" — sound like a giant,
or sound tiny ("a midget"). It reshapes the *virtual* vocal tract, not the pitch melody.

## Top-row global controls (left→right)
- **Vocal Range** — like every Auto-Tune plugin: set it to match the incoming source range
  (Soprano…Baritone, etc.). Presenter is a baritone so selects the baritone option. (This is
  the source-tracking range, NOT the output character.)
- **Glottal Voice Type / performance style** — "depends on your performance": pick based on
  whether the part is **screaming / whispering / regular pop singing**. For a normal speaking/
  singing take → **Medium**; for loud/intense delivery → the **louder/intense** option. "See
  what feels right."
- **Throat Precision** (the source/depth control) — *"like Retune Speed for Auto-Tune"* but for
  the throat: tells the model **how much change** to apply. **Subtle** (barely there) →
  **Medium** (audible change) → **Extreme** (definitely audible). KEY control for how hard the
  re-voicing hits.
- **Pitch** — straightforward: up = higher pitch, down = lower pitch. (Modern Evo addition.)

## Breathiness section
- **Breathiness amount** — adds air (high-frequency-ish noise). Raise it → "more crisp"; the air
  rides on top.
- **High-pass frequency** (under breathiness) — the higher you push it, **the less of your
  original track you keep** — i.e. the modelled throat takes over more of the sound. (So this
  doubles as a wet-balance/character control: high HPF = more synthetic/modelled, less natural.)

## Modeled-throat controls (the heart)
- **Length** — taller person = lengthened tract = lower/longer voice; short = "lil midget"
  (small, raised). Lengthen → formants down; shorten → formants up.
- **Width** — "the whiteness/airy-ness": **wide → more airy**; **narrow → more nasal**. Narrowing
  closes the tract toward nasal honk.
- **Glottal Model** (pulse display) — the vibration source in the voice; an animated pulse
  waveform adjusts to your delivery. Even on a high-pitched note you can hear "a lot of bass"
  through it — it sets how thick/buzzy the excitation is.

## Output section
- **Output / Bypass** — output gain + a bypass that removes all processing.
- **Level Matching** — auto-compensates: if your re-voicing gets loud/intense during sculpting,
  it tries to match output volume to the original. With it OFF the processed voice can drop "way
  low in comparison" — turn it on (or trim Output) to keep gain sane while sculpting.

## The 5-point graphical Throat-Shaping display
A node graph you drag to reshape the tract by hand:
- **Point 1** = the **vocal cords** (the source end).
- **Points 2, 3, 4** = the **throat passageway**.
- **Point 5** = the **mouth / lips** (the diagram shows it as the mouth opening).
You drag node positions/widths to "close it in" or open it out → re-voices the source without
touching the top knobs. IMPORTANT linkage: the graph and the Length/Width knobs are the SAME
model — moving Length/Width re-scales the graph nodes and vice-versa ("it's basically scaling").
A **Reset** button returns the graph to default.

## Takeaways for sound design
- Throat Precision (Subtle→Extreme) is the master "how-wrong" dial — treat it like a wet amount.
- The HPF-under-breathiness is a sneaky way to dial *out* the natural source and let the modelled
  (synthetic) tract dominate → more alien.
- The graphical display is where the "physically impossible" re-voicing lives: drag nodes past
  natural shapes for vowel-locked / hollow / honking timbres.
