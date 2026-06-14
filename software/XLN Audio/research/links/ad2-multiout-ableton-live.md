https://forum.ableton.com/viewtopic.php?t=152664
ableton.com forum "Addictive Drums, separate outputs in LIVE" + companion threads (t=152605, t=184234) · Ableton users · accessed 2026-06-11 (steps from search-indexed forum text)

# AD2 multi-out in ABLETON LIVE (the owner's secondary DAW — Live 12 LITE)

## Steps (Session or Arrangement)
1. Load the **Multi-Output** AD2 device variant on a MIDI track.
2. Inside AD2, click the **down-arrow** on each channel you want separated (turns
   the channel into a discrete output).
3. Create a **new Audio track** for each separated AD2 channel.
4. On each new audio track: **"Audio From" → Addictive Drums** (the AD2 track), then
   the second dropdown → pick the **specific AD2 channel/output** (kick, snare, OH…).
5. Set **Monitor → "In"** (default is Auto; In forces it to pass the AD2 output).
6. Repeat per drum. Then you can **deselect/disable** AD2's own stereo output to the
   Master so you're only hearing the routed tracks (avoids double signal).

## ⚠️ ABLETON LIVE 12 *LITE* CEILING — this is the real constraint for this rig
- **Live Lite caps total tracks at 16 (8 audio + 8 MIDI in older Lite; 16 in 12 Lite
  but still a hard ceiling).** A full AD2 multi-out wants ~10 mono + 3 stereo
  destination tracks PLUS the MIDI track — that can blow the Lite track budget by
  itself before you've added guitars/synths.
- **Practical Lite workflow:** do NOT explode every drum. Route only the 2-3 drums
  you actually want to degrade separately (e.g. snare + room out, kick out), leave
  the rest summed on AD2's internal master. Or: bounce/freeze AD2 to audio early and
  free up the device slot.
- The "render separate track outputs" thread (t=184234) notes export/freeze of
  multi-out can be fiddly in Live — **freeze-then-flatten per track**, or just
  bounce each routed audio track to a clip.
- Lite also limits scenes and some devices; if you hit a wall, this is a strong
  reason to do the heavy drum work in **Logic** and treat Live as the sketch/scene
  box.
