https://valhalladsp.com/shop/reverb/valhalla-room/ + https://valhalladsp.com/2011/05/03/valhallaroom-the-reverb-modes/ + https://valhalladsp.wordpress.com/tag/sulaco/ + https://valhalladsp.wordpress.com/tag/lv-426/ + https://valhalladsp.com/2011/06/21/valhallaroom-v1-0-6-introducing-dark-room/
Valhalla DSP (Sean Costello) · official product page + "The Reverb Modes" blog + mode-tag pages · 2011-2023

# ValhallaRoom — the 12 reverb modes (authoritative taxonomy)

**IMPORTANT CORRECTION for the rig brief:** ValhallaRoom does **NOT** have a "Bloom" mode family (BloomRevDark/Bright etc.). "Bloom" is a **ValhallaShimmer** concept (and the original Alesis Midiverb II preset Shimmer emulates) — it is not in Room. Room's ambient/drone family is the **Dark** group + the **Alien-named** modes (Nostromo / Narcissus / Sulaco / LV-426). The "lush evolving pad" job in Room is done by **Bright Room** (long decay turns static input into pads) and the dark space modes — see below. The brief also lists "RandomSpace" and "Medium/Large Hall" — those are not literal ValhallaRoom mode names either (halls are a VintageVerb thing; Room uses Room/Chamber/Space/Dark/Alien naming). The dual-engine "depth" knob IS real — see room-controls-deep-dive.

## Full current mode list (v2.0.0, 12 algorithms)
Large Room · Medium Room · Bright Room · Large Chamber · Dark Room · Dark Chamber · Dark Space · Nostromo · Narcissus · Sulaco · LV-426 · Dense Room.

The product page frames the whole plugin as "an algorithmic vision of perfection and precision... a wide range of **natural** reverberation sounds — from tight ambiences and rooms, through traditional hall and plate sounds, all the way up to **vast modulated spaces**." Late section decays from **0.1 s to 100 s**; Early section does "subtle short bursts of early reverberation energy, as well as gated reverbs up to one second."

---

## The "natural / realistic depth" modes
- **Large Room** — the most "natural" algorithm. Sparse initial decay that quickly builds high reflection density; exponential decay with slight HF absorption ("air"). Modulation is designed for a wide stereo image **without random pitch shifts in the decay** → deeper at higher mod depth while keeping pitch stable. *The honest, believable space — the default depth bed.*
- **Medium Room** — wider, more "square" geometry; sparsest initial echo density (audible discrete echoes at large Late Size). Modulation more random than Large Room and *can* cause random pitch shifts on long decays. Classic-Lexicon flavor.
- **Large Chamber** — very high initial echo density from the start (echo-chamber, not room). Aim was "larger than life": echo density of a small space but the modal density of a large hall → "fairly colorless" reverb that suits any source. *The clean, big, neutral space.*
- **Dense Room** — (newer) high-density realistic room.

## The "ambient pad / evolving" modes
- **Bright Room** — slower attack, more "digital" character, extra HF "air" and "sheen." Modulation is "random, complex, and deep, with the goal to provide lush chorusing." **"For long decays, it turns static input sounds into evolving pads"** and "at some settings can sound close to string ensembles." Costello's reference: **"Vangelis 'Blade Runner' reverbs."** *★ the in-Room shimmer-adjacent / drone-pad mode.*

## The "dark / lo-fi / deep-space" modes (the drone/doom family)
- **Dark Room** — deliberately **lo-fi**: noisy interpolation, **no highs above ~11 kHz**, low initial echo density, wide stereo image, clear decay with **lush randomized chorusing**. Inspired by the noisy interpolation + sparse density of vintage digital (Lexicon 224, EMT 250). **"Turn up the Early and Late Mod Depth when using Dark Room"** for the big lush spacey decay (the random pitch mod kills metallic artifacts). Audible "flutter/grain" in the tail. Lowest CPU. *★ the degraded/tape-aesthetic ambient mode — closest in spirit to VintageVerb's 1970s color.*
- **Dark Chamber** — dark Large-Chamber relative; more automatic chorusing → more "wishy-washy"/washy.
- **Dark Space** — "a HUGE dark space, with a somewhat sparser early echo density and **deep detuning modulation**." *The biggest dark wall.*

## The Alien-named modes (dark, slow-attack, lush — drone heaven)
Named after Alien-franchise ships/places (Nostromo, Narcissus, Sulaco, LV-426); "lusher modulation and a much slower attack" than the room/chamber families.
- **Nostromo** — "Deep, dark, echoing reverb" with slow density buildup and wide spatial image; the parent of Narcissus/LV-426.
- **Narcissus** — "Dark, lush, wide, with random modulation that quickly builds into rich chorusing." The little sibling of Nostromo; most CPU-efficient. (Workhorse-presenter: "great on pianos.")
- **Sulaco** — **Dark** (top octave gone, nothing above ¼ sample rate), with a LOT of detuning modulation and a well-centered stereo image. Discrete early reflections appear as Late Size rises (smooth them with Early Send). **Late Cross** affects its stereo image rather than the decay → "solid" imaging. Late Size sweeps it from tight rooms to vast echoing spaces. Good on drums/percussion too. 2nd-lowest CPU. Added v1.0.9.
- **LV-426** — "a deep dark space verb... a cross between Nostromo and Narcissus," but with **far higher early echo density** than either, a **slower attack** than the other modes, and "lush, diffuse random modulation that produces beautiful long decays." Has the full LATE LowMult/Xover + HighMult/Xover tone controls. Community: try it for **lo-fi / very retro / old-school** vibes. *★ the lush slow-bloom deep-space drone mode.*

## Pick-by-job summary (for this rig)
- **Natural depth bed:** Large Room (stable pitch) · Large Chamber / Dense Room (clean & big).
- **Evolving pad / shimmer-adjacent:** Bright Room (long decay → pad; string-ensemble at some settings).
- **Degraded / lo-fi drone wall:** Dark Room (11 kHz ceiling, grainy) · Dark Space (huge, detuned).
- **Lush slow-bloom ambient drone:** LV-426 (slow attack, dense, deep) · Narcissus / Nostromo / Sulaco.
