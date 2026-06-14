https://www.youtube.com/watch?v=R-FFWr_9JKk
ADSR / Nick Chen · "How to use RC-20: use Retro Color LIKE A PRO with this complete walkthrough" · May 2020

The single most complete module-by-module walkthrough. Distilled below (the cleaned transcript follows the notes).

## Distilled — UI map & per-module behavior

**Four sections:** (1) Top = preset browser + the global **Magnitude** slider; (2) the
six **effect modules**; (3) the **big knobs** (per-module amount); (4) the **Master** section
(dynamics + EQ).

- **Magnitude (top)** = "one of the most important parameters." Scales all six big knobs
  *and* some master-section params at once. **0% = fully bypassed** (instant unprocessed
  A/B), 100% = all effects in. Fully automatable. Use it to A/B the whole patch in one move.
- **Signal flows LEFT→RIGHT** through the modules (Noise → Wobble → Distort → Digital →
  Space → Magnetic) — turn them on in that order.
- **Master section:** input gain; EQ with selectable **low-end cuts** (incl. a boosted
  resonant-peak option) and **high-end cuts** (a steeper curve option); a **Tone** option
  (boost highs / tuck highs+boost lows); and a **Width** control for stereo spread.
- **Start from INIT preset** (everything zeroed/off) to learn or build from scratch — the
  modules grey out until enabled.

**Flux (per-module):** "Not a dry/wet of anything — it controls parameters *under the hood*
we can't reach on the UI. Adds organic, non-linear fluctuations customized per module."
Great for the *end* of sound-design or when fast-auditioning presets; high Flux = randomized
volume/dropouts; zero Flux = dead-consistent. **Mess with Flux on every module.**

### Noise
Preset noise types (vinyl crackle, hiss, etc.) — click the title to browse. Won't be heard if
the big knob is down. **Tone** = overall brightness (emphasize highs vs lows). **POST**
routes the noise *after the master section*. **Follow** = noise tracks the input (comes in
with the piano, decays with its gain). **Duck** = inverse — noise gets *out of the way* of
the source ("sounds really great on drums").

### Wobble
Most important param = the **Wow↔Flutter slider**. Wow = slower pitch mod (rate down to
~4 Hz feels slow); Flutter = faster (slowest ~600 / fast). Blend between the two — "I love
closer to the Wow side." **Stereo** separates Wow and Flutter between L/R. **Trick:** lower
the **Mix** knob (Mix = unprocessed vs processed) to ~50% with Stereo on → a **chorus effect**.

