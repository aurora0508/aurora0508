"""Draw the banner: python3 scripts/princess

Writes assets/banner-light.svg and assets/banner-dark.svg.
"""

from pathlib import Path

from card import render
from palette import PALETTES

ASSETS = Path(__file__).resolve().parents[2] / "assets"

ASSETS.mkdir(exist_ok=True)
for theme, palette in PALETTES.items():
    (ASSETS / f"banner-{theme}.svg").write_text(render(palette), encoding="utf-8")
    print(f"wrote assets/banner-{theme}.svg")
