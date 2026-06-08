https://www.youtube.com/watch?v=tIY4F3b0zDA
Marcus Curtis Music · The BOSS VG-800 Setup and Demo · 2025-03-17

(Auto-captions cleaned to prose. Marcus Curtis runs a long-running guitar-synth series and owns the GM-800 and SY-1000 too, so this is a knowledgeable setup/firmware/compatibility walkthrough followed by a factory-patch tour. ~35 min.)

## GK-5 pickup mounting
The GK-5 is NOT included with the VG-800 — buy it separately (~$250). Mounting options:
- **Double-sided tape** — stick it anywhere under the strings (his preference; no drilling).
- **Drill/screw** — permanent.
- **Tail-piece mounting plate** — for this guitar there's a plate that hooks in behind the tailpiece (remove the tailpiece, the plate pops on/off). He prefers this for more stability than tape; the whole thing removes with no damage to the guitar.
- He taped the GK cable down in one corner to stop it flopping around.
- **Critical clearance:** you need ~**1 mm of height between the strings and the pickup** when mounting. (He links a separate dedicated GK-5 mounting video.)

## Power and auto-off
The VG-800 has **no power switch** — the DC-IN jack is the switch (plug = on). He powers it from a Furman power strip and uses the strip as the on/off. On first boot it warns it will auto-off after **20 minutes** of no use. He turns auto-off OFF (MENU → the auto-off page; options are 20 min / 1 hr / 5 hr / 10 hr / OFF, each assigned to a knob; "disabling auto-off increases power consumption" → OK). For studio use, set it OFF.

## Firmware update procedure (step by step)
1. **Check installed firmware:** power off, **hold [EXIT]** while powering on. His unit shipped with **v1.01 (build 0102)**. Compare to boss.info.
2. **Download** from boss.info → VG-800 → Explore → Downloads: firmware **v1.02**, the **USB driver** (Windows or Mac), and **BOSS Tone Studio** (Windows or Mac). Under Support you also get all the owner's manuals as PDFs (Quick Start, Reference Manual, Parameter Guide) — right-click → open in new tab → agree → download.
3. **Connect** USB-C (unit) to USB-A/USB 2.0 (computer) with a fairly long cable.
4. **Enter update mode:** hold **[MENU]** while powering on → screen shows "VG-800 UPDATOR / copy file and disconnect USB cable." The unit mounts as a USB drive.
5. On the computer, **extract** the downloaded v1.02 archive, copy the firmware (the VG-800 "system" file) onto the mounted VG-800 drive.
6. **Eject** the VG-800 drive, **unplug** USB. The unit walks step 1→2→3→4 → "**update succeeded**." Power-cycle (off then on at the strip); it boots back to GUITAR MODE / first preset.
7. **Install the driver, then install BOSS Tone Studio** (don't launch yet → finish). Reconnect the unit; verify it appears in Device Manager as "VG-800." Launch Tone Studio → select VG-800 → OK → you're in the editor.

## Pickup compatibility (GK-5 vs older GK-3 / GK-2A / 13-pin)
- The native pickup is the **GK-5** over Serial GK (the TRS cable).
- You CAN use older **GK-3 / GK-2A** (or a Godin-style built-in 13-pin) — but you need the **conversion box** (~$199) that converts the 13-pin connector to the Serial-GK TRS cable.
- His verdict on the pickups: "I don't really see a lot of difference with the pickups, they all work great — there's really no latency." He notes the **GM-800 had GK-5 tracking problems early on that firmware updates mostly ironed out**, but says **the VG-800 doesn't have any of those issues at all — it doesn't matter which pickup system you use, any of them works really well.** (This is a useful corroboration that VG-800 tracking is solid out of the box, more so than the GM-800 was.)

## Chaining with the GM-800 (Serial GK out)
The VG-800 and GM-800 are designed to work together, chained **in series** via a **BOSS TRS Serial-GK cable** (he has 3 ft / 15 ft / 30 ft; ordinary TRS worked on the GM-800 but he uses the Boss ones). Either order works: GK pickup → GM-800 in → GM-800 out → VG-800 in, OR GK → VG-800 → GM-800. He says he doesn't know which order is "proper" and plans to test both. Note the new ecosystem is more expensive than the old all-in-one Roland units — VG-800 (~$650) + GM-800 (~$750) + a control footswitch and expression pedal for each + cables ≈ ~$1,900–1,950 for the full rig, because hardware that used to be built in (controls, expression) is now bought separately per unit.

## Lineage framing
He frames the VG-800 as the "modeling/amp" half and the GM-800 as the "synth" half of what the GR-55 used to be in one box — the GM-800's synth is a big improvement over the GR-55 (more/better tones, better layering), the VG-800 has the newer **AIRD** amps (vs the GR-55's COSM) and upgraded effects.

## Factory-patch tour (ships with ~60 patches; more via BOSS Tone Exchange)
He stresses patches are "fairly simple to program yourself." Highlights of factory patches he plays:
- **"Ultimate split"** (the first preset) — DUAL GUITAR: a clean guitar on the high strings + distortion on the low strings, two different guitars at once.
- **Wide 12-string** — stereo 12-string, "really sounds pretty good" (from a 12-string owner).
- **Sitar** in **DADGAD** / a sitar tuning for DAD-CAD — per-patch ALT TUNING means you set the tuning when you build the patch.
- **Fretless guitar** — "Boss does pretty good fretless, great for funk."
- A **metal tone built on an ACOUSTIC guitar model** — surprisingly heavy.
- An **OPEN G** distorted patch.
- **GR-300** synth — "on everything Boss puts out."
- Acoustic, mild jazz, "City Pop," blues (blues amp + blues guitars).
- **"Cristo Echo"** — a synth tone he really likes for interesting textures.
- Fretless bass, standup bass (lots of basses).
- A **Gibson acoustic blended with a Gibson ES-335** (you can hear the acoustic "tinty" component layered in).
- **"Breeze solo"** — synthy lead; he notes each patch has a **CTL (control footswitch) function** that toggles an effect — on this one he prefers it OFF.
- Stereo Telecaster clean (neck pickup), nylon string ("one of the real tests — how well did they nail nylon" — "not bad"), an organ ("Shiny Phase Clean").

He closes promising follow-up videos on recording with it, blending it with other synths, hidden features, and using it as a **MIDI controller**.
