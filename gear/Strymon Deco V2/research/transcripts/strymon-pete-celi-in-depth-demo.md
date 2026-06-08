https://www.youtube.com/watch?v=ST8pp4HN554
strymon · Deco Tape Saturation & Doubletracker pedal - In Depth Demo · 2014-11-03

> NOTE: This is the official Strymon factory demo, narrated by sound designer Pete Celi. It documents the **original Deco**, but the two engines (Tape Saturation + Doubletracker), all the controls demonstrated here (Saturation, Volume, Lag Time, Blend, Wobble, Type: Sum/Invert/Bounce), and their behavior are **carried over unchanged into the V2**. The V2 only *added* the Tone knob, the Cassette voice, full stereo I/O, and MIDI/presets — none of which contradict anything below. This is the single most authoritative explanation of how the engines actually work.

## Tape Saturation

The tape saturation effect is characterized by the addition of odd-order harmonics that create a nice fattening up of the signal and some dynamic compression, which helps tame the peaks. Additionally there's dynamic band-limiting, which is very effective in creating a sense of dynamics in the frequency response: high, sharp transients are not only limited through compression but also band-limited through the interaction of the pre-emphasis and de-emphasis equalization in the tape process.

At low levels of saturation the effect is very transparent — something that's felt a bit more than heard. (Demonstrates bypass, then saturation at minimum.) It's barely audible as an effect, but you do feel it and sense it when playing.

As you increase the saturation the tape system gets driven harder and produces more odd-order harmonics. You can hear the increased harmonics in the low end and the fattening of it, plus a little bit of saturation effect on the top end. As we increase saturation further we push the system harder and start creating more distortion products and get more of the compression effect.

That (around 2 o'clock) is about the limit you'd push a deck in a recording environment, where you'd be really slamming the VU meters. We thought it'd be nice to extend the range to allow the same principles of the effect to go into further levels of saturation, so if we turn it up further — at maximum we get a decent amount of gain, certainly for a tape-style system.

One of the nice aspects of the tape system is its dynamics: at low levels the system is essentially wide-bandwidth, clean reproduction, and it responds very nicely to dynamics. Harder inputs and attacks benefit from the compression and dynamic band-limiting, but low-level inputs stay clean. That allows it to be very responsive to your volume control and very transparent. So you can set a fairly high level of saturation, and turning your guitar volume back (or switching to a lower-output pickup) cleans it up.

**Workflow takeaway (Celi's own framing):** "It lends itself to setting it at a certain distortion level and letting your guitar volume really set the amount of drive through the system, without sacrificing your tone when your volume's rolled back. As an always-on effect it's nice to have it at a level where you don't really hear any saturation, but it's fattening up your sound in a way that lends itself to kind of sweeten everything that's before it."

With a low-output Strat (vs. humbuckers): at minimum it's very subtle; around **10 o'clock** it's warming up the sound and getting some of the benefits. At maximum it adds harmonics and dynamic compression but doesn't take the characteristic tone away from the instrument — it's just enhanced. Rolling the guitar volume back keeps the tone intact and clean, suitable for dynamic playing; even picking very lightly still retains the clean base tone.

## Doubletracker

Doubletracking effects are achieved in the studio by running two tape decks simultaneously, offset from each other in time. The amount of time offset determines the type of effect:
- **through-zero flanging** at very short delay times,
- **tape chorus / doubling** at slightly longer offsets,
- **slapback echoes**, then
- **longer tape delays** as the offset increases.

The parameters engineers manipulated to create variations were: the relative mix level of the two decks; the offset in time; how the decks were summed (in phase, or one deck phase-inverted, or a variation); and they could manipulate one deck's flange (speed) to create motion beyond the static offset — which is how you get interesting through-zero flange and chorus sounds.

Deco's controls map directly:
- **Lag Time** = relative time offset between the two decks.
- **Blend** = relative mix between the two decks.
- **Type switch** = how the decks are summed: **Sum** (in phase), **Invert** (lag deck inverted relative to reference deck), **Bounce** ("we borrow the lag deck from the other channel to add an extra repeat").
- **Wobble** = random variation to the speed of the lag deck, "similar to manipulating the flange with your hand as the decks are turning."

### The Lag Time sweep (Blend at 12 o'clock = equal reference + lag)

Starting at minimum lag time, the lag deck is actually slightly **ahead** of the reference deck in time — you hear a comb filter created by the offset. As you increase lag time, the lag deck slows down to become synchronized with the reference deck **at the zero mark** on the knob; the two decks are essentially in phase there, so there's very minimal effect on tone. Continue turning and you hear more combing as the decks move further apart, then doubling and slapback sounds, a little further for separated slapback, then at maximum a **500 ms delay** (further than traditional doubletracking — they extended the range).

### Blend control

Turn Blend fully clockwise to hear **only the lag deck** (no reference signal). With lag at minimum and only the lag deck, add **Wobble** to get a pitched, randomized vibrato; reduce it for very slight variations. Bring Blend back to 50/50 and it works with the lag deck to create flanging, with a little Wobble emulating the engineer manipulating the reel.

**"For the most intense flanging effects you'll want to set the Blend right at 50/50 so the two decks can cancel and complement each other fully."** Just adjusting Blend slightly to favor the reference deck makes a big difference — cancellations/reinforcements are no longer absolute, so you get a more mellow flange.

### Type: Invert (negative through-zero)

Switching to Invert gives a **negative through-zero flanger** — a very different effect, as the frequencies that cancel and sum are swapped. You hear complete cancellations when the decks align, with the lag deck inverted in phase. To mellow it: reduce Blend, OR keep Blend at 50/50 and increase Lag Time slightly beyond zero so the lag deck approaches but **doesn't actually cross through zero** — full flange intensity without full cancellation. Increase Wobble for wilder excursions; increase lag time further with Wobble for nice tape-chorus effects. Use Blend to vary intensity (subtle to strong).

### Type: Bounce

Bounce uses the lag deck from the right channel (always active) and sums it back into the left channel, creating a second repeat / second lagged signal. **In stereo it gives a nice stereo effect; in mono it still creates a fatter sound; at longer delays it gives a second repeat.** In Bounce you get a wide stereo chorus spread; compare with Invert for a very nice stereo field. Increase lag further → very wide stereo chorus → doubling chorus; reduce Blend to mellow.

### Slapback and echo region

Going into slapback, you can exploit real physics: a wave reflecting off a back wall gets **inverted** as it bounces — recreate that with **Invert mode** so the echo returns out of phase with the dry signal. Compared to Sum it's a subtle difference, but Invert gives a sense of extra depth on the slap. Bounce gives the second repeat. Back in Invert with reduced Blend you get control over repeat level (very subtle, "hard to tell it's on until you turn it off — it just gives it a little extra depth and dimension"). Turn Wobble down for a straight slap with no motion.

Increase lag time further for delays suitable for lead fattening or rhythm enhancement; Bounce for the extra repeat; more Wobble for modulation depth. At maximum delay time, reduce Blend to have just a faint callback on the lead line. Increase Saturation to max to get a lead tone going.
