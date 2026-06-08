https://www.strymon.net/faq/how-to-control-iridium-with-midi/
strymon.net · Strymon official FAQ · undated (current as of 2026)

# Iridium MIDI workflow (authoritative)

**Physical connection:** No 5-pin DIN. MIDI rides the **EXP jack** via the **Strymon MIDI EXP cable** (DIN-MIDI → TRS, with in-line filter), the **Strymon Conduit** hub, or third-party TRS-MIDI interfaces (Disaster Area, Empress, etc.). Set EXP jack to **DIGITAL** mode: hold FAV while powering on, turn LEVEL until the ON LED turns **blue**.

**MIDI channel:** default **Channel 1**. To change: hold BOTH footswitches at power-up, turn DRIVE — LED GREEN=ch1, AMBER=ch2, RED=ch3, BLUE=ch4-16 (set by receiving a PC on the desired channel).

**MIDI output mode (THRU chaining):** at the dual-footswitch power-up screen, turn LEVEL — GREEN="ON" (generates MIDI), AMBER="THROUGH" (relays incoming — lets you daisy-chain Iridium in a MIDI string), RED="OFF" (default).

**300 presets / 3 banks (the bank trap):**
- MIDI BANK 0 = presets 0–127
- MIDI BANK 1 = presets 128–255
- MIDI BANK 2 = presets 256–299

Within the first 127 presets a plain **Program Change** recalls them. For banks 1/2 you MUST send a **Bank Change (CC#0 = bank number)** BEFORE each Program Change, or it stays in bank 0. Powers up in BANK 0 every time.

**Save a preset:** hold FAV until LED blinks blue, then send the PC for the target slot.

**CC map** (this FAQ omits it; full map is in the manual / dossier §8): Amp=CC19, Cab=CC20, Room Size=CC18, Drive=CC13, Level=CC12, Bass/Mid/Treble=CC14/15/16, Amp Disable=CC21, Bypass=CC102, Expression=CC100, MIDI volume=CC9 (added fw 1.19).

**Rig note:** an H90 or Blooper already on the boards could flip Iridium presets if patched into the EXP/TRS jack via a TRS-MIDI adapter — Iridium is a receive-only-style slave here (or set to THROUGH to pass MIDI onward). The MultiSwitch Plus on the EXP jack gives 3-preset footswitching without any MIDI device.
