#!/usr/bin/env python3
"""Render the telecom sample crate: sampler-ready one-shots and beds built from
first principles - real DTMF pairs, Bell System call-progress tones, Morse, a
full modem-handshake miniature, POST beeps, CRT degauss, RTTY, static beds.
All original synthesis (lane 1: shippable, sampleable, yours).

Writes 48 kHz / 16-bit mono WAVs to ../sample-crate/. Pure stdlib.
"""

import math
import os
import random
import struct
import wave

from render_prototypes import SR, steady, pop, tone, mix

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sample-crate")
os.makedirs(OUT, exist_ok=True)


def noise(dur, brightness=0.5, amp=1.0, seed=1):
    """Sustained one-pole-filtered noise (pop() decays; this holds level)."""
    rng = random.Random(seed)
    n = int(dur * SR)
    out, y = [], 0.0
    for _ in range(n):
        y += brightness * (rng.uniform(-1, 1) - y)
        out.append(y * amp)
    return out


def shape(buf, fade_in=0.005, fade_out=0.02, decay_tau=None):
    """Fades and optional exponential decay applied to a buffer."""
    n = len(buf)
    fi, fo = int(fade_in * SR), int(fade_out * SR)
    for i in range(min(fi, n)):
        buf[i] *= i / fi
    for i in range(min(fo, n)):
        buf[-1 - i] *= i / fo
    if decay_tau:
        buf = [s * math.exp(-(i / SR) / decay_tau) for i, s in enumerate(buf)]
    return buf


def write(name, buf, peak_db=-3.0):
    peak = max(1e-9, max(abs(s) for s in buf))
    g = (10 ** (peak_db / 20.0)) / peak
    path = os.path.join(OUT, name + ".wav")
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(b"".join(
            struct.pack("<h", max(-32767, min(32767, int(s * g * 32767))))
            for s in buf))
    print(f"  {name:<24} {len(buf)/SR:5.2f}s")


# --- DTMF: the real Bell frequencies ----------------------------------------
DTMF = {
    "1": (697, 1209), "2": (697, 1336), "3": (697, 1477),
    "4": (770, 1209), "5": (770, 1336), "6": (770, 1477),
    "7": (852, 1209), "8": (852, 1336), "9": (852, 1477),
    "star": (941, 1209), "0": (941, 1336), "hash": (941, 1477),
}
for key, (lo, hi) in DTMF.items():
    write("dtmf_" + key, steady([float(lo), float(hi)], 0.18), peak_db=-6.0)

# --- Call-progress tones (Bell System specs) ---------------------------------
write("dial_tone", steady([350.0, 440.0], 4.0), peak_db=-9.0)

busy = mix([(i * 1.0, steady([480.0, 620.0], 0.5)) for i in range(4)], 3.6)
write("busy_signal", busy, peak_db=-8.0)

ringback = mix([(0.0, steady([440.0, 480.0], 2.0)), (3.0, steady([440.0, 480.0], 2.0))], 5.2)
write("ringback", ringback, peak_db=-9.0)

sit = mix([(0.00, steady([985.2], 0.33)), (0.33, steady([1370.6], 0.33)),
           (0.66, steady([1776.7], 0.38))], 1.10)
write("sit_disconnected", sit, peak_db=-8.0)

howl = mix([(i * 0.2, steady([1400.0, 2060.0, 2450.0, 2600.0], 0.1)) for i in range(10)], 2.1)
write("offhook_howler", howl, peak_db=-6.0)

# --- Morse: "ARLO" at 20 wpm, 700 Hz ----------------------------------------
def morse(text, wpm=20, freq=700.0):
    dit = 1.2 / wpm
    code = {"A": ".-", "R": ".-.", "L": ".-..", "O": "---", "T": "-", "I": "..", "B": "-..."}
    ev, t = [], 0.0
    for ch in text:
        for sym in code[ch]:
            d = dit if sym == "." else 3 * dit
            ev.append((t, steady([freq], d, gain=0.9)))
            t += d + dit
        t += 2 * dit
    return mix(ev, t + 0.2)

