https://www.elektronauts.com/t/digitakt-resampling-through-fx/213230
elektronauts.com · community thread · 2024 (+ older OG-era thread, flagged below)

# Digitakt II — Resampling Through External FX / Pedals (re-amp loop)

Directly relevant to this rig: running a DT2 track out through the pedalboard (or a looper/rack) and resampling it back in. Plus the perennial feedback/monitoring problem.

## The core problem (transfers OG→DT2)
With input monitoring ON, "what you hear is sent via headphones and L/R OUT" (sezare56) — so if you patch Main Out → pedals → DT2 In, the signal you're recording is *also* going back out the mains, creating a feedback loop.

- **Craig (OG-era, principle still applies):** "you can't resample back into the Digitakt without creating a feedback loop unless Monitoring is turned off because the signal you're sampling will be sent back out of the Main Outs."

## Workarounds people use on DT2
1. **Disable TO MAIN, sample the inputs blind.** In AUDIO ROUTING, turn off TO MAIN for the source so it isn't re-sent out the mains; you sample the returning processed signal without feedback — but you lose live monitoring ("flying blind," trial-and-error).
2. **External mixer for monitoring.** Put a small mixer between DT2 and the pedals so monitoring is handled outside the feedback path. The cleanest answer for a re-amp-through-the-board workflow.
3. **USB/Overbridge loop** (blaize, OG method, transfers): remove tracks from Main Out, pull audio out over USB, add a plugin/external FX, send back over USB, and **sample from USB with monitor on** — feedback-free because the loop is in the box/computer, not on the analog mains.
4. **Looper as the FX hub** (jamiemellor): DT → RC-505 looper → pedals → external mixer → DT inputs. "Record the digitakt to the looper, add fx then resample." He runs the **looper as MIDI clock master** when syncing: "set it up as master when syncing the midi clock to the DT."

## Selective USB output (cross-ref)
From the Overlooked-Features thread: you can route **only specific tracks** out over USB (a stereo pair or two monos) for external processing — Python's example chained it "through… guitar pedals" with an OP-1 Field, then resampled. This is the tidy way to re-amp a single drone track through the texture boards without dumping the whole mix.

## Gain staging (from the pedals-resampling thread, OG-era, transfers)
Source: https://www.elektronauts.com/t/resampling-using-effects-pedals/159329
- jrjulius: "DT's input attenuates to something like −12dB and then normalizes to 0dB after recording." Avoid pedals that boost a lot to prevent overload/feedback; on newer firmware you may need to lower input level in the mixer manually.
- Use TS (mono) cables to the pedals as appropriate; a pedal/interface with its own headphone out solves monitoring.

[OG-vs-DT2 flag: the feedback mechanism, monitoring fix, and gain-staging notes originate on the OG Digitakt but apply identically to the DT2's analog I/O. The DT2 adds stereo I/O and selective USB-audio output, which makes workaround #3 cleaner than it was on the OG.]

NOTE: the DT2-specific thread confirms users were still troubleshooting the headphone/output level conflict — the workflow works but isn't frictionless. Flagged accordingly.
