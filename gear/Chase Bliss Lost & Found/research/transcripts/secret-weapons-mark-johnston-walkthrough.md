https://www.youtube.com/watch?v=7ebOPVUX8Ew
youtube · Mark Johnston (Secret Weapons) · 2025-08-01 · 1:09:39

# Lost + Found — Secret Weapons deep walkthrough (Mark Johnston)

Long-form (70 min) demo + tutorial by demoer Mark Johnston, recorded on a **pre-release unit running beta firmware** (he flags this repeatedly — some engines, especially the synth, were "the farthest thing from being locked in firmware-wise"). The single most useful community video for understanding routing logic and the practical control scheme. Distilled tips below; "[beta]" marks anything he warned may have changed.

## Control-scheme essentials (confirms + clarifies the manual)
- Layout is **the original Brothers' two-channel topology**: a Left channel and Right channel, shared MIX (top) and BLEND (below it), routing toggle at bottom-center.
- Per-channel toggle picks the **category 1–2–3 (left) / 4–5–6 (right)**; **MODIFY noon→CCW = the "A" effect, noon→CW = the "B" effect.** Six categories × A/B = **12 unique engines**.
- **MODIFY at exact noon = effect bypassed** (pedal still on / signal passes). This is deliberate so you can run the GLUE compressor alone. Easy to mistake for a dead channel.
- **ALT and EQ are accessed the same way:** hold BOTH footswitches, then turn the ALT knob (mode-specific param) or the MODIFY knob for that channel (which becomes a per-channel EQ in hidden mode).
- **Tap tempo:** double-tap BOTH footswitches together to enter tap mode; while in it, hold one side and turn its TIME to set that engine's **subdivision independently**; tap right footswitch to exit; the side LEDs keep flashing to show you're still following tempo; moving any TIME knob exits.

## Routing logic — the headline feature (quoted/paraphrased precisely)
- **Parallel (center toggle):** MIX = overall wet/dry; BLEND = balance between the two engines inside the wet mix. Dry hits both engines.
- **Series (L→R or R→L):** MIX becomes "blend of dry + engine 1," that sum feeds engine 2; **BLEND = mix of engine-2 into the chain. Your dry signal does NOT reach engine 2** by default.
- **SPILL** (hidden, hold both + raise the spill control): routes dry past engine 1 directly into engine 2 as well — so in series you get *three* independent send amounts: dry→eng1, eng1→eng2, and dry→eng2. Johnston: "more connection points than anything else doing this kind of thing I've ever used."
- The L SWAP / R SWAP dips copy one side's entire category bank to the other side, so **you can run any two engines together — including two of the exact same engine** (e.g. dual tape delay, dual reverb, synth+GenLite).

## Concrete recipes he built (worth trying on the rig)
- **"Build-your-own shimmer reverb":** swap right channel to **2B Pitch Repeater** (octave-up, long/skittery), feed it into **1A Slow-verb** in bank 2 → a denser, better-than-stock shoegaze shimmer.
- **Dual tape delay:** swap left to tape too, double-tap into tap mode, give each side a different subdivision, then feed one delay into the other and add dry via SPILL — "basically a build-your-own reverb."
- **Synth + GenLite:** **5A Impulse Synth** swapped onto both sides so you can stack **6B Gen Lite** after it; the GenLite grit/inconsistency "softens up" the synth and removes its clinical edge.
- **Cinematic pad:** Impulse Synth + **1B Useful Ambience** set large, raise BLEND toward the reverb. "Very classic cinematic sound."
- **70s clean-guitar tone:** **6A Ensemble** chorus + **3A Pinging Phaser** (double modulation) — "but something's always missing: compression," then engage **GLUE** to glue it together.
- **Stereo pinging phaser via ramp:** 3A, SPREAD on, arm **BOUNCE** on the left MODIFY so the pole count sweeps min↔max; slow ramp = "intermittent stereo pinging," fast = aggressive. (His first time using ramping in a demo — a nudge that the internal-mod feature is underused.)

## Per-engine notes that matter for textures
- **1A Slow-verb:** ALT = diffusion; min diffusion gives springy/fast multitap delays, max = smeared reverb. Freeze (hold) holds it as a pad. EQ ducks it out of the way.
- **3A Pinging Phaser:** **adjusting the number of poles while playing throws off "weird, not-intentional but very cool" artifacts** — a happy-accident generator.
- **3B Spectral Modulator:** "bizarre synthy resonant filter" — from lo-fi low-pass to "laser-gun tremolo" fast, or giant glacial filter sweeps slow.
- **4A Tape echo:** has TIME, feedback (MODIFY), modulation, EQ (ALT clockwise carves lows), tap, and hold=freeze.
- **4B Grain Tumbler:** slow TIME = bigger grains; ALT = grain shape (square/choppy → soft/reverb-like).
- **5A Impulse Synth [beta]:** explicitly NOT for fast lead playing — "it will not keep up with you." Built for **slow pads, chord changes, sustained textures**; tracks non-power-chord chords surprisingly well. He expects the shipping firmware to track better than his beta.
- **5B Sympathetic Resonator:** "chromatically tuned tubes that rattle"; ALT = octave ±1; lower octave + reduced feedback = "menacing octave-down that shakes around your core sound."
- **6A Ensemble:** **hold (set LATCH on) switches the chorus LFO from a clean sine to a smooth random waveform** — inconsistent, non-cyclical movement instead of seasick wobble.
- **6B Gen Lite:** general lo-fi sheen; ALT raises pops/clicks/failures; **hold = tape-stop record-slowdown, and the slowdown speed is tied to the effect's modulation speed.**

## Gotchas he surfaced
- MODIFY-at-noon = no effect (see above) is the #1 "is it broken?" trap.
- Beta-firmware caveat on the **synth tracking** — treat any pre-release synth demo with skepticism vs. a shipping unit.
- This is a pre-order/small-batch model: a fixed buy window, not "sells out," but goes to the "Disney vault" when the window closes.
