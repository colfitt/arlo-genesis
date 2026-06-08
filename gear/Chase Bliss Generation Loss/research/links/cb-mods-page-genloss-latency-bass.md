https://www.chasebliss.com/gen-loss-mkii-mods
chasebliss.com · Chase Bliss (official) · accessed 2026-06-03 (guide dated Dec 2022)

# Gen Loss MkII OFFICIAL MODS — latency firmware + bass hardware mod (AUTHORITATIVE)

Chase Bliss ships TWO optional, independent mods for the Gen Loss MkII. Both became the **default on units shipped after late 2022 / batch 2** (chosen "to accommodate a wider range of instruments"). CB stresses these are "very minor changes — only apply them if you notice latency or bass issues." Source content pulled from the official mods page AND the full text of the official Modification Guide PDF (`gen loss modification manual 04`, Adobe, created 2022-12-19).

## 1. FIRMWARE / LATENCY MOD (software, reversible)

**What it is (quoted from the guide):** "Generation Loss MKII has a short delay between your input signal and the effect, called latency. The original latency was set to be as tight as possible while also giving a nice chorus sound, but some users noticed that this can give you a doubling effect with short, percussive sources like a drum machine. **This update tightens up that latency.**"

**The trade-off (quoted):** "The sound will be **more flange-y than chorus-y when used in stereo or with some DRY mixed in.** The tape stop effect also has some **gritty artifacts** and the **noise has a slightly different character**." Latency drops to "at least half the original amount" and it "mitigates the perceived 'double tracking'" on drums/percussion.

- Two firmware files exist: **1.0.0 (original)** and **1.1.0 (low-latency)** — both downloadable, so you can A/B and revert freely.
- **How to flash:** 9V center-neg power + **USB micro cable** + computer (**Windows recommended**) + **STM32CubeProgrammer** (free, requires quick registration). On **Mac you need a workaround** (shown in CB's walkthrough video). Steps in order: connect USB to pedal → power pedal → open STM → select USB + refresh → Connect → Open file (the .bin) → Download → unplug/repower. **Order matters; if it fails to connect, recheck USB and repeat in order.**

> ⚠️ **For THIS rig:** Gen Loss runs into stereo time/space effects (Big Time, MOOD, Blooper, H90). The low-latency 1.1.0 firmware makes the **stereo image flange-y rather than chorus-y** — which may actually be *better* for a width tool feeding stereo delays, but it's a real character change. If you prize the lush stereo chorus, the original 1.0.0 is the chorus-y voice. The pedal isn't being used as a tight drum processor here, so the latency benefit of 1.1.0 matters less than the stereo-character difference. Worth A/B'ing both .bins.

## 2. BASS HARDWARE MOD (solder, harder to undo)

**What it is (quoted):** "The EQ voicing of the Generation Loss MKII circuit has a **gentle, analog high pass filter** on it... this mod **restores full bass response**." Trade-off: "the high-pass filter can be pleasing and helpful depending on your instrument and context. If you already like how your pedal sounds, don't overthink it!"

- **Procedure (from guide):** open pedal → tuck black & red wires aside → identify **four parts (caps)** → **remove the four caps** → **bridge the four sets of pads**. "You should now have a full-frequency bass response." Requires SMD soldering comfort (thin-tip iron, tweezers helpful). The guide does **not** print component designators/values — just "the four caps" shown in photos/video.
- **CB will do it for FREE** (you only pay shipping to them) — email help@chasebliss.com. They'll also complete or swap a unit if you can't solder it.

> ⚠️ **For THIS rig:** the rig runs a **baritone Jazzmaster + banjo** and the dossier already flags Saturate getting "flubby on bass-heavy material." The stock analog HPF is what tames that low-end flub. For a baritone-drone rig you likely **want to KEEP the stock HPF** (do NOT do the bass mod) — it tidies the lows before the time effects. Community corroboration (Elektronauts): one user found post-mod "the pedal sounds better with all models when the dry toggle is set to SMALL," and the mod "means people can use it... incl on a full mix" — i.e. the mod is for full-range/full-mix use, not for guitar where the HPF is helpful. Skip unless lows feel too thin.

## Version / serial note
Community (Elektronauts) reports **"all of batch 2 is supposed to be modded."** One user with SN #03849 received an UNMODDED unit and CB offered free return for the mod. There is **no published serial cutoff** distinguishing modded vs original units — even CB hasn't documented it. To know what firmware your pedal runs, you basically have to flash it or ask CB.