### Distort
Six distortion types + a **frequency Focus** param (target where distortion applies — "not
the too-low end; some low-mids and highs") + a dry/wet Mix. "Sound quality is phenomenal."
Flux adds random volume/distortion-amount fluctuation.

### Digital
Sample-rate + bit-depth reduction on one slider (top). **Frequency** param (left) = where to
crush ("add crystal-like crunch to the top"). **Smooth** = softens the curves (gentler
crush). Drag the **Rate↔Bit** slider: rate-side = sample-rate crush; bit-side = bit-depth
reduction = "a full wall of really harsh noise." **Cut** option on the frequency slider cuts
frequencies *outside* the range (vs focusing on it). Flux randomizes rate+bits (visible up top).

### Space
Reverb/resonator. **Decay** (top) = tail length. **Focus** (left) = which frequencies get
the verb (e.g. top-end only). **Pre-delay** = gap before the reverb. **Stereo** on by default.

### Magnetic
Tape-machine quirks. **Wear↔Flutter** knob (top): Wear = "how many times you've played it"
(volume fluctuations); Flutter = faster artifact from the tape pin/capstan. **Stereo** toggle.
**Rate** of flutter (right) = 6 Hz–30 Hz. **Dropout** = like Wear but more random — drops the
volume out.

### Combining / bus use
Modules are *meant to be combined and balanced*. Closing demo: builds a patch on piano
(noise type, gentle duck/flux, wobble, a touch of distortion, digital, space, magnetic, then
EQ low-cut), then A/Bs the whole thing with the Magnitude slider. Final example puts **one
RC-20 across a GROUP/BUS of melodic instruments** — confirmed bus-glue use.

---

## Cleaned transcript

hey everybody it's nick — retro color 20 by xln audio (rc20), a comprehensive walkthrough of
this multi-effects plug-in. The UI is broken into four main sections: the top section, the
effects modules, the big knobs, and the master section. The top section is where you choose
presets and slide the global magnitude — one of the most important parameters in rc20. The
magnitude slider controls all of the big knobs as well as some master-section parameters; at
0% it's bypassed so you can quickly hear unprocessed audio, at 100% all the effects are
kicking in. Below the top section are the effects modules. Below those are the big knobs which
control the amount of each effect (0 = bypassed; you can also toggle each on individually with
the button top-left of each knob). Last is the master section with dynamic and eq controls:
input gain, an eq with different cuts on the low end (one has a boosted resonant peak),
different cuts on the high end (a steeper curve option), a tone option (boost the high, or
tuck the high and boost the low), and a width section for stereo width.

To test the plug-in, load the init preset (defaults, everything zero/off) — the modules grey
out until turned on. Going left to right (how audio flows in rc20): turn the noise on first.
rc20 has preset noises — click the vinyl title to browse them. Even with it on, if the big
knob is down you won't hear the noise. The tone knob is overall brightness (emphasize higher
vs lower frequencies). You can route the noise POST master so it comes after the master
section. The follow parameter follows the input signal — if the piano comes in, the noise
comes in and decays with the piano gain. Duck is almost the inverse: it gets out of the way of
the piano — duck sounds really great on drums. All modules have a flux parameter; it's not a
dry/wet — it controls parameters under the hood we can't control on the UI (straight from the
manual: it adds organic, non-linear fluctuations customized for each module). Good to use at
the end of the process or when going through presets quickly — high flux gives randomized
volume and dropouts; without flux it's very consistent.

Next the wobble module — a powerful one. The most important parameter is the wow-to-flutter
slider. Wow is a slower pitch modulation; you control the rate of the wow below it (4 hertz is
still not that fast) versus 100% flutter (slowest 600, really fast). Blend between the two — I
love closer to the wow side. Moving toward flutter mixes the modulation. Stereo separates the
wow and flutter between left and right channels. A cool trick: the mix knob is unprocessed vs
processed audio — set it to ~50% with stereo on and you get a chorus effect.

The distort module — one of my favorites — six distortion types, a frequency parameter to
focus where the distortion applies, and a dry/wet. Simple but very effective; the sound
quality is phenomenal. It's really effective when you focus it on a specific frequency (not
the too-low end; some low-mids, and the high end). Flux adds random volume/distortion-amount
fluctuation.

The digital module simulates technologies through the years via sample rate and bit depth on
the top slider, plus a frequency parameter on the left to control where to crush. Add a little
crystal-like crunch to the top with the frequency slider. The smooth parameter smooths the
curves for a softer result. Drag the rate-to-bit slider: rate-side crushes sample rate;
bit-side is bit-depth reduction — really a full wall of harsh noise. There's a cut option on
the frequency slider to cut frequencies outside the range (vs focus on it). Flux randomizes
rate and bits (visible up top). A fun way to make something 8-bit very quickly.

The space module is a reverb/resonator. The decay at the top is the length of the
reverb/resonator tail. The focus slider on the left sets which frequencies to focus (top-end
only vs full spectrum). Pre-delay puts space before the reverb starts. Stereo on by default.
You wouldn't normally put a lot of reverb on the bass.

The magnetic module simulates the quirky stuff when you record to tape: the wear-to-flutter
knob at top (wear = how many times you've played it → inconsistent volume fluctuations;
flutter = a faster artifact caused by the pin of the tape mechanism), a stereo option, the
rate of the flutter on the right (6 to 30 hertz), and a dropout parameter (like wear but more
random — drops the volume out).

Those are the modules — they're meant to be combined and balanced. On the piano: start with
noise (find a type, not too much ducking or flux), introduce wobble, take down the (too-much)
distortion, add digital, add space (nice on piano), add magnetic, turn on the eq with a little
low cut, then A/B with the magnitude slider. Lastly, a work-in-progress with rc20 on a group
of melodic instruments — a good way to use rc20 on a group or bus of tracks.
