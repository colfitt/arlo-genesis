https://forum.morningstar.io/t/uafx-del-verb-midi-implementation/11876
forum.morningstar.io · Morningstar user forum (real users + UAFX rep) · 2025

# Morningstar forum — "UAFX Del-Verb MIDI implementation" (THE practical snapshot gotcha)

The single most important real-world source for building Del-Verb "snapshots." It exposes a quirk no marketing page mentions.

## Confirmed CC numbers
- **CC-14 = Delay Select** (the 3-position delay engine toggle: Tape EP-III / Analog DMM / Precision)
- **CC-15 = Reverb Select** (the 3-position reverb engine toggle: Spring '65 / Plate 140 / Hall 224)
(Full per-knob CC map — time, feedback, mix, color, mod, reverb level, bypass, trails, tap — is in the UAFX Control app and the manual; not enumerated in this thread.)

## THE GOTCHA — WYSIWYG / engine-select wipes your CC values
- Reported by a user, confirmed by a UAFX rep: *"any change in the Delay Select (CC-14) or Reverb Select (CC-15) makes the pedal revert back to the physical positions of the knobs."*
- UAFX's framing: *"reverting to the top panel when switching effect type is expected … the effect select CCs are really remote controlling the switch position."* The pedal is **WYSIWYG** — selecting an engine snaps every knob back to where the **physical knob** is pointing.
- CONSEQUENCE for snapshots: if you send Delay/Reverb Select in the MIDDLE of your CC stack, it **wipes** every parameter CC you already sent. So a working snapshot MUST send **CC-14 and CC-15 FIRST**, then all the parameter CCs (time/feedback/mix/color/mod/reverb level) AFTER.

## Timing requirements (real, from the thread)
- Initial guess 20 ms between messages was unreliable.
- **~50 ms between every CC message** is the practical working spacing.
- Some CCs need an even longer gap before the next message lands reliably.
- On a Morningstar this means inserting message delays / using the per-message delay field so the stack doesn't fire too fast.

## How users build a "preset"
- No Program Change recall on Del-Verb (no onboard presets). You build a snapshot as a **single Morningstar button that sends a sequenced stack of CCs**: engine-selects first, then each parameter, with ~50 ms spacing.
- This is the literal mechanic behind UA's "CC snapshots" marketing.

TAKEAWAY: gigging the Del-Verb preset-like is doable but fiddly — order-sensitive (selects first), timing-sensitive (~50 ms gaps), and you must keep the physical knobs in a sane "home" position because engine-select snaps to them. A clean approach: park the physical knobs at a neutral baseline, let the CC stack do the work, and never touch Delay/Reverb Select mid-snapshot.
