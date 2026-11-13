#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-01.

The competition asks for a single image that sums up the world news of
Friday, 13 November 2026 for a vision judge who has no news feed, so the
entry is a finished front page: an editorial collage of the day's six big
stories under a newspaper masthead, composed ahead of time and shipped
beside this file as art.png.

This program is the delivery mechanism. It copies art.png byte-for-byte
to entry.png inside the output directory named by the MAKEFUN_OUTPUT_DIR
environment variable (default /output), creating that directory when it
does not exist yet. Nothing is re-encoded, so the judged pixels are
exactly the ones committed to the repository.

Python 3 standard library only; no network access. Exits 1 with a clear
message on stderr when the bundled artwork is missing.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, "art.png")


def copy_artwork(source, dest_dir):
    """Copy the bundled artwork into dest_dir as entry.png."""
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(dest_dir, "entry.png"))


def main():
    if not os.path.isfile(ART):
        print(f"error: bundled artwork not found: {ART}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    copy_artwork(ART, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
