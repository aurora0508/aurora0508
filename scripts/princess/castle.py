"""The castle: a crenellated keep with an arched gate, and five towers."""

from anims import Anims
from tower import tower

BASE = 300


def keep(p: dict) -> str:
    wall = f'fill="{p["castle"]}" stroke="{p["castle_edge"]}" stroke-width="1.5"'
    merlons = "".join(f'<rect x="{900 + i * 20}" y="{BASE - 102}" width="12" height="12" {wall}/>' for i in range(7))
    return (f'<rect x="900" y="{BASE - 92}" width="140" height="92" {wall}/>' + merlons
            + f'<path d="M952 {BASE} v-34 a18 18 0 0 1 36 0 v34 Z" fill="{p["castle_edge"]}"/>')


def castle(p: dict, an: Anims) -> str:
    towers = (tower(880, BASE, 34, 130, 44, p) + tower(1060, BASE, 34, 130, 44, p)
              + tower(970, BASE - 92, 40, 70, 56, p) + tower(830, BASE, 24, 80, 32, p) + tower(1110, BASE, 24, 80, 32, p))
    return keep(p) + towers
