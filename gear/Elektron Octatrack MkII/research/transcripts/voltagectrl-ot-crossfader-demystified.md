https://www.youtube.com/watch?v=2VHovBWC3hs
VoltageCtrlRtv · Octatrack Sketchbook | Crossfader Demystified + Performance Effects · 2022-06-23

Goes beyond the standard beat-repeat crossfader trick into **scene-locked LFOs for "controlled randomness"** — the most musically interesting crossfader video found. The core idea: lock an LFO's *depth* (and other params) into a scene so the crossfader turns a modulation on/off, and because the LFO shape is random you "know what it'll do but not exactly what it'll land on."

## Setup
- `[BANK]` → new pattern; `[FUNC]` + `PAGE` → set **64 steps**.
- Tracks: a mix of static + flex machines (he converts a couple to Flex). Loads a basic drum loop, lays a trig, slows to **92 BPM** (hip-hop zone) as the foundation.
- **Enable the master track** (he flags this as easy to forget): PROJECT → CONTROL → AUDIO → enable MASTER TRACK (track 8).

## Approach 1 — scene-locked random LFOs (controlled randomness)
1. LFO page → **LFO1** is routed to **FX1 = low-pass filter** base. Change LFO1 **waveshape to RANDOM**, adjust speed → it wobbles the filter base width. Dial the sound, then **zero the LFO depth** so it's off by default.
2. Hold **`[SCENE A]`** and **lock the LFO depth into scene A** — now the crossfader B→A turns the random filter modulation on, with controllable on/off timing.
3. Layer more onto scene A:
   - Track 8 (master) FX → add a **comb filter**; dial its frequency, lock it into scene A too (combine with the filter sweeps — "season to taste").
   - **LFO3 → filter WIDTH**, **square wave** (hard off/on states) for a more drastic A↔B jump; lock into scene A.
   - SRC page → lock **~4–5 retrigs** into scene A so a crossfader pull randomly *might* fire a retrig (chance-based per the p-lock).
- Result: pulling to A unleashes a stacked, semi-random filter/comb/retrig burst; pulling to B is the clean state.

## Approach 2 — pitch + EQ LFOs locked to a scene
- **LFO1 → sample PITCH**, square wave (drastic pitch shifts, but time-stretched so they stay in time).
- **LFO2 → DJ EQ frequency**, automating low↔high frequency shifts simultaneously with the pitch shifts.
- Zero all LFO depths, then on **track 4** with the crossfader at A, **hold `[SCENE A]`** and lock in those LFO depths. B = no effect; A = pitch + frequency mangling that you trigger but can't fully predict.

## Approach 3 — beat repeat (the classic) via the delay LOCK
- Track 8 (master) FX2 = **delay**: double-tap → **LOCK ON**, **TAPE OFF**.
- To engage: bring **SEND to 0** (with LOCK on, send=0 freezes the buffer; you hear nothing until feedback is up). Hold `[SCENE A]` and lock SEND=0 + raise **FEEDBACK** (a little = short echoes, **127 = loop indefinitely** = beat repeat).
- **Delay control divisions:** `[FUNC]` → DELAY CONTROLS; hold key **16 (master channel)** to access beat-repeat divisions/multiplications live — plus the one armed on the crossfader. Gives rhythmic transition options for live performance.

## Approach 4 — "VoltageCtrl way": TAPE delay + scene-locked time (Korpiklaani/glitch territory)
- Delay: **LOCK OFF, TAPE ON** → delay runs all the time; turn **FEEDBACK** down for a decent echo, ride **TIME** for rhythmic effects.
- Lock the delay's params into **scene A** so the crossfader brings in the tape-delay character on demand, then use **DELAY CONTROL** to access the whole palette of delay times live — "best of both worlds" with far more sonic options than the locked beat-repeat.

## Rig relevance
This is the recipe for making a static drone *perform*: lock random/square LFOs on filter cutoff, pitch (time-stretched), DJ EQ, and a comb filter into Scene B, leave Scene A clean, and ride the crossfader so the wall breathes and mangles unpredictably-but-controllably — exactly the "degraded, recorded-wrong, evolving texture" aesthetic. The tape-delay-with-scene-locked-time approach is the more flexible cousin of the freeze beat-repeat for live transitions.
