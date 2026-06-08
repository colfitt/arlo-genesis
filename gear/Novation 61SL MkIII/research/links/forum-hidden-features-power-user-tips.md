https://userguides.novationmusic.com/hc/en-gb/articles/25626813121298-Using-the-SL-MkIII-s-Arpeggiators-Arp
userguides.novationmusic.com (Arp / features / micro-steps KB) + loopopmusic.com review · current
(KB 403 WebFetch — distilled from search snippets quoting the official text + Loopop's walkthrough)

The buried-in-the-manual power moves. Several are unusually well-suited to this rig's drone/sustain aesthetic.

## Shift = "enable feature", press alone = "edit feature"
- **Hold Shift + Zones / Sequencer / Scales / Arp** to ENABLE that feature. Pressing the button by itself only opens its EDIT menu. This trips up everyone (see Brookes + Elektronauts files). Memorize: Shift turns things ON.

## HIDDEN: Arp Latch works even with Arp OFF → drone generator
- **Latch** holds notes and delays their note-offs until you release everything and play new notes.
- **Key trick:** Latch works **whether Arp is on or off.** With Arp OFF, Latch triggers a **continuous sustained MIDI note** regardless of arp state — i.e. hold a chord, latch it, and the SL keeps sending those note-ons indefinitely. Perfect for **sustained walls / drones into the VG-800 or a soft synth**, and for feeding external arps/long-sustain patches without holding the keys.

## Polyrhythmic generative arps (firmware 1.4)
- Each of the 8 Parts has its **own independent arp**. Latch several Parts and give each a **different arp Length/rate** → evolving polyrhythmic layers from one held chord. Add **arp probability** for drift. This is the aleatoric/"happy accident" engine for the rig.

## Scales apply to the SEQUENCER too (not just the keys)
- Scales mode: set root + scale, then choose **Filter** (off-key notes removed), **Snap** (played notes snap to nearest in-scale note), or **Display-only**.
- Hidden bonus: **sequences in a Part also conform to the scale setting**, and you can **transpose sequences in semitones** independently. So you can write loose and let Scale Snap keep everything in key across both live playing and the sequencer.

## Micro-steps (firmware 1.2) — exact procedure
- In **Steps** view press **Options** to reveal micro-steps.
- Pick a step (press its pad); the **6 micro-steps** light on the **top row of buttons** (above the faders).
- **Hold a micro-step button + play keys** to place a note on that micro-step. This is how you get triplet runs / glitch repeats / off-grid feel inside a 16-step pattern.

## Pattern Shift (firmware 1.4)
- Patterns view → **Options** → set **Pattern Shift** 0–15 to offset the whole pattern by N steps from its original position. Fast way to generate variations live.

## Other surfaced shortcuts
- **Shift + Play** = start from current position + send MIDI Continue (vs Play-from-top).
- **Grid** button toggles the 8×2 pads between the last Sequencer subview and Template mode.
- **Pads have polyphonic aftertouch** (the keybed strip is channel AT only — the pads are the poly-pressure surface).
- **Light guide:** key LEDs mirror scale notes / played notes / arp+seq notes / incoming external MIDI — usable as a visual play-along + scale aid.
