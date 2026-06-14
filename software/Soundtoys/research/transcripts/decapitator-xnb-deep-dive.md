https://www.youtube.com/watch?v=B6ANk9jfG6k
XNB · "A deep look to the DECAPITATOR by Soundtoys — Guide tutorial" · 2023-02-27 (14:15)

(Auto-caption transcript, cleaned to prose. The most thorough signal-flow walkthrough
— uses a spectrum analyzer + harmonic display to SHOW what each style does with zero
drive.)

This is a deep dive, not a review. **Start with the Styles — this is the most
important section of the plugin.** As soon as you turn Decapitator on, even with NO
drive, it starts working: the spectrum goes from flat (bypassed) to shaped, and the
harmonic display shows it's already adding harmonics. The different styles are
emulations of different hardware units, so each one shapes the sound differently
before you touch drive.

**Styles, with zero drive, on a drum patch:**
- **A** — emulation of the Ampex 350 tape and preamp. It's a little bit flat, the
  flattest of them all, and smooth.
- **E** — emulation of the Chandler. Notice a little more low end / punch, a tiny dip
  in the low mids, then it sounds brighter than A — there's "air" at the very top.
- **N** — a Neve 1057. Less bright, a tight low end, and more mids. Really different
  from the previous two.
- **T** and **P** — both emulations of the Culture Vulture, the same hardware unit in
  two configurations. **T = triode mode → leans to EVEN harmonics. P = pentode mode →
  the odd harmonics.** There's a little difference between them.

Key takeaway: when you throw the plugin on a channel you often **don't need to drive
it** — just audition the different styles and you may already get what you want. A lot
of people slam the drive instantly; try just stepping through styles first, and only
reach for drive if you need it.

**Drive and Punish.** The drive control adds more INPUT to the saturation stage of
whatever emulation you're using — more input → more saturation. Drive it up on A and
it gets really aggressive; each style sounds a bit different driven hard. **Punish
adds an extra 20 dB of gain** — that's all it does. Even with drive at zero, Punish
on means you're already 20 dB up into the circuit, and then you can drive further.
Use it when the thing you want to saturate is very quiet.

**Low Cut + Thump (PRE-saturation).** When you drive a full drum kit hard you get a
low-end bump because of the kick/snare, which is why you have the low cut — it reacts
BEFORE the signal gets saturated, cutting low frequencies so the saturation stays
tight. Find the combination of cutting and driving you like. **Thump is a peak/bump
right at the low-cut cutoff frequency** — sweep the low cut and you can hear the bump
move. Both the low cut and Thump happen before the saturation stage.

**Tone (PRE-saturation).** The tone control is a **tilt EQ**: go dark → more lows, less
highs; go bright → more highs, less lows (that's why it's a "tilt" — boost one, cut the
other). At center it does nothing. It happens pre-saturation, just like the low cut, so
it changes WHICH frequencies get distorted — you can even use it to balance the sound.

**High Cut + Steep (POST-saturation).** The high cut acts AFTER everything gets
saturated — it just chops high frequencies off the output. By default it's **6 dB/oct
(gentle)**; flip **Steep** and it becomes **30 dB/oct (aggressive)**. Remember it goes
after the saturation — you're not chopping before you get the harmonics.

**Output / Auto.** As you drive up, the output gets louder, but **Auto is on by default**
— move the drive and the output knob moves the opposite way to hold level. If it's still
too loud and you don't plan to automate drive, just lower the output yourself; or disable
Auto and set output fully manually.

Summary signal order: **Low Cut → Thump → Tone → [SATURATION/Drive+Style+Punish] → High
Cut → Steep → Output.** It's a simple plugin to use but you need to be aware of all the
styles and what they do, because everything you do at the top is reactive to the style
chosen at the bottom.
