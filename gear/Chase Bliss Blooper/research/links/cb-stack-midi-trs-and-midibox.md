https://www.chasebliss.com/shoputility/p/midibox
chasebliss.com · Chase Bliss (product page) · accessed 2026-06-03

# CB-stack MIDI: TRS-MIDI standard, the MIDIBox, daisy-chaining

Reusable across all 7 Chase Bliss pedals in the rig. The Chase Bliss MIDI convention is *remarkably consistent* — verified against the MOOD MkII, Lost + Found, Onward, and Big Time MIDI manuals (all in this repo / fetched from chasebliss.com). One pedal is the exception (Big Time, see below).

## 1. The TRS-MIDI standard CB uses

- **Connector on the pedal:** a single 1/4" (¼") **TRS jack** that doubles as the TAP / MIDI input. (Same jack handles an external momentary footswitch on most pedals.)
- **TRS standard = "ring-active."** Chase Bliss carries the MIDI data signal on the **RING** of the TRS jack (not the tip). Quoted from the MIDIBox page: *"the jumpers on this product are **'ring active'** (instead of 'tip active') on the TRS jack so that they interface to the Chase Bliss tap / MIDI jack with a common TRS patch cable."*
  - In the MIDI-DIN-to-TRS naming scheme this corresponds to **MIDI TRS Type B** (Type A = tip-active = MIDI standard / Korg / Make Noise; Type B = ring-active = older Chase Bliss / Empress). ⚠️ FLAG: the chasebliss.com page says "ring active" explicitly but does **not** print the literal words "Type A" or "Type B." The mapping ring-active → Type B is the standard industry definition (MMA RP-054), applied here — verified by the ring-active quote, *inferred* on the A/B label. Use a **CB/Empress-compatible TRS cable** or the CB MIDIBox and you don't need to think about A/B.
- **Cable:** *"For Chase Bliss devices, use a TRS / stereo cable."* A standard stereo ¼" patch cable works pedal-to-MIDIBox.

## 2. The Chase Bliss MIDIBox (5-pin DIN → TRS converter)

This is the rig's DIN→TRS bridge. The Digitakt 2 outputs 5-pin DIN MIDI; the MIDIBox converts it to the ring-active TRS the CB pedals want.

