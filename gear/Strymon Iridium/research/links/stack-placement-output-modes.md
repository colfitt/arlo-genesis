https://www.strymon.net/faq/how-can-i-disable-the-amp-or-cab-on-iridium/ + https://www.strymon.net/faq/how-do-you-connect-to-iridium/ + worship/FOH community reports (via Sweetwater reviews + jazzguitar.be)
strymon.net official FAQs + community · undated/2019–2024

# Stacking, placement & the 3 output modes

## Placement (the rule)
Iridium goes at the **END of the pedal chain** — "so the entire pedalboard connected to the amp is simulated." Dirt/mod/time pedals run INTO the amp input (Round/Chime/Punch), exactly like pedals-in-front-of-a-real-amp; the modeled cab+room is last. It replaces the amp+mic+cab, so nothing cab-sim-like should follow it.

## The 3 output modes (hold ON at power-up, turn DRIVE)
LED color shows the mode when ON:
- **Normal (RED)** — amp + cab + room. Default. The DI use.
- **Cab Bypass (AMBER)** — amp + room, NO cab IR. Feed Iridium's output into a real amp's **Power Amp In / FX Return** to use Iridium as the *preamp*. (Strymon notes this is off-label — the pedal's purpose is direct; "not recommended to connect Iridium to a guitar amplifier," but it's a valid power-amp/FRFR move.)
- **Amp Bypass (GREEN)** — cab + room, NO amp model. Load an **external preamp/dirt pedal into the IR engine**. This is the key non-obvious mode for this rig.
- **ROOM is ALWAYS active** in all three modes (cannot be removed, only level/size).

## Stacking recipes for THIS rig
1. **Amp Bypass + JHS Colour Box V2 (or any preamp/dirt).** Set Amp Bypass, run the Colour Box (its own preamp/EQ/dirt) → Iridium IN → Iridium just convolves a cab IR + room → Apollo. Turns the Iridium into a standalone IR loader for any external preamp. (Watch input level — a hot Colour Box output may want INPUT LEVEL = LINE; see tips file.)

2. **VG-800 FX-BYPASS → Iridium IR engine (the niche non-redundant pairing).** The VG-800's own amp/cab is its weak link (its reviewers call it "harsh/digital"). On the VG-800: `[▲]+[CTL 1]` = **FX BYPASS** (hear only the raw INST model, no Boss cab) and set OUTPUT SELECT = LINE/PHONES. Feed that into Iridium in **Amp Bypass** mode → Strymon's premium stereo IRs cab the raw Boss model. The ONLY sane way to combine the two boxes (don't stack two cab sims). Set Iridium INPUT LEVEL = LINE (the VG-800 line out is hot; the EHX Effects Interface is on the bench to reconcile levels if it clips).

3. **Travel board.** Iridium (FAV preset) + Polytune 3 (tuner first) + UAFX Del-Verb (after Iridium, or in front per taste) → interface or FOH. Complete amp+verb fly rig, any magnetic guitar, no real amp. Headphone out for silent practice.

4. **Bass DI.** Jazz Bass → Iridium with **AMP DISABLE / Amp Bypass** + a bass-cab IR loaded in a slot → clean bass DI with a real cab IR + room. Or use Punch lightly for grindy bass-amp grind. INPUT LEVEL stays Instrument for passive bass.

## FOH / interface connection (community-verified)
- Mono = OUT L; stereo = OUT L+R. To Apollo: straight into a LINE input, no DI box needed (100 Ω out, studio-grade).
- Long cable runs to a board: one user ran ~50 ft via a Mogami 1/4" TRS→XLR cable into a mixer with NO DI box, no issues. Worship players report 2+ yrs direct-to-FOH + IEMs on silent stage.
- Use the headphone jack to monitor yourself while OUT goes to FOH.
