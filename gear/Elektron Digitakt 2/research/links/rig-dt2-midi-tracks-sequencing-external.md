https://www.elektron.se/explore/digitakt-ii
Elektron Digitakt II User Manual OS 1.15A (local: manuals/Digitakt-2-User-Manual_ENG_OS1.15A_250708.pdf) · Elektron · 2025-07-08
Supplemented by: midi.guide/d/elektron/digitakt-ii · AudioVandal DT2 tutorial (https://audiovandal.com/elektron-digitakt-ii-tutorial-mastering-the-next-evolution-in-sampling-and-sequencing/)

# DT2 as MIDI brain — sequencing & modulating external gear

Authoritative source is the DT2 manual (§5.3.2 MIDI TRACKS, §14.4 MIDI CONFIG, §16.3 CONTROLLING A SYNTHESIZER, Appendix A MIDI machine). Distilled below with exact button combos.

## Any of the 16 tracks can be a MIDI track
- Each of the DT2's 16 tracks is freely audio OR MIDI (no fixed 8+8 split like the OG, which had 8 dedicated MIDI tracks). Assign a MIDI machine to make a track a MIDI track.
- **Assign MIDI machine:** `[FUNC] + [SRC]` to open the MACHINE menu → `[LEFT]/[RIGHT]` to the SRC category → `[UP]/[DOWN]` to select the **MIDI** machine → `[YES]`.
- A MIDI track triggers **a chord of up to 4 notes** with velocity/length, plus pitch bend, aftertouch, mod wheel, breath, AND **sixteen freely assignable MIDI CCs** per track. (NOTE: this is 16 CCs/track, correcting the "8 CCs" figure — the dossier spec table's "16 assignable CCs/track" is the right number.)
- MIDI tracks support the full Elektron treatment: **parameter locks, conditional trigs, LFO modulation (2 LFOs on MIDI tracks vs 3 on audio tracks), micro-timing, per-track length & time-signature (polymeter)**. They generate no sound; data goes out MIDI OUT / USB.
- Several tracks can share one MIDI channel; on a conflict the **lowest-numbered track wins**.
- The control-all function is NOT available on MIDI tracks.

## Where the MIDI parameters live (the 6 parameter pages)
For a MIDI machine the pages are remapped (manual Appendix A):
- **TRIG page 1:** NOTE, VEL (velocity), LEN (length), PROB (probability), LFO.T, **NOT2–NOT4** (chord offset notes — set to build up-to-4-note chords). TRIG page 2 = FILL / COND (trig conditions).
- **SRC page** (press `[SRC]`): **CHAN** (MIDI channel, OFF/1–16 — *cannot* be p-locked; OFF disables the track), **BANK** (sends Bank-change CC 0 MSB), **SBNK** (Sub Bank, CC 32 LSB), **PROG** (Program Change), **PB** (pitch bend), **AT** (aftertouch), **MW** (mod wheel), **BC** (breath). *All default to OFF/disabled — `[FUNC]` + press the DATA ENTRY knob to enable a parameter, then turn it.*
- **FLTR page 1** (press `[FLTR]`): **VAL1–VAL8** = the values for CC slots 1–8. FLTR page 2 (`[FLTR]` twice): **SEL1–SEL8** = which CC number each slot sends.
- **AMP page 1** (press `[AMP]`): **VAL9–VAL16** = values for CC slots 9–16. AMP page 2 (`[AMP]` twice): **SEL9–SEL16** = the CC numbers.
- **FX page:** empty for MIDI tracks. **MOD page:** 2 LFOs.

### Assigning which CC number a slot sends (incl. MIDI Learn)
- On FLTR page 2 / AMP page 2, set SELx to the standard MIDI CC number you want.
- **MIDI Learn:** on FLTR page 2 or AMP page 2 hold `[FUNC] + DATA ENTRY knob A–H` → "MIDI LEARN" pops up / param flashes → send the CC from the external device on the track's MIDI channel (or the auto channel) → the slot captures that CC number. Cancel with `[NO]` twice.
- You can name each CC slot: hold `[FUNC]` then press-and-hold a DATA ENTRY knob → naming screen.

### Default CC map (from manual Appendix B table)
VAL1 defaults to CC 70; VAL10→CC 61, VAL11→62, VAL12→63, VAL13→64, VAL14→65, VAL15→66, VAL16→67 (these are just defaults — reassign any slot to any CC via SELx).

## P-locking CCs, notes, and Program Change per step
- Because MIDI tracks behave like audio tracks, **any VAL/PB/AT/CC parameter can be parameter-locked per step**: hold a `[TRIG]` step + turn the DATA ENTRY knob → that step sends its own CC/value. This is how you automate an external pedal/synth parameter rhythmically (filter sweeps, pedal mix, etc.).
- **Program Change per step (recall external presets in time):** the canonical technique is a **trigless/"lock" trig** — place a trig that carries no note-on, then p-lock **BANK / SBNK / PROG** on it (set on the SRC page). When the sequence reaches that step the DT2 fires the bank+program change. (Elektronauts confirms: "when sending PC to non-elektron devices… you're sending bank, sbnk and program number." Note an Elektron *receiver* defers a mid-sequence PC until the pattern plays through; third-party gear generally acts immediately.)

## Connecting & enabling MIDI out (§16.3 walkthrough)
1. MIDI cable: DT2 **MIDI OUT** → synth/pedal **MIDI IN**.
2. `[SETTINGS]` → MIDI CONFIG > **PORT CONFIG** → set **OUT PORT FUNC = MIDI** (the OUT/THRU ports can alternatively send DIN-24 / DIN-48 sync — see clock-sync file).
3. Same menu: **OUTPUT TO = MIDI** (or MIDI+USB / USB).
4. Main screen: `[TRK] + [TRIG 1–16]` to select a MIDI-machine track.
5. `[SRC]` → set **CHAN** to the target channel.
6. Set the external device to receive on the matching channel.

## Auto Channel (play/record the active track from a controller)
- `[SETTINGS]` → MIDI CONFIG > **CHANNELS** > **AUTO CHANNEL** = a single channel that always addresses the *currently selected* track. An external keyboard (e.g. Novation 61SL MkIII) sending on the auto channel plays/records whichever track is active — ideal for jumping between tracks live and for recording the MIDI tracks from a controller.
- **PROGRAM CHG IN/OUT CH** (CHANNELS menu): channels for PC in/out; "AUTO" uses the auto channel. Per-track parameter MIDI channel is **TRACK 1–16** in the same menu (OFF = no param send/receive). **FX CONTROL CH** addresses the Delay/Reverb/Chorus/Compressor/master-OD pages.

## Concrete rig application — sequencing the Boss VG-800
- VG-800 receives MIDI; sequence it on a DT2 MIDI track: set **CHAN** to the VG-800's MIDI channel; place **note** trigs to play its synth/GR voices; p-lock **PROG** on a trigless trig to switch VG-800 patches mid-pattern; assign CC slots (SEL1–16) to VG-800 CC-mapped parameters and p-lock VALx to modulate them in time. (Verify the VG-800's exact CC/PC map in its MIDI implementation chart before relying on specific CC numbers.)
- Reverse direction: the VG-800's **pitch-to-MIDI** (from GK-5 on the baritone/banjo) can play the DT2 — route VG-800 MIDI OUT → DT2 MIDI IN on the **auto channel** to trigger the active track from a string instrument (monophonic lines track best).
