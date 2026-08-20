#!/usr/bin/env python3
"""Render the 15 AI-harness prototype sounds as 48 kHz / 16-bit mono WAVs.

Pure standard library — runs anywhere (`python3 render_prototypes.py`).
These are design prototypes: they nail the pitch grammar, timing, and envelope
of each cue so the family can be auditioned in context. The production pass
(see ../03-Production-Plan.md) re-voices them with real instruments.

Family voice: a warm struck-bell/kalimba hybrid — sine partials with fast
exponential decay, a quiet felt-strike transient, and a +4 cent ghost voice
for organic shimmer. Everything lives in D major pentatonic except `error`,
which is allowed the one dissonance in the palette (a low minor second).

Semantic grammar (matches the spec in ../02-Sound-Spec.md):
  rising interval  = incoming / needs attention
  falling, resolving = completion / outgoing
  octave up / down = session connect / disconnect
  low + damped     = something went wrong (never harsh, never loud)
"""

import json
import math
import os
import random
import struct
import wave

SR = 48000
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# D major pentatonic + the few outsiders the grammar needs
N = {
    "D3": 146.83, "E3": 164.81, "F3": 174.61, "A3": 220.00,
    "D4": 293.66, "Eb4": 311.13, "E4": 329.63, "F4": 349.23, "F#4": 369.99,
    "A4": 440.00, "B4": 493.88,
    "D5": 587.33, "E5": 659.25, "F#5": 739.99, "A5": 880.00, "B5": 987.77,
    "D6": 1174.66, "E6": 1318.51, "F#6": 1479.98, "A6": 1760.00,
}

# timbre name -> list of (partial ratio, relative amp, decay scale)
TIMBRES = {
    # the family voice: bell-kalimba hybrid, bright but round
    "bell":  [(1.0, 1.00, 1.00), (2.001, 0.32, 0.55), (3.008, 0.11, 0.32),
              (4.16, 0.05, 0.22), (6.27, 0.02, 0.15)],
    # softer, woodier — for outgoing / ambient cues
    "soft":  [(1.0, 1.00, 1.00), (2.0, 0.18, 0.45), (3.99, 0.06, 0.25)],
    # dark and damped — for error / warning / deny
    "dark":  [(1.0, 1.00, 1.00), (1.995, 0.38, 0.60), (2.91, 0.14, 0.35)],
}


def strike(dur=0.006, brightness=0.35, amp=0.045, seed=1):
    """A tiny felt-mallet transient: one-pole-filtered noise burst."""
    rng = random.Random(seed)
    n = int(dur * SR)
    out, y = [], 0.0
    for i in range(n):
        y += brightness * (rng.uniform(-1, 1) - y)
        out.append(y * amp * (1.0 - i / n))
    return out


def pop(dur=0.14, brightness=0.5, amp=0.8, seed=7):
    """A firework crackle: filtered noise burst with an exponential decay."""
    rng = random.Random(seed)
    n = int(dur * SR)
    out, y = [], 0.0
    for i in range(n):
        y += brightness * (rng.uniform(-1, 1) - y)
        out.append(y * amp * math.exp(-(i / SR) / (dur * 0.28)))
    return out


def tone(freq, dur, timbre="bell", gain=1.0, attack=0.004, tau=0.22,
         detune_cents=4.0, vibrato=None, glide_from=None, glide_time=0.06,
         seed=1):
    """One struck note. Returns a list of float samples of length dur*SR.

    vibrato: (rate_hz, depth_fraction) or None.
    glide_from: start frequency for a quick pitch sweep into the note.
    """
    n = int(dur * SR)
    partials = TIMBRES[timbre]
    voices = [(1.0, 1.0), (2 ** (detune_cents / 1200.0), 0.35)]  # main + ghost
    out = [0.0] * n
    for vmul, vamp in voices:
        phase = [0.0] * len(partials)
        for i in range(n):
            t = i / SR
            f = freq
            if glide_from is not None and t < glide_time:
                k = t / glide_time
                f = glide_from * (freq / glide_from) ** k
            if vibrato:
                f *= 1.0 + vibrato[1] * math.sin(2 * math.pi * vibrato[0] * t)
            env_a = min(1.0, t / attack) if attack > 0 else 1.0
            s = 0.0
            for pi, (ratio, amp, dscale) in enumerate(partials):
                phase[pi] += 2 * math.pi * f * ratio * vmul / SR
                s += amp * math.exp(-t / (tau * dscale)) * math.sin(phase[pi])
            out[i] += vamp * env_a * s
    # normalize voice sum, apply gain, add the strike transient
    out = [x * gain / 1.35 for x in out]
    for i, s in enumerate(strike(seed=seed)):
        if i < n:
            out[i] += s * gain
    return out


