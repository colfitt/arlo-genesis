https://www.mpc-forums.com/viewtopic.php?f=50&t=220660
mpc-forums.com (MPC Sample subforum) · "Septimo" (Q) + MPC-Tutor (A) · 2026

AC50-SPECIFIC and RIG-CRITICAL (this studio makes baritone/doom sub-bass). The AC50 has an audible static/crackle problem on low-frequency content.

## The gotcha
Septimo: "samples with low frequencies like Bass / 808s / kick drums will have static... at random sections of any sample of these characteristics... it doesn't happen with anything else of mid frequencies on up... it's annoying to hear that crackle whenever you hit an 808. I'm on the latest firmware but it was doing this with original factory firmware too." (Persists across firmware → likely intrinsic, not a one-off bug.)

## Cause + fix (MPC-Tutor)
> "It is very sensitive to low frequencies so it will clip the output when playing bass and subby kicks, especially if they are normalised. Have you tried adjusting the level of the affected pad?"
- It's **output clipping on sub/low-end**, made WORSE by Normalising the sample (Normalize pushes peaks to 0 dB, and the low-end then clips the output stage).
- FIX: **turn DOWN the level of the affected (bass/kick) pad.** Septimo confirms it helped but "I had to turn it down significantly... lower than I'd like... higher frequency samples can be loud as heck without clipping." So it's a real headroom asymmetry: low-end needs much more attenuation than highs.

## Rig implications (doom / baritone / sub-bass material)
- For Repitched-down baritone drones and sub-bass beds, DON'T just Normalize and slam them — leave headroom and **pull the bass pad's level down** to avoid the crackle.
- Consider doing final low-end leveling/limiting downstream in the Apollo rather than maxing it on the MPC.
- Be cautious stacking Normalize on subby chops; it's the specific trigger MPC-Tutor calls out.
