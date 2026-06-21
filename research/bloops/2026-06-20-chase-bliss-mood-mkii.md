# Bloop — Chase Bliss MOOD MkII
Date: 2026-06-20 · Category: gear · Corpus: gear/Chase Bliss MOOD MkII

## What we already knew  (from recon)

The MOOD MkII corpus was mature on controls, sonic behavior, dip switches, hidden options, recipes, and rig placement — but it had **essentially zero verified MIDI CC data in its own folder**. Specifically:

- `GearProfile.md` flagged `midi:true` with empty MIDI notes (placeholder channel field).
- The DeepResearch (§8/§12) described MIDI only as "Full — note, PC, CC, clock sync via Chase Bliss MIDIbox" with **no CC numbers**.
- The UsageGuide (§5) asserted only **three** MOOD CCs — CC51 (clock-ignore), CC53 (wet division), CC54 (looper division) — plus default channel 2, all borrowed from shared `cb-stack` files in the **Blooper** folder rather than verified against a MOOD source.
- The bundled `manuals/MOOD+MKII_Manual_Pedal_Chase+Bliss.pdf` is the **27-page MAIN pedal manual**, which contains **no CC chart** and explicitly defers MIDI detail (p.49: "MIDI requires a Chase Bliss MIDIbox to convert the signal to a 1/4" TRS jack... check out the MIDI manual").
- A scattered, partially-verified MOOD CC set existed across the Blooper `cb-stack` files but was not assembled, not in the MOOD folder, and not cross-checked.
- **The deliverable gap:** MOOD was the **only** `midi:true` Chase Bliss pedal lacking a `research/links/midi-official-cc-chart.md`, the file every sibling (Onward, Brothers AM, Blooper, Clean, Generation Loss, Big Time) already has.

## New findings  (verified)

### Official / primary-source

**The dedicated MOOD MkII MIDI Manual was located, downloaded, and is now the on-disk primary source.** It is a separate document from the 27-page main manual — internal ref "CBA ref 2023 - MD2", embedded title "Chase Bliss MOOD MKII MIDI manual", letter-size, with the CC chart and Synth Mode tables. Fetched from the Squarespace CDN and saved to `gear/Chase Bliss MOOD MkII/manuals/MOOD+MKII_MIDI-Manual_Pedal_Chase+Bliss.pdf` (669,120 bytes; byte-identical to the live URL). Contact `midi@chasebliss.com`. Source: [official MIDI manual PDF](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf); [chasebliss.com/manuals](https://www.chasebliss.com/manuals).

**The missing deliverable file now exists**, transcribed verbatim from the PDF and formatted exactly like the Onward sibling (header block: primary URL + midi.guide cross-check + default-channel/PC paragraph, then a `| CC | Parameter | Notes |` table): `gear/Chase Bliss MOOD MkII/research/links/midi-official-cc-chart.md`. This closes the #1 gap.

**Front-panel knob CCs (resolves the two-MODIFY-knob ambiguity).** Verbatim KNOBS table: CC14 Time, CC15 Mix, CC16 Length, **CC17 Modify (Wet Channel)**, CC18 Clock, **CC19 Modify (Micro-Looper)**, CC20 Ramp Speed — all 0-127. The pg.8 Tape/Stretch mode-speed value tables are keyed to CC19, confirming CC19 is the looper modify; midi.guide independently labels CC17 "Wet channel modify" and CC19 "Micro-looper modify." This corrects the scattered `cb-stack` data, which listed only a single ambiguous Modify=CC17 and omitted CC19. Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf); [midi.guide](https://midi.guide/d/chase-bliss/mood-mkii/).

**Engine/mode-select CCs (answers the human's "which CCs select Loop vs Delay/Reverb" question).** There is no single mode CC — each engine is its own 3-way toggle: **CC21 = Wet Channel engine** (REVERB=0,1 / DELAY=2 / SLIP=>2), **CC23 = Micro-Looper engine** (ENV=0,1 / TAPE=2 / STRETCH=>2), and **CC22 = Routing** (IN=0,1 / IN+micro-loop=2 / micro-loop only=>2). Both PDF and midi.guide agree on every value range. Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf); [midi.guide](https://midi.guide/d/chase-bliss/mood-mkii/).

**Per-channel clock-division CCs with exact subdivision list.** CC53 = Wet Channel division, CC54 = Micro-Looper division, each 0-7, **both saved globally**, with an identical enumeration: 0=thirty-second, 1=sixteenth, **2=eighth-note triplet**, 3=eighth, **4=dotted-eighth**, 5=quarter, 6=half, 7=whole. CC51 = MIDI Clock Ignore (0=ignore, >0=follow, saved globally). A footnote: if multipliers push the BPM past the max, the BPM halves until in range. This corrects the UsageGuide's loose "0=1/32…7=whole" — the middle steps are not linear (index 2 is a triplet, index 4 is dotted). Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf); [midi.guide](https://midi.guide/d/chase-bliss/mood-mkii/).

**Dip-switch CCs — fully enumerated (previously entirely unsourced for MOOD).** Left Bank (Ramping/Expression) CC61-68: 61=Time, 62=Modify (Wet), 63=Clock, 64=Modify (Micro-Looper), 65=Length, 66=Bounce, 67=Sweep (B=0/T=1+), 68=Polarity (F=0/R=1+). Right Bank (Customize) CC71-78: 71=Classic, 72=Miso, 73=Spread, 74=Dry Kill, 75=Trails, 76=Latch, 77=No Dub, 78=Smooth. Manual note: "CC numbers are left to right as you look down over the top of the pedal. The left bank is labeled 61-68 and the right bank is 71-78." The two MODIFY dips (62, 64) mirror the two MODIFY knobs. midi.guide independently lists the identical block. Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf); [midi.guide](https://midi.guide/d/chase-bliss/mood-mkii/).

**Hidden-option CCs CC24-33 (previously entirely unsourced for MOOD).** CC24 Stereo Width (0-127), CC25 Ramping Waveform (5 stepped ranges 0-14 / 15-54 / 55-80 / 81-126 / 127, waveforms not named), CC26 Fade (0-127), CC27 Tone/hi-cut (0-127), CC28 Level Balance (0-127), CC29 Direct Micro-Loop (0-127), CC31 Sync (=0,1 / no sync=2 / =>2), CC32 Spread (only=0,1 / both=2 / only=>2), CC33 Buffer/Loop Length (Half like MkI=0,1 / Full=>1). **CC30 is unused** — the table jumps 29→31, matching the Onward chart's CC30 gap. Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf).

**Synth Mode CCs (confirms and extends the UsageGuide's CC59 claim).** Synth Mode **auto-engages on any incoming MIDI Note — there is no dedicated enter CC** ("ENTER SYNTH MODE = NA, any value"). Exit = CC59 (>1) or move the Clock knob. CC58 Output Type (OPEN=0 / ON-OFF=1 / ADSR=>1), CC57 Octave Transpose (1=12 semitones … 9=108 semitones), CC80-83 ADSR (Attack/Decay/Sustain/Release, each 0-127), CC84 Portamento (0-127), CC1 Mod Wheel (0-127); Pitch Bend range ±4 semitones (no CC). MIDI Notes drive the CLOCK knob in semitones; **MIDI clock is ignored while in Synth Mode**; Synth Mode settings are saved globally, not per-preset; the pedal follows velocity in On/Off and ADSR modes. Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf); [midi.guide](https://midi.guide/d/chase-bliss/mood-mkii/).

**Preset / Program-Change model (confirmed verbatim).** PC recalls/saves presets. **PC 0 = "Live" mode** (matches current settings). **122 total slots**; slots 1 & 2 = the face preset toggle — **slot 1 = right position, slot 2 = left**. Empty slots recall nothing; the only factory content is the two presets pre-loaded in slots 1 & 2. To save: send a PC while holding both footswitches (PC 45 → preset 45), or send CC111 (0-122). This corrects the UsageGuide framing of "only 2 onboard slots" — there are 122 MIDI slots; only slots 1-2 are reachable from the face toggle. Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf).

**Misc / global CCs.** CC52 Stop Ramping (0=stop, >0=resume), CC55 True Bypass Mode (0=Standard Buffered, 1-127=True Bypass), CC56 Factory Reset (0-127), CC93/CC107 Tap Tempo (any value >0; exit tap mode by holding the footswitch and turning TIME), CC100 Expression Over MIDI (0-127), CC110 MIDI Reset (1-127; resets clock-ignore off, octave transpose +3 octaves, clock dividers to quarter note, portamento to 0, gate mode to 0). The repo's earlier "only three MOOD CCs" framing is superseded — the pedal exposes ~50 CCs. Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf); [midi.guide](https://midi.guide/d/chase-bliss/mood-mkii/).

**MIDI connector and default channel (chart header).** MOOD MkII receives MIDI over a standard 1/4" TRS patch cable (ring-active TRS); 5-pin DIN must be converted via the Chase Bliss MIDIBox, sold separately. Default MIDI channel = **2**; relearn by holding both stomp switches at power-up and sending the first Program Change. Confirmed in both the MIDI manual (p.1) and the main manual (p.49). Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf).

**Stepped/synced knob value tables (pg.8).** Captured into the chart Notes column so ARLO can snap to musical/discrete values: **SYNCED TIME (CC14)** 1/32=0-12 … quarter=111-128; **SYNCED LENGTH (CC16, Tape mode only)** x1/32=0-12 … x1=111-128; **STEPPED CLOCK (CC18)** 2k=0-4 … 64k=122-127; **TAPE MODE SPEED (CC19)** 4x Rev=0-4 … 4x Fwd=120-127; **STRETCH MODE SPEED (CC19)** No-Stretch-Rev=0-15 … Stalled=61-80 … No-Stretch-Fwd=127. Source: [MIDI manual](https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf).

### Comparison (rig / control-surface)

For ARLO's control surface, MOOD MkII is now the **deepest-MIDI texture/looper box in the rig stack**: both engines' knobs, both mode toggles, all 16 dips, 9 hidden options, **independent wet vs looper clock divisions (CC53/54)**, and a CC-addressable monophonic Synth Mode (ADSR CC80-83, octave CC57, portamento CC84) are all individually mappable. The dual-channel layout — separate bypass, freeze/overdub, modify, and clock-division per engine — lets ARLO sequence the Wet Channel and Micro-Looper as two semi-independent voices off one pedal, a flexibility the single-engine siblings (Onward, Generation Loss) don't have. **Caveat:** MIDI clock is ignored in Synth Mode and a stray MIDI Note auto-engages Synth Mode, so ARLO must avoid sending Notes on MOOD's channel when it wants clock-sync. (Lens confidence: medium — rig-fit reasoning, not a primary-source spec.)

## Flagged / uncertain

- **CC102/CC103 wet-vs-micro-looper bypass split — UNRESOLVED, verify on hardware.** The MIDI manual labels **both** CC102 and CC103 only as "BYPASS" (icons, no text), and CC105/CC106 only as "FREEZE"/"OVERDUB", without printing which is Wet vs Micro-Looper. The chart **infers CC102 = Wet/left bypass, CC103 = Micro-Looper/right bypass** from the main manual's footswitch layout (left=Wet, HOLD=Freeze=CC105; right=Micro-Looper, HOLD=Overdub=CC106). **midi.guide states the OPPOSITE: CC102 = Micro-looper bypass, CC103 = Wet-channel bypass** (and labels CC105 = Wet freeze, CC106 = Micro-looper freeze). The CC *numbers* (102/103/104/105/106) are certain; only the wet/looper attribution is in doubt. The chart honestly flags this; **do not rely on the 102/103 split until verified by ear on hardware.** This also supersedes the old `cb-stack` guess (CC102=dry/loop, CC103=wet), which the inference reverses.

- **Output Type CC — manual is authoritative (CC58); midi.guide is wrong (CC87).** The official PDF prints "OUTPUT TYPE 58" and details OPEN=CC58,0 / ON-OFF=CC58,1 / ADSR=CC58,2-127. midi.guide instead lists Output Type at **CC87** and omits CC58 — treat midi.guide's CC87 as a transcription error; the chart uses CC58. There is also a minor *internal* manual discrepancy: the pg.10 summary table abbreviates ADSR as ">1" while the pg.14 body text says "2-127" — both reconcile to ON/OFF=1, ADSR=2+. (Flagged in the chart's Notes.)

- **CLAIM REFUTED — "PDF and midi.guide agree on every CC number."** A recon finding asserted the two sources cross-checked and agreed on *every* CC. The verifier refuted this: they disagree on Output Type (CC58 vs CC87, above), on the CC102/103 wet-vs-looper split (opposite), and on CC106's label (PDF "Overdub" vs midi.guide "Micro-looper freeze"). **The deliverable file itself is sound** — it is a faithful verbatim transcription of the official PDF and correctly prefers the manual where the two conflict — but the blanket "agree on everything" statement is false. The manual is authoritative; midi.guide is a useful but looser secondary cross-check.

- **CLAIM CORRECTED — MIDI manual page count is 9 physical pages, not 14.** A recon finding called it a "14-page" manual with the CC chart on "pages 3-8" and Synth Mode on "pages 9-14." The verifier found it is **9 physical pages**; the "14" is the highest *printed folio number* (several sheets carry two folios). The CC/Control-Change chart spans physical pages 3-5; Synth Mode begins on physical page 6 (folio 09) and runs through page 8; the contact page is page 9. The file is genuine and authoritative — only the page-count/range description was wrong.

- **CC16 LENGTH glyph note (minor).** One recon detail described CC16 LENGTH as carrying "the water-drop/wet glyph." In the actual KNOBS table, LENGTH (CC16) carries no glyph — it carries an asterisk pointing to the pg.8 synced-value breakdown; the water-drop glyph is on the next row, CC17 MODIFY. Does not affect any CC number. The chart's CC16 row is correct.

- **Factory preset dump — standing gap, NOT closable from CB docs.** The MIDI manual states plainly "there are no factory presets besides the two that come loaded in slots 1 and 2." So no 122-slot factory dump exists to capture; only slots 1-2 ship populated (Andy Othling-authored). The Tim-&-Eric-named demos referenced in the UsageGuide (e.g. "Nude Tayne," "Tittleman's Crest") are audio demos on CB's SoundCloud, not retrievable patch files — copy-by-ear is the only route. `presets/` folder remains empty (low priority).

## Suggested corpus edits

- **`gear/Chase Bliss MOOD MkII/research/links/midi-official-cc-chart.md`** — DONE this bloop (new file). Verbatim CC chart from the official MIDI manual, Onward-format header + table + verification-flags section. Keep the CC102/103 and CC58-vs-CC87 flags intact.
- **`gear/Chase Bliss MOOD MkII/GearProfile.md`** — update the `midi:true` frontmatter / Notes section: fill the placeholder MIDI-channel field with **channel 2 (default; relearn by holding both footswitches at power-up)** and add a pointer to `research/links/midi-official-cc-chart.md` as the canonical CC source. (Still pending — flagged in recon as open.)
- **`gear/Chase Bliss MOOD MkII/research/MOOD-MkII-UsageGuide.md`** — §5 currently claims only three MOOD CCs (51/53/54). Replace with a one-line summary ("~50 CCs; full chart in research/links/midi-official-cc-chart.md") and correct the clock-division enumeration (the middle steps are triplet/dotted, not linear 1/16→1/8→1/4) and the "only 2 onboard slots" wording (122 MIDI slots; slots 1-2 = face toggle).
- **`gear/Chase Bliss MOOD MkII/research/MOOD-MkII-DeepResearch.md`** — §8/§12 describe MIDI with no CC numbers; add a cross-reference to the new chart so the deep-research doc stops being the only MIDI authority.
- **Index / `chunks.jsonl`** — re-run the suggestion-index build so the new chart's CC facts (tagged `content_type` as MIDI/CC) enter the corpus; MOOD currently contributes no CC chunks.
- **`manuals/` (DONE)** — `MOOD+MKII_MIDI-Manual_Pedal_Chase+Bliss.pdf` is now mirrored locally (669,120 bytes) alongside the main pedal manual.

## Candidate index chunks

- Chase Bliss MOOD MkII has a dedicated MIDI manual (CBA ref 2023 - MD2, 9 pages) separate from its 27-page main pedal manual; the main manual contains no CC chart.
- MOOD MkII receives MIDI over a 1/4" TRS patch cable via the Chase Bliss MIDIBox (sold separately); default MIDI channel is 2, relearned by holding both stomp switches at power-up.
- MOOD MkII knob CCs: Time=14, Mix=15, Length=16, Wet-Channel Modify=17, Clock=18, Micro-Looper Modify=19, Ramp Speed=20 (all 0-127).
- MOOD MkII has two MODIFY knobs: CC17 is the Wet-Channel modify, CC19 is the Micro-Looper modify.
- MOOD MkII engine-select CCs: CC21 selects the Wet Channel engine (Reverb/Delay/Slip), CC23 selects the Micro-Looper engine (Env/Tape/Stretch), CC22 sets Routing — each a 3-way toggle (0,1 / 2 / >2).
- MOOD MkII has independent per-channel MIDI clock divisions: CC53 = Wet Channel, CC54 = Micro-Looper, each 0-7 (0=1/32 … 2=8th-triplet … 4=dotted-8th … 7=whole), both saved globally.
- MOOD MkII Synth Mode auto-engages on any incoming MIDI Note (no enter CC); exit via CC59 (>1); MIDI clock is ignored while in Synth Mode.
- MOOD MkII Synth Mode CCs: CC58 Output Type, CC57 Octave Transpose, CC80-83 ADSR, CC84 Portamento, CC1 Mod Wheel; pitch-bend range ±4 semitones.
- MOOD MkII dip-switch CCs: Left Bank (Ramping/Expression) CC61-68, Right Bank (Customize) CC71-78; off=0, on=1+.
- MOOD MkII hidden-option CCs run CC24-33 (CC30 unused): Stereo Width, Ramping Waveform, Fade, Tone, Level Balance, Direct Micro-Loop, Sync, Spread, Buffer Length.
- MOOD MkII presets use Program Change: PC 0 = Live mode, 122 total slots, slot 1 = right toggle / slot 2 = left; CC111 saves (value = slot); no factory presets beyond slots 1 & 2.
- MOOD MkII bypass CCs are CC102 and CC103 (both labeled only "BYPASS"); the wet-vs-micro-looper split is unresolved — the manual is silent and midi.guide contradicts the inferred mapping.
- For Output Type, the official MOOD MkII manual uses CC58; midi.guide's CC87 is a transcription error.

## Follow-up questions

- **Hardware-verify the CC102/103 wet-vs-micro-looper bypass split** (and the CC105 Freeze / CC106 Overdub channel pairing) by ear on the actual pedal — the single unresolved attribution in the chart.
- **Capture the slots-1&2 factory presets by ear** (Andy Othling's Tim-&-Eric-named patches) since no MIDI dump exists; document as audio-reference recipes rather than patch files.
- **Name the CC25 Ramping Waveform shapes** — the manual prints only the 5 value bands (0-14 / 15-54 / 55-80 / 81-126 / 127) as icons; cross-reference the main manual's hidden-options chapter or a video walkthrough to label each band.
- **Confirm the CC32 Spread "only / both / only" wording** — which side (Spread vs Solo) maps to the low band vs high band — against the main manual's SPREAD/SPREAD-SOLO description.
- **Audit the other Chase Bliss siblings' charts** for the same midi.guide CC87/CC58-class slips now that MOOD exposed one.

## Sources

- Official MOOD MkII MIDI Manual (primary, CBA ref 2023 - MD2): https://static1.squarespace.com/static/622176a9b8d15d57ffbf5700/t/64405904508bd86d899117d0/1681938693019/MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf — mirrored locally at `gear/Chase Bliss MOOD MkII/manuals/MOOD+MKII_MIDI-Manual_Pedal_Chase+Bliss.pdf`
- Chase Bliss manuals index: https://www.chasebliss.com/manuals
- midi.guide cross-check (community, looser/secondary): https://midi.guide/d/chase-bliss/mood-mkii/
- Chase Bliss MIDIBox product page: https://www.chasebliss.com/shoputility/p/midibox
- Onward sibling chart (format template): `gear/Chase Bliss Onward/research/links/midi-official-cc-chart.md`
- Bundled main pedal manual (no CC chart; defers to MIDI manual): `gear/Chase Bliss MOOD MkII/manuals/MOOD+MKII_Manual_Pedal_Chase+Bliss.pdf`
