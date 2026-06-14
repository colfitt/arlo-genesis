https://www.manualslib.com/manual/3657983/Roland-Boss-Vg-800.html
manualslib.com (mirror of BOSS VG-800 Parameter Guide, eng02) · Roland Corporation · 2025 — distilled from local `manuals/VG-800_parameter_eng02_W.pdf`, pp.4–5

Authoritative ALT TUNE + 12STR + HARMONY + DUAL-string parameter values. These are the
exact "patch ingredients" for every alt-tuned/baritone/12-string memory. Param names and
ranges are manual-verified.

=== ALT TUNE block ===
- ALT TUNE SW: OFF, ON
- ALT TUNE MODE: ALT TUNE / HARMONY
- ALT TUNE TYPE (when MODE = ALT TUNE):
   - OPEN D, OPEN E, OPEN G, OPEN A — "open strings play a major chord"
   - DROP D–A — "With 'DROP D', the sixth string is tuned to a lower D. For the other
     tunings, the DROP D tunings are lowered even further." (DROP D / Db / C / B / Bb / A)
   - D-MODAL — "drops the first, second and sixth strings a whole step for an ethnic feel"
     (= DADGAD-type)
   - NASHVL — "raises the third, fourth, fifth and sixth strings one octave, giving the
     effect of playing just the secondary strings on a 12-string guitar"
   - 4TH — "tuning in fourths that raises the first and second strings by a half step"
   - -12 to +12 STEP — "lowers or raises ALL strings in half steps" (← THE baritone/doom
     transposer: -5 STEP = down a 4th, -7 STEP = down a 5th, -12 = down an octave)
   - USER — per-string tuning:
        PITCH 1–7 / PITCH HiC–LowB: -24 to 0 to +24 semitones (per string)
        FINE 1–7 / FINE HiC–LowB: -50 to +50
- KEY: C (Am) – B (G#m), Major/Minor (matches MASTER block KEY, p.37)

=== HARMONY mode (when ALT TUNE MODE = HARMONY) ===
- HARMONY: -2oct, ... UNISON ... , +2oct, USER — "pitch of the sound added to the input...
  up to 2 octaves higher or lower." (USER = USER SCALE number)
- USER SCALE table: per-key diatonic harmony intervals (C, D, E, F, G, A, B + sharps/flats),
  each string mappable to a harmony note above/below; triangles = octave offsets.

=== 12-string simulator (12STR) ===
- 12STR SW: OFF, ON — "adds the sound of a sub-string... like a 12-string guitar"
  (enabled for E.GUITAR/E.BASS/ACOUSTIC/AC BASS/DUAL)
- 12STR TYPE: NORMAL / USER
- 12STR PITCH 1–7 (HiC–LowB): -24 to 0 to +24 semitones (sub-string pitch)
- 12STR FINE 1–7: -50 to +50
- 12STR LEVEL 1–7: 0–100 (sub-string volume)
- 12STR DELAY 1–7: 0 ms–100 ms (delay before sub-string sounds — the jangle/shimmer knob;
  small per-string delays = the "24-String" / chorus-y doubling)

=== STR BEND (the B-Bender / pedal-steel mechanism) ===
- STR BEND SW: OFF, ON
- BEND CONTROL: 0–100 ("Normally set to 0, use a control assignment to shift bend 0→100")
- BEND DEPTH 1–7 (HiC–LowB): -24 to 0 to +24 semitones per string
  → B-Bender = BEND DEPTH on the B string only set to +2 (one tone up), assigned to CTL1.

=== DUAL string-delay (fake 12-string / chorus via two models) ===
- A:STR DELAY 1–7 / B:STR DELAY 1–7: 0 ms–100 ms — "delay the string sound of one of them
  to simulate a 12-string guitar." (NOT applied when ALT TUNE SW is OFF.)
  → This is the "fake chorus" Gear Sounds builds with DUAL GUITAR + per-string tuning offsets.

Confidence: HIGH — primary manufacturer parameter manual; all ranges/explanations quoted.
