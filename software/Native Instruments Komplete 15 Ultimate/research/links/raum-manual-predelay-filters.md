https://native-instruments.com/ni-tech-manuals/raum-manual/en/predelay-and-filters
native-instruments.com · RAUM manual (Predelay & Filters) · n.d. (accessed 2026-06)

# RAUM — Predelay & Filters: the looper/comb/resonator engine (official manual)

This section is what turns RAUM from "a reverb" into the rig's resonator/comb/looper. It feeds
ALL three algorithms (and on Cosmic it IS the decay engine).

## Predelay
- **Range:** below 1 ms → 2 seconds.
- **Predelay Sync** (button): swaps ms for musical intervals, host-synced **up to four bars (64|4)**.
  Numerator + Denominator + Sync Mode (Straight / Triplet / etc.).

## Feedback — the creative core
- Turn right → echo effects (which then get processed by the chosen reverb algorithm).
- **Feedback = 100% → infinite delay repeats.** (This is the real "infinite Cosmic drone" path.)
- **Comb filter / resonator:** **low Predelay + high Feedback** → predelay acts as a comb filter
  adding a distinct *tonal/pitched* quality. Manual: *"Percussive input signals can be used for
  resonator sounds similar to physical modelling."* → pluck a banjo into it = tuned resonator.
- **Looper:** with Predelay Sync on (up to 4 bars) + Feedback 100% = a four-bar looper.
- **Built-in limiter / auto-overdub:** a limiter in the feedback path prevents runaway when high
  feedback meets loud input — "causing the input to duck the delay sound." (= input ducks the
  loop, so new playing sits on top; acts like auto-overdub. See Parker interview for "adaptive.")

## Filters (both sit IN the feedback/reverb path → shape every repeat progressively)
- **Low Cut** — low-shelf attenuation, **0 to −24 dB**, on both reverb + feedback.
- **High Cut** — high attenuation, **90 kHz → 1 kHz**, same path. Rolling High Cut down each pass
  = "analog-style echo" / dub-decay where repeats darken into the drone.

## Rig takeaways
- **Infinite drone (any algorithm):** Predelay short-to-medium, Feedback → 100%, hold a chord.
- **Tuned resonator on banjo/baritone:** very low Predelay (sub-ms→few ms), Feedback high; the
  predelay length sets the pitch (comb). Percussive pluck → physical-model-ish ring.
- **4-bar drone looper:** Predelay Sync ON @ up to 4 bars, Feedback 100%; play to overdub.
- **Dub decay:** Feedback high + High Cut swept down → repeats dissolve darker into the wall.
