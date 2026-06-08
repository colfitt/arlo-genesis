https://modwiggler.com/forum/viewtopic.php?t=249422
modwiggler.com · "Analogue clock driving SL MKiii sequencer - dropping out of phase" + related SL MkIII MIDI-CV thread (t=207935) · 2019–2021
(threads 403 WebFetch — distilled from search-engine snippets quoting the posts; also djjondent.blogspot.com modular-clock reference and the VCV thread below)

THE clock/timing file for this rig. The SL is the intended clock master + MIDI-to-CV bridge, so this is load-bearing.

## SL is locked to 24 PPQN over MIDI (no choice)
- MIDI clock leaves the SL at **24 PPQN** on USB and BOTH DIN ports. The SL **only recognizes incoming external MIDI clock at 24 PPQN** — feed it 8 PPQN (or anything else) as a slave and it won't lock at all. Effectively fixed at 24 PPQN for MIDI in both directions.

## Analogue Clock Out divisions DRIFT (the real gotcha)
- The 3.5 mm analog **Clock Out** is selectable **1 / 2 (default) / 4 / 8 / 24 PPQN**.
- Multiple wigglers report: **only /1 and /2 stay phase-locked.** Divisions of **/4, /8, /16, /32 are prone to losing phase and drifting** against the master over time. (Original symptom: an external analog clock driving the SL's sequencer "dropping out of phase.")
- **Rig takeaway:** when clocking analog/modular gear off the SL's Clock Out, set the destination to accept **1 or 2 PPQN** and divide DOWN in the modular if you need slower pulses — do NOT rely on the SL's higher Clock-Out divisions to stay tight over a long take. For doom/drone long-form pieces this matters; phase drift on a sustained wall is audible.

## MIDI-clock jitter is real but bounded (USB especially)
- VCV Rack tester (juozasgaigalas): syncing VCV to the SL Mk3 was "jittery, drifty and laggy" — sometimes in sync, sometimes not.
- Responder Soxsa: persistent jitter "of a few ms whatever method I try" — acknowledged as inherent USB/MIDI timing slop, not unique to the SL.
- Mitigations that helped in-thread: let **hardware drive Start/Stop** (transport resets re-align phase); a third user suggested the **3.5 mm analog Clock Out is tighter than MIDI out** for the gear that can take it.
- Counterpoint: other owners call the MIDI-CV clock "rock solid" for simpler chains (Digitakt receiving clock, a couple of sequences running) — drift mostly bites with clock divisions and long unattended runs.

## Practical rig guidance
- For the **Digitakt / Octatrack / MPC** chain: SL as MIDI clock master at 24 PPQN over DIN is fine for normal song lengths; if you ever hear drift, hand clock-master duty to an Elektron and slave the SL (it'll lock at 24 PPQN).
- Send clock to **USB OR DIN, not both** to the same device path (Novation's own warning — double clock causes "loss of synchronisation or erratic tempo"). See the MIDI-routing file.
- For analog sync, prefer **Clock Out at 1 or 2 PPQN**; avoid /4–/32 for anything that must stay locked over minutes.
