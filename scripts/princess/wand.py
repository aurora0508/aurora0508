"""A magic-wand trail that sweeps over the name, led by a sparkle."""

from anims import Anims
from star import star

TRAIL = "M70 120 C200 40 380 40 520 100"
LENGTH = 520


def wand_trail(p: dict, an: Anims) -> str:
    frames = [(0.0, f"stroke-dashoffset:{LENGTH};opacity:0"), (0.6, f"stroke-dashoffset:{LENGTH};opacity:1"),
              (2.0, "stroke-dashoffset:0;opacity:1"), (3.2, "stroke-dashoffset:0;opacity:0")]
    return (f'<path {an.attr(frames, base="opacity:0;")} d="{TRAIL}" fill="none" stroke="{p["gold_hi"]}" '
            f'stroke-width="2.5" stroke-linecap="round" stroke-dasharray="{LENGTH}"/>')


def wand_tip(p: dict, an: Anims) -> str:
    frames = [(0.0, "opacity:0;transform:translate(0,0)"), (0.6, "opacity:1;transform:translate(0,0)"),
              (2.0, "opacity:1;transform:translate(450px,-20px)"), (2.6, "opacity:0;transform:translate(450px,-20px)")]
    return f'<g fill="{p["gold_hi"]}" {an.attr(frames, base="opacity:0;")}>{star(70, 120, 9)}</g>'
