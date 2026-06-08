https://support.akaipro.com/en/support/solutions/articles/69000859300-mpc-series-convert-your-chopped-samples-into-a-drum-program
support.akaipro.com (official) · "MPC Series | Convert Your Chopped Samples Into A Drum Program"

GENERAL-MPC documentation — TRANSFER FLAGGED. This is Akai's official chop-to-kit workflow, but it is written for the FULL standalone MPC OS (One/Live/X/Key), NOT the MPC Sample (AC50). Captured here specifically to flag what does and doesn't transfer, because the AC50 is the one model where this is the WRONG procedure.

## The FULL-MPC procedure (does NOT match the AC50 UI)
1. Browse > Places > load the sample.
2. **Menu > Sample Edit.**
3. Tap the **Trim tab → switch to Chop tab.**
4. **Threshold** auto-chops and assigns slices to pads; drag red/green tabs to refine.
5. **Hold SHIFT + tap "Convert"** at the bottom of the screen.
6. In the pop-up choose **"New Drum Track Using Slices" → "Do It".**
7. Press **Main** to see the slices as a drum program track.

## Why this does NOT cleanly transfer to the AC50 — FLAG
- The AC50 has **no "Menu" / "Sample Edit" screen, no Main/track view, no drum-PROGRAM/track architecture** like the touchscreen MPCs. It is a single-track, kit-based box.
- The community explicitly reports the AC50 does NOT auto-convert chopped slices into a full kit: chopped slices "don't auto-convert into a full kit — manual slice extraction" (matches the project dossier §11), and you can only have **one kit at a time** (confirmed in the Ten-Tips video and gearnews review).
- The "Convert > New Drum Track Using Slices > Do It" command and the "Main button = drum program track" step rely on features the AC50's reduced OS doesn't expose.
- The underlying reason: per MPC-Tutor on the forums, the AC50 runs a cut-down MPC3-era firmware with "many MPC3 features... removed." So bigger-MPC tutorials should be assumed NOT to apply until verified on the AC50.

## What the AC50 DOES do for chopping (verified-on-device alternative)
- **Chop mode** (blue CHOP button) auto-slices a sample (Threshold by default; also 4/8/16 equal regions or manual) and lays slices across the 16 pads for triggering/re-sequencing — this is the AC50's strength.
- For "kit-like" building you extract/place slices onto pads manually, and use **pad LINK** (SHIFT while PLAY/B2 selected) to tie pads together as a partial layering workaround (no keygroups).
- Bottom line for the rig: chop-and-trigger on the AC50 = native and fast; "convert chop to a multi-program drum kit" = a bigger-MPC feature, NOT available the same way — don't follow the desktop/standalone tutorial verbatim.
