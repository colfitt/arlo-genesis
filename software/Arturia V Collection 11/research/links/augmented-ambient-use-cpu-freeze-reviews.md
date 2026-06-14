(roundup — see inline URLs)
Engadget / KVR forum + reviews / Sweetwater / ADSR · "Augmented STRINGS/VOICES ambient & cinematic use, sound character, CPU" · 2022–2024 · triangulated

== Sound character / who it's for (honest) ==
- https://www.engadget.com/arturia-augmented-strings-synth-vst-150018015.html (review) — "leans towards the cinematic, with lush orchestral sounds often brushing up against **thick analog-sounding pads and subtly glitchy granular effects**." More *restrained* than Output Analog Strings (which gets "wild and chaotic") — stays tied to recognizable strings while adding synthetic texture. Big central Morph + 7 macros are intuitive but their exact functions are "somewhat mysterious" (macro-first, not deep-edit-first design).
- KVR reviews / forum (https://www.kvraudio.com/forum/viewtopic.php?t=588186, product reviews): mixed. Fans — "one of my faves to use for ambient music," "so many sounds and possibilities," lush evolving soundscapes. Skeptics — "nothing more than a bunch of presets and not that many," aimed at "newer producers/hobbyists," limited deep customization. STRINGS ensemble recorded ~20 hrs, 70+ articulations, Neumann/Schoeps/DPA/Millennia mics; ~500 presets.
- VOICES: "create percussive and sustained **textures**, not words" (per manual) → presets like "Crystal Figures" (additive + wavetable + sample, evolving ambient keys); dark immersive choral soundscapes. Preset names span realistic choir → "futuristic hybrid vocalizations."

== CPU / freeze (the documented gotcha — matches the project navigator) ==
- Engadget + KVR both flag it: **computationally demanding**; one case "brought a 2019 MacBook Pro to a crawl." This is the worst-offender pair in V Collection for CPU.
- **Mitigation for this rig:** these are sustained-wall / pad sources → **commit early**. Freeze the track (Logic: Freeze, or Bounce-in-Place) or print the wash to audio as soon as the part is set, then degrade the audio downstream. Lower the **Polyphony** setting (top-toolbar pop-up), raise buffer size for tracking, and don't stack multiple live instances — bounce the first before adding the next.

== Ambient/drone technique synthesis (from the above + manual) ==
- Pick a Layer-A sample engine = a sustained string ensemble (STRINGS) or sustained "Ah/Oo" choir / pitch-Drift voice (VOICES); Layer-B = a synth engine (granular for shimmer/glitch, wavetable for motion, harmonic/additive for glassy air).
- Set **Morph to Additive** so morphing *adds* the synth layer onto the strings/choir → swelling wall; or **Custom** with per-Part Min/Max curves so the acoustic recedes as the synth blooms.
- Route an **LFO + a Function (slow, unsynced)** to Morph and to a filter, and assign **Motion** macro to LFO/function *rates* → the wall never settles. (Same "unsynced modulators never line up" trick as the universal V-Collection technique in the navigator.)
- Hold a low cluster, long attack/release (Time macro), generous global reverb + delay, then bounce → run through Valhalla / EchoBoy / Decapitator / RC-20 / SketchCassette for the degraded "recorded-wrong" finish. Banjo/baritone plays the lead over the printed wall.
- ⚠️ Honesty: **no named shoegaze/doom/slowcore artist is documented using Augmented Strings/Voices specifically** — relevance is by technique (evolving hybrid texture source), consistent with the rest of the V Collection navigator's "no specific-artist credit" finding.
