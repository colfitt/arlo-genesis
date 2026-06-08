https://forum.morningstar.io/t/chase-bliss-onward-and-ml10x/10029
Morningstar Engineering user forum · thread "Chase bliss onward and ml10x" · user vbpart4 + CB support (james)

# Onward in an ML10X loop — real-world GOTCHA (config corruption, fixed by factory reset)

Real owner troubleshooting thread (not a MIDI-control deep dive — see the cb-stack MIDI files for that). The useful, repo-worthy takeaway is a **gotcha + fix**, not CC values:

- **Symptom 1:** owner **vbpart4** put the Onward in an ML10X effects loop and *"whenever I enable onward in one of the loops in ml10x, it sound like everything is on 'DryKill' mode"* — i.e. the dry signal vanished / the effect swamped the mix even though MIX wasn't changed. (DRY KILL is a power-up gesture on the Onward — hold Glitch on power-up — so a stuck/unexpected Dry-Kill state is a real failure mode to know about.)
- **Symptom 2:** after that, a downstream effect (Meris Mercury) had no output despite correct routing.
- **Fix:** *"after a factory reset everything worked just fine."* → Config corruption, not hardware incompatibility. Owner flagged anxiety about recurrence before a gig.
- CB support (**james**) asked about ML10X firmware version (distinguished v1.1.2 stable vs v1.2.0 beta) — so loop-controller firmware can be a factor.

**Practical rule for this rig:** if the Onward behaves like dry is gone or routing is broken when integrated with a MIDI loop switcher / controller, suspect a stuck DRY-KILL / saved-state issue first → **factory reset (CC56, or the onboard gesture)**, then reconfigure. Pairs with the broader community wisdom captured in `onward-troubleshooting-dips-off.md`.
