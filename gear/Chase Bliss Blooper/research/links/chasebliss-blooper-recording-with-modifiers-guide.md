https://blooper.chasebliss.com/resources/docs/recording-mod.pdf
chasebliss.com (official Blooper resources) · Chase Bliss Audio · undated (current with v3.x firmware)

Official "Recording with Modifiers — a guide to blooper's stranger side" PDF. This is the deepest official doc on ADD-mode behavior and contains a HIDDEN FEATURE (Additive Assist) not covered in the standard manual. Distilled below.

## The "two-headed anomaly" — the single most important mental model
Blooper uses a record head and a play head (tape-machine concept). On normal loopers the two heads are locked together. On Blooper, **time-based modifiers split the heads apart.**

> "The record head is always steady. It always moves forward, at real-time speed... If things are getting zany, it's always the play head's fault."

Consequence: when you overdub WHILE a time-based modifier is running, **what gets recorded depends on the play head's location, but WHERE it's recorded depends on the record head's location** — they are in different places, so "you may wind up overdubbing one part of your loop into another." When the modifier turns off, the heads snap back in sync.

### Modifier classification (which ones split the heads):
- **Time-based (will desync the heads):** Speed, Trimmer, Stutter, Stretcher, Scrambler, Stopper (tape-stop side).
- **Non-time-based (heads stay in sync — safe to overdub under):** Dropper, Swapper, Filter, Pitcher, Stopper (fade-out side).

This is a genuinely useful distinction the dossier doesn't break out: if you want to overdub cleanly while a modifier colors the sound, use a NON-time-based modifier (Filter, Pitcher, Dropper, Swapper). Pitcher is explicitly the "safe zone" alternative to the Speed modifiers.

## THE FIXED LENGTH rule (ADD mode)
> "Once you set the loop length with your original recording, it will never change. Ever, no matter what. You can think of it like a container — you can change the contents, but the container is always the same size."

The consequence everyone trips on:
- Record a 3-sec loop, engage half-speed, do a one-shot overdub → because the loop now "wants" 6 sec but the container is still 3 sec, **half your recording gets squeezed out / lost — it can't fit.**
- Conversely, record a 2x-speed modifier and your loop content plays twice within one loop length.
- UPSIDE for this rig: for synced/rhythmic loops the fixed length is a feature — you can record any modifier chaos and the loop stays exactly the same length, never drifting out of sync with the Digitakt clock.

## HIDDEN FEATURE: "Additive Assist" (BLIP toggle, OFF by default)
There are two ADD-mode recording behaviors, switchable in the BLIP interface:
- **Free Recording (default):** play head and record head drift apart continuously; the longer a modifier is on, the less you know where you're recording. "Useful if you want to embrace the unexpected." Tip: the loop-reset LED blinks each time the record head hits the loop start — use it to track the record head.
- **Additive Assist (optional, enable in BLIP):** "resets the play head whenever the record head reaches the beginning of the loop." This makes the loop play the SAME each pass no matter what modifiers are on — so you get a repeatable pattern, can tweak modifiers to taste, then commit a one-shot. Much more predictable / less random.

→ For this drone/doom rig: leave it on Free Recording for happy-accident walls; switch to Additive Assist (via BLIP) when you want to dial in a specific modifier result before printing it.

## Named overdubbing techniques (ADD mode)
- **One-shot** — "print modifiers neatly into your loop." Overdubs for exactly one loop length, then auto-stops and turns the modifier off. Engaged by briefly HOLDING the record footswitch (record LED blinks). The clean way to commit one modifier pass without timing it by hand.
- **Punch-in** — guarantees precise placement. Order: (1) start overdubbing, (2) briefly engage modifier, (3) stop overdubbing. Because audio isn't altered until the modifier turns on, you can be relaxed about start/stop timing. "Great for placing unique moments and blips into your loop."
- **Accumulation** — leave a (generally mild) modifier on while overdubbing so the loop evolves. The marquee recipe: (1) record a loop, (2) turn up STABILITY, (3) start overdubbing → loop ages like a tape machine wearing out in real time. Radical version: steadily record Stutter or Trimmer to slice the loop into smaller and smaller parts. Key advantage over Frippertronics: "you can play new notes as you go, which will appear fresh and start the cycle all over."

## NORMAL-mode experimental recipes (modifiers NOT baked in)
- **Mystery looping** — record a loop; turn ON Trimmer (loop shrinks to a small play area); record overdubs into that small window; then turn Trimmer OFF → "your whole loop, and the overdubs you've been recording... could be anywhere!" Structured surprise/chance.
- **All slow** — record a loop; engage Stepped Speed at half-speed; begin overdubbing. "Notice that everything — including your new overdubs — play at half-speed. This behaviour is unique to Blooper, allowing you to build up a slow soundscape over time while your live playing naturally stays in the forefront." (Great for doom: a half-speed bed under live, full-speed banjo/baritone.)

NORMAL-mode caveat: overdubbing with a time modifier ON still lands your new audio in unexpected places (head disconnect), even though the modifier itself isn't recorded. For straightforward looping, turn time-based modifiers OFF before overdubbing.
