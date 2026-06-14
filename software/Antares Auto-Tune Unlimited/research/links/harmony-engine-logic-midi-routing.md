https://help.antarestech.com/hc/en-us/articles/41109250589716-How-to-configure-MIDI-control-of-Harmony-Engine-in-Logic-Pro
Antares Support Center · "How to configure MIDI control of Harmony Engine in Logic Pro" · n.d.
[NOTE: Antares help domain 403s to direct fetch — captured from the search-engine summary of the official article; steps cross-confirmed against the Sage Audio Prismizer guide. LABELED triangulated.]

The exact Logic Pro (AU-only host) routing for using Harmony Engine in any MIDI mode (Chord Via MIDI / MIDI Omni / MIDI Channels) — i.e. to *play* the harmony voices. This is the rig-critical bit since Logic doesn't expose a plain "sidechain a harmonizer" path the way Pro Tools does:

**Steps (official):**
1. Create an **audio track** (holds your source: vocal, or a banjo/baritone/synth/drone print) AND a **Software Instrument track**.
2. Record/import the source audio onto the audio track. **Set that audio track's output to "No Output"** (so it only feeds the side-chain, not the mix bus — Harmony Engine re-voices it).
3. On the Software Instrument track, load Harmony Engine as the **Instrument** — it lives under Logic's **"AU MIDI-controlled Effects"** category (NOT the normal insert FX list, NOT the Instruments list). This is the non-obvious part: in Logic an AU MIDI-controlled effect is instantiated in the instrument slot.
4. In the Harmony Engine window, open the **Side Chain** dropdown (upper-right) and select the audio track you made (e.g. "Audio 1"). That tells it which audio to harmonize.
5. Set **Harmony Source = MIDI Omni** (or Chord Via MIDI / MIDI Channels).
6. **Record-enable (red R) the Software Instrument track**, start playback, and play your MIDI controller (the 61SL MkIII) to drive the harmony voices in real time; record the MIDI to print the performance.

**Caveats / rig notes:**
- Without this routing, Harmony Engine on a plain audio insert only does the *non-MIDI* modes (Fixed/Scale Interval, Chord Degrees, Chord Name). The "play the wall from the keyboard" modes REQUIRE the AU-MIDI-controlled-Effect + side-chain setup above.
- Source audio output = **No Output** is the gotcha people miss (otherwise you hear the dry source doubled with the harmonized version, or it clutters the bus).
- All harmony voices come out of the **instrument track**, so EQ / Choir-multiplier / reverb / the Valhalla send all go on that instrument channel, not the source audio track.
- For live (un-printed) play, lower the I/O buffer (<128 samples per the Sage Audio Prismizer guide) to cut latency; otherwise print and use Freeze for sustained drone-chords.

This is the Logic mechanism behind the Prismizer / played-choral-bed recipes. Same idea works for the AVOX *Choir* note: Choir has no MIDI, so it just goes on a normal stereo insert — only Harmony Engine needs this.
