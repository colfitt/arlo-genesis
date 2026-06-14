https://www.kvraudio.com/forum/viewtopic.php?t=596679
kvraudio.com · DSP/Plugin Dev forum · Markus Krause (Tone2), kerfuffle, hugoderwolf, Fender19 · 2023-05

# Why AU plugins fail Logic validation — developer-side reality (matters to AU-only users)

This is a plugin-developer thread, but it explains the "Logic can't find my
plugin / failed validation" pain every AU-only Logic user eventually hits.

## The core truth (Markus Krause, Tone2)
- **AudioUnit (AUv2) detection has been broken for ~8 years** at the OS level
  (since High Sierra) — NOT Logic-specific. Newly installed AUs often:
  - **require a full reboot** to be detected, OR
  - rely on an "ugly script in the installer that kills a process"
    (`killall -9 AudioComponentRegistrar`) to force a re-scan.
- Apple is aware and **won't fix it** — a dev was told AUv2 is "deprecated."
- Other failure causes he lists:
  - **Missing/invalid code signature** → `auval` crashes with `Error #FFFFFF7`
    (the OS kills auval when it tries to load an unsigned framework).
  - **Caching problems.**
  - **Behaves differently Intel vs Apple-Silicon (Rosetta vs native).**

## Validation can pass on one Logic version, fail on the next
Fender19: a plugin that **passed in Logic 10.7.1 / Monterey FAILED in Logic
10.7.7 / Ventura** with `ERROR: 4099 ... Problem with initial Channel layout
state` — same binary, same simple mono/stereo I/O. Logic let him "run anyway"
and it worked fine. So a "failed validation" is frequently a Logic/OS edge-case,
not a broken plugin.

## What this means for an AU-only user (practical takeaways)
1. **After installing any new AU, reboot** (or relaunch Logic) before assuming
   it's missing — the registrar is the usual culprit, not the plugin.
2. If a plugin fails validation but you can **"Use Anyway" in Plug-in Manager,
   do it** — it usually works (devs confirm Logic's "run anyway" override is
   reliable in practice).
3. A plugin that worked then vanished after a Logic update may just need a
   **Plug-in Manager > Reset & Rescan** (see au-validation-troubleshoot file) —
   the binary is probably fine.
4. Running Logic **native (Apple Silicon) vs under Rosetta** changes which AUs
   validate — keep a consistent mode. For an Intel-only legacy AU you may need
   Logic in Rosetta.
5. Since this is OS-level, the **same flakiness does NOT exist for VST in other
   hosts** — it's a real cost of the AU-only world, mitigated by reboot +
   rescan + "use anyway."
