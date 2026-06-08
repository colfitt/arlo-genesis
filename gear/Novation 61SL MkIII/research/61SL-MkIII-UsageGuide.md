# Novation 61SL MkIII — Usage Guide

How to *actually* get the most out of the 61SL MkIII in this rig, to complement the spec/reference dossier in `61SL-MkIII-DeepResearch.md`. It is the rig's **central nervous system** — it makes no sound and lives **off-board**, above all three pedalboards on the MIDI/clock/CV plane, and its whole job is to **play, sequence, clock, and CV-bridge** everything else from one keybed. Two truths govern daily use: **you live in one of two worlds at a time** — standalone (sequencer + Sessions, the DAW-less brain) *or* InControl (DAW surface) — and switching mid-song is the box's one real friction; and **templates are built on a computer in Novation Components, not on the hardware**, so the controller side is a "set it up once, recall by Session" instrument, not a menu-dive one.

> Captured this wave (second pass, 4 agents — the rig-central centerpiece treatment): **8 video transcripts + 41 distilled links = 49 artifacts** (see §12). All video attributions verified via `yt-dlp --print channel`. One dossier correction folded in (pitch-bend→CV is a **firmware 1.4** addition, not original spec — §6 patched). Coverage honesty: a 2018 controller whose lore is **front-loaded to 2018–2020** and concentrated on Elektronauts / Gearspace / MOD WIGGLER / Novation's KB; Reddit and lines/llllllll returned almost nothing, and development effectively stopped at firmware 1.4. **No famous-artist endorsement exists** — normal for the category.

---

## 1. Essential workflows

**Pick your world first.** The sequencer/Sessions world and the **InControl** DAW world are a hard mode toggle (**Shift + InControl**), and reviewers consistently flag the clunk — "remember to stick to one transport." Decide per song: is the SL *running the room* (standalone clock master + 8-track sequencer) or *serving the DAW* (InControl)? ([transcripts/loopop-deep-dive.md](transcripts/loopop-deep-dive.md), [links/brookes-audio-61sl-mkiii-longterm-review.md](links/brookes-audio-61sl-mkiii-longterm-review.md))

**Setup once.** It needs the **12V/1A brick — no USB power, ever**. Learn the universal modifier rule that confuses everyone: **Shift + a mode button ENABLES that mode; the button alone only opens its EDIT menu** (Zones / Sequencer / Scales / Arp all behave this way) ([links/brookes-audio-61sl-mkiii-longterm-review.md](links/brookes-audio-61sl-mkiii-longterm-review.md), [links/forum-hidden-features-power-user-tips.md](links/forum-hidden-features-power-user-tips.md)).

**The three daily jobs** (each detailed below):
- **Master keyboard for soft synths** → standard-MIDI mode or InControl into Logic/Ableton (§5). The velocity-and-aftertouch front end the OP-1 lacks and the weighted S08 isn't built for.
- **DAW-less sequencer/clock brain** → standalone, 8 Parts driving the Elektrons + MPC + MIDI pedals, SL as clock master (§2, §6, §9).
- **MIDI-to-CV bridge** → the only box in the rig that throws pitch/gate/mod CV + analog clock at modular gear (§6).

---

## 2. The 8-track sequencer — core craft

The mechanics, distilled from the V2 manual (all `links/seq-manual-*.md`):

