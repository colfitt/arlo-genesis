https://www.elektron.se/support-downloads/overbridge
Elektron Overbridge support page + Overbridge 2.0 User Manual (https://elektron.se/wp-content/uploads/2024/10/overbridge_user_manual_2.0_241016.pdf) · Elektron · 2024-10
Also: gearnews DT2 Overbridge launch (https://www.gearnews.com/elektron-digitakt-ii/) · Elektronauts "Overbridge + Digitakt 2 + Ableton" (232338) · "Digitakt II and Pro Tools" blog (paul.frields.org, 2025-06-14) for the 42-input breakdown

# Digitakt II Overbridge into Logic / Ableton — setup, streams, gotchas

## When DT2 Overbridge arrived (flag the version history)
- **Digitakt II Overbridge shipped with OS 1.03 / Overbridge 2.13, announced Oct 16 2024** — about 6 months after the DT2's April 2024 launch (early adopters waited). (gearnews; matches the OB 2.0 manual dated 2024-10-16.)
  - ⚠️ Discrepancy to flag: the DT2 dossier currently says "Overbridge 2.13 / OS 1.10A in March 2025." The OS-version/date there looks off — the OB-arrival update was **OS 1.03, Oct 2024** per gearnews and the OB 2.0 manual date. Overbridge version 2.13 is consistent across both. Recommend correcting the dossier's OS/date for the OB-arrival line.

## Setup walkthrough (Ableton + Logic)
1. **Install** the Overbridge suite from elektron.se (Overbridge engine + the Digitakt II VST/AU plugin). Latest version (always-update per environment).
2. **USB:** A→B cable, DT2 USB → computer.
3. **On the DT2:** `[SETTINGS]` → **SYSTEM > USB CONFIG** → set to **OVERBRIDGE MODE** (it will not stream without this).
4. **In the DAW:** drop the **Digitakt II Overbridge plugin** onto a MIDI/instrument track (Ableton) or an instrument/AU track (Logic). The plugin handles the USB audio + control bridge.
5. **In the plugin header:** enable **"Sync clock and transport"** so DAW Play/Stop drives the DT2 and they stay locked (DT2 effectively slaves to the DAW transport).
6. **Enable Delay Compensation / PDC** in the plugin (Ableton: the plugin's "compensate for delay" option + Ableton's own delay compensation) so the streamed audio lines up with the DAW grid.
7. **MIDI port (latency):** on the DT2 set MIDI CONFIG > PORT CONFIG **INPUT FROM = MIDI** (not MIDI+USB) when you want lowest-jitter audio recording — a forum-reported tweak that trims latency.
8. **Route per-track audio:** in the DAW, add audio tracks and set each input to the corresponding Digitakt track exposed by the plugin; arm and record all simultaneously.

### Latency knob
- Overbridge engine **buffer 64 / fastest speed** reports ~**7–8 ms** total latency in practice (forum). Use PDC to compensate rather than chasing zero.

## What streams (the channel map)
The DT2 presents **42 Overbridge inputs total**: **Main L/R + 16 stereo tracks + 3 stereo FX busses (delay/reverb/chorus) + line input L/R** (paul.frields.org breakdown).
- **Per-track stems stream in STEREO** (the DT2's big upgrade over the OG, which was 8 mono tracks).
- ⚠️ **Tracks are DRY (pre-send-FX).** Recording the 16 individual tracks captures them **without the send FX** — the delay/reverb/chorus only appear if you also record the 3 FX busses (or the Main L/R mix).
- ⚠️ **Default channel limit:** Logic/Ableton see Main L/R + only **15 of 16 tracks** by default; to get the 16th track and/or the FX busses you must **reassign outputs in the Overbridge app's audio-routing matrix** (and grabbing the 3 FX busses means dropping 3 of the 16 track feeds in the same session — total channel budget is finite). A forum workaround: sum tracks 15+16 to one output in the OB app.
- **Input passthrough:** the DT2's analog IN L/R also streams — you can use the DT2 as a small USB audio interface / re-amp return.

## Logic vs Ableton specifics
- Both work via the same AU/VST plugin + USB Overbridge mode. Logic Pro is supported; "should work, though not in the same way as Ableton" — in Logic add the plugin on a software-instrument track and create aux/audio tracks fed by the plugin's outputs (Logic's PDC is automatic). Ableton's per-track input-routing into a group (1 instrument track sending MIDI + 1 main-mix audio track + up to 15 per-track audio tracks) is the documented layout.
- **Total recall:** because the plugin stores DT2 state with the DAW project, reopening recalls the kit/pattern/parameters — full project recall is the headline OB benefit (the forum poster's reason for the setup: "sequence and record other external gear in Ableton… with full project recall").

## OG Digitakt vs DT2 Overbridge differences (flag)
- **OG Digitakt:** 8 tracks, **mono** stems over Overbridge.
- **DT2:** 16 tracks, **stereo** stems; 42 total inputs incl. 3 stereo FX busses + line in. Same caveat on both — individual track feeds are **dry / pre-send-FX**.

## Practical rig recommendation
Stream the **DT2 over Overbridge** for stereo multitrack stems + recall into Logic/Ableton; keep the **Octatrack and the pedalboard as analog** into the Apollo x8 / Babyface (the OT's OB support is more limited — see DT↔OT combo file). For lowest latency: INPUT FROM = MIDI, OB buffer 64/fastest, rely on PDC.
