#!/usr/bin/env python3
"""Inline every generated image as a data: URI so index.html is one file.

index.src.html carries {{name}} tokens; each resolves to assets/gen/<name>.jpg.
Run assets_gen.py first if assets/gen is empty.
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
GEN = ROOT / "assets" / "gen"


def uri(name: str) -> str:
    data = (GEN / f"{name}.jpg").read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()


def main() -> None:
    src = (ROOT / "index.src.html").read_text()
    names = sorted(set(re.findall(r"\{\{(\w+)\}\}", src)))
    missing = [n for n in names if not (GEN / f"{n}.jpg").exists()]
    if missing:
        raise SystemExit(f"assets/gen missing: {missing} — run assets_gen.py")
    table = {n: uri(n) for n in names}
    out = re.sub(r"\{\{(\w+)\}\}", lambda m: table[m.group(1)], src)
    (ROOT / "index.html").write_text(out)
    print(f"index.html  {len(out) / 1024:.0f} KB  ({len(names)} images inlined)")


if __name__ == "__main__":
    main()
