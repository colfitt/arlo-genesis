http://konstructnoise.blogspot.com/2015/08/octatrack-button-fu-beat-repeat.html
Konstruct Noise (blog) · author "Konstruct Noise" · Aug 2015

# BEAT-REPEAT / STUTTER via the master Delay + DELAY CTRL mode — full parameter recipe

The OT's hidden beat-repeat: park the FX2 Delay in a freeze/loop state, then play it live as a stutter from the trig row. Concrete values (quote-verbatim from the blog):

## Delay SETUP page (FUNC + FX2 / the setup screen)
- **SYNC = 1** (tempo-sync the delay time to grid)
- **LOCK = 1** (freezes the buffer — repeats hold instead of decaying)
- **PASS = 0** (kills the dry pass-through so you ONLY hear the repeated buffer)
- *(optional)* **TAPE = 1** — "can be interesting" (vari-speed tape character on the repeats)

## Delay MAIN page
- **TIME = 32** (the repeat length; 32 = a longer grab, drop lower for tighter stutters)
- **FB (feedback) = 127** (max — infinite/frozen repeat)
- **VOL = 127**
- **BASE = 0**
- **WDTH (width) = 127** (full stereo)
- **SEND = 2** (just enough to feed the delay; small value)

## Playing it live (the performance gesture)
1. Put the trig row into **DELAY CTRL** mode: **[FUNCTION] + [DOWN ARROW]** until "DELAY CTRL" shows.
2. **Press & hold the rightmost trig [P/T8]** → you hear the beat-repeat stutter on the held buffer.
3. With [P/T8] held, **tap the yellow-lit trigs** to set repeat rate — **trigs toward the LEFT = shorter delay time = faster stutter**.
4. **[P/T8] + a left trig together = freeze and set** that delay time.

## Rig fit
This is the "stutter/collapse" scene move made into a live instrument over the fuzz wall or a banjo loop. Park this delay on the Thru track (track 1) or the master, and ride DELAY CTRL during a crossfader B-side for glitch-collapse transitions. With LOCK=1 + FB=127 it's a true freeze — sustained-wall friendly.

PROVENANCE: community (Konstruct Noise blog, cited).
