https://forum.cockos.com/showthread.php?t=214234
forum.cockos.com (Reaper) · "Novation sl mkIII ff & rewind transport button problem" + DrivenByMoss docs · 2019
(page itself 403s WebFetch — distilled from search snippets + the DrivenByMoss documentation below)

## The bug
In **HUI / "HUI partial" mode** with Reaper (the fallback for any DAW without a dedicated SL script — i.e. NOT Ableton/Logic/Reason), the SL MkIII's **fast-forward and rewind transport buttons do not work**. Play/Stop work; FF/RW are dead under stock HUI.

## The fix the community lands on
- **DrivenByMoss** (free, git-moss) — a third-party control-surface script. Universal answer in-thread: "YOU NEED DrivenByMoss." Restores full transport and gives much deeper, screen-aware mapping than HUI.
- Enable DAW control by pressing the **InControl** button (top-left, between Global and Tempo). Toggling it switches between DrivenByMoss DAW control and the SL's own hardware features.
- Under DrivenByMoss the **<< / >>** buttons move the play cursor left/right in the arranger; double-click Play jumps to song start; Shift+Play toggles repeat/loop.

## Relevance to this rig
This rig uses **Logic Pro + Ableton Live 12**, both of which have dedicated SL scripts, so the raw HUI FF/RW bug shouldn't bite directly. But the takeaway generalizes: **stock HUI on the SL is weak** — if Logic/Ableton's built-in InControl ever feels limited, DrivenByMoss is the known upgrade path (it also covers Bitwig/Reaper). It is the single most-recommended SL companion software in the forums after Components itself.
