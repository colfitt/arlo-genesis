https://www.chasebliss.com/ (per-pedal MIDI manuals, URLs inline)
chasebliss.com + local MIDI manuals · Chase Bliss · accessed 2026-06-03

# CB-stack presets & whole-stack scene recall via the Digitakt 2

Reusable across all 7 CB pedals. Verified against the MOOD MkII, Lost + Found, Onward, and Big Time MIDI manuals (verbatim). The CB preset/PC model is uniform, which is exactly what makes one-PC whole-stack "scenes" possible.

## 1. How CB onboard presets work

- **The face toggle = 2 presets.** Every CB pedal with a 3-position PRESETS toggle stores **slot 1 = right position, slot 2 = left position, middle = "live" (current knobs)**. (Verbatim in MOOD/L+F/Onward manuals.)
- **MIDI expands this to a deep preset bank:**
  - **MOOD MkII, Lost + Found, Onward, Blooper: 122 total preset slots** (slots 1–2 = the face toggle).
  - **Big Time: 127 slots** (10 factory presets loaded; restorable by holding MOTION+VOICING 5 s on the slot).
  - **Generation Loss MkII: 2 onboard presets** + PC recall of saved slots (PC/CC only, no clock).
- **Saving onboard (no MIDI):** hold a footswitch combo to store to the left/right slot (e.g. Onward: hold right FS 3 s then add left FS 3 s for the right slot). Exact combo differs per pedal — see each base manual.

## 2. Save / recall a preset via MIDI (uniform across the stack)

**Quoted, essentially identical wording on MOOD / L+F / Onward / Big Time:**
- **Recall:** *"To recall a preset, simply send [pedal] a Program Change message."* PC# → that slot. *"If the target slot is empty, nothing will be recalled."*
- **PC 0 = LIVE mode:** *"Sending a Program Change message of 0 puts the pedal in 'Live' mode, matching the pedal's current [knob] settings."* (So PC0 = "ignore presets, follow the knobs.")
- **Save:** *"send a Program Change message while holding down both footswitches"* → saves current settings to that slot number. (e.g. PC 45 while holding both = save to preset 45.)
  - Big Time also exposes **CC#27 = save-to-slot** (value = slot #) and **CC#28 = save to current slot** — saveable hands-free over MIDI. (Lost + Found / MOOD use **CC111 = SAVE PRESET**, value = slot #.)