write("morse_arlo", morse("ARLO"), peak_db=-7.0)
write("morse_tiobi", morse("TIOBI"), peak_db=-7.0)

# --- POST beeps --------------------------------------------------------------
write("post_ok", steady([880.0], 0.35), peak_db=-6.0)
post_err = mix([(i * 0.24, steady([880.0], 0.12)) for i in range(3)], 0.85)
write("post_error", post_err, peak_db=-6.0)

# --- The full modem handshake miniature (~8 s) -------------------------------
digits = [DTMF[d] for d in "5551234"]
hs = [(0.0, steady([350.0, 440.0], 1.1, gain=0.7))]                       # dial tone
t = 1.3
for lo, hi in digits:                                                     # dialing
    hs.append((t, steady([float(lo), float(hi)], 0.11, gain=0.8)))
    t += 0.19
hs.append((t + 0.2, steady([440.0, 480.0], 1.1, gain=0.6)))               # ringback
t += 1.6
hs.append((t, steady([2100.0], 0.9, gain=0.5)))                           # answer tone
t += 1.0
hs.append((t, tone(1800.0, 0.25, "soft", tau=0.5, attack=0.01, gain=0.6,
                   glide_from=600.0, glide_time=0.2)))                    # carrier chirp
hs.append((t + 0.3, tone(2400.0, 0.25, "soft", tau=0.5, attack=0.01, gain=0.5,
                         glide_from=1200.0, glide_time=0.2)))
t += 0.7
hs.append((t, shape(noise(1.6, 0.65, 0.5, seed=51), decay_tau=None)))     # data roar
hs.append((t + 0.2, steady([1650.0], 0.5, gain=0.15)))                    # tones in the roar
hs.append((t + 0.9, steady([980.0], 0.4, gain=0.15)))
t += 1.8
hs.append((t, steady([587.33, 1174.66], 0.5, gain=0.9)))                  # lock: D octave
write("modem_handshake", mix(hs, t + 0.7), peak_db=-5.0)

# --- Machinery & radio -------------------------------------------------------
crt = mix([
    (0.00, shape(noise(0.10, 0.15, 1.0, seed=61), decay_tau=0.04)),       # thump
    (0.02, shape(steady([55.0], 0.5, gain=0.8), decay_tau=0.15)),         # bwoom
    (0.10, shape(steady([15734.0], 2.2, gain=0.25), decay_tau=0.8)),      # line whine
], 2.4)
write("crt_degauss", crt, peak_db=-8.0)

sw = noise(6.0, 0.35, 0.8, seed=71)
het = steady([1000.0], 6.0, gain=0.1)
wob = [s * (0.6 + 0.4 * math.sin(2 * math.pi * 0.23 * i / SR)) for i, s in enumerate(sw)]
write("shortwave_bed", shape([a + b for a, b in zip(wob, het)], fade_out=0.4), peak_db=-12.0)

sq = mix([(0.0, pop(0.12, 0.85, 1.0, seed=81)),
          (0.5, pop(0.09, 0.9, 0.8, seed=83)),
          (1.0, pop(0.15, 0.8, 0.9, seed=87))], 1.4)
write("squelch_bursts", sq, peak_db=-7.0)

rtty = mix([(i * 0.022, steady([2125.0 if i % 2 else 2295.0], 0.022, attack=0.001))
            for i in range(90)], 2.2)
write("rtty_burst", rtty, peak_db=-9.0)

dm = mix([(i * 0.03, pop(0.02, 0.9, 1.0, seed=90 + (i % 7))) for i in range(66)]
         + [(0.0, steady([118.0], 2.0, gain=0.12))], 2.2)
write("dot_matrix", dm, peak_db=-7.0)

rng = random.Random(99)
hdd_t, hdd = 0.0, []
while hdd_t < 1.5:
    hdd.append((hdd_t, pop(0.015, 0.7, rng.uniform(0.5, 1.0), seed=int(hdd_t * 1000) + 7)))
    hdd_t += rng.choice([0.02, 0.03, 0.05, 0.11])
write("hdd_seek", mix(hdd, 1.7), peak_db=-9.0)

print(f"\ncrate written to {os.path.abspath(OUT)}")