- **Turn it on:** **Shift + Sequencer**. (Sequencer lit orange = viewable/editable but transport-dead; you must enable it to actually run.)
- **Enter notes — Steps view:** hold a step pad + play the keybed (up to **8 notes/step**); press a lit step to see/edit its notes. Per-step via **Options** → encoders: **Velocity 1–127**, **Gate 1–32 steps** (in 6 fractions/step), **Chance** (0% = a muted step), and which **Pattern**. Per-note gate lengths within a chord work — e.g. give step 1 a 16-step gate to ring a held chord across the whole pattern ([links/seq-manual-step-editing.md](links/seq-manual-step-editing.md), [transcripts/novation-deep-dive.md](transcripts/novation-deep-dive.md)).
- **Micro-steps (firmware 1.2):** Steps → Options → pick a step → **6 buttons above the faders** light → hold a micro-step + play a key. Triplet runs, glitch ratchets, off-grid feel ([links/seq-manual-micro-steps.md](links/seq-manual-micro-steps.md)).
- **Pattern view:** **Start/End** (End may precede Start for reverse spans), **Direction** = Forward / Backwards / Ping-Pong / **Random**, **Sync Rate** 1/32T → 1/4 (default 1/16 — a 1/4 rate turns 16 steps into 4 bars), **Pattern Shift 0–15**. **Chains** = press 2+ pattern pads together; **Shift + a pattern pad** = instant audible blend instead of waiting for the boundary ([links/seq-manual-pattern-view.md](links/seq-manual-pattern-view.md)). 8 patterns/Part, each with its own rate/length/direction.
- **Record:** Record + Play = quantised (note-on → Sync Rate); **Shift + Record** = non-quantised to a 1/6 tick; **hold Record** = momentary punch-in. **8 automation lanes per track** (knobs/faders/buttons/pads/wheels/pedals), recorded at 24 PPQN — it's an automation *curve*, **not** Elektron-style p-locks ([links/seq-manual-recording-automation.md](links/seq-manual-recording-automation.md)).
- **Sessions = the save unit:** all 8 Parts × 8 patterns + templates + scales + arp + zones. **64 Sessions**; rename/reorder only in Components. **Mute/Solo** Parts (the yellow/blue soft-button rows) to arrange live; **cued Session switch** (tap a Session pad while playing) jumps a whole arrangement at the next boundary ([links/seq-manual-sessions-parts-model.md](links/seq-manual-sessions-parts-model.md)).

> ⚠️ **Save Lock the Sessions you care about.** Save overwrites in place, and a **Program Change on channel 16 can switch the Session on the SL itself** and lose unsaved work. Enable Save Lock with **Shift + Save while powering on** (Save LED off = locked); it persists through power-off. Keep ch.16 clear of PC traffic ([links/novation-faq-save-lock-sessions.md](links/novation-faq-save-lock-sessions.md)).

---

## 3. Generative / aleatoric recipes (the rig's whole aesthetic)

The SL's "happy accidents" are designed in — and for a drone/doom/shoegaze rig they're the point, not filler. The key insight: **Scales (Snap/Filter) keeps every chaotic note diatonic**, so you can let Random direction + Chance run wild while staying in a chosen drone key. Per-Part independent Sync Rates + per-Part swing make tracks drift out of phase and re-converge. Four copyable setups — full detail in [links/seq-generative-recipes.md](links/seq-generative-recipes.md):

| Recipe | Setup |
|---|---|
| **A — Never-repeating drone bed** | 1 Part, 4–6 long overlapping notes (Gate 8–24), **Direction = Random**, Sync 1/8–1/4, **Chance 40–70%** (varied per step), **Scales On / Snap** (Natural Minor / Dorian / Phrygian). An ever-reshuffling diatonic chord cloud that never resolves the same way. |
| **B — Phasing two-Part drift** (Reich/Eno) | Same notes both Parts; **different Sync Rates** (P1 = 1/16, P2 = 1/16T), **Pattern Shift 3–5** on P2, **swing 58% on P2 only**, Chance ~80%, Snap on both. They phase apart over many bars and re-converge. |
| **C — Glitch/degraded texture** | Percussive source; fill **multiple micro-steps** on 3–4 steps for ratchets at **Chance 30–60%**, **Direction = Ping-Pong**, Sync 1/16–1/32, plus non-quantised hits and one slow filter **automation lane**. |
| **D — Aleatoric arp wall** (firmware 1.4) | Latch a chord on a Part with Arp **Random**, Octaves 3–6, **Chance 60–80%**, Gate 100%; run a 2nd Part's arp on the same chord as **Played, 1/8T, Oct 2**; Scales On. Latch self-sustains hands-free — tweak Chance/Octaves live. |

**Live glue:** Mute/Solo to bring layers in/out, Pattern Chains for sections, **Sequence Transpose from the pads** (firmware 1.4) to shove the whole wall ±11 semitones for swells/drops.

---

## 4. Components templates & the controller side

