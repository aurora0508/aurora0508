"""Draw the banner: python3 scripts/princess

Writes assets/banner-light.svg, assets/banner-dark.svg and assets/divider.svg.
"""

from pathlib import Path

from card import render
from divider import divider
from palette import PALETTES

ASSETS = Path(__file__).resolve().parents[2] / "assets"

ASSETS.mkdir(exist_ok=True)
for theme, palette in PALETTES.items():
    (ASSETS / f"banner-{theme}.svg").write_text(render(palette), encoding="utf-8")
    print(f"wrote assets/banner-{theme}.svg")
(ASSETS / "divider.svg").write_text(divider(), encoding="utf-8")
print("wrote assets/divider.svg")
