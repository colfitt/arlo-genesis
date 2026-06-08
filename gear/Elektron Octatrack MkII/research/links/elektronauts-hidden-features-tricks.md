https://www.elektronauts.com/t/ot-special-tricks/7416
elektronauts.com · Octatrack subforum (+ "P-locking a sample lock" /14486, MOD WIGGLER OT Tips & Tricks t=88827, "Elektron Octatrack Master Reference" Google Doc)

# Hidden features + power-user tricks (the non-obvious moves)

## STRT (start point) is the secret weapon
- Apply an **LFO to STRT** (the sample start parameter, Playback page) to scrub through a sample for endless variation. On a **sample chain / sliced sample** this effectively rolls through different samples/slices — "completely different drum kits" from one chain.
- **Audition a whole sample chain** by putting a **HOLD-triggered LFO on slice start** to hear every sample in it.
- **Slide trigs on RATE** = "tape inertia" PIPO (ping-pong) playback / pitch glides — tape-stop and tape-start feel. (Made for this rig's degraded-tape aesthetic.)

## Sample LOCKS + SLICE LOCKS + p-locking them
- **Sample lock** = a different sample on a specific step. **Slice lock** = a specific slice on a step. Any slice is addressable anywhere/anytime via locks.
- You CAN combine a sample lock with p-locks on the same step (the "p-locking a sample lock" thread confirms it) — different sample AND different filter/pitch per step.

## Scenes as a keyboard
- Program several scenes with different filter/pitch/STRT values, then **hold the [SCENE B] button and tap scene slots like keys** to play them as a real-time performance instrument (beyond the crossfader morph).

## Crossfader → RETRIG
- Assign the crossfader to **retrig**: fade 1/16 hats up into 1/32 or triplet rolls by moving the fader. **RTIM (retrig time) steps are tuned in accurate chromatic semitones** — retrig becomes a pitch/comb tool, not just a roll.

## The dice + reload
- `[TRACK PARAM] + [YES]` = randomize the current param page; `+ [NO]` = reload saved. Pair with **PART RELOAD** (`[FUNC] + [up/RELOAD]`) to safely tweak destructively then snap back to the saved Part.

## MIDI loopback trick
- Route MIDI **OUT back into MIDI IN** with matching TRIG channels so one MIDI track can drive multiple audio tracks at once — unconventional polyrhythm/beat generation. (Use a DIN loop; mind feedback.)

## CC p-lock gotcha (MIDI tracks)
- The OT **filters out CCs that haven't changed** — if you p-lock a CC to a value equal to the track's default, it WON'T send. Fix: set the track default knob to a DIFFERENT value than the p-lock, or put p-locks on all trigs so a change always fires.

## Arp tricks (MIDI tracks)
- Turn ARP **legato ON + note length INF** → every note slides into the next; p-lock legato off on notes you don't want to slide.
- Drive the arp with a **stepped-random LFO (trig'd per note)** over a sparse sequence to sprinkle generative flourishes on top of a riff.

## Removing locks surgically
- Hold **[NO] + the PARAM knob** while the sequencer plays over the step to wipe ONLY that parameter's locks (not the whole trig).
