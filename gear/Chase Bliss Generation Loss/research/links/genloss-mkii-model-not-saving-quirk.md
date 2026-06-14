https://forum.morningstar.io/t/generation-loss-mkii-model-not-saving/7953
forum.morningstar.io · user support thread (Gen Loss MkII + Morningstar MC6 + CB MIDIbox) · fetched 2026-06-14

# Gen Loss MkII MIDI preset gotcha — the MODEL knob can fail to recall on power-up

**Directly relevant to this rig** (the End Board recalls Gen Loss via Program
Change in a one-PC whole-stack scene). A user reports: after powering up the
board and sending a **PC message in MkII mode**, the Gen Loss MkII recalls
**everything about the preset EXCEPT the Model** — the Model parameter reverts to
a "no model" / OFF state. Reproduced across **multiple replacement units and
different MIDI controllers**; the user's other CB pedals (Thermae, MOOD MkII)
recall their presets fine, so it's Gen-Loss-Model-specific, not a board fault.

- Setup in the report: ChaseBliss MIDIbox + Morningstar MC6 sending PC on power-up.
- Symptom: preset's knobs/toggles recall correctly; **Model resets to 0/OFF** (no EQ color).
- The thread is an **open support request — no confirmed CC fix or workaround posted** at fetch time.

## Why it matters for THIS rig (practical takeaway)
Because the whole stack recalls on one PC, a silently-dropped Model = your Gen
Loss tape character loses its EQ-color voice (Model 0 = no model = unfiltered)
without you noticing on stage. Practical mitigations until CB/firmware resolves it:
- **Verify the Model after a power-up scene recall** before relying on it live.
- If a PC-recalled Model keeps dropping, **set the Model explicitly via a CC**
  in the same scene right after the PC (Gen Loss exposes its knobs over CC per
  the MIDI manual) — i.e. don't trust PC alone to restore Model.
- Or store the wanted Model into the **2 onboard preset slots at the pedal** and
  recall those, rather than leaning only on external PC state.

## NOT a patch — captured as a recall reliability gotcha.
No new knob *values* here; this is a MIDI-recall caveat that affects how reliably
any saved Gen Loss patch reappears in the cb-stack scene.

## Sources
- https://forum.morningstar.io/t/generation-loss-mkii-model-not-saving/7953 (the report; multi-unit, multi-controller, unresolved)
- (cross-ref on-disk: cb-stack-preset-scene-recall + Gen Loss MIDI = PC/CC only, NO clock, 2 onboard presets)