- **Function:** *"converts the standard 5-pin MIDI cable to a simple TRS patch cable."* Its internal circuitry *"accepts MIDI, splits it to each Control Port, and passes data through to other MIDI devices in your chain."*
- **Capacity:** **one MIDIBox controls up to FOUR Chase Bliss pedals simultaneously** (four ¼" TRS output ports). (Perfect Circuit / retailer spec; corroborated by the multi-port design on the box.)
- **Universal jumpers:** *"Internal jumpers make any port you want compatible with Chase Bliss, Empress, or Meris products"* — so the same box can also feed Empress/Meris gear if their TRS type differs.
- **Power:** the MIDIBox **requires its own 9V DC center-negative power** (~10 mA; "a supply with higher amperage is acceptable"). ⚠️ The #1 documented gotcha: *"It's easy to forget to power the MIDIBox, but it does need it."* The Blooper MIDI quick-start lists "power: The MIDIbox requires power. Easy to forget" as the first troubleshooting item.
- **Pass-through:** the MIDIBox has MIDI in + passes data through, so you can chain it anywhere and continue MIDI to other devices.

### Setup recipe (verified, from Blooper MIDI quick-start)
1. Power the MIDIBox.
2. Digitakt 2 DIN **MIDI OUT** → MIDIBox **input** (5-pin).
3. **TRS cable from any MIDIBox ¼" output → the CB pedal's MIDI/TAP jack.** Repeat for up to 4 pedals.
4. The pedal is now listening. *"As long as you're on the right channel, [the pedal] is always looking for MIDI signals. Once you plug in the cable it's basically ready to go."*

Since the rig has 7 CB pedals (well, 6 TRS + 1 DIN — see Big Time), **two MIDIBoxes** cover the TRS pedals (4 + 2), or one MIDIBox plus a multi-output DIN→TRS hub. Each MIDIBox needs power.

## 3. The Big Time exception — native 5-pin DIN, NO MIDIBox needed

⚠️ IMPORTANT CORRECTION to the prior rig clock-sync table (which listed Big Time as "TRS (MIDIBox)"). The current **Big Time (CBA+EAE ref 2026 – BT001)** is a larger-format pedal that **receives MIDI through a standard 5-pin DIN cable**, verified in two places:
- Big Time MIDI Manual p.1: *"Big Time receives MIDI through a standard 5-pin DIN cable."*
- Big Time base manual I/O diagram: labels the jack **"5-PIN DIN"** (plus a separate AUX jack). Spec sheet shows it's a different platform (400 mA nominal, 1A startup, 32-bit/48 kHz).
- So: **Digitakt DIN MIDI OUT → Big Time MIDI IN directly, no MIDIBox.**
- Big Time also has **MIDI THRU vs OUT** (CC110): it can pass MIDI through (THRU=0) or output its own clock (OUT, see clock file). This makes Big Time a convenient DIN hub or even the stack's clock master.

## 4. MIDI channels per pedal (the key to scenes)

- **Every CB pedal ships on MIDI channel 2 by default.** (Verified verbatim in MOOD MkII, Lost + Found, Onward, Big Time manuals; Blooper too.)
- **Changing channel (same procedure across the stack):** *"hold down both stomp/foot switches when you power up the pedal. The pedal is now looking for the first 'Program Change' [PC or CC on newer pedals] message it sees, and it will set itself to that channel."*
  - Blooper variant: holding both footswitches at power-up puts Blooper in **auto-detect** — *"if blooper detects incoming MIDI, it will automatically change to that channel (and stay that way even after being turned off)."*
- **To address pedals individually**, assign each a distinct channel (power-up + send a PC on the target channel). To address several at once for a "scene," put them on a **shared channel** (e.g. all on ch.2) and send one PC — every pedal on that channel recalls its same-numbered preset.

## 5. Daisy-chaining multiple CB pedals (concrete)

Three workable topologies for this rig:
- **Star from one MIDIBox:** Digitakt DIN → MIDIBox → 4 separate TRS runs to 4 CB pedals. Cleanest; up to 4 per box. (Morningstar forum users confirm running multiple CB pedals off one box; *"need to set to Ring active on the jumpers"* if using a generic/Morningstar box.)
- **Two MIDIBoxes** (or a MIDIBox + its pass-through) for >4 TRS pedals.
- **DIN hub via Big Time:** Digitakt → Big Time MIDI IN (DIN), Big Time THRU → next DIN device; MIDIBox(es) for the TRS CB pedals branch off the DIN chain.

⚠️ FLAG: CB doesn't publish an official "max number of MIDIBoxes you can chain." The 4-pedals-per-box figure is from retailer specs + the box's physical 4-port design and is reliable; the rest are standard MIDI-chaining practice.

## Sources
- https://www.chasebliss.com/shoputility/p/midibox (ring-active TRS, universal jumpers, power)
- https://www.perfectcircuit.com/chase-bliss-midibox-pedal-interface.html (controls up to 4 CB pedals)
- https://forum.morningstar.io/t/midi-box-and-cba-pedals/5702 (ring-active jumper requirement, multi-pedal)
- https://blooper.chasebliss.com/midi/docs/midi-quick-start.pdf (connection recipe, "MIDIbox requires power")
- Local manuals: MOOD MkII MIDI Manual, Lost + Found MIDI Manual, Onward MIDI Manual, Big Time MIDI Manual (all in repo Gear/Chase Bliss */manuals/ or fetched from chasebliss.com) — channel-2 default + channel-set procedure are verbatim in each.
- Big Time MIDI Manual (CBA+EAE 2026 BT001) + Big Time base manual I/O page: 5-pin DIN, MIDI THRU/OUT.