- **No factory presets** beyond the two loaded in slots 1–2 (except Big Time's 10 factory presets).

## 3. One-PC whole-stack "scene" recall from the Digitakt

The payoff. Because every CB pedal recalls a preset on the SAME PC mechanism, you have two scene strategies:

### Strategy A — shared channel, one PC = whole-stack scene (simplest)
1. Set **all the CB pedals you want in a scene to the SAME MIDI channel** (e.g. ch.2 default). (Power-up + send a PC on the target channel to set each.)
2. **Save the same preset NUMBER on every pedal** for a given song/scene — e.g. "Verse" = preset **10** saved on Blooper, MOOD, L+F, Onward, Big Time, Gen Loss.
3. From the DT2, send **one Program Change (PC 10)** on that channel → **every CB pedal on the channel jumps to its own preset 10 simultaneously.** That's the whole-stack scene in a single message.
- On the **Digitakt 2**, send PC per pattern/track: set the MIDI track's **PROG CHG** value (and the MIDI channel) so changing pattern fires the scene. DT2 can send PC on pattern change or as a trig.

### Strategy B — distinct channels, addressed individually (max control)
1. Give each pedal its own channel (Blooper ch.2, MOOD ch.3, L+F ch.4, Onward ch.5, Big Time ch.6, Gen Loss ch.7, Clean ch.8 — your choice).
2. Build a DT2 scene/pattern that sends a **different PC on each channel** (one DT2 MIDI track per pedal). More setup, but each pedal can load an unrelated preset number, and you can also send per-pedal CC automation without crosstalk.

➜ For this rig, **Strategy A (shared channel + matched preset numbers)** is the lean way to get song-recall across the whole CB board with one PC; use Strategy B only where you need per-pedal CC automation simultaneously.

⚠️ Gen Loss MkII and Clean recall presets fine via PC (they're in the scene), they just won't clock-sync (Gen Loss) or have unconfirmed clock (Clean) — see the clock file.

## 4. CC control of parameters + bypass/engage via CC (shared map)

The CB CC layout is **highly consistent** — learn it once:
- **Knobs / sliders:** **CC14–CC20** (top row of knobs left→right; CC20 is usually RAMP SPEED). E.g. Blooper LAYERS = CC15, RAMP = CC20; MOOD TIME=14/MIX=15/LENGTH=16/MODIFY=17/CLOCK=18; Onward SIZE=14; Big Time COLOR=14/TIME=15/…/WET=19.
- **Toggles / mode switches:** **CC21–CC23** (and up).
- **Footswitches:** **CC102 = right FS, CC103 = left FS, CC104 = ALT/hidden menu (hold both), CC105 = left-hold, CC106 = right-hold.** (Uniform on Blooper, L+F, MOOD, Onward. Big Time reassigns 102–107 in Loop Mode.)
  - **Bypass / engage via CC:** send the relevant footswitch CC — `off = 0, on = 1 or >`. (e.g. MOOD: CC102 = dry/loop BYPASS, CC103 = wet BYPASS; Onward: CC102 = Freeze bypass, CC103 = Glitch bypass; L+F: CC102/103 = R/L footswitch.) ⚠️ Exactly which "engage" a footswitch CC maps to is pedal-specific — check the pedal's CC table.
  - Onward extra: **CC108 = retrigger Glitch, CC109 = retrigger Freeze** ("send any value") — great for clock-quantized re-triggers.
- **Dip switches over MIDI:** **CC61–68 (left bank) and CC71–78 (right bank)** — every physical dip is a CC (off=0, on=1+). Lets you flip DRY KILL, TRAILS, BANK, ramping/sweep/polarity, etc. remotely.
- **Tap tempo:** **CC93** (legacy, "any value") on the whole stack; some pedals also map CC107. **EOM (Expression Over MIDI) = CC100** (0–127) — send an expression sweep over MIDI instead of a physical pedal.
- **Misc:** CC51 = clock ignore (clock file), CC52 = stop ramping / ramp-bounce, CC56 = factory reset.

## 5. Ramping / expression over MIDI (where relevant)
- **RAMP SPEED = CC20** on the stack; ramping waveform/bounce/sweep/polarity are dip CCs (CC52, CC66–68, etc.). The Digitakt can sweep any knob CC directly via p-locks for rhythmic, clock-quantized modulation — an alternative to onboard ramping that's grid-aligned even on pedals whose ramp LFO free-runs.
- **EOM (CC100)** lets the DT2 act as the expression pedal for any CB param that accepts expression — useful for Blooper VOLUME→ramp-speed, MOOD CLOCK swells, etc.

## Sources
- MOOD MkII MIDI Manual (122 slots, PC save/recall, PC0=live, CC map, CC111 save) — chasebliss.com
- Lost + Found MIDI Manual (122 slots, full CC map incl. CC61–78 dips, CC100 EOM, CC111 save) — repo Gear/Chase Bliss Lost & Found/manuals/
- Onward MIDI Manual (122 slots, CC14–23 knobs/toggles, CC102–106 + CC108/109) — chasebliss.com
- Big Time MIDI Manual (127 slots, 10 factory, CC27/28 save, CC110 clock out) — chasebliss.com
- Blooper MIDI quick-start (PC = recall loops, CC#1 RECORD/#15 LAYERS/#20 RAMP, auto-channel) — blooper.chasebliss.com
- https://www.chasebliss.com/generation-loss-mkii (MIDI PC, CC; 2 presets) ; https://www.chasebliss.com/clean (clock-sync feature-listed, CC-unconfirmed)
