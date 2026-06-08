https://www.eventideaudio.com/forums/topic/need-help-to-sync-h90-with-tap-tempo-of-the-mc6-pro-midi-controller/
Eventide official forum · stekadon (Q) / Brock (Eventide support, A) · Mar 1–2, 2025

# Syncing the H90's tempo to a MIDI rig — clock vs CC-tap

Two ways to make H90 delays follow rig tempo:

## Method 1 (recommended): MIDI Clock
- Set the H90's delay Programs to **Tempo Sync mode** (Tempo Source = MIDI; clock source DIN or USB).
- Send a real **MIDI Clock** stream from the controller. On an MC6 Pro, program a switch as **"MIDI Clock Tap"** so taps generate clock.
- stekadon confirmed it working. Brock recommended clock over CC.

## Method 2 (if you prefer tap-CC, like a TimeLine):
- Map the **Program Tap Tempo** Performance Parameter to an **external MIDI CC** (per-Program or as a Global mapping), then have the controller's tap switch send that CC.
- Match the controller's outgoing CC# to the H90 assignment.

## Key gotcha
> MIDI **preset changes worked fine, but tempo sync initially failed** — successful MIDI routing does NOT guarantee all message types work without explicit configuration.

In other words: PCs landing correctly tells you NOTHING about whether clock is reaching the H90. You must explicitly set Tempo Source = MIDI AND confirm the clock source (DIN/USB) AND that the master is actually emitting clock.

## Rig relevance
The rig's clock master is the **Digitakt 2**, and the dossier says H90 syncs via Tempo Source = MIDI. Confirmed correct path: Digitakt 2 → MIDI clock → H90 (Clock Source = DIN), Tempo Source = MIDI, delay Programs in Tempo Sync. Verify clock is actually flowing (this thread's gotcha) — test a Tempo-Sync delay and change the Digitakt tempo; the H90's repeats should track. If you'd rather tap-sync from a Morningstar in the chain, use the CC-tap method instead.
