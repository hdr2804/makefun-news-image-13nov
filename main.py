#!/usr/bin/env python3
"""news-image-01 entry: emit the bundled front-page image as entry.png.

The entry is a single static artwork (art.png, shipped beside this file).
Running the program copies it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output), creating the output directory when needed.
Python 3 standard library only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "art.png")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(ART, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
