https://www.strymon.net/manuals/Deco_v2_UserManual_RevD.pdf
strymon.net · Strymon (official) · Deco V2 User Manual Rev D (created 2022-04-24)

Authoritative V2 reference for hidden/Live Edit functions, power-up modes, MIDI CCs, factory presets, factory reset. This is the V2-specific procedure set — it DIFFERS from older V1 guides (e.g. daftparagon, which uses "hold BOTH footswitches"). On V2 the Live Edit functions are entered by holding ONLY the TAPE SATURATION ON footswitch until both LEDs flash.

## LIVE EDIT (hidden) FUNCTIONS — V2 procedure
Enter Live Edit: **press and hold TAPE SATURATION ON until both LEDs flash, then release.** Turn the mapped knob, then press either footswitch to store/exit. All Live Edit settings are saved PER Favorite/MIDI preset.

| Hidden function | Knob | Behavior / LED |
|---|---|---|
| **Auto-Flange Time** | LAG TIME | sweep speed of the press-hold Auto-Flange. Both ON LEDs GREEN (fast) → AMBER (slow). Default = 12 o'clock |
| **Low Trim** | TONE | subtle high-pass to clean rumble/mud. TAPE SAT ON LED GREEN (full bandwidth) → AMBER (high-pass applied). Default = minimum (full bandwidth) |
| **Doubletracker Boost/Cut** | BLEND | ±3 dB level match for the doubletracker. Both ON LEDs GREEN (−3 dB cut) → AMBER (+3 dB boost). Default = 12 o'clock (unity) |
| **Wide Stereo Mode** | WOBBLE | Reference Deck→Left, Lag Deck→Right. Knob left of 12 = GREEN/Off (default); right of 12 = RED/On. Auto-disabled with mono out |
| **MIDI Clock Sync** | TYPE | echo repeats sync to MIDI clock. Switch DOWN to bounce = Off/RED (default); UP to sum = On/BLUE. When synced, DOUBLETRACKER ON LED lights PINK, LAG TIME becomes a mult/div |
| **MIDI Expression respond/ignore** | VOICE | switch UP classic = On/BLUE (default, responds to CC#100); DOWN cassette = Off/RED |

KEY CORRECTION vs older guides: V1 had a **High Trim** Live Edit (4 kHz low-pass on the SATURATION knob) AND Low Trim on the VOLUME knob, both via "hold both footswitches." On **V2** there is **NO separate High Trim Live Edit** — the new front-panel TONE knob handles saturation EQ — and **Low Trim moved to the TONE knob** in Live Edit (V1 had it on Volume). Only FOUR Live Edit params on V2: Low Trim, Auto-Flange Time, Wide Stereo, Boost/Cut (+ the two MIDI toggles).

## MIDI Clock detail (quoted from manual)
"When synced to MIDI Clock, the DOUBLETRACKER ON LED will light PINK, and the LAG TIME knob will act as a multiplier or divider of the incoming clock tempo. The synced LAG TIME mult/div settings from left to right are: **x2/3, x1, x2, x3, x4, x6, and x8. Maximum delay time is 500ms.**" — So you CAN clock the echo/lag to rig tempo, but it is a tempo MULT of the lag, not a wobble-rate sync. Wobble itself is free-running random, NOT clockable.

## POWER-UP MODES (persist across power cycles, NOT saved per preset)
Enter: hold the noted footswitch WHILE powering up, until both LEDs flash.
- **Input Mode** — hold DOUBLETRACKER ON; turn SATURATION. Normal/GREEN (default, instrument level) vs Studio/RED (+10 dB headroom for DAW/mixer insert/hot loop).
- **Bypass Mode** — hold DOUBLETRACKER ON; turn LAG TIME. True/GREEN (default) vs Buffered/RED (preserves highs over long cable runs).
- **EXP/MIDI Jack function** — hold TAPE SATURATION ON; turn LAG TIME. Expression/GREEN (default) · Favorite/AMBER · Tap/RED · MIDI/BLUE.
- **MIDI Channel** — hold TAPE SATURATION ON; turn SATURATION. Ch1/GREEN (default), Ch2/AMBER, Ch3/RED, Ch4-16/BLUE (set by next received PC).
- **MIDI OUT Mode** — hold TAPE SATURATION ON; turn TONE. Off/RED (default) · Thru/BLUE · Send CC PC Other/WHITE · Send CC Other/GREEN · Send PC Other/PURPLE · Send Other/AMBER.

## MIDI CC TABLE (full, from manual pg 34)
| CC# | Param | Range / values |
|---|---|---|
| 0 | Bank Select | 0-2 (0=Bank1, 1=Bank2, 2=Bank3) |
| 10 | Tape Saturation Off/On | 0=off, 1-127=on |
| 11 | Voice | 1=classic, 2=cassette |
| 12 | Saturation | 0-127 |
| 13 | Volume | 0-127 |
| 14 | Tone | 0-127 |
| 15 | Low Trim | 0-127 |
| 16 | Doubletracker Off/On | 0=off, 1-127=on |
| 17 | Type | 1=sum, 2=invert, 3=bounce |
| 18 | Lag Time | 0-127 |
| 19 | Wobble | 0-127 |
| 20 | Blend | 0-127 |
| 21 | Doubletracker Boost/Cut | 0-127 |
| 22 | Auto-Flange Time | 0-127 |
| 23 | Wide Stereo Mode Off/On | 0=off, 1-127=on |
| 25 | MIDI Clock Tempo Mult/Div | 0-6 (0=x2/3,1=x1,2=x2,3=x3,4=x4,5=x6,6=x8) |
| 33 | Bypass/On A and B | 0=bypass, 1-127=on |
| 60 | MIDI Expression Off/On | 0=off, 1-127=on |
| 63 | MIDI Clock Off/On | 0=off, 1-127=on |
| 93 | Remote Tap | any |
| 97 | Auto-Flange | 0=off, 1-127=on (i.e. trigger Auto-Flange via MIDI!) |
| 100 | Expression Pedal | 0=heel, 127=toe |

## MIDI PRESETS / PROGRAM CHANGE
- 300 presets, 0-299, split into 3 banks: Bank0=PC 0-127, Bank1=PC 128-255, Bank2=PC 256-299. To reach banks 1/2 send CC#0 (Bank Select) first.
- Reserved: **PC0 = Favorite (MiniSwitch); PC1/2/3 = MultiSwitch Plus footswitches A/B/C; PC127 (Bank0) = Manual mode** ("knobs" — live front-panel, no preset data stored there).
- Save in MIDI mode: hold BOTH footswitches (both LEDs blink GREEN) to arm; then either hold TAPE SAT ON until LED BLUE to save to currently-loaded slot, OR send a PC on the current channel to save to that slot. DOUBLETRACKER ON cancels.
- GOTCHA: some controllers number PC from 1 not 0 — increment by one.
- Quick MIDI test: with TAPE SAT footswitch OFF, send CC#10 value 127 — it should turn the Tape Saturation LED on if MIDI is wired/configured right.

## FACTORY DEFAULTS
EXP/MIDI Jack=Expression (controls SATURATION) · Input=Normal · Bypass=True · MIDI Ch=1 · MIDI OUT=Off · MIDI Clock Sync=Off · MIDI Expression=On · Low Trim=0% (full bandwidth) · Boost/Cut=12 o'clock · Auto-Flange Time=12 o'clock · Wide Stereo=Off.

## FACTORY RESET
Hold DOUBLETRACKER ON while powering up (until both LEDs flash, release), then **sweep VOLUME 0→100→0 twice** (LEDs cycle AMBER/RED/AMBER, then flash RED). Restores defaults AND replaces all stored presets with factory presets.

## FACTORY PRESETS (named, from Sample Settings appendix)
- PC0 "WIDE WOBBLE" (MiniSwitch Favorite)
- PC1 "WET SLAPBACK CASSETTE" (MultiSwitch Plus A)
- PC2 "ON THE EDGE" (MultiSwitch Plus B)
- PC3 "WORN OUT DECK" (MultiSwitch Plus C)
- PC4 "PRETTY TAPE FLANGE"

## OFFICIAL TIPS from Lag Time "In Depth" pages (manual pg 7-8), quoted/paraphrased
- **Flange (−.3-3 ms):** BLEND to 50/50 (12:00) for most pronounced flange. "Through-zero effects are more intense when using distorted guitars or high-bandwidth input signals" — feed it the dirt wall. A **static comb filter** is achieved when WOBBLE = minimum. For an inverted flange that "doesn't cancel completely," set BLEND below 12 and LAG TIME ~10:00 so the Lag Deck doesn't cross through zero. For random vibrato: min LAG TIME + BLEND maximum (no Reference Deck) + WOBBLE maximum.
- **Chorus (3-50 ms):** reduce BLEND toward Reference Deck for subtler. Switching TYPE sum→invert "will change the response of the low frequencies." Increase LAG TIME for wider chorus.
- **Slapback (50-150 ms):** with BLEND past 12, "the slap can be louder than the input." invert TYPE models a true wall reflection (waves invert on bounce). bounce TYPE = thicker slap with two distinct repeats.
- **Echo (150-500 ms):** lower BLEND for distant echo + add WOBBLE for random modulation-delay. bounce TYPE = two repeats filling the field.

## I/O / POWER (confirms dossier)
9VDC center-neg, 300 mA min. In = 1 MΩ Class A JFET (TRS adapter needed for stereo IN). Out = 100 Ω stereo (OUT L = mono). Max input +10 dBu. 24-bit/96 kHz. True bypass relay (default) or buffered. MONO/STEREO input slide switch on rear; in MONO, output is still stereo.