def mix(events, total_dur):
    """events: list of (start_seconds, sample_list). Sum onto one buffer."""
    buf = [0.0] * int(total_dur * SR)
    for start, samples in events:
        o = int(start * SR)
        for i, s in enumerate(samples):
            j = o + i
            if j < len(buf):
                buf[j] += s
    return buf


def finish(buf, peak_db=-3.0, fade_ms=12):
    """Normalize to peak_db and apply a declick fade at the tail."""
    peak = max(1e-9, max(abs(s) for s in buf))
    g = (10 ** (peak_db / 20.0)) / peak
    buf = [s * g for s in buf]
    nf = int(fade_ms / 1000.0 * SR)
    for i in range(nf):
        buf[-1 - i] *= i / nf
    return buf


def write_wav(name, buf):
    path = os.path.join(OUT_DIR, name + ".wav")
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        frames = bytearray()
        for s in buf:
            frames += struct.pack("<h", max(-32767, min(32767, int(s * 32767))))
        w.writeframes(bytes(frames))
    return path


# ---------------------------------------------------------------------------
# The 15 cues. Each entry: (filename, peak_dB, builder, description)
# Relative levels are part of the design: attention cues sit at -3 dB peak,
# ambient cues at -9 to -12, error/warning deliberately no louder than a ping.
# ---------------------------------------------------------------------------

def s_ping():
    return mix([(0.0, tone(N["A5"], 0.40, "bell", tau=0.16))], 0.42)

def s_mention():
    return mix([
        (0.00, tone(N["D5"], 0.30, "bell", tau=0.12)),
        (0.11, tone(N["A5"], 0.42, "bell", tau=0.18)),
    ], 0.55)

def s_message_in():
    return mix([
        (0.00, tone(N["E5"], 0.25, "soft", tau=0.10, gain=0.8)),
        (0.09, tone(N["F#5"], 0.34, "soft", tau=0.14)),
    ], 0.45)

def s_message_out():
    return mix([
        (0.00, tone(N["F#5"], 0.20, "soft", tau=0.08)),
        (0.08, tone(N["D5"], 0.30, "soft", tau=0.12, gain=0.75)),
    ], 0.40)

def s_question():
    return mix([
        (0.00, tone(N["D5"], 0.28, "bell", tau=0.11)),
        (0.12, tone(N["F#5"], 0.28, "bell", tau=0.11, gain=0.9)),
        (0.24, tone(N["B5"], 0.44, "bell", tau=0.20)),  # ends unresolved
    ], 0.70)

def s_done():
    return mix([
        (0.00, tone(N["A5"], 0.26, "bell", tau=0.11)),
        (0.12, tone(N["D5"], 0.55, "bell", tau=0.26)),  # settles home
    ], 0.70)

def s_done_big():
    return mix([
        (0.00, tone(N["D5"], 0.30, "bell", tau=0.13)),
        (0.11, tone(N["A5"], 0.30, "bell", tau=0.14, gain=0.9)),
        (0.22, tone(N["D6"], 0.55, "bell", tau=0.28, gain=0.95)),
        (0.22, tone(N["F#6"], 0.45, "bell", tau=0.18, gain=0.22)),  # sparkle
        (0.30, tone(N["D4"], 0.55, "soft", tau=0.30, gain=0.35)),   # warm floor
    ], 0.90)

def s_error():
    return mix([
        (0.000, tone(N["D4"], 0.45, "dark", tau=0.14)),
        (0.012, tone(N["Eb4"], 0.40, "dark", tau=0.11, gain=0.55)),  # rub
    ], 0.50)

def s_warning():
    return mix([
        (0.0, tone(N["F4"], 0.42, "dark", tau=0.16, vibrato=(5.5, 0.008))),
    ], 0.46)

def s_start():
    return mix([
        (0.00, tone(N["D5"], 0.34, "bell", tau=0.15, glide_from=N["A4"])),
        (0.10, tone(N["D6"], 0.30, "bell", tau=0.12, gain=0.30)),  # lift
    ], 0.46)

def s_progress():
    return mix([(0.0, tone(N["D6"], 0.10, "soft", tau=0.030, gain=0.9))], 0.13)

def s_connect():
    return mix([
        (0.00, tone(N["D5"], 0.26, "bell", tau=0.11)),
        (0.11, tone(N["D6"], 0.40, "bell", tau=0.18, gain=0.85)),
    ], 0.55)

