# news-summary-01 entry (Python 3.13, standard library only).
# Copies the summary in summary.txt to /output/entry.txt.
# Deterministic: same input bytes produce the same output bytes on every run.
# No network, no randomness, no environment dependence.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# Read and write as text with explicit UTF-8 and no newline translation,
# so the output bytes are exactly the summary's bytes on any platform.
text = (HERE / "summary.txt").read_text(encoding="utf-8")
OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(text, encoding="utf-8", newline="")
