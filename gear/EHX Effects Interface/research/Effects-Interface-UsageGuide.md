# Electro-Harmonix Effects Interface — Usage Guide

How people *actually* use the Effects Interface (model FXI), to complement the spec/reference dossier in `Effects-Interface-DeepResearch.md`. It's a **bench/studio bridge, not a live in-chain insert**: a USB-C 2-in/2-out box that runs **real pedals as DAW plugins** (re-amp), runs **DAW plugins as pedals** on your board, and reconciles **instrument ↔ line level** with its gain sliders. In this rig its jobs are re-amping the VG-800 / dry DIs through the full Board 1 inside the DAW, putting software plugins on the physical board, and running line-level synth/sampler gear through the pedals. The mental model: **level matching is done with the INPUT/OUTPUT sliders, not a transformer**, and **the plugin modes need the software plugin connected (USB LED green) or no audio passes**.

> Captured this wave (Tier C, 1 agent): 5 video transcripts + 6 distilled links = 11 sources (see §7). Better coverage than expected for a NAMM-2026 product. All channels verified via yt-dlp — and the official EHX walkthrough URL (`wEFHeO-KxS0`) is now confirmed and added to the dossier §10 (it was previously unverified).

---

## 1. The three modes (step-by-step)

**Hardware Plugin Mode (pedals-as-plugins / re-amp).** Pedal OUT → the FXI's **INPUT** jacks; FXI **OUTPUT** jacks → pedal IN. Keep your normal interface (Apollo) as the DAW's I/O. Insert the **EHX plugin** on a track → Settings → Select Device → FXI → **Audio > Stereo/Mono** (USB LED **green** = connected; otherwise no audio); calibrate on first use; press play. **Print in real time to a new track** ([ehx-official-walkthrough](transcripts/ehx-official-walkthrough.md); [sweetwater-fluff-reamp](transcripts/sweetwater-fluff-reamp.md)).

**Pedalboard Mode (plugins-as-pedals).** Instrument → **INPUT**, **OUTPUT** → amp/rest of chain. On one DAW track put **two plugin instances** — the first set **Pedalboard > IN**, your DAW plugins between them, the second set **Pedalboard > OUT**. *Tip:* leave a few empty slots between IN and OUT to avoid dropouts ([pedalscapes-in-the-studio](transcripts/pedalscapes-in-the-studio.md)).

**Audio Interface Mode.** Select the FXI as the DAW's I/O device; don't load the plugin. Lowest latency, but it monopolizes the DAW (use the Apollo for normal sessions).

---

## 2. Level matching (VG-800 line ↔ instrument board)

Done with the **sliders, not a transformer.** **OUTPUT sliders** set how hot the board is driven (start so the front end sees *instrument* level); **INPUT sliders** trim the wet return. **Watch the INPUT meters — orange = −6 dB, red = −3 dB (back off).** The 2 MΩ input / 330 Ω output + +7/+8 dBu headroom accept the VG-800's hot output and deliver instrument level "without a DI/re-amp box." In **Audio Mode** the **MIX** knob blends the dry track with the wet return — a per-track wet/dry an on/off pedal can't give ([level-matching-and-reamp](links/level-matching-and-reamp.md); [guitarworld-review](links/guitarworld-review.md)).

---

## 3. DAW gotchas (manual-authoritative — read before first use)

- **Offline render/bounce must be OFF** — the signal physically leaves to analog pedals, so it's **real-time only**.
- **Sample rate must be 44.1 / 48 / 88.1 / 96 kHz.**
- **The DAW may auto-grab the FXI as a MIDI device** → disable its MIDI I/O/sync, or the plugin won't connect.
- **Logic: Low Latency Mode *bypasses* the FXI** — turn it off; for Pedalboard Mode, use a MIDI/Software-Instrument track with a blank region so Logic passes real buffer sizes (not 1024).
- **Reaper: disable Anticipative Processing** (Audio → Buffering). **Pro Tools (Windows): `ExcludedMIDIPorts.txt`.**
- **Lower the buffer/block** in the plugin's Device Options to cut latency; **Speed Control** on = more stable, but turn it **off when you need tight wet/dry phase agreement** (it can cause phasing) ([daw-setup-gotchas](links/daw-setup-gotchas.md)).

---

## 4. Rig-specific recipes

- **Re-amp the VG-800 through Board 1 (primary use):** record the VG-800 / a dry DI to a track via the Apollo; insert the FXI plugin (Hardware Plugin, Audio > Stereo); patch FXI **OUTPUT → front of Board 1** (Polytune/CB Clean), **Deco stereo out → FXI INPUT**; set OUTPUT sliders for instrument level, INPUT peaking orange (not red); record the wet return to a new track in real time. This is the cleanest way to commit "VG-800 → full pedalboard" passes without playing live.
- **Plugins-as-pedals on the live board:** drop a Valhalla/Soundtoys/Auto-Tune plugin "onto" the board via Pedalboard Mode (two FXI instances IN/OUT).
- **Line-gear-through-pedals:** run a Digitakt/OP-1/MPC loop through the **Microcosm / Dark Star / H90** — the line-level headroom is the point; turn a dry loop into a granular wash and capture it.
- **Latency reality for this rig:** Fluff measured ~30-sample round-trip on a fast machine, and dr. ooh confirms **Apollo + an M-series Mac = unnoticeable latency** — directly relevant here ([sweetwater-fluff-reamp](transcripts/sweetwater-fluff-reamp.md); [dr-ooh-shoegaze-pedalboard-mode](transcripts/dr-ooh-shoegaze-pedalboard-mode.md)).

