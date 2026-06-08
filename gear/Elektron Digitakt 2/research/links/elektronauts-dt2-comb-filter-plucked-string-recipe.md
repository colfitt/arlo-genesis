https://www.elektronauts.com/t/making-pianos-harps-and-strings-with-comb-filter/222328
elektronauts.com · community thread (refs Loopop demo) · 2024-10

# DT2 Comb filter → plucked-string / harp / piano tones (banjo-relevant)

Directly relevant to the rig's banjo material: the DT2's Comb filter can synthesize Karplus-Strong-style plucked-string tones from a short noise/click excitation, OR turn a real banjo pluck into a tuned metallic resonator.

## The one verified fact from this thread
- **Comb+ is the filter that makes the plucked-string sound.** (Quote, user "garf": "DT2 has Comb, which is actually Comb− on DN2. Comb+ is the filter that makes the string sound.") Comb+ uses **positive feedback → metallic, pitch-tuned overtones**; at lower feedback it's a slap-back/reflection.
- **Key tracking lives on filter page 2** (dedicated param) — turn it on so the comb's tuned resonance **tracks the keyboard**, i.e. the "string" plays in pitch across the trig keys.

## Honest status
- This thread is EXPLORATORY — people wanted the recipe but **no one posted a finished preset or exact ADSR/frequency/feedback numbers**. The working demo everyone points to is **Loopop's DT2 video** (search "Loopop Digitakt II" — he demonstrates comb-filter strings). So the *technique is confirmed*, the *exact numbers are not* in this thread.

## Practical starting recipe (synthesized, NEEDS DIALING BY EAR — not quoted values)
1. Source = a very short **noise burst** or **click** one-shot (or a real banjo pluck for hybrid tone).
2. FLTR machine = **Comb+**; turn **resonance/feedback up** for a ringing tuned tone (the more feedback, the more sustained the "string").
3. **Key tracking ON** (filter page 2) so the comb frequency follows note pitch.
4. Short **AMP attack**, medium **decay** for a pluck; longer decay/INF for a sustained bowed-string drone.
5. For banjo specifically: feed the actual banjo pluck through Comb+ to get a detuned metallic resonator (dossier §6) rather than synthesizing from noise.

NOTE: Only the Comb+ = string fact and key-tracking-on-page-2 are VERIFIED here. Steps 1–5 are a reasoned starting point, not forum-quoted values. The Comb filter is DT2-only (the OG Digitakt has no comb filter).
