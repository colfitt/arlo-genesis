https://support.splice.com/en/articles/8652822-adding-arturia-plugins-into-logic-pro-x
support.splice.com + Arturia FAQ (Apple Silicon) · 2024-2025

GETTING ARTURIA V INSTRUMENTS INTO LOGIC PRO (AU):
1. Install via the Arturia Software Center (ASC) — the hub for install + updates.
2. Log in with the Arturia account; click Activate on each product (license can
   live on up to 5 devices). Use Sync to refresh license info.
3. ASC drops AU components into /Library/Audio/Plug-Ins/Components (VST3 alongside).
   Logic = AU-ONLY, so the .component is what matters; it appears under the track
   Instrument slot → AU Instruments → Arturia → <instrument>.
4. Restart the machine + relaunch Logic so the AU validation/scan picks them up.
5. If a plugin doesn't appear: Logic re-validates AU on launch; force a rescan
   (Logic → Settings → Plug-in Manager → select Arturia → Reset & Rescan
   Selection). Splice-specific tip: log out/in of the Splice app.

APPLE SILICON / ROSETTA:
- Modern V Collection is Universal Binary (native Apple Silicon + Intel).
- To verify a plugin is running NATIVE arm64: open the plugin's About → check the
  build number. "ARM64" = native on Apple Silicon; "Rosetta" = running translated.
- For standalone apps: Finder → right-click the .app → Get Info → ensure "Open
  with Rosetta" is UNticked for native performance.
- Running Logic itself natively (not under Rosetta) keeps the Arturia AUs native.

FORMATS: every V instrument ships Standalone, AU, VST, VST3, AAX. In this rig
only the AU matters for Logic; standalone is handy for sound-design auditioning
outside the DAW (no host CPU/automation overhead) before committing a part.