You **cannot build a template on the hardware** — it's [Novation **Components**](https://components.novationmusic.com) (web needs **Chrome/Edge/Opera** for Web-MIDI; **Firefox does not work**; or the standalone app). This is the SL's biggest day-to-day friction ([links/components-template-editor.md](links/components-template-editor.md), [links/brookes-audio-61sl-mkiii-longterm-review.md](links/brookes-audio-61sl-mkiii-longterm-review.md)).

- **What a template holds:** per control — **type** (CC 0–127 / **NRPN** / Program Change + Bank / Note / MMC / Off), **MIDI channel 1–16**, **Low/High value** (set Low > High to invert), behaviour (toggle/momentary, absolute/relative encoders). Covers 16 rotaries (8 encoders × 2 pages), 16 pads (hit + pressure separately), 8 faders, 16 buttons, mod/pitch wheels, 3 pedals. **64 template slots**, sent over SysEx.
- **The crucial subtlety:** the **physical port (USB / DIN1 / DIN2 / CV) is NOT in the template** — it's a **Part Setting stored per Session**. So one template can drive a DIN pedal in one Session and a USB synth in another ([links/components-template-editor.md](links/components-template-editor.md)).
- **Community template state (honest):** the **factory library includes Octatrack and Digitakt templates** (plus TR-8S, Sub37, OB-6, Prophet 6, BigSky) — directly usable here. There is **no factory template for the VG-800, Chase Bliss, Hologram, H90, or MPC** → build your own. Community sharing is sparse and partly dead-linked (the piedpipers.club archive is **down**; a Facebook group remains) ([links/components-template-sharing.md](links/components-template-sharing.md)).
- **Bulk authoring:** [`libslmkiii`](https://github.com/inno/slmkiii) is a community Python lib converting **JSON ↔ .syx** — ideal for cloning the **seven near-identical Chase Bliss pedal maps** programmatically (generate one, offset CC#/channel per pedal, batch-import) rather than hand-building each in the UI ([links/int-libslmkiii-library.md](links/int-libslmkiii-library.md)).

---

## 5. InControl / HUI — DAW control

InControl is the dedicated DAW mode (host port "**SL MkIII InControl / Port 2**"). Native scripts for **Ableton, Logic, Reason**; **HUI/Mackie** is the fallback for everything else ([links/incontrol-overview-hui.md](links/incontrol-overview-hui.md)).

- **Ableton is the most capable** — clip launch is Ableton-exclusive (pad grid mirrors clip colors), plus device banking, track names, metronome. The clearest tutorial is [transcripts/gammalens-incontrol-ableton.md](transcripts/gammalens-incontrol-ableton.md); setup in [links/incontrol-ableton-setup.md](links/incontrol-ableton-setup.md).
- **Logic** gets device control + Smart Controls + count-in but **no Save and no clip launch**; setup in [links/incontrol-logic-reason-setup.md](links/incontrol-logic-reason-setup.md). (Video coverage of Logic+InControl is thin — Ableton dominates.)
- **Upgrade the stock surface:** **[DrivenByMoss](https://www.mossgrabers.de)** (free) is the community-standard replacement for the weak stock HUI — color-coded knob modes (Track/Vol/Pan/Send), real ⏪/⏩ transport (stock HUI breaks FF/RW in Reaper), faders→track volume. Enable via the **InControl** button, set the 2nd InControl port as primary ([links/forum-drivenbymoss-slmkiii-doc.md](links/forum-drivenbymoss-slmkiii-doc.md), [links/forum-reaper-transport-bug-drivenbymoss.md](links/forum-reaper-transport-bug-drivenbymoss.md)).
- **Limitations:** **Automap is gone** — deep per-plugin auto-mapping the MkII had is "significantly reduced"; use the DAW script's device banking, a standard-MIDI template + plugin MIDI-learn, or DrivenByMoss ([links/gearspace-automap-removed-plugin-control.md](links/gearspace-automap-removed-plugin-control.md)). **Faders aren't motorized/touch-sensitive** so values "jump"; **Fader Pickup is BYPASSED in InControl** (you inherit the DAW's behavior) — Pickup only helps in standalone/Template mode, so turn it **on** for standalone VG-800/pedal control ([links/novation-faq-fader-pickup-incontrol.md](links/novation-faq-fader-pickup-incontrol.md)). **No MPE** for soft synths ([links/forum-loopypro-game-changer-thread.md](links/forum-loopypro-game-changer-thread.md)).

---

## 6. Clock & CV — master clock + MIDI-to-CV bridge

**Clock** ([links/clock-master-slave-setup.md](links/clock-master-slave-setup.md), [links/novation-faq-midi-routing-clock-warning.md](links/novation-faq-midi-routing-clock-warning.md)):
- **MIDI Clock Tx On** → 24 PPQN to **USB + both DINs at once**; Play/Stop/Shift+Play also send Start/Stop/Continue (only when Tx is on). **Rx On** slaves the SL to one input. **Decide ONE master per song; never Tx and Rx at once.**
- **Feed clock on USB *or* DIN, not both** — double-pathing causes sync loss / erratic tempo. This is also the real root cause behind the reported **USB-to-Logic timeouts** (fix order: stop double-clocking → trash Logic's control-surface prefs + reinstall the Novation plugin → fall back to DIN out if USB still flakes) ([links/novation-faq-midi-routing-clock-warning.md](links/novation-faq-midi-routing-clock-warning.md)).
- **Analog Clock Out** is separate: PPQN **1/2/4/8/24**. **Caveat:** only **/1 and /2 stay phase-locked** — /4–/32 drift out of phase over time, so clock the modular at 1 or 2 PPQN and **divide down in the rack**. MIDI-clock jitter is a bounded ~few ms (USB worst) — prefer the analog Clock Out for tight phase-lock, and for the most timing-critical pieces consider slaving the SL to an Elektron ([links/modwiggler-clock-jitter-drift.md](links/modwiggler-clock-jitter-drift.md), [links/forum-vcv-rack-clock-jitter.md](links/forum-vcv-rack-clock-jitter.md)).
- **3 DIN sockets:** In / Out1 / **Out2-Thru** — Out2 Global-switches between a 2nd independent clock-capable Out (two fan-out chains) and pure hardware **Thru** ([links/int-din-routing-destinations.md](links/int-din-routing-destinations.md)).

**CV/Gate/Mod** ([links/cv-gate-mod-calibration.md](links/cv-gate-mod-calibration.md), [links/novation-faq-cv-gate-calibration.md](links/novation-faq-cv-gate-calibration.md), [transcripts/divkid-eurorack-cv.md](transcripts/divkid-eurorack-cv.md)):
- Pitch CV: notes **24–108 → 0–7 V** (1 V/oct), **monophonic last-note** (mono lines/drones, not chords). Gate goes high while a note is held. **Mod out = a CC→voltage**, CC# and range set in Global, switchable **bipolar −5/+5 V or unipolar 0/+5 V**.
- **Calibrate the pitch ports:** Global → CV → set **CV-Low against 220 Hz (A2)** and **CV-High against 880 Hz (A4)** with the Tune knob into a VCO/tuner → Apply. (Also a microtonal trick.)
- **Pitch-bend → CV at ±1..±12 semis** for playable bends — *added in firmware 1.4* (see §11). To use **both Mod outputs from one Part**, set the part's CV mode to "**both**" ([transcripts/bobeats-review.md](transcripts/bobeats-review.md)). Host "To CV/Gate" port: MIDI **ch.1 → CV1, ch.2 → CV2**.
- **Texture trick (DivKid):** gate length *is* modulation — long gates make notes swell/breathe through reverb/delay, short gates "ping"; selectable Clock Out PPQN (e.g. 4) clocks a 16th-note trigger straight off the jack.

---

## 7. Power-user tips & hidden features

- **Arp Latch with Arp OFF = a drone generator** — latch a held chord with the arp disabled and the SL sends a continuous sustained note indefinitely. Sustained walls into the VG-800 or a soft synth, hands-free ([links/forum-hidden-features-power-user-tips.md](links/forum-hidden-features-power-user-tips.md)).
- **Per-Part independent arps (firmware 1.4)** — all 8 Parts can arp at once with different Length/rate + per-arp probability → a polyrhythmic generative engine from one chord ([links/forum-firmware-lore-12-and-14.md](links/forum-firmware-lore-12-and-14.md)).
- **The pads have polyphonic aftertouch** (the keybed strip is channel-AT only) — map pad pressure for expressive per-note control ([links/elektronauts-sl-mkiii-megathread.md](links/elektronauts-sl-mkiii-megathread.md)).
- **Per-template DIN disable** (Templates page) sends a Part to USB/DAW only without blasting a DIN synth ([links/novation-faq-midi-routing-clock-warning.md](links/novation-faq-midi-routing-clock-warning.md)).
- **Sequence Program Changes per step** to automate patch changes on downstream gear; map **poly-AT to faders** for swarm-detune ([transcripts/divkid-eurorack-cv.md](transcripts/divkid-eurorack-cv.md)).
- **Fine control:** **Shift + Play** = start from current position + MIDI Continue; **Grid** toggles the pads between Sequencer subview and Template ([links/forum-hidden-features-power-user-tips.md](links/forum-hidden-features-power-user-tips.md)).

---

## 8. Notable users (honest)

Controllers don't accrue signature-artist mythology, and the SL MkIII is no exception — **no headline artist claims it as a defining instrument** (normal for the category; treat the absence as expected, not a knock). The useful "users" here are the **technique creators** whose workflows transfer:
- **Ron Cavagnaro** — the deepest *technique* channel for this box: 1/4-sync-rate song-sketching, chord-memory, sequencing a synth **through the Hologram Microcosm** (rig-relevant) ([transcripts/roncavagnaro-basic-sequencing.md](transcripts/roncavagnaro-basic-sequencing.md)).
- **DivKid** — the CV/modular reference ([transcripts/divkid-eurorack-cv.md](transcripts/divkid-eurorack-cv.md)).
- **GammaLensMedia** — the only modern (2023–24) structured tutorial series ([transcripts/gammalens-sequencing-basics.md](transcripts/gammalens-sequencing-basics.md)).
*(Unverified: any specific artist attribution — none found in research.)*

---

## 9. Rig-specific recipes & pairings

- **Play / configure the Boss VG-800** — full recipe in [links/int-recipe-vg800.md](links/int-recipe-vg800.md). The VG-800 has **TRS MIDI** (not full DIN): link **SL DIN Out → VG-800 MIDI IN via a BMIDI-5-35 TRS↔DIN cable**. VG side: **RX CHANNEL** = a chosen channel (e.g. Ch4, matched to the SL Part), **RX PC MAP = FIX** (so PC recalls VG memories), **SYNC CLOCK = MIDI/MIDI-AUTO** (follow the SL's tempo). The VG's **CONTROL ASSIGN** has **16 slots** mapping incoming **CC#1–31 / CC#64–95 → any VG parameter** with MIN/MAX — so in Components you pick CC#s in those windows, and on the VG you point the assigns at the same CC#s. The keybed then auditions the VG's GR-300/organ/acoustic models **without picking up the banjo/baritone**. *(Don't conflate directions: the VG's GUITAR-TO-MIDI is the opposite path — VG feeding the SL/Elektrons.)*
- **Sequence the Elektron rig + MPC** — [links/int-recipe-elektrons-mpc.md](links/int-recipe-elektrons-mpc.md): Part 1 → Digitakt (Ch1), Part 2 → Octatrack (Ch2), Part 3 → MPC (Ch3), each its own destination; **load the factory Octatrack/Digitakt Components templates**; run the SL as **Clock Tx master**. Decide who sequences whom per song to avoid double-sequencing chaos. *(Note: the Digitakt does **not** pass pitch-bend or mod-wheel through, and Elektron sequencers cap at 4 notes/step — route expressive Parts out the SL's 2nd DIN directly, not through the Digitakt ([links/elektronauts-digitakt-sl-mk3-workflow.md](links/elektronauts-digitakt-sl-mk3-workflow.md)).)*
- **Control the MIDI pedalboard (CB stack / Hologram / H90)** — [links/int-recipe-cb-stack-pedals.md](links/int-recipe-cb-stack-pedals.md): one Part/template per pedal (clone-and-re-channel the near-identical CB maps via libslmkiii), clock-sync via Tx, Template buttons send PC to recall presets — and a **Session becomes whole-pedalboard recall**.
- **MIDI-to-CV bridge for modular / soft-synth master** — [links/int-recipe-modular-softsynth.md](links/int-recipe-modular-softsynth.md): calibrated CV mono voice + a Mod-CC for filter/VCA + Clock Out to the rack; soft-synth master via USB standard-MIDI or InControl, with **Zones** for splits/layers (bass low, pad up top from one keybed).
- **The keyboard the OP-1 lacks** — when a part needs a real velocity-and-aftertouch keybed, this is it; audio stays on the **Apollo x8 / Babyface Pro FS**, the SL rides USB/MIDI + clock alongside.

---

## 10. Best learning resources

- **loopop** — [the canonical deep-dive](transcripts/loopop-deep-dive.md): the three-pillars concept + honest launch-era pros/cons.
- **Novation (official)** — [the 48-min Deep Dive](transcripts/novation-deep-dive.md) (the single best end-to-end reference, demoed on Peak/SP-404/Octatrack/0-Coast) and [the Components masterclass](transcripts/novation-components-masterclass.md) (the exact template-building process — your VG-800/CB map blueprint).
- **DivKid** — [the CV/Eurorack reference](transcripts/divkid-eurorack-cv.md). **BoBeats** — [Circuit-lineage workflow + dual-Mod CV](transcripts/bobeats-review.md).
- **GammaLensMedia** — the only modern structured series: [sequencing basics](transcripts/gammalens-sequencing-basics.md) + [InControl with Ableton](transcripts/gammalens-incontrol-ableton.md). **Ron Cavagnaro** — [deepest technique channel](transcripts/roncavagnaro-basic-sequencing.md).
- **Written:** the **Elektronauts megathread** ([links/elektronauts-sl-mkiii-megathread.md](links/elektronauts-sl-mkiii-megathread.md)) is the richest community source; the **Brookes Audio long-term review** ([links/brookes-audio-61sl-mkiii-longterm-review.md](links/brookes-audio-61sl-mkiii-longterm-review.md)) is the most useful owner write-up; **DrivenByMoss** docs ([links/forum-drivenbymoss-slmkiii-doc.md](links/forum-drivenbymoss-slmkiii-doc.md)) for the DAW-surface upgrade.

---

## 11. Common pitfalls / gotchas

- **Mode-switch clunk** — standalone ↔ InControl is a hard toggle; pick one transport per song ([links/elektronauts-sl-mkiii-megathread.md](links/elektronauts-sl-mkiii-megathread.md)).
- **Save Lock or lose work** — Save overwrites in place; a PC on **ch.16** can swap the Session on the SL itself. Lock the ones you care about (**Shift+Save while powering on**) ([links/novation-faq-save-lock-sessions.md](links/novation-faq-save-lock-sessions.md)).
- **Don't double-path clock** (USB *and* DIN) — sync loss / erratic tempo, and the likely cause of the USB-Logic timeouts. DIN-out is the fallback ([links/novation-faq-midi-routing-clock-warning.md](links/novation-faq-midi-routing-clock-warning.md)).
- **Analog Clock Out drifts above /2** — only /1 and /2 stay phase-locked; divide down in the modular ([links/modwiggler-clock-jitter-drift.md](links/modwiggler-clock-jitter-drift.md)).
- **Templates need a computer** (Components) — no on-hardware editing; **use Chrome/Edge, not Firefox** ([links/components-template-editor.md](links/components-template-editor.md)).
- **Automap is gone** and **fader moves jump** (Pickup bypassed in InControl) ([links/gearspace-automap-removed-plugin-control.md](links/gearspace-automap-removed-plugin-control.md), [links/novation-faq-fader-pickup-incontrol.md](links/novation-faq-fader-pickup-incontrol.md)).
- **Automation doesn't copy between tracks** (notes do); **gate is MIDI note-length only** (won't stretch a short sample); **CV collapses poly to last-note mono** ([links/seq-manual-recording-automation.md](links/seq-manual-recording-automation.md), [links/seq-manual-transport-clock-tempo.md](links/seq-manual-transport-clock-tempo.md)).
- **Shift enables, button alone edits** — the single most common point of confusion ([links/brookes-audio-61sl-mkiii-longterm-review.md](links/brookes-audio-61sl-mkiii-longterm-review.md)).
- **No USB power** — always the 12V brick; **no MPE**; aftertouch is uneven white-vs-black key (channel-pressure strip) ([links/kvr-sl-mk3-the-itch.md](links/kvr-sl-mk3-the-itch.md)).

---

## 12. Captured sources

**Transcripts** (`research/transcripts/`, 8):
- `loopop-deep-dive.md` — the canonical orientation (three pillars + honest cons).
- `novation-deep-dive.md` — official 48-min end-to-end reference (sequencer, CV cal, zones, scales, arp, InControl).
- `divkid-eurorack-cv.md` — CV/modular reference (pitch/gate/mod, clock-out PPQN, gate-as-modulation).
- `novation-components-masterclass.md` — definitive template-building (CC/NRPN/PC/poly-AT).
- `bobeats-review.md` — Circuit-lineage workflow + dual-Mod CV ("both" setting).
- `gammalens-incontrol-ableton.md` — clearest InControl-with-Ableton tutorial.
- `gammalens-sequencing-basics.md` — beginner-friendly multi-part sequencer build.
- `roncavagnaro-basic-sequencing.md` — technique + generative; sequences through the Microcosm.

**Links** (`research/links/`, 41) — grouped:
- **Sequencer (manual-derived, `seq-*`):** sessions-parts-model · step-editing · micro-steps · pattern-view · recording-automation · arpeggiator · scales · zones · transport-clock-tempo · firmware-1.4-features · musicradar-hardware-brain-workflow · generative-recipes.
- **Integration (`int-*`, `components-*`, `incontrol-*`, `clock-*`, `cv-*`):** components-template-editor · components-template-sharing · int-libslmkiii-library · incontrol-overview-hui · incontrol-ableton-setup · incontrol-logic-reason-setup · clock-master-slave-setup · int-din-routing-destinations · cv-gate-mod-calibration · int-recipe-vg800 · int-recipe-elektrons-mpc · int-recipe-cb-stack-pedals · int-recipe-modular-softsynth.
- **Community / reviews / firmware (`forum-*`, `elektronauts-*`, `gearspace-*`, `kvr-*`, `brookes-*`, `modwiggler-*`, `novation-faq-*`):** elektronauts-sl-mkiii-megathread · elektronauts-digitakt-sl-mk3-workflow · kvr-sl-mk3-the-itch · brookes-audio-61sl-mkiii-longterm-review · gearspace-automap-removed-plugin-control · modwiggler-clock-jitter-drift · forum-vcv-rack-clock-jitter · forum-firmware-lore-12-and-14 · forum-reaper-transport-bug-drivenbymoss · forum-drivenbymoss-slmkiii-doc · forum-hidden-features-power-user-tips · forum-loopypro-game-changer-thread · novation-faq-cv-gate-calibration · novation-faq-save-lock-sessions · novation-faq-fader-pickup-incontrol · novation-faq-midi-routing-clock-warning.

## Sources

All claims above cite a captured file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`61SL-MkIII-DeepResearch.md`](61SL-MkIII-DeepResearch.md); the manual is in `manuals/` (SL MkIII User Guide V2).

> **Honest coverage notes:** strong-for-its-age coverage, but **front-loaded to 2018–2020** and concentrated on Elektronauts / Gearspace / MOD WIGGLER / Novation's KB — **Reddit and lines/llllllll returned almost nothing**, and development effectively stopped at firmware 1.4 (2020). Gearspace/MOD WIGGLER/Novation KB pages **403 automated fetch** (distilled from quoted snippets + reachable mirrors); the **V2 manual is the authoritative source** for sequencer mechanics and fully corroborates the dossier's spec claims. Genuinely thin areas: **deep CV-to-modular tutorials beyond DivKid's single overview**, **Logic-Pro InControl video**, and **no dedicated video** for using the SL as clock master over the Elektron/MPC ecosystem (that lives in the manual + forums). The **community Components-template ecosystem is sparse and partly dead-linked** — build-your-own (Components or libslmkiii) is the realistic path for this rig's boutique pedals. **One dossier correction:** pitch-bend→CV is a **firmware 1.4** addition, not original spec (§6 patched). **No verified famous user exists** — normal for a controller.
