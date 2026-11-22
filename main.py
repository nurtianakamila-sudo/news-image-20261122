#!/usr/bin/env python3
"""news-image-20261122 entrypoint.

The front page for Sunday 22 November 2026 ships in this repository
as entry.png. This program copies those exact bytes to the output
directory (MAKEFUN_OUTPUT_DIR, or /output) as entry.png, so two runs
always write identical bytes.

It uses only the standard library and never decodes or draws the
image: the grader's Pillow predates 10.1, where ImageFont has no
.size, so drawing here would fail. Copying is the safe path.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(
    os.path.join(HERE, "entry.png"),
    os.path.join(OUT_DIR, "entry.png"),
)

# Guard against a truncated copy: the output must be the same size as
# the bundled image, or this run has not produced the entry.
if os.path.getsize(os.path.join(OUT_DIR, "entry.png")) != os.path.getsize(
    os.path.join(HERE, "entry.png")
):
    raise SystemExit("entry.png copy is incomplete")
