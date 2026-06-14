https://support.xlnaudio.com/hc/en-us/articles/10851951752861-Separate-Outputs-in-Logic
xlnaudio.com (official support) "Separate Outputs in Logic" + Logic Pro Help thread "LPX & AD2 Multi Out Problem [SOLVED]" (logicprohelp.com/forums/topic/99415) · accessed 2026-06-11 (XLN page 403s bots; steps triangulated from search-indexed text + the [SOLVED] forum thread)

# AD2 multi-out in LOGIC PRO (the owner's primary DAW, AU-only)

## Steps
1. New **Software Instrument** track → load the **Multi-Output** AU variant of AD2
   ("Addictive Drums 2" with the multi-out / "4x Stereo, 10x Mono" designation in the
   AU instrument menu). Logic shows multi-out AUs with the little output count.
2. Inside AD2, click the **green down-arrow** on each channel you want separated
   (Kit/Mixer view).
3. In Logic's **Mixer**, find the AD2 channel strip. At the bottom there's a small
   **[+]** button — click it repeatedly. Each click **adds an Aux channel strip and
   auto-assigns** it to the next AD2 output. This is the fast way (vs. manually
   creating auxes and setting inputs).
   - Manual alternative: Mixer → **Options → Create New Auxiliary Channel Strip**
     (Ctrl+N), then set each Aux's **Input** to the AD2 instrument's outputs
     (Inst 1 (3-4), Inst 1 (5-6), etc.).

## Known Logic gotchas (from the [SOLVED] thread)
- If the extra outputs don't show up, you likely loaded the **stereo (non-multi)
  AU** — delete and reload the multi-out variant. Logic will not "upgrade" a stereo
  instance to multi-out in place.
- Output numbering: AD2's internal channel order maps to Logic outputs 3/4, 5/6,
  7/8… (1/2 = the AD2 master/main pair). Confirm by soloing one drum and watching
  which Aux meters.
- Because routed drums **bypass AD2's master FX** (see ad2-xln-separate-outputs),
  do glue/character on the Logic auxes — this is exactly where you'd insert RC-20,
  DS-10, Decapitator, SketchCassette per-drum.
- AU-only host: no quirk beyond "use the multi-out AU variant." AD2 is a mature AU;
  no VST-vs-AU behavior difference reported in Logic.
