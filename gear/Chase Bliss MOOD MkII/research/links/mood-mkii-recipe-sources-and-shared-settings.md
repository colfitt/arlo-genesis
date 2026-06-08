https://www.chasebliss.com/setting-the-mood
chasebliss.com + community sources · compiled · accessed 2026-06-03

# MOOD MkII — where to get patches/recipes + the best shared settings

## TL;DR on the preset situation
MOOD has only **2 onboard preset slots** (face toggle; 122 via MIDI — see the cb-stack file). Chase Bliss deliberately did **not** ship a "preset cookbook" — the pedal is pitched as a chemistry set for improvisation, and "tiny differences in knob settings can be crucial" (loopydemos), so exact-value sharing is genuinely hard. Recipes therefore live as **described techniques + approximate knob positions**, not exact patches. Below: where to look, then the concrete recipes worth copying.

## Where to find recipes / shared settings (ranked by usefulness)

1. **Official video manuals (pt.1 + pt.2)** — the authoritative "what each control does" reference; captured to `../transcripts/`. Build recipes from these.
   - https://www.youtube.com/watch?v=O87_xgGxJgI (controls/modes)
   - https://www.youtube.com/watch?v=9UzYim0o_Wo (dip switches / hidden options)
2. **Andy Othling's official onboard presets** — streamable demos at https://soundcloud.com/chaseblissaudio/sets/m-o-o-d (the "M O O D" set). These are *the* official "preset suggestions" referenced everywhere (see artists file). NOTE: the actual stored knob values aren't published as a table — you copy them by ear / by feel.
3. **loopydemos.com** — https://loopydemos.com/demos/chase-bliss-audio-mood/ — interactive demo widget where you can audition clips with the knobs shown per clip; author Silvio Schmidt also gives two named recipes (below) and confirms the manual's Othling presets.
4. **TheGearPage settings threads** — community sharing, but behind an anti-bot wall (couldn't extract programmatically; flagged):
   - "MOOD MKII Settings Share": https://www.thegearpage.net/board/index.php?threads/mood-mkii-settings-share.2548278/
   - "Chase Bliss MOOD mki Tips/Tricks/Settings": https://www.thegearpage.net/board/index.php?threads/chase-bliss-mood-mki-tips-tricks-settings.2464812/ (V1, but most settings translate)
5. **ModWiggler MOOD MkII thread** (modular/experimental crowd, on-aesthetic): https://www.modwiggler.com/forum/viewtopic.php?t=291890 (403'd to scraping; check in a browser).
6. **Facebook "Chase Bliss Audio Settings" group**: https://www.facebook.com/groups/193586297878114/ — active user setting-shares (login-gated).
7. **GuitarChalk "MOOD settings suggestions"**: https://www.guitarchalk.com/chase-bliss-mood-settings/ — ⚠️ **treat as unverified/likely-AI**: it lists "Reverb" and "Delay" as *knobs* with 1–10 values and a single-position routing per recipe, which does **not** match MOOD's real control set (Reverb/Delay/Slip are a 3-way MODE toggle, not two knobs). The vibe descriptions are fine; the exact numbers are not trustworthy. Do not copy verbatim.

## Verified named recipes worth copying

### From loopydemos (Silvio Schmidt) — V1 but valid on MkII
- **"Gooey Modulation"** — Wet Channel on **Delay** with a *very short* TIME, then use the dip switches to **auto-ramp TIME from zero up to the set short delay time** (the classic "warble up" you know from other delays). MIX sets the ramp rate when bounce/ramp is engaged.
- **"Pixy Dust"** — Wet **Reverb**, **CLOCK ramped from 0 to maximum** (one-shot or bounce). Produces a rising "level-up / slot-machine" sparkle as the sample rate climbs. "The MOOD reverb is very primitive by design" — lean into it.
- General loopydemos advice (verbatim): *"Don't worry about the dip switches. First, learn to use the pedal and pretend they're not there."* Then: *"Just try turning some knobs while playing... then dip those switches to get the MOOD to ramp it for you."* The **bounce** dip + a knob's own dip = MOOD turns that knob internally; MIX becomes the ramp rate.

### From the official video manual (Chase Bliss) — copyable starting moves
- **Manual time-stretch (Delay):** Wet **Delay**; turn **MIX and MODIFY up**, then sweep the **TIME** knob by hand — yields a manual tape-style time-stretch with no pitch artifacts.
- **Gritty Tape loop:** Micro-Looper **Tape**; combine a **slower CLOCK** with a **faster playback speed** (MODIFY toward 2×/4×) "to introduce interesting grit and vibe."
- **Frozen grain (Stretch):** Micro-Looper **Stretch**, **MODIFY at noon** freezes a single moment; **LENGTH** then sizes the held grain → sustained wall.
- **Stutter/freeze (Env):** Micro-Looper **Env**, small **LENGTH** (grains) → high; **MODIFY** sets detector sensitivity; play then go quiet so the current slice repeats.
- **Trail Catcher:** run a micro-loop through the **Reverb**, briefly toggle the Micro-Looper off then back on — it resamples the reverb trails into the loop (manual p.29; stated in pt.1 video).
- **Freeze pad:** hold the **left (Wet) footswitch** to repeat the current Wet sound infinitely; move knobs while frozen. (Reverb→ambient pad; Delay→looping echo; Slip→repeating tone.)

### Rig-specific starting points (already in the dossier §13, reproduced for copy)
- **Frozen micro-loop drone:** Wet Reverb TIME 2:00 / MODIFY 1:00; Micro Tape LENGTH noon / MODIFY half-speed; CLOCK 11:00; MIX 1:00; ROUTING IN+micro-loop.
- **Slip-reverb smear:** Wet Slip TIME 11:00 / MODIFY just off neutral; CLOCK noon; MIX noon; SPREAD on.
- **Granular stutter:** Micro Env LENGTH 9:00 / MODIFY low; Wet Reverb MODIFY low; CLOCK 10:00; + CLASSIC dip.
- **Clock-synced loop layer:** Micro Tape (length set by CLOCK) + SYNC hidden option; Wet Delay quarter-note TIME / MODIFY 1:00; feed MIDI clock.

## Recipe-building cheat-sheet (from the official walkthroughs)
- **CLOCK is tone+length+quality in one.** Low = aliased/crunchy/short loops; high = clean/hi-fi/long. The single most impactful knob.
- **Reverb:** TIME = decay/size; MODIFY CW = washed reverb, CCW = distinguishable multi-tap clusters.
- **Delay:** TIME = time (no pitch artifacts, sweepable); MODIFY CW = piles up like a looper.
- **Slip:** TIME = sample size (low = pitch-shifter, high = trailing harmonies); MODIFY = semitone-stepped speed/direction (CCW = reverse).
- **Tape:** LENGTH = playback amount; MODIFY = octave-quantized speed (½/1×/2×/4×, fwd/rev).
- **Stretch:** LENGTH = slice size (low = grainy, high = clear); MODIFY noon = freeze, CCW = classic stretch, dir set by side of noon.
- **Env:** LENGTH = slice size; MODIFY = audio-detector sensitivity.
- **CLASSIC dip** = MkI grit (clock noise, deteriorating loops). On-brief for "recorded-wrong."
- **Hidden gems:** Wet MODIFY = TONE high-cut; Micro MODIFY = clean micro-loop blend; Wet MODE = SYNC; Micro LENGTH = fade-while-overdub.

## Sources
- https://www.chasebliss.com/setting-the-mood (promo/blog; no recipe tables)
- https://www.chasebliss.com/mood-mkii (downloads: Manual, MIDI manual, "What's New" — no preset cookbook)
- https://loopydemos.com/demos/chase-bliss-audio-mood/ (Silvio Schmidt — Gooey Modulation, Pixy Dust, dip-switch advice)
- https://www.youtube.com/watch?v=O87_xgGxJgI + https://www.youtube.com/watch?v=9UzYim0o_Wo (official video manuals — see transcripts)
- https://soundcloud.com/chaseblissaudio/sets/m-o-o-d (Andy Othling's official presets, audio)
- https://www.thegearpage.net/board/index.php?threads/mood-mkii-settings-share.2548278/ (community share thread — bot-walled)
- https://www.guitarchalk.com/chase-bliss-mood-settings/ (⚠️ unverified, control names don't match the pedal)
