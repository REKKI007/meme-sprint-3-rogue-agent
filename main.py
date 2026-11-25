"""Meme Sprint 3 entry: copy the meme image to the output directory.

The image (entry.png, 1024x1024 PNG, 809880 bytes) sits beside this
program. The program copies it byte for byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output), so both runs write
identical bytes. Standard library only, no network, no randomness, no
model calls: the image was made once during the build and is shipped
as data.
"""

import os
import shutil
import struct
from pathlib import Path

ENTRY_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def png_size(path: Path) -> tuple:
    """Return (width, height) of a PNG from its IHDR chunk, stdlib only."""
    with open(path, "rb") as f:
        header = f.read(33)
    assert header[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    assert header[12:16] == b"IHDR", "entry.png has no IHDR chunk"
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / ENTRY_NAME
    # Fail loudly instead of writing an entry the gate would refuse:
    # the bounty gate takes a whole PNG of at most 1 MiB, 1024x1024.
    assert source.stat().st_size <= MAX_BYTES, "entry.png over 1 MiB"
    width, height = png_size(source)
    assert width <= MAX_SIDE and height <= MAX_SIDE, "entry.png over 1024x1024"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / OUTPUT_NAME
    shutil.copyfile(source, dest)
    # The copy must be byte-identical: the gate weighs the file the
    # program writes, so a short write must never pass silently.
    assert dest.stat().st_size == source.stat().st_size, "short copy"


if __name__ == "__main__":
    main()
