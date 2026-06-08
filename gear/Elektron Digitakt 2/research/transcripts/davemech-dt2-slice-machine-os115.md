https://www.youtube.com/watch?v=sSEMZsMSjd4
Dave Mech · MANUAL SLICES for Digitakt II // OS 1.15 Update Deep Dive · 2025-06-25

> Source captions: YouTube auto-generated, cleaned to prose. ~26m. DIGITAKT II specific — the OS 1.15 **Slice machine** (manual slicing). Builds a jungle/amen-break workflow.

## Adding the Slice machine
- New pattern, pick a track → SRC page → machine-select menu → **Slice** (the new SRC machine). Looks like the Grid machine but adds a dedicated slice editor.
- Load a sample (an amen break). On the SRC page press **YES** → menu: **Edit Slice Points / Create Slice Grid / Create Linear Locks / Create Random Locks**.
- **Create Slice Grid**: choose e.g. **32 slices**. New option **DIRT = transient detection** — places slice points on **zero crossings**, eliminating clicks. YES.

## Slice editor (a dedicated audio editor, Octatrack-style)
- Scroll slices by playing the track; arrows step through slices; enable the keyboard to play slices chromatically. Set the slice param to anything other than a specific slice and the keyboard plays all slices individually.
- New **trig mode = Slice**: all 16 trig keys become the slices; change pages to scroll through more slices. Record a drum pattern efficiently this way.
- Editing a slice: **ZOOM** (FUNC = vertical zoom for quiet sections), **POSITION** (move the view), **START/END** points. The link toggle connects this slice's end to the next slice's start (move one and both move); disconnect to set them independently — re-catching the next start reconnects. **LOOP point** (useful with play-mode Loop). FUNC snaps a start/end to a **zero crossing**.
- Remove a slice: **FUNC + left**. Add/split a slice: **FUNC + right** (splits the selected slice in two). Move the *entire* slice keeping its length: FUNC + POSITION.
- Save the sliced sample after manual chopping (so you don't lose the work).

## Playing & sequencing slices
- Keyboard mode plays slices; slices start at C1 and wrap around past the last slice. Octave changes apply.
- The SLICE parameter selects which slice a trig plays; you can also p-lock the slice per step.
- **Create Linear Locks** (slices 1,2,3,4…) or **Create Random Locks** for instant rearranged sequences — "a lot of fun". Copy a page, go back to Random Locks, paste the first page back to keep a good intro and randomize the next page.
- **Note LENGTH** > one step plays *multiple consecutive slices* (timing is lost after the initial slice — it just plays straight on). Length 1 = choppy; length 2 = longer phrases.
- **Retrig** on slices is "pretty cool". **Reverse** play mode plays each slice backwards; reverse+loop too.

## Mangling (the aesthetic-relevant part)
- LFO → slice-select with **sample-and-hold** (a little slew/slope) for smooth randomness.
- Tune slices down an octave for weight; add delay (change delay time); add bit crush — "destroy it as much as you want".
- LFO retrig off → set LFO to **trigger mode**; copy LFO1 to LFO2 and route LFO2 → low-pass frequency; reverse + loop per slice.
- Switch the filter to **Comb** filters for metallic synthesis of the drums, or **Lowpass 4** ("love that one"). Shorten and modulate.
- Worked example: sliced an amen break fully, sequenced a classic jungle beat, then performance-mangled with per-slice tuning p-locks, delay-time changes, bit crush, LFO-to-filter, retrigs, reverse-loop.

Dave Mech: "you can slice a sample up and make it into something completely different in a matter of seconds — that's the cool thing about the Digitakt II."
