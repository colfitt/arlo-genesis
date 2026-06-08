https://www.youtube.com/watch?v=9-2ipA5t2qE
Radial Engineering · "Reamp® Academy: How to Reamp®" (Part 2 of the Reamp 101 series, host "Austin from Radial Engineering") · 2023-05-09

Radial's own part-2 tutorial on the **ideal reamping workflow and how to wire it up**. (Part 1 covered "what reamping is"; the announced part 3 covers DAW setup — which the Apollo guide's `radial-reamp-academy.md` link captures.) Channel verified via `yt-dlp --print channel` = **Radial Engineering**. Generic to any Radial reamper; the X-Amp is the active dual-output member of that family.

## The 3-step reamp workflow (verbatim framing)
1. **Record the dry, unprocessed guitar takes into the DAW.**
2. **Play those takes back out through the guitar amp/rig.**
3. **Re-capture the amped takes back into the DAW.**

## Step 1 — record clean
- Guitar → **DI box** input. The DI converts the high-impedance instrument signal to a low-impedance mic-level output "for the best clarity and fidelity when feeding your mic preamps." Record that dry DI into the DAW.
- Want to hear an amp while you play? Feed it from the **DI's THRU output** — but you're only *recording* the dry signal. "You can focus on getting the best sounding takes possible while focusing on tone later." (This is the whole point: performance now, tone later.)

## Step 2 — send the DI back out through the reamp box
- In the DAW, **assign the DI track's output to whichever physical interface output the reamp box is connected to.**
- **No dedicated line output free?** Radial's workaround is the **Reamp HP**, which takes the interface's **headphone jack** instead. (Not relevant to this rig — the Apollo x8 has spare line outs — but worth knowing.)
- Reamp box output → guitar rig via a **standard ¼" instrument (TS) cable.** "Here is where you can start experimenting with different effects pedals, speaker cabinets, or even amp setups as a whole."
- Why a reamp box and not a bare line out: it "converts the low-impedance line-level output to a high-impedance signal best suited for amps and pedals," recreating "the rich and fullness you'd expect when connecting your guitar directly."

## Step 3 — re-record
- Mic the new rig, **press record** while the DAW plays the dry DI out to the amp — you record the finished amp tracks back in simultaneously. (Demo plays a clean DI → an amped/effected result.)

## Three extra tips (stated explicitly)
1. **Get the output level as high as you can without clipping** when feeding the interface output into the reamp box. (Best reamp signal-to-noise — same advice as the FAQ and the Apollo guide.)
2. **You can put DAW effects (EQ / limiting) on the dry DI track** as you feed the amp — shape the signal hitting the front end without re-recording.
3. **If you reamp a lot, get a combined box** (Radial Reamp Station) so DI + reamp are one unit and always on hand.

## Relevance to the X-Amp / this rig
- The workflow is identical with the X-Amp; the X-Amp's extra is the **second output** (drive two destinations) and the active class-A buffer. The "level as hot as possible without clipping" tip maps to the X-Amp's CLIP LED procedure (push the interface output until CLIP just blinks, back off).
- For the all-balanced Apollo→X-Amp loop, **no DI box is needed on the send side** (both are balanced line level) — the DI in step 1 is only for the original clean capture.
