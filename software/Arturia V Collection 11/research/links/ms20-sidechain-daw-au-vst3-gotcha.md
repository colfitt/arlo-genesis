(roundup — see inline URLs)
MOTUnation forum / Arturia legacy forum / Logic Pro Help / MusicTech / Apple Support · "Arturia MS-20 V external-audio sidechain in a DAW, AU vs VST3, Logic specifics" · 2022–2024 · triangulated (several threads 403/JS-gated)

THE honesty flag for the user's Logic-AU-only rig. The MS-20 V's "run the banjo into the ESP" trick depends entirely on the host exposing a **sidechain input on an instrument plugin** — and that is genuinely fiddly, format- and host-dependent.

== How Logic exposes sidechain (confirmed) ==
- https://musictech.com/tutorials/logic-pro/how-to-sidechain-in-logic-pro-x/ — Logic's side-chain selector is a **drop-down at the top-right of the plugin header** ("Side Chain"). It exists on **instrument plugins too**, not just effects — Apple's own ES2, Sculpture, and EVOC 20 PolySynth all expose it. So Logic *can* route an audio track/bus into an instrument's side-chain in principle.
- BUT a third-party AU instrument must explicitly implement the AU side-chain bus for that menu to appear. If the plugin doesn't, the menu is simply absent.

== The reported MS-20 V problem ==
- https://www.motunation.com/forum/viewtopic.php?t=68667 ("Sidechain option not always available?") — users report **the sidechain menu is NOT available in the instrument window for the Arturia MS-20 External Signal Processor**. (Thread is largely Digital Performer, but the symptom is the same class of issue.)
- Suggested fix surfaced repeatedly: **disable the AU version and use the VST3 build instead** — one user said VST3 worked, another said it still didn't for them. **Inconclusive.**
- https://www.logicprohelp.com/forums/topic/143607-side-chain-option-gone/ + Apple discussions — separate but related: third-party AU side-chain menus sometimes vanish after reinstall while stock Logic plugins keep theirs; AU validation quirks.

== Practical conclusion for THIS rig (honest) ==
- **Logic Pro is AU-only and does NOT host VST3.** So if the MS-20 V *AU* doesn't show a side-chain input in Logic, the "feed the banjo into the ESP" trick may not be available *inside Logic at all* via the documented sidechain path. THIS IS THE SINGLE MOST IMPORTANT THING TO VERIFY ON THE USER'S OWN MACHINE: open MS-20 V (AU) on an instrument track in Logic, look top-right of the plugin header for a "Side Chain" menu.
- **Reliable fallbacks if the AU side-chain is missing in Logic:**
  1. Use **MS-20 V in standalone** (its own Audio Settings → Input Channels selects a hardware input → patch Ext Out): cleanest documented path, but outside the DAW.
  2. Use **Ableton Live 12 Lite** (the secondary DAW) where VST3 + audio-into-instrument routing is straightforward — but Lite caps tracks/limits some routing; verify Lite allows the configuration.
  3. **Reamp-the-other-way (recommended for Logic):** record the banjo to audio, then use the **free Arturia "Filter MS-20" effect plugin** (AU) as an *insert* on that audio track — same KORG-35/OTA filters + distortion + envelope-follower-to-cutoff, no sidechain needed. This is the in-Logic way to get the MS-20 filter crunch onto the banjo without fighting the instrument-sidechain.
  4. Or print the banjo and feed it back through MS-20 V via whatever your host does support, then re-record.
