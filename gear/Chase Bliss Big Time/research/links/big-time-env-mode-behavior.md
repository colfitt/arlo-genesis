https://www.chasebliss.com/s/Big-Time_Manual_Chase-Bliss.pdf
Chase Bliss Big Time manual (pp.32–33, MOTION / Env) + SonicState Superbooth John Snyder interview · accessed 2026-06-19

# Big Time ENV mode — how it actually behaves (sensitivity, SCALE, polarity, STATE)

Consolidated, first-party-verified account of Big Time's envelope (ENV) modulation, written to settle the recurring confusions in the patch notes: ENV is **not** a continuous attack-proportional dive-bomb, and its pitch direction is **not** fixed. All quotes below are verbatim from the owned manual (byte-identical to the official Squarespace-hosted PDF, MD5 247793f3…).

## 1. Sensitivity is set by COLOR + FEEDBACK — because the follower hears its own echoes

The envelope follower tracks **both** the input signal **and** the delay line, so the gain structure that feeds the delay (COLOR) and the recirculation amount (FEEDBACK) directly change how hair-trigger ENV is.

> "The envelope detection follows both the input and delay line. Turning up COLOR and/or FEEDBACK will make the envelope more sensitive, because the envelope also responds to your echoes." — manual p.33

So COLOR and FEEDBACK — not just DEPTH — govern how sensitive and self-feeding the ENV motion is. DEPTH and RATE remain the *labelled* Env alt-controls; COLOR/FEEDBACK are sensitivity levers as a **consequence** of the follower hearing the feedback loop, not as dedicated knobs. Practical read: a hot COLOR/FEEDBACK setting makes ENV re-trigger off the echoes themselves (it can self-feed), where a clean low-FEEDBACK setting only moves on your actual played transients.

## 2. SCALE-on = quantized step sequencing; SCALE-off = un-quantized bends — the split is *quantization*, not continuous-vs-triggered

The SCALE-on/off structural mapping is verbatim manual text:

- **SCALE on:** "ENV - Envelope-controlled step sequencing." → play-triggered, **quantized** step sequencing.
- **SCALE off:** "ENV - Envelope-controlled time bends." Under SCALE-off: "When SCALE is off you will get classic, bendy pitch modulation, useful for creating chorusing, flanging, and tape-style warble." → play-triggered, **un-quantized** pitch bends (smooth glides).

The real distinction between the two is **quantization**, not "continuous vs triggered." Do **not** describe SCALE-off ENV as "continuous" and do **not** call it "Thermae-style" — both are editorial glosses, not manual wording. ("Thermae" appears in the manual exactly once, as Factory Preset 4 "BOUNCY THERMAE," unrelated to the SCALE/Env text. Only SINE/SQUARE are genuinely continuous LFO shapes.)

## 3. ENV is transient-triggered in BOTH SCALE states

This is the key correction. ENV does not respond proportionally and continuously to attack in either state — it **waits for an event, then advances**:

> "Instead of constantly responding to your signal, it instead waits for a transient or a distinct note, then moves the sequence forward… like a version of Step (pg.41) that is controlled by your playing." — manual p.32–33

So in **both** SCALE-on and SCALE-off, ENV is event/transient-triggered. The difference between them is only whether the movement lands on quantized steps (SCALE on) or glides freely (SCALE off).

## 4. Pitch polarity is NOT fixed — DEPTH above/below TIME sets the direction

The manual fixes **no** attack-vs-release pitch direction. With SCALE on:

> "TIME sets the starting delay time and DEPTH sets the shifted delay time… Big Time will then move back and forth between those spots."

Direction is therefore **user-configurable**: set DEPTH **above** TIME and the move goes one way; set DEPTH **below** TIME and it goes the other. "Dig in and the repeats dive-bomb" is **one achievable character** for a particular DEPTH/SCALE-off configuration — it is a valid flavor (cf. Snyder's "failing power supply" inspiration anecdote in the Superbooth interview, line 41), but it must **not** be cited as a universal fixed polarity. Snyder's failing-PSU line is explicitly framed as the *inspiration / callback*, not a spec of shipping firmware. Exact attack/recovery feel and direction need confirming by ear / on hardware.

## 5. STATE Digital removes the limiter entirely

For clean pitch movement, choose STATE **Digital** — there is no limiter to pump on top of the pitch motion:

> "DIGITAL - No limiter… uses a completely digital feedback path, useful when you want cleaner textures and stable, steady feedback (when looping). TEXTURE introduces aliasing and lowers the bit depth." — manual p.32–33

Two takeaways: (a) Digital is the right STATE when you want the ENV pitch movement to read cleanly without limiter pumping (this is the rationale behind the env-divebomb-lead patch); (b) in Digital, TEXTURE = aliasing + bit-depth reduction, **not** misbias amount.

## Sources

First-party
- Chase Bliss Big Time manual — local `gear/Chase Bliss Big Time/manuals/Big+Time_Manual_Chase+Bliss.pdf`, byte-identical to the official Squarespace-hosted PDF (MD5 247793f3…); MOTION / Env printed pp.32–33, Step reference p.41
- SonicState Superbooth — John Snyder / EAE interview; corpus transcript `gear/Chase Bliss Big Time/research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md` (line 41 failing-PSU Env inspiration anecdote)

Corpus
- `research/bloops/2026-06-19-chase-bliss-big-time-l2.md` (L2 digest — Env mechanics lens; "continuous"/"Thermae-style" refutations)
- `Patches/Chase Bliss Big Time/{mod-broken-dynaflange,big-time-env-divebomb-lead}.md` (the patches this note reconciles)

> Honesty flags: ENV pitch **direction** is not fixed by the manual and needs hardware confirmation. Avoid "continuous" and "Thermae-style" as descriptors of SCALE-off ENV — both are editorial, not manual wording.
