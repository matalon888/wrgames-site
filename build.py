#!/usr/bin/env python3
"""Inline every game asset as a data: URI so index.html is one self-contained file.

Reads index.src.html, replaces {{key}} tokens with base64 JPEG data URIs built
from assets/, writes index.html. Re-runnable.
"""
import base64
import io
import pathlib
import re

from PIL import Image

ROOT = pathlib.Path(__file__).parent
ASSETS = ROOT / "assets"

# token -> (source file, target width, jpeg quality)
SHOTS = {
    "cd0": "ss_1494327881_0.jpg",
    "cd1": "ss_1494327881_1.jpg",
    "cd2": "ss_1494327881_2.jpg",
    "cd3": "ss_1494327881_3.jpg",
    "cd4": "ss_1494327881_4.jpg",
    "cd5": "ss_1494327881_5.jpg",
    "am0": "ss_1592988294_0.jpg",
    "am1": "ss_1592988294_1.jpg",
    "am2": "ss_1592988294_2.jpg",
    "am3": "ss_1592988294_3.jpg",
}
ICONS = {
    # the live store icons are both burning airliners (an ASO re-skin), which
    # reads as a bug on a two-title page — badge each card with its own game art
    "icon_cd": "badge_cd.jpg",
    "icon_am": "badge_am.jpg",
}


def encode(path: pathlib.Path, width: int, quality: int) -> str:
    im = Image.open(path).convert("RGB")
    h = round(im.height * width / im.width)
    im = im.resize((width, h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def main() -> None:
    table = {k: encode(ASSETS / v, 300, 70) for k, v in SHOTS.items()}
    table.update({k: encode(ASSETS / v, 144, 78) for k, v in ICONS.items()})

    src = (ROOT / "index.src.html").read_text()
    missing = {m for m in re.findall(r"\{\{(\w+)\}\}", src)} - set(table)
    if missing:
        raise SystemExit(f"no asset for token(s): {sorted(missing)}")
    out = re.sub(r"\{\{(\w+)\}\}", lambda m: table[m.group(1)], src)
    (ROOT / "index.html").write_text(out)
    print(f"index.html  {len(out) / 1024:.0f} KB  ({len(table)} assets inlined)")


if __name__ == "__main__":
    main()
