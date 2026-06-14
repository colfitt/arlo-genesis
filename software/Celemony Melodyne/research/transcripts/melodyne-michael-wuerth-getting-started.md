https://www.youtube.com/watch?v=hck80UJgXKc

Michael Wuerth · "How to Use Melodyne! Everything You Need to Get Started!" · 2020-12-31 · 14:43

(Practical session on Harry Styles "Watermelon Sugar" (re-sung). Strong on the pitch-drift vs pitch-modulation distinction and separating a note into transition/sustain/vibrato. Distilled from auto-subs.)

---

## Setup
- Melodyne is the **first insert** on the vocal track — "we're basically making a whole new version." Give it the **dry signal off the mic** so EQ/comp come later. If Melodyne is later in the chain, prior processing gets baked into the tuned vocal.
- Transfer: click **Transfer** or the **record-enable** button. The track list (left) shows every track that has Melodyne on it — you can **record-enable several at once** and transfer all in one play pass. (Non-ARA Pro Tools makes you wait; "almost every other DAW outside Pro Tools has much better integration… automatically transfers the audio.")

## Reading blobs (key clarification)
- The big orange shapes are an **outline of the waveform / volume**, NOT pitch — they're "misleading." Zoom in and the **thin red line through the centre is the exact pitch modulation** across the note. Focus on that red line when deciding where the note sits.
- Melodyne uses **averaging** to place a note, so double-click-snap isn't always "nearest lane." Example: a note that starts in tune then goes flat — double-click averages the whole thing and pulls it flat (worse). Fix = **separate** the in-tune part from the flat part, then snap each.

## The three pitch behaviours (the heart of Melodyne)
- **Pitch tool / double-click** = move/centre the note's average pitch.
- **Pitch Drift tool** (Pitch sub-tools, 3rd down) = the "**secret weapon**." Click-drag down on a note whose vibrato/peaks are drifting upward — it **keeps all the vibrato and natural movement** and just centres it in the lane. This is why Melodyne sounds the most natural of the tuners: you correct drift without killing motion.
- **Pitch Modulation tool** (Pitch sub-tools, 2nd down) = the **opposite/more destructive** one. Reduces vibrato depth; pushed to **100%** gives the vocoder / hard-autotune flatline. Used sparingly it just tightens a sustain.

## Advanced: split a note into transition / sustain / vibrato
On a held note, use **Note Separation** to cut it into pieces — the **transition** (the slide in from the previous word), the **sustain**, and the **vibrato tail** — so Melodyne analyses/averages each independently. Snap the transition, drift-correct the body, and (optionally) gently pull the **sustain** with the pitch-mod tool for a really tight centre without flatlining the whole note. Pull modulation too far → straight line → vocoder sound.

## Quick keys shown
- Select all = **Cmd-A**; centre everything with the Pitch tool, then apply modulation across the lot for an extreme/global autotune demo.

## Philosophy
Tuning is "post-production polish," like fixing the harness wires in a superhero movie — fine for a record, not a crutch for live. Decide how far to push.