def s_disconnect():
    return mix([
        (0.00, tone(N["D6"], 0.22, "soft", tau=0.09, gain=0.8)),
        (0.10, tone(N["D5"], 0.38, "soft", tau=0.16, gain=0.9)),
    ], 0.52)

def s_approve():
    return mix([
        (0.00, tone(N["F#5"], 0.20, "bell", tau=0.09)),
        (0.07, tone(N["A5"], 0.32, "bell", tau=0.14)),
    ], 0.42)

def s_deny():
    return mix([
        (0.00, tone(N["A4"], 0.24, "dark", tau=0.10)),
        (0.10, tone(N["F4"], 0.34, "dark", tau=0.14, gain=0.85)),
    ], 0.48)


# --- The milestone "da-ding" family -----------------------------------------
# Same voice, and the syllable count scales with the size of the milestone:
# ding < da-DING < da-DING-a-LING. space-complete is the one sad ding —
# a single bell that droops a minor third as it decays.

def s_published():
    return mix([(0.0, tone(N["D6"], 0.38, "bell", tau=0.15))], 0.40)

def s_signed_off():
    return mix([
        (0.00, tone(N["A5"], 0.14, "bell", tau=0.06, gain=0.6)),   # da
        (0.10, tone(N["D6"], 0.46, "bell", tau=0.20)),             # DING
    ], 0.60)

def s_phase_advance():
    return mix([
        (0.00, tone(N["A5"], 0.12, "bell", tau=0.05, gain=0.55)),  # da
        (0.09, tone(N["D6"], 0.30, "bell", tau=0.13)),             # DING
        (0.23, tone(N["E6"], 0.12, "bell", tau=0.05, gain=0.5)),   # a
        (0.32, tone(N["F#6"], 0.50, "bell", tau=0.22, gain=0.9)),  # LING
        (0.32, tone(N["D5"], 0.45, "soft", tau=0.25, gain=0.30)),  # warm floor
    ], 0.85)

def s_space_complete():
    return mix([
        (0.0, tone(N["B4"], 0.62, "bell", tau=0.24,
                   glide_from=N["D5"], glide_time=0.30)),
    ], 0.66)

def s_fireworks():
    # Hero cue: launch riser, burst, crackle, pentatonic sparkle falling as embers
    return mix([
        (0.00, tone(N["D5"], 0.28, "soft", tau=0.10, gain=0.5,
                    glide_from=N["D4"], glide_time=0.24)),          # launch
        (0.26, pop(0.18, 0.50, 0.90, seed=7)),                      # burst
        (0.30, tone(N["D6"], 0.42, "bell", tau=0.16, gain=0.80)),
        (0.38, pop(0.12, 0.35, 0.50, seed=11)),
        (0.42, tone(N["F#6"], 0.36, "bell", tau=0.13, gain=0.55)),
        (0.50, pop(0.10, 0.60, 0.35, seed=13)),
        (0.55, tone(N["A6"], 0.46, "bell", tau=0.18, gain=0.45)),
        (0.63, pop(0.14, 0.30, 0.28, seed=17)),
        (0.72, pop(0.09, 0.70, 0.18, seed=19)),
    ], 1.15)


# --- The Declan (in-house family, never ships) ------------------------------
# Caricatures by design: party-popper salvo, two ominous low notes, a passing
# two-tone siren with doppler drop, and a flush. All synthesized from scratch.

def s_declan_approve():
    ev = []
    for i, t in enumerate([0.00, 0.09, 0.16, 0.26, 0.33, 0.45, 0.55]):
        ev.append((t, pop(0.10 + 0.02 * (i % 3), 0.55 + 0.05 * (i % 4),
                          0.9 - 0.07 * i, seed=23 + i)))
    ev.append((0.30, tone(N["D6"], 0.30, "bell", tau=0.10, gain=0.25)))  # confetti glint
    return mix(ev, 0.85)

def s_declan_mention():
    return mix([
        (0.00, tone(N["E3"], 0.45, "dark", tau=0.20)),
        (0.42, tone(N["F3"], 0.60, "dark", tau=0.22)),
    ], 1.05)

def s_declan_error():
    ev, t = [], 0.0
    for i in range(4):
        shift = 1.0 - 0.05 * i                      # the truck drives past
        g = [0.5, 0.9, 0.7, 0.45][i]
        ev.append((t,        tone(940.0 * shift, 0.16, "soft", tau=0.30, attack=0.02, gain=g)))
        ev.append((t + 0.16, tone(700.0 * shift, 0.16, "soft", tau=0.30, attack=0.02, gain=g)))
        t += 0.32
    return mix(ev, 1.45)

