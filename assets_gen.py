#!/usr/bin/env python3
"""Cut the site's imagery out of the real store screenshots.

Sources are the 900x1600 App Store shots in assets/src/. Everything the page
uses — landscape marquee tiles, the hero device, corner objects, case-study
stills — is a crop of actual gameplay, never stock. Writes assets/gen/*.jpg.
"""
import pathlib

from PIL import Image

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "assets" / "src"
GEN = ROOT / "assets" / "gen"

CD = "1494327881"   # Crash Delivery
AM = "1592988294"   # Airplane Crash Madness


def load(app: str, n: int) -> Image.Image:
    return Image.open(SRC / f"{app}_{n}.jpg").convert("RGB")


def band(app: str, n: int, top: int, size=(840, 540)) -> Image.Image:
    """Landscape slice through the gameplay, clear of the store banners."""
    im = load(app, n)
    h = round(im.width * size[1] / size[0])
    top = max(0, min(top, im.height - h))
    return im.crop((0, top, im.width, top + h)).resize(size, Image.LANCZOS)


def tall(app: str, n: int, top: int, size=(640, 900)) -> Image.Image:
    im = load(app, n)
    h = round(im.width * size[1] / size[0])
    top = max(0, min(top, im.height - h))
    return im.crop((0, top, im.width, top + h)).resize(size, Image.LANCZOS)


def square(app: str, n: int, box, size=320) -> Image.Image:
    return load(app, n).crop(box).resize((size, size), Image.LANCZOS)


def portrait(app: str, n: int, size=(520, 924)) -> Image.Image:
    return load(app, n).resize(size, Image.LANCZOS)


PLAN = {
    # marquee, row one then row two
    "t0": (band(CD, 0, 420), 72),
    "t1": (band(CD, 2, 520), 72),
    "t2": (band(AM, 1, 380), 72),
    "t3": (band(CD, 4, 480), 72),
    "t4": (band(AM, 0, 300), 72),
    "t5": (band(CD, 5, 360), 72),
    "t6": (band(AM, 2, 400), 72),
    "t7": (band(CD, 1, 460), 72),
    "t8": (band(AM, 3, 420), 72),
    "t9": (band(CD, 3, 300), 72),
    # hero device
    "hero": (portrait(CD, 0), 78),
    # floating objects in the corners of the manifesto
    "d0": (square(CD, 0, (240, 780, 700, 1240)), 80),
    "d1": (square(AM, 1, (180, 700, 720, 1240)), 80),
    "d2": (square(CD, 2, (200, 640, 700, 1140)), 80),
    "d3": (square(CD, 3, (170, 380, 730, 940)), 80),
    # case studies
    "c1a": (band(CD, 5, 340, (900, 520)), 72),
    "c1b": (band(CD, 4, 470, (900, 700)), 72),
    "c1c": (tall(CD, 2, 334), 74),
    "c2a": (band(AM, 0, 300, (900, 520)), 72),
    "c2b": (band(AM, 3, 400, (900, 700)), 72),
    "c2c": (tall(AM, 1, 334), 74),
    "c3a": (band(CD, 3, 300, (900, 520)), 72),
    "c3b": (band(CD, 5, 340, (900, 700)), 72),
    "c3c": (tall(CD, 0, 334), 74),
}


def main() -> None:
    GEN.mkdir(parents=True, exist_ok=True)
    total = 0
    for name, (im, q) in PLAN.items():
        p = GEN / f"{name}.jpg"
        im.save(p, "JPEG", quality=q, optimize=True, progressive=True)
        total += p.stat().st_size
    print(f"{len(PLAN)} images -> assets/gen  ({total / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