---

## 5. vs the Radial X-Amp (why both)

The owned **Radial X-Amp** is the better **pure/analog** re-amp — instant, zero latency, no computer, no converter — reach for it for fast clean re-amping of a recorded track/DI through pedals, especially when you want zero digital round-trip. The **Effects Interface** is the better **DAW-integrated** re-amp + bridge — the re-amp lives *in the session* (recallable, automatable, wet return on its own track) and it can run plugins-as-pedals, but it's technical to set up. Owning both is justified; PedalScapes (who owns a Radial XTC) keeps both ([pedalscapes-in-the-studio](transcripts/pedalscapes-in-the-studio.md); [nate-navarro-demo](transcripts/nate-navarro-demo.md)).

---

## 6. Notable users & common pitfalls

**Users:** none yet — it's a NAMM-2026 product with no developed mythology. The demos above are reviewers/creators, not signature users.

**Pitfalls / gotchas:**
- **Buffered (not true) bypass** — always in-circuit as a buffer; still passes signal when "off," but it's not a passive wire.
- **One plugin instance can hold the hardware at a time** — disconnect on one track before connecting on another.
- **Mono↔mono or stereo↔stereo only** — no clean mono-out/stereo-in path.
- **Not plug-and-play** — budget setup/config time (PedalScapes needed an EHX support ticket; the manual is thin on detail).
- **The connected-plugin requirement** — in plugin modes, no audio passes unless the software plugin is connected (USB LED green).
- **Power ≥150 mA** — 125 mA draw, but supplies under 150 mA may be unreliable; USB-C bus power works.
- **Latency is config/computer-dependent** — a slight lag can read as a "double-track" (sometimes useful); lower buffers + a fast machine minimize it.

---

## 7. Captured sources

**Transcripts** (`research/transcripts/`):
- `ehx-official-walkthrough.md` — EHX, "Bridging the Pedalboard-Plugin Gap" (2026-01-12) — the official 3-mode demo (pedals-on-tracks + plugins-as-pedals; dual-mono).
- `sweetwater-fluff-reamp.md` — Sweetwater Soundcheck ft. Fluff — re-amp loop in Pro Tools; ~30-sample latency; MIX-knob fine-tune; double-track both DI sides.
- `nate-navarro-demo.md` — Nate Navarro — bass; pedalboard into the session both directions; automation as the killer feature.
- `pedalscapes-in-the-studio.md` — PedalScapes — **the richest gotchas**: one-instance-at-a-time, mono/stereo limit, real-time print, phasing on lowest buffer, empty-slot fix, vs Radial XTC.
- `dr-ooh-shoegaze-pedalboard-mode.md` — dr. ooh — shoegaze Pedalboard Mode; Apollo + M4 = unnoticeable latency; studio-only value take *(mostly music)*.

**Links** (`research/links/`):
- `daw-setup-gotchas.md` — EHX EIHP Manual v1.0 — authoritative setup + all DAW gotchas (verbatim).
- `level-matching-and-reamp.md` — Manual — the sliders/meters + level/re-amp recipe + dual-mono.
- `guitarworld-review.md` — Guitar World (Alex Lynham) — gain-matching sliders, "crucial" meters, Pedalboard Mode fiddlier, value.
- `musicradar-announcement.md` — MusicRadar (Si Truss) — clean 3-mode statement, "pedalboard-friendly levels / no DI box."
- `guitar-com-news.md` — guitar.com (Crystal Koe) — vocals/synths/MIDI through pedals; real-time.
- `juno-daily-review.md` — Juno Daily (Greg Scarth) — verdict + no-DI framing *(page 403'd; summary-sourced; an auto-latency-comp claim flagged unverified)*.

## Sources

All claims above cite a captured `transcripts/` or `links/` file; original URLs are on the first line of each. Video attributions verified via `yt-dlp --print channel`. Authoritative spec/reference lives in [`Effects-Interface-DeepResearch.md`](Effects-Interface-DeepResearch.md); the manual is at [`manuals/EIHP_manual_Web_v1.pdf`](manuals/EIHP_manual_Web_v1.pdf).

> **Honest coverage notes:** NAMM-2026 product — coverage is thin but better than expected (one official demo + four real creator/review videos + the manual + written pieces). EHX's product page, the "Five Stars" blog, Juno Daily's full text, and guitar.com all 403'd direct fetch (content reconstructed from extracts where noted). No famous users exist this early. The PedalScapes and manual sources carry the real workflow gold; the dr. ooh video is mostly music (framing/latency only).
