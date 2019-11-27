#!/usr/bin/env python3

import sys
import zipfile
from PIL import Image
from pathlib import Path

def add_resource_to_theme(zf, path, new_path):
    im = Image.open(path).convert("RGBA")

    # Convert to BGRA
    r, g, b, a = im.split()
    im = Image.merge("RGBA", (b, g, r, a))

    zf.writestr(new_path, im.tobytes())

if __name__ == "__main__":
    usage = "Usage: gen_theme.py <resources folder> <output theme.zip>"

    if len(sys.argv) < 3:
        print(usage)
        sys.exit(1)

    res_dir = Path(sys.argv[1])
    if not res_dir.is_dir():
        print(usage)
        sys.exit(1)

    theme_path = Path(sys.argv[2])
    if not theme_path.parent.exists():
        theme_path.parent.mkdir()

    with zipfile.ZipFile(theme_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in res_dir.iterdir():
            add_resource_to_theme(zf, p, f"{p.stem}.bin")