def s_declan_merge():
    return mix([
        (0.00, pop(0.55, 0.10, 0.70, seed=31)),                       # whoosh bed
        (0.05, tone(N["D4"], 0.16, "soft", tau=0.06, gain=0.60,
                    glide_from=N["A4"], glide_time=0.12)),
        (0.22, tone(N["A3"], 0.16, "soft", tau=0.06, gain=0.55,
                    glide_from=N["D4"], glide_time=0.12)),
        (0.40, tone(N["D3"], 0.30, "soft", tau=0.10, gain=0.50,
                    glide_from=N["A3"], glide_time=0.20)),
        (0.55, pop(0.45, 0.05, 0.40, seed=37)),                       # drain tail
    ], 1.10)


def family_of(name):
    if name.startswith("declan-"):
        return "declan"
    if name in ("published", "signed-off", "phase-advance", "space-complete"):
        return "milestone"
    if name == "fireworks":
        return "hero"
    return "core"


CUES = [
    ("ping",        -3.0, s_ping,        "Generic notification. Single bright A5; neutral, glanceable."),
    ("mention",     -3.0, s_mention,     "You were named directly. Rising fifth D5>A5 - more insistent than ping."),
    ("message-in",  -6.0, s_message_in,  "Incoming message, ambient. Gentle E5>F#5 step up."),
    ("message-out", -9.0, s_message_out, "Message sent. Quick falling step - outgoing, no attention needed."),
    ("question",    -3.0, s_question,    "The agent needs your input. Three rising notes ending unresolved on B5."),
    ("done",        -4.0, s_done,        "Task complete. A5 resolving down to home D5 - closure."),
    ("done-big",    -3.0, s_done_big,    "Long-running job finished. D-A-D octave flourish with a warm low floor."),
    ("error",       -6.0, s_error,       "Something failed. Low damped D4 with a minor-second rub. Dark, never loud."),
    ("warning",     -7.0, s_warning,     "Caution, non-fatal. Single muted F4 with slow vibrato."),
    ("start",       -6.0, s_start,       "Task/agent kicked off. Upward glide into D5 with an octave lift."),
    ("progress",   -12.0, s_progress,    "Milestone tick. Tiny wooden D6 blip - felt more than heard."),
    ("connect",     -6.0, s_connect,     "Session/agent connected. Octave up, D5>D6."),
    ("disconnect",  -8.0, s_disconnect,  "Session ended. The same octave, coming down."),
    ("approve",     -4.0, s_approve,     "Permission granted / confirmed. Quick bright F#5>A5."),
    ("deny",        -7.0, s_deny,        "Permission declined / cancelled. Soft low falling third - a no, not a slap."),
    ("published",     -4.0, s_published,      "Milestone: published. One short bright ding."),
    ("signed-off",    -3.0, s_signed_off,     "Milestone: signed off. Happy da-DING."),
    ("phase-advance", -3.0, s_phase_advance,  "Milestone: phase advancing. Joyful da-DING-a-LING, rising."),
    ("space-complete",-5.0, s_space_complete, "Milestone: space complete. A single ding that droops a minor third - wistful closure."),
    ("fireworks",     -3.0, s_fireworks,      "Hero cue for the rare big win. Launch, burst, crackle, pentatonic embers."),
    ("declan-approve", -3.0, s_declan_approve, "Declan: approve. Celebratory party-popper salvo with a confetti glint."),
    ("declan-mention", -5.0, s_declan_mention, "Declan: mention. Two ominous low semitone notes. Something approaches."),
    ("declan-error",   -5.0, s_declan_error,   "Declan: error. Two-tone siren doppler-dropping as the truck drives past."),
    ("declan-merge",   -4.0, s_declan_merge,   "Declan: merge. The flush - whoosh, three descending glugs, drain tail."),
]


def main():
    manifest = []
    for name, peak_db, builder, desc in CUES:
        buf = finish(builder(), peak_db=peak_db)
        path = write_wav(name, buf)
        manifest.append({
            "id": name,
            "family": family_of(name),
            "file": name + ".wav",
            "duration_s": round(len(buf) / SR, 3),
            "peak_dbfs": peak_db,
            "description": desc,
        })
        print(f"  {name:<12} {len(buf)/SR:.2f}s  peak {peak_db} dBFS  -> {os.path.basename(path)}")
    with open(os.path.join(OUT_DIR, "manifest.json"), "w") as f:
        json.dump({"sample_rate": SR, "bit_depth": 16, "channels": 1,
                   "cues": manifest}, f, indent=2)
    print(f"\n{len(CUES)} cues + manifest.json written to {OUT_DIR}")


if __name__ == "__main__":
    main()
