#!/usr/bin/env python3
"""Build ../audition.html: the self-contained listening page for the 15 cues.

Embeds every prototype WAV as a base64 data URI so the page works anywhere —
double-click it locally, or publish it as an artifact. Re-run after
render_prototypes.py whenever the sounds change.
"""

import base64
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "audition_template.html")
OUT = os.path.join(HERE, "..", "audition.html")

with open(os.path.join(HERE, "manifest.json")) as f:
    manifest = json.load(f)

sounds = {}
for cue in manifest["cues"]:
    with open(os.path.join(HERE, cue["file"]), "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    sounds[cue["id"]] = "data:audio/wav;base64," + b64

with open(TEMPLATE) as f:
    html = f.read()

html = html.replace("/*__SOUNDS__*/", "const SOUNDS = " + json.dumps(sounds) + ";")

with open(OUT, "w") as f:
    f.write(html)

print(f"wrote {os.path.abspath(OUT)} ({os.path.getsize(OUT)//1024} KB)")
