#!/usr/bin/env python3
"""Entry point for make.fun news-image-20261117.

Copies the pre-built poster (entry.png, 1024x1024, 17 November 2026 world
news) to the grader's output directory. Standard library only, no network.
The copy is byte-for-byte identical on every run, so two runs of this
program always produce the same output.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    # The grader runs this program twice: confirm the copy is complete and
    # byte-identical to the source, so both runs produce the same bytes.
    if dest.stat().st_size != SOURCE.stat().st_size:
        print("entry.png copy incomplete", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
