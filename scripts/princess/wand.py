"""A magic-wand trail that sweeps over the name."""

from anims import Anims

TRAIL = "M70 120 C200 40 380 40 520 100"
LENGTH = 520


def wand_trail(p: dict, an: Anims) -> str:
    frames = [(0.0, f"stroke-dashoffset:{LENGTH};opacity:0"), (0.6, f"stroke-dashoffset:{LENGTH};opacity:1"),
              (2.0, "stroke-dashoffset:0;opacity:1"), (3.2, "stroke-dashoffset:0;opacity:0")]
    return (f'<path {an.attr(frames, base="opacity:0;")} d="{TRAIL}" fill="none" stroke="{p["gold_hi"]}" '
            f'stroke-width="2.5" stroke-linecap="round" stroke-dasharray="{LENGTH}"/>')

