#!/usr/bin/env python3
"""Write tiobi-cues.mid: every Tiobi cue as MIDI, one cue every 2 bars at 120 BPM,
with a marker naming each cue. Drop it on a Logic software-instrument track and
bounce cue by cue. space-complete carries its pitch-bend droop (set bend range ±2).
Pure stdlib."""

import struct, os

TPQ = 480                     # ticks per quarter; 120 BPM -> 1 s = 960 ticks
BAR = 4 * TPQ
GAP = 2 * BAR                 # one cue every 2 bars

def s2t(sec): return int(round(sec * 960))

# (name, [(offset_s, midi_note, velocity), ...])
CUES = [
    ("ping",           [(0, 81, 100)]),
    ("mention",        [(0, 74, 90), (0.11, 81, 105)]),
    ("message-in",     [(0, 76, 70), (0.09, 78, 85)]),
    ("message-out",    [(0, 78, 75), (0.08, 74, 60)]),
    ("question",       [(0, 74, 90), (0.12, 78, 90), (0.24, 83, 105)]),
    ("done",           [(0, 81, 95), (0.12, 74, 100)]),
    ("done-big",       [(0, 74, 95), (0.11, 81, 95), (0.22, 86, 105), (0.22, 90, 40), (0.30, 62, 50)]),
    ("error",          [(0, 62, 85), (0.012, 63, 60)]),
    ("warning",        [(0, 65, 80)]),
    ("start",          [(0, 69, 60), (0.06, 74, 95), (0.10, 86, 40)]),
    ("progress",       [(0, 86, 70)]),
    ("connect",        [(0, 74, 90), (0.11, 86, 95)]),
    ("disconnect",     [(0, 86, 75), (0.10, 74, 85)]),
    ("approve",        [(0, 78, 95), (0.07, 81, 100)]),
    ("deny",           [(0, 69, 80), (0.10, 65, 75)]),
    ("published",      [(0, 86, 95)]),
    ("signed-off",     [(0, 81, 70), (0.10, 86, 105)]),
    ("phase-advance",  [(0, 81, 70), (0.09, 86, 100), (0.23, 88, 60), (0.32, 90, 105), (0.32, 74, 40)]),
    ("space-complete", [(0, 74, 90)]),          # droop added via pitch bend below
    ("fireworks",      [(0, 62, 60), (0.05, 74, 80), (0.30, 86, 100), (0.42, 90, 80), (0.55, 93, 70)]),
]

NOTE_LEN = s2t(0.30)

def vlq(n):
    out = [n & 0x7F]
    while n >> 7:
        n >>= 7
        out.append((n & 0x7F) | 0x80)
    return bytes(reversed(out))

events = []  # (tick, order, bytes)
events.append((0, 0, b"\xFF\x51\x03" + (500000).to_bytes(3, "big")))     # 120 BPM
events.append((0, 0, b"\xFF\x58\x04\x04\x02\x18\x08"))                   # 4/4

for i, (name, notes) in enumerate(CUES):
    base = i * GAP
    events.append((base, 0, b"\xFF\x06" + vlq(len(name)) + name.encode()))
    for off, note, vel in notes:
        t = base + s2t(off)
        events.append((t, 1, bytes([0x90, note, vel])))
        events.append((t + NOTE_LEN, 2, bytes([0x80, note, 0])))
    if name == "space-complete":
        # droop 2 semitones over 0.4 s (patch bend range +/-2), then recenter
        for k in range(9):
            bend = 8192 - int(8191 * k / 8)
            events.append((base + s2t(0.05 + 0.05 * k), 1,
                           bytes([0xE0, bend & 0x7F, (bend >> 7) & 0x7F])))
        events.append((base + s2t(0.9), 2, bytes([0xE0, 0x00, 0x40])))

events.sort(key=lambda e: (e[0], e[1]))
track, last = bytearray(), 0
for tick, _, data in events:
    track += vlq(tick - last) + data
    last = tick
track += vlq(GAP) + b"\xFF\x2F\x00"

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tiobi-cues.mid")
with open(out, "wb") as f:
    f.write(b"MThd" + struct.pack(">IHHH", 6, 0, 1, TPQ))
    f.write(b"MTrk" + struct.pack(">I", len(track)) + track)
print(f"wrote {out} ({len(CUES)} cues, one every 2 bars at 120 BPM)")
