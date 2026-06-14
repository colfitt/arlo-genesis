https://www.youtube.com/watch?v=mmn6iSBKdp8
You Suck at Producing (or similar pad-focused channel) · How to Make HUGE Evolving Pads with Ableton Drift · 2024

> **LITE NOTE (orchestrator-added):** This is the single most Lite-friendly drone/pad
> tutorial captured. Devices used and their Lite status — **Drift ✓ (in Lite)**,
> **Phaser-Flanger/"Doubler" ✓**, **Reverb ✓**, **Utility ✓**, **Simpler ✓**,
> **Redux ✓**, **Auto Filter ✓**. The ONE exception: **Grain Delay ✗ — NOT in Live 12
> Lite** (it is in Intro/Standard/Suite but the Lite features page omits it). Lite
> substitute for the grain-delay step: use **Delay** with short time + high feedback +
> the band-pass narrowed, or **Beat Repeat** with a small grid + pitch decay, or just
> resample the pad and warp it in **Texture** mode (see the "turn any sound into a drone"
> transcript). Everything else in this video works verbatim in Lite.

## Cleaned transcript

Making a synth pad from scratch is actually super easy, and you can make it super ambient, have lots of texture and depth and emotion with some really simple techniques. This video, we're going to be working with Ableton Live Drift, which most people have access to, even if you're on Ableton Intro. [LITE: Drift is also in Lite.] By the end of this video, you're going to have a world of possibilities you can take with you in these techniques.

**Setup / Drift basics.** Go to Instruments → Drift. Drift came out around Ableton 11.3, so on 11 or 12 you probably have it — it's in Intro/Standard/Suite [and Lite]. It's analog-inspired subtractive synthesis, a traditional more basic form. It's a great synth — limited, but that's its advantage because you can experiment without getting overwhelmed. Right off the bat in the default screen you might notice some things are turned up — they don't look like zeros. If you double-click on them they'll become zeros, and you probably want that, because (for example) with one setting up, even when you pull the filter all the way down you'll still have a pointy sound, which confuses people. By default these things are on. Double-click to turn off, then hit the three dots → Save as Default Preset.

**Oscillators.** Drift gives you a bunch of oscillator shapes, including a Moog-inspired Shark Tooth (saturated, great for bass). For an ambient evolving pad I like **triangle** — it has a really warm sound. Turn it down so both oscillators match the same octave; both oscillators are on. Don't get overwhelmed by shapes — they change the tone and you can change them later.

**Shape modulation via LFO (the key to evolving sound).** Next to Shape you'll see Slide and LFO — go for **LFO**. Click it, go to the LFO on the far right. Turn the amount to **100** so you can really hear it. As you hold a key, the movement is the LFO. Turn up its rate and it happens fast — that's how you know what an LFO is doing. For slow/evolving I set **rate ≈ 0.2 Hz** (slow). Change the LFO **shape to Wander** — smooth like a sine but with randomness, so it's not erratic the way Sample & Hold would be. So it's moving, but not dramatically.

**Mixer / oscillator balance.** The little area over here is a mini-mixer for the two oscillator levels — set the balance to taste.

**Filter.** Click the gray panes to switch the screen. Click Frequency. Go for a lower-mid sound: **high cut ≈ 430 Hz**, **high-pass ≈ 40 Hz** (clean up the lows), **resonance ≈ 0.5**.

**The Mod matrix (Drift's secret).** Hit the little "mod" square — it reveals drop-down routing. Route **LFO → lowpass frequency** by a percentage; route **LFO → lowpass resonance** at ~30% (creates a little spike); and the third slot — route **Velocity → LFO rate**, turned all the way up. So how hard you hit the keys changes the LFO rate, meaning the pad responds to your playing. "A lot of people don't get this far because they never learn what an LFO is."

**Amp envelope (DNA of the sound).** Click the envelope pane. A slower attack is the big part of a pad. Type in **Attack 3 s** (30,000 ms). My muscle-memory setting is **"3-6-5-9": Attack 3 s, Decay 6 s, Sustain 50%, Release very slow** — so the sound drifts in, and when you release, it really drifts away. Hit a chord and it slowly drifts in with movement; hit harder and it moves more (velocity → LFO rate).

**Effects — Phaser-Flanger as a "Doubler" [LITE ✓].** Type "phaser/flanger" and drag in — note it says **Doubler** mode. Turn it on, **warmth all the way up**, **time down to 40 ms** (halve it). Play a chord — the sound becomes heavily stereo-ised (most obvious on headphones). Stereoising a sound is a really useful way to make it instantly more exciting, but you don't have to lose the center: use the dry/wet, or go **parallel**. Highlight the device and hit **Ctrl/Cmd-G** to group it; click the chain button → right-click → Create Chain to get your dry center channel back alongside the doubled signal. Thicker sound.

**Grain Delay [LITE ✗ — see Lite note above].** Drag Grain Delay into its own parallel lane. Unlike a clean echo, it breaks the sound into ~1–50 ms grains — perfect for dense evolving textures because it randomises the delayed signal. Settings shown: **Spray 260**, **Feedback 30**. You hear granular "dirt"/break-up. *(In Lite, substitute Delay with feedback + narrow band-pass, or Beat Repeat, or resample-and-Texture-warp.)*

**Reverb [LITE ✓].** Use the stock Reverb. The "Large Space Chorus" preset is great for big ambient sounds; the presenter's own variant "Steady Space" removes some modulation to keep it steadier — added in parallel, 100% wet, balanced with the small blue volume faders on each chain.

**Gain staging — Utility [LITE ✓].** Stacking many parallel signals can overwhelm gain staging and clip. Drop **Utility** and pull gain back ~**−10 dB**.

**Glue everything with a Reverb in front.** To push the pad further back, duplicate the "Steady Space" reverb (Ctrl-click-drag) and place it in front of all the parallel chains — gluing them and giving the whole thing dimension.

**Add an organic texture layer [LITE ✓ via Simpler].** Group Drift + all effects (shift-click Drift, Ctrl-G) → now you have an instrument chain you can add to. Add a texture/foley layer — wind, rain, waves, even "bacon grease" cooking sounds. Drag the sample into the chain — Ableton makes a **Simpler**. Click **Loop** so it plays indefinitely like the pad; **turn up Fade, turn down Loop** to make the triangle loop shape. Add **Redux [LITE ✓]** right next to the texture for a lo-fi/darker version (turns "bacon grease" into something like space interference). Layer the two.

**Final glue — Auto Filter [LITE ✓].** Add Auto Filter *after* the big grouping (outside all the panes) so it affects both chains. Pull the frequency down. Now you have a beautiful ambient pad with lots of texture, sound and low end.
