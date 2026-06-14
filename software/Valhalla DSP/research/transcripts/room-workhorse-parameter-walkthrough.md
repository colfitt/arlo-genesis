https://www.youtube.com/watch?v=UvlSyfwCKp8
YouTube · "Valhalla Room Tutorial | In Depth How to Use Valhalla Reverb Guide" · 2017

(Auto-caption transcript, cleaned to prose. Presenter calls ValhallaRoom his "workhorse... the best reverb I own" — an enthusiastic, parameter-by-parameter walkthrough on a synth + kick. The strongest source on how the Depth / Early-size / Late-size triad actually interacts.)

## The "I only look at 3-4 knobs" philosophy

"When I open it my eyes focus on three or four parameters at most, and it's usually just the **Mix** (if it's on a separate track), the **Decay**, the **High Cut**, and then **Early Size** and **Late Size**. Everything else happens after — I just tweak the other stuff after the fact." He states the three most important parameters in *any* reverb are **Mix, Decay, and High Cut**.

## Mix
Balance between dry (no reverb) and wet. At 100% all you hear is the reverb itself, nothing else. (On a send/aux track he runs it at 100% wet.)

## Predelay
The time between hearing the original sound and the reverb coming in. Test it on something with a sharp transient. At 200 ms it "basically sounds like a delay or an echo." At 0 ms the reverb lines up perfectly with the source and you get more phasing/comb-filtering. Conceptually it's the distance from the source to the back walls of the room (longer predelay = source further from the wall). **Practical rule: if you don't know what to do with predelay, keep it between 0 and 20 ms — safest is 0-10 ms.** For bass he likes **10-20 ms** ("a nice room feel"). Past ~50 ms you get a slapback-delay character. Long predelay on fast/chugging material fights the timing.

## Decay
How long the reverb takes to fade out. **Longer decay = bigger perceived room; shorter decay = smaller room.** On sustaining/evolving sounds you can push it long, but eventually it becomes an unusable "wish-wash." On bass he keeps decay short and instead adds size — or sends bass lightly to a separate long-tail reverb rather than lengthening its own.

## High Cut
A lowpass on the reverb. Also affects how "far back" a sound is perceived: pulling High Cut down doesn't literally place the source further back, it makes it *tighter* by removing highs the source doesn't need. He found ~5k sounded good on bass.

## Depth (the key/esoteric control)
**Depth determines whether ValhallaRoom relies on the EARLY-reflections engine or the LATE-reflections engine to build the space.** Depth all the way **up = the Late page is the main sound**; all the way **down = the Early page is the main sound**. At 0% the late section does nothing — you hear only the early reflections, and the reverb sounds much closer.

## The Early page
- **Early Size** — "one of the most interesting parameters." It does the job of two parameters most reverbs have (attack + decay), but only for the early reflections. It's how long it takes the early energy to build up so you can hear it. Turn it up to ~800 ms and "it takes forever to build up"; turn it down and it's super tight. It's "a mix of pre-delay, decay, and something else, but for just the early reflections." **He always dials Early Size FIRST** — it's the largest determinant of perceived room size — then does finishing touches with Late Size.
- **Diffusion** — at low settings you hear the individual early reflections (delay-like, distinct); turning it up smears them into a wash. "It makes it more diffuse."
- **Early Cross** — his honest take: "it does barely anything that I can detect... it's the control I generally skip over." His guess: stereo spread of the early reflections. Subtle.
- **Mod Rate / Mod Depth (Early)** — the pitch modulation of the early reflections. Rate = how fast, Depth = how much the pitch swings. Crank Mod Depth to max then sweep Rate and "it wreaks havoc on the pitch of those early reflections."
- **Early Send** — counterintuitive: as you turn Depth up toward 100, Early Send tells ValhallaRoom how much of that early reverb gets fed into the second/late stage. Balancing Early Send against Late Size lets you build "a very epic delay." A common setting he uses is 100 Depth with Early Send dialed to taste.

## The Late page
- "The late section doesn't do anything if Depth is at zero."
- **Late Size** — the other main control. Bigger Late Size = bigger room, and you hear more of the delay/echo character inside the room. **If you don't know what you're doing, keep Late Size at ~15 (the default) and configure your Early Size into it.**
- **Late Mod Rate / Depth** — controls how "wishy-washy" the tail sounds. With full Mod Depth it "causes the hell out of that reverb"; turn Mod Depth down for a less washy tail. (Hard to hear if Decay or Late Size is very short — "everything's related in this thing.")

## The EQ section (Bass/High multipliers)
The final stage is "basically an EQ — the balance you want the reverb to have." Think of it as: how long do I want the lows in my reverb vs the highs. On bass he wants the reverb tight — sets the bass crossover ~800 Hz-1 kHz and subtracts a little so it doesn't muddy the bass. The high multiplier is "like a shelving filter"; set the high crossover ~5k and pull the mult down to go darker.

## Modes he reaches for
"The tones I use the most are **Large Room, Bright Room, Dark Room, Dark Chamber, and Narcissus**. Dark Chamber and Dark Space automatically have more chorusing on them so they sound more wishy-washy. Narcissus is great on pianos. Large Room and Bright Room — **Bright Room in particular sounds fantastic on basses** — sound fantastic on just about anything."

## Closing
Praises it as extremely low CPU, "insanely cheap" ($50), versatile, the most elegantly-simplified reverb he's used. Credits Sean Costello / valhalladsp.com.
